"""r14-micro arithmetic recheck of the numbers the summaries compute themselves.

Predicates fixed before the first run (claimed value from SPATIAL_FLOW.md / MATCHED_MEASUREMENT.md;
tolerance = half a unit of the last quoted digit, from the rounding convention of the quoted number,
unless stated otherwise):
 Q1  6*0.3690 = 2.214 ; 12*0.1905 = 2.286                                   (tol 5e-4)
 Q2  mismatch 12*0.1905/(6*0.3690)-1 = +3.25 %  (tol 0.005 %); its error 0.94 % (tol 0.005 %),
     relative errors 30/3690 and 8/1905 in quadrature, times the ratio
 Q3  a^2/(8s): s/a^2=0.5 -> 0.25, s/a^2=2 -> 0.0625 (exact); sqrt(8s)/a -> 2, 4 (exact)
 Q4  s=l^2/72: sqrt(6s)/l = 0.29 (tol 0.005); s/a^2 = 0.5 (l=6a), 2.0 (l=12a) (exact)
 Q5  ratios: R(0) 0.913(33), R(l/6) 0.494(67), Q0 0.956(12) (value tol 5e-4, error tol 5e-4)
 Q6  Q0 differs 4.4 % (tol 0.05) at 3.6 sigma (tol 0.05, ratio form); R(0) 9 % (tol 0.5) at 2.7 sigma
     (tol 0.05, ratio form); R(l/6) "factor of two" (ratio in [0.45,0.55]) at 7.6 sigma (tol 0.05, ratio form)
 Q7  (2.214/2.286)^3 = 0.91 (tol 0.005)
 Q8  coarse significances 88, 31, 11 (tol 0.5 on the rounded table values; result file gives 88.3, 31.2, 10.9)
 Q9  -2.0(1.1)e-3 is within two standard errors: |-2.0|/1.1 < 2
 Q10 strong coupling 1-I2(0.5)/I1(0.5) = 0.876282 (tol 5e-7), series for I_n
 Q11 sqrt(pi)/(640 pi^2) = 0.00028060 to 8 decimals; brief value 0.00028061 differs (expected: differs)
 Q12 cosh effective mass, T=6, from R(1)=1.012e-2, R(2)=3.652e-3 (result-file values): m/0.3690 = 3.01 (tol 0.005)
 Q13 grid 0..50 step 0.05 inclusive has 1001 points (exact)
 Q14 160 configs / 8 blocks: block 19 in result file -> 8 blocks of 19 = 152 <= 160 (consistency, exact)
 Q15 seeds disagree "by five of the quoted errors": (29.6-14.4)/sqrt(2.2^2+2.4^2) in [4.5,5.5]
 Q16 extension: ratios 0.498(54) and 0.972(11) equal results_2 0.4982+-0.0536, 0.9718+-0.0109 (tol 5e-4)
 Q17 5/8 * sqrt(pi)/(640 pi^2) = 1.754e-4 (tol 5e-8)
 Q18 tree ratios: (1/(32pi^2))/(3/(256pi^2)) = 8/3, (1/(32pi^2))/(3/(128pi^2)) = 4/3 (exact to 1e-12)
 Q19 magnetic "to 0.25 per cent": |0.006317/(3/(48pi^2)) - 1| <= 0.0025 at tau=8 ; also report the other taus
     (0.006591, 0.006342, 0.006249) -- measured only
 Q20 t>0 bound range: summary "1e-3 to 1e-13" vs volchal "1e-3 to 2e-2 (t=0.02); 1e-13 to 4e-8 (t=0.1)":
     predicate: summary's upper end >= report's max (2e-2). Expected to FAIL (summary drops 2e-2).
 Q21 counts 25+1+8 = 34 ; 18 of 18 ; 21 of 23 items ; 9 of 9 controls  -- consistency only
 Q22 strong-coupling diff in sigma (0.875486-0.876282)/0.000760 ~ -1.0 (tol 0.05)
 Q23 plaquette diffs in combined sigma: (0.602953-0.602934)/sqrt(159^2+37^2)e-6 and
     (0.652029-0.651941)/sqrt(160^2+198^2)e-6 -- measured only
Seed: none needed (deterministic).
"""
import math, sys, json

out = open(sys.argv[1], "x")
res = []
def P(name, ok, detail):
    res.append((name, "MET" if ok else "FAILED", detail)); print(name, "MET" if ok else "FAILED", detail, file=out)
def M(name, detail):
    res.append((name, "MEASURED", detail)); print(name, "MEASURED", detail, file=out)

lc, lf = 6*0.3690, 12*0.1905
P("Q1a", abs(lc-2.214) <= 5e-4, f"{lc:.6f}"); P("Q1b", abs(lf-2.286) <= 5e-4, f"{lf:.6f}")
r = lf/lc; mis = 100*(r-1); err = 100*r*math.hypot(30/3690, 8/1905)
P("Q2a", abs(mis-3.25) <= 0.005, f"{mis:.4f}%"); P("Q2b", abs(err-0.94) <= 0.005, f"{err:.4f}%")
P("Q3", [1/(8*0.5), 1/(8*2.0), math.sqrt(8*0.5), math.sqrt(8*2.0)] == [0.25, 0.0625, 2.0, 4.0], "0.25 0.0625 2 4")
P("Q4a", abs(math.sqrt(6/72)-0.29) <= 0.005, f"{math.sqrt(6/72):.5f}")
P("Q4b", 36/72 == 0.5 and 144/72 == 2.0, "0.5 2.0")
def ratio(a, ea, b, eb):
    q = a/b; return q, q*math.hypot(ea/a, eb/b)
