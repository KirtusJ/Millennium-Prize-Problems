#!/usr/bin/env python3
"""
nys.py -- independent Nystrom computation of the transfer-operator spectrum of SU(2)
Wilson LGT on the 1x1xZ lattice (g2-numchal, task T78).

METHOD (different from the target's Peter-Weyl / Gegenbauer basis):
  state = grid function f(a1, a2, t) with U_i = cos a_i + i sin a_i n_i.sigma, t = n1.n2.
  a-grid: a_k = k pi/(n+1), k=1..n, Haar weights w_k = 2 sin^2 a_k/(n+1) (sum = 1).
  t-grid: Gauss-Legendre n_t nodes; Legendre transform (orthogonal matrix Q).
  Kernel per link, derived by Funk-Hecke (see report): on the partial wave l in t,
     kappa_l(a,a') = exp(beta(cos(a-a') - 1)) * [e^{-z} i_l(z)],  z = beta sin a sin a',
  with e^{-z} i_l(z) = (1/2) int_{-1}^{1} e^{z(c-1)} P_l(c) dc computed by Gauss-Legendre
  QUADRATURE (no Bessel recurrences, no Gegenbauer functions).
  V = beta * 2 s1^2 s2^2 (1-t^2) on the grid (checked against explicit 2x2 matrices, C3).
  Operator S = e^{-V/2} K e^{-V/2} in symmetric (sqrt-weight) form; Lanczos with full
  reorthogonalisation in a center sector. Center element z1: (a1,a2,t) -> (pi-a1, a2, -t).

PREDICATES (fixed before first run):
 controls mode:
  C1  |quad e^{-z}i_0 - closed form| < 1e-13 and same for i_1, z in {0.1,1,10,64,256};
      recurrence |i_{l-1}-i_{l+1}-(2l+1)/z i_l| e^{-z} < 1e-13 for l<=40.   (tolerance: double
      precision with O(100) terms; absolute because values are O(1) or smaller)
  C2  V=0 operator, beta=4: top 4 distinct eigenvalues in ee sector equal products
      lam_{n1} lam_{n2} (n even) where lam_n = (2/pi) int e^{beta(cos a-1)} sin((n+1)a) sin a/(n+1) da
      computed by a separate 4000-point trapezoid; relative tol 1e-9 (grid error of Nystrom
      for smooth periodic integrands is exponentially small; 1e-9 is a safe margin).
  C3  V formula vs explicit matrices at 200 random points (seed 1): |diff| < 1e-12.
  C4  ||S z1 g - z1 S g|| / ||S g|| < 1e-12 for a random g (seed 2), beta=4.
 spec mode (beta, n_a, n_t, n_c): writes eigenvalues of ee sector (top 4) and eo sector (top 2),
  Lanczos residuals; predicate R: residual of each reported Ritz pair < 1e-10 * lam0.
 Comparisons with the target are done in analyse.py, not here.
"""
import sys, json, time
import numpy as np


def leggauss(n):
    return np.polynomial.legendre.leggauss(n)


def legendre_table(x, L):
    """P_0..P_{L-1} at x by three-term recurrence; shape (len(x), L)."""
    P = np.zeros((len(x), L))
    P[:, 0] = 1.0
    if L > 1:
        P[:, 1] = x
    for l in range(1, L - 1):
        P[:, l + 1] = ((2 * l + 1) * x * P[:, l] - l * P[:, l - 1]) / (l + 1)
    return P


def eil_quad(z, L, nc):
    """e^{-z} i_l(z), l=0..L-1, by Gauss-Legendre quadrature of (1/2)int e^{z(c-1)}P_l(c)dc."""
    c, wc = leggauss(nc)
    Pc = legendre_table(c, L) * (0.5 * wc)[:, None]          # (nc, L)
    z = np.asarray(z, dtype=float).ravel()
    out = np.empty((len(z), L))
    ch = 4096
    for s in range(0, len(z), ch):
        E = np.exp(np.outer(z[s:s + ch], c - 1.0))
        out[s:s + ch] = E @ Pc
    return out


class Model:
    def __init__(self, beta, na, nt, nc, V_on=True):
        self.beta, self.na, self.nt = beta, na, nt
        k = np.arange(1, na + 1)
        a = k * np.pi / (na + 1)
        w = 2 * np.sin(a) ** 2 / (na + 1)
        self.a, self.w = a, w
        t, wt = leggauss(nt)
        self.t = t
        P = legendre_table(t, nt)
        self.Q = np.sqrt(wt)[:, None] * P * np.sqrt((2 * np.arange(nt) + 1) / 2.0)[None, :]
        s = np.sin(a)
        Z = beta * np.outer(s, s)
        G = eil_quad(Z, nt, nc).reshape(na, na, nt)             # e^{-z} i_l(z)
        base = np.exp(beta * (np.cos(a[:, None] - a[None, :]) - 1.0)) * np.sqrt(np.outer(w, w))
        self.M = np.ascontiguousarray((base[:, :, None] * G).transpose(2, 0, 1))  # (nt, na, na)
        if V_on:
            V = 2 * beta * (s[:, None, None] ** 2) * (s[None, :, None] ** 2) * (1 - t[None, None, :] ** 2)
        else:
            V = np.zeros((na, na, nt))
        self.eh = np.exp(-V / 2)

    def apply(self, g):
        g = g * self.eh
        h = (g @ self.Q).transpose(2, 0, 1)                    # (nt, na, na)
        h = self.M @ h @ self.M.transpose(0, 2, 1)
        g = h.transpose(1, 2, 0) @ self.Q.T
        return g * self.eh

    @staticmethod
    def z1(g):
        return g[::-1, :, ::-1]

    @staticmethod
    def z2(g):
        return g[:, ::-1, ::-1]

    def proj(self, g, s1, s2):
        g = 0.5 * (g + s1 * self.z1(g))
        return 0.5 * (g + s2 * self.z2(g))


