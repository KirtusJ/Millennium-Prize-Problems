"""e13_bounds.py -- worker q1-E13 (T149). Checks of the ingredients of the proof of (E1), (E3) in E13.md and
evaluation of the explicit error terms Delta1(x,beta), Delta3(x,beta).

NOTATION (E13.md). x = (U1,U2), U_i = (x0_i, u_i). Step U_i' = U_i g_i, g = (g0, xi), g0 = sqrt(1-|xi|^2) on the
upper hemisphere, xi = sin(theta) xhat. w = u1 x u2, S^2 = |u1|^2+|u2|^2, b = sqrt(beta) w, h(S) = 1 + sqrt(1+S^2)/S.
Linear map l: R^6 -> R^3, l(xi) = R1 xi1 x u2 + u1 x R2 xi2, R_i = x0_i I + [u_i]_x.  rho := u1'xu2' - w - l(xi).
Exponents: F1(xi) = -h(S') beta W' - sqrt(b)(Psi(a1')-Psi(a1)) - sqrt(b)(Theta(a2')-Theta(a2)), F3 = same without Theta.
Model: M1(xi) = -h(S) beta |w + l xi|^2 - sqrt(beta)(Psi'(a1) u1hat.xi1 + Theta'(a2) u2hat.xi2), M3 without Theta.
Parameters (as in tube_ratio.py v2 of p1-lower2): eta = 0.25, theta0 = 0.5, ell = 0.08, r0 = 0.15, M = 2, tube
a1 in [0.5, pi-0.5], a2 in [0, r0], support of (G-c1)_+: beta*alpha(S)*q/2 < M^2.

PREDICATES (fixed before the first run).
 P1 identity l l^T = S^2 I - u1u1^T - u2u2^T - 2 w w^T at 2000 random points of SU(2)^2: max abs err <= 1e-12
    (tolerance: double rounding on O(1) entries, ~10 ops).
 P2 l l^T w = (S^2 - 2|w|^2) w and l p is parallel to w, for p = -(Psi' u1hat, Theta' u2hat): residual <= 1e-12 (same).
 P3 closed-form log J (SVD formula of E13.md sec.3) equals the det/solve formula: |diff| <= 1e-9 at 2000 tube points;
    and at valley points (w = 0) log J = |p|^2/2 - log A(S), and (h-2)(1+2 S^2 h) = h: |err| <= 1e-12.
 P4 pointwise Taylor bound: |F1 - M1| <= Err1(x,lambda) and |F3 - M3| <= Err3(x,lambda) for every sample
    (x in tube, xi in the product ball |xi_i| <= lambda = L/sqrt(beta)), 2*10^5 samples, beta in {256,1024,4096,16384},
    L in {2,3}. Tolerance 0 (a proved bound; a failure = defect of my derivation).
 P5 analytic bound of the Gaussian perturbation: -DG3 <= logJ_flat - logJ <= DG1 at all tube grid points (tolerance 1e-12).
 P6 rho(beta) = sqrt(2 pi beta) e^-beta I1(beta) satisfies D <= rho <= 1 (I7 lower bound D) at the betas used.
 P7 the uniform error sup_tube Delta1, sup_tube Delta3 (L optimised over a grid) is decreasing along
    beta = 256 * 4^k, k=0..10, and <= 0.1 at beta = 256*4^10 (= 2.7e8). Expectation (the asymptotics is beta^{-1/2+3/10}
    up to logs, constants unknown before the run).
 Measured only: Delta1(x), Delta3(x) at the 12 child points, beta = 256..16384 (to compare with the child's MC delta).
VERSION 2 (after run1, kept in e13_run1.log / register K2: crash, math domain error in err_terms at beta=256, L=3,
 where the crude bound |S'^2 - S^2| <= 2 sum(sin a_i lam + lam^2) exceeds S^2, i.e. the h-Lipschitz bound is vacuous).
 Fix: Err = inf there; such (x, lambda) do not qualify for P4 and are counted ("vacuous"). Predicates unchanged.
VERSION 3 (after run2, kept: results_run2.txt, register K3): (i) P6 FAILED at beta=2.7e8 and (ii) crash (overflow) in
 deltas at a vacuous lambda. Both my code defects: (i) ive used a fixed grid on [0,pi], too coarse for width 1/sqrt(beta)
 at beta=2.7e8; now the grid is on [0, 40/sqrt(z)] (neglected part < e^-700); same fix in Q_outer ([0, 60/sqrt(beta)]);
 (ii) vacuous lambda skipped. Predicates unchanged.
VERSION 4 (after run3, kept: results_run3.txt, register K5): overflow of exp(e3) when the error bound is > 709
 (large lambda at small beta); my code defect; now log-sum-exp. Predicates unchanged.
Seed 20261123. Output results_<tag>.txt opened with mode "x".
"""
import sys, math
import numpy as np

