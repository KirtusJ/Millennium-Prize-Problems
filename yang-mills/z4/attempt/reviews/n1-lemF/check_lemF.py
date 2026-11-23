"""check_lemF.py  [sup over rho: 51-pt grid on [0,1] + 21-pt refinement around the max] -- numerical checks for LEMMA_F.md (worker n1-lemF, T134). numpy only (no scipy on this machine).

Objects (definitions as in LEMMA_F.md):
  A = 1 + 2 s^2 + alpha, alpha = 2 s sqrt(1+s^2), c = s^2 + alpha/2;  log A = 2 asinh(s).
  Barta ratio of psi = exp(-beta alpha rho^2/2), reduced to one integral (angles integrated exactly):
    B(rho) = (beta/I1e(beta)) int_0^1 r' I0e(beta R R') I0e(beta rho r') exp(beta[(alpha/2-s^2)rho^2 + R R' + rho r' - c r'^2 - 1]) dr',
    R = sqrt(1-rho^2), R' = sqrt(1-r'^2).
  Master bound (LEMMA_F.md, Theorem 1):  ||F|| <= (1/A) max(M_in, A M_out), with tau, delta parameters.

PREDICATES (fixed before the first run):
 Q1 (Z identity, exact) for beta in {1,64,1024}: (2/pi) int e^{beta cos} sin^2 == 2 I_1(beta)/beta, rel. tol 1e-10
     (both by 4000-node Gauss-Legendre; tolerance = quadrature accuracy, far below any effect used).
 Q2 (I0 envelope, Lemma B1) for all z on a log grid [1e-3, 1e6] (300 pts) and delta in {0.05,0.2,0.5,1}:
     I0e(z) <= min(1, Hdelta(z)) with Hdelta(z) = 1/sqrt(2 pi z (1-5 delta^2/48)) + exp(-z(1-cos delta)).  tol 1e-12 relative (rounding).
     Also: Hdelta decreasing in z on the grid (exact claim).
 Q3 (I1 lower bound, Lemma B2) for all z on the grid: I1e(z) >= (1-1/(2z))/sqrt(2 pi z) - exp(-z)/2, tol 1e-12 rel.
 Q4 (outer bound, Lemma D) for s in a grid of 50 values in (0,1], r = rho^2 in 200 values of (0,1]:
     Phi(r) := (c/A) r - 1 + max_u [cos(u-v) - c sin^2 u] (v = asin(rho), max over 20001-pt u grid + local refine)
     <= -(r^2/64)(1-1/A^2)^2 + 1e-12 (rounding).  Also flat identity alpha/2 - s^2 == c/A to 1e-14.
 Q5 (Schur consistency, exact logic) for beta in {64,256,1024,4096}, s in {0.01,0.03,0.1,0.3,0.6,1}:
     -log Bsup <= eps_eff(target eps_eff.py) + 1e-7 (Barta gives an upper bound on ||F||; tolerance = quadrature/convergence ~1e-9 of both programs, x100).
     (beta=4096 eps_eff is computed with J = 8 sqrt(beta)+40, Q=400 as in eps_eff.py.)
 Q6 (master bound is a bound) same cases, tau = delta = beta^(-1/3): Bsup <= (1/A) max(M_in, A M_out) (exact claim; tol 1e-9 rel).
 Q7 (my expectation, not a claim of the lemma): -log Bsup >= 2 asinh(s) - 3/beta for s >= 0.1 (Barta with the flat Gaussian is
     nearly sharp). 3 is my guess from eps_eff deficits 0.65-0.98/beta.
 Measured only: Bsup, argmax rho, -log Bsup - 2asinh(s), eps_eff - 2asinh(s), master-bound deficit log max(M_in, A M_out)
     for those cases and for beta up to 1e12.
 Q8 convergence: Bsup with doubled quadrature changes by < 1e-9 relative (tolerance: double rounding x quadrature size).
No randomness.
CHANGE AFTER run1 (run1 kept, exit 1): run1 crashed in master() at beta=64 because tau=beta^(-1/3)=1/4 violates the
 theorem's hypothesis tau < 1/5 (defect of MY program, not of the target). From run2 on, Q6 uses tau = min(beta^(-1/3), 0.15).
"""
import numpy as np, sys, json, math
from numpy.polynomial.legendre import leggauss
sys.path.insert(0, '.')
import eps_eff as EE

def gl(a, b, n):
    x, w = leggauss(n); return a + (b - a) * (x + 1) / 2, w * (b - a) / 2

