"""chal.py -- challenger checks of SCALING_LIMIT.md (h1-chal, T87).

PREDICATES (fixed before the first run; tolerances and their origin stated):
Notation r_v(x) = I_{v+1}(x)/I_v(x), kappa_n = I_{n+1}(b)/I_1(b).
Ratios are computed by the backward continued fraction r_v = x/(2(v+1)+x r_{v+1}),
cross-checked against scipy ive (TOL_R = 1e-10 relative: worst observed CF-vs-ive
disagreement is printed; predicates use slack 1e-10 relative = double precision
accumulated over <=1e4 recurrence steps, an a-priori allowance, reported).

P1  (U1, cited RAS lower bound) for all v in 0..300, x in logspace(-2,4,61):
      r_v(x) >= x/(v+1+sqrt((v+1)^2+x^2)) (1-1e-10).
P2  (U1/L4, cited upper bound)  same grid: r_v(x) <= x/(v+1/2+sqrt((v+1/2)^2+x^2)) (1+1e-10).
P3  (B3) for all n in 0..400, beta in {4,16,64,256,1024,4096,16384}:
      -ln kappa_n <= n(n+3)/(2 beta) (1+1e-10).
P4  (B4) same grid: -ln kappa_n >= n(n+2)/(2(beta+n+1/2)) (1-1e-10).
P5  (U1 operator inequality, spectral) n1,n2 in 0..200 even, same betas:
      1-kappa_n1 kappa_n2 <= (1/2b) sum_i (n_i(n_i+2)+sqrt(n_i(n_i+2))) + 1e-12.
P6  (L2) 1 - I2/I1 <= 2/beta and int k(g) d(g,1)^2 dg <= pi^2/beta (quadrature, 2000-node GL, tol 1e-12).
P7  (U4) Z >= (2/pi)(d^3/3)(1-d^2/3) exp(b(1-d^2/2)), d=b^{-1/2}, betas above.
P8  (S3 closed form of V used by U3, L4, L5) 1000 random pairs (seed 7):
      |(1-1/2 ReTr U1U2U1^-1U2^-1) - 2 s1^2 s2^2 sin^2 gamma| < 1e-12.
P9  (C1) E0_lower = 2*4^{-1/3}*a' with a' = first zero of Ai: |E0_lower-2.94583|<1e-5 and < 3.3505330.
P10 (L3 identity AS WRITTEN, '+' sign) discretised ring N=240, circulant kernel
      k_ij ~ exp(b cos(2pi(i-j)/N)) rows sum 1, b=40, random real g (seed 11), 3 smooth chi with sum chi^2=1:
      <g,(1-K)g> - sum <chi g,(1-K)chi g> == +1/2 sum_ij k_ij g_i g_j sum_a (chi_a(i)-chi_a(j))^2   (rel tol 1e-10).
P11 (L3 with '-' sign) same with -1/2. (Exactly one of P10/P11 can hold unless the term is 0.)
P12 (L3 size) |error term| <= (#a) L^2 sup_i sum_j k_ij d_ij^2 ||g||^2 (d = arc distance).
P13 (L4 capped fibre lemma) fibre operator on L^2(S^3)=L^2(SU(2)):
      A = (1-K_1) + 2 b s^2 rho^2, rho^2 = |x x n|^2 (n=e3 suffices: K_1 is conjugation invariant),
      exact in Peter-Weyl/Hopf basis, sectors (p,q) 0..2 [EDITED before first successful run: scipy absent, cost]; for b in {1e3,1e4,1e5,1e6} and
      s in the claimed range (0, 0.002]: lowest eigenvalue >= s - 1/b (tol 1e-10).
      Hypothesis "b >= b_0": b_0 is not given; counted per b. Cap s in (0.002, 1]: measured only.
P14 (U1-U5 chain, trial function, k=0) phi = product of psi(|Y_i|), psi = exp(-al r^2) c(r/R),
      al = 2^{-1/3}, R = 4, c smooth cutoff (1 on [0,.75], 0 at >=1); g = sum of 4 center copies.
      At b in {64,256,1024,4096}: exact lattice Q(g) (K via characters, W by quadrature) and
      nu = -ln(1-Q) satisfy  (a) <1-K> <= U1 bound,  (b) lattice Dirichlet <= flat/(1-aR^2/3) (U2),
      (c) b^{1/3} nu <= chain bound assembled from U1-U4 with its explicit constants.
      Measured only: d(b) = b^{1/3} nu - E_trial(R), b^{1/3} d(b), and comparison with E_0 = 3.3505330.
"""
import json, math, sys, os
import numpy as np
from numpy.polynomial.legendre import leggauss

