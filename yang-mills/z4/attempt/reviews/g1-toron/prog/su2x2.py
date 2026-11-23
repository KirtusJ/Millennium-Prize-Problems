"""su2x2.py -- g1-toron (T71). Two-direction model: lattice 1x1xZ, SU(2), configuration (U1,U2) in SU(2)^2.
T = e^{-V/2} K e^{-V/2},  V(U) = beta*(1 - (1/2) Re Tr(U1 U2 U1^-1 U2^-1)),
K = convolution with prod_i k(U_i W_i^-1), k(g) = e^{(beta/2) Tr g}/Z  (eigenvalue kappa_j = I_{2j+1}(beta)/I_1(beta) on spin j).
Center-even gauge-invariant sector = span of Psi_{j1 j2 J}(U) = Tr[(D^{j1}(U1) (x) D^{j2}(U2)) P_J], j1,j2 INTEGER <= jmax.
Spectrum computed for the compression of K^{1/2} e^{-V} K^{1/2} (same nonzero spectrum as T) to j<=jmax.
Reduced quadrature: U1 = exp(i th1 s3), U2 = exp(i th2 n.s), n=(sin ph,0,cos ph);
measure (2/pi)sin^2 th1 dth1 (2/pi) sin^2 th2 dth2 (1/2) sin ph dph. Trapezoid in th1, th2 (period pi), Gauss-Legendre in ph.

PREDICATES (fixed before the first run):
 P1  closed form V = 2 beta sin^2 th1 sin^2 th2 sin^2 ph agrees with the matrix computation on 2000 random pairs
     (seed 1, axes random) to 1e-10*beta  [tolerance: double rounding of 2x2 products, ~1e-15 relative, with margin].
 P2  quadrature/normalisation control: with V = 0 the Gram matrix is the identity, max|M - 1| < 1e-10
     [the V=0 integrand is a trig polynomial of degree <= 4*jmax+2 in th1,th2 and a polynomial-in-trig in ph;
      trapezoid with n > 4jmax+2 and GL with n points are exact up to rounding; 1e-10 is rounding with margin].
 P3  V=0 gap equals -ln(I_3/I_1) (abelian-like control: kinetic only) to 1e-10.
 P4  convergence: for beta in {2,4,8,16}, the gap m_e at (jmax=6, n=48) and (jmax=5, n=40) differ by < 5 % (my expectation).
 P5  m_e(beta) > -ln(I_3(beta)/I_1(beta)) (gap with V switched off) for each beta in {2,4,8,16} (expectation from R1).
 P6  nu0(beta) = lowest eigenvalue of the compression of 1-K+V (Galerkin UPPER bound): nu0*beta^(1/3) varies by
     less than a factor 2 over beta in {4,8,16} (expectation from the Simon-type bound; measured, upper-bound only).
 Measured only: m_e*beta^(1/3), m_e*beta, ratio m_e / (-ln I_3/I_1).
Results written to a new file (mode "x").
"""
import os, sys, math, json
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np

def bessel_I(n, x, N=4000):
    # e^{-x} I_n(x) = (1/pi) int_0^pi e^{x(cos t - 1)} cos(n t) dt, trapezoid (periodic, spectrally accurate)
    t = np.linspace(0, math.pi, N + 1)
    f = np.exp(x * (np.cos(t) - 1)) * np.cos(n * t)
    return (f.sum() - 0.5 * (f[0] + f[-1])) * math.pi / N / math.pi

def kappa(j, beta):
    return bessel_I(2 * j + 1, beta) / bessel_I(1, beta)

def spin(j):
    ms = np.arange(j, -j - 1, -1, dtype=float)
    d = len(ms)
    Jz = np.diag(ms)
    Jp = np.zeros((d, d))
    for i in range(1, d):
        m = ms[i]
        Jp[i - 1, i] = math.sqrt(j * (j + 1) - m * (m + 1))
    Jx = (Jp + Jp.T) / 2
    Jy = (Jp - Jp.T) / 2j
    return ms, Jx, Jy, Jz

