#!/usr/bin/env python3
"""
fits.py -- A4/A5: extrapolation of the TABULATED m_e beta^{1/3} (NUMERICS.md table 2b).
Data: beta = 2^k, k=1..10, values to 6 decimals (rounding 5e-7 -> data tolerance 1e-6).

PREDICATES (fixed before the first run):
 F1 (A4) fit y = E + c beta^{-2/3} to beta = 128..1024 (4 points, least squares):
    |E - 1.974964| < 3*sigma_E, sigma_E = max(least-squares standard error, spread of E over
    the leave-one-out 3-point fits). (tolerance: statistical + model spread; no other source.)
 F2 (A5) free-exponent fit y = E + c beta^{-p} on beta = 128..1024: |p - 2/3| < 0.1.
    (tolerance: chosen a priori as 'distinguishes 2/3 from 1/3 and from 1')
 F3 (A5) the model y = E + c beta^{-1/3} on beta=128..1024 has rms residual > 10 x that of the
    beta^{-2/3} model (i.e. it is clearly worse).
 Measured only: E from 3-term fits, logarithmic model E + c/ln(beta), geometric extrapolation.
"""
import sys, json
import numpy as np

beta = 2.0 ** np.arange(1, 11)
y = np.array([2.063272, 1.211503, 1.031170, 1.364293, 1.635544, 1.759769, 1.836969, 1.886615, 1.918586, 1.939100])
E1 = 1.974964


def lsq(X, yy):
    c, *_ = np.linalg.lstsq(X, yy, rcond=None)
    r = yy - X @ c
    dof = len(yy) - X.shape[1]
    s2 = (r @ r) / dof if dof > 0 else 0.0
    cov = s2 * np.linalg.inv(X.T @ X)
    return c, r, np.sqrt(np.diag(cov))


def fit(model, idx):
    b = beta[idx]; yy = y[idx]
    cols = {'p23': [np.ones_like(b), b ** (-2 / 3)],
            'p13': [np.ones_like(b), b ** (-1 / 3)],
            'p13_23': [np.ones_like(b), b ** (-1 / 3), b ** (-2 / 3)],
            'p23_43': [np.ones_like(b), b ** (-2 / 3), b ** (-4 / 3)],
            'p23_1': [np.ones_like(b), b ** (-2 / 3), b ** (-1.0)],
            'log': [np.ones_like(b), 1 / np.log(b)],
            'log2': [np.ones_like(b), 1 / np.log(b), 1 / np.log(b) ** 2]}[model]
    X = np.array(cols).T
    c, r, se = lsq(X, yy)
    return dict(model=model, betas=b.tolist(), E=float(c[0]), seE=float(se[0]), coef=c.tolist(),
                rms=float(np.sqrt(np.mean(r ** 2))), maxres=float(np.max(np.abs(r))))


def freep(idx):
    best = None
    for p in np.linspace(0.05, 2.0, 3901):
        b = beta[idx]
        X = np.array([np.ones_like(b), b ** (-p)]).T
        c, r, _ = lsq(X, y[idx])
        s = r @ r
        if best is None or s < best[0]:
            best = (s, p, c[0])
    return dict(p=float(best[1]), E=float(best[2]), rms=float(np.sqrt(best[0] / len(idx))))


out = {}
last4 = np.arange(6, 10)
f1 = fit('p23', last4)
loo = [fit('p23', np.delete(last4, i))['E'] for i in range(4)]
sig = max(f1['seE'], max(loo) - min(loo))
out['F1'] = dict(fit=f1, loo_E=loo, sigma=sig, dev=f1['E'] - E1, met=bool(abs(f1['E'] - E1) < 3 * sig))
fp = freep(last4)
out['F2'] = dict(freep_last4=fp, freep_last5=freep(np.arange(5, 10)), met=bool(abs(fp['p'] - 2 / 3) < 0.1))
f13 = fit('p13', last4)
out['F3'] = dict(p13=f13, ratio_rms=f13['rms'] / f1['rms'], met=bool(f13['rms'] > 10 * f1['rms']))
mo = {}
for m in ['p23', 'p13', 'p13_23', 'p23_43', 'p23_1', 'log', 'log2']:
    for lo in [4, 5, 6]:
        idx = np.arange(lo, 10)
        if len(idx) >= 3 or m in ['p23', 'p13', 'log']:
            mo[f'{m}_from_beta{int(beta[lo])}'] = fit(m, idx)
out['measured'] = mo
inc = np.diff(y[4:])
out['increments'] = inc.tolist()
out['inc_ratios'] = (inc[1:] / inc[:-1]).tolist()
q = inc[-1] / inc[-2]
out['geometric_extrap'] = float(y[-1] + inc[-1] * q / (1 - q))
out['local_exponent_dist'] = (1 / 3 - (1 - np.log2(y[1:] / y[:-1])) * 0 - (1/3 - np.log2(y[1:]/y[:-1])) ).tolist()
with open(sys.argv[1], 'x') as f:
    json.dump(out, f, indent=1)
print(json.dumps({k: v for k, v in out.items() if k != 'measured'}, indent=1))
for k, v in mo.items():
    print(f"{k:22s} E={v['E']:.5f} +- {v['seE']:.5f}  rms={v['rms']:.2e} maxres={v['maxres']:.2e}")
sys.exit(0 if all(out[k]['met'] for k in ['F1', 'F2', 'F3']) else 1)