def roots_legendre(n):
    return leggauss(n)

def Iv_quad(v, x, M=4000):
    """exp(-x) I_v(x) for integer v by (1/pi) int_0^pi e^{x(cos t-1)} cos(v t) dt (GL M nodes)."""
    t, w = leggauss(M); t = (t + 1) * math.pi / 2; w = w * math.pi / 2
    return float(np.sum(np.exp(x * (np.cos(t) - 1)) * np.cos(v * t) * w) / math.pi)

def sturm_count(d, e2, xs):
    """number of eigenvalues < x for each x in xs (vectorised over xs)."""
    q = d[0] - xs; cnt = (q < 0).astype(int)
    for i in range(1, len(d)):
        q = np.where(q == 0, 1e-300, q)
        q = d[i] - xs - e2[i - 1] / q
        cnt += (q < 0)
    return cnt

def lowest_tridiag(d, e):
    e2 = e * e
    rad = np.concatenate([[0], np.abs(e)]) + np.concatenate([np.abs(e), [0]])
    lo, hi = float(np.min(d - rad)), float(np.min(d + rad))
    for _ in range(8):
        xs = np.linspace(lo, hi, 65)
        c = sturm_count(d, e2, xs)
        j = int(np.argmax(c >= 1))
        lo, hi = xs[j - 1], xs[j]
        if hi - lo < 1e-14 * max(1.0, abs(hi)): break
    return 0.5 * (lo + hi)

def airy_first_zero():
    """E with -u''+r u = E u, u(0)=0, decaying: shoot backward from r=14 (u~Ai), bisection."""
    def u0(E):
        h = 1e-3; r = 14.0; u = 1e-12; up = -math.sqrt(r - E) * u
        while r > 0:
            def f(rr, y): return np.array([y[1], (rr - E) * y[0]])
            y = np.array([u, up])
            k1 = f(r, y); k2 = f(r - h/2, y - h/2*k1); k3 = f(r - h/2, y - h/2*k2); k4 = f(r - h, y - h*k3)
            y = y - h/6*(k1 + 2*k2 + 2*k3 + k4); u, up = y; r -= h
        return u
    lo, hi = 2.2, 2.5; flo = u0(lo)
    for _ in range(40):
        m = 0.5 * (lo + hi); fm = u0(m)
        if (fm > 0) == (flo > 0): lo, flo = m, fm
        else: hi = m
    return 0.5 * (lo + hi)

out = {}
def rec(k, v):
    out[k] = v
    print(k, json.dumps(v, default=float)[:400]); sys.stdout.flush()

# ---------- Bessel ratios
def ratios(x, nmax):
    """r_v(x), v=0..nmax by backward CF from N with N^2 >= nmax^2 + 60x + 400."""
    N = int(math.sqrt(nmax**2 + 60 * x + 400)) + nmax + 20
    r = x / (N + 0.5 + math.sqrt((N + 1.0) ** 2 + x * x))
    out_r = np.empty(nmax + 1)
    for v in range(N - 1, -1, -1):
        r = x / (2.0 * (v + 1) + x * r)
        if v <= nmax:
            out_r[v] = r
    return out_r

def logkappa(b, nmax):
    r = ratios(b, nmax + 1)
    lk = np.concatenate([[0.0], np.cumsum(np.log(r[1:nmax + 1]))])  # ln kappa_n = sum_{v=1}^n ln r_v
    return lk

TOL = 1e-10
# cross-check CF vs ive
worst = 0.0
for x in [0.5, 3.0, 40.0, 700.0]:
    rr = ratios(x, 150)
    for v in [0, 1, 3, 10, 25]:
        a = Iv_quad(v + 1, x); bq = Iv_quad(v, x)
        if a > 1e-200 and bq > 1e-200:
            worst = max(worst, abs(rr[v] / (a / bq) - 1))
rec("cf_vs_quadrature_worst_rel", worst)

