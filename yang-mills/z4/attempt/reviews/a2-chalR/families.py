"""families.py -- a2-chalR attack items A2 and A3 on Theorem R of A1_REDUCTION.md.

Spectral measures are finite sums of atoms in E = eps*xi (energy in units of the gap),
nu_beta = sum_k w_k delta_{E_k}, all E_k >= 1 (hypothesis (A): support in [m, inf)).
C(t xi) = sum w_k exp(-t E_k).  mu_beta = normalised exp(-E) nu_beta.  G(t) = C(t xi)/C(xi).
xi runs over XI = 1e1 ... 1e6 (hypothesis (B): xi -> infinity).

PREDICATES (fixed before first run; tolerance REL=1e-9 is float64 round-off headroom
for sums of <= 2e5 positive terms; LIM=1e-3 is the "converged" tolerance across the last
two xi values, chosen by me, not from the target):

Family F1 (A),(B),(C) hold: discretised free-field density sqrt(E^2-1) on [1, xi*4],
  plus atom at E=1 (tests the 'atom at m' question).
  P1a  D1 := max over xi of C(xi/2)/C(xi) is finite and >= sqrt(e) (sqrt(e) is the minimum
       possible for any measure on [1,inf)).
  P1b  (R2) for every xi and every K in 0..40: mu(E>K) <= D1*exp(-K/2)*(1+REL).
  P1c  (R4) for t in {1,1.5,2,3,5}: D1^(-2(t-1))*(1-REL) <= G(t) <= exp(-(t-1))*(1+REL), every xi.
  P1d  (R4 Jensen) mean_mu(E) <= 2 log D1 *(1+REL), every xi.
  P1e  (R3) G(t) at the two largest xi agree within LIM for t in {0.6,0.75,1,2,3}.
Family F2a (A),(B) hold, (C) fails, mu tight: nu = e^{-A} d_1 + d_{1.5A}, A = log(xi)^2/4...
  here A = sqrt(xi).
  P2a  C(xi/2)/C(xi) at largest xi > 1e3 (C fails).
  P2b  G(2) at largest xi within LIM of exp(-1) (nondegenerate limit for t>1 anyway).
Family F2b (A),(B) hold, (C) fails, mass escapes: nu = e^{-2K} d_1 + d_K, K = log(xi).
  P2c  G(2) at largest xi < 1e-3 ; G(1) = 1 (degenerate limit: 1 at t=1, 0 for t>1).
Family F3 (C) holds, (C+) fails: nu = d_1 + e^{K/2} d_K, K = log(xi)^2 /2 ... K = 2 log(xi).
  P3a  C(xi/2)/C(xi) bounded by 1+e^{1/2} ... checked as: max over xi <= 3.
  P3b  G(1/4) at largest xi > 1e2 (C+ with j=2 fails; G_beta(1/4) diverges).
  P3c  G(2) at largest xi within LIM of exp(-1) (limit for t>1/2 is e^{-(t-1)}, whose
       continuation to t=1/4 is finite: the limit at t<1/2 is not the continuation).
Family F4 (A),(B),(C) hold, bottom weight vanishes: nu = (1/xi) d_1 + d_3.
  P4a  G(2) at largest xi within LIM of exp(-2) (limit spectral bottom 3, not 1).
Family F5 subsequence dependence: nu = d_1 for even index, d_2 for odd.
  P5a  |G_even(2) - G_odd(2)| > 0.1 (limit depends on subsequence; R3 allows it, item 6 lists it).
A3: model density eps^(p-1) on [m,1], i.e. E^(p-1) on [1, xi] (up to xi^-p factor).
  P6a  for p in {0.5,1,2,3}, j in {1,2,3,4}: ratio_j(xi=1e6) within 1e-3 relative of the exact
       limit 2^(jp) Gamma(p,2^-j)/Gamma(p,1) (my derivation; quadrature tolerance).
  P6b  the text's constant e*2^(jp) is an upper bound for ratio_j at xi=1e6 for all (p,j).
       (Expected by me to FAIL for p<1.)
Output: results_families.txt, opened with mode "x".
"""
import math
import numpy as np

REL = 1e-9
LIM = 1e-3
XI = [1e1, 1e2, 1e3, 1e4, 1e5, 1e6]
out = open("results_families.txt", "x")
fails = []


def say(s):
    print(s)
    out.write(s + "\n")


