"""Check (T239): the child's 'min R' (direction-SUM 4-bin function c.(ind_0+ind_1+ind_2) at one site, class L, c2 HELD)
differs from G4's lambda2 because it is a different function (sum over three lines through a site, not one line of the
direction-pooled law). Predicate: my value equals the child's 0.943850 to 1e-6 (same formula, float rounding)."""
import sys; sys.path.insert(0, "/home/user/z4-workers/f2-cross2/src")
import numpy as np, analysis2 as A
H = A.split(A.load("c2"))[1]
V, E = A.mats(H, "L")
S = np.zeros((54, 4))
for mu in range(3):
    for b in range(4): S[42 + 4 * mu + b, b] = 1
V4 = S.T @ V @ S; E4 = S.T @ E @ S
w, U = np.linalg.eigh(V4); W = U[:, 1:] / np.sqrt(w[1:])
m = np.linalg.eigvalsh(W.T @ E4 @ W).min()
print(f"dir-sum min R = {m:.6f}; child 0.943850; |diff| {abs(m-0.943850):.1e}: {'MET' if abs(m-0.943850)<1e-6 else 'FAILED'}")
print(f"pooled one-line 1-lambda2 = {1-A.pooled_min_R(H):.6f}")
