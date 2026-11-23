#!/usr/bin/env python3
"""mc_check.py -- independent recheck (Monte Carlo, no projectors, own lattice code) of
dual_sign.py, and exact-vs-child comparison.

PREDICATES (fixed before first run):
 M1 (target of the test): on the periodic 2x1x1 lattice in d=3 with plaquette spins
    site (0,0,0): j(01)=0, j(02)=1, j(12)=1 ; site (1,0,0): j(01)=1, j(02)=0, j(12)=1/2
    the amplitude A = E_Haar[prod_p chi_{j_p}(U_p)] is NEGATIVE: estimate + 4 SE < 0.
    Also consistent with the exact value -0.003086419753 within 4 SE.
    Tolerance 4 SE: CLT standard error of the sample mean, N = 4e7, seed 7.
 M2 (cross-check of the child): exact A(a,b,c) on the one-site 3-torus (from dual_sign.amplitude)
    agrees with the child's MC values within 4 of the child's SEs, for the 8 cases it reported.
Characters: x = tr U; chi_0 = 1, chi_{1/2} = x, chi_1 = x^2 - 1.
"""
import sys, numpy as np

def haar(rng, n):
    q = rng.standard_normal((n, 4)); q /= np.linalg.norm(q, axis=1, keepdims=True)
    a = q[:, 0] + 1j*q[:, 1]; b = q[:, 2] + 1j*q[:, 3]
    U = np.empty((n, 2, 2), complex)
    U[:, 0, 0] = a; U[:, 0, 1] = -np.conj(b); U[:, 1, 0] = b; U[:, 1, 1] = np.conj(a)
    return U

def chi(j, x):
    return {0: np.ones_like(x), 0.5: x, 1: x*x - 1}[j]

def main(out):
    f = open(out, 'x'); W = lambda s: (print(s), f.write(s+'\n'), f.flush())
    rng = np.random.default_rng(7)
    # links of 2x1x1: x in {0,1}, mu in {0,1,2}; neighbours: x+e0 = 1-x, x+e1 = x, x+e2 = x
    spins = {(0, 0, 1): 0, (0, 0, 2): 1, (0, 1, 2): 1, (1, 0, 1): 1, (1, 0, 2): 0, (1, 1, 2): 0.5}
    def nb(x, mu): return 1 - x if mu == 0 else x
    N, chunk = 40_000_000, 1_000_000
    s1 = s2 = 0.0
    dag = lambda M: np.conj(np.transpose(M, (0, 2, 1)))
    for _ in range(N // chunk):
        U = {(x, mu): haar(rng, chunk) for x in (0, 1) for mu in (0, 1, 2)}
        prod = np.ones(chunk)
        for (x, mu, nu), j in spins.items():
            if j == 0: continue
            P = U[(x, mu)] @ U[(nb(x, mu), nu)] @ dag(U[(nb(x, nu), mu)]) @ dag(U[(x, nu)])
            tr = (P[:, 0, 0] + P[:, 1, 1]).real
            prod *= chi(j, tr)
        s1 += prod.sum(); s2 += (prod*prod).sum()
    m = s1/N; se = np.sqrt((s2/N - m*m)/N)
    exact = -0.003086419753
    m1a = m + 4*se < 0; m1b = abs(m - exact) < 4*se
    W(f"M1 A_MC = {m:.6f} +- {se:.6f} (N={N}, seed 7); negative at 4SE: {'MET' if m1a else 'FAILED'}; "
      f"agrees with exact {exact} at 4SE: {'MET' if m1b else 'FAILED'}")
    # M2
    sys.path.insert(0, '.')
    import dual_sign as ds
    nl, pl = ds.lattice((1, 1, 1))  # plaquettes (01),(02),(12) = (a,b,c) with a=P12-of-child etc.
    child = {(0.5, 0.5, 0.5): (0.55573, 0.00088), (0.5, 0.5, 1): (0.41578, 0.00101), (0.5, 1, 0.5): (0.41579, 0.00101),
             (0.5, 1, 1): (0.35944, 0.00117), (1, 0.5, 0.5): (0.41647, 0.00101), (1, 0.5, 1): (0.36033, 0.00117),
             (1, 1, 0.5): (0.36032, 0.00117), (1, 1, 1): (0.40670, 0.00136)}
    ok = 0
    for k, (v, e) in child.items():
        A = ds.amplitude(nl, pl, list(k)).real; good = abs(A - v) < 4*e; ok += good
        W(f"M2 {k}: exact {A:.6f}  child {v} +- {e}  z={(v-A)/e:+.2f} {'MET' if good else 'FAILED'}")
    W(f"M2: {ok} of {len(child)} met")
    f.close(); return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
