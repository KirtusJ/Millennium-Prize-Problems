"""ff_check.py -- independent check (c2-chalS) of the free-field known-answer test of THEOREM_S.md section 6.

(numpy only: Bessel I_n by Miller recurrence, K1 by trapezoid on its cosh integral, Gauss-Legendre 80x32 in u=log t.)
Lattice: Z^4, action sum (1/2)(grad phi)^2 + (m^2/2) phi^2. Propagator by the Schwinger/Bessel representation
    G_m(n) = int_0^inf dt exp(-m^2 t) prod_mu [exp(-2t) I_{n_mu}(2t)]
(exact; 1D quadrature in u = log t).  Scale a := E0 = 2 asinh(m/2) (claimed exact gap), N = 2 floor(1/(2a)),
normalized S(x) = G(x/a)/G(N e0) with x/a rounded to the nearest lattice point. Masses m = 1/4, 1/8, 1/16, 1/32.

PREDICATES (fixed before the first run):
 Q0  quadrature self-check: residual |(m^2+8)G(0) - 8 G(e1) - 1| <= 1e-8 for each m.
     (tolerance: quad epsabs/epsrel 1e-12 on O(1) integrals; 1e-8 leaves 4 orders margin)
 Q1  exact gap: zero-momentum correlator C(n) = int dt e^{-m^2 t} ive(n,2t)  equals e^{-E0 n}/(2 sinh E0)
     with E0 = 2 asinh(m/2), relative error <= 1e-7 for n = 1, 5, 20, each m.  (quadrature tolerance as Q0)
 Q2  H3(b) k=2 for phi: sup over lattice points 0 < |x| <= 3 (physical) of |x|^2 S(x) is <= 3 for every m, and
     the four sups differ pairwise by <= 1 (bounded, not growing). (3 and 1: my expectation from the continuum value
     1/K1(1) = 1.66 plus lattice O(1) corrections at |n|=1; author reports 1.64 .. 2.15.)
 Q3  limit = continuum mass-1 propagator: at m = 1/32, for the 6 points listed below,
     |S_lat(x) / S_cont([x]_a) - 1| <= 1e-2, where S_cont(y) = K1(|y|)/(|y| K1(1)).  (expected O(a^2) ~ 1e-3
     plus rounding of the normalization point aN vs 1, which is absent since S_cont is normalized at 1 exactly
     and aN = 1 - O(a): this adds O(a) ~ 3e-2 * dlog S/dx ... so I ALSO record the version normalized at aN;
     the predicate is on the aN-normalized ratio  S_lat(x)/[S_cont([x]_a)/S_cont(aN e0)] ).
     Also the error must decrease from m=1/8 to m=1/32 at each point.
 Q4  unnormalized: a^{-2} G(x/a) -> K1(|x|)/(4 pi^2 |x|): relative error at m=1/32 <= 2e-2 at |x| = 1, 2 on axis
     and off axis.  (2e-2: m/a - 1 = O(m^2) negligible; O(a^2) lattice + rounding of |x| up to a/2 in the
     argument; measured vs continuum at the ROUNDED point, so 2e-2 is generous.)
 Q5  rotation: |S([R x]_a) - S([x]_a)| at x = e1 (|x|=1) for rotation by 1 rad in (1,2) plane, and
     |S(e0) - S((1/2,1/2,1/2,1/2))|: decrease monotonically over m = 1/8, 1/16, 1/32 (measured; predicate
     is monotone decrease).
 Q6  :phi^2: two-point function is 2G^2, normalized S_{phi^2} = S_phi^2 exactly (algebraic identity; check
     |x|^4 S_{phi^2} bounded by 9 (=3^2) on the Q2 range: H3(b) with D=2).
 Q7  A6: truncated 4-point function of :phi^2: (Wick: 16 [G12G23G34G41 + G13G32G24G41 + G12G24G43G31]) is
     nonzero; verified against Monte Carlo of a 4-dim Gaussian vector with covariance G (seed 20261123,
     2e6 samples), agreement within 5 standard errors.
Results go to ff_check.out (opened with mode "x").
"""
import math, sys
import numpy as np
# numpy only (no scipy on this machine): own scaled Bessel I_n, own K1, own Gauss-Legendre quadrature.

def i0e(x):
    x = np.asarray(x, float); out = np.empty_like(x)
    sm = x <= 30
    out[sm] = np.i0(x[sm]) * np.exp(-x[sm])
    xl = x[~sm]; ser = np.zeros_like(xl); term = np.ones_like(xl)
    for k in range(0, 40):
        if k > 0:
            term = term * (2 * k - 1) ** 2 / (k * 8.0 * xl)
        ser += term
    out[~sm] = ser / np.sqrt(2 * np.pi * xl)
    return out

