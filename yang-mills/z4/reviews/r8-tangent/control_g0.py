"""control_g0.py -- rerun of predicate P0 of free_curv.py after a defect in MY program:
free_curv.py used 1/(4-2 sum cos k) instead of 1/sum(2-2cos k) = 1/(8-2 sum cos k).
P0': G(0)=int d^4k/(2pi)^4 1/sum_mu(2-2cos k_mu) = 0.15493339 within 2e-3 on midpoint M=48
(tol: integrable 1/k^2 singularity, midpoint error O(M^-2)); and Richardson (M=32,48, error ~M^-2)
within 2e-4. Result file results/control_g0.txt, never overwritten. Exit 0 iff met."""
import os, sys, numpy as np
out = "results/control_g0.txt"
if os.path.exists(out): sys.exit(2)
def G(M):
    g = -np.pi + (np.arange(M) + .5) * 2 * np.pi / M
    c = np.cos(g); a, b, d = np.meshgrid(c, c, c, indexing="ij"); s3 = (a + b + d).ravel()
    return sum((1.0 / (8 - 2 * (s3 + c4))).sum() for c4 in c) / M**4
g32, g48 = G(32), G(48)
rich = (48**2 * g48 - 32**2 * g32) / (48**2 - 32**2)
ok = abs(g48 - .15493339) < 2e-3 and abs(rich - .15493339) < 2e-4
s = f"G(0) M=32 {g32:.8f} M=48 {g48:.8f} Richardson {rich:.8f} known 0.15493339 -> {'met' if ok else 'FAILED'}"
print(s); open(out, "x").write(s + "\n"); sys.exit(0 if ok else 1)
