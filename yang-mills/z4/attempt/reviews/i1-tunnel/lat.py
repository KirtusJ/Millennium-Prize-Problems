"""lat.py -- exact-numerics spectrum of the SU(2) transfer matrix on the 1x1xZ lattice (2 spatial directions).

Model: T = e^{-V/2} K e^{-V/2} on L^2(SU(2)^2)^{conj}, V = beta(1 - 1/2 Tr(U1U2U1^-1U2^-1)),
K = product over the 2 links of convolution with e^{-beta(1-1/2 Tr U)} followed by the gauge projection.
We diagonalize M = K^{1/2} E K^{1/2} (same nonzero spectrum as T), E_ab = <Phi_a| e^{-V} |Phi_b>,
basis Phi_{n1 n2 L} = F_{n1 L}(a1) F_{n2 L}(a2) sqrt(2L+1) P_L(cos gamma), n_i <= N, L <= min(n1,n2).
K eigenvalue per link: kn(n) = e^{-beta} (2/beta) I_{n+1}(beta).
Quadrature: a_k = k pi/(Nx+1), k=1..Nx (Gauss-Chebyshev-U, exact for polynomials in cos a of degree <= 2Nx+1
against sin^2 a da); Gauss-Legendre with Nt nodes in t = cos gamma.
V is computed on the grid from explicit 2x2 matrices (not from the closed formula).

Modes
  controls OUTFILE                      -- controls C1..C6 below
  spec BETA N NX NT OUTFILE             -- lowest eigenvalues in every symmetry subsector
  dense BETA N NX NT OUTFILE            -- full spectrum by dense diag of the matrix built from the same matvec (small N)

PREDICATES (fixed before the first run)
 C1 Bessel: e^{-b}I_n(b) by trapezoid (M points) agrees with Miller backward recurrence normalised by
    e^b = I_0 + 2 sum I_n, relative difference < 1e-12 for n <= 40, b in {0.1,2,16,64,128}.
    (tolerance: both are double-precision methods with error ~1e-15; 1e-12 leaves 1000x room)
 C2 Basis orthonormality under the quadrature: max |G - 1| < 1e-12 for N=40, Nx=60 (exact Gauss rule; rounding only).
 C3 Commutator: 1/2 Tr comm from matrices equals 1 - 2 s1^2 s2^2 (1-t^2) to 1e-13 on the whole grid (rounding).
 C4 U(1)^2 through the same matvec + Lanczos/dense: eigenvalue ratios lambda/lambda0 equal
    I_{n1}(b) I_{n2}(b)/I_0(b)^2 to 10 digits (relative error < 1e-10) for the 10 largest, b=4 and b=16.
 C5 SU(2) with V forced to 0: ratios equal I_{n1+1}I_{n2+1}/I_1^2 to rel. 1e-10 (same code path, checks transforms).
 C6 Strong coupling beta=0.01, 0.001: center-even gap m_e satisfies |m_e + ln(I_3/I_1)| < 10*beta and the
    (odd,even) gap |m_o + ln(I_2/I_1)| < 10*beta (first-order perturbation in V = O(beta); constant 10 is generous:
    V <= 2 beta, so the shift of log-eigenvalues is bounded by ~2 beta... we allow 10 beta).
 Lanczos convergence: residual < 1e-11 * lambda0 for every reported eigenvalue (else flagged).
 Convergence in N, Nx, Nt is judged in analyse.py (predicate there: 4 digits).
"""
import sys, json, time, math
import numpy as np

np.random.seed(12345)


# ---------------- Bessel functions ----------------
def besselI_scaled_trap(nmax, b, M=None):
    """e^{-b} I_n(b), n=0..nmax via (1/pi) int_0^pi e^{b(cos t -1)} cos(n t) dt, trapezoid."""
    if M is None:
        M = int(max(4000, 8 * nmax + 8 * b))
    t = np.linspace(0, np.pi, M + 1)
    w = np.full(M + 1, 1.0 / M); w[0] = w[-1] = 0.5 / M
    f = np.exp(b * (np.cos(t) - 1.0)) * w
    n = np.arange(nmax + 1)
    return np.cos(np.outer(n, t)) @ f


