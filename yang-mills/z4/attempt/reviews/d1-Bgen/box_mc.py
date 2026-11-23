"""box_mc.py -- test (ii) of brief d1-Bgen.

Box R_1 = [-1,1]^4: one interior site (origin), 8 links from the origin (oriented outward,
W_i, i=(mu,sign)), shell links fixed to 1. P_R = the 24 plaquettes spanned by two perpendicular
links at the origin; U_p = W_i W_j^{-1} up to conjugation/inversion, which leave
s(U) = 1 - (1/N) Re Tr rho(U) unchanged. Measure on (W_i): prop. exp(-beta sum_p s(U_p)) prod Haar.
Observable O_p = beta * s(U_p).

Derived prediction (THEOREM_B_GENERAL.md sec. 'Box normalisation'): in rho-orthonormal
coordinates of the Lie algebra the Laplace limit is dim(G) independent colours, each with the
one-colour Dirichlet Maxwell covariance C; O_p -> (1/2)|F_p|^2_rho, hence
    lim_{beta->inf} E O_p = (dim G / 2) * C_pp,  C_pp = 7/24 (one colour, R_1),
with normalisation factor exactly 1 for every faithful rho (no group-dependent factor).

PREDICATES (fixed before the first run):
 P0: C_pp computed by linear algebra from Q(phi)=sum_p (phi_i-phi_j)^2, phi_{(0,+)}=0 (T_int gauge),
     equals 7/24 within 1e-12 (tolerance: double-precision rounding of an 7x7 solve).
 For G in {U1 (rho=e^{it}), U1x2 (rho=e^{it}+e^{2it}, N=2, faithful), SU2 (fund), SU3 (fund)}, beta=300:
 P1[G]: |mean O_{p0} - (d/2)(7/24)| <= 4*SE + 0.03*(d/2)(7/24)
 P2[G]: |mean over the 24 plaquettes of O_p - (d/2)(7/24)| <= 4*SE + 0.03*(d/2)(7/24)
   SE = standard error across independent chains (chains independent, fixed seed).
   4*SE: statistical (two-sided Gaussian ~6e-5 false-alarm). 3%: allowance for O(1/beta)
   corrections at beta=300 (relative coefficient up to 9 tolerated); it is an assumption, not derived.
 MEASURED ONLY: acceptance rates; SU3 at beta=1200 (trend), SU3 at beta=75.
Seeds: numpy default_rng(20261123 + k). Output: box_mc_results.txt opened with mode 'x'.
Exit code 0 if all predicates met, 1 otherwise.
"""
import itertools, sys, time
import numpy as np

LINKS = [(mu, sg) for mu in range(4) for sg in (+1, -1)]          # 8 links
PAIRS = [(a, b) for a, b in itertools.combinations(range(8), 2) if LINKS[a][0] != LINKS[b][0]]
assert len(PAIRS) == 24
P0IDX = PAIRS.index((LINKS.index((1, 1)), LINKS.index((2, 1))))
NBR = {i: [k for k, (a, b) in enumerate(PAIRS) if i in (a, b)] for i in range(8)}
assert all(len(v) == 6 for v in NBR.values())


def cpp():
    free = [i for i in range(8) if LINKS[i] != (0, 1)]
    D = np.zeros((24, 7))
    for k, (a, b) in enumerate(PAIRS):
        if a in free: D[k, free.index(a)] += 1
        if b in free: D[k, free.index(b)] -= 1
    Q = D.T @ D
    C = D @ np.linalg.solve(Q, D.T)
    return C[P0IDX, P0IDX], np.diag(C)


class Group:
    def __init__(self, name):
        self.name = name
        if name == 'U1': self.d, self.N = 1, 1
        elif name == 'U1x2': self.d, self.N = 1, 2
        elif name == 'SU2': self.d, self.N = 3, 2
        elif name == 'SU3': self.d, self.N = 8, 3

    # elements: abelian -> angle array; SU(n) -> complex matrices
    def identity(self, M):
        if self.name.startswith('U1'): return np.zeros(M)
        n = self.N
        return np.broadcast_to(np.eye(n, dtype=complex), (M, n, n)).copy()

    def s(self, A, B):  # s(A B^{-1})
        if self.name == 'U1': return 1 - np.cos(A - B)
        if self.name == 'U1x2':
            t = A - B
            return 1 - 0.5 * (np.cos(t) + np.cos(2 * t))
        P = A @ np.conj(np.swapaxes(B, -1, -2))
        return 1 - np.real(np.trace(P, axis1=-2, axis2=-1)) / self.N

    def propose(self, A, eps, rng):
        M = A.shape[0]
        if self.name.startswith('U1'):
            return A + eps * rng.standard_normal(M)
        n = self.N
        Z = rng.standard_normal((M, n, n)) + 1j * rng.standard_normal((M, n, n))
        H = (Z + np.conj(np.swapaxes(Z, -1, -2))) / 2
        H = H - np.trace(H, axis1=-2, axis2=-1)[:, None, None] * np.eye(n) / n
        w, V = np.linalg.eigh(H)
        R = (V * np.exp(1j * eps * w)[:, None, :]) @ np.conj(np.swapaxes(V, -1, -2))
        return R @ A   # symmetric proposal (H and -H equally likely) -> Haar-reversible