def bessel_e(z, nu, n=200):
    """e^{-z} I_nu(z) = (1/pi) int_0^pi e^{z(cos t-1)} cos(nu t) dt, nu in {0,1}; Gauss-Legendre on [0,t1],[t1,pi]."""
    z = np.atleast_1d(np.asarray(z, float)); out = np.empty_like(z)
    for i, zz in enumerate(z):
        t1 = min(np.pi, 30.0 / math.sqrt(max(zz, 1e-300)))
        tot = 0.0
        for a, b in ((0, t1), (t1, np.pi)):
            if b > a:
                t, w = gl(a, b, n); tot += np.sum(w * np.exp(zz * (np.cos(t) - 1)) * np.cos(nu * t))
        out[i] = tot / np.pi
    return out

def i0e_vec(x):
    """vectorised e^{-x} I0(x): power series (120 terms) for x<=40, asymptotic series (12 terms) above (rel. error < 1e-14 both)."""
    x = np.asarray(x, float); out = np.empty_like(x)
    m = x <= 40
    y = x[m]
    if y.size:
        q = (y / 2) ** 2; term = np.ones_like(y); s = np.ones_like(y)
        for k in range(1, 120):
            term = term * q / (k * k); s = s + term
        out[m] = s * np.exp(-y)
    y = x[~m]
    if y.size:
        s = np.ones_like(y); term = np.ones_like(y)
        for k in range(1, 13):
            term = term * (2 * k - 1) ** 2 / (8 * k * y); s = s + term
        out[~m] = s / np.sqrt(2 * np.pi * y)
    return out

_I1E = {}
def i1e_cached(beta):
    if beta not in _I1E: _I1E[beta] = bessel_e(beta, 1, 400)[0]
    return _I1E[beta]

def params(s):
    al = 2 * s * math.sqrt(1 + s * s); A = 1 + 2 * s * s + al; c = s * s + al / 2
    return al, A, c

def barta(beta, s, rho, nsub=400, nq=24):
    al, A, c = params(s)
    I1e = i1e_cached(beta)
    R = math.sqrt(max(1 - rho * rho, 0.0))
    xs, ws = [], []
    edges = np.linspace(0, 1, nsub + 1)
    for a, b in zip(edges[:-1], edges[1:]):
        x, w = gl(a, b, nq); xs.append(x); ws.append(w)
    rp = np.concatenate(xs); w = np.concatenate(ws)
    Rp = np.sqrt(np.clip(1 - rp * rp, 0, None))
    ex = beta * ((al / 2 - s * s) * rho * rho + R * Rp + rho * rp - c * rp * rp - 1)
    f = rp * i0e_vec(beta * R * Rp) * i0e_vec(beta * rho * rp) * np.exp(ex)
    return beta / I1e * np.sum(w * f)

def barta_sup(beta, s, nsub=400, nq=24):
    rhos = np.linspace(0, 1, 51)
    vals = np.array([barta(beta, s, r, nsub, nq) for r in rhos])
    k = int(np.argmax(vals)); lo = rhos[max(k - 1, 0)]; hi = rhos[min(k + 1, 50)]
    fine = np.linspace(lo, hi, 21)
    fv = np.array([barta(beta, s, r, nsub, nq) for r in fine])
    j = int(np.argmax(fv))
    return max(fv[j], vals[k]), fine[j] if fv[j] >= vals[k] else rhos[k]

def Hdel(z, d):
    return 1 / np.sqrt(2 * np.pi * z * (1 - 5 * d * d / 48)) + np.exp(-z * (1 - np.cos(d)))

def master(beta, s, tau, delta):
    """returns log max(M_in, A M_out) using the PROVED lower bound on I1 (D) -- everything in logs to allow huge beta."""
    al, A, c = params(s)
    D = 1 - 1 / (2 * beta) - math.sqrt(2 * math.pi * beta) * math.exp(-min(beta, 700)) / 2
    k = 1 - 5 * delta ** 2 / 48
    sq = math.sqrt(2 * math.pi * beta)
    Min = (((1 - tau) * (1 - 4 * tau) * k) ** -0.5 + sq * math.exp(-beta * (1 - 5 * tau) * (1 - math.cos(delta)))
           + sq * math.exp(-beta * A * tau / 2)) / D
    logAMout = math.log(A) + math.log(beta * sq / (2 * D)) - beta * tau ** 2 * (1 - 1 / A ** 2) ** 2 / 64
    return max(math.log(Min), logAMout), math.log(Min), logAMout

