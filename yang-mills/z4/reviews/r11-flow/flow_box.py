"""
flow_box.py (r11-flow). Diagnosis of the failed predicate P5 of flow_bench run1 (s = 0.01).
Hypothesis (stated before this run): the lattice values converge to the CONTINUUM BOX sum
  B2_box(s) = l^-3 sum_{k in (2pi/l)Z^3, k != 0} ((k1^2+k2^2)/|k|^2)(|k|/2) exp(-2 s |k|^2),
which differs from the infinite-volume 1/(48 pi^2 s^2) by images of a power-law (~r^-4) kernel,
relative size ~ s^2/l^4, not exp(-l^2/8s) as assumed in flow_bench's P5 tolerance.
PREDICATES:
 Q1 |B2_rich / B2_box - 1| <= 2e-3 for s in {0.002, 0.005, 0.01}, B2_rich from results_flow_run1.json
    (tolerance: P4 measured N=64->96 changes <= 9e-3 for B2; Richardson removes the b^2 term, the
    b^4 remainder is ~(b^2/6s)^2 <= 3e-3 at s = 0.002 -> 2e-3 for the smaller s-values is the
    stated margin; s = 0.002 is the hardest case).
 Q2 (1 - B2_box * 48 pi^2 s^2) / s^2 is constant in s within 10% (finite-volume correction ~ s^2).
Sum: |n_i| <= 60, tail bounded by exp(-2 s (2 pi 60)^2) * (polynomial) < 1e-100: negligible.
"""
import json, os, sys, math
import numpy as np
out = 'results_box_run1.json'
if os.path.exists(out): print('refusing to overwrite'); sys.exit(3)
res = json.load(open('results_flow_run1.json'))
n = np.arange(-60, 61); k = 2 * math.pi * n
K1, K2, K3 = np.meshgrid(k, k, k, indexing='ij'); kk2 = K1**2 + K2**2 + K3**2
ok = True; rows = {}
for s in (0.002, 0.005, 0.01):
    with np.errstate(invalid='ignore', divide='ignore'):
        t = np.where(kk2 > 0, (K1**2 + K2**2) / np.where(kk2 > 0, kk2, 1) * np.sqrt(kk2) / 2 * np.exp(-2 * s * kk2), 0)
    box = float(t.sum()); rich = res['cases'][str(s)]['richardson']['B2']
    inf = 1 / (48 * math.pi**2 * s**2)
    q1 = abs(rich / box - 1)
    rows[s] = dict(box=box, rich=rich, inf=inf, rel_rich_box=q1, fv_coef=(1 - box / inf) / s**2)
    print(s, rows[s], 'Q1', 'MET' if q1 <= 2e-3 else 'FAILED'); ok &= q1 <= 2e-3
c = [rows[s]['fv_coef'] for s in rows]; q2 = (max(c) - min(c)) / max(c) <= 0.10
print('Q2 fv coefficients', c, 'MET' if q2 else 'FAILED'); ok &= q2
json.dump(dict(rows={str(s): r for s, r in rows.items()}, Q2=bool(q2)), open(out, 'w'), indent=1)
sys.exit(0 if ok else 1)