for nm, (f, ef, c, ec), (cv, ce) in [("R0", (3.424e-2, 1.2e-3, 3.751e-2, 4.2e-4), (0.913, 0.033)),
                                     ("Rl6", (5.002e-3, 6.6e-4, 1.012e-2, 3.2e-4), (0.494, 0.067)),
                                     ("Q0", (8.927232e-2, 1.10e-3, 9.334673e-2, 2.55e-4), (0.956, 0.012))]:
    q, e = ratio(f, ef, c, ec)
    P("Q5_"+nm, abs(q-cv) <= 5e-4 and abs(e-ce) <= 5e-4, f"{q:.4f}({e:.4f}); (1-q)/e={(1-q)/e:.2f}; diff/sig={abs(c-f)/math.hypot(ef,ec):.2f}")
    if nm == "Q0":
        P("Q6_Q0", abs(100*(1-q)-4.4) <= 0.05 and abs((1-q)/e-3.6) <= 0.05, f"{100*(1-q):.2f}% {(1-q)/e:.2f}sig")
    if nm == "R0":
        P("Q6_R0", abs(100*(1-q)-9) <= 0.5 and abs((1-q)/e-2.7) <= 0.05, f"{100*(1-q):.2f}% {(1-q)/e:.2f}sig")
    if nm == "Rl6":
        P("Q6_Rl6", 0.45 <= q <= 0.55 and abs((1-q)/e-7.6) <= 0.05, f"{q:.3f} {(1-q)/e:.2f}sig")
P("Q7", abs((lc/lf)**3-0.91) <= 0.005, f"{(lc/lf)**3:.4f}")
sg = [3.751e-2/4.2e-4, 1.012e-2/3.2e-4, 3.652e-3/3.4e-4]
P("Q8", all(abs(a-b) <= 0.5 for a, b in zip(sg, [88, 31, 11])), " ".join(f"{x:.2f}" for x in sg))
P("Q9", 2.0/1.1 < 2, f"{2.0/1.1:.3f}")
def I(n, x):
    return sum((x/2)**(2*k+n)/(math.factorial(k)*math.factorial(k+n)) for k in range(40))
sc = 1-I(2, .5)/I(1, .5)
P("Q10", abs(sc-0.876282) <= 5e-7, f"{sc:.7f}")
v = math.sqrt(math.pi)/(640*math.pi**2)
P("Q11", round(v, 8) == 0.00028060 and round(v, 8) != 0.00028061, f"{v:.10f}")
R1, R2 = 1.012e-2, 3.652e-3; tgt = R1/R2
lo, hi = 1e-6, 10.0
for _ in range(200):
    mid = (lo+hi)/2
    if math.cosh(2*mid)/math.cosh(mid) < tgt: lo = mid
    else: hi = mid
P("Q12", abs(lo/0.3690-3.01) <= 0.005, f"m a={lo:.5f}, m/sqrt(sigma)={lo/0.3690:.4f}, m l={6*lo:.4f}; log form {math.log(tgt)/0.3690:.4f}")
P("Q13", len([i for i in range(0, 1001)]) == round(50/0.05)+1 == 1001, "1001")
P("Q14", 8*19 <= 160 < 9*19, "8*19=152")
d = (29.6-14.4)/math.hypot(2.2, 2.4); P("Q15", 4.5 <= d <= 5.5, f"{d:.2f}")
P("Q16", abs(0.4982-0.498) <= 5e-4 and abs(0.0536-0.054) <= 5e-4 and abs(0.9718-0.972) <= 5e-4 and abs(0.0109-0.011) <= 5e-4, "ok")
P("Q17", abs(5/8*v-1.754e-4) <= 5e-8, f"{5/8*v:.5e}")
a, b, c = 1/(32*math.pi**2), 3/(256*math.pi**2), 3/(128*math.pi**2)
P("Q18", abs(a/b-8/3) < 1e-12 and abs(a/c-4/3) < 1e-12, f"{a/b:.6f} {a/c:.6f}; 1/(48pi^2)={1/(48*math.pi**2):.10f}")
ref = 3/(48*math.pi**2)
devs = {t: x/ref-1 for t, x in [(1, 0.006591), (4, 0.006342), (8, 0.006317), (16, 0.006249)]}
P("Q19", abs(devs[8]) <= 0.0025, f"tau=8 {100*devs[8]:+.3f}%")
M("Q19_all", " ".join(f"tau={t}:{100*x:+.2f}%" for t, x in devs.items()))
P("Q20", 1e-3 >= 2e-2, "summary upper end 1e-3 < report max 2e-2")
P("Q21", 25+1+8 == 34 and 21+1+1 == 23, "34, 23")
P("Q22", abs((0.875486-0.876282)/0.000760+1.0) <= 0.05, f"{(0.875486-0.876282)/0.000760:.3f}")
M("Q23", f"{(0.602953-0.602934)/math.hypot(159e-6,37e-6):.2f} {(0.652029-0.651941)/math.hypot(160e-6,198e-6):.2f}")
# extra: R(0) differs "by 9 per cent (2.7)"; extension R(0) ratio
M("X_ext_R0", "results_2 R(0) ratio 0.8802(252), 4.8 sigma (not quoted in summary)")
n = {k: sum(1 for x in res if x[1] == k) for k in ("MET", "FAILED", "MEASURED")}
print(f"COUNTS met {n['MET']} failed {n['FAILED']} measured {n['MEASURED']}", file=out)
out.close()
sys.exit(0)
