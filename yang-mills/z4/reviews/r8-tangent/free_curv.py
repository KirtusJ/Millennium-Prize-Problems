"""free_curv.py -- known-answer test of Director C4's tangent law against the free
four-dimensional lattice gauge field (one colour; colours are independent copies).

Conventions. theta_{mn}(x) = A_m(x)+A_n(x+e_m)-A_m(x+e_n)-A_n(x) = (grad_m A_n - grad_n A_m)(x);
Fourier multiplier of grad_m is p_m = exp(i k_m)-1. Action (1/2) sum theta^2 (g=1, which is
C4's normalisation: F = sqrt(beta) Im U, weight exp(-|F|^2/2) to leading order). The curvature
covariance is P(k) = D D^dagger/|p|^2, D[(mn),l] = p_m d_{nl} - p_n d_{ml} (projection onto
exact 2-forms, k != 0). cov(theta_a(x), theta_b(y)) = int dk/(2pi)^4 P_ab(k) e^{ik(x-y)}.

PREDICATES (fixed before first run; tolerances and their source):
 P0 control: 4D lattice Green G(0)=int 1/|p|^2 = 0.15493339 within 2e-3.
    Tol: midpoint rule on M^4 grid with an integrable 1/k^2 singularity, error O(M^-2) ~ 1e-3 at M=48.
 P1 rank/idempotence: for 2000 random k (seed 1), max|P^2-P| < 1e-12, trace P = 3. Tol: float64 roundoff.
 P2 exact torus: on the periodic L^4 torus (k=0 excluded), <theta_12^2> = (1-L^-4)/2 for L=4,8,16,
    within 1e-12 (roundoff on <=65536 terms). Derivation: sum_m |p_m|^2/|p|^2 = 1 per k, permutation
    symmetry of the k-set gives 1/4 per direction, so 1/2 per face times (L^4-1)/L^4.
 P3 equipartition hypothesis: infinite volume <theta_12^2> = 2/d = 1/2 within 2e-4.
    Tol: bounded integrand with a point discontinuity at k=0, midpoint error O(M^-4)*const; and
    |value(M=48)-value(M=32)| must be < 2e-4 (measured convergence).
 P4 C4's C1(1) = 0.06887475 = cov(theta_12(0),theta_12(e_4)) within 2e-4 (same tol as P3).
 P5 single-edge test (gaussian.md): Var sum_p eps_pe theta_p over the 6 faces at an edge = 6 within 1e-3
    (off-diagonal phases enter; tol = 6 x P3 tol rounded up).
 P6 reflection sign (reflection.md odd test; for the free field RP requires it):
    "for all" ordered (i,j), i normal to the site plane, n=0..4: cov(theta_ij at n e_i, theta_ij at
    (-n-1)e_i) <= +2e-4. Counted per case (rule 4).
 P7 dipole consistency: C4's C(0)=int k3hat^2 (k1hat^2+k2hat^2)/|p|^2 equals 2(<th12^2>-<th12(0)th12(e3)>)
    within 2e-4.
 P8 plaquette action: Y=|F|^2/2, F~N(0,I3/2): E Y=3/4, Var Y=3/8, and C4's moment formula
    2^-k Gamma(k+3/2)/Gamma(3/2) equals E[(chi2_3/4)^k] for k=0..6 (exact, rel tol 1e-12); Monte Carlo
    of E Y, Var Y (seed 7, 10^6 samples) within 5 sigma.
Measured only: adjacent coplanar cov(th12(0),th12(e1)), perpendicular cov(th12(0),th13(0)),
parallel cov(th12(0),th12(e3)), cov at 3e3; and the same on L=16 torus.
Exit code 0 iff all predicates hold, 1 otherwise. Results written to results/free_curv_<tag>.txt,
refusing to overwrite.
"""
import itertools, math, os, sys
import numpy as np

ORI = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
OI = {o: i for i, o in enumerate(ORI)}


def ori(i, j):
    return OI[(min(i, j), max(i, j))], (1 if i < j else -1)


