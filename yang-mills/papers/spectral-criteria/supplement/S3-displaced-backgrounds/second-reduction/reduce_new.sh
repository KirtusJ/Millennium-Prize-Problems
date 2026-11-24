#!/bin/bash
set -e
python3 reduce_fixed.py stream results/N-d2 results_fixed/new-N-d2.json
python3 reduce_fixed.py stream results/N-d0 results_fixed/new-N-d0.json
python3 reduce_fixed.py ratio results_fixed/new-N-d2.json results_fixed/new-N-d0.json results_fixed/new-ratio-Nd2-Nd0.json
python3 - <<'PY'
import json
q=json.load(open("results_fixed/new-ratio-Nd2-Nd0.json"))["r1"]
Q,e=q["Q"],q["err_independent"]; tol=2*(e*e+0.011**2)**0.5
print(f"R5: Q1={Q:.4f}({e:.4f}) |Q1-1.016|={abs(Q-1.016):.4f} tol={tol:.4f} ->", "reproduced" if abs(Q-1.016)<=tol else "not reproduced")
print(f"measured: (Q1-1)/e = {(Q-1)/e:+.2f}")
PY
