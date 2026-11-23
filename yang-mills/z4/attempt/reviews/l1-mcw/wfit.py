#!/usr/bin/env python3
"""wfit.py -- l1-mcw. Exact spectral weights of the single spatial plaquette Gaussian correlator (gauss2 output).
Atoms at omega_i+omega_j, cosh omega_m = 1+2m (m=1,2,3: one-photon energies on 2^3, phat^2=4m).
Linear least squares for the 6 weights on t=0..10 (C known to ~1e-16 relative per entry).
Predicate W1: max relative residual over t=0..10 < 1e-6 (tolerance: same as the child's P4; roundoff in Pi^2 grows with t).
Expectation (before run): w1 absolute = 3/64 = 0.046875 (auditor), i.e. w1/C(0) = 0.1522, NOT 0.046875 relative.
USAGE: python3 wfit.py GAUSS2.json OUT.json"""
import sys, json, math, numpy as np
r = json.load(open(sys.argv[1])); out = open(sys.argv[2], 'x')
C = np.array(r['R']) * r['C0']
om = [math.acosh(1 + 2 * m) for m in (1, 2, 3)]
E = sorted({round(om[i] + om[j], 12) for i in range(3) for j in range(i, 3)})
t = np.arange(0, 11); A = np.exp(-np.outer(t, E))
w, *_ = np.linalg.lstsq(A / C[t, None], np.ones(len(t)), rcond=None)
res = np.max(np.abs(A @ w / C[t] - 1))
o = {'E': E, 'w_abs': list(w), 'w_rel': list(w / C[0]), 'C0': C[0], 'maxrelres': float(res), 'W1': bool(res < 1e-6)}
print(json.dumps(o, indent=1)); json.dump(o, out, indent=1); out.close()
