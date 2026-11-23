"""prog2b_weight_schur.py (= prog2 with log-space Lemma K comparison after OWN overflow defect; predicates unchanged) -- referee tests of Lemma tu:U-W13, Lemma tu:U-weight, Lemma tu:U-K, Lemma tu:U-schur,
Lemma tu:U-kernel and the fibre reduction (quaternion Monte Carlo).

Predicates (fixed before first run; tolerances in brackets with their source):
 W  (Lemma W13 + weight), for eta in {0.5,0.2,0.05}, tau in {0.5,0.1,0.02}, delta=0.1, grid of 400001 points in [0,pi/2]:
   W1 rho<=(eps-eta)_+ ; rho=0 where eps<=1.5 eta ; rho>=eps-2eta where eps>=3eta      [1e-14 abs: rounding]
   W2 max|g_eta'| <= 3/sqrt(2 eta)   (analytic derivative formula of the proof, sampled) [exact]
   W3 0<=ft'<=f' ; f - L tau/2 <= ft <= f (cumulative trapezoid)                          [1e-9 abs: trapezoid error]
   W4 sup|ft''| <= 6/sqrt(eta)+3L/tau ; sup|ft' cot a| <= L/sinh(3eta/4)                    [exact, analytic derivs]
   W5 c^rho >= c* - pi sqrt(6 eta) and c^rho <= c*_eta <= c*                                [1e-9: quadrature]
   W6 off I: Phi'^2/2 <= (1-delta)^2 (eps-eta)                                              [1e-14]
   W7 Lemma weight(4): Phi(ax)+Phi(ay) >= (1-delta)(c^rho - 2L tau - L(ay-ax)) on 200x200 pairs ax<pi/2<ay [1e-9]
 K  Lemma K, first bound: LHS(beta,|p|,H,eta) <= RHS, on grid beta in {200,1000,4096,16384}, |p| in {0,.5,1,L},
    H in {0,1,5,18}, eta in {beta^-1/8, 0.5, 1}; only cases with beta'>0 qualify (count reported).
    LHS by 1-D quadrature: angular average of cosh(sqrt(b) p.X) over directions is sinh(y)/y, y=sqrt(b)|p|theta.
    [relative 1e-8: GL quadrature, checked by doubling]
 KR Lemma K radial bound: same, L in {0.5, L, 3}.
 S  Lemma Schur: for (eta,tau,delta)=(0.5,0.5,0.1), beta in {4096,16384}, a1 on 120-pt grid in (0,pi):
    log w(a1) <= Phi'(a1)^2/2 + omega(beta), omega from Remark tu:U-K-rem with P=L, H0 = H (actual sup computed
    on grid) -- the hypothesis beta(1-5/48 b^-1/4) - sqrt(b) H > 0 is checked per beta.
    w by 2-D Gauss quadrature in (theta, z=cos angle) [tolerance: doubling change must be <1e-8 rel].
 MC quaternion Monte Carlo, seed 20261123, N=2,000,000 Haar points (normalised Gaussian 4-vectors), beta=3:
    MC1 Z = E[e^{b x0}] equals 2 I1(b)/b ; MC2 (1/(n+1)) E[k chi_n] equals I_{n+1}/I_1, n=0..4 ;
    MC3 P(r<=0.3) = 0.3 (r = x1^2+x2^2 uniform, eq. tu:U-eq-haar) ; MC4 P(theta<=1) = (2/pi)(1/2 - sin2/4) (eq. tu:U-eq-exp)
    [|est - exact| <= 4 standard errors]
    MC5 fibre reduction: after conjugating by h with h u1 h^-1 = s e3, |u1 x u2|^2 = s^2 (x1^2+x2^2) [1e-12 abs]
    MC6 <U,U'> = (1/2) Tr(U^{-1}U') with 2x2 matrices; V gauge invariant [1e-12 abs]
Result file opened with mode 'x'.
"""
import numpy as np, math, sys
out = open(sys.argv[1], 'x')
def P(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.write(s + '\n'); out.flush()
cnt = {}
def rec(name, ok, nq=False):
    c = cnt.setdefault(name, [0, 0, 0])
    if nq: c[2] += 1
    else: c[0 if ok else 1] += 1

L = math.sqrt(4 * math.asinh(1))
def epsf(a): return 2 * np.arcsinh(np.sin(a))
def Sm(x): x = np.clip(x, 0, 1); return 3 * x * x - 2 * x ** 3
def dSm(x): xc = np.clip(x, 0, 1); return np.where((x > 0) & (x < 1), 6 * xc * (1 - xc), 0.0)
def g_eta(e, eta):
    t = (e - eta) / eta; return np.sqrt(np.clip(e - eta, 0, None)) * Sm(2 / 3 * (t - 0.5))
def dg_eta(e, eta):
    t = (e - eta) / eta; ok = t > 0.5; em = np.where(ok, e - eta, 1.0)
    psi = Sm(2 / 3 * (t - 0.5)); dpsi = 2 / 3 * dSm(2 / 3 * (t - 0.5))
    return np.where(ok, psi / (2 * np.sqrt(em)) + np.sqrt(em) / eta * dpsi, 0.0)

# c* reference
xg, wg = np.polynomial.legendre.leggauss(400)
v = (xg + 1) / 2; wv = wg / 2
cstar = 2 * np.sum(wv * np.sqrt(4 * np.arcsinh(np.sin(np.pi / 2 * v * v))) * np.pi * v)
P('c* =', repr(cstar))

def build(eta, tau, delta, n=400001):
    a = np.linspace(0, np.pi / 2, n)
    e = epsf(a)
    p = math.sqrt(2) * g_eta(e, eta)
    de = 2 * np.cos(a) / np.sqrt(1 + np.sin(a) ** 2)
    dp = math.sqrt(2) * dg_eta(e, eta) * de
    chi = Sm((np.pi / 2 - a) / (tau / 2)); dchi = -(2 / tau) * dSm((np.pi / 2 - a) / (tau / 2))
    ftp = p * chi; ftpp = dp * chi + p * dchi
    h = a[1] - a[0]
    f = np.concatenate([[0], np.cumsum((p[1:] + p[:-1]) / 2 * h)])
    ft = np.concatenate([[0], np.cumsum((ftp[1:] + ftp[:-1]) / 2 * h)])
    return dict(a=a, e=e, p=p, dp=dp, ftp=ftp, ftpp=ftpp, f=f, ft=ft, chi=chi)

for eta in (0.5, 0.2, 0.05):
    for tau in (0.5, 0.1, 0.02):
        delta = 0.1
        B = build(eta, tau, delta); a, e = B['a'], B['e']
        rho = g_eta(e, eta) ** 2
        ok1 = np.all(rho <= np.clip(e - eta, 0, None) + 1e-14) and np.all(rho[e <= 1.5 * eta] <= 1e-14) and \
              np.all(rho[e >= 3 * eta] >= e[e >= 3 * eta] - 2 * eta - 1e-14)
        rec('W1', ok1)
        es = np.linspace(0, 3, 300001); gmax = np.max(np.abs(dg_eta(es, eta)))
        ok2 = gmax <= 3 / math.sqrt(2 * eta); rec('W2', ok2)
        ok3 = np.all(B['ftp'] >= 0) and np.all(B['ftp'] <= B['p'] + 1e-15) and np.all(B['ft'] <= B['f'] + 1e-9) and \
              np.all(B['ft'] >= B['f'] - L * tau / 2 - 1e-9)
        rec('W3', ok3)
        sfpp = np.max(np.abs(B['ftpp'])); bnd = 6 / math.sqrt(eta) + 3 * L / tau
        with np.errstate(divide='ignore', invalid='ignore'):
            cotm = np.nanmax(np.where(B['ftp'] > 0, np.abs(B['ftp'] / np.tan(a)), 0))
        ok4 = sfpp <= bnd and cotm <= L / math.sinh(3 * eta / 4); rec('W4', ok4)
        # continuity of ft'' at pi/2 (C^2 gluing): ft''(pi/2^-) must be 0
        glue = abs(B['ftpp'][-1]); rec('W4glue', glue <= 1e-12)
        crho = 2 * B['f'][-1]
        ceta = 2 * np.sum(wv * np.sqrt(2 * np.clip(2 * np.arcsinh(np.sin(np.pi / 2 * v * v)) - eta, 0, None)) * np.pi * v)
        ok5 = crho >= cstar - math.pi * math.sqrt(6 * eta) - 1e-9 and crho <= ceta + 1e-6 and ceta <= cstar + 1e-12
        rec('W5', ok5)
        Phip = (1 - delta) * B['ftp']; off = e >= eta
        ok6 = np.all(Phip[off] ** 2 / 2 <= (1 - delta) ** 2 * (e[off] - eta) + 1e-14); rec('W6', ok6)
        Phi = (1 - delta) * B['ft']
        ax = np.linspace(0, np.pi / 2, 201)[:-1]; ay = np.pi - np.linspace(0, np.pi / 2, 201)[:-1]
        Pax = np.interp(ax, a, Phi); Pay = np.interp(np.pi - ay, a, Phi)
        lhs = Pax[:, None] + Pay[None, :]; rhs = (1 - delta) * (crho - 2 * L * tau - L * (ay[None, :] - ax[:, None]))
        ok7 = np.all(lhs >= rhs - 1e-9); rec('W7', ok7)
        Hact = (1 - delta) * max(sfpp, cotm)
        P(f'eta={eta} tau={tau}: W1={ok1} W2={ok2} (max|g\'|sqrt(2eta)/3={gmax*math.sqrt(2*eta)/3:.4f}) W3={ok3} '
          f'W4={ok4} (|ft\'\'|/bnd={sfpp/bnd:.3f}, cot/bnd={cotm*math.sinh(3*eta/4)/L:.3f}) glue={glue:.1e} '
          f'W5={ok5} (c^rho={crho:.6f}, c*-c^rho={cstar-crho:.4f} <= pi sqrt(6eta)={math.pi*math.sqrt(6*eta):.4f}) '
          f'W6={ok6} W7={ok7} H_actual={Hact:.3f} H_lemma_bound={(1-delta)*max(bnd, L/math.sinh(3*eta/4)):.3f}')

# ---------------- Lemma K -----------------
def ive_asym(nu, x, K=14):
    s = 1.0; term = 1.0
    for k in range(1, K + 1):
        term = term * (-(4 * nu * nu - (2 * k - 1) ** 2)) / (k * 8 * x); s += term
    return s / math.sqrt(2 * math.pi * x)
def ive1(b):
    if b >= 60: return ive_asym(1, b)
    M = 1 << 14; t = (np.arange(M) + 0.5) * np.pi / M
    return float(np.mean(np.exp(b * (np.cos(t) - 1)) * np.cos(t)))
def logk_theta(th, b):  # log of k(theta)=e^{b cos th}/Z
    return b * (np.cos(th) - 1) + math.log(b / (2 * ive1(b)))
def integ_theta_log(logf, b, n):
    # log of int_0^pi (2/pi) sin^2 th * exp(logf(th)) dth, split at a few scales (log-sum-exp; prog2b change)
    edges = sorted(set([0, min(np.pi, 10 / math.sqrt(b)), min(np.pi, 30 / math.sqrt(b)), min(np.pi, 1.0), np.pi]))
    x, w = np.polynomial.legendre.leggauss(n); terms = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        if hi <= lo: continue
        th = (hi - lo) / 2 * (x + 1) + lo
        terms.append(np.log((hi - lo) / 2 * w * (2 / np.pi) * np.sin(th) ** 2 + 1e-300) + logf(th))
    t = np.concatenate(terms); m = t.max(); return m + math.log(np.exp(t - m).sum())
def integ_theta(logf, b, n): return math.exp(integ_theta_log(logf, b, n))
def lse2(x, y): m = max(x, y); return m + math.log(math.exp(x - m) + math.exp(y - m))
def log_sinhc(y):
    y = np.asarray(y, float); out_ = np.zeros_like(y); big = y > 1e-6
    out_[big] = y[big] + np.log1p(-np.exp(-2 * y[big])) - math.log(2) - np.log(y[big])
    return out_
def EexpN(c):  # E e^{c|N|}, N std normal in R^3
    x, w = np.polynomial.legendre.leggauss(400); r = (x + 1) / 2 * (c + 12); wr = w / 2 * (c + 12)
    return float(np.sum(wr * math.sqrt(2 / math.pi) * r * r * np.exp(c * r - r * r / 2)))
worstK = -1e9
for b in (200, 1000, 4096, 16384):
    sb = math.sqrt(b)
    for pp in (0, 0.5, 1, L):
        for H in (0, 1, 5, 18):
            for eta in (b ** -0.125, 0.5, 1.0):
                bp = b * (1 - 5 * eta * eta / 48) - sb * H
                if bp <= 0: rec('K', None, nq=True); continue
                lf = lambda th: logk_theta(th, b) + log_sinhc(sb * pp * th) + sb * H * th * th / 2
                l1 = integ_theta_log(lf, b, 300); l2 = integ_theta_log(lf, b, 600)
                lrhs = -math.log(1 - 1 / b) + lse2(1.5 * math.log(b / bp) + pp * pp * b / (2 * bp),
                                          1.5 * math.log(b / (2 * math.pi)) + math.log(2 * math.pi ** 2)
                                          - b * (1 - math.cos(eta)) + sb * (pp * math.pi + H * math.pi ** 2 / 2))
                ok = l2 <= lrhs + 1e-8 and abs(l1 - l2) <= 1e-8
                rec('K', ok); worstK = max(worstK, l2 - lrhs)
                if not ok: P(f'K FAIL b={b} p={pp} H={H} eta={eta:.3f} loglhs={l2:.6e} logrhs={lrhs:.6e} conv={abs(l1-l2):.1e}')
P('Lemma K first bound: worst log(lhs/rhs) =', worstK)
worstKR = -1e9
for b in (200, 1000, 4096, 16384):
    sb = math.sqrt(b)
    for Lr in (0.5, L, 3.0):
        for eta in (b ** -0.125, 0.5, 1.0):
            b0 = b * (1 - 5 * eta * eta / 48)
            lf = lambda th: logk_theta(th, b) + sb * Lr * th
            l2 = integ_theta(lf, b, 600); l1 = integ_theta(lf, b, 300)
            rhs = (1 / (1 - 1 / b)) * ((b / b0) ** 1.5 * EexpN(Lr * math.sqrt(b / b0)) +
                                      (b / (2 * math.pi)) ** 1.5 * 2 * math.pi ** 2 * math.exp(-b * (1 - math.cos(eta)) + sb * Lr * math.pi))
            ok = l2 <= rhs * (1 + 1e-8) and abs(l1 - l2) <= 1e-8 * l2
            rec('KR', ok); worstKR = max(worstKR, l2 / rhs)
            if not ok: P(f'KR FAIL b={b} L={Lr} eta={eta:.3f} lhs={l2:.6e} rhs={rhs:.6e}')
P('Lemma K radial: worst lhs/rhs =', worstKR, ' limit E e^{L|N|} at L=1.8776:', EexpN(L))

# ---------------- Schur step on the actual kernel -----------------
eta, tau, delta = 0.5, 0.5, 0.1
B = build(eta, tau, delta)
aa = np.concatenate([B['a'], np.pi - B['a'][::-1][1:]])
Phi_full = (1 - delta) * np.concatenate([B['ft'], B['ft'][::-1][1:]])
Phip_half = (1 - delta) * B['ftp']
Hact = (1 - delta) * max(np.max(np.abs(B['ftpp'])), np.nanmax(np.where(B['ftp'] > 0, np.abs(B['ftp'] / np.tan(np.where(B['a'] > 0, B['a'], 1))), 0)))
P(f'Schur: eta={eta} tau={tau} delta={delta} H_actual={Hact:.4f}')
def Phi(x): return np.interp(x, aa, Phi_full)
def w_of(a1, b, nt, nz):
    sb = math.sqrt(b)
    xz, wz = np.polynomial.legendre.leggauss(nz)
    tot = 0.0; x, w = np.polynomial.legendre.leggauss(nt)
    edges = [0, 8 / sb, 20 / sb, 45 / sb]
    for lo, hi in zip(edges[:-1], edges[1:]):
        th = (hi - lo) / 2 * (x + 1) + lo; wt = (hi - lo) / 2 * w
        ca = np.cos(a1) * np.cos(th)[:, None] - np.sin(a1) * np.sin(th)[:, None] * xz[None, :]
        ap = np.arccos(np.clip(ca, -1, 1))
        ch = np.cosh(sb * (Phi(ap) - Phi(np.array(a1))))
        inner = (ch * wz[None, :]).sum(1) / 2
        tot += np.sum(wt * (2 / np.pi) * np.sin(th) ** 2 * np.exp(logk_theta(th, b)) * inner)
    return tot
for b in (4096, 16384, 1e6, 1e8):   # prog2b run2: 1e6, 1e8 added (omega is astronomically large at 4096)
    sb = math.sqrt(b); et = b ** -0.125
    bp = b * (1 - 5 * et * et / 48) - sb * Hact
    if bp <= 0: P('Schur: beta', b, 'does not qualify'); rec('S', None, nq=True); continue
    om = lse2(1.5 * math.log(b / bp) + L * L / 2 * (b / bp - 1),
              1.5 * math.log(b / (2 * math.pi)) + math.log(2 * math.pi ** 2) - b * (1 - math.cos(et)) + sb * (L * math.pi + Hact * math.pi ** 2 / 2)) \
         - math.log(1 - 1 / b)
    # log tail bound for theta>45/sqrt(b): 1-cos th >= 2 th^2/pi^2, cosh(...) <= e^{sqrt(b) L th}
    tailb = -2 * 45 ** 2 / math.pi ** 2 + 45 * L + math.log(b / (2 * ive1(b))) + math.log(math.pi)
    worst = -1e9; maxconv = 0
    for a1 in np.linspace(0.01, np.pi - 0.01, 120):
        w1 = w_of(a1, b, 200, 200); w2 = w_of(a1, b, 400, 400)
        maxconv = max(maxconv, abs(w1 - w2) / w2)
        php = np.interp(a1 if a1 <= np.pi / 2 else np.pi - a1, B['a'], Phip_half)
        lhs = math.log(w2); rhs = php ** 2 / 2 + om
        ok = lhs <= rhs + 1e-8; rec('S', ok); worst = max(worst, lhs - php ** 2 / 2)
        if not ok: P(f'S FAIL b={b} a1={a1:.3f} logw={lhs:.6f} Phi\'^2/2={php**2/2:.6f} omega={om:.6f}')
    P(f'Schur b={b}: omega={om:.5f}, max_a1 (log w - Phi\'^2/2)={worst:.5f}, quad conv={maxconv:.1e}, log tail bound={tailb:.1f}')

# ---------------- quaternion Monte Carlo -----------------
rng = np.random.default_rng(20261123)
N = 2_000_000; b = 3.0
Q = rng.standard_normal((N, 4)); Q /= np.linalg.norm(Q, axis=1)[:, None]
x0 = Q[:, 0]; th = np.arccos(np.clip(x0, -1, 1))
def In(n, bb, M=1 << 14):
    t = (np.arange(M) + 0.5) * np.pi / M; return float(np.mean(np.exp(bb * np.cos(t)) * np.cos(n * t)))
Zex = 2 * In(1, b) / b
ez = np.exp(b * x0); Zmc = ez.mean(); se = ez.std() / math.sqrt(N)
ok = abs(Zmc - Zex) <= 4 * se; rec('MC1', ok); P(f'MC1 Z: mc={Zmc:.6f} exact={Zex:.6f} se={se:.1e} {ok}')
kk = ez / Zex
for n in range(5):
    chi = np.sin((n + 1) * th) / np.sin(th)
    y = kk * chi / (n + 1); est = y.mean(); se = y.std() / math.sqrt(N); ex = In(n + 1, b) / In(1, b)
    ok = abs(est - ex) <= 4 * se; rec('MC2', ok); P(f'MC2 n={n}: mc={est:.6f} exact I_(n+1)/I_1={ex:.6f} se={se:.1e} {ok}')
r = Q[:, 1] ** 2 + Q[:, 2] ** 2; y = (r <= 0.3).astype(float)
ok = abs(y.mean() - 0.3) <= 4 * y.std() / math.sqrt(N); rec('MC3', ok); P(f'MC3 P(r<=.3)={y.mean():.5f} {ok}')
y = (th <= 1).astype(float); ex = (2 / np.pi) * (0.5 - math.sin(2) / 4)
ok = abs(y.mean() - ex) <= 4 * y.std() / math.sqrt(N); rec('MC4', ok); P(f'MC4 P(theta<=1)={y.mean():.5f} exact={ex:.5f} {ok}')
def qmul(p, q):
    a0, a = p[..., :1], p[..., 1:]; b0, bb = q[..., :1], q[..., 1:]
    return np.concatenate([a0 * b0 - np.sum(a * bb, -1, keepdims=True), a0 * bb + b0 * a + np.cross(a, bb)], -1)
def conj(q): return q * np.array([1, -1, -1, -1])
M = 20000
U1 = rng.standard_normal((M, 4)); U1 /= np.linalg.norm(U1, axis=1)[:, None]
U2 = rng.standard_normal((M, 4)); U2 /= np.linalg.norm(U2, axis=1)[:, None]
u1 = U1[:, 1:]; s = np.linalg.norm(u1, axis=1); uh = u1 / s[:, None]
e3 = np.array([0, 0, 1.0])
hq = np.concatenate([(1 + uh @ e3)[:, None], np.cross(uh, e3)], 1); hq /= np.linalg.norm(hq, axis=1)[:, None]
U1c = qmul(qmul(hq, U1), conj(hq)); U2c = qmul(qmul(hq, U2), conj(hq))
d1 = np.max(np.abs(U1c[:, 1:] - s[:, None] * e3))
V0 = np.sum(np.cross(U1[:, 1:], U2[:, 1:]) ** 2, 1); Vc = s ** 2 * (U2c[:, 1] ** 2 + U2c[:, 2] ** 2)
ok = d1 <= 1e-12 and np.max(np.abs(V0 - Vc)) <= 1e-12; rec('MC5', ok)
P(f'MC5 conj to s e3 err={d1:.1e}, max|V-V_a|={np.max(np.abs(V0-Vc)):.1e} {ok}')
def tomat(q):
    return np.stack([np.stack([q[:, 0] + 1j * q[:, 3], q[:, 2] + 1j * q[:, 1]], -1),
                     np.stack([-q[:, 2] + 1j * q[:, 1], q[:, 0] - 1j * q[:, 3]], -1)], -2)
M1, M2 = tomat(U1), tomat(U2)
tr = 0.5 * np.trace(np.linalg.inv(M1) @ M2, axis1=1, axis2=2).real
ip = np.sum(U1 * U2, 1)
g = rng.standard_normal((M, 4)); g /= np.linalg.norm(g, axis=1)[:, None]
V1 = np.sum(np.cross(qmul(qmul(g, U1), conj(g))[:, 1:], qmul(qmul(g, U2), conj(g))[:, 1:]) ** 2, 1)
ok = np.max(np.abs(tr - ip)) <= 1e-12 and np.max(np.abs(V1 - V0)) <= 1e-12; rec('MC6', ok)
P(f'MC6 max|Tr/2 - <,>|={np.max(np.abs(tr-ip)):.1e} max|V(gauge)-V|={np.max(np.abs(V1-V0)):.1e} {ok}')
P('counts [met, failed, not qualifying]:', cnt)
