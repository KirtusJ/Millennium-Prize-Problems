#!/usr/bin/env python3
"""pfit.py -- l1-mcw. Measured only (no pass/fail): power p in A_soft = c beta^-p from the three primary analyses
(48/48/32 chains), fits with m_soft from the same run's winding channel (A1 for PA, E for PE and PS).
chi2(p) with c profiled (weighted LS, jackknife errors, betas independent); report p_min, 1-sigma range (dchi2=1),
and chi2 at p = 0, 1/3, 2/3, 1.
USAGE: python3 pfit.py OUT.json ANA1.md ANA2.md"""
import sys, json, numpy as np
out = open(sys.argv[1], 'x'); recs = []
for f in sys.argv[2:]:
    recs += json.loads(open(f).read().split('```json\n')[1].split('\n```')[0])
res = {}
for op, ch in (('PA', 'A1'), ('PE', 'E'), ('PS', 'E'), ('PS', 'A1')):
    b, A, e = [], [], []
    for r in sorted(recs, key=lambda r: r['beta']):
        fit = [x for x in r[op]['fits'] if x['ch'] == ch and x['src'] == 'run'][0]
        b.append(r['beta']); A.append(fit['A']); e.append(fit['eA'])
    b, A, e = map(np.array, (b, A, e))
    ps = np.linspace(-1, 2.5, 3501); chi = []
    for p in ps:
        f = b ** -p; w = 1 / e ** 2; c = np.sum(w * f * A) / np.sum(w * f * f); chi.append(np.sum(w * (A - c * f) ** 2))
    chi = np.array(chi); i = chi.argmin(); ok = ps[chi <= chi[i] + 1]
    res[op + '_' + ch] = dict(beta=b.tolist(), A=A.tolist(), eA=e.tolist(), p_min=float(ps[i]), p_1sig=[float(ok.min()), float(ok.max())],
                             chi2_min=float(chi[i]), chi2_at={k: float(chi[np.abs(ps - v).argmin()]) for k, v in (('0', 0), ('1/3', 1/3), ('2/3', 2/3), ('1', 1))})
print(json.dumps(res, indent=1)); json.dump(res, out, indent=1); out.close()
