"""Q1 table (a2-mixb): reads results_q1/<tag>/<summary file> and prints a markdown table to stdout and to
results_q1/table_<n>.md (mode 'x'). For runs that failed a hot/cold check, the rerun (-r) is used if it passed all
checks; if the rerun also fails, NO number is printed (rule in run_q1.py). Ratios relative to d0 at the same beta,
errors combined in quadrature (independent runs)."""
import json, sys, math
from pathlib import Path
R = Path(__file__).resolve().parent / "results_q1"
def load(tag):
    for f in ("summary_full.json", "summary.json"):
        if (R / tag / f).exists(): return json.load(open(R / tag / f))
def ok(s): return all(v["verdict"] == "MET" for v in s["checks"].values() if isinstance(v, dict))
rows = []
for b, bt in ((6.0, "b6"), (12.0, "b12")):
    names = [("d0", "0"), (f"{bt}-k1", "1/beta"), (f"{bt}-k2", "2/beta"), (f"{bt}-k4", "4/beta"), ("fix-k1", "0.30524"), ("fix-k2", "0.61048"), ("fix-k4", "1.22095")]
    base = None
    for s, lab in names:
        tag = f"q1-{bt}-{s}"; sm = load(tag); used = tag; note = "first run"
        if sm is None: rows.append(f"| {b:g} | {lab} | not run |"); continue
        if not ok(sm):
            fails = ",".join(k for k, v in sm["checks"].items() if isinstance(v, dict) and v["verdict"] != "MET")
            r = load(tag + "-r")
            if r is None: rows.append(f"| {b:g} | {lab} | {sm['min_angle']:.4f} | NO NUMBER (first run failed {fails}; rerun pending/not run) |"); continue
            if not ok(r):
                f2 = ",".join(k for k, v in r["checks"].items() if isinstance(v, dict) and v["verdict"] != "MET")
                rows.append(f"| {b:g} | {lab} | {sm['min_angle']:.4f} | NO NUMBER (first run failed {fails}; rerun failed {f2}) |"); continue
            sm, used, note = r, tag + "-r", f"rerun (first failed {fails})"
        p = sm["pooled"]; f = lambda k, d=4: f"{p[k][0]:.{d}g}({p[k][1]:.2g})"
        if s == "d0": base = p
        rel = lambda k: (p[k][0] / base[k][0], p[k][0] / base[k][0] * math.hypot(p[k][1] / p[k][0], base[k][1] / base[k][0]))
        r1, r4 = rel("ratio1"), rel("ratio4")
        z = " ".join(f"{k.replace('T2_ratio','r').replace('T2','')}:{v['z']:+.2f}" for k, v in sm["checks"].items() if isinstance(v, dict) and "z" in v)
        rows.append(f"| {b:g} | {lab} | {sm['min_angle']:.4f} | {f('J1')} | {f('var1')} | {f('J4')} | {f('var4')} | {f('ratio1')} | {f('ratio4')} | "
                    f"{b*p['ratio1'][0]:.4f}({b*p['ratio1'][1]:.2g}) | {b*p['ratio4'][0]:.4f}({b*p['ratio4'][1]:.2g}) | {r1[0]:.3f}({r1[1]:.3f}) | {r4[0]:.3f}({r4[1]:.3f}) | "
                    f"{f('spread')} | {sm['stream_sd']['ratio1']:.4f}, {sm['stream_sd']['ratio4']:.4f} | {z} | {p['mean_tries'][0]:.1f} | {used} ({note}) |")
hdr = ("| beta | delta | min angle | J1 | Var1 | J4 | Var4 | J1/Var1 | J4/Var4 | beta*J1/Var1 | beta*J4/Var4 | r1/r1(d0) | r4/r4(d0) | mean spread | stream sd r1, r4 | hot/cold z (r1 r4 plaq spread) | pair tries | run |\n"
       "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
out = hdr + "\n" + "\n".join(rows) + "\n"
print(out)
n = 1
while (R / f"table_{n}.md").exists(): n += 1
open(R / f"table_{n}.md", "x").write(out)
