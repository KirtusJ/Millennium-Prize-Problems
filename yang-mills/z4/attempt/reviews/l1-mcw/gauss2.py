#!/usr/bin/env python3
"""gauss2.py -- l1-mcw. Single-plaquette Gaussian correlator (measured only; to locate the auditor's weight 0.046875).
C_single(t) = (3/2) Pi_pq^2, p = spatial plaquette (site 0, plane 12) at time t, q = same at time 0.
Also mixed: single p at t vs box operators at 0. Predicate S1: C_single(0) == var_spatial_single of gauss.py (1e-12).
Expectation before run: weight of the 3.525 atom relative to C_single(0) is 0.046875 if the auditor meant the single plaquette.
USAGE: python3 gauss2.py OUT.json T"""
import sys, json, math
import numpy as np
from gauss import build
out = open(sys.argv[1], 'x'); T = int(sys.argv[2])
B, meta, V = build(T); U, s, Vt = np.linalg.svd(B, full_matrices=False)
rank = int(np.sum(s > 1e-9 * s.max())); Q = U[:, :rank]; Pi = Q @ Q.T
meta = np.array(meta); tt, mu, nu = meta.T
# plaquette index = 6*site + pair index; site 0 at time t is site index t*8; pair (1,2) is index 3
pairs = [(a, b) for a in range(4) for b in range(a + 1, 4)]; k12 = pairs.index((1, 2))
p = lambda t: 6 * (t * 8) + k12
TM = T // 2 + 1
Cs = np.array([1.5 * Pi[p(t), p(0)] ** 2 for t in range(TM)])
k = np.array([Pi[p(t), p(0)] for t in range(TM)])
E1 = 2 * math.acosh(3)
r = {'T': T, 'C0': Cs[0], 'R': list(Cs / Cs[0]), 'k': list(k),
     'meff': [float(x) for x in np.log(Cs[:-1] / Cs[1:])],
     'w_est': [float(Cs[t] * math.exp(E1 * t) / Cs[0]) for t in range(1, min(9, TM))],
     'kmeff': [float(x) for x in np.log(np.abs(k[:-1] / k[1:]))]}
r = {a: (float(b) if np.isscalar(b) else [float(x) for x in b]) for a, b in r.items()}
print(json.dumps(r)); json.dump(r, out, indent=1); out.close()