def accumulate(k4list, targets):
    """k4list: iterable of arrays (n,4) of momenta (equal weights). targets: list of (a,b,r).
    Returns mean over all k of P_ab(k) e^{ik.r} (real part)."""
    acc = np.zeros(len(targets)); cnt = 0
    for K in k4list:
        p = np.exp(1j * K) - 1.0
        p2 = (np.abs(p) ** 2).sum(1)
        D = np.zeros((K.shape[0], 6, 4), complex)
        for a, (m, n) in enumerate(ORI):
            D[:, a, n] += p[:, m]; D[:, a, m] -= p[:, n]
        for t, (a, b, r) in enumerate(targets):
            Pab = (D[:, a, :] * np.conj(D[:, b, :])).sum(1) / p2
            acc[t] += np.real(Pab * np.exp(1j * (K @ np.asarray(r, float)))).sum()
        cnt += K.shape[0]
    return acc / cnt


def midpoint_slices(M):
    g = -np.pi + (np.arange(M) + 0.5) * 2 * np.pi / M
    a, b, c = np.meshgrid(g, g, g, indexing="ij")
    base = np.stack([a.ravel(), b.ravel(), c.ravel()], 1)
    for k4 in g:
        yield np.column_stack([base, np.full(base.shape[0], k4)])


def torus_slices(L):
    g = 2 * np.pi * np.arange(L) / L
    a, b, c = np.meshgrid(g, g, g, indexing="ij")
    base = np.stack([a.ravel(), b.ravel(), c.ravel()], 1)
    for k4 in g:
        K = np.column_stack([base, np.full(base.shape[0], k4)])
        if k4 == 0:
            K = K[1:]  # drop k = 0 (first row)
        yield K


