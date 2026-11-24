"""b2-matrix supplementary: subsets of the mark list. usage: python3 supp.py <tag> -> results/<tag>/supp.json (mode 'x')
Same estimators as analyze.py (imported). For each subset: cond(C_train) of the subset (no truncation needed if the
subset is non-degenerate), train lambda_min, held-out quotient with jackknife over held streams, weights.
Subsets (fixed before running): plaquettes (i); marked square (i)+(iii); neighbour (iv); marked+neighbour without
the marks that are exactly degenerate at W=-I (L_no00, L_no10, L_no01); all marks; at W != -I also (i)+(ii) and all+(ii).
Predicate S1 (expectation): a non-degenerate subset has cond(C_train) < 1e6 (sampling error of C entries ~1e-2
relative with ~18k rows, so cond < 1e6 keeps the solve meaningful; the held-out check is the real guard).
"""
import json, sys
import numpy as np
from analyze import load, CD, gsolve, q, jack, ROOT, BETA
tag = sys.argv[1]
names, Xs, Dcs, minang = load(tag)
TR, HE = list(range(16)), list(range(16, 32))
idx = {nm: k for k, nm in enumerate(names)}
P = ["B.g00", "B.g10", "B.g01", "B.g11"]; III = ["B.Rv", "B.Rh", "B.L_no00", "B.L_no10", "B.L_no01", "B.L_no11"]
IV = ["B.n00", "B.n10", "B.n01", "B.n11"]; II = [n for n in names if n[:2] in ("Wt", "Ct")]
subsets = {"plaquettes(i)": P, "marked(i+iii)": P + III, "marked_nondeg": P + ["B.Rv", "B.Rh", "B.L_no11"], "neighbour(iv)": IV,
           "nondeg(i+iii'+iv)": P + ["B.Rv", "B.Rh", "B.L_no11"] + IV, "all": names}
if II:
    subsets["(i)+(ii)"] = P + II; subsets["nondeg+(ii)"] = P + ["B.Rv", "B.Rh", "B.L_no11"] + IV + II
    subsets["all_but_ii"] = [n for n in names if n not in II]
out = {}
for lab, sub in subsets.items():
    s = [idx[n] for n in sub]
    Xsub = [X[:, s] for X in Xs]; Dsub = [Dc[:, s][:, :, s] for Dc in Dcs]
    Ct, Dt = CD(Xsub, Dsub, TR)
    lam, w, nd, _ = gsolve(Ct, Dt)
    qh, eh = jack(HE, lambda ii: q(w, *CD(Xsub, Dsub, ii)))
    out[lab] = {"n": len(s), "cond_C_train": float(np.linalg.cond(Ct)), "dropped": nd, "train_lambda": float(lam),
                "held_q": [qh, eh], "beta_held_q": BETA * qh, "w": dict(zip(sub, np.round(w, 4).tolist())),
                "S1_met": bool(np.linalg.cond(Ct) < 1e6) if lab not in ("marked(i+iii)", "all") else None}
with open(ROOT / "results" / tag / "supp.json", "x") as fh: json.dump(out, fh, indent=1)
for k, v in out.items(): print(k, v["n"], f"cond {v['cond_C_train']:.3g} drop {v['dropped']} train {v['train_lambda']:.5f} held {v['held_q'][0]:.5f}({v['held_q'][1]:.5f}) S1 {v['S1_met']}")
