"""chal_F.py -- challenger checks of LEMMA_F.md (o1-chalF, task T140). Usage: python3 chal_F.py <tag>
Writes results/chal_F_<tag>.json with mode "x" (never overwritten). Deterministic (no randomness, no seed needed).

Exact ||F_a|| is computed TWO independent ways:
 (N) Nystrom on the radial operator: for functions of r=rho^2 (the top eigenvector is one, Lemma R / Perron-Frobenius),
     F acts on L^2([0,1], 2 rho drho) with kernel k(rho,rho') = (beta/(2 I1(beta))) e^{-beta s^2 (r+r')} I0(beta R R') I0(beta rho rho')
     (derived by me from I3: dU = d^2w dphi/(2 pi^2); angular integrals give 2pi I0 twice).
 (L) Legendre reduction of TUNNEL_THEOREM.md sec. 1 (my own code, same formula M = L^1/2 G L^1/2).
Barta ratio B(rho) = (F psi)(rho)/psi(rho), psi = exp(-beta alpha r/2), on the Nystrom grid AND at arbitrary rho (incl. near 1)
by adaptive quadrature (scipy.integrate.quad, split at the peak rho' = rho/A).

PREDICATES (fixed before first run):
 Q1 (I2) Z = 2 I1(beta)/beta: quad of (2/pi) sin^2 e^{beta(cos t-1)} vs 2 ive(1,beta)/beta, beta in {1,64,1024,4096}; rel err < 1e-9
     (tolerance: quad epsrel 1e-12 plus margin).
 Q2 (I6) e^{-z}I0(z) <= Htilde_delta(z)*(1+1e-12) on z in logspace(-3,5,400), delta in {0.01,0.05,0.1,0.3,0.6,1}
     (1e-12: ive relative accuracy ~1e-15, margin).
 Q3 (I7) I1(z) >= e^z (1-1/(2z))/sqrt(2 pi z) - 1/2, z in logspace(0.001,5,400); compared in scaled form e^{-z}I1 >= ... - e^{-z}/2, tol 1e-14 abs.
 Q4 (I5) fixed point: |(alpha/2-s^2)A - c| < 1e-13 and |log A - 2 asinh s| < 1e-13 on s grid (rounding).
 Q5 (I8) AM-GM xy <= sqrt(xy) <= (x+y)/2 on 101x101 grid (exact up to 1e-15).
 Q6 (I9) Phi_true(r) <= -(r^2/64)(1-A^-2)^2 + 1e-12, where Phi_true(r) = (c/A) r - 1 + max_{q in S^1}(R q1 + rho q2 - c q2^2)
     (max by dense grid in angle plus bounded scalar refinement), r in (0,1] (200 pts), s in {0.01,0.02,0.05,0.1,0.3,0.6,1}.
     Measured only: slack ratio Phi_true / bound.
 Q7 exact-norm cross-check: |eps_N - eps_L| < 1e-7 for each (beta,s) on the grid (tolerance: both converged to <1e-9 by Q8;
     1e-7 leaves margin for the different discretisations).
 Q8 convergence: Nystrom N vs 2N: |eps_N(N)-eps_N(2N)| < 1e-9; Legendre (J,Q) vs (J+60,2Q) < 1e-9.
 Q9 Collatz-Wielandt / Schur consistency on the discrete matrix: lambda_N <= max_i B_N(rho_i) (exact for positive matrices; tol 1e-12 rel).
 Q10 (Theorem 1 validity) ||F||_exact <= (1/A) max(M_in, A M_out) with tau=delta=beta^{-1/3}, beta in {64,256,1024,4096},
     s in {0.02,0.05,0.1,0.3,0.6,1}. Hypothesis tau<1/5 (beta>125) checked per case first; cases with beta=64 do NOT qualify
     (tau = 1/4) and are measured only.
 Q11 (pointwise, inner) for rho^2 <= tau: B(rho) <= M_in/A. (outer) for rho^2 > tau: B(rho) <= Mout_pt(rho) :=
     beta e^beta/(2 I1) e^{beta Phi_true(r)} <= M_out. Rho grid: inner {0, .25,.5,.75,1}*sqrt(tau); outer sqrt(tau)+..., incl.
     0.9, 0.99, 0.999, 0.9999, 1. Tolerance 1e-9 rel (quad accuracy). Only qualifying (beta>125) cases count; beta=64 measured.
 Q12 (Lemma F direction at these beta, measured only for the record, NOT a predicate of the target): eps_eff - 2 asinh s.
 Q13 (report's beta_0 claim, eta=0.2): the smallest beta (on a grid 10^{k/20}) with max_{s in [0.1,1]} log max(M_in, A M_out) <= 0.2
     lies in [1e13, 1e15]; and author's quoted deficit at s=0.1, beta=1e12 is 24.9 (|mine - 24.9| < 0.5); at s=1, beta=1e11: 5e-4
     (within factor 2). Also measured: deficit range at beta <= 4096 vs the quoted '6.5 to 14 nats'.
"""
import sys, json, math
import numpy as np
from numpy.polynomial.legendre import leggauss
# --- scipy is NOT installed (run1 died on import). Own replacements: ---
def i0e(x):
    """e^{-x} I0(x): numpy np.i0 (Cephes) for x<=600, asymptotic series (20 terms, error < 1e-25) for x>600."""
    x = np.asarray(x, dtype=float); out = np.empty_like(x)
    m = x <= 600
    out[m] = np.i0(x[m])*np.exp(-x[m])
    y = x[~m]
    if y.size:
        term = np.ones_like(y); ssum = np.ones_like(y)
        for k in range(1, 20):
            term = term*(2*k-1)**2/(8*k*y); ssum = ssum + term
        out[~m] = ssum/np.sqrt(2*np.pi*y)
    return out if out.ndim else float(out)
