"""(c) Both clear-reference conventions for the three prior side-six clear skeletons, from results_fixed/old-clear{0,2,4}.json
(produced by reduce_fixed.py on the archived ../z1-mix6/results/clear*). Raw B = columns single/average (full xz holonomy);
normalised traceless B = *_tl columns. Predicate (fixed before run): C1 raw r4 values equal G4's readback .09201,.08599,.09281
and traceless .08476,.08266,.09546 to the 5 printed decimals (tolerance 0.000005 = half a unit of G4's last printed digit).
Writes results_fixed/clear_conventions.md (mode x)."""
import json
G4 = {"clear0": (.09201, .08476), "clear2": (.08599, .08266), "clear4": (.09281, .09546)}
rows = ["| skeleton | min angle (G4) | r1 raw B | r1 traceless B | r4 raw B | r4 traceless B | C1 vs G4 |", "|---|---:|---:|---:|---:|---:|---|"]
mins = {"clear0": 1.14269, "clear2": 0.95857, "clear4": 1.18204}
ok = True
for t in ("clear0", "clear2", "clear4"):
    p = json.load(open(f"results_fixed/old-{t}.json"))["pooled"]
    f = lambda k: f"{p[k][0]:.5f}({p[k][1]:.5f})"
    m = abs(p["r4"][0] - G4[t][0]) <= 5e-6 and abs(p["r4_tl"][0] - G4[t][1]) <= 5e-6
    ok &= m
    rows.append(f"| {t} | {mins[t]} | {f('r1')} | {f('r1_tl')} | {f('r4')} | {f('r4_tl')} | {'MET' if m else 'FAILED'} |")
txt = "\n".join(rows) + "\n\nSide eight: see G4 readback (z4-readback.md): raw .09052(.00453), .10824(.00527), .08237(.00393); traceless .08984(.00352), .10826(.00528), .07420(.00369).\n"
open("results_fixed/clear_conventions.md", "x").write(txt)
print(txt); print("C1", "MET" if ok else "FAILED")
