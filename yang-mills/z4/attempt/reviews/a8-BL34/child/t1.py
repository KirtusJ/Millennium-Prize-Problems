"""T1. Predicates fixed before first run:
P1: lambda (smallest eig of Qmat=D^T D, 7x7) > 1e-9 (tolerance: far above float eps ~1e-15*norm, far below expected O(0.1..1)).
Also self-checks: trace(D Qmat^-1 D^T)=7 within 1e-10 (projector of rank 7); D has rank 7.
Output written with mode 'x'."""
import numpy as np
from su2lib import *
D = Dmatrix(); Q = D.T @ D
ev = np.linalg.eigvalsh(Q); lam = ev[0]
H = D @ np.linalg.inv(Q) @ D.T
p = plaq_index(1, 2, 1, 1)
cpp = H[p, p]
res = dict(eigs=ev.tolist(), lam=lam, lam_over_16=lam/16, rank=int(np.linalg.matrix_rank(D)),
           trace=float(np.trace(H)), plaq_index=p, Cpp=float(cpp), target_1p5Cpp=float(1.5*cpp),
           diag_H_min=float(H.diagonal().min()), diag_H_max=float(H.diagonal().max()))
with open("out/t1.txt", "x") as f:
    for k, v in res.items(): f.write(f"{k} = {v}\n")
print(open("out/t1.txt").read())
print("P1", "met" if lam > 1e-9 else "FAILED", "| trace check", abs(res['trace']-7) < 1e-10)