SEED = 20261123
ETA, TH0, ELL, R0, MM = 0.25, 0.5, 0.08, 0.15, 2.0
ETAP = 0.5
GLx, GLw = np.polynomial.legendre.leggauss(20)


def ive(nu, z, m=200001):
    t = np.linspace(0, min(math.pi, 40 / math.sqrt(z)), m)  # v3: resolve width 1/sqrt(z); rest < e^-700
    f = np.exp(z * (np.cos(t) - 1)) * np.cos(nu * t)
    return float((f.sum() - (f[0] + f[-1]) / 2) * (t[1] - t[0]) / math.pi)


def eps(s): return 2 * np.arcsinh(s)
def alpha(S): return 2 * S * np.sqrt(1 + S * S)
def hfun(S): return 1 + np.sqrt(1 + S * S) / S
def dPsi(a): return np.sqrt(2 * (eps(np.sin(a)) + ETA))
def ddPsi(a): return 2 * np.cos(a) / (np.sqrt(1 + np.sin(a) ** 2) * dPsi(a))
def Theta(a): return TH0 * (np.sqrt(a * a + ELL * ELL) - ELL)
def dTheta(a): return TH0 * a / np.sqrt(a * a + ELL * ELL)


def Psi_diff(a, b):
    mid, half = (a + b) / 2, (b - a) / 2
    t = mid[..., None] + half[..., None] * GLx
    return half * np.sum(GLw * dPsi(t), axis=-1)


def cross_mat(a):
    return np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])


def qmul(p, q):
    a0, a = p[..., 0], p[..., 1:]
    b0, b = q[..., 0], q[..., 1:]
    return np.concatenate([(a0 * b0 - np.sum(a * b, -1))[..., None],
                           a0[..., None] * b + b0[..., None] * a + np.cross(a, b)], -1)


def lmat(U1, U2):
    R1 = U1[0] * np.eye(3) + cross_mat(U1[1:])
    R2 = U2[0] * np.eye(3) + cross_mat(U2[1:])
    return np.hstack([-cross_mat(U2[1:]) @ R1, cross_mat(U1[1:]) @ R2])


def unit(v):
    n = np.linalg.norm(v)
    return v / n if n > 0 else np.zeros(3)


def pvec(U1, U2, with_theta=True):
    a1 = math.acos(U1[0]); a2 = math.acos(U2[0])
    p = np.concatenate([-dPsi(a1) * unit(U1[1:]), -(dTheta(a2) if with_theta else 0.0) * unit(U2[1:])])
    return p


def logJ_det(l, b, p, h):
    Mx = np.eye(6) + 2 * h * l.T @ l
    v = p - 2 * h * l.T @ b
    return -0.5 * np.linalg.slogdet(Mx)[1] + 0.5 * v @ np.linalg.solve(Mx, v) - h * b @ b


def logJ_svd(l, b, p, h):
    Uu, sig, Vt = np.linalg.svd(l)  # l = Uu diag(sig) Vt[:3]
    out = 0.5 * p @ p
    for j in range(3):
        pj = Vt[j] @ p; bj = Uu[:, j] @ b; s = sig[j]
        den = 1 + 2 * h * s * s
        out -= 0.5 * math.log(den) + (pj * pj * h * s * s + 2 * h * s * pj * bj + h * bj * bj) / den
    return out


