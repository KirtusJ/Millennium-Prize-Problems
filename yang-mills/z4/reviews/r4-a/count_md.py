"""Count .md files in input/.
Predicates fixed before first run:
 P1: total .md under input/ == 28 (hypothesis from ls listing before the script)
 P2: observable-normalization lane has 27 .md, volume-uniformity lane has 1 .md
 P3: execution.md files in obs-norm == 11 (pure receipts, used only for evidence column)
Tolerance: exact integer counts (no tolerance). Result file count_result.json is never overwritten.
Exit 0 iff all predicates met, 1 otherwise.
"""
import json, os, sys
root = "input"
md = sorted(os.path.join(d, f).replace("\\", "/") for d, _, fs in os.walk(root) for f in fs if f.endswith(".md"))
obs = [p for p in md if "/observable-normalization/" in p]
vol = [p for p in md if "/volume-uniformity/" in p]
exe = [p for p in obs if p.endswith("execution.md")]
res = {"total": len(md), "obs": len(obs), "vol": len(vol), "obs_execution": len(exe),
       "P1": len(md) == 28, "P2": len(obs) == 27 and len(vol) == 1, "P3": len(exe) == 11, "files": md}
out = "count_result.json"
if os.path.exists(out):
    print("result file exists; not overwriting"); sys.exit(2)
json.dump(res, open(out, "w"), indent=1)
print({k: v for k, v in res.items() if k != "files"})
sys.exit(0 if res["P1"] and res["P2"] and res["P3"] else 1)
