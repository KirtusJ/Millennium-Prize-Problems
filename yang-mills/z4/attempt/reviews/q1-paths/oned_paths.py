"""oned_paths.py -- worker o1-lower (T141). Canonical-path lower bound (Lemma P of TUNNEL_LOWER.md)
on the discrete 1-D model of oned_split.py (same build(), same weight trick).

Lemma P (discrete): with g the normalised even top eigenvector on the full circle (||g||=1),
Q_e = T_{z,z+1} g_z g_{z+1} for nearest-neighbour edges e=(z,z+1), and the path from x to sigma x
going in the positive direction (N/2 edges),
   Delta >= B1 := 4 / max_e ( W_e / Q_e ),  W_e = (N/2) * sum_{x : e in path(x)} g_x^2,
   B1 >= B2 := 8 min_e Q_e / N.
PREDICATES (fixed before first run):
 Q1 (theorem) B1 <= Delta*(1+1e-9) for all beta.  Tolerance: rounding.
 Q2 (theorem) B2 <= B1*(1+1e-12) for all beta.
 Q3 (expectation) log(Delta/B2)/sqrt(beta) < 0.15 for beta >= 1024 (prefactor log(N)/sqrt(beta) ~ 0.1).
 Q4 (expectation) -log(min_e Q_e)/sqrt(beta) -> c*: |.-c*| at 4096 < |.-c*| at 256.
Deterministic (seed 0). Output results_paths_<tag>.txt opened with mode "x".
"""
import sys, math
import numpy as np
import oned_split as o

np.random.seed(0)


def run(beta, hfac):
    N = int(math.ceil(2 * math.pi * math.sqrt(beta) / hfac / 4.0)) * 4
    x, T = o.build(beta, N)
    A = np.arange(N // 4, 3 * N // 4)
    sA = (A + N // 2) % N
    TAA = T[np.ix_(A, A)]; R = T[np.ix_(A, sA)]
    sb = math.sqrt(beta)
    P = o.psi(x[A])
    Wl = np.exp(sb * (P[:, None] - P[None, :]))
    lam_e, gw = o.top((TAA + R) * Wl)
    lam_o, fw = o.top((TAA - R) * Wl)
    s = np.exp(-sb * P)
    g = gw * s; f = fw * s
    Delta = 2 * float(f @ R @ g) / float(f @ g)
    G = np.zeros(N); G[A] = g; G[sA] = g
    G /= math.sqrt(float(G @ G))
    z = np.arange(N); z1 = (z + 1) % N
    Q = T[z, z1] * G[z] * G[z1]
    g2 = G ** 2
    # W_e for edge (z,z+1): x in {z-N/2+1, ..., z} (mod N)
    c = np.concatenate([[0.0], np.cumsum(np.concatenate([g2, g2]))])
    W = np.array([(N / 2) * (c[zz + N] - c[zz + N - N // 2]) for zz in range(N)])
    B1 = 4.0 / float(np.max(W / Q))
    B2 = 8.0 * float(Q.min()) / N
    return dict(N=N, Delta=Delta, B1=B1, B2=B2, minQ=float(Q.min()))


def main():
    tag = sys.argv[1]
    betas = [float(b) for b in sys.argv[2].split(",")]
    hf = float(sys.argv[3])
    cs = o.cstar()
    out = open(f"results_paths_{tag}.txt", "x")
    def w(s):
        print(s); out.write(s + "\n"); out.flush()
    w(f"c* = {cs:.7f}")
    w("beta N Delta B1 B2 Delta/B1 log(Delta/B2)/sqrtb -log(minQ)/sqrtb")
    rows = []
    for b in betas:
        r = run(b, hf); r['beta'] = b; rows.append(r)
        w(f"{b:g} {r['N']} {r['Delta']:.6e} {r['B1']:.6e} {r['B2']:.6e} {r['Delta']/r['B1']:.3f} "
          f"{math.log(r['Delta']/r['B2'])/math.sqrt(b):.4f} {-math.log(r['minQ'])/math.sqrt(b):.4f}")
    res = []
    def pred(n, ok, info):
        res.append(ok); w(f"{n}: {'MET' if ok else 'FAILED'} {info}")
    pred("Q1", all(r['B1'] <= r['Delta'] * (1 + 1e-9) for r in rows), "")
    pred("Q2", all(r['B2'] <= r['B1'] * (1 + 1e-12) for r in rows), "")
    big = [r for r in rows if r['beta'] >= 1024]
    pred("Q3", all(math.log(r['Delta'] / r['B2']) / math.sqrt(r['beta']) < 0.15 for r in big),
         ",".join(f"{math.log(r['Delta']/r['B2'])/math.sqrt(r['beta']):.4f}" for r in big))
    by = {r['beta']: r for r in rows}
    if 256.0 in by and 4096.0 in by:
        d = [abs(-math.log(by[b]['minQ']) / math.sqrt(b) - cs) for b in (256.0, 4096.0)]
        pred("Q4", d[1] < d[0], f"{d[0]:.4f} -> {d[1]:.4f}")
    w(f"SUMMARY met={sum(res)} failed={len(res)-sum(res)}")
    out.close()


if __name__ == "__main__":
    main()
