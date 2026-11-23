"""lat.py -- library (no predicates here; predicates live in the run_*.py docstrings).

SU(N) lattice gauge theory on a d-dim hypercubic box (periodic or open).
Conventions (from PROOF_A_curv.md):
  <X,Y> = -Tr(XY); orthonormal basis e_a (SU(2): i sigma_a/sqrt2; SU(3): i lambda_a/sqrt2).
  V = -(beta/N) sum_p Re Tr Q_p,  Q_p = U1 U2 U3^dag U4^dag  (U1=U_{x,mu},U2=U_{x+mu,nu},U3=U_{x+nu,mu},U4=U_{x,nu}).
  coordinates U_e -> exp(sum_a t_{e,a} e_a) U_e  (normal coordinates of the bi-invariant metric,
  so the coordinate Hessian at t=0 IS the Riemannian Hessian).
  Ric = N/2.  B = Ric*I + Hess V.  Gauge direction at omega: T_e = omega_x - Ad(U_e) omega_y, e=(x->y).
"""
import itertools
import numpy as np

SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


def basis(N):
    if N == 2:
        return np.array([1j * s / np.sqrt(2) for s in SIG])
    if N == 3:
        l = np.zeros((8, 3, 3), complex)
        l[0][0, 1] = l[0][1, 0] = 1
        l[1][0, 1] = -1j; l[1][1, 0] = 1j
        l[2][0, 0] = 1; l[2][1, 1] = -1
        l[3][0, 2] = l[3][2, 0] = 1
        l[4][0, 2] = -1j; l[4][2, 0] = 1j
        l[5][1, 2] = l[5][2, 1] = 1
        l[6][1, 2] = -1j; l[6][2, 1] = 1j
        l[7] = np.diag([1, 1, -2]) / np.sqrt(3)
        return 1j * l / np.sqrt(2)
    raise ValueError


def expm_su(A):
    """exp of anti-hermitian matrices (batch) via eigen-decomposition of the hermitian -iA."""
    H = -1j * A
    w, v = np.linalg.eigh(H)
    return np.einsum('...ij,...j,...kj->...ik', v, np.exp(1j * w), v.conj())


class Lattice:
    def __init__(self, L, d=4, periodic=True):
        self.L, self.d, self.periodic = L, d, periodic
        sites = list(itertools.product(range(L), repeat=d))
        self.sites = sites
        self.sidx = {s: i for i, s in enumerate(sites)}
        links, lidx = [], {}
        for s in sites:
            for mu in range(d):
                t = list(s); t[mu] += 1
                if t[mu] == L:
                    if not periodic:
                        continue
                    t[mu] = 0
                lidx[(s, mu)] = len(links)
                links.append((self.sidx[s], self.sidx[tuple(t)], mu))
        self.links = np.array(links)
        self.lidx = lidx
        plaq = []
        for s in sites:
            for mu in range(d):
                for nu in range(mu + 1, d):
                    def sh(x, m):
                        y = list(x); y[m] = (y[m] + 1) % L; return tuple(y)
                    k1 = (s, mu); k2 = (sh(s, mu), nu); k3 = (sh(s, nu), mu); k4 = (s, nu)
                    if all(k in lidx for k in (k1, k2, k3, k4)):
                        # open bc: also need that the shifts did not wrap
                        if not periodic and (s[mu] + 1 >= L or s[nu] + 1 >= L):
                            continue
                        plaq.append([lidx[k1], lidx[k2], lidx[k3], lidx[k4]])
        self.plaq = np.array(plaq)
        self.nE = len(links); self.nS = len(sites); self.nP = len(plaq)
        # link coloring so that links in one batch share no plaquette (greedy)
        inc = [[] for _ in range(self.nE)]
        for p, pl in enumerate(self.plaq):
            for k, e in enumerate(pl):
                inc[e].append((p, k))
        self.inc = inc
        color = -np.ones(self.nE, int)
        for e in range(self.nE):
            used = set()
            for p, _ in inc[e]:
                for f in self.plaq[p]:
                    if color[f] >= 0:
                        used.add(color[f])
            c = 0
            while c in used:
                c += 1
            color[e] = c
        self.batches = [np.where(color == c)[0] for c in range(color.max() + 1)]
        maxinc = max(len(i) for i in inc)
        self.incP = -np.ones((self.nE, maxinc), int); self.incK = np.zeros((self.nE, maxinc), int)
        for e in range(self.nE):
            for j, (p, k) in enumerate(inc[e]):
                self.incP[e, j] = p; self.incK[e, j] = k


