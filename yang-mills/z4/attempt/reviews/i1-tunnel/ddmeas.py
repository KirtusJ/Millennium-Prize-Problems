"""ddmeas.py -- splitting m_eo, m_oo of T = e^{-V/2} K e^{-V/2} (one site, two directions, SU(2)) beyond double precision.

Method (own code): Peter-Weyl basis Phi_{n1 n2 L} = F_{n1 L}(a1) F_{n2 L}(a2) sqrt(2L+1) P_L(t), symmetric form
M = K^{1/2} E K^{1/2}, E_ab = <Phi_a| e^{-V} |Phi_b>, V = 2 beta s1^2 s2^2 (1-t^2), K eigenvalue per link ~ I_{n+1}(beta).
Sector (p1,p2) = parities of (n1,n2); only L even (the ground state of each center sector is L-even; V even in t).
1) double-precision Lanczos (full reorth.) gives Ritz vector v per sector;
2) lambda = v^T M v / v^T v evaluated in double-double (all tables: nodes, weights, basis, Bessel ratios, e^{-V} in dd).
   RQ error <= ||r||^2/gap (r = double residual), i.e. ~1e-30 relative; m = -log(lam_oe/lam_ee) from the dd difference.
Quadrature: Gauss-Chebyshev-U in a (M nodes, M odd, half grid by a->pi-a symmetry), Gauss-Legendre in t (Mt even, t>0 half).

CORRECTED PREDICTION (stated before measurement, see notes.md step2):
  -log m_eo = 4.605413 sqrt(beta) - 8.9888 beta^{1/6} + p log beta + b + o(1)   (p, b not derived)
  m_oo / m_eo -> 2.

PREDICATES (fixed before first run):
 D1 dd self-test: |exp(-a)exp(-b)/exp(-(a+b)) - 1| < 1e-29 for 50 seeded a,b in [0,40]; |sin^2+cos^2-1| < 1e-30 on nodes.
    (tolerance: ~100 dd roundings of 4.9e-32 times squaring amplification 16)
 D2 Bessel ratios: Miller start S and S+60 agree to 1e-29 relative for all n<=N+1 (truncation of recurrence).
 D3 quadrature orthonormality: max |G_ab - delta_ab| < 1e-28 over the radial basis for L=0,2 (exact Gauss rule; dd rounding).
 R  double Lanczos residual ||Mv - lam v|| / lam < 1e-13 per sector (double rounding ~ sqrt(dim)*1e-16).
 E  estimated RQ error res^2/gap < 1e-3 * m (so that m has 3 digits); gap taken as 0.1 (lower bound of m_e for beta<=512).
 (controls C and convergence N/M are evaluated by analyse2.py across runs)
Usage: python3 ddmeas.py BETA N M Mt OUTFILE
"""
import sys, json, time, math
import numpy as np
import dd

np.random.seed(12345)


def nodes_a(M):
    """Chebyshev-U nodes theta_j=j pi/(M+1), j=1..(M+1)/2 (half grid). returns x=cos, s=sin (dd), weight (dd) incl. symmetry factor."""
    assert M % 2 == 1
    h = (M + 1) // 2
    j = np.arange(1, h + 1, dtype=float)
    num = dd.mul_d((dd.PI[0] + 0 * j, dd.PI[1] + 0 * j), 1.0)
    y = dd.div_d(dd.mul_d(num, 1.0), 1.0)
    y = dd.div_d((dd.PI[0] * (2 * j - M - 1), 0 * j), 1.0)  # placeholder overwritten below
    p, e = dd.two_prod(dd.PI[0] + 0 * j, 2 * j - M - 1)
    e = e + dd.PI[1] * (2 * j - M - 1)
    y = dd.div_d(dd.two_sum_fast(p, e), 2.0 * (M + 1))
    x = dd.neg(dd.sin_small(y))
    s = dd.cos_small(y)
    s2 = dd.mul(s, s)
    w = dd.div_d(dd.mul_d(s2, 2.0), float(M + 1))
    fac = np.where(j < h, 2.0, 1.0)
    w = dd.mul_d(w, fac)
    return x, s, w