def pred(name, ok, info=""):
    say(f"{name}: {'MET' if ok else 'FAILED'} {info}")
    if not ok:
        fails.append(name)


def C(E, w, t):
    # stable: factor out exp(-t*Emin)
    return np.sum(w * np.exp(-t * (E - E.min()))) * math.exp(-t * E.min())


def G(E, w, t):
    return C(E, w, t) / C(E, w, 1.0)


def mu(E, w):
    q = w * np.exp(-(E - E.min()))
    return q / q.sum()


# ---------- F1 ----------
def f1(xi):
    Emax = 4.0 * xi
    n = 200000
    # graded grid: denser near 1
    u = (np.arange(n) + 0.5) / n
    E = 1.0 + (Emax - 1.0) * u ** 3
    dE = 3 * (Emax - 1.0) * u ** 2 / n
    w = np.sqrt(E * E - 1.0) * dE / xi ** 2  # overall normalisation irrelevant
    E = np.concatenate([[1.0], E])
    w = np.concatenate([[1e-3 * w.sum() / 10], w])  # atom exactly at E=1
    return E, w


say("== F1: (A),(B),(C) hold; free-field-like density + atom at E=1 ==")
D1 = 0
rows = {}
for xi in XI:
    E, w = f1(xi)
    r = G(E, w, 0.5)
    D1 = max(D1, r)
    rows[xi] = (E, w)
    say(f"xi={xi:.0e} C(xi/2)/C(xi)={r:.6f} G(0.6)={G(E,w,0.6):.6f} G(2)={G(E,w,2):.6f}")
pred("P1a", math.isfinite(D1) and D1 >= math.sqrt(math.e), f"D1={D1:.6f} sqrt(e)={math.sqrt(math.e):.6f}")
ok = True
for xi, (E, w) in rows.items():
    m_ = mu(E, w)
    for K in range(41):
        if m_[E > K].sum() > D1 * math.exp(-K / 2) * (1 + REL):
            ok = False
pred("P1b", ok, "(R2) tail bound")
ok = True
for xi, (E, w) in rows.items():
    for t in [1, 1.5, 2, 3, 5]:
        g = G(E, w, t)
        if not (D1 ** (-2 * (t - 1)) * (1 - REL) <= g <= math.exp(-(t - 1)) * (1 + REL)):
            ok = False
            say(f"  viol xi={xi} t={t} G={g}")
pred("P1c", ok, "(R4) two-sided bounds")
ok = True
for xi, (E, w) in rows.items():
    mean = float(np.sum(mu(E, w) * E))
    if mean > 2 * math.log(D1) * (1 + REL):
        ok = False
    say(f"  xi={xi:.0e} mean E={mean:.6f}  2logD1={2*math.log(D1):.6f}")
pred("P1d", ok, "(R4) Jensen mean bound")
E5, w5 = rows[1e5]
E6, w6 = rows[1e6]
diffs = [abs(G(E5, w5, t) - G(E6, w6, t)) for t in [0.6, 0.75, 1, 2, 3]]
pred("P1e", max(diffs) < LIM, f"max diff {max(diffs):.2e}")

# ---------- F2a ----------
say("== F2a: (C) fails, mu tight ==")
for xi in XI:
    A = math.sqrt(xi)
    E = np.array([1.0, 1.5 * A])
    # weights in log form to avoid underflow: w1 = e^{-A}, w2 = 1 -> rescale by e^{A}
    w = np.array([1.0, math.exp(min(A, 700.0)) if A < 700 else np.inf])
    # compute with logs
    def lC(t):
        a = -A - t * 1.0
        b = -t * 1.5 * A
        mx = max(a, b)
        return mx + math.log(math.exp(a - mx) + math.exp(b - mx))
    r = math.exp(lC(0.5) - lC(1.0))
    g2 = math.exp(lC(2.0) - lC(1.0))
    say(f"xi={xi:.0e} C(xi/2)/C(xi)={r:.4e} G(2)={g2:.6f}")
pred("P2a", r > 1e3, f"ratio={r:.3e}")
pred("P2b", abs(g2 - math.exp(-1)) < LIM, f"G(2)={g2:.6f}")

