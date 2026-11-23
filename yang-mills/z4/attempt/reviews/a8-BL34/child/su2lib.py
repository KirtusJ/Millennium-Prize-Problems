"""Shared helpers. SU(2) element exp(i sigma.x) = a + i b.sigma stored as quaternion (a,b1,b2,b3).
Product: (a,b)(a',b') = (aa'-b.b', a b'+a' b - b x b').  Inverse: (a,-b).  (1/2)Tr = a."""
import numpy as np, itertools
def qmul(p, q):
    a, b = p[..., :1], p[..., 1:]
    c, d = q[..., :1], q[..., 1:]
    return np.concatenate([a*c - (b*d).sum(-1, keepdims=True),
                           a*d + c*b - np.cross(b, d)], -1)
def qinv(q): return np.concatenate([q[..., :1], -q[..., 1:]], -1)
def qexp(x):
    n = np.linalg.norm(x, axis=-1, keepdims=True)
    s = np.where(n > 1e-12, np.sin(n)/np.where(n > 1e-12, n, 1), 1.0)
    return np.concatenate([np.cos(n), s*x], -1)
# interior links: id = 2*mu + (0 if s=+1 else 1); id 0 = (mu0,+) pinned
def lid(mu, s): return 2*mu + (0 if s == 1 else 1)
PLAQ = [(mu, nu, s, t) for mu in range(4) for nu in range(mu+1, 4) for s in (1, -1) for t in (1, -1)]
assert len(PLAQ) == 24
PA = np.array([lid(m, s) for m, n, s, t in PLAQ]); PB = np.array([lid(n, t) for m, n, s, t in PLAQ])
def plaq_index(mu, nu, s, t): return PLAQ.index((mu, nu, s, t))
def Dmatrix():
    """24x7 incidence of d on the unknown links (ids 1..7), shell set to 0."""
    D = np.zeros((24, 8))
    for p, (m, n, s, t) in enumerate(PLAQ):
        D[p, lid(m, s)] += 1; D[p, lid(n, t)] -= 1
    return D[:, 1:]
def S_action(q, V1, V2):
    """q: (...,8,4) interior link quaternions (q[...,0,:]=identity); V1,V2: (24,4) shell quats
    (V1 = V(s e_mu -> s e_mu+t e_nu), V2 = V(t e_nu -> s e_mu+t e_nu)). Returns sum(1-cos alpha_p)."""
    W = qmul(V1, qinv(V2))
    Up = qmul(qmul(q[..., PA, :], W), qinv(q[..., PB, :]))
    return (1 - Up[..., 0]).sum(-1)
