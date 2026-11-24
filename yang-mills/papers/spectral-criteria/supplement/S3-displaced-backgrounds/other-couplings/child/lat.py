"""Shared library: SU(2) quaternion lattice, KP heat bath (checkerboard), marks.
Link array U[mu, x, y, z, t, 4]; site axes 0..3 = x,y,z,t; mu index = axis. Sizes 6,6,6,12."""
import numpy as np
BETA = 3.276133577
DIMS = (6, 6, 6, 12)

def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3,
                     a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2+b0*a2+a3*b1-a1*b3,
                     a0*b3+b0*a3+a1*b2-a2*b1], axis=-1)

def qc(a):
    return a * np.array([1., -1., -1., -1.])

def haar(rng, shape):
    g = rng.standard_normal(shape + (4,))
    return g / np.linalg.norm(g, axis=-1, keepdims=True)

def sh(f, off):
    """f evaluated at (site + off), as array indexed by site."""
    return np.roll(f, shift=tuple(-o for o in off), axis=(0, 1, 2, 3))

def unit(mu, s=1):
    o = [0, 0, 0, 0]; o[mu] = s; return tuple(o)

def add(*offs):
    return tuple(sum(c) for c in zip(*offs))

def kp_w0(rng, alpha):
    """Kennedy-Pendleton: sample w0 with density ∝ sqrt(1-w0^2) exp(alpha w0), vectorised."""
    n = alpha.shape[0]
    out = np.empty(n); pend = np.arange(n)
    while pend.size:
        a = alpha[pend]
        r = 1.0 - rng.random((4, pend.size))
        X = -(np.log(r[0]) + np.log(r[1]) * np.cos(2*np.pi*r[2])**2) / a
        ok = r[3]**2 <= 1.0 - X/2.0
        out[pend[ok]] = 1.0 - X[ok]
        pend = pend[~ok]
    return out

def sample_su2_given_w0(rng, w0):
    v = rng.standard_normal((w0.size, 3)); v /= np.linalg.norm(v, axis=1, keepdims=True)
    s = np.sqrt(np.maximum(1 - w0**2, 0))
    return np.concatenate([w0[:, None], s[:, None]*v], axis=1)

def staples(U, mu):
    S = np.zeros(DIMS + (4,))
    for nu in range(4):
        if nu == mu: continue
        e_mu, e_nu, m_nu = unit(mu), unit(nu), unit(nu, -1)
        up = qmul(qmul(sh(U[nu], e_mu), qc(sh(U[mu], e_nu))), qc(U[nu]))
        dn = qmul(qmul(qc(sh(U[nu], add(e_mu, m_nu))), qc(sh(U[mu], m_nu))), sh(U[nu], m_nu))
        S += up + dn
    return S

_par = sum(np.indices(DIMS)) % 2

def sweep(U, rng, beta=BETA):
    for p in (0, 1):
        mask = _par == p
        for mu in range(4):
            S = staples(U, mu)[mask]
            k = np.linalg.norm(S, axis=1); V = S / k[:, None]
            W = sample_su2_given_w0(rng, kp_w0(rng, beta*k))
            Unew = qmul(W, qc(V))
            Unew /= np.linalg.norm(Unew, axis=1, keepdims=True)
            U[mu][mask] = Unew

def avg_plaq(U):
    tot = 0.0
    for mu in range(4):
        for nu in range(mu+1, 4):
            P = qmul(qmul(U[mu], sh(U[nu], unit(mu))), qmul(qc(sh(U[mu], unit(nu))), qc(U[nu])))
            tot += P[..., 0].mean()
    return tot / 6

def loop2(U, a, b):
    """2x2 loop at every site in the (a,b) plane."""
    ea, eb = unit(a), unit(b); ea2 = add(ea, ea); eb2 = add(eb, eb)
    F = lambda mu, off: sh(U[mu], off)
    path = [F(a, (0,0,0,0)), F(a, ea), F(b, ea2), F(b, add(ea2, eb)),
            qc(F(a, add(ea, eb2))), qc(F(a, eb2)), qc(F(b, eb)), qc(F(b, (0,0,0,0)))]
    W = path[0]
    for q in path[1:]: W = qmul(W, q)
    return W

def marks(U):
    """Return m1 and theta on the root grid (3,3,3,12)."""
    W = loop2(U, 0, 1); B = loop2(U, 0, 2)
    g = 0
    for a in (0, 1):
        for b in (0, 1):
            plaq = qmul(qmul(U[0], sh(U[1], unit(0))), qmul(qc(sh(U[0], unit(1))), qc(U[1])))
            s_off = add(*( [unit(0)]*a + [unit(1)]*b + [(0,0,0,0)] ))
            Pl = sh(plaq, s_off)
            P = np.zeros(DIMS + (4,)); P[..., 0] = 1
            if a: P = qmul(P, U[0])
            if b: P = qmul(P, sh(U[1], unit(0) if a else (0,0,0,0)))
            g = g + qmul(qmul(P, Pl), qc(P))
    g = g / 4
    nb = np.linalg.norm(B[..., 1:], axis=-1)
    B0 = np.zeros_like(B); nz = nb > 1e-14
    B0[nz, 1:] = B[nz, 1:] / nb[nz][:, None]
    m1 = qmul(B0, g)[..., 0]
    theta = np.arccos(np.clip(-W[..., 0], -1, 1))
    return m1[::2, ::2, ::2], theta[::2, ::2, ::2]

def gauge(U, G):
    V = np.empty_like(U)
    for mu in range(4):
        V[mu] = qmul(qmul(G, U[mu]), qc(sh(G, unit(mu))))
    return V
