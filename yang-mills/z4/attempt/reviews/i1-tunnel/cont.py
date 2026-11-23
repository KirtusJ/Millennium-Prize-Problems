"""cont.py -- spectrum of the continuum zero-mode matrix model
     h = -1/2 (Lap_{Y1} + Lap_{Y2}) + kappa |Y1 x Y2|^2 ,  Y_i in R^3 (su(2) via U = exp(i Y.sigma)), kappa = 2,
restricted to SO(3)-invariant states (simultaneous rotation), by Rayleigh-Ritz in a harmonic-oscillator basis.
Derivation of kappa (lattice normalization): U_i = exp(i A_i.sigma), V = beta(1 - 1/2 Tr comm) = 2 beta sin^2a1 sin^2a2 sin^2 gamma
~ 2 beta |A1 x A2|^2; -ln K ~ (1/2beta)(-Lap_S3) ~ (1/2beta)(-Lap_A); A = beta^{-1/3} Y gives
-ln T ~ beta^{-1/3} [ -1/2 Lap_Y + 2 |Y1 x Y2|^2 ].
Basis: |k1 k2 L> = R_{k1 L}(r1) R_{k2 L}(r2) sqrt(2L+1) P_L(cos gamma), R_{kL} = 3D HO radial functions (frequency w),
k_i <= K, L <= Lmax. Matrix elements exact: generalized Gauss-Laguerre (alpha=1/2) rule in s = w r^2 with
nq = K + Lmax/2 + 10 nodes (integrands are s^{1/2} e^{-s} times polynomials of degree <= 2K+Lmax+4).
Kinetic: -1/2 Lap = H_ho - 1/2 w^2 r^2, H_ho diagonal w(2k+L+3/2). Potential |Y1xY2|^2 = r1^2 r2^2 (1-t^2).
Sectors: L parity (Y2 -> -Y2), exchange (Y1 <-> Y2).
Usage: python3 cont.py K LMAX W OUTFILE
PREDICATES (fixed before first run):
 P1 (control) kappa=0, the matrix is -1/2 Lap: in the HO basis Rayleigh-Ritz of a free particle is not a check;
    instead control: replace potential by 1/2 w^2 (r1^2+r2^2) -> eigenvalues exactly w(2k1+2k2+2L+3), rel. err < 1e-12.
 P2 Rayleigh-Ritz: eigenvalues decrease monotonically when K or Lmax increases (variational); checked in analyse.
 P3 Convergence: the lowest 4 levels per sector stable to 1e-4 relative between the two largest bases (analyse).
"""
import sys, json, math, time
import numpy as np


def gauss_genlaguerre(n, alpha):
    k = np.arange(n)
    a = 2 * k + alpha + 1
    b = np.sqrt((k[1:]) * (k[1:] + alpha))
    J = np.diag(a) + np.diag(b, 1) + np.diag(b, -1)
    x = np.linalg.eigvalsh(J)
    # Christoffel weights 1/sum_k q_k(x)^2 from the stable orthonormal recurrence (Golub-Welsch V[0]^2 loses
    # relative accuracy for the tiny weights at large nodes), computed in logs-safe form
    Q = np.zeros((n, n)); Q[0] = 1 / math.sqrt(math.gamma(alpha + 1))
    Q[1] = (alpha + 1 - x) * Q[0] / math.sqrt(1 + alpha)
    for j in range(1, n - 1):
        Q[j + 1] = ((2 * j + alpha + 1 - x) * Q[j] - math.sqrt(j * (j + alpha)) * Q[j - 1]) / math.sqrt((j + 1) * (j + 1 + alpha))
    w = 1 / (Q ** 2).sum(0)
    return x, w


def radial(K, L, s):
    """Rt[k, j] = s^{L/2} q_k^{(L+1/2)}(s_j), q orthonormal wrt s^{L+1/2} e^{-s}."""
    al = L + 0.5
    Q = np.zeros((K + 1, len(s)))
    q0 = np.exp(0.5 * L * np.log(s) - 0.5 * math.lgamma(al + 1))
    Q[0] = q0
    if K >= 1:
        Q[1] = (2 * 0 + al + 1 - s) * Q[0] / math.sqrt(1 * (1 + al))
    for k in range(1, K):
        Q[k + 1] = ((2 * k + al + 1 - s) * Q[k] - math.sqrt(k * (k + al)) * Q[k - 1]) / math.sqrt((k + 1) * (k + 1 + al))
    return Q


