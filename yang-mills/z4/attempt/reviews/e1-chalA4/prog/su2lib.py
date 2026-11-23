"""Shared SU(2) quaternion helpers for e1-chalA4 programs (no predicates here)."""
import numpy as np

def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([a0*b0 - a1*b1 - a2*b2 - a3*b3,
                     a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1,
                     a0*b3 + a1*b2 - a2*b1 + a3*b0], axis=-1)

def qinv(a):
    return a * np.array([1., -1., -1., -1.])

def shift(A, mu, k):
    """A[x] -> A[x + k e_mu] (periodic); lattice axes are 0..3, last axis quaternion."""
    return np.roll(A, -k, axis=mu)

def plaq12(U):
    """Positive 12-face holonomy based at x, steps [+1,+2,-1,-2]: U1(x) U2(x+e1) U1(x+e2)^-1 U2(x)^-1."""
    U1, U2 = U[1], U[2]
    return qmul(qmul(U1, shift(U2, 1, 1)), qmul(qinv(shift(U1, 2, 1)), qinv(U2)))

def plaq(U, mu, nu):
    return qmul(qmul(U[mu], shift(U[nu], mu, 1)), qmul(qinv(shift(U[mu], nu, 1)), qinv(U[nu])))

def rooted_faces(U, s, offsets, beta):
    """For every line along axis 1 (all x0,x2,x3), root at x1=s; return dict offset->sqrt(beta)*Im(W P W^-1)
    for the 12-face based at x1 = s+offset, W the straight axis-1 path from the root to the base."""
    N = U.shape[2]
    P = plaq12(U)
    out = {}
    for off in offsets:
        b = (s + off) % N
        W = np.zeros(U.shape[1:]); W[..., 0] = 1.0
        W = W[:, 0]  # shape (N0, N2, N3, 4) after selecting x1 below
        Wl = np.zeros_like(U[1][:, 0]); Wl[..., 0] = 1.0
        if off >= 0:
            for m in range(off):
                Wl = qmul(Wl, U[1][:, (s + m) % N])
        else:
            for m in range(1, -off + 1):
                Wl = qmul(Wl, qinv(U[1][:, (s - m) % N]))
        R = qmul(qmul(Wl, P[:, b]), qinv(Wl))
        out[off] = np.sqrt(beta) * R[..., 1:]
    return out

def reflect_axis1(U, s):
    """Site reflection x1 -> 2s - x1 on the torus, applied to the link configuration (theta U)."""
    N = U.shape[2]
    idx = (2*s - np.arange(N)) % N
    V = np.empty_like(U)
    for mu in (0, 2, 3):
        V[mu] = U[mu][:, idx]
    # link (x, x+e1) maps to (thx, thx-e1) = inverse of U1 at thx - e1
    V[1] = qinv(U[1][:, (idx - 1) % N])
    return V

def random_su2(rng, shape):
    q = rng.normal(size=shape + (4,))
    return q / np.linalg.norm(q, axis=-1, keepdims=True)