def dag(A):
    return np.conj(np.swapaxes(A, -1, -2))


def plaquettes(lat, U):
    U1, U2, U3, U4 = (U[lat.plaq[:, k]] for k in range(4))
    return U1 @ U2 @ dag(U3) @ dag(U4)


def action(lat, U, beta, N):
    return -(beta / N) * np.trace(plaquettes(lat, U), axis1=1, axis2=2).real.sum()


def Ad(W, E):
    """Ad matrix in basis E: Ad_{ab} = -Tr(e_a W e_b W^dag) ; W batch (n,N,N) -> (n,D,D)."""
    M = np.einsum('nij,bjk,nlk->nbil', W, E, W.conj())  # W e_b W^dag
    return -np.einsum('aij,nbji->nab', E, M).real


def hessV(lat, U, beta, N):
    E = basis(N); D = len(E)
    U1, U2, U3, U4 = (U[lat.plaq[:, k]] for k in range(4))
    I = np.broadcast_to(np.eye(N, dtype=complex), U1.shape)
    W = [I, U1, U1 @ U2 @ dag(U3), U1 @ U2 @ dag(U3) @ dag(U4)]
    Q0 = W[3]
    s = [1, 1, -1, -1]
    # X[k] : (nP, D, N, N)
    X = [s[k] * np.einsum('nij,ajk,nlk->nail', W[k], E, W[k].conj()) for k in range(4)]
    h = np.zeros((lat.nP, 4 * D, 4 * D))
    for k in range(4):
        for l in range(k, 4):
            m = np.einsum('naij,nbjk,nki->nab', X[k], X[l], Q0).real
            if k == l:
                m = 0.5 * (m + np.swapaxes(m, 1, 2))
                h[:, k * D:(k + 1) * D, k * D:(k + 1) * D] += m
            else:
                h[:, k * D:(k + 1) * D, l * D:(l + 1) * D] += m
                h[:, l * D:(l + 1) * D, k * D:(k + 1) * D] += np.swapaxes(m, 1, 2)
    h *= -(beta / N)
    n = lat.nE * D
    H = np.zeros((n, n))
    idx = (lat.plaq[:, :, None] * D + np.arange(D)[None, None, :]).reshape(lat.nP, 4 * D)
    for p in range(lat.nP):
        ii = idx[p]
        H[np.ix_(ii, ii)] += h[p]
    return H


def gauge_matrix(lat, U, N):
    """G: (nE*D, nS*D); column block x = tangent of infinitesimal gauge transformation at site x."""
    E = basis(N); D = len(E)
    G = np.zeros((lat.nE * D, lat.nS * D))
    A = Ad(U, E)
    for e, (x, y, mu) in enumerate(lat.links):
        G[e * D:(e + 1) * D, x * D:(x + 1) * D] += np.eye(D)
        G[e * D:(e + 1) * D, y * D:(y + 1) * D] -= A[e]
    return G


def horizontal_basis(G, rtol=1e-9):
    Uu, s, Vt = np.linalg.svd(G, full_matrices=True)
    r = int((s > rtol * s[0]).sum())
    return Uu[:, r:], r, s


def kappa_H(lat, U, beta, N, want_vec=False):
    H = hessV(lat, U, beta, N)
    G = gauge_matrix(lat, U, N)
    Nh, r, s = horizontal_basis(G)
    B = N / 2 * np.eye(H.shape[0]) + H
    Bh = Nh.T @ B @ Nh
    w, v = np.linalg.eigh(Bh)
    out = dict(kH=w[0], kfull=np.linalg.eigvalsh(B)[0], rankG=r, dimH=Nh.shape[1], wH=w)
    if want_vec:
        out['vec'] = Nh @ v[:, 0]
    return out


