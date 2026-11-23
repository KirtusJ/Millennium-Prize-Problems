"""numcheck.py -- consistency of the numbers used in paper/sec_smallbox.tex (task T99).

Inputs are transcribed by hand from the input files (line numbers given).
Predicates (fixed before the first run):
 P1  for each beta in 32..1024: |log(lam0/lam1)*beta^(1/3) [crossreview.md l.164-169]
       - m_e beta^(1/3) [A3_NOTES.md l.85]| <= 6e-4.  Tolerance: A3_NOTES prints 3 decimals
       (rounding 5e-4) plus 1e-4 for the cube root.
 P2  e1 - e0 (numerics2 l.14-15: 3.3505330, 5.3254970) equals 1.974964 within 1e-6 (7-decimal
       rounding of two numbers: 1e-7 each, 1.974964 printed to 6 decimals: 5e-7).
 P3  6.534885 * 4^(-1/3) equals 4.1167196 within 3.5e-7 (6.534885 rounded at 5e-7, times 0.63;
       4.1167196 rounded at 5e-8)  [numerics3 l.164, A3_NOTES l.116, grounding l.10].
 P4  |4.1167196 - 4.116719735| <= 3.5e-7 (same rounding budget) [grounding l.10].
 P5  3.012539 * 4^(-1/3) and 3.602838 * 4^(-1/3) equal 1.89778, 2.26965 within 1e-5
       (A3_NOTES l.116 prints 5 decimals; numerics3 l.244 prints 2.26964 -- both tested).
 P6  three directions: m_e beta^(1/3) at beta=1,2,4 from m_e (numerics3 l.225-227) equals
       2.88, 2.04, 1.54 within 5e-3 (2-decimal rounding).
 P7  heuristic rescaling: with s = 2 (b L^3)^(-1/3), (2/(bL^3))/s^2 == 1/2 * (bL^3)^(-1/3) and
       (bL^3/8) s^4 == 2 (bL^3)^(-1/3), for 20 random (b,L) (seed 7), rel tol 1e-12 (float).
Measured only: the fit limit 1.97496 is not recomputed (no 4-point data beyond 3 decimals).
Exit code: number of failed predicates.
"""
import json, math, random, sys
out = sys.argv[1]
res = {"met": [], "failed": [], "measured": []}
def P(name, ok, info):
    (res["met"] if ok else res["failed"]).append({"p": name, "info": info})
betas = [32, 64, 128, 256, 512, 1024]
logr = [0.5151641763, 0.4399423291, 0.3645007923, 0.2971232997, 0.2398232122, 0.1923831345]
a3 = [1.636, 1.760, 1.837, 1.887, 1.919, 1.939]
for b, l, a in zip(betas, logr, a3):
    v = l * b ** (1 / 3)
    P(f"P1 beta={b}", abs(v - a) <= 6e-4, f"{v:.5f} vs {a}")
    res["measured"].append({"beta": b, "m_e*beta^1/3": round(v, 6)})
g = 5.3254970 - 3.3505330
P("P2", abs(g - 1.974964) <= 1e-6, f"{g:.7f}")
c = 4 ** (-1 / 3)
P("P3", abs(6.534885 * c - 4.1167196) <= 3.5e-7, f"{6.534885*c:.8f}")
P("P4", abs(4.1167196 - 4.116719735) <= 3.5e-7, f"{4.1167196-4.116719735:.2e}")
for v, t in [(3.012539, 1.89778), (3.602838, 2.26965), (3.602838, 2.26964)]:
    P(f"P5 {v}->{t}", abs(v * c - t) <= 1e-5, f"{v*c:.7f}")
for b, m, t in [(1, 2.876117, 2.88), (2, 1.621505, 2.04), (4, 0.968930, 1.54)]:
    P(f"P6 beta={b}", abs(m * b ** (1 / 3) - t) <= 5e-3, f"{m*b**(1/3):.4f}")
random.seed(7)
ok = True
for _ in range(20):
    b, L = random.uniform(1, 1e4), random.randint(1, 64)
    N = b * L ** 3; s = 2 * N ** (-1 / 3)
    ok &= math.isclose((2 / N) / s ** 2, 0.5 * N ** (-1 / 3), rel_tol=1e-12)
    ok &= math.isclose((N / 8) * s ** 4, 2 * N ** (-1 / 3), rel_tol=1e-12)
P("P7", ok, "20 random cases")
with open(out, "x") as f:
    json.dump(res, f, indent=1)
print(f"met {len(res['met'])}, failed {len(res['failed'])}, measured only {len(res['measured'])}")
for r in res["failed"]: print("FAILED", r)
sys.exit(len(res["failed"]))
