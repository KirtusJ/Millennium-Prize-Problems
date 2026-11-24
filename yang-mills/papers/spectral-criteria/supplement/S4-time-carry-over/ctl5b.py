"""T-P0 re-test (after ctl5.py K4 failed on .meta.txt because the prefixes differed): run z1mx4 and z1mx5 'fixed' with the SAME
relative prefix 's' in two fresh directories results_ctl_b/{old,new}; predicate T-P0b: all 5 files byte-identical (exact), 3 cases.
T-P4 (not reached in K4 because of sys.exit order? no: it ran; repeated here): series m0 = w_L4.X to 1e-9.
"""
import subprocess, filecmp, sys
import numpy as np
from pathlib import Path
R = Path(__file__).resolve().parent; out = R / "results_ctl_b"; out.mkdir(exist_ok=False)
ok = True
for tag, seed, hot, sk in [("d0c", "11100001", "0", "skeletons/d0.txt"), ("d0h", "11107920", "1", "skeletons/d0.txt"), ("clc", "11300001", "0", "results/gen/chain.skel0.txt")]:
    for v in ("old", "new"):
        d = out / tag / v; d.mkdir(parents=True)
        exe = R / "build" / ("z1mx4" if v == "old" else "z1mx5")
        subprocess.run([str(exe), "fixed", "3.276133577", seed, hot, "12", "8", "6", "6", "12", str(R / sk), "s"], check=True, cwd=d)
    for s in [".csv", ".colours.csv", ".meta.txt", ".X.csv", ".Dc.txt"]:
        same = filecmp.cmp(out / tag / "old" / f"s{s}", out / tag / "new" / f"s{s}", shallow=False)
        print(f"T-P0b {tag} {s}: {'MET' if same else 'FAILED'}"); ok &= same
for tag in ("d0c", "d0h", "clc"):
    X = np.loadtxt(R / "results_ctl" / f"{tag}_time.X.csv", delimiter=",", skiprows=1)
    W = np.loadtxt(R / "weights/w_d0.txt")
    S = np.loadtxt(R / "results_ctl" / f"{tag}_time.series.csv", delimiter=",", skiprows=1)
    d = np.abs(X @ W.T - S[:, :3]).max(); print(f"T-P4 {tag}: max dev {d:.2e} {'MET' if d < 1e-9 else 'FAILED'}"); ok &= d < 1e-9
sys.exit(0 if ok else 1)