# ---------------- SU(2) heat bath (Kennedy-Pendleton), vectorized over a batch of links ---------
def staple_sum(lat, U, links):
    """S_e such that sum over plaquettes containing e of Re Tr Q_p = Re Tr(U_e S_e)."""
    S = np.zeros((len(links), 2, 2), complex)
    for j in range(lat.incP.shape[1]):
        P = lat.incP[links, j]; K = lat.incK[links, j]
        ok = P >= 0
        for k in range(4):
            sel = ok & (K == k)
            if not sel.any():
                continue
            pl = lat.plaq[P[sel]]
            U1, U2, U3, U4 = (U[pl[:, i]] for i in range(4))
            if k == 0:
                M = U2 @ dag(U3) @ dag(U4)
            elif k == 1:
                M = dag(U3) @ dag(U4) @ U1
            elif k == 2:
                M = dag(dag(U4) @ U1 @ U2)
            else:
                M = dag(U1 @ U2 @ dag(U3))
            S[sel] += M
    return S


def su2_proj(M):
    """project 2x2 matrices onto the real-quaternion form [[a,b],[-b*,a*]] and normalise (returns M_q/|M_q|, |M_q|)."""
    a = (M[:, 0, 0] + np.conj(M[:, 1, 1])) / 2; b = (M[:, 0, 1] - np.conj(M[:, 1, 0])) / 2
    k = np.sqrt(np.abs(a) ** 2 + np.abs(b) ** 2)
    a, b = a / k, b / k
    R = np.empty_like(M); R[:, 0, 0] = a; R[:, 0, 1] = b; R[:, 1, 0] = -np.conj(b); R[:, 1, 1] = np.conj(a)
    return R, k


def heatbath_sweep(lat, U, beta, rng):
    for b in lat.batches:
        S = staple_sum(lat, U, b)
        Vm, k = su2_proj(S)
        a = beta * k  # weight exp((beta/2) ReTr(U S)) = exp(beta k x0) for X = U Vm
        n = len(b)
        x0 = np.empty(n); todo = np.arange(n)
        while len(todo):
            r1, r2, r3, r4 = (1 - rng.random(len(todo)) for _ in range(4))
            lam2 = -(np.log(r1) + np.cos(2 * np.pi * r2) ** 2 * np.log(r3)) / (2 * a[todo])
            acc = r4 ** 2 <= 1 - lam2
            x0[todo[acc]] = 1 - 2 * lam2[acc]
            todo = todo[~acc]
        r = np.sqrt(np.maximum(1 - x0 ** 2, 0))
        v = rng.normal(size=(n, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
        X = x0[:, None, None] * np.eye(2) + 1j * r[:, None, None] * np.einsum('na,aij->nij', v, np.array(SIG))
        U[b] = su2_proj(X @ dag(Vm))[0]
    return U


def avg_plaq(lat, U, N):
    return np.trace(plaquettes(lat, U), axis1=1, axis2=2).real.mean() / N


def landau_gauge(lat, U, sweeps=200):
    """Relaxation toward max sum_e Re Tr U_e (SU(2)); returns gauge-transformed copy."""
    U = U.copy()
    xs = lat.links[:, 0]; ys = lat.links[:, 1]
    OUT = [np.where(xs == x)[0] for x in range(lat.nS)]; INN = [np.where(ys == x)[0] for x in range(lat.nS)]
    for _ in range(sweeps):
        for x in range(lat.nS):
            out = OUT[x]; inn = INN[x]
            K = U[out].sum(0) + dag(U[inn]).sum(0)
            R, k = su2_proj(K[None])
            if k[0] < 1e-14:
                continue
            g = dag(R[0])
            U[out] = su2_proj(g @ U[out])[0]
            U[inn] = su2_proj(U[inn] @ dag(g))[0]
    return U
