"""free_G.py -- challenger a5-chalB, attack A4 / S3c.

Free one-colour lattice Maxwell field on Z^4 (action 1/2 sum (dA)^2), Feynman gauge.
G(n) := <F_12(0) F_12(n e_0)>.  Integrating k_0 exactly:
   G(n) = int_{[-pi,pi]^3} d^3k/(2pi)^3 (khat_1^2 + khat_2^2) e^{-E n} / (2 sinh E),
   cosh E = 1 + w^2/2,  w^2 = khat_1^2+khat_2^2+khat_3^2,  khat_i^2 = 4 sin^2(k_i/2).
Midpoint rule on an N^3 grid (avoids k = 0 exactly).

PREDICATES (fixed before the first run):
 F1  G(0) = 1/2 (equipartition: 3 physical modes per site / 6 plaquettes per site),
     |G(0) - 0.5| <= 2e-3 at N = 256.  Tolerance: midpoint error of an integrand with a
     |k| cusp at 0, estimated O(N^-3)*const; 2e-3 is generous.
 F2  for all n in 0..16: G(n) > 0  (per-case count reported).
 F3  G strictly decreasing on 0..16.
 F4  continuum: G(t) ~ 1/(pi^2 t^4).  pi^2 n^4 G(n) in [0.85, 1.15] at n = 12.
     Tolerance: lattice artefacts O(n^-2) (~1%) plus grid error at k ~ 1/n with spacing
     2pi/256 = 0.025 (~ several % at n=12): 15%.
 F5  grid stability: |G_256(n) - G_192(n)| / G_256(n) <= 0.05 for n <= 12.
 F6  c(n) = (G(n)/G(0))^2 and -log c(n)/n decreasing for n = 2..16 (towards 0).
Measured only: c(n) for n=1..16, n log(c(n)/c(n+1)).
"""
import numpy as np, sys, json

def G_all(N, nmax):
    k = (np.arange(N) + 0.5) * 2*np.pi/N - np.pi
    s = 4*np.sin(k/2)**2
    out = np.zeros(nmax+1)
    for i in range(N):  # slice over k1 to save memory
        s1 = s[i]
        S2, S3 = np.meshgrid(s, s, indexing="ij")
        w2 = s1 + S2 + S3
        E = np.arccosh(1 + w2/2)
        base = (s1 + S2) / (2*np.sinh(E))
        for n in range(nmax+1):
            out[n] += np.sum(base*np.exp(-E*n))
    return out / N**3

def main(outfile):
    nmax = 16
    g256 = G_all(256, nmax); g192 = G_all(192, nmax)
    res = {"G256": g256.tolist(), "G192": g192.tolist()}
    preds = {}
    preds["F1"] = abs(g256[0]-0.5) <= 2e-3
    pos = [bool(g256[n] > 0) for n in range(nmax+1)]
    preds["F2"] = all(pos); res["F2_count"] = f"{sum(pos)}/{len(pos)} cases qualify"
    preds["F3"] = all(g256[n+1] < g256[n] for n in range(nmax))
    r12 = np.pi**2 * 12**4 * g256[12]; res["pi2_n4_G"] = {n: float(np.pi**2*n**4*g256[n]) for n in range(1, nmax+1)}
    preds["F4"] = 0.85 <= r12 <= 1.15
    rel = [abs(g256[n]-g192[n])/g256[n] for n in range(13)]; res["grid_rel"] = rel
    preds["F5"] = max(rel) <= 0.05
    c = (g256/g256[0])**2; res["c"] = c.tolist()
    rate = [-np.log(c[n])/n for n in range(1, nmax+1)]; res["minus_log_c_over_n"] = rate
    preds["F6"] = all(rate[i+1] < rate[i] for i in range(1, nmax-1))
    res["n_log_ratio"] = [float(n*np.log(c[n]/c[n+1])) for n in range(1, nmax)]
    res["predicates"] = {k: bool(v) for k, v in preds.items()}
    with open(outfile, "x") as f:
        json.dump(res, f, indent=1)
    for k, v in preds.items(): print(k, "MET" if v else "FAILED")
    print("G(0..4)", g256[:5], "c(1),c(2),c(4),c(10)", c[1], c[2], c[4], c[10])
    print("pi^2 n^4 G(n) at n=4,8,12,16:", [res["pi2_n4_G"][n] for n in (4, 8, 12, 16)])
    print("-log c(n)/n at n=2,8,16:", rate[1], rate[7], rate[15])
    return 0 if all(preds.values()) else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
