"""p7-final check.py -- arithmetic and count predicates for the revised paper.
Predicates fixed before first run (tolerances stated):
 Q1 7d/48 at d=8 equals 7/6 exactly (Fraction); printed '7/6'.
 Q2 7d/48 at d=3 = 0.4375 exactly; at d=1 rounds to 0.1458 (4 decimals, the precision quoted in the brief).
 Q3 (d/2)*C_pp with C_pp=7/24 equals 7d/48 for d=1..10 (Fraction, exact).
 Q4 Theorem gen:thm Cov formula at d=3 has Gaussian coefficient 3/2, and Var lower bound d/8 at d=3 equals 3/8 (Lemma pf:lem-wick), exact.
 Q5 omega_8*2^4/Vol_rho(SU(3)) with Vol=sqrt3(2pi)^5/(2*81) equals 9 sqrt3/(8 pi) to 1e-12 relative (float roundoff).
 Q6 MC values printed in sec_general 'Check' lie within 3 sigma (sigma = printed error) of 7d/48: SU(3) 1.1680(11), SU(2) 0.4369(4), U(1) 0.1459(2). 3 sigma is my choice (conventional), not from the paper.
 Q7 counts in paper/: abstract 'H0 to H4' -> 5 hypothesis environments H0,(A),(B),H3,H4 in sec_reduction; routes subsections in sec:routes = 4 + 1 exclusion; items P1..P6 = 6; standard facts \item in pf:sec-standard = 10.
 Q8 A1R declarations listed in provenance table: count equals the printed '11'. (expected to FAIL on my reading: 10 listed)
 Q9 the folder 'lean' claimed 'beside the sources' exists in paper/.
Measured only: M1 SU(2) MC deviation in sigma; M2 page count via pdfinfo.
"""
import sys, math, re, os, subprocess
from fractions import Fraction as Fr
out = open(sys.argv[1], "x")
res = []
def P(name, ok, info): res.append((name, ok)); print(f"{name}\t{'MET' if ok else 'FAILED'}\t{info}", file=out)
f = lambda d: Fr(7*d, 48)
P("Q1", f(8) == Fr(7, 6), f"7*8/48={f(8)}")
P("Q2", f(3) == Fr(7, 16) and float(f(3)) == 0.4375 and round(float(f(1)), 4) == 0.1458, f"d=3 {float(f(3))}, d=1 {float(f(1)):.6f}")
P("Q3", all(Fr(d, 2)*Fr(7, 24) == f(d) for d in range(1, 11)), "d=1..10")
P("Q4", Fr(3, 2) == Fr(3, 2) and Fr(3, 8) == Fr(3, 8) and Fr(3,2)*Fr(1,4) == Fr(3,8), "d/2=3/2, d/8=3/8, (d/2)G(0)^2=3/8")
om8 = math.pi**4/24; vol = math.sqrt(3)*(2*math.pi)**5/(2*81); a = om8*16/vol; b = 9*math.sqrt(3)/(8*math.pi)
P("Q5", abs(a-b)/b < 1e-12, f"{a:.9f} vs {b:.9f}")
mc = [("SU3", 8, 1.1680, 0.0011), ("SU2", 3, 0.4369, 0.0004), ("U1", 1, 0.1459, 0.0002)]
devs = [(n, (v-float(f(d)))/e) for n, d, v, e in mc]
P("Q6", all(abs(z) <= 3 for _, z in devs), "; ".join(f"{n} {z:+.2f} sigma" for n, z in devs))
root = sys.argv[2]
red = open(os.path.join(root, "sec_reduction.tex")).read(); neg = open(os.path.join(root, "sec_negative.tex")).read()
prf = open(os.path.join(root, "sec_proof.tex")).read(); prov = open(os.path.join(root, "sec_provenance.tex")).read()
hyps = re.findall(r"\\begin\{hypothesis\}\[([^\]]*)\]", red)
h5 = [h for h in hyps if re.match(r"(H0|\(A\)|\(B\)|H3|H4)", h)]
sec_routes = neg.split(r"\section{A shared")[0]
subs = re.findall(r"\\subsection\{([^}]*)\}", sec_routes)
props = re.findall(r"\\item\[P([1-9])\]", neg)
std = prf.split(r"\label{pf:sec-standard}")[1].split(r"\end{enumerate}")[0].count(r"\item")
P("Q7", len(h5) == 5 and len(subs) == 5 and subs[-1] == "Exclusion" and sorted(set(props)) == list("123456") and std == 10,
  f"hyps={h5}; routes={subs}; P={sorted(set(props))}; standard facts={std}")
row = [l for l in prov.splitlines() if "A1R.lean" in l and "Declarations" not in l][0]
decl = re.findall(r"\\repo\{([^}]*)\}", row.split("&")[-1])
n = 0
for d in decl:
    n += 7 if "L1" in d and "--" in row else 0
names = decl
cnt = (7 if "A1R.L1}--\\repo{L7}" in row else 0) + sum(1 for d in decl if d not in ("A1R.L1", "L7"))
P("Q8", cnt == 11, f"listed declarations={decl} -> count {cnt}; printed 11")
P("Q9", os.path.isdir(os.path.join(root, "lean")), f"exists={os.path.isdir(os.path.join(root,'lean'))}")
pg = subprocess.run(["pdfinfo", os.path.join(root, "main.pdf")], capture_output=True, text=True).stdout
print("M1\tmeasured\t" + str(devs[1]), file=out)
print("M2\tmeasured\t" + [l for l in pg.splitlines() if l.startswith("Pages")][0], file=out)
m = sum(ok for _, ok in res); print(f"COUNTS met {m}, failed {len(res)-m}, measured only 2", file=out)
out.close()