def projectors(j1, j2):
    _, X1, Y1, Z1 = spin(j1); _, X2, Y2, Z2 = spin(j2)
    I1 = np.eye(2 * j1 + 1); I2 = np.eye(2 * j2 + 1)
    C = sum((np.kron(A, I2) + np.kron(I1, B)) @ (np.kron(A, I2) + np.kron(I1, B))
            for A, B in ((X1, X2), (Y1, Y2), (Z1, Z2)))
    w, v = np.linalg.eigh(C)
    out = {}
    for J in range(abs(j1 - j2), j1 + j2 + 1):
        sel = np.abs(w - J * (J + 1)) < 1e-8
        assert sel.sum() == 2 * J + 1
        out[J] = v[:, sel] @ v[:, sel].conj().T
    return out

def grid(n, nph):
    th = (np.arange(n) + 0.5) * math.pi / n
    wth = (math.pi / n) * (2 / math.pi) * np.sin(th) ** 2
    x, wx = np.polynomial.legendre.leggauss(nph)
    ph = (x + 1) * math.pi / 2
    wph = wx * math.pi / 2 * 0.5 * np.sin(ph)
    return th, wth, ph, wph

def basis(jmax, n, nph):
    th, wth, ph, wph = grid(n, nph)
    funcs, labels = [], []
    TH2, PH = np.meshgrid(th, ph, indexing="ij")  # (n, nph)
    for j2 in range(jmax + 1):
        ms2, X2, Y2, Z2 = spin(j2)
        wy, vy = np.linalg.eigh(Y2)
        # D2[p, a, b] for each (th2, ph)
        R = np.einsum("ak,pk,bk->pab", vy, np.exp(-1j * np.outer(PH.ravel(), wy)), vy.conj())
        Dg = np.exp(2j * np.outer(TH2.ravel(), ms2))  # (p, m)
        D2 = np.einsum("pak,pk,pbk->pab", R, Dg, R.conj())
        for j1 in range(jmax + 1):
            ms1 = np.arange(j1, -j1 - 1, -1, dtype=float)
            E1 = np.exp(2j * np.outer(th, ms1))  # (n, d1)
            d1, d2 = 2 * j1 + 1, 2 * j2 + 1
            for J, P in projectors(j1, j2).items():
                P4 = P.reshape(d1, d2, d1, d2)
                B = np.einsum("iaib->iba", P4)  # B[m1, m2, m2'] = P[(m1,m2'),(m1,m2)]
                G = np.einsum("pab,iab->ip", D2, B)  # (d1, n*nph)
                Psi = (E1 @ G).ravel()  # (n * n * nph), order th1, th2, ph
                Psi = Psi * math.sqrt(d1 * d2 / (2 * J + 1))
                funcs.append(Psi); labels.append((j1, j2, J))
    W = np.einsum("a,b,c->abc", wth, wth, wph).ravel()
    T1, T2, P3 = np.meshgrid(th, th, ph, indexing="ij")
    S = (np.sin(T1) ** 2 * np.sin(T2) ** 2 * np.sin(P3) ** 2).ravel()
    return np.array(funcs), labels, W, S

def su2(theta, n):
    s = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])
    return math.cos(theta) * np.eye(2) + 1j * math.sin(theta) * np.einsum("k,kab->ab", n, s)

def run(betas, jmax, n, nph, Psi, labels, W, S):
    res = {}
    for beta in betas:
        kap = np.array([kappa(j1, beta) * kappa(j2, beta) for (j1, j2, J) in labels])
        A = (Psi.conj() * (W * np.exp(-2 * beta * S))) @ Psi.T
        Kh = np.sqrt(kap)
        Tm = Kh[:, None] * A * Kh[None, :]
        ev = np.sort(np.linalg.eigvalsh((Tm + Tm.conj().T) / 2))[::-1]
        Vm = (Psi.conj() * (W * 2 * beta * S)) @ Psi.T
        H = np.diag(1 - kap) + Vm
        nu = np.sort(np.linalg.eigvalsh((H + H.conj().T) / 2))
        free = -math.log(kappa(1, beta))
        res[beta] = dict(lam0=ev[0], lam1=ev[1], gap=-math.log(ev[1] / ev[0]), nu0=nu[0], free_gap=free)
    return res