def legendre_dd(Mt):
    t0, w0 = np.polynomial.legendre.leggauss(Mt)
    t0 = t0[t0 > 0]
    t = (t0, 0 * t0)
    for _ in range(3):
        pm1 = (np.ones_like(t0), 0 * t0); p = t
        for k in range(1, Mt):
            nxt = dd.div_d(dd.sub(dd.mul_d(dd.mul(t, p), 2 * k + 1), dd.mul_d(pm1, k)), k + 1)
            pm1, p = p, nxt
        one = (np.ones_like(t0), 0 * t0)
        dp = dd.div(dd.mul_d(dd.sub(dd.mul(t, p), pm1), Mt), dd.sub(dd.mul(t, t), one))
        t = dd.sub(t, dd.div(p, dp))
    pm1 = (np.ones_like(t0), 0 * t0); p = t
    for k in range(1, Mt):
        nxt = dd.div_d(dd.sub(dd.mul_d(dd.mul(t, p), 2 * k + 1), dd.mul_d(pm1, k)), k + 1)
        pm1, p = p, nxt
    one = (np.ones_like(t0), 0 * t0)
    dp = dd.div(dd.mul_d(dd.sub(dd.mul(t, p), pm1), Mt), dd.sub(dd.mul(t, t), one))
    # standard weight 2/((1-t^2)P'^2); measure (1/2)dt, two halves -> factor 1
    w = dd.div(dd.const(2) if False else (2.0 + 0 * t0, 0 * t0), dd.mul(dd.sub(one, dd.mul(t, t)), dd.mul(dp, dp)))
    return t, w


def legendre_vals(Lmax, t):
    """sqrt(2L+1) P_L(t) for L=0..Lmax, dd, shape (Lmax+1, nt)."""
    P = [(np.ones_like(t[0]), 0 * t[0]), t]
    for k in range(1, Lmax):
        P.append(dd.div_d(dd.sub(dd.mul_d(dd.mul(t, P[k]), 2 * k + 1), dd.mul_d(P[k - 1], k)), k + 1))
    out = []
    for L in range(Lmax + 1):
        out.append(dd.mul(P[L], dd.sqrt((np.float64(2 * L + 1), np.float64(0)))))
    return out


def radial_vals(N, L, x, s):
    """F_{nL}(a) for n=L..N on nodes (dd): sin^L * orthonormal Gegenbauer(lam=L+1)."""
    from fractions import Fraction
    lam = L + 1
    mu = Fraction(1)
    for l in range(1, L + 1):
        mu *= Fraction(2 * l + 1, 2 * l + 2)
    p0 = dd.div((1.0 + 0 * x[0], 0 * x[0]), dd.sqrt(dd.const(mu)))
    sL = (np.ones_like(x[0]), 0 * x[0])
    for _ in range(L):
        sL = dd.mul(sL, s)
    b = [None] + [dd.sqrt(dd.const(Fraction(k * (k + 2 * lam - 1), 4 * (k + lam) * (k + lam - 1)))) for k in range(1, N - L + 2)]
    ps = [p0]
    if N > L:
        ps.append(dd.div(dd.mul(x, p0), (b[1][0] + 0 * x[0], b[1][1] + 0 * x[0])))
    for k in range(1, N - L):
        nxt = dd.sub(dd.mul(x, ps[k]), dd.mul(ps[k - 1], (b[k][0] + 0 * x[0], b[k][1] + 0 * x[0])))
        ps.append(dd.div(nxt, (b[k + 1][0] + 0 * x[0], b[k + 1][1] + 0 * x[0])))
    return [dd.mul(sL, p) for p in ps]  # index n-L


def bessel_ratios(nmax, beta, extra=0):
    """r_n = I_n(beta)/I_1(beta), n=0..nmax, dd scalars via Miller backward recurrence."""
    S = int(nmax + 60 + 2 * beta + 25 * math.sqrt(beta + 1)) + extra
    Ikp1 = (np.float64(0.0), np.float64(0.0)); Ik = (np.float64(1e-300), np.float64(0.0))
    vals = {}
    for k in range(S, 0, -1):
        # I_{k-1} = I_{k+1} + (2k/beta) I_k
        Ikm1 = dd.add(Ikp1, dd.div_d(dd.mul_d(Ik, 2.0 * k), float(beta)))
        Ikp1, Ik = Ik, Ikm1
        if k - 1 <= nmax:
            vals[k - 1] = Ik
        if Ik[0] > 1e250:
            sc = 1e-250
            Ikp1 = (Ikp1[0] * sc, Ikp1[1] * sc); Ik = (Ik[0] * sc, Ik[1] * sc)
            vals = {n: (v[0] * sc, v[1] * sc) for n, v in vals.items()}
    vals[nmax] = vals.get(nmax)
    I1 = vals[1]
    return [dd.div(vals[n], I1) for n in range(nmax + 1)]


