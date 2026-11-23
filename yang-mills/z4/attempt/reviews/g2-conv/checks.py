"""checks.py -- scalar inequalities used in SCALING_LIMIT.md (g2-conv, T77).

Predicates (fixed before the first run).  r_nu(x) := I_{nu+1}(x)/I_nu(x),
computed by backward recurrence r_{nu-1} = 1/(2nu/x + r_nu) started at nu=20000 with r=0.
Grid: nu = 0..400, x in {0.5,1,2,4,...,4096}.  Tolerance REL = 1e-12: double-precision
rounding of a recurrence of a few thousand steps (each step relative error ~1e-16, contracting).
 B0  recurrence agrees with a direct power series (log-space terms, 6000 terms) for
     nu=0..40, x in {1,4,16,64}: relative difference <= 1e-10 (series summation error).
 B1  (Amos lower) r_nu(x) >= x/(nu+1+sqrt((nu+1)^2+x^2)) * (1-REL)   for all grid points.
 B2  (Amos upper) r_nu(x) <= x/(nu+1/2+sqrt((nu+1/2)^2+x^2)) * (1+REL) for all grid points.
 B3  (derived kinetic upper bound, Lemma U2) -ln(I_{n+1}(x)/I_1(x)) <= n(n+3)/(2x) (1+REL)
     for n = 0..400 and every x of the grid.
 B4  (derived kinetic lower bound, TORON S5) -ln(I_{n+1}(x)/I_1(x)) >= n(n+2)/(2(x+n+1/2))(1-REL).
 B5  (second moment, Lemma L3) 1 - r_1(x) <= 2/x for every x of the grid.
 B6  (geometry) on a 200001-point grid of a in [0,pi]: sin^2 a <= a^2 ; a^2 <= (pi^2/2)(1-cos a);
     sin^2 a >= a^2 (1 - a^2/3) (tolerance 1e-15 absolute, rounding).
 B7  (Airy zero, CITED value 2.33810741) the lowest eigenvalue e of -u''+r u on (0,inf),
     u(0)=0, by RK4 shooting (h=1e-3, r<=12) agrees with 2.33810741 to 1e-6 (step size h^4).
 B8  (arithmetic, Lemma C1) 2 * (1/4)^(1/3) * 2.33810741 <= 3.3505330 (E_0 of NUMERICS.md).
 M1  measured only: beta * (-ln(I_2/I_0)) at beta = 16..1024 (U(1) discriminator, ->2).
Exit code 0 iff all predicates B0..B8 are met.  Output: results/checks2.json (mode "x").
"""
import json, math, os, sys
import numpy as np

REL = 1e-12
NUS = np.arange(0, 401)
XS = [0.5] + [2.0 ** k for k in range(0, 13)]


def ratios(x, numax=400, start=20000):
    r = 0.0
    out = np.zeros(numax + 1)
    for nu in range(start, 0, -1):
        r = 1.0 / (2.0 * nu / x + r)   # this is r_{nu-1}
        if nu - 1 <= numax:
            out[nu - 1] = r
    return out


def series_I(n, x, K=6000):
    s = 0.0
    for k in range(K):
        t = (2 * k + n) * math.log(x / 2) - math.lgamma(k + 1) - math.lgamma(k + n + 1) - x
        s += math.exp(t)
    return s


res = {}
ok = {}
# B0
worst = 0.0
for x in [1.0, 4.0, 16.0, 64.0]:
    r = ratios(x)
    for nu in range(0, 41):
        rs = series_I(nu + 1, x) / series_I(nu, x)
        worst = max(worst, abs(rs / r[nu] - 1))
res["B0_worst_rel"] = worst; ok["B0"] = worst <= 1e-10
b1 = b2 = b3 = b4 = 0; b1f = []; b2f = []; b3f = []; b4f = []; ncase = 0
slack3 = 1e9
b5 = []
for x in XS:
    r = ratios(x)
    for nu in NUS:
        ncase += 1
        lo = x / (nu + 1 + math.sqrt((nu + 1) ** 2 + x * x))
        hi = x / (nu + 0.5 + math.sqrt((nu + 0.5) ** 2 + x * x))
        if r[nu] >= lo * (1 - REL): b1 += 1
        else: b1f.append((int(nu), x))
        if r[nu] <= hi * (1 + REL): b2 += 1
        else: b2f.append((int(nu), x))
    cum = np.concatenate([[0.0], np.cumsum(-np.log(r[1:]))])  # cum[n] = -ln(I_{n+1}/I_1)
    for n in NUS:
        ub = n * (n + 3) / (2 * x); lb = n * (n + 2) / (2 * (x + n + 0.5))
        if cum[n] <= ub * (1 + REL) + 1e-300: b3 += 1
        else: b3f.append((int(n), x))
        if cum[n] >= lb * (1 - REL): b4 += 1
        else: b4f.append((int(n), x))
        if n > 0: slack3 = min(slack3, ub / cum[n] - 1)
    b5.append((x, 1 - r[1], 2 / x, (1 - r[1]) <= 2 / x))
res.update(B1=[b1, ncase, b1f[:10]], B2=[b2, ncase, b2f[:10]], B3=[b3, ncase, b3f[:10], slack3],
           B4=[b4, ncase, b4f[:10]], B5=b5)
ok["B1"] = b1 == ncase; ok["B2"] = b2 == ncase; ok["B3"] = b3 == ncase; ok["B4"] = b4 == ncase
ok["B5"] = all(t[3] for t in b5)
a = np.linspace(0, math.pi, 200001)
g1 = np.max(np.sin(a) ** 2 - a ** 2); g2 = np.max(a ** 2 - (math.pi ** 2 / 2) * (1 - np.cos(a)))
g3 = np.max(a ** 2 * (1 - a ** 2 / 3) - np.sin(a) ** 2)
res["B6"] = [float(g1), float(g2), float(g3)]; ok["B6"] = max(g1, g2, g3) <= 1e-15


def shoot(E, h=1e-3, R=12.0):
    u, v, r = 0.0, 1.0, 0.0
    f = lambda r, u, v: (v, (r - E) * u)
    while r < R:
        k1 = f(r, u, v); k2 = f(r + h / 2, u + h / 2 * k1[0], v + h / 2 * k1[1])
        k3 = f(r + h / 2, u + h / 2 * k2[0], v + h / 2 * k2[1]); k4 = f(r + h, u + h * k3[0], v + h * k3[1])
        u += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); v += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]); r += h
    return u


lo_, hi_ = 2.0, 2.6
for _ in range(40):
    mid = (lo_ + hi_) / 2
    if shoot(lo_) * shoot(mid) <= 0: hi_ = mid
    else: lo_ = mid
e = (lo_ + hi_) / 2
res["B7"] = e; ok["B7"] = abs(e - 2.33810741) <= 1e-6
bound = 2 * 0.25 ** (1 / 3) * 2.33810741
res["B8"] = bound; ok["B8"] = bound <= 3.3505330
m1 = {}
for b in [16, 64, 256, 1024]:
    r = ratios(float(b))
    m1[b] = b * (-math.log(r[0] * r[1]))
res["M1_beta_times_U1gap"] = m1
res["ok"] = ok
os.makedirs("results", exist_ok=True)
with open("results/checks2.json", "x") as fh:
    json.dump(res, fh, indent=1, default=float)
ok = {k: bool(v) for k, v in ok.items()}
print(json.dumps(ok), "B3 min slack", slack3, "B7", e, "B8", bound, "M1", m1)
sys.exit(0 if all(ok.values()) else 1)
