"""Own control reducer for G4's 2l winding streams (g4/cyclic-transfer/unz/).
Predicate C1 (fixed before run): the second-largest algebraic eigenvalue of the symmetrized, marginal-normalised
pooled 4x4 joint matrix equals G4's reported .06197 (n5) and .00408 (n10) to the 5 decimals quoted
(tolerance 5e-6 = half a unit in the 5th decimal, from G4's rounding).
C2: delete-one-stream jackknife SE equals G4's .00257 and .00072 within 5e-6.
Implemented independently from G4's winding.py (own code, numpy eigvalsh)."""
import sys, numpy as np
D = "/home/user/z4-workers/e2-cross/g4/cyclic-transfer/unz/"
def lam2(c):
    j = c + c.T; j = j / j.sum(); v = j.sum(1)
    return np.sort(np.linalg.eigvalsh(j / np.sqrt(np.outer(v, v))))[-2]
ok = True
for lab, ref, refse in (("n5", .06197, .00257), ("n10", .00408, .00072)):
    S = np.array([np.loadtxt(f"{D}{lab}-{i}.csv", delimiter=",", dtype=np.int64)[:, 1:].sum(0).reshape(4, 4) for i in range(4)])
    full = lam2(S.sum(0)); jk = np.array([lam2(S.sum(0) - s) for s in S]); n = len(S)
    se = np.sqrt((n - 1) / n * ((jk - jk.mean()) ** 2).sum())
    c1 = abs(full - ref) < 5e-6; c2 = abs(se - refse) < 5e-6; ok &= c1 and c2
    print(f"{lab} lambda2={full:.7f} se={se:.7f} C1={'met' if c1 else 'FAILED'} C2={'met' if c2 else 'FAILED'}")
print("4l: long-streams.zip absent from g4/cyclic-transfer -> .06157/.00169 NOT reproducible from files")
sys.exit(0 if ok else 1)