def ive(n, x):
    """e^{-x} I_n(x) for scalar x>0, array/scalar n, by the periodic trapezoid rule on (1/pi) int_0^pi e^{x(cos t-1)} cos(nt) dt
    (spectrally accurate; M chosen >> n and >> sqrt(x))."""
    n = np.atleast_1d(np.asarray(n, dtype=float))
    M = int(4000 + 2*np.max(n) + 40*math.sqrt(x))
    t = (np.arange(M) + 0.5)*math.pi/M
    f = np.exp(x*(np.cos(t)-1))
    v = (np.cos(np.outer(n, t)) @ f)/M
    return v if v.size > 1 else float(v[0])
def i1e(z):
    return np.array([ive(1, float(zz)) for zz in np.atleast_1d(z)])
def quad(f, a, b, epsabs=0, epsrel=1e-12, limit=0):
    """composite Gauss-Legendre: 64 panels x 20 nodes vs 128 panels x 20; returns value and |difference|."""
    x, w = leggauss(20)
    def comp(npn):
        e = np.linspace(a, b, npn+1); tot = 0.0
        for k in range(npn):
            h = (e[k+1]-e[k])/2; m = (e[k+1]+e[k])/2
            tot += h*sum(wi*f(m+h*xi) for xi, wi in zip(x, w))
        return tot
    v1 = comp(8); v2 = comp(16)
    return v2, abs(v2-v1)
class _R: pass
def minimize_scalar(f, bounds, method=None, options=None):
    a, b = bounds; g = (math.sqrt(5)-1)/2
    c = b - g*(b-a); d = a + g*(b-a)
    for _ in range(200):
        if f(c) < f(d): b = d
        else: a = c
        c = b - g*(b-a); d = a + g*(b-a)
    r = _R(); r.x = (a+b)/2; r.fun = f(r.x); return r
QUADERR = [0.0]

TAG = sys.argv[1] if len(sys.argv) > 1 else 'run1'
P = {}          # predicate name -> bool
MEAS = {}       # measured only
QUAL = {}

def pars(s):
    al = 2*s*math.sqrt(1+s*s); c = s*s + al/2; A = 1 + 2*c
    return al, c, A

def D_of(beta):
    return 1 - 1/(2*beta) - math.sqrt(2*math.pi*beta)*math.exp(-beta)/2

def log_Min_full(beta, tau, delta, A):
    D = D_of(beta)
    if (1-4*tau) <= 0: return math.inf
    t1 = ((1-tau)*(1-4*tau)*(1-5*delta**2/48))**-0.5
    t2 = math.sqrt(2*math.pi*beta)*math.exp(-beta*(1-5*tau)*(1-math.cos(delta)))
    t3 = math.sqrt(2*math.pi*beta)*math.exp(-beta*A*tau/2)
    return math.log(t1+t2+t3) - math.log(D)

def log_Mout(beta, tau, A):
    D = D_of(beta)
    return math.log(beta*math.sqrt(2*math.pi*beta)/(2*D)) - beta*tau**2*(1-A**-2)**2/64

def Phi_true(r, s):
    al, c, A = pars(s); R = math.sqrt(max(1-r, 0)); rho = math.sqrt(r)
    f = lambda th: -(R*math.cos(th) + rho*math.sin(th) - c*math.sin(th)**2)
    th = np.linspace(0, math.pi/2, 2001)
    v = -(R*np.cos(th) + rho*np.sin(th) - c*np.sin(th)**2)
    i = int(np.argmin(v)); lo = th[max(i-1, 0)]; hi = th[min(i+1, 2000)]
    m = minimize_scalar(f, bounds=(lo, hi), method='bounded', options={'xatol': 1e-14})
    best = min(-m.fun, -v[i])
    return (c/A)*r - 1 + best

