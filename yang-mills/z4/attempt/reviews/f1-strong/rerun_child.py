"""rerun_child.py -- reread/rerun of the child's (T69) claim with MY Hessian code (hess.py).
Predicate R1 (fixed before run): spectrum of Hess V (beta=1) at pi-flux on L=2 has multiplicities
 -8:9, -6:36, -4:54, -2:36, 0:57 (child's claim; also my Fourier prediction -2m with 9*C(4,m) for m>=1,
 zero 57), each eigenvalue within 1e-9 of the integer (eigh roundoff).
Measured only: c of child's best random-start configuration is not reproduced (it saved .npy; not loaded,
to keep its file untrusted-free) -- the child's 7.29 is reported as CLAIMED.
"""
import sys, numpy as np, hess
f = open(sys.argv[1], "x")
L = hess.Lattice(2); H, _ = hess.hessian(L, hess.piflux(L)); ev = np.linalg.eigvalsh(H)
r = np.round(ev).astype(int); ok = np.max(np.abs(ev - r)) < 1e-9
cnt = {v: int((r == v).sum()) for v in sorted(set(r))}
exp = {-8: 9, -6: 36, -4: 54, -2: 36, 0: 57}
res = ok and cnt == exp
print("multiplicities", cnt, "R1", "MET" if res else "FAILED", file=f); print(cnt, res)
sys.exit(0 if res else 1)
