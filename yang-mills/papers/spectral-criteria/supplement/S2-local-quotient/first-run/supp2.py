"""b2-matrix EXTRA: subsets of the 31-mark list of z1mx2. usage: python3 supp2.py <tag> -> results/<tag>/supp2.json (mode 'x')
Same estimators as analyze.py. Subsets (fixed before running): marked (7 non-degenerate marks); marked + one adjacent
square (each of the six); marked + xp (= the 11-mark set of the M-runs, cross-check against M-d0 with independent seeds);
marked + all six (31). Predicate X1 (cross-check): marked+xp held quotient agrees with M-d0's 11-mark .02675(69) within
|z| <= 2 (independent streams). Expectation X2 (not a defect if failed): adding all six squares lowers the held-out
quotient below marked+xp by more than 2 sigma.
"""
import json, sys
import numpy as np
from analyze import load, CD, gsolve, q, jack, ROOT, BETA
tag = sys.argv[1]
names, Xs, Dcs, minang = load(tag)
TR, HE = list(range(16)), list(range(16, 32))
idx = {nm: k for k, nm in enumerate(names)}
M = ["B.g00", "B.g10", "B.g01", "B.g11", "B.Rv", "B.Rh", "B.L_no11"]
sq = lambda lab: [f"B.n{lab}{c}" for c in ("00", "10", "01", "11")]
subsets = {"marked": M}
for lab in ("xp", "xm", "yp", "ym", "zp", "zm"): subsets[f"marked+{lab}"] = M + sq(lab)
subsets["marked+all6"] = names
out = {}
for lab, sub in subsets.items():
    s = [idx[n] for n in sub]
    Xsub = [X[:, s] for X in Xs]; Dsub = [Dc[:, s][:, :, s] for Dc in Dcs]
    Ct, Dt = CD(Xsub, Dsub, TR); lam, w, nd, _ = gsolve(Ct, Dt)
    qh, eh = jack(HE, lambda ii: q(w, *CD(Xsub, Dsub, ii)))
    out[lab] = {"n": len(s), "cond_C_train": float(np.linalg.cond(Ct)), "dropped": nd, "train_lambda": float(lam),
                "held_q": [qh, eh], "beta_held_q": BETA * qh, "w": dict(zip(sub, np.round(w, 4).tolist()))}
z = (out["marked+xp"]["held_q"][0] - .02675) / np.hypot(out["marked+xp"]["held_q"][1], .00069)
out["X1"] = {"z": float(z), "met": bool(abs(z) <= 2)}
a, b = out["marked+all6"]["held_q"], out["marked+xp"]["held_q"]
out["X2"] = {"diff": b[0] - a[0], "sigma": float(np.hypot(a[1], b[1])), "met": bool(b[0] - a[0] > 2 * np.hypot(a[1], b[1]))}
with open(ROOT / "results" / tag / "supp2.json", "x") as fh: json.dump(out, fh, indent=1)
for k, v in out.items():
    if k.startswith("X"): print(k, v); continue
    print(k, v["n"], f"cond {v['cond_C_train']:.3g} drop {v['dropped']} train {v['train_lambda']:.5f} held {v['held_q'][0]:.5f}({v['held_q'][1]:.5f})")