def ive_table(nmax, x):
    """rows n=0..nmax of exp(-x) I_n(x) by Miller backward recurrence on ratios."""
    x = np.asarray(x, float)
    start = int(nmax + 60 + 12 * math.sqrt(x.max()))
    r = np.zeros_like(x)
    ratios = np.empty((nmax + 1, x.size))
    for n in range(start, 0, -1):
        r = 1.0 / (2.0 * n / x + r)
        if n <= nmax:
            ratios[n] = r
    T = np.empty((nmax + 1, x.size)); T[0] = i0e(x)
    for n in range(1, nmax + 1):
        T[n] = T[n - 1] * ratios[n]
    return T

_XG, _WG = np.polynomial.legendre.leggauss(32)
_cache = {}
def _nodes(m, nmax):
    key = (m, nmax)
    if key in _cache: return _cache[key]
    lo, hi = -30.0, math.log(60.0 / (m * m))
    edges = np.linspace(lo, hi, 81)
    us = []; ws = []
    for i in range(80):
        A, B = edges[i], edges[i + 1]
        us.append(0.5 * (B - A) * _XG + 0.5 * (A + B)); ws.append(0.5 * (B - A) * _WG)
    u = np.concatenate(us); w = np.concatenate(ws); t = np.exp(u)
    base = w * t * np.exp(-m * m * t)
    T = ive_table(nmax, 2 * t)
    _cache[key] = (base, T)
    return _cache[key]

NMAX = 200
def G(n, m):
    n = [abs(int(v)) for v in n]
    base, T = _nodes(m, NMAX)
    p = base.copy()
    for k in n: p = p * T[k]
    return float(p.sum())

def C0(n, m):
    base, T = _nodes(m, NMAX)
    return float((base * T[n]).sum())

def k1(x):
    u = np.linspace(0, 12, 24001); h = u[1] - u[0]
    f = np.exp(-x * np.cosh(u)) * np.cosh(u)
    return float(h * (f.sum() - 0.5 * f[0] - 0.5 * f[-1]))

class special:
    k1 = staticmethod(k1)

def Scont(r):
    return special.k1(r) / (r * special.k1(1.0))