def point(a1, a2, chi):
    U1 = np.array([math.cos(a1), 0, 0, math.sin(a1)])
    U2 = np.array([math.cos(a2), math.sin(a2) * math.sin(chi), 0, math.sin(a2) * math.cos(chi)])
    return U1, U2


def invariants(U1, U2):
    w = np.cross(U1[1:], U2[1:])
    S = math.sqrt(U1[1:] @ U1[1:] + U2[1:] @ U2[1:])
    return w, S


def HPsi(a1, lp):
    a = np.linspace(a1 - lp, a1 + lp, 201)
    return float(np.max(np.maximum(np.abs(ddPsi(a)), np.abs(dPsi(a) / np.tan(a)))))


def err_terms(U1, U2, beta, lam, with_theta=True):
    w, S = invariants(U1, U2)
    nw = math.sqrt(w @ w)
    h = hfun(S)
    Mm = nw + S * math.sqrt(2) * lam
    Rr = 2 * lam ** 2 * nw + (lam + lam ** 2) ** 2
    EW = beta * (2 * Mm * Rr + Rr ** 2)
    dS2 = 2 * sum(math.sqrt(max(0.0, 1 - U[0] ** 2)) * lam + lam ** 2 for U in (U1, U2))
    sm = S * S - dS2
    if sm <= 0:
        return math.inf  # bound vacuous at this lambda (S' may reach 0); case does not qualify (rule 4)
    dh = dS2 / (2 * sm ** 2 * math.sqrt(1 + 1 / sm))
    BW = beta * (Mm + Rr) ** 2
    lp = math.asin(lam)
    a1 = math.acos(U1[0]); a2 = math.acos(U2[0])
    sb = math.sqrt(beta)
    ePsi = sb * (0.5 * HPsi(a1, lp) * lp ** 2 + dPsi(a1) * (lp - lam))
    eTh = sb * (0.5 * (TH0 / ELL) * lp ** 2 + dTheta(a2) * (lp - lam))
    e = h * EW + dh * BW + ePsi
    return (e + eTh) if with_theta else e


def F_and_M(U1, U2, beta, xi1, xi2, with_theta=True):
    g1 = np.concatenate([np.sqrt(1 - np.sum(xi1 ** 2, -1))[:, None], xi1], -1)
    g2 = np.concatenate([np.sqrt(1 - np.sum(xi2 ** 2, -1))[:, None], xi2], -1)
    V1 = qmul(U1[None], g1); V2 = qmul(U2[None], g2)
    wp = np.cross(V1[:, 1:], V2[:, 1:]); Wp = np.sum(wp ** 2, -1)
    Sp = np.sqrt(np.sum(V1[:, 1:] ** 2, -1) + np.sum(V2[:, 1:] ** 2, -1))
    a1 = math.acos(U1[0]); a2 = math.acos(U2[0])
    a1p = np.arccos(np.clip(V1[:, 0], -1, 1)); a2p = np.arccos(np.clip(V2[:, 0], -1, 1))
    sb = math.sqrt(beta)
    F = -hfun(Sp) * beta * Wp - sb * Psi_diff(np.full_like(a1p, a1), a1p)
    if with_theta: F = F - sb * (Theta(a2p) - Theta(a2))
    w, S = invariants(U1, U2)
    l = lmat(U1, U2)
    m = w[None] + np.concatenate([xi1, xi2], -1) @ l.T
    p = pvec(U1, U2, with_theta)
    Mo = -hfun(S) * beta * np.sum(m ** 2, -1) + sb * np.concatenate([xi1, xi2], -1) @ p
    return F, Mo


def chi3_tail(r):
    if r <= 0: return 1.0
    return math.erfc(r / math.sqrt(2)) + math.sqrt(2 / math.pi) * r * math.exp(-r * r / 2)


