"""b2-matrix EXTRA 2: usage python3 supp3.py <tag> -> results/<tag>/supp3.json (mode 'x'). Same estimators as analyze.py.
Subsets (fixed before running): marked (7); marked+xp (11); marked+yz (11); marked+xp+yz (15, the three faces at -I
sharing the W edge); all 35. Predicate Y1 (cross-check): marked+xp agrees with M-d0's .02675(69), |z| <= 2.
Expectation Y2 (failure is an outcome): marked+xp+yz lower than marked+xp by > 2 sigma.
"""
import json, sys
import numpy as np
from analyze import load, CD, gsolve, q, jack, ROOT, BETA
tag = sys.argv[1]
names, Xs, Dcs, minang = load(tag)
TR, HE = list(range(16)), list(range(16, 32)); idx = {nm: k for k, nm in enumerate(names)}
M = ["B.g00", "B.g10", "B.g01", "B.g11", "B.Rv", "B.Rh", "B.L_no11"]
XP = [f"B.nxp{c}" for c in ("00", "10", "01", "11")]; YZ = [f"B.yz{c}" for c in ("00", "10", "01", "11")]
subsets = {"marked": M, "marked+xp": M + XP, "marked+yz": M + YZ, "marked+xp+yz": M + XP + YZ, "all35": names}
out = {}
for lab, sub in subsets.items():
    s = [idx[n] for n in sub]
    Xsub = [X[:, s] for X in Xs]; Dsub = [Dc[:, s][:, :, s] for Dc in Dcs]
    Ct, Dt = CD(Xsub, Dsub, TR); lam, w, nd, _ = gsolve(Ct, Dt)
    qh, eh = jack(HE, lambda ii: q(w, *CD(Xsub, Dsub, ii)))
    num = np.array([np.mean([w @ Dsub[i][c] @ w for i in HE]) for c in range(24)])
    out[lab] = {"n": len(s), "cond_C_train": float(np.linalg.cond(Ct)), "dropped": nd, "train_lambda": float(lam),
                "held_q": [qh, eh], "beta_held_q": BETA * qh, "w": dict(zip(sub, np.round(w, 4).tolist())),
                "colour_shares": (num / num.sum()).round(4).tolist()}
z = (out["marked+xp"]["held_q"][0] - .02675) / np.hypot(out["marked+xp"]["held_q"][1], .00069)
out["Y1"] = {"z": float(z), "met": bool(abs(z) <= 2)}
a, b = out["marked+xp+yz"]["held_q"], out["marked+xp"]["held_q"]
out["Y2"] = {"diff": b[0] - a[0], "sigma": float(np.hypot(a[1], b[1])), "met": bool(b[0] - a[0] > 2 * np.hypot(a[1], b[1]))}
with open(ROOT / "results" / tag / "supp3.json", "x") as fh: json.dump(out, fh, indent=1)
for k, v in out.items():
    if k.startswith("Y"): print(k, v); continue
    print(k, v["n"], f"cond {v['cond_C_train']:.3g} train {v['train_lambda']:.5f} held {v['held_q'][0]:.5f}({v['held_q'][1]:.5f})", v["w"] if v["n"] <= 15 else "", [i for i, x in enumerate(v["colour_shares"]) if x > 0.005])
