"""hess.py -- f1-strong (T63). Exact Hessian of the SU(2) Wilson action and its lower bound.

Conventions: V = -(beta/2) sum_p Re Tr Q_p, Q_p = U1 U2 U3^-1 U4^-1, <X,Y> = -Tr(XY),
e_a = i sigma_a/sqrt2, variation U_e -> exp(s t_e) U_e. beta = 1 throughout (Hess V linear in beta).
Formula under test (derived in STRONG_COUPLING.md):
  d^2/ds^2 V_p = -(1/2) Re Tr[(sum_i X_i^2 + 2 sum_{i<j} X_i X_j) Q],
  X1=t1, X2=Ad(U1)t2, X3=-Ad(U1U2U3^-1)t3, X4=-Ad(U1U2U3^-1U4^-1)t4.
Per-plaquette claim: max over (X_i) of -Hess_p/(1/2) / sum|X_i|^2 = h(th) = 2s(1+s), s = sin(th/2),
  Re Tr Q = 2 cos th.  Consequence: Hess V >= -(1/2) max_e sum_{p ni e} h(th_p) |t|^2 >= -12 |t|^2.

PREDICATES (fixed before first run):
 P1 FD: analytic Hess(t,t) agrees with central 2nd difference of V along exp(s t) U, h=1e-3,
    |diff| <= 1e-5 * max(1,|Hess|)  [tolerance: FD truncation O(h^2 * |V''''|) ~ 1e-6*24 plus
    roundoff 1e-16*|V|/h^2 ~ 1e-8] on 5 random configs x 3 random directions (L=2).
 P2 per-plaquette: lambda_max of the 12x12 form -2*Hess_p equals h(th) within 1e-9 (eigensolver
    roundoff) for 200 random plaquettes (Haar-random links, seed 2).
 P3 pi-flux (all Q_p = -1): lambda_min(Hess V) = -8 within 1e-9, and min over horizontal t = -8,
    on L=2 and L=4.
 P4 for all tested configs (30 random Haar, the one-link flip, pi-flux; L=2):
    -lambda_min <= local bound b(U) = (1/2) max_e sum_{p ni e} h(th_p) + 1e-9 <= 12.
 P5 hill-climb over U on L=2 from 6 seeds, 300 accepted-or-rejected steps each, (plus pi-flux start): best -lambda_min <= 12 + 1e-9.
    Value: measured only.
 M1 (measured only): horizontal min at the one-link-flip configuration on L=2 and L=3.
"""
import numpy as np, sys, itertools, time

I2 = np.eye(2, dtype=complex)
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
E = [1j * s / np.sqrt(2) for s in sig]


def expm_su2(X):
    # X in su(2): X = i a.sigma ; exp = cos|a| + i sin|a| a.sigma/|a|
    a = np.array([np.imag(X[0, 1]), np.real(X[0, 1]), np.imag(X[0, 0])])
    a = np.array([(X[0, 1] + X[1, 0]).imag / 2, (X[0, 1] - X[1, 0]).real / 2, X[0, 0].imag])
    n = np.linalg.norm(a)
    if n < 1e-300:
        return I2.copy()
    return np.cos(n) * I2 + np.sin(n) / n * X


def vec2alg(x):
    return sum(x[a] * E[a] for a in range(3))


def haar(rng):
    q = rng.normal(size=4); q /= np.linalg.norm(q)
    return np.array([[q[0] + 1j * q[3], q[2] + 1j * q[1]], [-q[2] + 1j * q[1], q[0] - 1j * q[3]]])


class Lattice:
    def __init__(s, L, d=4):
        s.L, s.d = L, d
        s.sites = list(itertools.product(range(L), repeat=d))
        s.sidx = {x: i for i, x in enumerate(s.sites)}
        s.nl = len(s.sites) * d
        s.plaq = []
        for x in s.sites:
            for mu in range(d):
                for nu in range(mu + 1, d):
                    xm = s.sh(x, mu); xn = s.sh(x, nu)
                    s.plaq.append((s.link(x, mu), s.link(xm, nu), s.link(xn, mu), s.link(x, nu)))

    def sh(s, x, mu):
        y = list(x); y[mu] = (y[mu] + 1) % s.L; return tuple(y)

    def link(s, x, mu):
        return s.sidx[x] * s.d + mu