def Q_outer(beta, lp, Lam):
    """E[e^{sqrt(b) Lam th} 1{th>lp}] + E[e^{sqrt(b) Lam th}] P(th>lp), th = class angle of g ~ k (exact 1D quadrature)."""
    th = np.linspace(0, min(math.pi, 60 / math.sqrt(beta)), 400001)  # v3: resolve width 1/sqrt(beta)
    dens = (2 / math.pi) * np.sin(th) ** 2 * np.exp(beta * (np.cos(th) - 1)) / (2 * ive(1, beta) / beta)
    dth = th[1] - th[0]
    wgt = dens * dth
    ex = np.exp(math.sqrt(beta) * Lam * th)
    big = th > lp
    return float(np.sum((ex * wgt)[big]) + np.sum(ex * wgt) * np.sum(wgt[big]))


def deltas(U1, U2, beta, rho, Ls, Qcache):
    w, S = invariants(U1, U2)
    h = hfun(S); b = math.sqrt(beta) * w; A = 1 + 2 * S * S * h
    l = lmat(U1, U2)
    a1 = math.acos(U1[0]); a2 = math.acos(U2[0])
    best1, best3 = np.inf, np.inf
    p1 = pvec(U1, U2, True); p3 = pvec(U1, U2, False)
    lJ1 = logJ_det(l, b, p1, h); lJ3 = logJ_det(l, b, p3, h)
    base = (h - 2) * (b @ b)
    gap1 = (-eps(S) + p1 @ p1 / 2) - (base + lJ1)   # flat - actual (E1)
    gap3 = (base + lJ3) - (-eps(S) + p3 @ p3 / 2)   # actual - flat (E3)
    Lam = math.sqrt(2 * (eps(1.0) + ETA))
    for L in Ls:
        lam = L / math.sqrt(beta)
        if lam > 0.5: continue
        e1 = err_terms(U1, U2, beta, lam, True); e3 = err_terms(U1, U2, beta, lam, False)
        if not (math.isfinite(e1) and math.isfinite(e3)): continue  # v3: vacuous lambda
        tail = math.exp(p1 @ p1 / 2 - lJ1) * (chi3_tail(L - abs(dPsi(a1))) + chi3_tail(L - dTheta(a2)))
        if tail < 1:
            d1 = gap1 + e1 + L ** 4 / beta + 2 * math.log(rho) - math.log(1 - tail)
            best1 = min(best1, d1)
        key = (beta, L)
        if key not in Qcache: Qcache[key] = Q_outer(beta, math.asin(lam), Lam)
        out = math.exp(base + eps(S) - dPsi(a1) ** 2 / 2) * Qcache[key]
        lo = math.log(out) if out > 0 else -np.inf
        d3 = float(np.logaddexp(e3 + gap3 - math.log(rho ** 2 * (1 - lam ** 2)), lo))  # v4: log-sum-exp
        best3 = min(best3, d3)
    return best1, best3, gap1, gap3


