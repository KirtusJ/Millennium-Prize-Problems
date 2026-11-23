"""check_line769.py -- referee 6's claim on tun_lower.tex line 769 (unplanted text).
Predicate (fixed before run): L769: the written chain 2.65+3.61/eta < 4.53/eta holds for all eta on a grid of (0,0.4]
(4000 points). Measured: the set where it fails; max sinh(eta)/eta on (0,0.4] versus the cited 1.03 and the needed
4.656/4.53 = 1.02781. Output check_line769.json (mode "x").
"""
import json, math
import numpy as np
eta = np.linspace(1e-4, 0.4, 4000)
fail = eta[2.65 + 3.61 / eta >= 4.53 / eta]
r = np.sinh(eta) / eta
res = {"cases": int(eta.size), "chain_holds": int(eta.size - fail.size), "chain_fails": int(fail.size),
       "fail_from_eta": float(fail.min()) if fail.size else None, "max_sinh_over_eta": float(r.max()),
       "needed_ratio": 4.656 / 4.53, "L769_met": fail.size == 0}
json.dump(res, open("check_line769.json", "x"), indent=1)
print(res)