xs = np.logspace(-2, 4, 61); vs = np.arange(0, 301)
f1 = f2 = 0; n1 = 0; minslack1 = minslack2 = 1e9
for x in xs:
    r = ratios(x, 300)
    lo = x / (vs + 1 + np.sqrt((vs + 1.0) ** 2 + x * x))
    up = x / (vs + 0.5 + np.sqrt((vs + 0.5) ** 2 + x * x))
    f1 += int(np.sum(r < lo * (1 - TOL))); f2 += int(np.sum(r > up * (1 + TOL))); n1 += len(vs)
    minslack1 = min(minslack1, float(np.min(r / lo - 1))); minslack2 = min(minslack2, float(np.min(1 - r / up)))
rec("P1", dict(cases=n1, qualify=n1, failed=f1, min_rel_slack=minslack1, holds=f1 == 0))
rec("P2", dict(cases=n1, qualify=n1, failed=f2, min_rel_slack=minslack2, holds=f2 == 0))

betas = [4, 16, 64, 256, 1024, 4096, 16384]
f3 = f4 = f5 = c3 = c5 = 0; ms3 = ms4 = 1e9
for b in betas:
    lk = logkappa(b, 400); n = np.arange(0, 401)
    y = -lk
    ub = n * (n + 3) / (2.0 * b); lb = n * (n + 2) / (2.0 * (b + n + 0.5))
    f3 += int(np.sum(y > ub * (1 + TOL) + 1e-15)); f4 += int(np.sum(y < lb * (1 - TOL) - 1e-15)); c3 += len(n)
    m = n >= 1
    ms3 = min(ms3, float(np.min(ub[m] - y[m]) )); ms4 = min(ms4, float(np.min(y[m] - lb[m])))
    ne = np.arange(0, 201, 2); kap = np.exp(lk[ne])
    lhs = 1 - np.outer(kap, kap)
    e = ne * (ne + 2.0); per = (e + np.sqrt(e)) / (2 * b)
    rhs = per[:, None] + per[None, :]
    f5 += int(np.sum(lhs > rhs + 1e-12)); c5 += lhs.size
rec("P3", dict(cases=c3, failed=f3, min_abs_slack=ms3, holds=f3 == 0))
rec("P4", dict(cases=c3, failed=f4, min_abs_slack=ms4, holds=f4 == 0))
rec("P5", dict(cases=c5, failed=f5, holds=f5 == 0))

# P6, P7
xg, wg = roots_legendre(2000)
a_ = (xg + 1) * math.pi / 2; w_ = wg * math.pi / 2
f6 = 0; f7 = 0; rows6 = []
for b in betas:
    r = ratios(b, 3)
    c1 = 1 - r[1] <= 2.0 / b
    wt = np.exp(b * (np.cos(a_) - 1)) * (2 / math.pi) * np.sin(a_) ** 2 * w_
    m2 = float(np.sum(wt * a_ ** 2) / np.sum(wt))
    c2 = m2 <= math.pi ** 2 / b + 1e-12
    f6 += (not c1) + (not c2)
    Z_log = math.log(float(np.sum(np.exp(b * (np.cos(a_) - 1)) * (2 / math.pi) * np.sin(a_) ** 2 * w_))) + b
    d = b ** -0.5
    Zlb_log = math.log((2 / math.pi) * (d ** 3 / 3) * (1 - d * d / 3)) + b * (1 - d * d / 2)
    f7 += Zlb_log > Z_log
    rows6.append(dict(beta=b, one_minus_I2I1_times_b=(1 - r[1]) * b, b_times_E_d2=m2 * b, logZ=Z_log, logZlb=Zlb_log))
rec("P6", dict(failed=f6, rows=rows6, holds=f6 == 0))
rec("P7", dict(failed=f7, holds=f7 == 0))

# P8 closed form of V
rng = np.random.default_rng(7)
def su2(q):
    q = q / np.linalg.norm(q)
    return np.array([[q[0] + 1j * q[3], q[2] + 1j * q[1]], [-q[2] + 1j * q[1], q[0] - 1j * q[3]]])
mx = 0.0
for _ in range(1000):
    q1 = rng.normal(size=4); q2 = rng.normal(size=4)
    q1 /= np.linalg.norm(q1); q2 /= np.linalg.norm(q2)
    U1, U2 = su2(q1), su2(q2)
    lhs = 1 - 0.5 * np.trace(U1 @ U2 @ np.linalg.inv(U1) @ np.linalg.inv(U2)).real
    v1, v2 = q1[1:], q2[1:]
    rhs = 2 * np.linalg.norm(np.cross(v1, v2)) ** 2  # = 2 s1^2 s2^2 sin^2 gamma
    mx = max(mx, abs(lhs - rhs))
