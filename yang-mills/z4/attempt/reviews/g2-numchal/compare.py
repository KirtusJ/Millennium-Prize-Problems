#!/usr/bin/env python3
"""
compare.py -- my Nystrom m_e (and 2nd ee level, m_eo) vs the NUMERICS.md table 2b.
PREDICATE (fixed before first run), per beta, for m_e and the 2nd ee level:
  |mine_refined - target| <= 5e-9 + |mine_refined - mine_base|
  (5e-9 = rounding of the 8-decimal table; |refined-base| = my own discretisation-error estimate).
  For m_eo (beta<=64, 5 significant digits in table): relative diff <= 5e-5 + rel |refined-base|.
"Hypothesis per case" (rule 4): a beta qualifies if both a base and a refined run exist.
Exit 0 iff every qualifying case meets the predicate.
"""
import json, glob, sys, math
T = {2: (1.63761996, 1.88234137, 5.4390e-01), 4: (0.76319885, 0.99450927, 1.3393e-01),
     8: (0.51558519, 0.61668249, 1.4768e-02), 16: (0.54142013, 0.60392748, 3.2111e-04),
     32: (0.51516418, 0.54929832, 7.6936e-07), 64: (0.43994233, 0.45571058, 8.9923e-11),
     128: (0.36450079, 0.37215008, None), 256: (0.29712330, 0.30088500, None),
     512: (0.23982321, 0.24168615, None), 1024: (0.19238313, 0.19330933, None)}
runs = {}
for f in glob.glob('results/spec_b*.json'):
    d = json.load(open(f)); runs.setdefault(int(d['beta']), []).append(d)
rows, met, failed, q = [], 0, 0, 0
for b in sorted(T):
    rs = sorted(runs.get(b, []), key=lambda d: d['na'])
    if len(rs) < 2:
        rows.append(f'{b}: does not qualify ({len(rs)} runs)'); continue
    q += 1
    base, ref = rs[0], rs[-1]
    for key, i in (('m_e', 0), ('m_e2', 1)):
        diff = abs(ref[key] - T[b][i]); tol = 5e-9 + abs(ref[key] - base[key])
        ok = diff <= tol; met += ok; failed += (not ok)
        rows.append(f'{b:5d} {key:5s} mine {ref[key]:.10f} target {T[b][i]:.8f} diff {diff:.1e} tol {tol:.1e} {"MET" if ok else "FAILED"}')
    if T[b][2] is not None:
        rel = abs(ref['m_eo'] / T[b][2] - 1); tol = 5e-5 + abs(ref['m_eo'] / base['m_eo'] - 1)
        ok = rel <= tol; met += ok; failed += (not ok)
        rows.append(f'{b:5d} m_eo  mine {ref["m_eo"]:.6e} target {T[b][2]:.4e} rel {rel:.1e} tol {tol:.1e} {"MET" if ok else "FAILED"}')
    rows.append(f'{b:5d} m_e*b^(1/3) = {ref["m_e"] * b ** (1/3):.6f}')
rows.append(f'qualifying betas {q}; predicates met {met}, failed {failed}')
with open(sys.argv[1], 'x') as f:
    f.write('\n'.join(rows) + '\n')
print('\n'.join(rows))
sys.exit(0 if failed == 0 else 1)