class Model:
    def __init__(self, beta, N, M, Mt):
        self.beta, self.N = beta, N
        x, s, wa = nodes_a(M)
        t, wt = legendre_dd(Mt)
        self.x, self.s, self.wa, self.t, self.wt = x, s, wa, t, wt
        self.P = legendre_vals(N, t)
        self.F = {L: radial_vals(N, L, x, s) for L in range(0, N + 1, 2)}
        self.r = bessel_ratios(N + 1, beta)
        # weights W = wa1 wa2 wt e^{-V}, V = 2 beta s1^2 s2^2 (1-t^2)
        s2 = dd.mul(s, s)
        one = (np.ones_like(t[0]), 0 * t[0])
        omt = dd.sub(one, dd.mul(t, t))
        A = dd.mul(s2[0][:, None] + 0 * s2[0][None, :], (0,)) if False else None
        S1 = (s2[0][:, None, None] + 0 * np.zeros((1, len(x[0]), len(t[0]))), s2[1][:, None, None] + 0 * np.zeros((1, len(x[0]), len(t[0]))))
        S2 = (s2[0][None, :, None] + 0 * np.zeros((len(x[0]), 1, len(t[0]))), s2[1][None, :, None] + 0 * np.zeros((len(x[0]), 1, len(t[0]))))
        OT = (omt[0][None, None, :] + 0 * np.zeros((len(x[0]), len(x[0]), 1)), omt[1][None, None, :] + 0 * np.zeros((len(x[0]), len(x[0]), 1)))
        V = dd.mul_d(dd.mul(dd.mul(S1, S2), OT), 2.0 * beta)
        eV = dd.exp(dd.neg(V))
        WA = dd.mul((wa[0][:, None, None] + 0 * V[0], wa[1][:, None, None] + 0 * V[0]), (wa[0][None, :, None] + 0 * V[0], wa[1][None, :, None] + 0 * V[0]))
        WA = dd.mul(WA, (wt[0][None, None, :] + 0 * V[0], wt[1][None, None, :] + 0 * V[0]))
        self.W = dd.mul(WA, eV)
        self.Wd = self.W[0] + self.W[1]

    def sector(self, p1, p2):
        idx = []
        for L in range(0, self.N + 1, 2):
            n1 = [n for n in range(L, self.N + 1) if n % 2 == p1]
            n2 = [n for n in range(L, self.N + 1) if n % 2 == p2]
            if n1 and n2:
                idx.append((L, n1, n2))
        return idx

    def ksqrt(self, idx):
        out = []
        for L, n1, n2 in idx:
            k1 = [self.r[n + 1] for n in n1]; k2 = [self.r[n + 1] for n in n2]
            K1 = (np.array([k[0] for k in k1]), np.array([k[1] for k in k1]))
            K2 = (np.array([k[0] for k in k2]), np.array([k[1] for k in k2]))
            prod = dd.mul((K1[0][:, None] + 0 * K2[0][None, :], K1[1][:, None] + 0 * K2[0][None, :]),
                          (K2[0][None, :] + 0 * K1[0][:, None], K2[1][None, :] + 0 * K1[0][:, None]))
            out.append(dd.sqrt(prod))
        return out

    def dtables(self, idx):
        F1 = [np.array([self.F[L][n - L][0] + self.F[L][n - L][1] for n in n1]) for L, n1, n2 in idx]
        F2 = [np.array([self.F[L][n - L][0] + self.F[L][n - L][1] for n in n2]) for L, n1, n2 in idx]
        P = [self.P[L][0] + self.P[L][1] for L, _, _ in idx]
        return F1, F2, P

    def lanczos(self, idx, maxit=300, tol=1e-14):
        F1, F2, P = self.dtables(idx)
        Ks = [k[0] + k[1] for k in self.ksqrt(idx)]
        shapes = [(len(a), len(b)) for _, a, b in idx]
        sizes = [a * b for a, b in shapes]
        offs = np.cumsum([0] + sizes)
        W = self.Wd

        def mv(v):
            g = 0
            for i in range(len(idx)):
                y = Ks[i] * v[offs[i]:offs[i + 1]].reshape(shapes[i])
                B = F1[i].T @ y @ F2[i]
                g = g + B[:, :, None] * P[i][None, None, :]
            h = W * g
            out = np.empty_like(v)
            for i in range(len(idx)):
                Hl = np.tensordot(h, P[i], axes=([2], [0]))
                out[offs[i]:offs[i + 1]] = (Ks[i] * (F1[i] @ Hl @ F2[i].T)).ravel()
            return out
        n = offs[-1]
        rng = np.random.default_rng(7)
        q = np.abs(rng.standard_normal(n)); q /= np.linalg.norm(q)
        Q = [q]; al = []; be = []
        lam_old = None
        for it in range(min(maxit, n)):
            w = mv(Q[-1])
            a = Q[-1] @ w; al.append(a)
            w = w - a * Q[-1] - (be[-1] * Q[-2] if be else 0)
            Qm = np.array(Q)
            for _ in range(2):
                w -= Qm.T @ (Qm @ w)
            b = np.linalg.norm(w)
            Tm = np.diag(al) + np.diag(be, 1) + np.diag(be, -1)
            th, S = np.linalg.eigh(Tm)
            res = abs(b * S[-1, -1])
            if res < tol * th[-1] or b < 1e-300 or it == n - 1:
                break
            be.append(b); Q.append(w / b)
        v = np.array(Q).T @ S[:, -1]
        v /= np.linalg.norm(v)
        if v.sum() < 0:
            v = -v
        r = mv(v) - th[-1] * v
        return v, th[-1], np.linalg.norm(r) / th[-1], it + 1, (offs, shapes)

    def rq_dd(self, idx, v, offs, shapes):
        Ks = self.ksqrt(idx)
        g = (0.0, 0.0)
        nrm = (np.float64(0), np.float64(0))
        for i, (L, n1, n2) in enumerate(idx):
            vd = v[offs[i]:offs[i + 1]].reshape(shapes[i])
            y = dd.mul(Ks[i], (vd, 0 * vd))
            # T1[a1, n2] = sum_n1 F1[n1](a1) y[n1, n2]
            T1 = None
            for k, n in enumerate(n1):
                f = self.F[L][n - L]
                term = dd.mul((f[0][:, None] + 0 * y[0][k][None, :], f[1][:, None] + 0 * y[0][k][None, :]),
                              (y[0][k][None, :] + 0 * f[0][:, None], y[1][k][None, :] + 0 * f[0][:, None]))
                T1 = term if T1 is None else dd.add(T1, term)
            B = None
            for k, n in enumerate(n2):
                f = self.F[L][n - L]
                term = dd.mul((T1[0][:, k][:, None] + 0 * f[0][None, :], T1[1][:, k][:, None] + 0 * f[0][None, :]),
                              (f[0][None, :] + 0 * T1[0][:, k][:, None], f[1][None, :] + 0 * T1[0][:, k][:, None]))
                B = term if B is None else dd.add(B, term)
            Pl = self.P[L]
            term = dd.mul((B[0][:, :, None] + 0 * Pl[0][None, None, :], B[1][:, :, None] + 0 * Pl[0][None, None, :]),
                          (Pl[0][None, None, :] + 0 * B[0][:, :, None], Pl[1][None, None, :] + 0 * B[0][:, :, None]))
            g = term if i == 0 else dd.add(g, term)
        # norm v.v in dd
        sq = dd.mul((v, 0 * v), (v, 0 * v))
        nrm = self.ddsum(sq)
        num = self.ddsum(dd.mul(self.W, dd.mul(g, g)))
        return num, nrm

    @staticmethod
    def ddsum(x):
        a = (x[0].ravel(), x[1].ravel())
        while len(a[0]) > 1:
            if len(a[0]) % 2:
                a = (np.append(a[0], 0.0), np.append(a[1], 0.0))
            a = dd.add((a[0][0::2], a[1][0::2]), (a[0][1::2], a[1][1::2]))
        return (a[0][0], a[1][0])