def lanczos(op, v0, k):
    n = v0.size
    V = np.zeros((k + 1, n))
    al, be = np.zeros(k), np.zeros(k)
    V[0] = v0.ravel() / np.linalg.norm(v0)
    for j in range(k):
        w = op(V[j])
        al[j] = V[j] @ w
        w -= V[:j + 1].T @ (V[:j + 1] @ w)
        w -= V[:j + 1].T @ (V[:j + 1] @ w)
        be[j] = np.linalg.norm(w)
        if be[j] < 1e-300:
            k = j + 1
            break
        V[j + 1] = w / be[j]
    T = np.diag(al[:k]) + np.diag(be[:k - 1], 1) + np.diag(be[:k - 1], -1)
    ev, U = np.linalg.eigh(T)
    order = np.argsort(-ev)
    ev, U = ev[order], U[:, order]
    return ev, U, V[:k], be[k - 1]


def sector_spec(m, s1, s2, nev, k, seed):
    rng = np.random.default_rng(seed)
    shp = (m.na, m.na, m.nt)
    op = lambda v: m.proj(m.apply(v.reshape(shp)), s1, s2).ravel()
    v0 = m.proj(rng.standard_normal(shp), s1, s2)
    ev, U, V, _ = lanczos(op, v0, k)
    res = []
    for i in range(nev):
        x = U[:, i] @ V
        x /= np.linalg.norm(x)
        r = op(x) - ev[i] * x
        res.append(float(np.linalg.norm(r)))
    return ev[:nev].tolist(), res


def controls(out):
    ok = True
    rep = {}
    # C1
    zs = np.array([0.1, 1.0, 10.0, 64.0, 256.0])
    q = eil_quad(zs, 42, 600)
    i0 = (1 - np.exp(-2 * zs)) / (2 * zs)
    i1 = (zs * (1 + np.exp(-2 * zs)) / 2 - (1 - np.exp(-2 * zs)) / 2) / zs ** 2
    e0 = float(np.max(np.abs(q[:, 0] - i0))); e1 = float(np.max(np.abs(q[:, 1] - i1)))
    l = np.arange(1, 41)
    rec = q[:, l - 1] - q[:, l + 1] - (2 * l + 1)[None, :] / zs[:, None] * q[:, l]
    er = float(np.max(np.abs(rec)))
    c1 = max(e0, e1, er) < 1e-13
    rep['C1'] = dict(err_i0=e0, err_i1=e1, err_rec=er, met=c1); ok &= c1
    # C2
    beta = 4.0
    m = Model(beta, 48, 16, 200, V_on=False)
    ev, res = sector_spec(m, 1, 1, 6, 60, 3)
    aa = np.linspace(0, np.pi, 4001)
    lam = []
    for n in range(0, 9):
        f = np.exp(beta * (np.cos(aa) - 1)) * np.sin((n + 1) * aa) * np.sin(aa) / (n + 1)
        lam.append((2 / np.pi) * np.trapezoid(f, aa))
    prods = sorted({round(lam[i] * lam[j], 14) for i in range(0, 9, 2) for j in range(0, 9, 2)}, reverse=True)
    distinct = []
    for e in ev:
        if not distinct or abs(e - distinct[-1]) > 1e-9 * ev[0]:
            distinct.append(e)
    rel = [abs(distinct[i] - prods[i]) / prods[0] for i in range(min(4, len(distinct)))]
    c2 = len(rel) == 4 and max(rel) < 1e-9
    rep['C2'] = dict(nystrom=distinct[:4], products=prods[:4], rel=rel, met=bool(c2)); ok &= c2
    # C3
    rng = np.random.default_rng(1)
    sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
    mx = 0.0
    for _ in range(200):
        a1, a2 = rng.uniform(0, np.pi, 2)
        n1 = rng.standard_normal(3); n1 /= np.linalg.norm(n1)
        n2 = rng.standard_normal(3); n2 /= np.linalg.norm(n2)
        U1 = np.cos(a1) * np.eye(2) + 1j * np.sin(a1) * (n1[0] * sx + n1[1] * sy + n1[2] * sz)
        U2 = np.cos(a2) * np.eye(2) + 1j * np.sin(a2) * (n2[0] * sx + n2[1] * sy + n2[2] * sz)
        C = U1 @ U2 @ np.linalg.inv(U1) @ np.linalg.inv(U2)
        tt = n1 @ n2
        mx = max(mx, abs(np.real(np.trace(C)) / 2 - (1 - 2 * np.sin(a1) ** 2 * np.sin(a2) ** 2 * (1 - tt ** 2))))
        # center: -U1 has invariants (pi-a1, -n1)
    c3 = mx < 1e-12
    rep['C3'] = dict(maxdiff=mx, met=c3); ok &= c3
    # C4
    m = Model(4.0, 40, 16, 200)
    g = np.random.default_rng(2).standard_normal((40, 40, 16))
    d = np.linalg.norm(m.apply(m.z1(g)) - m.z1(m.apply(g))) / np.linalg.norm(m.apply(g))
    d2 = np.linalg.norm(m.apply(m.z2(g)) - m.z2(m.apply(g))) / np.linalg.norm(m.apply(g))
    c4 = max(d, d2) < 1e-12
    rep['C4'] = dict(z1=float(d), z2=float(d2), met=c4); ok &= c4
    with open(out, 'x') as f:
        json.dump(rep, f, indent=1, default=lambda o: o.item() if hasattr(o, "item") else o.tolist())
    print(json.dumps(rep, indent=1, default=lambda o: o.item() if hasattr(o, "item") else o.tolist()))
    return 0 if ok else 1


