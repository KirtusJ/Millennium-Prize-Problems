"""Independent cross-check: full cube (no octant symmetry), direct 3D numpy grid, M=32, t=0.5 and t=0.2.
Predicate: agrees with continuum.py's octant sum G(t,R,32) to relative 1e-12
(tolerance: double rounding of ~1e5 summed positive terms, ~1e-16 * sqrt/linear growth << 1e-12).
Prints only; writes no files. No randomness."""
import math, sys
import numpy as np
from continuum import G

ok = True
M = 32
n = np.arange(-M, M + 1, dtype=np.float64)
q = 2 * math.pi * n
for R in (0.25, 0.125):
    f1 = np.where(q == 0, R, 2 * np.sin(q * R / 2) / np.where(q == 0, 1, q))
    k1, k2, k3 = np.meshgrid(q, q, q, indexing="ij")
    F2 = (f1[:, None, None] * f1[None, :, None]) ** 2
    kk = np.sqrt(k1**2 + k2**2 + k3**2)
    for t in (0.2, 0.5):
        with np.errstate(divide="ignore", invalid="ignore"):
            term = F2 * (k1**2 + k2**2) / kk**2 * (kk / 2) * np.exp(-t * kk)
        term[kk == 0] = 0
        full = term.sum()
        octv = G(t, R, M)
        rel = abs(full - octv) / full
        print(f"R={R} t={t} full={full:.15e} octant={octv:.15e} rel={rel:.2e}")
        ok &= rel < 1e-12
print("CROSSCHECK", "MET" if ok else "FAILED")
sys.exit(0 if ok else 1)
