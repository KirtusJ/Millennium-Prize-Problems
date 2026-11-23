"""A1 exact identity test (own program, independent of target's check_strip.py).

Setting: 4D periodic lattice N=8, random (Haar and near-identity) SU(2) link configurations, seeds fixed.
Root at x1 = s on every axis-1 line; faces transported along the straight axis-1 path from the root
(this is the target's 're-rooting on the midpoint plane').  Pair sums D_j = F(a+2j)+F(a+2j+1).
theta = site reflection x1 -> 2s - x1, s = a+j+k+1.

PREDICATES (fixed before first run):
 R1 (for all j<k with k-j in {1,2,3}, all s, all lines, all 3 colours, 4 configs):
     D_k[theta U] == -D_j[U] componentwise, |diff| <= 1e-12 (tolerance: double rounding of <= 12 quaternion products).
 R2 (negative control, expected to FAIL the identity): same with s shifted by one (s = a+j+k):
     max |D_k[theta U] + D_j[U]| > 1e-3 on Haar-random configs.
 R3 (frame test): root moved to x1 = a (not on the reflection plane), i.e. faces transported from a
     (prefix path a->s then straight): dot products D_j.D_k equal those at root s to 1e-12 configuration by
     configuration (common conjugation, target 'returning to the original root').
 R4 (negative control of the colour frame): with root a, componentwise identity D_k[theta U] == -D_j[U]
     fails (> 1e-3) on Haar configs: the per-component identity needs the root on the plane.
"""
import sys, numpy as np
from su2lib import *

N = 8
rng = np.random.default_rng(20261123)
cfgs = []
for c in range(2):
    cfgs.append(random_su2(rng, (4, N, N, N, N)))
for eps in (0.1, 0.3):
    q = np.concatenate([np.ones((4, N, N, N, N, 1)), eps*rng.normal(size=(4, N, N, N, N, 3))], axis=-1)
    cfgs.append(q/np.linalg.norm(q, axis=-1, keepdims=True))

def pairs(U, s, a, j, k, beta=1.0, root_shift=None):
    offs = [a+2*j-s, a+2*j+1-s, a+2*k-s, a+2*k+1-s]
    f = rooted_faces(U, s, offs, beta)
    return f[offs[0]]+f[offs[1]], f[offs[2]]+f[offs[3]]

res = {"R1": [0, 0, 0.0], "R2": [0, 0, 0.0], "R3": [0, 0, 0.0], "R4": [0, 0, 0.0]}
for ci, U in enumerate(cfgs):
    for a in range(N):
        for d in (1, 2, 3):
            j, k = 0, d
            s = a+j+k+1
            Dj, Dk = pairs(U, s, a, j, k)
            V = reflect_axis1(U, s % N)
            Djr, Dkr = pairs(V, s, a, j, k)
            e = np.abs(Dkr + Dj).max()
            res["R1"][0 if e <= 1e-12 else 1] += 1; res["R1"][2] = max(res["R1"][2], e)
            # R2 wrong plane
            s2 = a+j+k
            Dj2, Dk2 = pairs(U, s2, a, j, k)
            V2 = reflect_axis1(U, s2 % N)
            Djr2, Dkr2 = pairs(V2, s2, a, j, k)
            e2 = np.abs(Dkr2 + Dj2).max()
            if ci < 2:
                res["R2"][0 if e2 > 1e-3 else 1] += 1; res["R2"][2] = max(res["R2"][2], e2)
            # R3/R4 root at a: path a->s then straight; equivalent to rooting at a directly (straight line)
            Dja, Dka = pairs(U, a, a, j, k)
            e3 = np.abs((Dja*Dka).sum(-1) - (Dj*Dk).sum(-1)).max()
            res["R3"][0 if e3 <= 1e-12 else 1] += 1; res["R3"][2] = max(res["R3"][2], e3)
            Djar, Dkar = pairs(V, a, a, j, k)   # same definition evaluated on theta U, root a
            e4 = np.abs(Dkar + Dja).max()
            if ci < 2:
                res["R4"][0 if e4 > 1e-3 else 1] += 1; res["R4"][2] = max(res["R4"][2], e4)
with open("../results/reflect_exact.txt", "x") as fh:
    for key, (m, f, mx) in res.items():
        line = f"{key}: met {m}, failed {f}, max|diff| {mx:.3e}"
        print(line); fh.write(line+"\n")
sys.exit(0 if all(res[k][1] == 0 for k in res) else 1)
