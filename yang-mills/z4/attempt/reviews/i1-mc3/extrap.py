#!/usr/bin/env python3
"""extrap.py -- MEASURED ONLY (no predicate): weighted least-squares extrapolation of m beta^(1/3) in x = beta^(-1/3).
Forms: (i) e + a x on beta = 256, 1024, 4096; (ii) e + a x + b x^2 on beta = 64..4096. Input: analysis json files.
Errors: from the covariance of the weighted fit (statistical only; no systematic from the form). Usage: python3 extrap.py OUT.md a.json ...
Output opened with mode "x"."""
import sys, json, numpy as np
f = open(sys.argv[1], 'x')
for path in sys.argv[2:]:
    runs = json.load(open(path))['runs']
    f.write(f"\n## {path}\n")
    for ch, e0 in (('E', 3.012539), ('T2', 3.012539), ('A1', 3.602838)):
        pts = sorted([(r['beta'], r['ch'][ch]['mb3'], r['ch'][ch]['mb3_err']) for r in runs if r['D'] == 3 and r['beta'] >= 64 and r['ch'][ch]['PLAT']])
        for name, bmin, deg in (('e+a x (beta>=256)', 256, 1), ('e+a x+b x^2 (beta>=64)', 64, 2)):
            p = [q for q in pts if q[0] >= bmin]
            if len(p) <= deg: continue
            x = np.array([q[0] ** (-1 / 3) for q in p]); y = np.array([q[1] for q in p]); s = np.array([q[2] for q in p])
            A = np.vstack([x ** k for k in range(deg + 1)]).T / s[:, None]
            cov = np.linalg.inv(A.T @ A); c = cov @ A.T @ (y / s)
            chi2 = float(np.sum((A @ c - y / s) ** 2)); dof = len(p) - deg - 1
            f.write(f"- {ch} {name}: e = {c[0]:.4f} +- {np.sqrt(cov[0,0]):.4f} (prediction {e0}; z = {(c[0]-e0)/np.sqrt(cov[0,0]):+.2f}), a = {c[1]:+.3f}, chi2/dof = {chi2:.2f}/{dof}\n")
f.close()