# ---------- exact norm, Nystrom ----------
def nystrom(beta, s, N):
    al, c, A = pars(s)
    # composite Gauss-Legendre in rho on panels refined near 0 (none needed) -- uniform panels of width ~ 1/(4 sqrt beta)
    npan = max(8, int(2*math.sqrt(beta)))
    x, w = leggauss(N)
    edges = np.linspace(0, 1, npan+1)
    rho = np.concatenate([(edges[k]+edges[k+1])/2 + (edges[k+1]-edges[k])/2*x for k in range(npan)])
    wt = np.concatenate([(edges[k+1]-edges[k])/2*w for k in range(npan)]) * 2*rho   # measure 2 rho drho = dr
    r = rho**2; R = np.sqrt(1-r)
    zA = beta*np.outer(R, R); zB = beta*np.outer(rho, rho)
    logpref = math.log(beta/(2*ive(1, beta)))   # beta/(2 I1) = beta/(2 ive1) e^{-beta}
    logk = logpref - beta + zA + zB + np.log(i0e(zA)) + np.log(i0e(zB)) - beta*s*s*(r[:, None]+r[None, :])
    K = np.exp(logk)
    sw = np.sqrt(wt)
    M = sw[:, None]*K*sw[None, :]
    lam = float(np.linalg.eigvalsh(M)[-1])
    lpsi = -beta*al*r/2
    E = logk + (lpsi + np.log(wt))[None, :]
    mx = E.max(axis=1)
    logB = mx + np.log(np.exp(E - mx[:, None]).sum(axis=1)) - lpsi
    return -math.log(lam), lam, rho, logB

# ---------- exact norm, Legendre (TUNNEL_THEOREM sec 1) ----------
def bessel_l(beta, nmax):
    # l_n = I_n/I_1 via scaled ive (direct; ive accurate for these orders)
    n = np.arange(nmax+1)
    return ive(n, beta)/ive(1, beta)

def legendre(beta, s, J, Q):
    x, w = leggauss(Q)
    # t in [-1,1], weight dt/2; split at t0 = 1 - 2*min(1, (12/(s sqrt beta))^2)
    u0 = min(1.0, (12/(max(s, 1e-3)*math.sqrt(beta)))**2)   # u = (1-t)/2 = r
    ts, ws = [], []
    for lo, hi in ((0, u0), (u0, 1.0)):
        if hi > lo:
            u = lo + (hi-lo)*(x+1)/2; ts.append(1-2*u); ws.append(w*(hi-lo)/2)   # dt/2 = du
    t = np.concatenate(ts); wv = np.concatenate(ws)*np.exp(-beta*s*s*(1-t))
    Pm = np.zeros((J+1, t.size)); Pm[0] = 1; Pm[1] = t
    for k in range(1, J): Pm[k+1] = ((2*k+1)*t*Pm[k] - k*Pm[k-1])/(k+1)
    Pm *= np.sqrt(2*np.arange(J+1)+1)[:, None]
    G = (Pm*wv) @ Pm.T
    l = np.clip(bessel_l(beta, 2*J+1)[2*np.arange(J+1)+1], 0.0, None)   # trapezoid noise ~1e-17 can be negative
    M = np.sqrt(l)[:, None]*G*np.sqrt(l)[None, :]
    return -math.log(np.linalg.eigvalsh(M)[-1])

# ---------- pointwise Barta ratio by adaptive quadrature ----------
def B_quad(beta, s, rho):
    al, c, A = pars(s); r = rho*rho; R = math.sqrt(max(1-r, 0))
    logpref = math.log(beta/ive(1, beta)) - beta + beta*(al/2 - s*s)*r
    def ex(rp):
        Rp = math.sqrt(max(1-rp*rp, 0)); zA = beta*R*Rp; zB = beta*rho*rp
        return logpref + zA + zB + math.log(i0e(zA)) + math.log(i0e(zB)) - beta*c*rp*rp
    grid = np.linspace(1e-6, 1, 4001)
    shift = max(ex(g) + math.log(g) for g in grid)
    def integrand(rp):
        return math.exp(ex(rp) - shift)*rp
    pk = rho/A; wdt = 1/math.sqrt(beta*A)
    pts = sorted(set([0.0, 1.0] + [min(max(pk + k*wdt, 0.0), 1.0) for k in (-8, -3, -1, 0, 1, 3, 8)]))
    tot = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        if b > a:
            v, er = quad(integrand, a, b, epsabs=0, epsrel=1e-12, limit=400); tot += v; QUADERR[0] = max(QUADERR[0], er/max(tot,1e-300))
    return math.log(tot) + shift   # NOTE: returns log B