def selftest(model, beta, N):
    rng = np.random.default_rng(1)
    a = rng.uniform(0, 40, 50); b = rng.uniform(0, 40, 50)
    ea = dd.exp((-a, 0 * a)); eb = dd.exp((-b, 0 * b))
    ab = dd.two_sum(-a, -b); eab = dd.exp(ab)
    q = dd.sub(dd.div(dd.mul(ea, eb), eab), (np.ones(50), np.zeros(50)))
    d1a = float(np.max(np.abs(q[0] + q[1])))
    one = dd.add(dd.mul(model.x, model.x), dd.mul(model.s, model.s))
    d1b = float(np.max(np.abs(one[0] - 1 + one[1])))
    r1 = bessel_ratios(N + 1, beta); r2 = bessel_ratios(N + 1, beta, extra=60)
    d2 = max(abs(float(dd.div(dd.sub(u, w), w)[0])) for u, w in zip(r1, r2))
    d3 = 0
    for L in (0, 2):
        F = model.F[L]
        for i in range(len(F)):
            for j in range(len(F)):
                if (i + j) % 2:
                    continue
                G = model.ddsum(dd.mul(model.wa, dd.mul(F[i], F[j])))
                d3 = max(d3, abs(G[0] - (i == j) + G[1]))
    return dict(D1_exp=d1a, D1_trig=d1b, D2=d2, D3=d3,
                D1=bool(d1a < 1e-29 and d1b < 1e-30), D2ok=bool(d2 < 1e-29), D3ok=bool(d3 < 1e-28))


