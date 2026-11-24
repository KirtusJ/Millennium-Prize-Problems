"""Clear-background selection, side 6, T=12, beta=3.276133577.
Generate: build/z1m6 gen, unconditioned Wilson chain (heat bath + reflection cycles), hot start,
seed 4100001, 300 discarded cycles, 60 skeletons 10 cycles apart -> results/gen/chain.*
Selection rule fixed before the run: theta = pi/4 (G4's largest allowed gate) if at least 3 of the 60
skeletons have ALL 81 coarse spatial faces at round distance > theta from -I; otherwise theta = pi/8;
otherwise theta = pi/16. Keep the first 3 qualifying skeletons in chain order.
Per-case report (rule 4): number qualifying at each theta; distribution of the min angle over all 60.
Writes results/gen/selection.json (mode 'x').
"""
import subprocess, json, math, sys
import numpy as np
from pathlib import Path
ROOT = Path(__file__).resolve().parent
out = ROOT / "results" / "gen"; out.mkdir(parents=True, exist_ok=False)
subprocess.run([str(ROOT / "build/z1m6"), "gen", "3.276133577", "4100001", "1", "300", "60", "10", "6", "12", str(out / "chain")], check=True)
rows = [l.split(",") for l in (out / "chain.angles.csv").read_text().splitlines()[2:]]
mins = np.array([float(r[1]) for r in rows]); plaq = np.array([float(r[2]) for r in rows])
allang = np.array([[float(v) for v in r[3:]] for r in rows])
res = {"n_skeletons": len(rows), "min_angle_all": mins.tolist(), "slice0_plaquette_mean": float(plaq.mean()),
       "min_angle_quantiles_0_25_50_75_100": np.quantile(mins, [0, .25, .5, .75, 1]).tolist(),
       "all_face_angle_quantiles": np.quantile(allang, [0, .01, .05, .25, .5, .75, 1]).tolist()}
for th in (math.pi / 4, math.pi / 8, math.pi / 16):
    q = [i for i, m in enumerate(mins) if m > th]
    res[f"qualify_theta_{th:.6f}"] = len(q)
    if len(q) >= 3 and "theta" not in res:
        res["theta"] = th; res["kept"] = q[:3]
with open(out / "selection.json", "x") as fh: json.dump(res, fh, indent=1)
print({k: v for k, v in res.items() if k != "min_angle_all"})
