"""sharp_chess2d.py -- worker a3-B, test (iii), part 2: the first CLAIMED step S3a, in two dimensions, exactly.

S3a (as used in PROOF.md, d-dimensional form): on an even periodic torus, for the Wilson SU(2) action
beta * sum_p cos(alpha_p), with O_p := beta (1 - cos alpha_p) and f_L(beta) := log Z_L(beta)/|Lambda| - (#plaq/site) beta,
    P_L( O_p > t ) <= exp( f_L(beta/2) - f_L(beta) - t * r_d / 2 ),
where r_d = (#distinct chessboard images of p)/|Lambda| = 1 in d = 2 (1/4 in d = 4).
(Proof: chessboard estimate; on the event that all images are bad, e^{-beta S} <= e^{-(beta/2) S} e^{-t r_d |Lambda|/2}.)
In d = 2 everything is exact by characters (N = L^2 plaquettes, j = 0..J):
    ahat_j(beta) = (2/pi) int_0^pi e^{beta(cos a - 1)} sin((j+1)a) sin(a)/(j+1) da,  Z_L e^{-beta N} = sum_j ahat_j^N,
    P_L(O_p > t) = sum_j ahat_j^(N-1) ahat'_j / sum_j ahat_j^N, ahat'_j: same integral over beta(1-cos a) > t.
Infinite volume (free b.c.): plaquettes i.i.d., P_inf = ahat'_0/ahat_0, f_inf = log ahat_0.

PREDICATES (fixed before the first run):
 Q1  normalisation: with t = -1 (whole group) P_L = 1 within 1e-9 for L in {2,4,6,8} and beta in grid
     (tolerance: double rounding over <= 300 terms; quadrature errors cancel in the ratio).
 Q2  for all L in {2,4,6,8,inf}, beta in {1,2,4,8,16,32,64,128}, t in {0.5,1,2,4,8,16}:
     P_L(O_p > t) <= bound * (1 + 1e-6)   (slack: quadrature error of a 400001-point Simpson rule, << 1e-6).
     Cases "qualify" as informative when bound < 1; reported separately.
 Q3  truncation: ahat_J/ahat_0 < 1e-30 at J = 300 for beta = 128 (largest beta), so omitted terms are negligible.
 Measured only: Delta(beta) = f(beta/2) - f(beta) for L = 8 and inf, compared with (3/2) log 2 = 1.0397
     (Gaussian count: 3 physical degrees of freedom per site in d = 2); -log P_inf(O>t) vs t/2.
Output: argv[1], mode "x". Deterministic.
"""
import sys, math
import numpy as np

A = np.linspace(0.0, math.pi, 400001)
W = np.ones_like(A); W[1:-1:2] = 4; W[2:-1:2] = 2; W *= (A[1] - A[0]) / 3  # Simpson
J = 300


def ahat(beta, t):
    base = np.exp(beta * (np.cos(A) - 1)) * np.sin(A) * (2 / math.pi)
    if t is not None:
        base = base * (beta * (1 - np.cos(A)) > t)
    js = np.arange(J + 1)
    # sin((j+1)a) for all j: matrix (J+1) x len(A) is big; loop in chunks
    out = np.empty(J + 1)
    for j in js:
        out[j] = np.dot(W, base * np.sin((j + 1) * A)) / (j + 1)
    return out


def logsumexp_pow(a, ap, N):
    # returns log sum_j a_j^(N-1) ap_j  and log sum_j a_j^N, handling signs (a_j > 0 here; ap_j may be any sign)
    la = np.log(np.abs(a))
    num = np.sum(np.sign(a) ** (N - 1) * ap * np.exp((N - 1) * la - (N - 1) * la[0]))
    den = np.sum(np.sign(a) ** N * np.exp(N * la - N * la[0]))
    return num, den, la[0]


def main():
    out = open(sys.argv[1], "x")
    w = lambda s: (out.write(s + "\n"), print(s))
    betas = [1, 2, 4, 8, 16, 32, 64, 128]
    ts = [0.5, 1, 2, 4, 8, 16]
    Ls = [2, 4, 6, 8]
    cache = {}
    for b in betas + [0.5]:
        cache[(b, None)] = ahat(b, None)
    q1 = True; q2_total = 0; q2_ok = 0; q2_inf = 0; fails = []
    q3 = abs(cache[(128, None)][J] / cache[(128, None)][0]) < 1e-30

    def f(b, L):
        a = cache[(b, None)]
        if L is None:
            return math.log(a[0])
        N = L * L
        _, den, l0 = logsumexp_pow(a, a, N)
        return (N * l0 + math.log(den)) / N

    for b in betas:
        a = cache[(b, None)]
        aw = ahat(b, -1)  # indicator always true: must reproduce P = 1
        for L in Ls:
            num, den, _ = logsumexp_pow(a, aw, L * L)
            if abs(num / den - 1) > 1e-9:
                q1 = False
        for t in ts:
            ap = ahat(b, t)
            for L in Ls + [None]:
                if L is None:
                    P = ap[0] / a[0]
                else:
                    num, den, _ = logsumexp_pow(a, ap, L * L)
                    P = num / den
                lb = f(b / 2, L) - f(b, L) - t / 2
                bound = math.exp(lb)
                ok = P <= bound * (1 + 1e-6)
                q2_total += 1; q2_ok += ok; q2_inf += bound < 1
                if not ok:
                    fails.append((b, t, L, P, bound))
                w(f"beta={b} t={t} L={'inf' if L is None else L} P={P:.6e} bound={bound:.6e} log(bound/P)={lb - math.log(P) if P > 0 else float('inf'):.4f}")
    w("measured: Delta(beta)=f(beta/2)-f(beta), (3/2)log2=%.4f" % (1.5 * math.log(2)))
    for b in betas:
        w(f"beta={b} Delta_L8={f(b/2, 8) - f(b, 8):.5f} Delta_inf={f(b/2, None) - f(b, None):.5f}")
    w(f"Q1 normalisation: {'MET' if q1 else 'FAILED'}")
    w(f"Q2: {q2_ok}/{q2_total} cases satisfy the bound; informative (bound<1) cases: {q2_inf}; {'MET' if q2_ok == q2_total else 'FAILED'}")
    for fl in fails:
        w(f"  Q2 failure: {fl}")
    w(f"Q3 truncation: {'MET' if q3 else 'FAILED'}")
    met = q1 + (q2_ok == q2_total) + q3
    w(f"counts: met {met}, failed {3 - met}, measured only 2")
    out.close()
    sys.exit(0 if met == 3 else 1)


if __name__ == "__main__":
    main()