def main(tag):
    out = open(f"results_{tag}.txt", "x")
    def P(*a):
        s = " ".join(str(x) for x in a); print(s); out.write(s + "\n"); out.flush()
    rng = np.random.default_rng(SEED)
    res = {k: [] for k in ["P1", "P2", "P3", "P4", "P5", "P6", "P7"]}
    # P1, P2 at random points of SU(2)^2
    e1m = e2m = 0.0
    for _ in range(2000):
        U1 = rng.normal(size=4); U1 /= np.linalg.norm(U1); U2 = rng.normal(size=4); U2 /= np.linalg.norm(U2)
        u1, u2 = U1[1:], U2[1:]; w = np.cross(u1, u2); S2 = u1 @ u1 + u2 @ u2
        l = lmat(U1, U2)
        e1m = max(e1m, np.max(np.abs(l @ l.T - (S2 * np.eye(3) - np.outer(u1, u1) - np.outer(u2, u2) - 2 * np.outer(w, w)))))
        a1 = math.acos(U1[0]); a2 = math.acos(U2[0])
        p = np.concatenate([-1.3 * unit(u1), -0.7 * unit(u2)])
        r1 = l @ l.T @ w - (S2 - 2 * w @ w) * w
        lp_ = l @ p; r2 = np.linalg.norm(lp_ - (lp_ @ unit(w)) * unit(w))
        e2m = max(e2m, np.max(np.abs(r1)), r2)
    res["P1"].append(e1m <= 1e-12); res["P2"].append(e2m <= 1e-12)
    P(f"P1 max|l l^T - formula| = {e1m:.2e} {'MET' if e1m <= 1e-12 else 'FAILED'}")
    P(f"P2 max residual (eigvec w, l p || w) = {e2m:.2e} {'MET' if e2m <= 1e-12 else 'FAILED'}")
    # tube sample generator
    def tube_point(beta):
        while True:
            a1 = rng.uniform(ETAP, math.pi - ETAP); a2 = rng.uniform(0, R0); chi = rng.uniform(0, math.pi)
            U1, U2 = point(a1, a2, chi)
            w, S = invariants(U1, U2)
            if beta * alpha(S) * (w @ w) / S ** 2 / 2 < MM * MM: return U1, U2
    # P3
    e3m = 0.0; ev = 0.0
    for _ in range(2000):
        beta = float(rng.choice([256, 1024, 4096, 16384]))
        U1, U2 = tube_point(beta)
        w, S = invariants(U1, U2); b = math.sqrt(beta) * w; h = hfun(S); l = lmat(U1, U2); p = pvec(U1, U2)
        e3m = max(e3m, abs(logJ_det(l, b, p, h) - logJ_svd(l, b, p, h)))
        U1v, U2v = point(math.acos(U1[0]), math.acos(U2[0]), 0.0)
        w, S = invariants(U1v, U2v); h = hfun(S); l = lmat(U1v, U2v); p = pvec(U1v, U2v)
        ev = max(ev, abs(logJ_det(l, np.zeros(3), p, h) - (p @ p / 2 - math.log(1 + 2 * S * S * h))),
                 abs((h - 2) * (1 + 2 * S * S * h) - h), abs(math.log(1 + 2 * S * S * h) - eps(S)))
    ok = e3m <= 1e-9 and ev <= 1e-12; res["P3"].append(ok)
    P(f"P3 max|svd-det| = {e3m:.2e}, valley/identity max err = {ev:.2e} {'MET' if ok else 'FAILED'}")
    # P4
    for beta in [256, 1024, 4096, 16384]:
        for L in [2.0, 3.0]:
            lam = L / math.sqrt(beta)
            nfail = [0, 0]; worst = [0.0, 0.0]; ntot = 0; nvac = [0, 0]
            for _ in range(200):
                U1, U2 = tube_point(beta)
                n = 1000
                def ball(n):
                    v = rng.normal(size=(n, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
                    r = lam * rng.random(n) ** (1 / 3)
                    r[: n // 10] = lam  # include boundary of the ball
                    return v * r[:, None]
                xi1, xi2 = ball(n), ball(n)
                for k, wt in enumerate([True, False]):
                    F, Mo = F_and_M(U1, U2, beta, xi1, xi2, wt)
                    E = err_terms(U1, U2, beta, lam, wt)
                    if not math.isfinite(E):
                        nvac[k] += 1; continue
                    r = np.max(np.abs(F - Mo)) / E
                    worst[k] = max(worst[k], r); nfail[k] += int(np.sum(np.abs(F - Mo) > E))
                ntot += n
            ok = nfail[0] == 0 and nfail[1] == 0; res["P4"].append(ok)
            P(f"P4 beta={beta} L={L} points={200} vacuous(E1,E3)={nvac} samples={ntot} fails(E1,E3)={nfail} max|F-M|/Err = {worst[0]:.3f}, {worst[1]:.3f} "
              f"{'MET' if ok else 'FAILED'}")
    # P6 rho
    rhos = {}
    for k in range(11):
        beta = 256 * 4 ** k
        rho = math.sqrt(2 * math.pi * beta) * ive(1, beta)
        D = 1 - 1 / (2 * beta) - math.sqrt(2 * math.pi * beta) * math.exp(-beta) / 2
        ok = D <= rho <= 1; res["P6"].append(ok); rhos[beta] = rho
        P(f"P6 beta={beta} rho={rho:.8f} D={D:.8f} {'MET' if ok else 'FAILED'}")
    # P5 and P7 on a tube grid
    Ls = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0]
    Qc = {}
    prev = (np.inf, np.inf)
    for k in range(11):
        beta = 256 * 4 ** k
        sup1 = sup3 = -np.inf; p5 = True
        for a1 in np.linspace(ETAP, math.pi - ETAP, 7):
            for a2 in [0.0, 0.02, 0.06, 0.1, R0]:
                for frac in [0.0, 0.5, 0.99]:
                    # chi chosen so that beta alpha q/2 = frac * M^2
                    S = math.sqrt(math.sin(a1) ** 2 + math.sin(a2) ** 2)
                    wmax = math.sqrt(frac * MM * MM * 2 * S * S / (beta * alpha(S)))
                    den = math.sin(a1) * math.sin(a2)
                    if den == 0:
                        if frac > 0: continue
                        chi = 0.0
                    else:
                        if wmax > den: continue
                        chi = math.asin(wmax / den)
                    U1, U2 = point(a1, a2, chi)
                    d1, d3, g1, g3 = deltas(U1, U2, beta, rhos[beta], Ls, Qc)
                    w, S = invariants(U1, U2); b2 = beta * (w @ w); h = hfun(S); nw2 = w @ w
                    sw = math.sqrt(S * S - 2 * nw2)
                    kap = abs(dPsi(a1) * U1[0] / math.sin(a1) + (dTheta(a2) * U2[0] / math.sin(a2) if a2 > 0 else 0))
                    kap3 = abs(dPsi(a1) * U1[0] / math.sin(a1))
                    DG1 = 2 * h * b2 / (beta * S * S) + kap ** 2 * b2 / (2 * beta * sw * sw) + kap * b2 / (math.sqrt(beta) * sw) + 4 * h * h * b2 * b2 / beta
                    DG3 = h * (2 + 2 / (S * S)) * b2 / beta + kap3 * b2 / (math.sqrt(beta) * sw)
                    p5 = p5 and (g1 <= DG1 + 1e-12) and (g3 <= DG3 + 1e-12)
                    sup1 = max(sup1, d1); sup3 = max(sup3, d3)
        res["P5"].append(p5)
        ok7 = sup1 <= prev[0] and sup3 <= prev[1]
        res["P7"].append(ok7); prev = (sup1, sup3)
        P(f"P7 beta={beta} sup_tube Delta1={sup1:.4f} sup_tube Delta3={sup3:.4f} (monotone {'MET' if ok7 else 'FAILED'}) P5 {'MET' if p5 else 'FAILED'}")
    ok = prev[0] <= 0.1 and prev[1] <= 0.1; res["P7"].append(ok)
    P(f"P7 final sup Delta at beta=2.7e8: {prev[0]:.4f}, {prev[1]:.4f} <= 0.1 {'MET' if ok else 'FAILED'}")
    # measured only: child points
    for beta in [256, 1024, 4096, 16384]:
        for a1 in [0.5, math.pi / 2, 2.6]:
            for c in [0.0, 0.07]:
                for y in [0.0, 1.5]:
                    d = y / (math.sqrt(beta) * math.sin(a1)); r = math.hypot(c, d)
                    U1 = np.array([math.cos(a1), 0, 0, math.sin(a1)])
                    U2 = np.array([1.0, 0, 0, 0]) if r == 0 else np.array([math.cos(r), math.sin(r) * d / r, 0, math.sin(r) * c / r])
                    d1, d3, g1, g3 = deltas(U1, U2, beta, rhos.get(beta, math.sqrt(2 * math.pi * beta) * ive(1, beta)), Ls, Qc)
                    P(f"CHILDPT beta={beta} a1={a1:.4f} c={c} y={y} Delta1={d1:.4f} Delta3={d3:.4f} gauss_gap1={g1:.2e} gap3={g3:.2e} (measured only)")
    for k, v in res.items():
        P(f"SUMMARY {k}: met {sum(v)}, failed {len(v) - sum(v)} of {len(v)}")
    out.close()
    return 0 if all(all(v) for v in res.values()) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
