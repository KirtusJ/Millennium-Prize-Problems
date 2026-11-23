"""Check of the reading of FdV-O'C eq.(30): plaquette field = Im Tr(U_p - 1)/(a^2 g).
PREDICATES (fixed before the run):
 Q1 For 10^4 Haar-random SU(2) matrices (seed 20261123), max |Im Tr U| < 1e-12
    (tolerance: double-precision rounding of a 2x2 trace, ~1e-15, with margin).
 Q2 For SU(3), U = exp(i eps X), X random traceless Hermitian (seed 20261123):
    Im Tr U has no linear term: |Im Tr U| / eps^3 is constant to 1% between
    eps = 1e-2 and 1e-3 (tolerance: next correction O(eps^2) ~ 1e-4 relative, margin 100x),
    while (1 - Re Tr U/3)/eps^2 is constant to 1% (action density is quadratic).
Result file results/imtr_check.txt, never overwritten.
"""
import sys, os
sys.path.append("C:/Users/donke/AppData/Roaming/Python/Python314/site-packages")
import numpy as np
out = "results/imtr_check.txt"
if os.path.exists(out): print("exists"); sys.exit(3)
rng = np.random.default_rng(20261123)
q = rng.normal(size=(10000, 4)); q /= np.linalg.norm(q, axis=1)[:, None]
U = np.empty((10000, 2, 2), complex)
U[:, 0, 0] = q[:, 0] + 1j*q[:, 3]; U[:, 0, 1] = q[:, 2] + 1j*q[:, 1]
U[:, 1, 0] = -q[:, 2] + 1j*q[:, 1]; U[:, 1, 1] = q[:, 0] - 1j*q[:, 3]
m = np.abs(np.trace(U, axis1=1, axis2=2).imag).max()
ok1 = m < 1e-12
A = rng.normal(size=(3, 3)) + 1j*rng.normal(size=(3, 3)); X = A + A.conj().T; X -= np.trace(X)/3*np.eye(3)
def expi(M):
    w, V = np.linalg.eigh(M); return V @ np.diag(np.exp(1j*w)) @ V.conj().T
r = {}
for e in [1e-2, 1e-3]:
    T = np.trace(expi(e*X)); r[e] = (abs(T.imag)/e**3, (1 - T.real/3)/e**2)
ok2 = abs(r[1e-2][0]/r[1e-3][0]-1) < 0.01 and abs(r[1e-2][1]/r[1e-3][1]-1) < 0.01
L = [f"Q1 max|ImTr U| SU(2) = {m:.2e} {ok1}", f"Q2 SU(3) ImTr/eps^3, (1-ReTr/3)/eps^2: {r} {ok2}",
     f"COUNTS met {int(ok1)+int(ok2)}, failed {2-int(ok1)-int(ok2)}, measured only 0"]
print("\n".join(L)); open(out, "w").write("\n".join(L)+"\n"); sys.exit(0 if ok1 and ok2 else 1)
