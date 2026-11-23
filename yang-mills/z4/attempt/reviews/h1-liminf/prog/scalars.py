"""Numerical sanity check of the scalar inequalities used in LIMINF.md (h1-liminf, T86).

PREDICATES (fixed before the first run). Notation: r_nu(x) = I_{nu+1}(x)/I_nu(x),
kappa_n(b) = I_{n+1}(b)/I_1(b) = prod_{nu=1}^{n} r_nu(b), M = floor(m sqrt(b)).
Grid G: nu, n in 0..400; x, b in XS below.
 Q0 (validation, known values): I_1(1)/I_0(1) = 0.4463899659 and I_1(10)/I_0(10) = 0.9485998259
    (A&S Table 9.8 values; tolerance 1e-9), and r_0 agrees with np.i0'(x)/np.i0(x)
    (central difference h=1e-5, tolerance 1e-7 relative: O(h^2) truncation plus 1e-16/h rounding) for x<=50.
 Q1 (A) r_nu(x) >= x/(nu+1+sqrt((nu+1)^2+x^2))               for all (nu,x) in G.
 Q2 (B) r_nu(x) <= x/(nu+1/2+sqrt((nu+1/2)^2+x^2))           for all (nu,x) in G.
 Q3 (C) n(n+2)/(2(b+n+1/2)) <= -ln kappa_n(b) <= n(n+3)/(2b)  for all (n,b) in G.
 Q4 (low set) for m in MS, b in XS with b>=100, 0<=n1,n2<=M:
     1-kappa_{n1}kappa_{n2} >= (b/(b+M+1/2)) (1/(1+m^2+3m/sqrt b)) (n1(n1+2)+n2(n2+2))/(2b).
 Q5 (high set) for m in MS, b>=100, n1 in M+1..400 (n2 arbitrary in 0..400):
     1-kappa_{n1}kappa_{n2} >= 1-exp(-(M+1)(M+3)/(2(b+M+3/2))) =: c(m,b).
 Q6 (S7 minimisation) 4s - 8su + 4s^2u^2 >= 4s - 4 for s in [0,50], u in [0,1] (2001x2001 grid).
 Q7 (chart) sin(a)^2 >= a^2(1-a^2/2) and sin(a) <= a, a in (0,1] (10^5 points).
Comparison tolerance for Q1-Q5: a predicate lhs >= rhs is met if lhs >= rhs - 1e-10*max(1,|rhs|).
Source of tolerance: double precision recurrence, <= ~1e3 operations per value at eps 1.1e-16,
 so accumulated relative error <~ 1e-12; 1e-10 is a 100x margin. Q6/Q7: exact-arithmetic-level tolerance 1e-12.
Deterministic: no randomness (seed fixed at 0 for form's sake).
Output: results/scalars.json opened with mode "x". Exit 0 iff every predicate met.
"""
import json, math, sys
import numpy as np
np.random.seed(0)
XS = [0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
MS = [0.05, 0.1, 0.2, 0.3]
NMAX = 400
TOL = 1e-10

def ratios(x, nmax=NMAX):
    """r_nu(x), nu = 0..nmax, by backward recurrence r_nu = 1/(2(nu+1)/x + r_{nu+1})."""
    N = nmax + 200 + int(4 * x)
    nu = N + 1
    r = x / (nu + 1 + math.sqrt((nu + 1) ** 2 + x * x))  # start value; errors damp
    out = [0.0] * (nmax + 1)
    for v in range(N, -1, -1):
        r = 1.0 / (2.0 * (v + 1) / x + r)
        if v <= nmax:
            out[v] = r
    return np.array(out)

res = {"predicates": {}}
def record(name, met, failed, worst, where):
    res["predicates"][name] = {"met": met, "failed": failed, "min_slack": worst, "where": where}
    print(name, "met", met, "failed", failed, "min_slack", worst, "at", where, flush=True)

# Q0
ok = 0; bad = 0
for x, ref in [(1.0, 0.4463899659), (10.0, 0.9485998259)]:
    v = ratios(x, 5)[0]
    if abs(v - ref) < 1e-9: ok += 1
    else: bad += 1; print("Q0 fail", x, v, ref)
for x in [0.5, 1, 2, 5, 10, 20, 50]:
    h = 1e-5
    d = (np.i0(x + h) - np.i0(x - h)) / (2 * h) / np.i0(x)
    v = ratios(x, 5)[0]
    if abs(v - d) / d < 1e-7: ok += 1
    else: bad += 1; print("Q0 fail i0", x, v, d)
record("Q0", ok, bad, None, None)

R = {x: ratios(x) for x in XS}
LK = {x: np.concatenate([[0.0], np.cumsum(-np.log(R[x][1:]))]) for x in XS}  # -ln kappa_n, n=0..400

for name, fn in [("Q1", lambda nu, x: (R[x][nu] - x / (nu + 1 + math.sqrt((nu + 1) ** 2 + x * x)))),
                 ("Q2", lambda nu, x: (x / (nu + .5 + math.sqrt((nu + .5) ** 2 + x * x)) - R[x][nu]))]:
    met = failed = 0; worst = (math.inf, None)
    for x in XS:
        for nu in range(NMAX + 1):
            s = fn(nu, x)
            if s >= -TOL: met += 1
            else: failed += 1
            rel = s / R[x][nu]
            if rel < worst[0]: worst = (rel, [nu, x])
    record(name, met, failed, worst[0], worst[1])

met = failed = 0; worst = (math.inf, None)
for b in XS:
    for n in range(NMAX + 1):
        y = LK[b][n]; lo = n * (n + 2) / (2 * (b + n + .5)); hi = n * (n + 3) / (2 * b)
        for s, rhs in [(y - lo, lo), (hi - y, hi)]:
            if s >= -TOL * max(1, rhs): met += 1
            else: failed += 1
            if n > 0 and s / max(rhs, 1e-300) < worst[0]: worst = (s / rhs, [n, b])
record("Q3", met, failed, worst[0], worst[1])

met = failed = 0; worst = (math.inf, None); met5 = failed5 = 0; worst5 = (math.inf, None)
for m in MS:
    for b in [b for b in XS if b >= 100]:
        M = int(math.floor(m * math.sqrt(b)))
        kap = np.exp(-LK[b])
        fac = (b / (b + M + .5)) / (1 + m * m + 3 * m / math.sqrt(b))
        for n1 in range(M + 1):
            for n2 in range(M + 1):
                lhs = 1 - kap[n1] * kap[n2]
                rhs = fac * (n1 * (n1 + 2) + n2 * (n2 + 2)) / (2 * b)
                if lhs >= rhs - TOL * max(1, rhs): met += 1
                else: failed += 1
                if rhs > 0 and (lhs - rhs) / rhs < worst[0]: worst = ((lhs - rhs) / rhs, [m, b, n1, n2])
        c = 1 - math.exp(-(M + 1) * (M + 3) / (2 * (b + M + 1.5)))
        lhs = 1 - kap[M + 1] * kap.max()  # worst n2 is the one with largest kappa (n2=0)
        for n1 in range(M + 1, NMAX + 1):
            for n2 in range(NMAX + 1):
                l = 1 - kap[n1] * kap[n2]
                if l >= c - TOL: met5 += 1
                else: failed5 += 1
                if (l - c) / c < worst5[0]: worst5 = ((l - c) / c, [m, b, n1, n2])
record("Q4", met, failed, worst[0], worst[1])
record("Q5", met5, failed5, worst5[0], worst5[1])

s = np.linspace(0, 50, 2001)[:, None]; u = np.linspace(0, 1, 2001)[None, :]
d = 4 * s - 8 * s * u + 4 * s * s * u * u - (4 * s - 4)
record("Q6", int((d >= -1e-12).sum()), int((d < -1e-12).sum()), float(d.min()), None)
a = np.linspace(1e-5, 1, 100000)
d1 = np.sin(a) ** 2 - a * a * (1 - a * a / 2); d2 = a - np.sin(a)
record("Q7", int((d1 >= -1e-12).sum() + (d2 >= -1e-12).sum()), int((d1 < -1e-12).sum() + (d2 < -1e-12).sum()),
       float(min(d1.min(), d2.min())), None)

allok = all(v["failed"] == 0 for v in res["predicates"].values())
res["all_met"] = allok
with open(sys.argv[1] if len(sys.argv) > 1 else "results/scalars.json", "x") as fh:
    json.dump(res, fh, indent=1)
sys.exit(0 if allok else 1)