def besselI_scaled_miller(nmax, b):
    start = int(nmax + 40 + 2 * b + 20 * math.sqrt(b + 1))
    I = np.zeros(start + 2)
    I[start + 1] = 0.0; I[start] = 1e-300
    for n in range(start, 0, -1):
        I[n - 1] = (2 * n / b) * I[n] + I[n + 1]
        if I[n - 1] > 1e250:
            I[n - 1:] *= 1e-250
    s = I[0] + 2 * I[1:].sum()  # = e^b * scale
    return I[:nmax + 1] / s


# ---------------- bases ----------------
def radial_basis(N, a):
    """F[L, n, k] = F_{nL}(a_k), orthonormal w.r.t. (2/pi) sin^2 a da. zero for n<L."""
    x = np.cos(a); s = np.sin(a)
    F = np.zeros((N + 1, N + 1, len(a)))
    for L in range(N + 1):
        lam = L + 1.0
        h0 = math.sqrt(math.pi) * math.exp(math.lgamma(lam + 0.5) - math.lgamma(lam + 1.0))
        pref = math.sqrt(math.pi / 2.0) / math.sqrt(h0)
        # start: sqrt(pi/2) (1-x^2)^{L/2} p0  computed in logs to avoid underflow issues
        with np.errstate(divide='ignore'):
            prev = pref * np.exp(L * np.log(s))
        F[L, L] = prev
        pm1 = np.zeros_like(x); bk = 0.0
        cur = prev
        for k in range(0, N - L):
            kk = k + 1
            bk1 = math.sqrt(kk * (kk + 2 * lam - 1) / (4.0 * (kk + lam) * (kk + lam - 1)))
            nxt = (x * cur - bk * pm1) / bk1
            pm1, cur, bk = cur, nxt, bk1
            F[L, L + kk] = cur
    return F


def legendre_basis(Lmax, t):
    P = np.zeros((Lmax + 1, len(t)))
    P[0] = 1.0
    if Lmax >= 1:
        P[1] = t
    for L in range(1, Lmax):
        P[L + 1] = ((2 * L + 1) * t * P[L] - L * P[L - 1]) / (L + 1)
    return P * np.sqrt(2 * np.arange(Lmax + 1) + 1)[:, None]


def su2(a, nvec):
    """U = cos a + i sin a n.sigma ; arrays broadcast, returns (...,2,2)."""
    c = np.cos(a); s = np.sin(a)
    nx, ny, nz = nvec
    U = np.empty(np.broadcast(c, nx).shape + (2, 2), complex)
    U[..., 0, 0] = c + 1j * s * nz
    U[..., 1, 1] = c - 1j * s * nz
    U[..., 0, 1] = 1j * s * (nx - 1j * ny)
    U[..., 1, 0] = 1j * s * (nx + 1j * ny)
    return U


def half_tr_comm(U1, U2):
    inv = lambda U: np.conj(np.swapaxes(U, -1, -2))
    C = U1 @ U2 @ inv(U1) @ inv(U2)
    return 0.5 * np.real(C[..., 0, 0] + C[..., 1, 1])


class Model:
    """generic separable model: basis index (L, n1, n2); grid (x1, x2, t)."""

    def __init__(self, F, P, w, wt, kn, Vgrid, mask):
        self.F = F            # (NL, Nn, Nx)
        self.P = P            # (NL, Nt)
        self.w = w; self.wt = wt
        self.kn = kn          # (Nn,) per-link K eigenvalue
        self.sq = np.sqrt(np.outer(kn, kn))[None, :, :] * mask
        self.mask = mask      # (NL, Nn, Nn)
        self.W = (w[:, None, None] * w[None, :, None] * wt[None, None, :]) * np.exp(-Vgrid)
        self.FT = np.ascontiguousarray(np.swapaxes(F, 1, 2))
        self.NL = F.shape[0]

    def fwd(self, c):
        G = self.FT @ c @ self.F                      # (NL, Nx, Nx)
        NL, Nx, _ = G.shape
        return (G.reshape(NL, Nx * Nx).T @ self.P).reshape(Nx, Nx, -1)

    def adj(self, f):
        Nx = f.shape[0]
        H = (f.reshape(Nx * Nx, -1) @ self.P.T).T.reshape(self.NL, Nx, Nx)
        return self.F @ H @ self.FT

    def matvec(self, c):
        return self.sq * self.adj(self.W * self.fwd(self.sq * c))