def run(gname, beta, seed, chains=1000, therm=400, meas=1200, eps_c=1.0):
    G = Group(gname)
    rng = np.random.default_rng(seed)
    W = [G.identity(chains) for _ in range(8)]
    eps = eps_c / np.sqrt(beta)
    acc = 0; tot = 0
    sum0 = np.zeros(chains); sumall = np.zeros(chains)
    for sweep in range(therm + meas):
        for i in range(8):
            new = G.propose(W[i], eps, rng)
            dS = np.zeros(chains)
            for k in NBR[i]:
                a, b = PAIRS[k]
                o = b if a == i else a
                dS += G.s(new, W[o]) - G.s(W[i], W[o])
            ok = rng.random(chains) < np.exp(-beta * dS)
            if G.name.startswith('U1'): W[i] = np.where(ok, new, W[i])
            else: W[i] = np.where(ok[:, None, None], new, W[i])
            acc += ok.sum(); tot += chains
        if sweep >= therm:
            Os = np.array([beta * G.s(W[a], W[b]) for a, b in PAIRS])
            sum0 += Os[P0IDX]; sumall += Os.mean(0)
    m0 = sum0 / meas; ma = sumall / meas
    return dict(G=gname, d=G.d, N=G.N, beta=beta, mean0=m0.mean(), se0=m0.std(ddof=1) / np.sqrt(chains),
                meanall=ma.mean(), seall=ma.std(ddof=1) / np.sqrt(chains), acc=acc / tot)


EPS = {'U1': 1.0, 'U1x2': 0.5, 'SU2': 0.5, 'SU3': 0.3}  # step tuned for ~50% acceptance (tuning runs wrote no result file)


def main():
    out = open('box_mc_results.txt', 'x')
    def w(s):
        print(s); out.write(s + '\n'); out.flush()
    allok = True
    c, diag = cpp()
    p0 = abs(c - 7 / 24) <= 1e-12
    allok &= p0
    w(f"P0 C_pp={c:.15f} 7/24={7/24:.15f} all-24 diag min/max={diag.min():.15f}/{diag.max():.15f} -> {'MET' if p0 else 'FAILED'}")
    k = 0
    for g in ['U1', 'U1x2', 'SU2', 'SU3']:
        t0 = time.time()
        r = run(g, 300.0, 20261123 + k, eps_c=EPS[g]); k += 1
        pred = r['d'] / 2 * 7 / 24
        tol0 = 4 * r['se0'] + 0.03 * pred; tola = 4 * r['seall'] + 0.03 * pred
        ok1 = abs(r['mean0'] - pred) <= tol0; ok2 = abs(r['meanall'] - pred) <= tola
        allok &= ok1 and ok2
        w(f"{g} d={r['d']} N={r['N']} beta=300 pred={pred:.5f} p0: {r['mean0']:.5f}+-{r['se0']:.5f} (rel {r['mean0']/pred-1:+.4f}) P1 {'MET' if ok1 else 'FAILED'}; "
          f"all24: {r['meanall']:.5f}+-{r['seall']:.5f} (rel {r['meanall']/pred-1:+.4f}) P2 {'MET' if ok2 else 'FAILED'}; acc={r['acc']:.3f} t={time.time()-t0:.0f}s")
    for beta in (75.0, 1200.0):
        r = run('SU3', beta, 20261123 + k, chains=500, eps_c=EPS['SU3']); k += 1
        pred = 8 / 2 * 7 / 24
        w(f"MEASURED SU3 beta={beta:.0f}: all24 {r['meanall']:.5f}+-{r['seall']:.5f} rel {r['meanall']/pred-1:+.4f} acc={r['acc']:.3f}")
    w('ALL PREDICATES MET' if allok else 'SOME PREDICATE FAILED')
    out.close()
    sys.exit(0 if allok else 1)


if __name__ == '__main__':
    main()
