"""Coercivity check, H = 1 - K + V - c1*D on the Z2-even, conjugation-invariant SU(2)^2 sector.

PREDICATES (fixed before first run):
 P1: beta^{1/3} * Lambda(beta, c1=1) >= -1 for every beta computed (tolerance -1 from parent).
     Hypothesis test: report how many (beta) cases qualify (are computed at the finest N, grid).
 P2 (measured only): beta^{1/3} * Lambda(beta, c1=0) (parent expects ~3.35 slowly).
 P3 (measured only): change of beta^{1/3}*Lambda between N and N+8 and between two quadrature grids.
 P4 (check): beta=16,c1=0,N=12 full space (no symmetry) Lambda ~ 0.811 (tolerance 5e-3, 'about').
Galerkin truncation gives UPPER bounds on the true lowest eigenvalue.
Reduction used for large N: swap-symmetric (n1<->n2) and L-even subspace; validated against the
full space at N=12 (P4 run), which also records lowest in each sector.
Quadrature: trapezoid in a on [0,pi] (endpoints half weight); Gauss-Legendre in t with N+4 points.
Run: python3 lam.py check|main
"""
import sys, json, numpy as np
from numpy.polynomial.legendre import leggauss, legval

def bessel_I(n, x):
    t = (x/2)**n
    for j in range(1, n+1): t /= j
    s = 0.0
    for k in range(1500):
        s += t; t *= (x/2)**2/((k+1)*(k+1+n))
        if t < 1e-18*s: break
    return s

def Fgrid(N, a):
    """F[L][n_even] on grid a, normalised numerically w.r.t. (2/pi) sin^2 a da (trapezoid weights w)."""
    x = np.cos(a); s = np.sin(a)
    M = len(a); w = np.full(M, np.pi/(M-1)); w[0] *= .5; w[-1] *= .5
    w = w*(2/np.pi)*s**2
    F = {}
    for L in range(N+1):
        lam = L+1
        C = [np.ones(M), 2*lam*x]
        for k in range(2, N-L+1):
            C.append((2*x*(k+lam-1)*C[k-1]-(k+2*lam-2)*C[k-2])/k)
        for n in range(L, N+1):
            if n % 2: continue
            f = s**L*C[n-L]
            f = f/np.sqrt(np.sum(w*f*f))
            F[(n, L)] = f
    return F, w, s

def build(beta, N, M, sym, lpar):
    """returns H0 (1-K+V) and D matrices in chosen subspace, and state list."""
    a = np.linspace(0, np.pi, M)
    F, w, s = Fgrid(N, a)
    ns = list(range(0, N+1, 2)); ni = {n: i for i, n in enumerate(ns)}
    I1 = bessel_I(1, beta)
    kap = np.array([bessel_I(n+1, beta)/I1 for n in ns])
    tg, tw = leggauss(N+4)
    Lmax = N
    P = [np.sqrt(2*L+1)*legval(tg, [0]*L+[1]) for L in range(Lmax+1)]
    Ls = [L for L in range(Lmax+1) if (lpar is None or L % 2 == lpar)]
    # states
    st = {}  # L -> (I,J,f) arrays
    for L in Ls:
        idx = [ni[n] for n in ns if n >= L]
        pr = [(i, j) for i in idx for j in idx if (i <= j if sym else True)]
        I = np.array([p[0] for p in pr]); J = np.array([p[1] for p in pr])
        f = np.where(I == J, 1/np.sqrt(2), 1.0) if sym else np.ones(len(I))
        st[L] = (I, J, f)
    off = {}; tot = 0
    for L in Ls: off[L] = tot; tot += len(st[L][0])
    H = np.zeros((tot, tot)); D = np.zeros((tot, tot))
    def MV(L, Lp):
        A = np.zeros((len(ns), len(ns)))
        for n in ns:
            if (n, L) not in F: continue
            for m in ns:
                if (m, Lp) in F: A[ni[n], ni[m]] = np.sum(w*s**2*F[(n, L)]*F[(m, Lp)])
        return A
    S = {}
    for L in Ls:
        A = np.zeros((len(ns), len(ns)))
        for n in ns:
            for m in ns:
                if (n, L) in F and (m, L) in F: A[ni[n], ni[m]] = np.sum(w*s*F[(n, L)]*F[(m, L)])
        S[L] = A
    def elem(X1, X2, f1, f2):
        return (X1 + (X2 if sym else 0))*np.outer(f1, f2)
    for L in Ls:
        I, J, f = st[L]
        kk = kap[I]*kap[J]
        H[off[L]:off[L]+len(I), off[L]:off[L]+len(I)] += np.diag(1-(kk if True else 0))
        # D
        A = S[L]; dl = lambda p, q: (p[:, None] == q[None, :]).astype(float)
        X1 = A[I[:, None], I[None, :]]*dl(J, J)+dl(I, I)*A[J[:, None], J[None, :]]
        X2 = A[I[:, None], J[None, :]]*dl(J, I)+dl(I, J)*A[J[:, None], I[None, :]]
        D[off[L]:off[L]+len(I), off[L]:off[L]+len(I)] += elem(X1, X2, f, f)
        for Lp in Ls:
            T = np.sum(tw*P[L]*P[Lp]*(1-tg**2))/2
            if abs(T) < 1e-14: continue
            A = MV(L, Lp); Ip, Jp, fp = st[Lp]
            X1 = A[I[:, None], Ip[None, :]]*A[J[:, None], Jp[None, :]]
            X2 = A[I[:, None], Jp[None, :]]*A[J[:, None], Ip[None, :]]
            H[off[L]:off[L]+len(I), off[Lp]:off[Lp]+len(Ip)] += 2*beta*T*elem(X1, X2, f, fp)
    return H, D, tot

def lam(H, D, c1):
    Hm = H - c1*D
    Hm = (Hm+Hm.T)/2
    return np.linalg.eigvalsh(Hm)[0]

if __name__ == "__main__":
    mode = sys.argv[1]
    out = {}
    if mode == "check":
        for name, sym, lp in [("full", False, None), ("sym_Leven", True, 0), ("sym_Lodd", True, 1), ("full_Leven", False, 0), ("full_Lodd", False, 1)]:
            H, D, tot = build(16, 12, 52, sym, lp)
            out[name] = dict(dim=tot, lam_c0=float(lam(H, D, 0)), lam_c1=float(lam(H, D, 1)))
            print(name, out[name], flush=True)
    else:
        for beta, Ns in [(16, [24, 32]), (64, [40, 48])]:
            for N in Ns:
                for gname, M in [("g1", 2*N+20), ("g2", 6*N+60)]:
                    H, D, tot = build(beta, N, M, True, 0)
                    for c1 in (0, 1):
                        L = float(lam(H, D, c1))
                        r = dict(beta=beta, N=N, M=M, c1=c1, dim=tot, Lambda=L, scaled=beta**(1/3)*L)
                        out[f"{beta}_{N}_{gname}_{c1}"] = r; print(r, flush=True)
    with open(f"result_{mode}.json", "x") as fh: json.dump(out, fh, indent=1)