def spec(beta, na, nt, nc, k, out):
    t0 = time.time()
    m = Model(beta, na, nt, nc)
    ee, ree = sector_spec(m, 1, 1, 4, k, 10)
    eo, reo = sector_spec(m, -1, 1, 2, k, 11)
    l0 = ee[0]
    rep = dict(beta=beta, na=na, nt=nt, nc=nc, k=k, ee=ee, ee_res=ree, eo=eo, eo_res=reo,
               m_e=-np.log(ee[1] / l0), m_e2=-np.log(ee[2] / l0), m_e3=-np.log(ee[3] / l0),
               m_eo=-np.log(eo[0] / l0), m_eo_1=-np.log(eo[1] / l0), secs=time.time() - t0)
    rep['R_met'] = bool(max(ree + reo) < 1e-10 * l0)
    with open(out, 'x') as f:
        json.dump(rep, f, indent=1, default=lambda o: o.item() if hasattr(o, "item") else o.tolist())
    print(json.dumps(rep, default=lambda o: o.item() if hasattr(o, "item") else o.tolist()))
    return 0 if rep['R_met'] else 1


def controls_b(out):
    """Amended predicates (after controls2 failures, own expectation/design):
    C1b recurrence error scaled by the amplification (2l+1)/z: |rec| < 1e-14 * (2l+1)/z.
    C2b as C2 but nev=14, Lanczos 120 steps, so 4 distinct values are reached."""
    rep = {}; ok = True
    zs = np.array([0.1, 1.0, 10.0, 64.0, 256.0])
    q = eil_quad(zs, 42, 600)
    l = np.arange(1, 41)
    rec = q[:, l - 1] - q[:, l + 1] - (2 * l + 1)[None, :] / zs[:, None] * q[:, l]
    ratio = float(np.max(np.abs(rec) / (1e-14 * (2 * l + 1)[None, :] / zs[:, None])))
    rep['C1b'] = dict(max_ratio=ratio, met=ratio < 1); ok &= ratio < 1
    beta = 4.0
    m = Model(beta, 48, 16, 200, V_on=False)
    ev, res = sector_spec(m, 1, 1, 14, 120, 3)
    aa = np.linspace(0, np.pi, 4001)
    lam = [(2 / np.pi) * np.trapezoid(np.exp(beta * (np.cos(aa) - 1)) * np.sin((n + 1) * aa) * np.sin(aa) / (n + 1), aa) for n in range(9)]
    prods = sorted({round(lam[i] * lam[j], 14) for i in range(0, 9, 2) for j in range(0, 9, 2)}, reverse=True)
    distinct = []
    for e in ev:
        if not distinct or abs(e - distinct[-1]) > 1e-9 * ev[0]:
            distinct.append(e)
    rel = [abs(distinct[i] - prods[i]) / prods[0] for i in range(min(4, len(distinct)))]
    c2 = len(rel) == 4 and max(rel) < 1e-9
    rep['C2b'] = dict(nystrom=distinct[:5], products=prods[:5], rel=rel, met=bool(c2)); ok &= c2
    with open(out, 'x') as f:
        json.dump(rep, f, indent=1, default=float)
    print(json.dumps(rep, indent=1, default=float))
    return 0 if ok else 1


if __name__ == '__main__':
    if sys.argv[1] == 'controls_b':
        sys.exit(controls_b(sys.argv[2]))
    if sys.argv[1] == 'controls':
        sys.exit(controls(sys.argv[2]))
    else:
        b, na, nt, nc, k = float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
        sys.exit(spec(b, na, nt, nc, k, sys.argv[7]))

