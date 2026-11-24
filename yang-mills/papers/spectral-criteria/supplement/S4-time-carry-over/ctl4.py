"""P8 control for z1mx4 (fixed before running): at seed 3100001, cold, burn 576, 64 measurements, d0 skeleton,
(a) z1mx4 .csv and .colours.csv byte-identical to z1mx3 (RNG calls and f1/f4 path unchanged);
(b) the 15 L1 marks of z1mx4 equal the corresponding z1mx3 marks at every measurement to 1e-12 (float printing at 12 digits: exact equality expected);
(c) the diagonal of z1mx4's D (mean over colours) equals the diagonal of mean_c z1mx3 Dc for the 15 marks to 1e-12 relative.
Tolerance 1e-12: both are printed with 12 decimals / 12-digit mantissa from identical arithmetic. Output results/ctl4/ (mode x)."""
import subprocess, numpy as np, filecmp, sys
from pathlib import Path
R = Path("results/ctl4"); R.mkdir(parents=True, exist_ok=False)
args = ["fixed", "3.276133577", "3100001", "0", "576", "64", "6", "6", "12", "skeletons/d0.txt"]
subprocess.run(["build/z1mx3"] + args + [str(R / "old")], check=True)
subprocess.run(["build/z1mx4"] + args + [str(R / "new")], check=True)
a = filecmp.cmp(R / "old.csv", R / "new.csv", shallow=False) and filecmp.cmp(R / "old.colours.csv", R / "new.colours.csv", shallow=False)
old = np.loadtxt(R / "old.X.csv", delimiter=",", skiprows=1); on = open(R / "old.X.csv").readline().strip().split(",")
new = np.loadtxt(R / "new.X.csv", delimiter=",", skiprows=1); nn = open(R / "new.X.csv").readline().strip().split(",")
mp = {"B.g00": "B.xy000.g00", "B.g10": "B.xy000.g10", "B.g01": "B.xy000.g01", "B.g11": "B.xy000.g11", "B.Rv": "B.xy000.Rv", "B.Rh": "B.xy000.Rh", "B.L_no11": "B.xy000.L_no11"}
for c in ("00", "10", "01", "11"): mp[f"B.nxp{c}"] = f"B.xy200.g{c}"; mp[f"B.yz{c}"] = f"B.yz204.g{c}"
dev = max(np.abs(old[:, on.index(k)] - new[:, nn.index(v)]).max() for k, v in mp.items())
lo = [l for l in open(R / "old.Dc.txt") if not l.startswith("#")]; no = len(on)
Dold = np.array([[float(x) for x in l.split()] for l in lo]).reshape(24, no, no).mean(0)
ln = [l for l in open(R / "new.Dc.txt") if not l.startswith("#")]; nnm = len(nn)
Dnew = np.array([float(x) for x in ln[0].split()]).reshape(nnm, nnm)
dd = max(abs(Dold[on.index(k), on.index(k)] - Dnew[nn.index(v), nn.index(v)]) / Dold[on.index(k), on.index(k)] for k, v in mp.items())
print(f"P8a csv identical {a}; P8b max L1 mark dev {dev:.3e}; P8c max rel D diag dev {dd:.3e}; n marks new {nnm}")
ok = a and dev <= 1e-12 and dd <= 1e-12
print("P8", "MET" if ok else "FAILED"); sys.exit(0 if ok else 1)