def main():
    beta = float(sys.argv[1]); N = int(sys.argv[2]); M = int(sys.argv[3]); Mt = int(sys.argv[4]); out = sys.argv[5]
    fh = open(out, 'x')
    t0 = time.time()
    m = Model(beta, N, M, Mt)
    st = selftest(m, beta, N)
    rec = dict(beta=beta, N=N, M=M, Mt=Mt, selftest=st, sectors={})
    lam = {}
    for name, (p1, p2) in dict(ee=(0, 0), oe=(1, 0), oo=(1, 1)).items():
        idx = m.sector(p1, p2)
        v, th, res, its, (offs, shapes) = m.lanczos(idx)
        num, nrm = m.rq_dd(idx, v, offs, shapes)
        lamdd = dd.div((np.float64(num[0]), np.float64(num[1])), (np.float64(nrm[0]), np.float64(nrm[1])))
        lam[name] = lamdd
        rec['sectors'][name] = dict(lam_double=float(th), lam_dd=[float(lamdd[0]), float(lamdd[1])], res=float(res), iters=its,
                                    dim=int(offs[-1]), R=bool(res < 1e-13))
    for nm in ('oe', 'oo'):
        dlt = dd.div(dd.sub(lam['ee'], lam[nm]), lam['ee'])
        x = float(dlt[0]) + float(dlt[1])
        mval = -math.log1p(-x)
        rec['m_' + ('eo' if nm == 'oe' else 'oo')] = mval
        res2 = max(rec['sectors']['ee']['res'], rec['sectors'][nm]['res']) ** 2 / 0.1
        rec['E_' + nm] = dict(err_est=res2, ok=bool(res2 < 1e-3 * abs(mval)))
    rec['seconds'] = time.time() - t0
    json.dump(rec, fh, indent=1); fh.close()
    print(json.dumps(dict(beta=beta, N=N, M=M, Mt=Mt, m_eo=rec['m_eo'], m_oo=rec['m_oo'], st=st,
                          res={k: v['res'] for k, v in rec['sectors'].items()}, E=[rec['E_oe'], rec['E_oo']], sec=rec['seconds'])))
    ok = st['D1'] and st['D2ok'] and st['D3ok'] and all(v['R'] for v in rec['sectors'].values()) and rec['E_oe']['ok'] and rec['E_oo']['ok']
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
