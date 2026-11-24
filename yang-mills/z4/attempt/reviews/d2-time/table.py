"""Make results/tables.md (mode 'x') from results/<tag>/summary.json. usage: python3 table.py <tag> ...
No predicates; formatting only. beta*ratio1 is the quantity compared with G4's disk numbers."""
import json, sys
import numpy as np
from pathlib import Path
ROOT = Path(__file__).resolve().parent
BETA = 3.276133577
f = lambda v, e, d=4: f"{v:.{d}f}({e:.{d}f})"
out = ["| run | streams x meas | min angle from -I | spread | J1 | Var1 | J4 | Var4 | J1/Var1 | J4/Var4 | beta J1/Var1 | traceless-B J1/V1, J4/V4 | hot-cold z (r1, r4) | stream sd r1, r4 | colours carrying J4 (fraction) |",
       "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|"]
for tag in sys.argv[1:]:
    d = json.load(open(ROOT / "results" / tag / "summary.json"))
    p = d["pooled"]; pc = d["per_colour"]
    ps = d["per_stream"]
    sd1 = np.std([s["ratio1"] for s in ps], ddof=1); sd4 = np.std([s["ratio4"] for s in ps], ddof=1)
    cols = ", ".join(f"c{k}:{pc[f'j4_frac{k}'][0]:.2f}" for k in range(24) if pc[f"j4_frac{k}"][0] > 1e-9)
    out.append(f"| {tag} | {d['streams']} x {d['measurements_per_stream'][0]} | {d['min_angle_from_minusI']:.4f} | {f(*p['spread'])} | "
               f"{f(*p['J1'],5)} | {f(*p['var1'])} | {f(*p['J4'],6)} | {f(*p['var4'],5)} | {f(*p['ratio1'])} | {f(*p['ratio4'])} | "
               f"{f(BETA*p['ratio1'][0], BETA*p['ratio1'][1])} | {p['ratio1_tl'][0]:.4f}, {p['ratio4_tl'][0]:.4f} | "
               f"{d['T2_hot_cold']['ratio1']['z']:.2f}, {d['T2_hot_cold']['ratio4']['z']:.2f} | {sd1:.4f}, {sd4:.4f} | {cols} |")
with open(ROOT / "results" / "tables.md", "x") as fh:
    fh.write("\n".join(out) + "\n")
print("\n".join(out))
