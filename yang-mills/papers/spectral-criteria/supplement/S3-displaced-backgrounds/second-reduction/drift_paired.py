"""Measured-only follow-up (not a registered predicate; added after seeing R4 fail on N-d0 r4):
paired jackknife of the half difference D = r(second halves) - r(first halves), deleting one stream from BOTH halves
(accounts for the within-stream correlation the registered R4 neglects); also Q1, Q4 computed on first and on second
halves separately (independent-arm errors). Writes results_fixed/drift_paired.txt (mode x)."""
import sys, numpy as np
sys.path.insert(0, ".")
from reduce_fixed import load, est, jack
out = []
H = {}
for t in ("N-d2", "N-d0"):
    ids, data, _, _ = load(f"results/{t}")
    h = 576
    f = lambda items: {k: est([m[h:] for m in items])[k] - est([m[:h] for m in items])[k] for k in ("r1", "r4")}
    j = jack(data, f)
    H[t] = (jack([m[:h] for m in data]), jack([m[h:] for m in data]))
    for k in ("r1", "r4"):
        out.append(f"{t} {k}: D = {j[k][0]:+.6f} +- {j[k][1]:.6f}  (D/err = {j[k][0]/j[k][1]:+.2f})")
for half, nm in ((0, "first"), (1, "second")):
    for k in ("r1", "r4"):
        a, b = H["N-d2"][half][k], H["N-d0"][half][k]
        q = a[0] / b[0]; e = q * np.hypot(a[1] / a[0], b[1] / b[0])
        out.append(f"Q_{k} on {nm} halves = {q:.4f} +- {e:.4f}")
txt = "\n".join(out) + "\n"
open("results_fixed/drift_paired.txt", "x").write(txt); print(txt)
