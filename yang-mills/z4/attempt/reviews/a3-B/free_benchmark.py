"""free_benchmark.py -- worker a3-B, test (iii), part 1: the free target of step S3.

Object. One colour of free lattice Maxwell field on Z^4, action (1/2) sum_p (dA)_p^2,
Feynman gauge <A_mu A_nu>(k) = delta_{mu nu} / khat^2, khat_mu^2 = 4 sin^2(k_mu/2).
G(n) := <F_12(0) F_12(n e_0)>, F_12 a spatial plaquette, separation n along time e_0.
Integrating k_0 exactly: int dk0/2pi e^{i k0 n}/(khat0^2 + M^2) = e^{-E n}/(2 sinh E), cosh E = 1 + M^2/2,
so G(n) = int_{[-pi,pi]^3} d^3k/(2pi)^3 (khat1^2 + khat2^2) e^{-E n} / (2 sinh E).
The SU(2) step S3 asserts beta^2 Cov(1-1/2TrU_p(0), 1-1/2TrU_p(n)) -> (3/2)*... * G(n)^2, so the ratio
c(n) := C(n)/C(0) = (G(n)/G(0))^2 (colour count cancels; Wick).
Quadrature: midpoint rule, K points per axis (never hits k=0).

PREDICATES (fixed before the first run):
 P1  |G(0) - 1/2| <= 2e-3 at K=128. (Exact value 1/2 by symmetry: sum_mu khat_mu^2 = khat^2, 2 of 4 directions.)
     Tolerance source: P1b must show the K=96 -> K=128 change is below 2e-3.
 P1b |G_K128(n) - G_K96(n)| <= 2e-3 * G_K128(n) for n = 0..10 (relative; quadrature-stability criterion I choose).
 P2  G(n) > 0 for n = 0..10 (required: Laplace transform of a positive measure, RP).
 P3  log-convexity G(n)^2 <= G(n-1) G(n+1) for n = 1..9 (required for the same reason), with slack 1e-12 relative.
 P4  power law: n^4 G(n) at n = 10 and n = 6 agree within 15 % (continuum F-F correlator ~ |x|^-4;
     15 % allows O(1/n^2) lattice corrections, 1/36 ~ 3 % times a constant I do not know; chosen by me).
 Measured only: c(n) = (G(n)/G(0))^2; b(n) = log(c(n)/c(n+1)) = the gap bound limsup m <= b(n) that S2 gives
     IF S3 held; n*b(n) (expected -> 8); the four-dimensional chessboard bad-plaquette bound of step S3a,
     exp(-beta delta + 6 beta (1-cos 4eps) - 4 log H(eps)), minimised over eps, for some beta, delta.
Output: argv[1], opened with mode "x". Deterministic (no randomness).
"""
import sys, math
import numpy as np


def G_all(K, nmax):
    k = -np.pi + (np.arange(K) + 0.5) * 2 * np.pi / K
    s = 4 * np.sin(k / 2) ** 2
    k1, k2, k3 = np.meshgrid(s, s, s, indexing="ij", sparse=True)
    M2 = k1 + k2 + k3
    E = np.arccosh(1 + M2 / 2)
    num = (k1 + k2) / (2 * np.sinh(E))
    out = []
    for n in range(nmax + 1):
        out.append(float(np.mean(num * np.exp(-E * n))))
    return out


def chess4(beta, delta):
    best = None
    for eps in np.linspace(1e-4, math.pi / 4, 20000):
        H = (eps - math.sin(eps) * math.cos(eps)) / math.pi
        v = -beta * delta + 6 * beta * (1 - math.cos(4 * eps)) - 4 * math.log(H)
        best = v if best is None or v < best else best
    return best  # natural log of the bound


def main():
    out = open(sys.argv[1], "x")
    w = lambda s: (out.write(s + "\n"), print(s))
    nmax = 10
    g96 = G_all(96, nmax)
    g128 = G_all(128, nmax)
    res = {}
    res["P1"] = abs(g128[0] - 0.5) <= 2e-3
    res["P1b"] = all(abs(g128[n] - g96[n]) <= 2e-3 * g128[n] for n in range(nmax + 1))
    res["P2"] = all(g > 0 for g in g128)
    res["P3"] = all(g128[n] ** 2 <= g128[n - 1] * g128[n + 1] * (1 + 1e-12) for n in range(1, nmax))
    r = (10 ** 4 * g128[10]) / (6 ** 4 * g128[6])
    res["P4"] = abs(r - 1) <= 0.15
    w("n  G_K96  G_K128  c(n)=(G/G0)^2  b(n)=log(c(n)/c(n+1))  n*b(n)")
    for n in range(nmax + 1):
        c = (g128[n] / g128[0]) ** 2
        b = 2 * math.log(g128[n] / g128[n + 1]) if n < nmax else float("nan")
        w(f"{n} {g96[n]:.6e} {g128[n]:.6e} {c:.6e} {b:.5f} {n*b:.4f}")
    w(f"P4 ratio 10^4G(10)/(6^4G(6)) = {r:.4f}")
    w("measured: 4D chessboard bound log P(1-cos a_p > delta) <= L(beta,delta)")
    for beta in (8, 32, 128, 512):
        for delta in (0.1, 0.5, 1.0):
            w(f"beta={beta} delta={delta} logBound={chess4(beta, delta):.3f}")
    met = sum(res.values()); failed = len(res) - met
    for kk, v in res.items():
        w(f"{kk}: {'MET' if v else 'FAILED'}")
    w(f"counts: met {met}, failed {failed}, measured only 3")
    out.close()
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
