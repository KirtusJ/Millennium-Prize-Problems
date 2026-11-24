"""d2-time: apply the interpretation rule fixed in the prodt.py docstring (before any production run).
usage: python3 verdict.py <out file>   reads results/T-d0/antime.json and (if present) results/T-clear0/antime.json.
Rule, per definition d in (loc, tr), R2 = R2_held(t=1) for w_L4 (row 0):
  persists := R2(-I) - R2(clear) > 3 sqrt(se(-I)^2 + se(clear)^2) AND R2(-I) > 0.1
  does not := R2(-I) < 0.02 AND se(-I) < 0.01 ;  otherwise not resolved. Both d agree -> that verdict, else 'not resolved'.
Also printed (measured only): the same comparison for w_L1 and f4, and rho differences -I minus clear with combined se.
"""
import json, sys, math
from pathlib import Path
R = Path(__file__).resolve().parent
d0 = json.load(open(R / "results/T-d0/antime.json"))["table"]
cp = R / "results/T-clear0/antime.json"; cl = json.load(open(cp))["table"] if cp.exists() else None
out = []; ver = {}
for d in ("loc", "tr"):
    a = d0[f"wL4 t=1 {d}"]; r2, se = a["R2_held"], a["R2_held_se"]
    if cl:
        b = cl[f"wL4 t=1 {d}"]; diff = r2 - b["R2_held"]; cse = math.hypot(se, b["R2_held_se"])
        pers = diff > 3 * cse and r2 > 0.1
        out.append(f"{d}: R2_held(-I) {r2:.5f}({se:.5f}) clear {b['R2_held']:.5f}({b['R2_held_se']:.5f}) diff {diff:.5f} comb se {cse:.5f} z {diff/cse:.2f}")
    else:
        pers = None; out.append(f"{d}: R2_held(-I) {r2:.5f}({se:.5f}); clear run absent -> 'persists' clause not evaluable")
    dn = r2 < 0.02 and se < 0.01
    v = "persists" if pers else ("does not" if dn else "not resolved")
    if pers is None and not dn: v = "not resolved (clear missing)"
    ver[d] = v; out.append(f"  persists clause: {pers}; does-not clause: {dn} -> {v}")
overall = ver["loc"] if ver["loc"] == ver["tr"] else "not resolved"
out.append(f"OVERALL (rule of prodt.py): {overall}")
if cl:
    out.append("measured only: -I minus clear, t=1")
    for k in d0:
        if "t=1 " not in k: continue
        a, b = d0[k], cl[k]
        for q in ("rho", "R2_held", "R2_held_L1Y"):
            e = math.hypot(a[q + "_se"], b[q + "_se"]); out.append(f"  {k} {q}: {a[q]:.5f} - {b[q]:.5f} = {a[q]-b[q]:.5f} ({e:.5f}) z {(a[q]-b[q])/e:.2f}")
with open(sys.argv[1], "x") as fh: fh.write("\n".join(out) + "\n")
print("\n".join(out))