# ---------- F2b ----------
say("== F2b: (C) fails, mass escapes to infinity ==")
for xi in XI:
    K = math.log(xi)
    def lC(t):
        a = -2 * K - t
        b = -t * K
        mx = max(a, b)
        return mx + math.log(math.exp(a - mx) + math.exp(b - mx))
    g2 = math.exp(lC(2.0) - lC(1.0))
    say(f"xi={xi:.0e} K={K:.3f} C(xi/2)/C(xi)={math.exp(lC(.5)-lC(1)):.4e} G(1.5)={math.exp(lC(1.5)-lC(1)):.6f} G(2)={g2:.6e}")
pred("P2c", g2 < 1e-3, f"G(2)={g2:.3e} (limit G = 1 at t=1, 0 for t>1)")

# ---------- F3 ----------
say("== F3: (C) holds, (C+) fails ==")
mx3 = 0
for xi in XI:
    K = 2 * math.log(xi)
    def lC(t):
        a = -t
        b = K / 2 - t * K
        mx = max(a, b)
        return mx + math.log(math.exp(a - mx) + math.exp(b - mx))
    r = math.exp(lC(0.5) - lC(1.0))
    mx3 = max(mx3, r)
    g14 = math.exp(lC(0.25) - lC(1.0))
    g2 = math.exp(lC(2.0) - lC(1.0))
    say(f"xi={xi:.0e} C(xi/2)/C(xi)={r:.6f} G(1/4)={g14:.4e} G(2)={g2:.6f} limit-continuation e^(3/4)={math.exp(.75):.4f}")
pred("P3a", mx3 <= 3, f"max ratio {mx3:.4f}")
pred("P3b", g14 > 1e2, f"G(1/4)={g14:.3e}")
pred("P3c", abs(g2 - math.exp(-1)) < LIM, f"G(2)={g2:.6f}")

# ---------- F4 ----------
say("== F4: bottom weight vanishes ==")
for xi in XI:
    E = np.array([1.0, 3.0])
    w = np.array([1 / xi, 1.0])
    say(f"xi={xi:.0e} C(xi/2)/C(xi)={G(E,w,.5):.6f} G(2)={G(E,w,2):.6f}")
pred("P4a", abs(G(E, w, 2) - math.exp(-2)) < LIM, f"G(2)={G(E,w,2):.6f} vs e^-2={math.exp(-2):.6f}")

# ---------- F5 ----------
say("== F5: alternating ==")
ge = G(np.array([1.0]), np.array([1.0]), 2)
go = G(np.array([2.0]), np.array([1.0]), 2)
pred("P5a", abs(ge - go) > 0.1, f"G_even(2)={ge:.6f} G_odd(2)={go:.6f}")


# ---------- A3 ----------
def uinc_gamma(p, x, n=400000):
    # Gamma(p, x) = int_x^inf s^(p-1) e^-s ds, substitution s = x + y, y in [0, 60]
    # midpoint on y = 60*u^2 grading
    u = (np.arange(n) + 0.5) / n
    y = 80.0 * u ** 2
    dy = 160.0 * u / n
    s = x + y
    return float(np.sum(s ** (p - 1) * np.exp(-s) * dy))


def ratio_model(p, j, xi, n=400000):
    # int_1^xi E^(p-1) e^(-E/2^j) dE / int_1^xi E^(p-1) e^-E dE ; log-graded grid
    u = (np.arange(n) + 0.5) / n
    L = math.log(xi)
    E = np.exp(L * u)
    dE = E * L / n
    f = E ** (p - 1)
    return float(np.sum(f * np.exp(-E / 2 ** j) * dE) / np.sum(f * np.exp(-E) * dE))


say("== A3: model density eps^(p-1) on [m,1] ==")
okA = True
okB = True
for p in [0.5, 1.0, 2.0, 3.0]:
    for j in [1, 2, 3, 4]:
        r6 = ratio_model(p, j, 1e6)
        r3 = ratio_model(p, j, 1e3)
        lim = 2 ** (j * p) * uinc_gamma(p, 2.0 ** -j) / uinc_gamma(p, 1.0)
        claim = math.e * 2 ** (j * p)
        say(f"p={p} j={j} D_j(xi=1e3)={r3:.5f} D_j(xi=1e6)={r6:.5f} exact-limit={lim:.5f} text e*2^jp={claim:.5f} ratio/claim={r6/claim:.4f}")
        if abs(r6 / lim - 1) > 1e-3:
            okA = False
        if r6 > claim:
            okB = False
pred("P6a", okA, "quadrature matches Gamma-function limit")
pred("P6b", okB, "text constant e*2^(jp) is an upper bound")
say(f"FAILED PREDICATES: {fails}")
out.close()
