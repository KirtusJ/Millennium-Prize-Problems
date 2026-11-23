"""h2spec.py -- independent Rayleigh-Ritz spectrum of
    h_2 = -1/2 (Lap_1 + Lap_2) + 2 |x1 x x2|^2   on rotation-invariant L^2(R^3 x R^3)
(paper/sec_smallbox.tex, operator h_k with k=2).

Method (third method; the folder used Peter-Weyl lattice + continuum Rayleigh-Ritz, and Nystrom):
rotation-invariant f = sum_l Phat_l(c) F_l(r1, r2), c = xhat1.xhat2, with
F_l(r1,r2) = sum_{n1,n2} a R_{n1,l}(r1) R_{n2,l}(r2), R_{n,l} the 3D harmonic-oscillator radial
functions of frequency w. In block l the kinetic part is the l-wave radial Laplacian in r1 and r2;
the potential 2 r1^2 r2^2 (1-c^2) couples l to l, l+-2. Quadratures: Gauss-Legendre in r on [0,RMAX]
and in c. Dense eigvalsh per l-parity sector (numpy only; scipy absent), one thread.

Predicates (fixed before the first run). Targets from sec_smallbox.tex Table sb:tab-num.
 P0 (convergence, my own): the lowest 6 levels change by < 2e-6 between truncation (L=Lb, N=Nb) and
    the largest truncation. Tolerance: chosen so that P1-P2 at 1e-5 are meaningful.
 P1: |e0 - 3.3505330| < 1e-5.      (paper quotes 7 decimals; 1e-5 = my truncation budget)
 P2: |e1 - 5.3254970| < 1e-5.
 P3: e1 is a doublet: |e2 - e1| < 1e-5 (exact O(2) doublet of charge two, stated proved).
 P4: the doublet lies below the first excited level of O(2)-charge 0. Charge is assigned by the
     swap r1<->r2 / degeneracy pattern: a nondegenerate level is charge 0. Predicate: the first
     nondegenerate level above e0 is > e1 + 1e-3. ("rests on the numerics" in the paper.)
 P5: |(e1 - e0) - 1.974964| < 2e-5.
Exit code 0 always (predicates are reported, not asserted); result file opened with mode "x".
"""
import os, sys, math, json
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
from numpy.polynomial.legendre import leggauss

def eval_genlaguerre(n, a, x):
    p0 = np.ones_like(x)
    if n == 0: return p0
    p1 = 1 + a - x
    for k in range(1, n):
        p0, p1 = p1, ((2 * k + 1 + a - x) * p1 - (k + a) * p0) / (k + 1)
    return p1
def eval_legendre(n, x):
    p0 = np.ones_like(x)
    if n == 0: return p0
    p1 = x.copy()
    for k in range(1, n):
        p0, p1 = p1, ((2 * k + 1) * x * p1 - k * p0) / (k + 1)
    return p1
gammaln = math.lgamma

def build(L, N, w, RMAX=9.0, NQ=600, NC=200):
    xr, wr = leggauss(NQ); r = 0.5 * RMAX * (xr + 1); wr = 0.5 * RMAX * wr
    xc, wc = leggauss(NC)
    R = {}
    for l in range(L + 1):
        M = np.empty((N, r.size))
        for n in range(N):
            lognorm = 0.5 * (math.log(2) + (l + 1.5) * math.log(w) + gammaln(n + 1) - gammaln(n + l + 1.5))
            with np.errstate(divide="ignore"):
                logpart = lognorm + l * np.log(r) - 0.5 * w * r * r
            M[n] = np.exp(logpart) * eval_genlaguerre(n, l + 0.5, w * r * r)
        R[l] = M
    # Legendre normalized
    P = np.empty((L + 1, xc.size))
    for l in range(L + 1):
        P[l] = math.sqrt((2 * l + 1) / 2) * eval_legendre(l, xc)
    Mc = (P * (1 - xc ** 2) * wc) @ P.T          # <l|(1-c^2)|l'>
    T, A = {}, {}
    for l in range(L + 1):
        r2 = (R[l] * (r ** 4) * wr) @ R[l].T      # <n|r^2|n'> with measure r^2 dr
        T[l] = np.diag(w * (2 * np.arange(N) + l + 1.5)) - 0.5 * w * w * r2
    for l in range(L + 1):
        for lp in (l, l + 2):
            if lp <= L:
                A[(l, lp)] = (R[l] * (r ** 4) * wr) @ R[lp].T
    ortho = max(np.abs((R[l] * r**2 * wr) @ R[l].T - np.eye(N)).max() for l in range(L + 1))
    return T, A, Mc, ortho

def spectrum(L, N, w, k=8):
    """dense diagonalization, separately for even l and odd l (potential couples l to l, l+-2)."""
    T, A, Mc, ortho = build(L, N, w)
    I = np.eye(N); allv = []
    for par in (0, 1):
        ls = [l for l in range(L + 1) if l % 2 == par]
        B = N * N; H = np.zeros((len(ls) * B, len(ls) * B))
        for i, l in enumerate(ls):
            H[i*B:(i+1)*B, i*B:(i+1)*B] = np.kron(T[l], I) + np.kron(I, T[l]) \
                + 2 * Mc[l, l] * np.kron(A[(l, l)], A[(l, l)])
            if l + 2 <= L:
                blk = 2 * Mc[l, l + 2] * np.kron(A[(l, l + 2)], A[(l, l + 2)])
                H[i*B:(i+1)*B, (i+1)*B:(i+2)*B] = blk
                H[(i+1)*B:(i+2)*B, i*B:(i+1)*B] = blk.T
        allv.append(np.linalg.eigvalsh(H)[:k])
    return np.sort(np.concatenate(allv))[:k], ortho

if __name__ == "__main__":
    out = sys.argv[1]
    w = 1.6
    runs = {}
    for (L, N) in [(16, 14), (22, 18), (28, 22)]:
        ev, ortho = spectrum(L, N, w)
        runs[f"L{L}_N{N}"] = ev.tolist()
        print(L, N, "ortho_err", f"{ortho:.1e}", " ".join(f"{x:.8f}" for x in ev), flush=True)
    keys = list(runs)
    big = np.array(runs[keys[-1]]); mid = np.array(runs[keys[-2]])
    e = big
    conv = float(np.abs(big[:6] - mid[:6]).max())
    # degeneracy grouping
    levels = []
    for x in e:
        if levels and abs(x - levels[-1][0]) < 1e-5: levels[-1][1] += 1
        else: levels.append([x, 1])
    first_nondeg_above = next((x for x, m in levels[1:] if m == 1), None)
    preds = {
        "P0_convergence<2e-6": (conv, conv < 2e-6),
        "P1_e0": (e[0], abs(e[0] - 3.3505330) < 1e-5),
        "P2_e1": (e[1], abs(e[1] - 5.3254970) < 1e-5),
        "P3_doublet": (e[2] - e[1], abs(e[2] - e[1]) < 1e-5),
        "P4_first_scalar_above_doublet": (first_nondeg_above,
                                         first_nondeg_above is not None and first_nondeg_above > e[1] + 1e-3),
        "P5_gap": (e[1] - e[0], abs(e[1] - e[0] - 1.974964) < 2e-5),
    }
    with open(out, "x") as f:
        json.dump({"w": w, "runs": runs, "levels": levels,
                   "predicates": {k: [float(v[0]) if v[0] is not None else None, bool(v[1])] for k, v in preds.items()}},
                  f, indent=1)
    for k, v in preds.items(): print(k, v)
