"""fidcheck.py -- p5-fid (T29) recomputation of the arithmetic the front matter / provenance rely on.

Predicates (fixed before the first run):
 Q1  G(0) = 1/2 within 1e-6          (tolerance: quadrature error estimate, compared at two grid sizes)
 Q2  G(1) = 0.0688747 within 1e-6    (value from src/a8-chalB2.report.md row 12; tol = its print rounding 5e-8 + quadrature)
 Q3  G(n) > 0 for every n in 1..16   ("for all": per-case count reported)
 Q4  |pi^2 n^4 G(n) - 1| decreasing in n for n=4..16 and < 0.05 at n=16  (paper: G = pi^-2 n^-4 + O(n^-6);
     a5-chalB reports pi^2 n^4 G -> 1.020 at n=16; 0.05 is my margin)
 Q5  D* = 48 + 3 log((pi/2)^(5/2) 2^(3/2)) - 3 log c_H, c_H = 2 sin^2(1)/(3 pi), equals 60.1922 within 1e-4
     (paper sec_proof.tex:174; tol = 4th decimal printed)
 Q6  1 - cos x >= 2 x^2/pi^2 on a 200001-point grid of [-pi, pi] (provenance Lean table; per-case count)
 Q7  number of \\section commands in the assembled paper == 8 (my count, = child's control)
 Q8  challenger verdict counts as printed in src reports:
       a2-chalR "STANDS 16 / DEFECT 8 / NOT CHECKED 1"; a5-chalB "STANDS 17, DEFECT 1, NOT CHECKED 1";
       a8-chalB2 "STANDS 12, DEFECT 2, NOT CHECKED 2"; a9 "11 STANDS, 1 DEFECT"; c2 "12 STANDS, 3 DEFECT, 2 NOT CHECKED"
 Q9  A1_LEDGER micro-review: "6 wrong, 10 overstated, 3 unsupported and 9 omitted" present verbatim.
 Q10 paper sec_paperreview.tex has non-placeholder content (paper claims the review was done).
Seeds: none needed (deterministic quadrature). Result file opened with mode "x".
"""
import math, re, sys, os
import numpy as np

out = open(sys.argv[1], "x")
def w(s):
    print(s); out.write(s + "\n")
res = {}
def pred(name, ok, msg):
    res[name] = ok; w(f"{name}: {'MET' if ok else 'FAILED'}  {msg}")

def Gvals(N, nmax=16):
    x, wt = np.polynomial.legendre.leggauss(N)
    u = 0.5 * (x + 1); wu = 0.5 * wt
    k = math.pi * u**2; wk = 2 * math.pi * u * wu   # k in [0,pi], graded toward 0
    s2 = 4 * np.sin(k / 2) ** 2
    S1, S2, S3 = np.meshgrid(s2, s2, s2, indexing="ij")
    W = wk[:, None, None] * wk[None, :, None] * wk[None, None, :] * 8 / (2 * math.pi) ** 3
    a = S1 + S2 + S3
    m = 2 * np.arcsinh(np.sqrt(a) / 2)   # run2: arccosh(1+a/2) underflowed to 0 near k=0 (my defect in run1)
    base = W * (S1 + S2) / (2 * np.sinh(m))
    return [float(np.sum(base * np.exp(-m * n))) for n in range(nmax + 1)]

GA = Gvals(120); GB = Gvals(180)
for n in range(17):
    w(f"n={n:2d} G={GB[n]:.10f} diff(120,180)={abs(GA[n]-GB[n]):.2e} pi2n4G={math.pi**2*n**4*GB[n]:.6f}")
pred("Q1", abs(GB[0] - 0.5) < 1e-6, f"G(0)={GB[0]:.10f}")
pred("Q2", abs(GB[1] - 0.0688747) < 1e-6, f"G(1)={GB[1]:.10f}")
pos = sum(1 for n in range(1, 17) if GB[n] > 0)
pred("Q3", pos == 16, f"{pos}/16 cases qualify")
r = [abs(math.pi**2 * n**4 * GB[n] - 1) for n in range(4, 17)]
dec = all(r[i+1] < r[i] for i in range(len(r)-1))
pred("Q4", dec and r[-1] < 0.05, f"|pi^2n^4G-1| n=4..16: {[round(v,4) for v in r]}")
cH = 2 * math.sin(1) ** 2 / (3 * math.pi)
Ds = 48 + 3 * math.log((math.pi / 2) ** 2.5 * 2 ** 1.5) - 3 * math.log(cH)
pred("Q5", abs(Ds - 60.1922) < 1e-4, f"c_H={cH:.6f} D*={Ds:.6f}")
xs = np.linspace(-math.pi, math.pi, 200001)
okc = int(np.sum(1 - np.cos(xs) >= 2 * xs**2 / math.pi**2 - 1e-15))
pred("Q6", okc == xs.size, f"{okc}/{xs.size} grid points qualify (slack 1e-15 = float rounding)")
P = sys.argv[2]; S = sys.argv[3]
def rd(p): return open(p, encoding="utf-8").read()
nsec = 0
for f in ["main.tex", "sec_reduction.tex", "sec_proof.tex", "sec_negative.tex", "sec_provenance.tex", "sec_paperreview.tex"]:
    t = "\n".join(l for l in rd(os.path.join(P, f)).splitlines() if not l.lstrip().startswith("%"))
    nsec += len(re.findall(r"\\section\{", t))
pred("Q7", nsec == 8, f"sections={nsec}")
pats = {"a2-chalR.report.md": "STANDS 16 / DEFECT 8 / NOT CHECKED 1", "a5-chalB.report.md": "STANDS 17, DEFECT 1, NOT CHECKED 1",
        "a8-chalB2.report.md": "STANDS 12, DEFECT 2, NOT CHECKED 2", "a9-chalL34.report.md": "11 STANDS, 1 DEFECT",
        "c2-chalS.report.md": "12 STANDS, 3 DEFECT, 2 NOT CHECKED"}
for f, p in pats.items():
    pred("Q8:" + f, p in rd(os.path.join(S, f)), f"'{p}'")
pred("Q9", "6 wrong, 10 overstated, 3 unsupported and 9 omitted" in rd(os.path.join(S, "A1_LEDGER.md")), "ledger micro-review counts")
pr = rd(os.path.join(P, "sec_paperreview.tex")).strip()
pred("Q10", "to be filled" not in pr and len(pr) > 80, f"sec_paperreview.tex = {pr!r}")
met = sum(res.values()); w(f"TOTAL met {met}, failed {len(res)-met}, measured only 17 (G table rows)")
out.close()