if __name__ == '__main__':
    tag = sys.argv[1] if len(sys.argv) > 1 else 'run1'
    P = {}; meas = {}
    # Q1
    for beta in (1, 64, 1024):
        th, w = gl(0, np.pi, 4000)
        lhs = (2 / np.pi) * np.sum(w * np.exp(beta * (np.cos(th) - 1)) * np.sin(th) ** 2)  # scaled by e^{-beta}
        rhs = 2 * bessel_e(beta, 1, 2000)[0] / beta
        P[f'Q1 b={beta}'] = abs(lhs / rhs - 1) < 1e-10
        print('Q1', beta, lhs, rhs, flush=True)
    # Q2, Q3
    zg = np.logspace(-3, 6, 300)
    I0g = bessel_e(zg, 0, 400); I1g = bessel_e(zg, 1, 400)
    for d in (0.05, 0.2, 0.5, 1.0):
        H = np.minimum(1, Hdel(zg, d))
        P[f'Q2 env d={d}'] = bool(np.all(I0g <= H * (1 + 1e-12)))
        P[f'Q2 decr d={d}'] = bool(np.all(np.diff(Hdel(zg, d)) < 0))
        print('Q2', d, 'min slack ratio', float(np.min(H / I0g)), flush=True)
    low = (1 - 1 / (2 * zg)) / np.sqrt(2 * np.pi * zg) - np.exp(-zg) / 2
    P['Q3'] = bool(np.all(I1g >= low - 1e-12 * np.abs(low)))
    print('Q3 min(I1e - low)', float(np.min(I1g - low)), flush=True)
    # Q4
    ug = np.linspace(-np.pi / 2, np.pi / 2, 20001)
    worst = -1e9; okid = True
    for s in np.linspace(0.02, 1, 50):
        al, A, c = params(s)
        okid &= abs(al / 2 - s * s - c / A) < 1e-14
        for r in np.linspace(0.005, 1, 200):
            v = math.asin(math.sqrt(r))
            g = np.cos(ug - v) - c * np.sin(ug) ** 2
            k = int(np.argmax(g)); uu = np.linspace(ug[max(k - 1, 0)], ug[min(k + 1, 20000)], 2001)
            mx = max(g[k], float(np.max(np.cos(uu - v) - c * np.sin(uu) ** 2)))
            Phi = (c / A) * r - 1 + mx
            bnd = -(r * r / 64) * (1 - 1 / A ** 2) ** 2
            worst = max(worst, Phi - bnd)
    P['Q4 flat identity'] = bool(okid); P['Q4 Phi bound'] = worst <= 1e-12
    meas['Q4 max(Phi - bound)'] = worst
    print('Q4 worst Phi-bound', worst, flush=True)
    # Q5-Q8
    rows = []
    for beta in (64, 256, 1024, 4096):
        J = int(8 * np.sqrt(beta)) + 40
        for s in (0.01, 0.03, 0.1, 0.3, 0.6, 1.0):
            al, A, c = params(s)
            B, rho_star = barta_sup(beta, s)
            B2 = barta(beta, s, rho_star, 800, 48)
            Bc = barta(beta, s, rho_star)
            ee = EE.eps_eff(beta, math.asin(s), J, 400)
            tau = min(beta ** (-1 / 3), 0.15); delta = beta ** (-1 / 3)
            mb, lmin, lout = master(beta, s, tau, delta)
            eps = 2 * math.asinh(s)
            P[f'Q5 b={beta} s={s}'] = -math.log(B) <= ee + 1e-7
            P[f'Q6 b={beta} s={s}'] = B <= math.exp(mb) / A * (1 + 1e-9)
            if s >= 0.1:
                P[f'Q7 b={beta} s={s}'] = -math.log(B) >= eps - 3 / beta
            P[f'Q8 b={beta} s={s}'] = abs(B2 / Bc - 1) < 1e-9
            row = dict(beta=beta, s=s, Bsup=B, rho_star=rho_star, mlogB=-math.log(B), eps=eps, barta_minus_eps=-math.log(B) - eps,
                       beta_times=beta * (-math.log(B) - eps), eps_eff=ee, epseff_minus_eps=ee - eps, master_deficit=mb,
                       logMin=lmin, logAMout=lout, conv=abs(B2 / Bc - 1))
            rows.append(row)
            print(' '.join(f'{k}={v:.6g}' for k, v in row.items()), flush=True)
    big = []
    for lb in range(2, 13):
        beta = 10.0 ** lb
        for s in (0.1, 0.3, 1.0):
            mb = master(beta, s, beta ** (-1 / 3), beta ** (-1 / 3))[0]
            big.append(dict(beta=beta, s=s, master_deficit=mb))
    meas['master deficit, tau=delta=beta^-1/3'] = big
    for b in big: print('master', b, flush=True)
    met = sum(bool(v) for v in P.values()); failed = [k for k, v in P.items() if not v]
    out = dict(predicates={k: bool(v) for k, v in P.items()}, met=met, failed=failed, rows=rows, measured=meas)
    with open(f'results/check_lemF_{tag}.json', 'x') as fh: json.dump(out, fh, indent=1, default=float)
    print('met', met, 'failed', len(failed), failed)
    sys.exit(0 if not failed else 1)
