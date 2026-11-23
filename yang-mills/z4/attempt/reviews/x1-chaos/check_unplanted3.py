"""check_unplanted3.py -- resolve the reading of "deficit 7.33 to 14.23" (tun_upper.tex 101, 564-565).
Predicate (fixed before run): U1b: min over (beta in 100..4096, s in [0.1,1] grid 901) of the deficit is within 0.01
of 7.33 (i.e. the note's range is the joint range over (beta,s), not the range of the s-maximised deficit).
Output check_unplanted3.json (mode "x"). Imports deficit() from check_unplanted2.py by exec of its function source only.
"""
import json, math
import numpy as np
src = open("check_unplanted2.py").read()
start = src.index("def deficit"); end = src.index("res = {}")
exec(src[start:end])
ss = np.linspace(0.1, 1, 901)
best = (1e9, None, None)
for b in range(100, 4097):
    for s in ss:
        d = deficit(b, s)
        if d < best[0]:
            best = (d, b, float(s))
res = {"joint_min": best[0], "beta": best[1], "s": best[2], "U1b_met": abs(best[0] - 7.33) <= 0.01}
json.dump(res, open("check_unplanted3.json", "x"), indent=1)
print(res)
