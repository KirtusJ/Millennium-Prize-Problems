"""model1d_ext.py -- extension of model1d.py to larger beta (same model, same identity method).
Predicates (fixed before first run):
 E1 fit -log m = c sqrt(beta) + b log beta + c0 over beta in {256,1024,4096,9216,16384}: |c - c*|/c* < 0.005
    (my expectation: WKB prefactor is a power of beta times constant; tolerance chosen as half of M5's).
 E2 local slope between 9216 and 16384 within 1% of c*.
 E3 theta=1 vs 0.9 at 16384: |dlog m| < 1e-6 (round-off check, as M3).
"""
import numpy as np, json, sys
from model1d import split_identity, cstar
tag = sys.argv[1]; c = cstar(); P = {}; rows = []
for beta in (256, 1024, 4096, 9216, 16384):
    r = split_identity(beta); rows.append(dict(beta=beta, logm=r['logm'], ratio=-r['logm']/np.sqrt(beta))); print(rows[-1], flush=True)
r2 = split_identity(16384, theta=0.9); P['E3'] = abs(r2['logm']-rows[-1]['logm']) < 1e-6
b = np.array([r['beta'] for r in rows], float); y = -np.array([r['logm'] for r in rows])
coef = np.linalg.lstsq(np.c_[np.sqrt(b), np.log(b), np.ones_like(b)], y, rcond=None)[0]
sl = (y[-1]-y[-2])/(np.sqrt(b[-1])-np.sqrt(b[-2]))
P['E1'] = abs(coef[0]-c)/c < 0.005; P['E2'] = abs(sl-c)/c < 0.01
out = dict(rows=rows, fit=list(coef), last_slope=sl, predicates=P, failed=[k for k, v in P.items() if not v])
print(out)
with open(f'results/model1d_ext_{tag}.json', 'x') as fh: json.dump(out, fh, indent=1, default=float)
sys.exit(0 if not out['failed'] else 1)
