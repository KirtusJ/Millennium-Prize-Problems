"""j1-micro arithmetic check of numbers in A3_NOTES.md sec 7-10 and sec_smallbox.tex.
Inputs are the record values (copied by hand, file:line in comments). Deterministic, no randomness.
Predicates fixed before the first run. Tolerance = half a unit of the last digit of the CLAIMED
number (source: the claim's own rounding) unless stated otherwise.
 P1  6.534885/4^(1/3) rounds to 4.1167196                               (tol 5e-8)
 P2  3.012539/4^(1/3) -> 1.89778 ; 3.602838/4^(1/3) -> 2.26965           (tol 5e-6)
 P3  |4.116719735 - 6.534885/4^(1/3)| rounds to 1.5e-7 and < 0.5e-6/4^(1/3)
 P4  5.3254970-3.3505330 = 1.974964                                       (tol 5e-7)
 P5  log(l0/l1)*beta^(1/3), h1-a4 table l.164-169 -> 1.636,1.760,1.837,1.887,1.919,1.939 (tol 5e-4)
 P6  at beta=1024 (1-l_j)/h is 16..23 % below e_j (each rounds into [16,23]) and -log l_j/h within 1.3 % (<=1.35)
 P7  3D m_e*beta^(1/3): 2.876117,1.621505,0.968930 -> 2.88,2.04,1.54        (tol 5e-3)
 P8  MC deviations at 4096 -> -0.7,-0.8,-1.6 %                             (tol 0.05)
 P9  (1.9019-1.887)/0.0084 -> 1.8                                          (tol 0.05)
 P10 c=int_0^pi sqrt(2 eps) = 4.6054132 (5e-8); d=int 1/sqrt(2 eps)=2.6828 (5e-5); 3.3505330*d -> 8.99 (5e-3);
     continuous-time 2*int sqrt(sin) = 4.7926 (5e-5). eps = 2 asinh(sin a). Quadrature: Gauss-Legendre after
     a=(pi/2)u^2 on [0,pi/2], symmetric; n=300 vs 600 must agree to 1e-10 (own convergence tolerance).
 P11 q: (8.99-8.1)/8.99 and (8.99-8.1)/8.1 vs "about 12 per cent": predicate = at least one rounds to 12 (tol 0.5)
 P12 brief size estimates 1e-18,1e-24,1e-30 vs measured 1.45974e-16,4.12662e-21,5.40315e-25 (i1-tunnel l.38-40):
     claim "too small by up to five orders": predicate = max log10 ratio rounds to 5 (in [4.5,5.5))
 P13 residual ratio c=4.7926 forced vs 4.6054 (i1-tunnel l.53,56): "five to six times" -> ratio in [4.5,6.5) for beta>=64 and >=96
 P14 E-T2 splitting at beta=1024: 0.018+-0.011 "zero within errors": predicate |x|/err <= 1
 P15 box scaling: A=2 s Y, s=(bL^3)^(-1/3): H coefficients equal s*(1/2) kinetic, s*2 potential (rel 1e-12)
 P16 Luescher normalisation Y=4^(-1/6)c gives h3 = 4^(1/3)*(-1/2 Lap + 1/2 |cxc|^2) (rel 1e-12)
 P17 beta^(-3/2) h^(-3) = h^(3/2) with h=beta^(-1/3) (exponent arithmetic, exact rationals)
 P18 m_oo/m_eo "2.00000" for beta 96..256: values 2.00000,2.00000,2.00000,1.99998 (i1-tunnel l.37-40), all must equal 2.00000
"""
import json, math, sys
from fractions import Fraction as F
import numpy as np

R = []
def rec(name, ok, val, note=""):
    R.append(dict(name=name, ok=bool(ok), value=val, note=note))
    print(("MET   " if ok else "FAILED"), name, val, note)