rec("P8", dict(max_abs_err=mx, holds=mx < 1e-12))

ap = airy_first_zero()
E0l = 2 * 4 ** (-1 / 3) * ap
rec("P9", dict(a_prime=ap, E0_lower=E0l, holds=abs(E0l - 2.94583) < 1e-5 and E0l < 3.3505330))

# ---------- L3 IMS on a ring
N = 240; bb = 40.0
th = 2 * math.pi * np.arange(N) / N
D = np.abs(th[:, None] - th[None, :]); D = np.minimum(D, 2 * math.pi - D)
Kr = np.exp(bb * (np.cos(D) - 1)); Kr /= Kr.sum(1, keepdims=True)  # circulant => symmetric, doubly stochastic
g = np.random.default_rng(11).normal(size=N)
# partition: chi_a = smooth, sum chi^2 = 1 (angles of a unit vector field)
s = 0.5 * (1 + np.sin(th)); t = 0.5 * (1 + np.cos(2 * th))
u = np.stack([np.cos(math.pi / 2 * s), np.sin(math.pi / 2 * s) * np.cos(math.pi / 2 * t), np.sin(math.pi / 2 * s) * np.sin(math.pi / 2 * t)])
assert np.allclose((u ** 2).sum(0), 1)
lhs = g @ (g - Kr @ g) - sum((ua * g) @ ((ua * g) - Kr @ (ua * g)) for ua in u)
term = 0.5 * np.sum(Kr * np.outer(g, g) * sum((ua[:, None] - ua[None, :]) ** 2 for ua in u))
Lc = max(float(np.max(np.abs(np.diff(np.concatenate([ua, ua[:1]])))) / (2 * math.pi / N)) for ua in u)
bound = len(u) * Lc ** 2 * float(np.max((Kr * D ** 2).sum(1))) * float(g @ g)
rec("P10", dict(lhs=float(lhs), plus_term=float(term), holds=abs(lhs - term) <= 1e-10 * abs(term)))
rec("P11", dict(lhs=float(lhs), minus_term=float(-term), holds=abs(lhs + term) <= 1e-10 * abs(term)))
rec("P12", dict(abs_term=abs(float(term)), bound=bound, ratio=abs(float(term)) / bound, holds=abs(term) <= bound))
# also with positive g (sign of term then fixed)
gp = np.abs(g) + 0.1
lhs_p = gp @ (gp - Kr @ gp) - sum((ua * gp) @ ((ua * gp) - Kr @ (ua * gp)) for ua in u)
rec("P10_positive_g_measured", dict(lhs=float(lhs_p), note="negative => localisation lowers energy estimate; '+' form would make it positive"))

# ---------- L4 fibre operator
def jacobi_matrix(K, al, be):
    k = np.arange(K, dtype=float)
    s2 = 2 * k + al + be
    with np.errstate(divide="ignore", invalid="ignore"):
        bdiag = (be ** 2 - al ** 2) / (s2 * (s2 + 2))
    if al + be == 0:
        bdiag[0] = (be - al) / (al + be + 2)
    kk = k[:-1]; s2k = s2[:-1]
    off = 2 / (s2k + 2) * np.sqrt((kk + 1) * (kk + al + 1) * (kk + be + 1) * (kk + al + be + 1) / ((s2k + 1) * (s2k + 3)))
    return bdiag, off
# validate Jacobi matrix against roots_jacobi
tq, wq = leggauss(400)
for (al, be) in [(0, 0), (2, 1), (3, 4), (1, 0)]:
    d0, e0 = jacobi_matrix(30, al, be)
    P = [np.zeros_like(tq), np.ones_like(tq)]
    w8 = (1 - tq) ** al * (1 + tq) ** be * wq
    P[1] = P[1] / math.sqrt(np.sum(w8))
    for k in range(29):
        prev = P[-2]; cur = P[-1]
        nxt = ((tq - d0[k]) * cur - (e0[k - 1] if k > 0 else 0) * prev) / e0[k]
        P.append(nxt)
    PP = np.array(P[1:])
    G = (PP * w8) @ PP.T
    assert np.max(np.abs(G - np.eye(30))) < 1e-9, (al, be, np.max(np.abs(G - np.eye(30))))