def main():
    out = open("ff_check.out", "x")
    def w(s):
        print(s); out.write(s + "\n"); out.flush()
    res = {}
    masses = [1/4, 1/8, 1/16, 1/32]
    w("masses " + str(masses))
    # Q0
    q0 = []
    for m in masses:
        r = abs((m*m + 8) * G((0,0,0,0), m) - 8 * G((1,0,0,0), m) - 1)
        q0.append(r); w(f"Q0 m={m}: residual {r:.3e}")
    res["Q0"] = all(r <= 1e-8 for r in q0)
    # Q1
    q1 = []
    for m in masses:
        E0 = 2 * math.asinh(m / 2)
        for n in (1, 5, 20):
            c = C0(n, m); ex = math.exp(-E0 * n) / (2 * math.sinh(E0))
            q1.append(abs(c / ex - 1)); w(f"Q1 m={m} n={n}: C={c:.12e} exact={ex:.12e} rel {abs(c/ex-1):.2e}")
    res["Q1"] = all(e <= 1e-7 for e in q1)
    # Q2, Q6
    sups = []; sups2 = []
    data = {}
    for m in masses:
        a = 2 * math.asinh(m / 2); N = 2 * math.floor(1 / (2 * a)); ZZ = G((N, 0, 0, 0), m)
        data[m] = (a, N, ZZ)
        R = int(math.floor(3 / a))
        best = 0; best2 = 0; arg = None
        # scan points on axis, face diagonals, body diagonals and a few generic directions up to |x|<=3
        cand = set()
        for k in range(1, R + 1):
            for v in [(k,0,0,0),(k,k,0,0),(k,k,k,0),(k,k,k,k),(k,(k+1)//2,0,0),(2*k,k,k,0)]:
                if math.sqrt(sum(c*c for c in v)) * a <= 3: cand.add(v)
        for v in [(1,1,0,0),(1,1,1,0),(1,1,1,1),(2,1,0,0),(2,1,1,0)]: cand.add(v)
        for v in sorted(cand):
            r = math.sqrt(sum(c*c for c in v)) * a
            s = G(v, m) / ZZ
            if r*r*s > best: best, arg = r*r*s, v
            best2 = max(best2, r**4 * s * s)
        sups.append(best); sups2.append(best2)
        w(f"Q2 m={m}: a={a:.8f} N={N} Z^2={ZZ:.6e} #pts={len(cand)} sup|x|^2 S={best:.4f} at n={arg}; Q6 sup|x|^4 S_phi2={best2:.4f}")
    res["Q2"] = all(s <= 3 for s in sups) and max(sups) - min(sups) <= 1
    res["Q6"] = all(s <= 9 for s in sups2)
    # Q3, Q4
    pts = [(1,0,0,0),(2,0,0,0),(0.5,0.5,0.5,0.5),(0,math.cos(1),math.sin(1),0),(0.6,0.8,1.2,0.4),(1,1,1,1)]
    err3 = {}; err4 = {}
    for m in [1/8, 1/16, 1/32]:
        a, N, ZZ = data[m]
        for x in pts:
            n = tuple(int(round(c / a)) for c in x)
            y = math.sqrt(sum(c*c for c in n)) * a
            g = G(n, m)
            s = g / ZZ
            sc = Scont(y) / Scont(a * N)
            e3 = abs(s / sc - 1)
            e3b = abs(s / Scont(math.sqrt(sum(c*c for c in x))) - 1)
            u = g / a**2; uc = special.k1(y) / (4 * math.pi**2 * y)
            e4 = abs(u / uc - 1)
            err3[(m, x)] = e3; err4[(m, x)] = e4
            w(f"Q3/Q4 m={m} x={tuple(round(c,4) for c in x)} n={n} |[x]|={y:.5f}: S={s:.6f} cont(aN-norm)={sc:.6f} rel={e3:.2e} | vs K1(|x|)/(|x|K1(1)) unrounded rel={e3b:.2e} | a^-2 G={u:.6f} K1/(4pi^2 r)={uc:.6f} rel={e4:.2e}")
    q3 = [err3[(1/32, x)] <= 1e-2 for x in pts]
    mono3 = [err3[(1/32, x)] < err3[(1/8, x)] for x in pts]
    w(f"Q3 per point (m=1/32 <=1e-2): {q3}; decreasing 1/8->1/32: {mono3}")
    res["Q3"] = all(q3) and all(mono3)
    q4 = [err4[(1/32, x)] <= 2e-2 for x in pts]
    w(f"Q4 per point: {q4}")
    res["Q4"] = all(q4)
    # Q5
    d1 = []; d2 = []
    for m in [1/8, 1/16, 1/32]:
        a, N, ZZ = data[m]
        def S(x):
            return G(tuple(int(round(c / a)) for c in x), m) / ZZ
        r1 = abs(S((0, math.cos(1), math.sin(1), 0)) - S((0, 1, 0, 0)))
        r2 = abs(S((1, 0, 0, 0)) - S((0.5, 0.5, 0.5, 0.5)))
        d1.append(r1); d2.append(r2); w(f"Q5 m={m}: rot diff {r1:.3e}, diag diff {r2:.3e}")
    res["Q5"] = d1[0] > d1[1] > d1[2] and d2[0] > d2[1] > d2[2]
    # Q7
    m = 1/8; a, N, ZZ = data[m]
    P = [(0,0,0,0),(3,1,0,0),(1,4,2,0),(5,2,1,3)]
    Cm = np.array([[G(tuple(p[i]-q[i] for i in range(4)), m) for q in P] for p in P])
    g = lambda i, j: Cm[i, j]
    tr = 16 * (g(0,1)*g(1,2)*g(2,3)*g(3,0) + g(0,2)*g(2,1)*g(1,3)*g(3,0) + g(0,1)*g(1,3)*g(3,2)*g(2,0))
    rng = np.random.default_rng(20261123)
    L = np.linalg.cholesky(Cm)
    X = rng.standard_normal((2_000_000, 4)) @ L.T
    W = X**2 - np.diag(Cm)  # :phi^2:
    def mom(idx):
        return np.prod(W[:, idx], axis=1)
    m4 = mom([0,1,2,3]); E = lambda idx: np.mean(mom(idx))
    pairs = [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
    trunc_samples = m4  # means of first moments are zero; truncated = E4 - sum E2E2 (3-point terms times 1-pt vanish)
    t_est = np.mean(m4) - sum(E(list(p)) * E(list(q)) for p, q in pairs)
    se = np.std(m4) / math.sqrt(len(m4))
    w(f"Q7 m=1/8 points {P}: Wick truncated 4pt of :phi^2: = {tr:.6e}; MC = {t_est:.6e} (se of 4-moment {se:.2e})")
    res["Q7"] = tr != 0 and abs(t_est - tr) <= 5 * se
    for k in sorted(res):
        w(f"PREDICATE {k}: {'MET' if res[k] else 'FAILED'}")
    out.close()
    return 0

if __name__ == "__main__":
    sys.exit(main())