c4 = 4 ** (1 / 3)
v = 6.534885 / c4; rec("P1", abs(v - 4.1167196) <= 5e-8, f"{v:.9f}")
v2, v3 = 3.012539 / c4, 3.602838 / c4
rec("P2", abs(v2 - 1.89778) <= 5e-6 and abs(v3 - 2.26965) <= 5e-6, f"{v2:.7f} {v3:.7f}")
d = abs(4.116719735 - v); rec("P3", round(d, 8) == 1.5e-7 and d < 0.5e-6 / c4, f"{d:.3e} bound {0.5e-6/c4:.3e}")
rec("P4", abs(5.3254970 - 3.3505330 - 1.974964) <= 5e-7, f"{5.3254970-3.3505330:.7f}")
tab = {32: 0.5151641763, 64: 0.4399423291, 128: 0.3645007923, 256: 0.2971232997, 512: 0.2398232122, 1024: 0.1923831345}
claim = {32: 1.636, 64: 1.760, 128: 1.837, 256: 1.887, 512: 1.919, 1024: 1.939}
vals = {b: tab[b] * b ** (1 / 3) for b in tab}
rec("P5", all(abs(vals[b] - claim[b]) <= 5e-4 for b in tab), {b: round(vals[b], 5) for b in vals})
e0, e1 = 3.350533, 5.325497
lo = [(1 - 2.82763 / e0) * 100, (1 - 4.09675 / e1) * 100]; lg = [(1 - 3.31863 / e0) * 100, (1 - 5.25773 / e1) * 100]
rec("P6", all(15.5 <= x < 23.5 for x in lo) and max(lg) <= 1.35, f"below {lo[0]:.2f}%,{lo[1]:.2f}%; log-form {lg[0]:.2f}%,{lg[1]:.2f}%")
m3 = [2.876117 * 1, 1.621505 * 2 ** (1 / 3), 0.968930 * 4 ** (1 / 3)]
rec("P7", all(abs(a - b) <= 5e-3 for a, b in zip(m3, [2.88, 2.04, 1.54])), [round(x, 4) for x in m3])
pc = [(2.992 / 3.0125 - 1) * 100, (2.989 / 3.0125 - 1) * 100, (3.544 / 3.6028 - 1) * 100]
rec("P8", all(abs(a - b) <= 0.05 for a, b in zip(pc, [-0.7, -0.8, -1.6])), [round(x, 3) for x in pc])
z = (1.9019 - 1.887) / 0.0084; rec("P9", abs(z - 1.8) <= 0.05, f"{z:.3f}")
def integ(f, n):
    x, w = np.polynomial.legendre.leggauss(n); u = (x + 1) / 2; w = w / 2
    a = (math.pi / 2) * u ** 2
    return 2 * float(np.sum(w * f(a) * math.pi * u))
eps = lambda a: 2 * np.arcsinh(np.sin(a))
I = {}
for k, f in [("c", lambda a: np.sqrt(2 * eps(a))), ("d", lambda a: 1 / np.sqrt(2 * eps(a))), ("cct", lambda a: 2 * np.sqrt(np.sin(a)))]:
    I[k] = (integ(f, 600), abs(integ(f, 600) - integ(f, 300)))
conv = all(I[k][1] <= 1e-10 for k in I)
c, dd, cct = I["c"][0], I["d"][0], I["cct"][0]
rec("P10", conv and abs(c - 4.6054132) <= 5e-8 and abs(dd - 2.6828) <= 5e-5 and abs(3.3505330 * dd - 8.99) <= 5e-3 and abs(cct - 4.7926) <= 5e-5,
    f"c={c:.9f} d={dd:.7f} E0d={3.350533*dd:.4f} cct={cct:.7f} conv={[I[k][1] for k in I]}")
r1, r2 = (8.99 - 8.1) / 8.99 * 100, (8.99 - 8.1) / 8.1 * 100
rec("P11", abs(r1 - 12) <= 0.5 or abs(r2 - 12) <= 0.5, f"{r1:.2f}% / {r2:.2f}%; with q=-7.9 (record l.100): {(8.99-7.9)/8.99*100:.2f}%; with -8.08 vs -8.989: {(8.989-8.08)/8.989*100:.2f}%")
ratios = [math.log10(m / e) for m, e in [(1.45974e-16, 1e-18), (4.12662e-21, 1e-24), (5.40315e-25, 1e-30)]]
rec("P12", 4.5 <= max(ratios) < 5.5, [round(x, 2) for x in ratios])
rr = [3.9e-3 / 7.7e-4, 1.4e-3 / 2.4e-4, 1.2e-2 / 3.4e-3]
rec("P13", all(4.5 <= x < 6.5 for x in rr[:2]), [round(x, 2) for x in rr], "beta>=64, >=96 (beta>=32 shown for info)")
rec("P14", 0.018 / 0.011 <= 1, f"{0.018/0.011:.2f} sigma at 1024; {0.037/0.012:.2f} at 256; {-0.003/0.018:.2f} at 4096")
for bL3 in [7.0, 1000.0]:
    s = bL3 ** (-1 / 3); kin = (2 / bL3) / (2 * s) ** 2; pot = (bL3 / 8) * (2 * s) ** 4
    ok15 = abs(kin / (s * 0.5) - 1) < 1e-12 and abs(pot / (s * 2) - 1) < 1e-12
rec("P15", ok15, "kinetic and quartic coefficients = s/2, 2s")
a = 4 ** (-1 / 6); kin, pot = 0.5 / a ** 2, 2 * a ** 4
rec("P16", abs(kin / 0.5 / c4 - 1) < 1e-12 and abs(pot / 0.5 / c4 - 1) < 1e-12, f"scale {kin/0.5:.12f} {pot/0.5:.12f} vs 4^(1/3)={c4:.12f}")
ex = F(-3, 2) * F(-3, 1) * F(1, 1)  # beta^(-3/2) = h^(9/2)
rec("P17", F(9, 2) - 3 == F(3, 2), str(F(9, 2) - 3))
rec("P18", all(x == "2.00000" for x in ["2.00000", "2.00000", "2.00000", "1.99998"]), "values 2.00000 x3, 1.99998 at 256")
out = sys.argv[1]
with open(out, "x") as fh:
    json.dump(R, fh, indent=1)
nm = sum(r["ok"] for r in R); print(f"met {nm}, failed {len(R)-nm}")
sys.exit(0 if nm == len(R) else 1)
