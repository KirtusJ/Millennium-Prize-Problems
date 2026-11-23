"""check_traj.py -- C4 trajectory bookkeeping vs asymptotic freedom (C2), fixed before first run.

l = log(2+r). Rows (smoothing.md): m=1: L/(r^3 sqrt l)->inf, beta/(r^16 l)->inf ; m=2: L/(r^2 sqrt l), beta/(r^12 l).
T1 example beta=r^17, L=ceil(r^4): both m=1 ratios increase monotonically over r=10^1..10^6. [monotone = proxy for ->inf]
T2 asymptotic-freedom trajectory beta_AF = (11/(3 pi^2)) log(r) (two-loop omitted; SU(2) one-loop, b0=11*2/(48 pi^2),
   beta=4/g^2=8 b0 log(1/(b Lambda)) with Lambda=1) FAILS both beta conditions: beta/(r^12 l) decreasing and < 1e-10 at r=100.
T3 Ward error of smoothing.md, C[A^{-m/2}+r^2 s^{-12}+A r^{2nu+2} sqrt l/sqrt beta], with the stated choice
   A=min(r, L/(r^nu sqrt l), (sqrt beta/(r^{2nu+2} sqrt l))^{1/2}), s=ceil(A r^{2nu}), on beta=r^17, L=r^4 (m=1, nu=3):
   decreasing in r and < 0.1 at r=10^6 (C set to 1).
T4 "for all beta,L->inf" rate statement (spectrum.md): with r=min(beta^{1/13},L^{1/3}) the m=2 ratios are >= r/l and
   >= r/sqrt(l) resp. Test on 10^4 random (log-uniform) pairs beta,L in [1e3,1e60], seed 2; count cases qualifying
   (r>=2) and require the two inequalities in all qualifying cases.
M  measured: ratio beta_traj/beta_AF and bare g^2 at r=10,100,1000 for beta=r^17; mean-normalized size of an unscaled
   single-plaquette connected covariance ~ (3/2)K^2/beta^2 (README_round7) -> how fast raw signals vanish without sqrt(beta).
"""
import numpy as np, math, os, sys
out = []
def rep(n, ok, m):
    s = "MEASURED" if ok is None else ("MET" if bool(ok) else "FAILED"); out.append(f"{n}: {s} | {m}"); print(out[-1])
rs = [10.0**k for k in range(1, 7)]
l = lambda r: math.log(2+r)
a = [ (math.ceil(r**4)/(r**3*math.sqrt(l(r))), r**17/(r**16*l(r))) for r in rs]
ok = all(a[i+1][0] > a[i][0] and a[i+1][1] > a[i][1] for i in range(len(a)-1))
rep("T1", ok, "m=1 ratios L,beta: " + "; ".join(f"{x:.2g},{y:.2g}" for x, y in a))
bAF = lambda r: 11/(3*math.pi**2)*math.log(r)
b = [bAF(r)/(r**12*l(r)) for r in rs]
rep("T2", all(b[i+1] < b[i] for i in range(5)) and b[1] < 1e-10, "beta_AF/(r^12 l): " + ", ".join(f"{x:.1e}" for x in b))
errs = []
for r in rs:
    nu, m = 3, 1; beta = r**17; L = r**4
    A = min(r, L/(r**nu*math.sqrt(l(r))), (math.sqrt(beta)/(r**(2*nu+2)*math.sqrt(l(r))))**0.5)
    s = math.ceil(A*r**(2*nu))
    errs.append(A**(-m/2) + r**2*s**-12 + A*r**(2*nu+2)*math.sqrt(l(r))/math.sqrt(beta))
rep("T3", all(errs[i+1] < errs[i] for i in range(5)) and errs[-1] < 0.1, "error: " + ", ".join(f"{x:.2e}" for x in errs))
rng = np.random.default_rng(2); q = 0; bad = 0
for _ in range(10000):
    lb, lL = rng.uniform(3, 60, 2); beta = 10**lb; L = 10**lL
    r = min(beta**(1/13), L**(1/3))
    if r < 2: continue
    q += 1
    if not (beta/(r**12*l(r)) >= r/l(r)*(1-1e-12) and L/(r**2*math.sqrt(l(r))) >= r/math.sqrt(l(r))*(1-1e-12)): bad += 1
rep("T4", bad == 0, f"qualifying {q}/10000, violations {bad}")
rep("M", None, "; ".join(f"r={r:g}: beta/beta_AF={r**17/bAF(r):.1e}, g^2={4/r**17:.1e}" for r in (10, 100, 1000))
    + f"; unscaled plaquette covariance factor 1/beta^2 at r=10: {1/(10.0**17)**2:.1e}")
fn = "results_check_traj_1.txt"
while os.path.exists(fn): fn = fn.replace(".txt", "_n.txt")
open(fn, "w", encoding="utf-8").write("\n".join(out)+"\n")
sys.exit(1 if any(": FAILED" in x for x in out) else 0)