def main():
    tag = sys.argv[1] if len(sys.argv) > 1 else "run1"
    out = f"results/free_curv_{tag}.txt"
    if os.path.exists(out):
        print("refusing to overwrite", out); sys.exit(2)
    os.makedirs("results", exist_ok=True)
    lines = []; ok = {}
    log = lambda s: (print(s), lines.append(s))
    e = np.eye(4, dtype=int)
    a12, a13 = OI[(0, 1)], OI[(0, 2)]

    # P0 control
    M0 = 48
    G = 0.0
    for K in midpoint_slices(M0):
        G += (1.0 / (4 - 2 * np.cos(K).sum(1))).sum()
    G /= M0 ** 4
    ok["P0"] = abs(G - 0.15493339) < 2e-3
    log(f"P0 G(0) M={M0}: {G:.8f} (known 0.15493339) -> {ok['P0']}")

    # P1
    rng = np.random.default_rng(1)
    K = rng.uniform(-np.pi, np.pi, (2000, 4))
    p = np.exp(1j * K) - 1; p2 = (abs(p) ** 2).sum(1)
    D = np.zeros((2000, 6, 4), complex)
    for a, (m, n) in enumerate(ORI):
        D[:, a, n] += p[:, m]; D[:, a, m] -= p[:, n]
    P = np.einsum("kal,kbl->kab", D, D.conj()) / p2[:, None, None]
    idem = np.abs(np.einsum("kab,kbc->kac", P, P) - P).max()
    tr = np.abs(np.einsum("kaa->k", P) - 3).max()
    ok["P1"] = idem < 1e-12 and tr < 1e-12
    log(f"P1 max|P^2-P|={idem:.2e}, max|trP-3|={tr:.2e} -> {ok['P1']}")

    # P2 exact torus
    p2ok = True
    for L in (4, 8, 16):
        v = accumulate(torus_slices(L), [(a12, a12, (0, 0, 0, 0))])[0] * (L ** 4 - 1) / L ** 4
        exp_ = (1 - L ** -4) / 2
        log(f"P2 torus L={L}: <th12^2>={v:.15f} expected {exp_:.15f} diff {v-exp_:.1e}")
        p2ok &= abs(v - exp_) < 1e-12
    ok["P2"] = p2ok

    # targets for infinite volume
    T = [(a12, a12, (0, 0, 0, 0)),            # 0 diag
         (a12, a12, tuple(e[3])),             # 1 one step in time (C4's C1(1))
         (a12, a12, tuple(e[2])),             # 2 parallel, one step transverse
         (a12, a12, tuple(3 * e[2])),         # 3 three steps
         (a12, a12, tuple(e[0])),             # 4 coplanar sharing link
         (a12, a13, (0, 0, 0, 0))]            # 5 perpendicular sharing A_1(0)
    # edge test: edge A_0(0); faces (0,nu) at 0 sign +, at -e_nu sign -
    faces = []
    for nu in (1, 2, 3):
        o, s = ori(0, nu)
        faces.append((o, s, np.zeros(4, int)))
        faces.append((o, -s, -e[nu]))
    edge_idx = []
    for (oa, sa, xa), (ob, sb, xb) in itertools.product(faces, faces):
        edge_idx.append((len(T), sa * sb)); T.append((oa, ob, tuple(xa - xb)))
    refl_idx = []
    for i in range(4):
        for j in range(4):
            if i == j: continue
            o, _ = ori(i, j)
            for n in range(5):
                refl_idx.append((i, j, n, len(T))); T.append((o, o, tuple((2 * n + 1) * e[i])))
    # dipole C(0) integrand handled separately
    res = {}
    for M in (32, 48):
        res[M] = accumulate(midpoint_slices(M), T)
        C0 = 0.0
        for K in midpoint_slices(M):
            kh = 2 - 2 * np.cos(K)
            C0 += (kh[:, 2] * (kh[:, 0] + kh[:, 1]) / kh.sum(1)).sum()
        res[(M, "C0")] = C0 / M ** 4
    r48, r = res[32], res[48]
    diag = r[0]
    ok["P3"] = abs(diag - 0.5) < 2e-4 and abs(r[0] - r48[0]) < 2e-4
    log(f"P3 inf vol <th12^2> M=48: {diag:.8f} (M=32 {r48[0]:.8f}); 2/d=0.5 -> {ok['P3']}")
    ok["P4"] = abs(r[1] - 0.06887475) < 2e-4
    log(f"P4 cov(th12(0),th12(e4)) = {r[1]:.8f} (M=32 {r48[1]:.8f}); C4 C1(1)=0.06887475 -> {ok['P4']}")
    ev = sum(s * r[t] for t, s in edge_idx)
    ok["P5"] = abs(ev - 6) < 1e-3
    log(f"P5 edge variance = {ev:.6f} (expect 6) -> {ok['P5']}")
    nq = 0; nf = 0
    for i, j, n, t in refl_idx:
        good = r[t] <= 2e-4
        nq += good; nf += (not good)
        log(f"   P6 case i={i+1} j={j+1} n={n}: cov(sep {2*n+1} e_{i+1}) = {r[t]:+.6f} {'ok' if good else 'FAIL'}")
    ok["P6"] = nf == 0
    log(f"P6 reflection sign: {nq} of {nq+nf} cases <= 0 -> {ok['P6']}")
    C0 = res[(48, "C0")]
    alt = 2 * (r[0] - r[2])
    ok["P7"] = abs(C0 - alt) < 2e-4
    log(f"P7 dipole C(0)={C0:.8f} vs 2(diag-par)={alt:.8f} -> {ok['P7']}")
    log(f"measured: parallel e3 {r[2]:.8f}; at 3e3 {r[3]:.8f}; coplanar e1 {r[4]:.8f}; perpendicular th12.th13 {r[5]:.8f}")
    # L=16 torus measured
    rt = accumulate(torus_slices(16), T[:6]) * (16 ** 4 - 1) / 16 ** 4
    log("measured L=16 torus (k=0 dropped): " + ", ".join(f"{x:.8f}" for x in rt))

    # P8
    mom_ok = True
    for k in range(7):
        c4 = 2.0 ** -k * math.gamma(k + 1.5) / math.gamma(1.5)
        chi = 4.0 ** -k * 2 ** k * math.gamma(k + 1.5) / math.gamma(1.5)  # E chi2_3^k = 2^k G(k+3/2)/G(3/2)
        mom_ok &= abs(c4 - chi) <= 1e-12 * chi
    rng = np.random.default_rng(7)
    F = rng.normal(0, math.sqrt(0.5), (10 ** 6, 3)); Y = (F ** 2).sum(1) / 2
    m, v = Y.mean(), Y.var()
    se_m = math.sqrt(3 / 8 / 1e6); se_v = math.sqrt((15 * 7 * 9 / 16 / 16 * 0 + 1) * 1e-6) * 1.0  # crude
    # exact Var of sample variance needs 4th central moment of chi2_3/4: mu4 = (12*3+3*9)/256*... use MC sd
    se_v = (Y ** 2).std() / 1e3
    ok["P8"] = mom_ok and abs(m - 0.75) < 5 * se_m and abs(v - 0.375) < 5 * se_v
    log(f"P8 moments formula ok={mom_ok}; MC E Y={m:.5f} (3/4), Var Y={v:.5f} (3/8) -> {ok['P8']}")

    log("SUMMARY " + " ".join(f"{k}:{'met' if v else 'FAILED'}" for k, v in ok.items()))
    with open(out, "x") as f:
        f.write("\n".join(lines) + "\n")
    sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