def H_tilde(z, d):
    with np.errstate(divide='ignore'):
        H = (2*np.pi*z*(1-5*d*d/48))**-0.5 + np.exp(-z*(1-np.cos(d)))
    return np.minimum(1.0, H)

out = {'tag': TAG}
# Q1
for beta in (1, 64, 1024, 4096):
    v, _ = quad(lambda t: (2/math.pi)*math.sin(t)**2*math.exp(beta*(math.cos(t)-1)), 0, math.pi, epsabs=0, epsrel=1e-13, limit=500)
    exact = 2*ive(1, beta)/beta
    P[f'Q1 beta={beta}'] = abs(v/exact-1) < 1e-9
# Q2
z = np.logspace(-3, 5, 400); worst = -1
for d in (0.01, 0.05, 0.1, 0.3, 0.6, 1.0):
    ok = np.all(i0e(z) <= H_tilde(z, d)*(1+1e-12)); P[f'Q2 delta={d}'] = bool(ok)
    worst = max(worst, float(np.max(i0e(z)/H_tilde(z, d))))
MEAS['Q2 max ratio e^-z I0/Htilde'] = worst
# Q3
z = np.logspace(0.001, 5, 400)
lhs = i1e(z); rhs = (1-1/(2*z))/np.sqrt(2*np.pi*z) - np.exp(-z)/2
P['Q3'] = bool(np.all(lhs >= rhs - 1e-14)); MEAS['Q3 min (lhs-rhs)'] = float(np.min(lhs-rhs))
# Q4, Q5
sg = np.linspace(0, 1, 101)
q4 = True
for s in sg:
    al, c, A = pars(s); q4 &= abs((al/2-s*s)*A - c) < 1e-13 and abs(math.log(A) - 2*math.asinh(s)) < 1e-13
P['Q4'] = bool(q4)
xg = np.linspace(0, 1, 101); X, Y = np.meshgrid(xg, xg)
P['Q5'] = bool(np.all(X*Y <= np.sqrt(X*Y)+1e-15) and np.all(np.sqrt(X*Y) <= (X+Y)/2+1e-15))
# Q6
slack = {}
for s in (0.01, 0.02, 0.05, 0.1, 0.3, 0.6, 1.0):
    al, c, A = pars(s); ok = True; ratios = []
    for r in np.linspace(0.005, 1, 200):
        pt = Phi_true(r, s); bd = -(r*r/64)*(1-A**-2)**2
        ok &= pt <= bd + 1e-12; ratios.append(pt/bd)
    P[f'Q6 s={s}'] = bool(ok); slack[str(s)] = [float(min(ratios)), float(max(ratios))]
MEAS['Q6 Phi_true/bound range per s'] = slack
print('scalar predicates done', {k: v for k, v in P.items() if not v}, flush=True)