def fibre_min(b, sig, lk, pq=2):
    best = (1e9, None)
    nmax = len(lk) - 1
    for p in range(pq + 1):
        for q in range(pq + 1):
            K = (nmax - p - q) // 2
            d0, e0 = jacobi_matrix(K, q, p)       # weight (1-t)^q (1+t)^p ; rho^2 = (1-t)/2
            n = p + q + 2 * np.arange(K)
            kin = -np.expm1(lk[n])
            diag = kin + 2 * b * sig ** 2 * 0.5 * (1 - d0)
            off = 2 * b * sig ** 2 * (-0.5) * e0
            ev = lowest_tridiag(diag, off)
            if ev < best[0]:
                best = (float(ev), (p, q))
    return best

rows = []; f13 = 0; q13 = 0
for b in [1e3, 1e4, 1e5, 1e6]:
    nmax = int(6 * math.sqrt(b)) + 200
    lk = logkappa(b, nmax)
    # truncation check: compare with nmax*1.5 at one point
    sig_claim = list(np.logspace(math.log10(0.5 / b), math.log10(0.002), 12))
    sig_cap = [0.004, 0.01, 0.03, 0.1, 0.3, 1.0]
    for s_ in sig_claim + sig_cap:
        lam, sec = fibre_min(b, s_, lk)
        claim = s_ <= 0.002 + 1e-15
        ok = lam >= s_ - 1 / b - 1e-10
        if claim:
            q13 += 1; f13 += (not ok)
        rows.append(dict(beta=b, sigma=s_, lam=lam, sector=sec, bound=s_ - 1 / b, lam_over_sigma=lam / s_, in_claim=claim, ok=bool(ok)))
    lk2 = logkappa(b, int(1.5 * nmax))
    lam2 = fibre_min(b, 0.002, lk2)[0]; lam1 = [r_ for r_ in rows if r_["beta"] == b and abs(r_["sigma"] - 0.002) < 1e-12][0]["lam"]
    rec(f"P13_trunc_b{b:g}", dict(lam_nmax=lam1, lam_1p5nmax=lam2, diff=abs(lam1 - lam2)))
rec("P13", dict(cases=q13, qualify=q13, failed=f13, holds=f13 == 0, rows=rows))

# ---------- P14 trial chain
al = 2 ** (-1 / 3); Rc = 4.0
def cut(x):
    x = np.asarray(x, float); y = np.clip((x - 0.75) / 0.25, 0, 1)
    with np.errstate(divide="ignore", over="ignore"):
        A_ = np.where(y < 1, np.exp(-1 / np.maximum(1 - y, 1e-300)), 0.0)
        B_ = np.where(y > 0, np.exp(-1 / np.maximum(y, 1e-300)), 0.0)
    return A_ / (A_ + B_)
def psi(r):
    return np.exp(-al * r * r) * cut(r / Rc)
def dpsi(r, h=1e-6):
    return (psi(r + h) - psi(r - h)) / (2 * h)