def V(lat, U):
    return -0.5 * sum(np.real(np.trace(U[a] @ U[b] @ U[c].conj().T @ U[e].conj().T)) for a, b, c, e in lat.plaq)


def plaq_block(Ul):
    """12x12 matrix B with Hess_p(t,t) = x^T B x, x = coords of (t1..t4) (beta=1)."""
    U1, U2, U3, U4 = Ul
    Q = U1 @ U2 @ U3.conj().T @ U4.conj().T
    G = [I2, U1, -(U1 @ U2 @ U3.conj().T), -(Q)]
    # X_i = G_i t_i G_i^-1 up to sign; sign of G irrelevant for Ad, so store sign separately
    sgn = [1, 1, -1, -1]
    Gs = [I2, U1, U1 @ U2 @ U3.conj().T, Q]
    F = np.array([sgn[i] * Gs[i] @ E[a] @ Gs[i].conj().T for i in range(4) for a in range(3)])
    # T[k,l] = Re Tr(F_k F_l Q)
    T = np.real(np.einsum('kij,ljm,mi->kl', F, F, Q))
    B = np.zeros((12, 12))
    for k in range(12):
        for l in range(12):
            i, j = k // 3, l // 3
            if i == j:
                B[k, l] = -0.25 * (T[k, l] + T[l, k])
            elif i < j:
                B[k, l] = B[l, k] = -0.5 * T[k, l]
    return B, Q


def hessian(lat, U):
    H = np.zeros((3 * lat.nl, 3 * lat.nl)); ths = []
    for p in lat.plaq:
        B, Q = plaq_block([U[k] for k in p])
        idx = np.concatenate([np.arange(3 * k, 3 * k + 3) for k in p])
        H[np.ix_(idx, idx)] += B  # repeated links (L=2 never repeats within a plaquette) add correctly
        ths.append(np.arccos(np.clip(np.real(np.trace(Q)) / 2, -1, 1)))
    return H, np.array(ths)


def hfun(th):
    s = np.sin(th / 2); return 2 * s * (1 + s)


def local_bound(lat, ths):
    acc = np.zeros(lat.nl)
    for p, th in zip(lat.plaq, ths):
        for k in p:
            acc[k] += hfun(th)
    return 0.5 * acc.max()


def gauge_basis(lat, U):
    Gm = np.zeros((3 * lat.nl, 3 * len(lat.sites)))
    for x in lat.sites:
        for mu in range(lat.d):
            e = lat.link(x, mu); y = lat.sh(x, mu)
            for a in range(3):
                # t_e = w_x - Ad(U_e) w_y
                Gm[3 * e:3 * e + 3, 3 * lat.sidx[x] + a] += np.eye(3)[a]
                Y = U[e] @ E[a] @ U[e].conj().T
                Gm[3 * e:3 * e + 3, 3 * lat.sidx[y] + a] -= np.array([-np.trace(Y @ E[b]).real for b in range(3)])
    u, sv, vt = np.linalg.svd(Gm, full_matrices=True)
    r = (sv > 1e-9).sum()
    return u[:, r:]  # horizontal basis


def lam(lat, U, horiz=False):
    H, ths = hessian(lat, U)
    if horiz:
        Pb = gauge_basis(lat, U); H = Pb.T @ H @ Pb
    return np.linalg.eigvalsh(H)[0], ths


def piflux(lat):
    U = []
    for x in lat.sites:
        for mu in range(lat.d):
            U.append(((-1) ** sum(x[:mu])) * I2)
    return U


