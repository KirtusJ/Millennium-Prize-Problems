"""Swap test (fixed before running): train on HELD (16..31), evaluate on TRAIN (0..15), for L1..L4.
Symmetrised optimism gap = mean of (q_held - lambda_train) and (q_train' - lambda_held'): removes the difference between halves.
Expectation S1 (measured, failure is an outcome): symmetrised gap > 0 for every list (training eigenvalue biased low).
Output results/<tag>/swap4.txt (mode x)."""
import sys, json, numpy as np
from an4 import load, CD, gsolve, qv, lists, ROOT
tag = sys.argv[1]; names, st = load(tag); L, _ = lists(names); idx = {n: k for k, n in enumerate(names)}
r = json.load(open(ROOT / "results" / tag / "an4.json")); TR, HE = list(range(16)), list(range(16, 32)); out = []
for lab, sub in L.items():
    sel = [idx[n] for n in sub]; Ch, Dh = CD(st, HE, sel); lam2, w2, nd = gsolve(Ch, Dh); q2 = qv(w2, *CD(st, TR, sel))
    g1 = r[lab]["held_q"][0] - r[lab]["train_lambda"]; g2 = q2 - lam2; sg = (g1 + g2) / 2
    w1 = np.array([r[lab]["w"][n] for n in sub]); Ct = CD(st, TR, sel)[0]
    cos = abs(w1 @ Ct @ w2) / np.sqrt((w1 @ Ct @ w1) * (w2 @ Ct @ w2))
    out.append(f"{lab} n {len(sub)} lambda_on_held {lam2:.5f} q_on_train {q2:.5f} gap_fwd {g1:+.5f} gap_swap {g2:+.5f} sym_gap {sg:+.5f} S1 {'MET' if sg > 0 else 'FAILED'} cos(w,w_swap)_C {cos:.4f}")
txt = "\n".join(out); print(txt)
with open(ROOT / "results" / tag / "swap4.txt", "x") as fh: fh.write(txt + "\n")