rr, wr = roots_legendre(4000); r_ = (rr + 1) * Rc / 2; w_r = wr * Rc / 2
Nn = np.sum(psi(r_) ** 2 * r_ ** 2 * w_r); T1 = np.sum(dpsi(r_) ** 2 * r_ ** 2 * w_r); M2 = np.sum(psi(r_) ** 2 * r_ ** 4 * w_r)
E_trial = T1 / Nn + (4 / 3) * (M2 / Nn) ** 2
rec("E_trial_R4", dict(E_trial=float(E_trial), gaussian_value=3 * al + 3 / (4 * al * al)))
xa, wa = roots_legendre(800); xu, wu = roots_legendre(48)
uu = (xu + 1) / 2; wuu = wu / 2
rows14 = []; f14 = 0
for b in [64, 256, 1024, 4096]:
    c13 = b ** (1 / 3); aR = Rc / c13
    a = (xa + 1) * aR / 2; wa_ = wa * aR / 2
    f = psi(c13 * a); fp = c13 * dpsi(c13 * a)
    mu = (2 / math.pi) * np.sin(a) ** 2 * wa_
    # character coefficients of g1 = f(a)+f(pi-a): c_n = 2 int f chi_n dmu (n even), 0 (n odd)
    nmax = int(12 * c13 * Rc) + 200
    n = np.arange(0, nmax + 1, 2)
    chi = np.sin(np.outer(n + 1, a)) / np.sin(a)
    cn = 2 * chi @ (f * mu)
    norm1 = 2 * np.sum(f * f * mu)  # ||g1||^2
    parse = float(np.sum(cn ** 2) / norm1)
    lk = logkappa(b, nmax)
    kap = np.exp(lk[n])
    k1 = np.sum(kap * cn ** 2) / np.sum(cn ** 2)
    one_minus_K = 1 - k1 ** 2
    e = n * (n + 2.0)
    lap = np.sum(e * cn ** 2) / np.sum(cn ** 2)
    sq = np.sum(np.sqrt(e) * cn ** 2) / np.sum(cn ** 2)
    U1b = 2 * (lap + sq) / (2 * b)
    # U2: lattice Dirichlet = int f'^2 sin^2 / int f^2 sin^2 (one copy); flat = int f'^2 a^2 / int f^2 a^2
    lat_D = np.sum(fp ** 2 * np.sin(a) ** 2 * wa_) / np.sum(f ** 2 * np.sin(a) ** 2 * wa_)
    flat_D = np.sum(fp ** 2 * a ** 2 * wa_) / np.sum(f ** 2 * a ** 2 * wa_)
    U2_ok = lat_D <= flat_D / (1 - aR ** 2 / 3) * (1 + 1e-9)
    # W: per copy, 2D in (a1,a2), gamma via u=cos gamma: int_0^1 (exp(c(1-u^2))-1) du
    A1, A2 = np.meshgrid(a, a, indexing="ij")
    c = 2 * b * np.sin(A1) ** 2 * np.sin(A2) ** 2
    Wg = np.zeros_like(c)
    for uk, wk in zip(uu, wuu):
        Wg += wk * np.expm1(c * (1 - uk * uk))
    F2 = np.outer(f * f * mu, f * f * mu)
    Wexp = float(np.sum(F2 * Wg) / np.sum(F2))     # <g,Wg>/||g||^2 (copies disjoint)
    Vexp = float(np.sum(F2 * c * (2 / 3)) / np.sum(F2))
    Q = (one_minus_K + Wexp) / (1 + Wexp)
    nu = -math.log1p(-Q)
    # chain bound (U1 + U2 + U3 + U4), all as stated:
    Vmax = Rc ** 4 / (2 * c13)
    flat_pot = (4 / 3) * (M2 / Nn) ** 2 / c13      # beta^{-1/3} <2|Y1xY2|^2> in flat measure
    kin_chain = 2 * (flat_D / (1 - aR ** 2 / 3) + math.sqrt(flat_D / (1 - aR ** 2 / 3))) / (2 * b)
    W_chain = flat_pot * math.exp(Vmax) / (1 - aR ** 2 / 3) ** 2
    Zl = math.log((2 / math.pi) * (b ** -1.5 / 3) * (1 - 1 / (3 * b))) + b * (1 - 1 / (2 * b))
    cross = 12 * math.exp(b - 2 * Zl)
    mu_chain = kin_chain + W_chain + cross
    nu_chain = mu_chain / (1 - mu_chain) if mu_chain < 1 else float("inf")
    okc = (one_minus_K <= U1b * (1 + 1e-9)) and U2_ok and (nu <= nu_chain * (1 + 1e-9))
    f14 += not okc
    d = c13 * nu - E_trial
    rows14.append(dict(beta=b, parseval=parse, one_minus_K=one_minus_K, U1_bound=U1b, lat_D=lat_D, flat_D_over=flat_D / (1 - aR ** 2 / 3),
                       W=Wexp, V=Vexp, Q=Q, b13_nu=c13 * nu, b13_nu_chain=c13 * nu_chain, d=d, b13_d=c13 * d,
                       b13_nu_minus_E0=c13 * nu - 3.3505330, ok=bool(okc)))
rec("P14", dict(E_trial=float(E_trial), failed=f14, cases=4, holds=f14 == 0, rows=rows14))

os.makedirs("results", exist_ok=True)
fn = sys.argv[1] if len(sys.argv) > 1 else "results/chal_run1.json"
with open(fn, "x") as fh:
    json.dump(out, fh, indent=1, default=float)
print("wrote", fn)