if __name__ == "__main__":
    out = open(sys.argv[1], "x")
    log = lambda *a: (print(*a), print(*a, file=out), out.flush())
    rng = np.random.default_rng(1)
    # P1
    err = 0.0; beta = 1.0
    for _ in range(2000):
        a = rng.normal(size=3); a /= np.linalg.norm(a); b = rng.normal(size=3); b /= np.linalg.norm(b)
        t1, t2 = rng.uniform(0, math.pi, 2)
        U1, U2 = su2(t1, a), su2(t2, b)
        Vd = beta * (1 - 0.5 * np.trace(U1 @ U2 @ U1.conj().T @ U2.conj().T).real)
        sph2 = 1 - np.dot(a, b) ** 2
        Vf = 2 * beta * math.sin(t1) ** 2 * math.sin(t2) ** 2 * sph2
        err = max(err, abs(Vd - Vf))
    log("P1 max|V_direct - V_formula| =", err, "MET" if err < 1e-10 else "FAILED")
    verdict = {}
    for (jmax, n) in ((5, 40), (6, 48)):
        Psi, labels, W, S = basis(jmax, n, n)
        G = (Psi.conj() * W) @ Psi.T
        e2 = np.abs(G - np.eye(len(labels))).max()
        log(f"jmax={jmax} n={n} N={len(labels)}  P2 max|Gram-1| = {e2:.3e}", "MET" if e2 < 1e-10 else "FAILED")
        # P3 with V=0
        b0 = 4.0
        kap = np.array([kappa(j1, b0) * kappa(j2, b0) for (j1, j2, J) in labels])
        ev = np.sort(kap)[::-1]
        d3 = abs(-math.log(ev[1] / ev[0]) + math.log(kappa(1, b0)))
        log(f"  P3 V=0 gap - (-ln I3/I1) = {d3:.2e}", "MET" if d3 < 1e-10 else "FAILED")
        r = run((2.0, 4.0, 8.0, 16.0), jmax, n, n, Psi, labels, W, S)
        verdict[(jmax, n)] = r
        for b, v in r.items():
            log(f"  beta={b:5.1f} lam0={v['lam0']:.8f} lam1={v['lam1']:.8f} m_e={v['gap']:.6f} m_e*b^(1/3)={v['gap']*b**(1/3):.4f} "
                f"m_e*b={v['gap']*b:.3f} free_gap={v['free_gap']:.6f} ratio={v['gap']/v['free_gap']:.3f} nu0={v['nu0']:.6f} nu0*b^(1/3)={v['nu0']*b**(1/3):.4f}")
        del Psi
    a, bb = verdict[(5, 40)], verdict[(6, 48)]
    for b in (2.0, 4.0, 8.0, 16.0):
        rel = abs(a[b]['gap'] - bb[b]['gap']) / bb[b]['gap']
        log(f"P4 beta={b} rel diff {rel:.4f}", "MET" if rel < 0.05 else "FAILED")
        log(f"P5 beta={b} m_e={bb[b]['gap']:.6f} > free {bb[b]['free_gap']:.6f}", "MET" if bb[b]['gap'] > bb[b]['free_gap'] else "FAILED")
    xs = [bb[b]['nu0'] * b ** (1 / 3) for b in (4.0, 8.0, 16.0)]
    log("P6 nu0*b^(1/3) over beta 4,8,16:", xs, "MET" if max(xs) / min(xs) < 2 else "FAILED")
    out.close()