def build(K, Lmax, w, kappa=2.0, Lpar=0, ex=+1, control=False):
    nq = K + Lmax // 2 + 12
    s, ws = gauss_genlaguerre(nq, 0.5)
    R = [radial(K, L, s) for L in range(Lmax + 1)]
    t, wt = np.polynomial.legendre.leggauss(Lmax + 4); wt = wt / 2
    P = [np.sqrt(2 * L + 1) * np.polynomial.legendre.legval(t, np.eye(Lmax + 1)[L]) for L in range(Lmax + 1)]
    Ls = [L for L in range(Lmax + 1) if L % 2 == Lpar]
    # exchange-symmetrised pair basis per L
    pairs = [(k1, k2) for k1 in range(K + 1) for k2 in range(K + 1) if (k1 < k2 or (k1 == k2 and ex == 1))]

    def symvec(k1, k2):
        v = np.zeros((K + 1, K + 1))
        if k1 == k2:
            v[k1, k2] = 1
        else:
            v[k1, k2] = 1 / math.sqrt(2); v[k2, k1] = ex / math.sqrt(2)
        return v.ravel()
    S = np.array([symvec(*p) for p in pairs]).T     # ((K+1)^2, npairs)
    nb = S.shape[1]
    H = np.zeros((len(Ls) * nb, len(Ls) * nb))
    for i, L in enumerate(Ls):
        for j, Lp in enumerate(Ls):
            if j < i:
                continue
            rho = (R[L] * ws * s / w) @ R[Lp].T              # <kL| r^2 |k'L'>
            if L == Lp:
                ov = (R[L] * ws) @ R[L].T
                diag = w * (2 * np.arange(K + 1) + L + 1.5)
                hho = np.diag(diag)
                I = np.eye(K + 1)
                blk = np.kron(hho, I) + np.kron(I, hho)
                if control:
                    blk = blk  # H_ho itself
                else:
                    blk = blk - 0.5 * w ** 2 * (np.kron(rho, I) + np.kron(I, rho))
            else:
                blk = np.zeros(((K + 1) ** 2,) * 2)
            if not control:
                B = np.sum(wt * P[L] * P[Lp] * (1 - t ** 2))
                if abs(B) > 0:
                    blk = blk + kappa * B * np.kron(rho, rho)
            blk = S.T @ blk @ S
            H[i * nb:(i + 1) * nb, j * nb:(j + 1) * nb] = blk
            H[j * nb:(j + 1) * nb, i * nb:(i + 1) * nb] = blk.T
    return H


if __name__ == '__main__':
    K = int(sys.argv[1]); Lmax = int(sys.argv[2]); w = float(sys.argv[3]); out = sys.argv[4]
    t0 = time.time()
    rec = dict(K=K, Lmax=Lmax, w=w, sectors=[])
    fails = []
    # P1 control
    Hc = build(6, 6, 1.3, control=True, Lpar=0, ex=1)
    ec = np.linalg.eigvalsh(Hc)
    exact = sorted(1.3 * (2 * k1 + 2 * k2 + 2 * L + 3) for L in range(0, 7, 2) for k1 in range(7) for k2 in range(k1, 7))
    rec['P1_maxrel'] = float(np.abs(np.array(sorted(ec)) / np.array(exact) - 1).max())
    if not rec['P1_maxrel'] < 1e-12:
        fails.append('P1')
    for Lpar in (0, 1):
        for ex in (1, -1):
            H = build(K, Lmax, w, Lpar=Lpar, ex=ex)
            e = np.linalg.eigvalsh(H)[:6]
            rec['sectors'].append(dict(Lpar=Lpar, exch=ex, dim=H.shape[0], E=e.tolist()))
            print(Lpar, ex, H.shape[0], ['%.8f' % x for x in e], '%.1fs' % (time.time() - t0), flush=True)
    rec['FAILED'] = fails; rec['seconds'] = time.time() - t0
    with open(out, 'x') as fh:
        json.dump(rec, fh, indent=1)
    sys.exit(1 if fails else 0)