def lanczos_top(mv, proj, shape, k=6, maxit=400, tol=1e-11, seed=1):
    rng = np.random.default_rng(seed)
    v = proj(rng.standard_normal(shape)); v /= np.linalg.norm(v)
    Q = [v.ravel()]; alpha = []; beta = []
    res = None
    for it in range(maxit):
        w = proj(mv(Q[-1].reshape(shape))).ravel()
        a = Q[-1] @ w; alpha.append(a)
        w = w - a * Q[-1] - (beta[-1] * Q[-2] if beta else 0)
        Qm = np.array(Q)
        for _ in range(2):
            w = w - Qm.T @ (Qm @ w)
        b = np.linalg.norm(w)
        m = len(alpha)
        if (m >= k + 2 and m % 10 == 0) or b < 1e-14 or it == maxit - 1:
            Tm = np.diag(alpha) + np.diag(beta, 1) + np.diag(beta, -1)
            th, S = np.linalg.eigh(Tm)
            idx = np.argsort(th)[::-1][:min(k, m)]
            res = b * np.abs(S[-1, idx])
            if b < 1e-14 or np.all(res < tol * th[idx[0]]) or it == maxit - 1:
                vecs = (np.array(Q).T @ S[:, idx]).T
                return th[idx], res, vecs, m
        beta.append(b); Q.append(w / b)
    raise RuntimeError


def build_su2(beta, N, Nx, Nt, zeroV=False):
    a = np.arange(1, Nx + 1) * np.pi / (Nx + 1)
    w = (2 / np.pi) * (np.pi / (Nx + 1)) * np.sin(a) ** 2
    t, wt = np.polynomial.legendre.leggauss(Nt); wt = wt / 2
    F = radial_basis(N, a)
    P = legendre_basis(N, t)
    # V from explicit matrices: U1 = exp(i a1 sigma3), U2 = cos a2 + i sin a2 (sin g sigma1 + cos g sigma3)
    sg = np.sqrt(1 - t ** 2)
    U1 = su2(a[:, None, None], (0 * a[:, None, None], 0, 1.0 + 0 * a[:, None, None]))
    U2 = su2(a[None, :, None], (sg[None, None, :], 0 * sg[None, None, :], t[None, None, :]))
    hc = np.empty((Nx, Nx, Nt))
    for i in range(Nx):
        hc[i] = half_tr_comm(U1[i:i + 1], U2[0])[0]
    V = np.zeros_like(hc) if zeroV else beta * (1 - hc)
    nn = np.arange(N + 1)
    Ls = np.arange(N + 1)
    mask = ((nn[None, :, None] >= Ls[:, None, None]) & (nn[None, None, :] >= Ls[:, None, None])).astype(float)
    ks = besselI_scaled_miller(N + 1, beta)
    kn = (2 / beta) * ks[1:N + 2]
    return Model(F, P, w, wt, kn, V, mask), hc, (a, t)


def sector_proj(N, p1, p2, pL, ex):
    nn = np.arange(N + 1); Ls = np.arange(N + 1)
    m = ((nn % 2 == p1)[None, :, None] & (nn % 2 == p2)[None, None, :] & (Ls % 2 == pL)[:, None, None]
         & (nn[None, :, None] >= Ls[:, None, None]) & (nn[None, None, :] >= Ls[:, None, None])).astype(float)

    def proj(c):
        c = c * m
        if ex != 0:
            c = 0.5 * (c + ex * np.swapaxes(c, 1, 2))
        return c
    return proj


SECTORS = [(0, 0, 0, +1), (0, 0, 0, -1), (0, 0, 1, +1), (0, 0, 1, -1),
           (1, 0, 0, 0), (1, 0, 1, 0),
           (1, 1, 0, +1), (1, 1, 0, -1), (1, 1, 1, +1), (1, 1, 1, -1)]


def spectrum(beta, N, Nx, Nt, k=4, model=None):
    if model is None:
        model, _, _ = build_su2(beta, N, Nx, Nt)
    shape = (N + 1, N + 1, N + 1)
    out = []
    for (p1, p2, pL, ex) in SECTORS:
        proj = sector_proj(N, p1, p2, pL, ex)
        th, res, _, m = lanczos_top(model.matvec, proj, shape, k=k)
        out.append(dict(center=[p1, p2], Lpar=pL, exch=ex, lam=th.tolist(), res=res.tolist(), iters=m))
    return out