def main(out):
    f = open(out, "x")
    def w(*a):
        print(*a); print(*a, file=f); f.flush()
    res = {}
    L2 = Lattice(2)
    # P1
    rng = np.random.default_rng(1); worst = 0
    for c in range(5):
        U = [haar(rng) for _ in range(L2.nl)]
        H, _ = hessian(L2, U)
        for r in range(3):
            x = rng.normal(size=3 * L2.nl)
            h = 1e-3
            def Vs(s):
                return V(L2, [expm_su2(s * vec2alg(x[3 * e:3 * e + 3])) @ U[e] for e in range(L2.nl)])
            fd = (Vs(h) - 2 * Vs(0) + Vs(-h)) / h ** 2
            an = x @ H @ x
            worst = max(worst, abs(fd - an) / max(1, abs(an)))
    res['P1'] = worst <= 1e-5; w("P1 FD worst rel diff", worst, "MET" if res['P1'] else "FAILED")
    # P2
    rng = np.random.default_rng(2); worst = 0; worst_ratio = 0
    for c in range(200):
        Ul = [haar(rng) for _ in range(4)]
        B, Q = plaq_block(Ul)
        th = np.arccos(np.clip(np.real(np.trace(Q)) / 2, -1, 1))
        lm = np.linalg.eigvalsh(-2 * B)[-1]
        worst = max(worst, abs(lm - hfun(th)))
    res['P2'] = worst <= 1e-9; w("P2 per-plaquette max |lambda_max - h(th)|", worst, "MET" if res['P2'] else "FAILED")
    # P3
    ok = True
    for L in (2, 4):
        lat = L2 if L == 2 else Lattice(4)
        U = piflux(lat)
        l0, ths = lam(lat, U); lh = lam(lat, U, True)[0] if L == 2 else None
        w(f"P3 L={L} pi-flux: all Q=-1: {np.allclose(ths, np.pi)}; lambda_min={l0:.12f}; horizontal={lh}")
        ok &= abs(l0 + 8) < 1e-9 and np.allclose(ths, np.pi) and (lh is None or abs(lh + 8) < 1e-9)
    res['P3'] = ok; w("P3", "MET" if ok else "FAILED")
    # P4
    rng = np.random.default_rng(4); cases = []
    for c in range(30):
        cases.append(("haar%d" % c, [haar(rng) for _ in range(L2.nl)]))
    U = [I2.copy() for _ in range(L2.nl)]; U[0] = -I2; cases.append(("oneflip", U))
    cases.append(("piflux", piflux(L2)))
    nok = 0
    for name, U in cases:
        l0, ths = lam(L2, U); b = local_bound(L2, ths)
        good = -l0 <= b + 1e-9 and b <= 12 + 1e-9; nok += good
        if name in ("oneflip", "piflux", "haar0"):
            w(f"P4 {name}: -lambda_min={-l0:.6f} local bound={b:.6f}")
    res['P4'] = nok == len(cases); w(f"P4 qualifying cases {len(cases)}/{len(cases)} (all configs qualify); met {nok}/{len(cases)}", "MET" if res['P4'] else "FAILED")
    allneg = [-lam(L2, U)[0] for _, U in cases[:30]]
    w("measured: Haar samples -lambda_min max %.4f mean %.4f" % (max(allneg), np.mean(allneg)))
    # M1
    for L in (2, 3):
        lat = L2 if L == 2 else Lattice(3)
        U = [I2.copy() for _ in range(lat.nl)]; U[0] = -I2
        l0, _ = lam(lat, U); lh, _ = lam(lat, U, True)
        w(f"M1 L={L} one-link flip: -lambda_min={-l0:.6f}, horizontal -min={-lh:.6f} (measured only)")
    # P5 hill climb
    t0 = time.time(); best = 0; bestname = None
    starts = [("piflux", piflux(L2))]
    for sd in range(6):
        r = np.random.default_rng(100 + sd); starts.append(("haar_seed%d" % (100 + sd), [haar(r) for _ in range(L2.nl)]))
    for name, U in starts:
        r = np.random.default_rng(7); U = [u.copy() for u in U]
        cur = -lam(L2, U)[0]; step = 0.3
        for it in range(300):
            e = r.integers(L2.nl); old = U[e]
            U[e] = expm_su2(vec2alg(step * r.normal(size=3))) @ old
            v = -lam(L2, U)[0]
            if v > cur: cur = v
            else: U[e] = old
        w(f"P5 start {name}: best -lambda_min after 300 steps = {cur:.6f}")
        if cur > best: best, bestname = cur, name
    res['P5'] = best <= 12 + 1e-9
    w(f"P5 overall best {best:.6f} from {bestname}", "MET" if res['P5'] else "FAILED", f"time {time.time()-t0:.0f}s")
    met = sum(res.values()); w(f"COUNTS met {met}, failed {len(res)-met}, measured only 2 (M1, Haar stats)")
    return 0 if met == len(res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
