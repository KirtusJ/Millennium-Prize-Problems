"""A3/A6: 1-D sums S0, S1 on shifted grids vs the Poisson+tail bounds of THEOREM_V step 4.

Units: s = 1 (only r = l/sqrt(s) matters). alpha = 4s = 4, Delta = 2 pi / l.
Parameters (my reading of 'kappa = 2.5, theta = 0.5'): K = 2.5/sqrt(s), Q = 0.5 K, K' = K - Q/2.
Definitions (mine, document gives only delta0, delta1):
  c0 = sqrt(pi/alpha)/Delta, c1 = c0/(2 alpha)
  U0 = c0 (1+delta0), L0 = c0 (1-delta0) - 2 T0,  T0 = (1/Delta) int_{K'-Delta}^inf e^{-alpha x^2}
  U1 = c1 (1+delta1), L1 = c1 (1-delta1) - 2 T1,  T1 = (1/Delta) int_{K'-Delta}^inf x^2 e^{-alpha x^2}
Hypothesis per case: H_tail: K' - Delta >= 1/sqrt(alpha).
Predicates (for every r in R and 20 shifts, seed 13):
  P1: |Delta S0full / sqrt(pi/alpha) - 1| <= delta0 + 1e-12   (tol: float64 roundoff of <=1e4 positive terms)
  P2: |S1full/c1 - 1| <= delta1 + 1e-12
  P3 (cases with H_tail): S0full - S0trunc <= 2 T0 + 1e-12 c0 ; same for S1 with c1
  P4 (cases with H_tail): L0 <= S0trunc <= U0 and L1 <= S1trunc <= U1 (tol 1e-12 relative)
  M1 (measured only): bracket = 2 L1 L0^2 - U1 U0^2 normalised by c1 c0^2 (=1 at r->inf); r where it turns positive.
  M2 (measured only): B'/(A s) at r, with eps = K^2 b^2/24, b = sqrt(s)/2.
Exit 0 if P1..P4 all met, 1 otherwise.
"""
import sys, math
import numpy as np
from math import erfc, sqrt, pi, exp

out = sys.argv[1]
rng = np.random.default_rng(13)
s = 1.0; al = 4*s
K = 2.5/sqrt(s); Q = 0.5*K; Kp = K - Q/2
b = sqrt(s)/2; eps = K**2*b**2/24
R = [5, 6, 7, 8, 9, 10, 12, 15, 20, 30, 50, 80, 130]
fails = []; lines = []
def deltas(l):
    d0 = 2*sum(exp(-m*m*l*l/(4*al)) for m in range(1, 60))
    d1 = 2*sum(abs(1-m*m*l*l/(2*al))*exp(-m*m*l*l/(4*al)) for m in range(1, 60))
    return d0, d1
nq = 0
for l in R:
    D = 2*pi/l; c0 = sqrt(pi/al)/D; c1 = c0/(2*al)
    d0, d1 = deltas(l)
    x = Kp - D
    htail = x >= 1/sqrt(al)
    T0 = (0.5*sqrt(pi/al)*erfc(sqrt(al)*x))/D if x > 0 else float('inf')
    T1 = ((x*exp(-al*x*x))/(2*al) + sqrt(pi)*erfc(sqrt(al)*x)/(4*al**1.5))/D if x > 0 else float('inf')
    U0, L0 = c0*(1+d0), c0*(1-d0) - 2*T0
    U1, L1 = c1*(1+d1), c1*(1-d1) - 2*T1
    nq += htail
    for j in range(20):
        sh = rng.uniform(0, D)
        nmax = int(40/D) + 2
        p = sh + D*np.arange(-nmax, nmax+1)
        g0 = np.exp(-al*p*p); g1 = p*p*g0
        S0f, S1f = g0.sum(), g1.sum()
        m = np.abs(p) <= Kp
        S0t, S1t = g0[m].sum(), g1[m].sum()
        e0 = abs(S0f/c0 - 1); e1 = abs(S1f/c1 - 1)
        ok1 = e0 <= d0 + 1e-12; ok2 = e1 <= d1 + 1e-12
        if not ok1: fails.append(f"P1 r={l} sh={sh:.4f} err={e0:.3e} d0={d0:.3e}")
        if not ok2: fails.append(f"P2 r={l} sh={sh:.4f} err={e1:.3e} d1={d1:.3e}")
        if htail:
            if not (S0f-S0t <= 2*T0 + 1e-12*c0): fails.append(f"P3 S0 r={l}")
            if not (S1f-S1t <= 2*T1 + 1e-12*c1): fails.append(f"P3 S1 r={l}")
            if not (L0 <= S0t*(1+1e-12) and S0t <= U0*(1+1e-12)): fails.append(f"P4 S0 r={l} sh={sh:.4f} L0={L0} S={S0t} U0={U0}")
            if not (L1 <= S1t*(1+1e-12) and S1t <= U1*(1+1e-12)): fails.append(f"P4 S1 r={l} sh={sh:.4f} L1={L1} S={S1t} U1={U1}")
    br = (2*L1*L0**2 - U1*U0**2)/(c1*c0**2)
    A = (1-eps)**4*(2*L1*L0**2 - U1*U0**2)/4
    Bp = (1-eps)**4*(3/16)*U0**3 + s*A
    lines.append(f"r={l:4d} Htail={htail} d0={d0:.3e} d1={d1:.3e} bracket/c1c0^2={br:+.6f} "
                 f"A*s^2.5*(2/l^3)={2*A/l**3:+.4e} B'/(A s)={(Bp/(A*s) if A>0 else float('nan')):.4f} Q^2>=A/B':{Q*Q>=A/Bp}")
with open(out, "x") as fh:
    fh.write(f"eps={eps:.5f} (1-eps)^4={(1-eps)**4:.5f} K={K} Q={Q} K'={Kp}\n")
    fh.write(f"cases with H_tail: {nq} of {len(R)} r-values (x20 shifts)\n")
    fh.write("\n".join(lines) + "\n")
    fh.write(f"true const sqrt(pi)/(640 pi^2) = {sqrt(pi)/(640*pi**2):.4e}; 5/8*(1-eps)^4*true = {0.625*(1-eps)**4*sqrt(pi)/(640*pi**2):.4e}\n")
    fh.write(f"FAILS ({len(fails)}):\n" + "\n".join(fails[:60]) + "\n")
print(open(out).read())
sys.exit(0 if not fails else 1)