def dense_from_matvec(model, proj, shape):
    idx = np.flatnonzero(proj(np.ones(shape)).ravel() != 0)
    # basis vectors of the subspace: use projected unit vectors; orthonormalise via QR on the columns
    cols = []
    for i in idx:
        e = np.zeros(int(np.prod(shape))); e[i] = 1
        cols.append(proj(e.reshape(shape)).ravel())
    B = np.array(cols).T
    Qb, R = np.linalg.qr(B)
    keep = np.abs(np.diag(R)) > 1e-10
    Qb = Qb[:, keep]
    MQ = np.array([model.matvec(Qb[:, j].reshape(shape)).ravel() for j in range(Qb.shape[1])]).T
    A = Qb.T @ MQ
    return np.linalg.eigvalsh(0.5 * (A + A.T))[::-1], np.abs(A - A.T).max()


def controls(outfile):
    rep = {}; fails = []
    # C1
    worst = 0
    for b in (0.1, 2.0, 16.0, 64.0, 128.0):
        t1 = besselI_scaled_trap(40, b); t2 = besselI_scaled_miller(40, b)
        rel = np.abs(t1 / t2 - 1); rel = rel[t2 > 1e-280]
        worst = max(worst, rel.max())
    rep['C1_bessel_maxrel'] = worst
    if not worst < 1e-12: fails.append('C1')
    # C2
    N, Nx = 40, 60
    a = np.arange(1, Nx + 1) * np.pi / (Nx + 1)
    w = (2 / np.pi) * (np.pi / (Nx + 1)) * np.sin(a) ** 2
    F = radial_basis(N, a)
    worstG = 0
    for L in range(N + 1):
        G = (F[L] * w) @ F[L].T
        G = G[L:, L:]
        worstG = max(worstG, np.abs(G - np.eye(len(G))).max())
    t, wt = np.polynomial.legendre.leggauss(50)
    P = legendre_basis(40, t)
    GP = (P * wt / 2) @ P.T
    worstG = max(worstG, np.abs(GP - np.eye(41)).max())
    rep['C2_orth_maxdev'] = worstG
    if not worstG < 1e-12: fails.append('C2')
    # C3
    model, hc, (a, t) = build_su2(4.0, 10, 30, 20)
    s2 = np.sin(a) ** 2
    formula = 1 - 2 * s2[:, None, None] * s2[None, :, None] * (1 - t ** 2)[None, None, :]
    rep['C3_comm_maxdev'] = np.abs(hc - formula).max()
    if not rep['C3_comm_maxdev'] < 1e-13: fails.append('C3')
    # C4: U(1)^2 in the same Model/matvec/Lanczos path. "L" index trivial, n index = real Fourier mode.
    rep['C4'] = {}
    for b in (4.0, 16.0):
        nmax = 12; Nth = 64
        th = 2 * np.pi * np.arange(Nth) / Nth
        wth = np.full(Nth, 1.0 / Nth)
        freqs = [0] + [f for f in range(1, nmax + 1) for _ in (0, 1)]
        Fu = np.zeros((1, len(freqs), Nth))
        Fu[0, 0] = 1
        j = 1
        for f in range(1, nmax + 1):
            Fu[0, j] = np.sqrt(2) * np.cos(f * th); Fu[0, j + 1] = np.sqrt(2) * np.sin(f * th); j += 2
        Pu = np.ones((1, 1)); wtu = np.ones(1)
        z = np.zeros(Nth)
        U = su2(th, (z, z, z + 1))
        hcu = half_tr_comm(U[:, None], U[None, :])
        Vu = (b * (1 - hcu))[:, :, None]
        ks = besselI_scaled_miller(nmax, b)
        kn = ks[np.array(freqs)]
        mask = np.ones((1, len(freqs), len(freqs)))
        mu = Model(Fu, Pu, wth, wtu, kn, Vu, mask)
        shape = (1, len(freqs), len(freqs))
        ev, asym = dense_from_matvec(mu, lambda c: c, shape)
        exact = np.sort(np.outer(kn, kn).ravel())[::-1]
        r_num = ev[:10] / ev[0]; r_ex = exact[:10] / exact[0]
        rel = np.abs(r_num / r_ex - 1).max()
        # also Lanczos (distinct values only)
        thl, res, _, _ = lanczos_top(mu.matvec, lambda c: c, shape, k=4)
        distinct = np.unique(np.round(exact / exact[0], 13))[::-1][:4]
        rel_l = np.abs(thl / thl[0] - distinct).max()
        rep['C4'][str(b)] = dict(maxV=float(np.abs(Vu).max()), dense_rel=rel, lanczos_distinct_absdev=rel_l,
                                 gaps=(-np.log(r_num[:6])).tolist(), exact_gaps=(-np.log(r_ex[:6])).tolist())
        if not (rel < 1e-10 and rel_l < 1e-10): fails.append('C4@%g' % b)
    # C5
    rep['C5'] = {}
    for b in (4.0, 16.0):
        N = 8
        m0, _, _ = build_su2(b, N, 20, 16, zeroV=True)
        shape = (N + 1,) * 3
        ev, asym = dense_from_matvec(m0, sector_proj(N, 0, 0, 0, 0) if False else (lambda c: c * m0.mask), shape)
        kn = m0.kn
        nn = np.arange(N + 1)
        ex = []
        for L in range(N + 1):
            for n1 in range(L, N + 1):
                for n2 in range(L, N + 1):
                    ex.append(kn[n1] * kn[n2])
        ex = np.sort(ex)[::-1]
        rel = np.abs(ev[:10] / ex[:10] - 1).max()
        rep['C5'][str(b)] = dict(rel=rel, dim=len(ev), exp_dim=len(ex))
        if not (rel < 1e-10 and len(ev) == len(ex)): fails.append('C5@%g' % b)
    # C6
    rep['C6'] = {}
    for b in (0.01, 0.001):
        N = 8
        mm, _, _ = build_su2(b, N, 24, 20)
        shape = (N + 1,) * 3
        sp = {}
        for (p1, p2, pL, ex) in [(0, 0, 0, 0), (1, 0, 0, 0), (0, 0, 1, 0)]:
            thv, res, _, _ = lanczos_top(mm.matvec, sector_proj(N, p1, p2, pL, ex), shape, k=3)
            sp[(p1, p2, pL)] = thv
        lam0 = sp[(0, 0, 0)][0]
        me = -np.log(max(sp[(0, 0, 0)][1], sp[(0, 0, 1)][0]) / lam0)
        mo = -np.log(sp[(1, 0, 0)][0] / lam0)
        ks = besselI_scaled_miller(4, b)
        pe = -np.log(ks[3] / ks[1]); po = -np.log(ks[2] / ks[1])
        rep['C6'][str(b)] = dict(me=me, pred_e=pe, de=me - pe, mo=mo, pred_o=po, do=mo - po)
        if not (abs(me - pe) < 10 * b and abs(mo - po) < 10 * b): fails.append('C6@%g' % b)
    rep['FAILED'] = fails
    with open(outfile, 'x') as fh:
        json.dump(rep, fh, indent=1, default=float)
    print(json.dumps(rep, indent=1, default=float))
    return 0 if not fails else 1


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'controls':
        sys.exit(controls(sys.argv[2]))
    elif mode in ('spec', 'dense'):
        beta = float(sys.argv[2]); N = int(sys.argv[3]); Nx = int(sys.argv[4]); Nt = int(sys.argv[5]); out = sys.argv[6]
        t0 = time.time()
        model, _, _ = build_su2(beta, N, Nx, Nt)
        if mode == 'spec':
            sp = spectrum(beta, N, Nx, Nt, model=model)
            rec = dict(beta=beta, N=N, Nx=Nx, Nt=Nt, log_kn0=float(2 * np.log(model.kn[0])), sectors=sp,
                       seconds=time.time() - t0)
        else:
            res = {}
            shape = (N + 1,) * 3
            ev, asym = dense_from_matvec(model, lambda c: c * model.mask, shape)
            rec = dict(beta=beta, N=N, Nx=Nx, Nt=Nt, eig=ev.tolist(), asym=asym, trace=float(ev.sum()),
                       trace2=float((ev ** 2).sum()), seconds=time.time() - t0)
        with open(out, 'x') as fh:
            json.dump(rec, fh, indent=1)
        lam0 = max(max(s['lam']) for s in rec['sectors']) if mode == 'spec' else rec['eig'][0]
        print('beta', beta, 'N', N, 'lam0', lam0, 'sec', time.time() - t0)
        if mode == 'spec':
            for s in rec['sectors']:
                print(s['center'], s['Lpar'], s['exch'], ['%.10f' % (-np.log(l / lam0)) for l in s['lam']],
                      'maxres/lam0 %.1e' % (max(s['res']) / lam0), 'it', s['iters'])