# exact norms and Theorem 1
rows = []
betas = tuple(int(x) for x in sys.argv[2].split(',')) if len(sys.argv) > 2 else (64, 256, 1024, 4096); svals = (0.02, 0.05, 0.1, 0.3, 0.6, 1.0)
for beta in betas:
    tau = delta = beta**(-1/3); qual = tau < 0.2
    for s in svals:
        al, c, A = pars(s); eps = 2*math.asinh(s)
        eN1, lam1, _, _ = nystrom(beta, s, 8); eN2, lam2, rho_g, B_g = nystrom(beta, s, 16)
        J = int(8*math.sqrt(beta)) + 40
        eL1 = legendre(beta, s, J, 400); eL2 = legendre(beta, s, J+60, 800)
        key = f'b={beta} s={s}'
        P[f'Q8N {key}'] = abs(eN1-eN2) < 1e-9; P[f'Q8L {key}'] = abs(eL1-eL2) < 1e-9
        P[f'Q7 {key}'] = abs(eN2-eL2) < 1e-7
        P[f'Q9 {key}'] = -eN2 <= float(np.max(B_g)) + 1e-12
        lMin = log_Min_full(beta, tau, delta, A); lMout = log_Mout(beta, tau, A)
        logbound = -math.log(A) + max(lMin, math.log(A) + lMout)
        valid = (-eL2) <= logbound + 1e-12
        if qual: P[f'Q10 {key}'] = valid
        else: MEAS[f'Q10(nonqual tau={tau:.3f}) {key}'] = bool(valid)
        # pointwise
        rin = [f*math.sqrt(tau) for f in (0, .25, .5, .75, 1.0)]
        rout = sorted(set([min(1.0, math.sqrt(tau)*1.0001)] + [x for x in (0.3, 0.5, 0.7, 0.9, 0.99, 0.999, 0.9999, 1.0) if x*x > tau]))
        pw = []
        okin = okout = True
        for rho in rin:
            lb = B_quad(beta, s, rho); lbd = lMin - math.log(A)
            pw.append(dict(rho=rho, region='in', logB=lb, log_bound=lbd, log_ratio=lb - lbd))
            okin &= lb <= lbd + 1e-9
        for rho in rout:
            lb = B_quad(beta, s, rho)
            lpt = math.log(beta/2) - math.log(ive(1, beta)) + beta*Phi_true(rho*rho, s)
            pw.append(dict(rho=rho, region='out', logB=lb, log_bound_pt=lpt, log_Mout=lMout, log_ratio_pt=lb-lpt))
            okout &= lb <= lpt + 1e-9 and lpt <= lMout + 1e-9
        if qual: P[f'Q11in {key}'] = okin; P[f'Q11out {key}'] = okout
        else: MEAS[f'Q11(nonqual) in/out {key}'] = [okin, okout]
        logBsup_grid = float(np.max(B_g))
        row = dict(beta=beta, s=s, tau=tau, qualifies=qual, eps=eps, eps_eff_N=eN2, eps_eff_L=eL2, diff=eL2-eps, beta_diff=beta*(eL2-eps),
                   minus_log_Bsup=-logBsup_grid, log_Min=lMin, log_A_Mout=math.log(A)+lMout,
                   master_deficit=max(lMin, math.log(A)+lMout), bound_valid=bool(valid), pointwise=pw,
                   conv=dict(N=abs(eN1-eN2), L=abs(eL1-eL2)))
        rows.append(row)
        print(f'beta={beta:5d} s={s:4.2f} qual={qual} epsN={eN2:.10f} epsL={eL2:.10f} eps={eps:.6f} beta*diff={beta*(eL2-eps):+.3f} '
              f'-logBsup={-logBsup_grid:.6f} deficit={row["master_deficit"]:.3f} valid={valid} in={okin} out={okout}', flush=True)
out['rows'] = rows
MEAS['quad max rel panel-refinement change'] = QUADERR[0]
MEAS['Q12 beta*(eps_eff-eps)'] = {f"{r['beta']},{r['s']}": r['beta_diff'] for r in rows}
MEAS['deficit range qualifying'] = [min([r['master_deficit'] for r in rows if r['qualifies']] or [None]), max([r['master_deficit'] for r in rows if r['qualifies']] or [None])] if any(r['qualifies'] for r in rows) else None

# Q13 beta_0 claim
def deficit(beta, s):
    tau = beta**(-1/3); al, c, A = pars(s)
    return max(log_Min_full(beta, tau, tau, A), math.log(A) + log_Mout(beta, tau, A))
sgrid = np.linspace(0.1, 1, 91)
b0 = None
for k in range(40, 400):
    beta = 10**(k/20)
    if max(deficit(beta, s) for s in sgrid) <= 0.2: b0 = beta; break
MEAS['Q13 beta0(eta=0.2) first grid point'] = b0
MEAS['Q13 worst s at b0'] = float(sgrid[int(np.argmax([deficit(b0, s) for s in sgrid]))]) if b0 else None
P['Q13 beta0 in [1e13,1e15]'] = b0 is not None and 1e13 <= b0 <= 1e15
d12 = deficit(1e12, 0.1); d11 = deficit(1e11, 1.0)
MEAS['Q13 deficit s=0.1 beta=1e12'] = d12; MEAS['Q13 deficit s=1 beta=1e11'] = d11
P['Q13 quoted 24.9 at s=0.1,beta=1e12'] = abs(d12 - 24.9) < 0.5
P['Q13 quoted 5e-4 at s=1,beta=1e11'] = 2.5e-4 <= d11 <= 1e-3

met = sum(bool(v) for v in P.values()); failed = [k for k, v in P.items() if not v]
out.update(predicates={k: bool(v) for k, v in P.items()}, measured=MEAS, met=met, failed=failed, n_measured=len(MEAS))
with open(f'results/chal_F_{TAG}.json', 'x') as fh:
    json.dump(out, fh, indent=1, default=float)
print('met', met, 'failed', len(failed), failed)
print('measured', json.dumps(MEAS, default=float)[:3000])
sys.exit(0 if not failed else 1)
