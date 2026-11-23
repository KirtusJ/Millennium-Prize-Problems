"""ff_q7.py -- A6 check redone with informative points (c2-chalS).
Truncated 4-point function of :phi^2: for the lattice free field (m=1/8), points a unit square in the (1,2)-plane
(0,0,0,0),(0,1,0,0),(0,1,1,0),(0,0,1,0). Wick: T4 = 16[G12G23G34G41 + G13G32G24G41 + G12G24G43G31].
PREDICATES (fixed before run):
 R1  T4 > 0 and T4 / (s.e. of the Monte Carlo estimate) >= 20 (informative; 20 = my choice so a 5-s.e. test can
     distinguish T4 from 0).
 R2  Monte Carlo (seed 20261123, 4e6 samples, Gaussian vector with the lattice covariance) truncated 4-pt agrees
     with T4 within 5 s.e. (5 s.e.: two-sided false-alarm < 1e-6 for a Gaussian estimator).
 R3  truncated 4-pt of the field phi itself (MC) is within 5 s.e. of 0 (Gaussian; control).
Output ff_q7.out (mode "x").
"""
import math, sys, numpy as np
sys.path.insert(0, '.')
from ff_check import G
m = 1/8
P = [(0,0,0,0),(0,1,0,0),(0,1,1,0),(0,0,1,0)]
C = np.array([[G(tuple(p[i]-q[i] for i in range(4)), m) for q in P] for p in P])
g = lambda i,j: C[i,j]
T4 = 16*(g(0,1)*g(1,2)*g(2,3)*g(3,0) + g(0,2)*g(2,1)*g(1,3)*g(3,0) + g(0,1)*g(1,3)*g(3,2)*g(2,0))
rng = np.random.default_rng(20261123)
L = np.linalg.cholesky(C)
pairs = [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
def trunc(V):
    prod = np.prod(V, axis=1)
    est = prod.mean() - sum(np.mean(V[:,p[0]]*V[:,p[1]])*np.mean(V[:,q[0]]*V[:,q[1]]) for p,q in pairs)
    return est, prod.std()/math.sqrt(len(prod))
acc = []
for chunk in range(4):
    X = rng.standard_normal((1_000_000, 4)) @ L.T
    acc.append(X)
X = np.vstack(acc)
W = X**2 - np.diag(C)
e2, s2 = trunc(W); e1, s1 = trunc(X)
out = open('ff_q7.out', 'x')
def w(s): print(s); out.write(s+'\n')
w(f"cov diag {np.diag(C)} offdiag G(e1)={C[0,1]:.6f} G(e1+e2)={C[0,2]:.6f}")
w(f"Wick T4(:phi^2:) = {T4:.6e}; MC = {e2:.6e} +- {s2:.2e}; phi truncated MC = {e1:.3e} +- {s1:.2e}")
r = {"R1": T4 > 0 and T4/s2 >= 20, "R2": abs(e2-T4) <= 5*s2, "R3": abs(e1) <= 5*s1}
for k in r: w(f"PREDICATE {k}: {'MET' if r[k] else 'FAILED'}")
out.close()
