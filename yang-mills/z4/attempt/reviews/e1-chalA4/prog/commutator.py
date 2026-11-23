"""A2 bullet-2 check: derivative of a rooted face whose root path traverses the varied link.
Variation U_e -> exp(eps T_e/sqrt(beta)) U_e with T_e = root generator T transported along the root prefix to e.
PREDICATES (fixed before first run), random configs, seed 7, 200 trials, beta=16:
 C1: finite-difference dF/deps (central, step 1e-5) equals (2/sqrt(beta)) T x F to 1e-6 (tolerance: O(step^2) FD error).
 C2: |dF/deps| <= 2|F|/sqrt(beta) (target's bound 2|F_p||h_e|/sqrt(beta) per traversal, |h_e|=1).
 C3 (negative control): the derivative is NOT zero, i.e. ignoring paths that contain the varied link changes the
     derivative: max |dF/deps| > 1e-3.
"""
import numpy as np, sys
from su2lib import qmul, qinv, random_su2
rng = np.random.default_rng(7); beta = 16.0
def qexp(v):
    t = np.linalg.norm(v); return np.concatenate([[np.cos(t)], np.sin(t)*v/t]) if t > 0 else np.array([1., 0, 0, 0])
c1 = c2 = c3 = 0; mx = 0.
for trial in range(200):
    path = random_su2(rng, (6,)); P = random_su2(rng, ())  # root path of 6 links, face holonomy at the end
    i = rng.integers(0, 6); T = rng.normal(size=3); T /= np.linalg.norm(T)
    W1 = np.array([1., 0, 0, 0])
    for m in range(i): W1 = qmul(W1, path[m])
    Te = qmul(qmul(qinv(W1), np.concatenate([[0.], T])), W1)[1:]
    def F(eps):
        W = np.array([1., 0, 0, 0])
        for m in range(6):
            W = qmul(W, qmul(qexp(eps*Te/np.sqrt(beta)), path[m]) if m == i else path[m])
        return np.sqrt(beta)*qmul(qmul(W, P), qinv(W))[1:]
    h = 1e-5; d = (F(h)-F(-h))/(2*h); F0 = F(0.)
    pred = 2/np.sqrt(beta)*np.cross(T, F0)
    c1 += np.abs(d-pred).max() <= 1e-6; c2 += np.linalg.norm(d) <= 2*np.linalg.norm(F0)/np.sqrt(beta)+1e-9
    mx = max(mx, np.linalg.norm(d))
c3 = mx > 1e-3
s = f"C1 met {c1} failed {200-c1}; C2 met {c2} failed {200-c2}; C3 {'MET' if c3 else 'FAILED'} (max |dF| {mx:.3f})"
open("../results/commutator.txt", "x").write(s+"\n"); print(s)
sys.exit(0 if c1 == 200 and c2 == 200 and c3 else 1)
