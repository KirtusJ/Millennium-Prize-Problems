"""d2-time control of the sampler extension. usage: python3 ctl5.py  -> results_ctl/ (mode 'x' files, created fresh)
Predicates (fixed before the first run):
 T-P0 z1mx5 'fixed' output files (.csv, .colours.csv, .meta.txt, .X.csv, .Dc.txt) byte-identical to z1mx4 'fixed' at the same
      arguments (seed 11100001 cold and 11107920 hot, burn 12, 8 samples, spacing 6, d0 skeleton; and seed 11300001 on chain.skel0).
 T-P3 z1mx5 'time' X.csv byte-identical to 'fixed' X.csv at the same arguments (the chain does not depend on the refresh).
 T-P4 in 'time' mode, column m0 of series.csv equals w_L4 . X(0) from X.csv to 1e-9 (printing + dot product rounding).
Tolerances: byte identity is exact; 1e-9 = 12-digit X printing times sum |w| (~30) plus 11-digit series printing.
"""
import subprocess, filecmp, sys
import numpy as np
from pathlib import Path
R = Path(__file__).resolve().parent; out = R / "results_ctl"; out.mkdir(exist_ok=False)
ok = True
cases = [("d0c", "11100001", "0", "skeletons/d0.txt"), ("d0h", "11107920", "1", "skeletons/d0.txt"), ("clc", "11300001", "0", "results/gen/chain.skel0.txt")]
for tag, seed, hot, sk in cases:
    a = [seed, hot, "12", "8", "6", "6", "12", sk]
    subprocess.run([str(R / "build/z1mx4"), "fixed", "3.276133577", *a, str(out / f"{tag}_old")], check=True)
    subprocess.run([str(R / "build/z1mx5"), "fixed", "3.276133577", *a, str(out / f"{tag}_new")], check=True)
    subprocess.run([str(R / "build/z1mx5"), "time", "3.276133577", *a, str(R / "weights/w_d0.txt"), "1", str(out / f"{tag}_time")], check=True)
    for s in [".csv", ".colours.csv", ".meta.txt", ".X.csv", ".Dc.txt"]:
        same = filecmp.cmp(out / f"{tag}_old{s}", out / f"{tag}_new{s}", shallow=False)
        print(f"T-P0 {tag} {s}: {'MET' if same else 'FAILED'}"); ok &= same
    same = filecmp.cmp(out / f"{tag}_new.X.csv", out / f"{tag}_time.X.csv", shallow=False)
    print(f"T-P3 {tag}: {'MET' if same else 'FAILED'}"); ok &= same
    X = np.loadtxt(out / f"{tag}_time.X.csv", delimiter=",", skiprows=1)
    w = np.loadtxt(R / "weights/w_d0.txt")[0]
    m0 = np.loadtxt(out / f"{tag}_time.series.csv", delimiter=",", skiprows=1)[:, 0]
    d = np.abs(X @ w - m0).max(); print(f"T-P4 {tag}: max dev {d:.2e} {'MET' if d < 1e-9 else 'FAILED'}"); ok &= d < 1e-9
sys.exit(0 if ok else 1)
