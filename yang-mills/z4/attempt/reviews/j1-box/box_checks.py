"""Independent finite checks for the periodic-box spectrum review (j1-box, T107).

Predicates (fixed before the first run):
P1 (item 3, constant-mode mass): abelianised quadratic theory on boxes (2,2,2),(3,2,2),(3,3,3):
    kernel K(A,A') = exp(-A^T M A/4) * [orbit-integrated electric Gaussian, width s] * exp(-A'^T M A'/4),
    A, A' on the slice ker d^* (orthogonal complement of range d). Integrate out the nonconstant slice
    modes at both ends (Gaussian Schur complement). The remaining form in (c, c') (c = per-link constant
    value) must equal n |c-c'|^2 / s^2 per direction: coefficient of c_i c_i equals n/s^2, of c_i c'_i equals
    -n/s^2, no other terms. Relative tolerance 1e-9 (double-precision linear algebra on <= 81-dim
    matrices, condition number ~1e2..1e4 for s=0.3, 0.1).
P2 slice dimension (abelian, one color) = 3n-(n-1) = 2n+1; nonzero eigenvalues of M (curl^T curl) on the
    nonconstant slice are exactly m_p = 4 sum sin^2(p_i/2) with multiplicity 2 per nonzero momentum.
    Tolerance 1e-9 (eigh roundoff).
P3 E_{*,N} = 3 sum_{p!=0} omega(m_p) equals (3 colours) x (1/2) sum omega(eig M on nonconstant slice);
    for (2,2,2) it equals (1/2)[18 w(4)+18 w(8)+6 w(12)]. Tolerance 1e-10.
P4 (full-neutral sec 1, for all): for box shapes (2,2,2),(3,2,2),(4,3,2),(5,3,3) and 200 random twists
    theta in [0,2pi)^3 each (seed 20261123), sum_p omega(m(p+theta)) - sum_p omega(m(p)) > 0 for every
    non-central theta (strict, > 1e-12); and = 0 (|.| < 1e-10) for all 8*... central theta_i = 2 pi k_i/N_i
    (all k). Report count of qualifying cases.
P5 (sec 2 oscillator): top eigenvalue of e^{-m y^2/4} K1 e^{-m y'^2/4} (K1 unit Gaussian convolution) equals
    e^{-omega(m)/2}, omega(m)=arcosh(1+m/2)=2 arsinh(sqrt(m)/2), for m in {0.01,0.1,1}; tolerance 1e-6
    relative (grid spacing 0.02 on [-L,L], trapezoid; discretisation error is exponentially small for
    Gaussians on a uniform grid; 1e-6 is a conservative margin).
P6 (item 2a): hard zero-point on the horizontal plane at commuting background c_i = r_i e, box (3,2,2) and
    (3,3,3): E(r) = sum_{p!=0}[w(m(p)) + w(m(p+2r)) + w(m(p-2r))] (one neutral + two charged colours, two
    transverse polarisations each, 1/2 per oscillator); first derivative at 0 is 0 (|.|<1e-8, central
    finite difference step 1e-4, error O(step^2)) and E(r)-E(0) ~ kappa |r|^2 (ratio test at r and r/2:
    ratio within 4 +- 0.01).
"""
import itertools
import numpy as np

rng = np.random.default_rng(20261123)
w = lambda x: np.arccosh(1.0 + np.asarray(x) / 2.0)
results = []


def rec(name, ok, detail):
    results.append((name, bool(ok), detail))
    print(("MET   " if ok else "FAILED"), name, detail, flush=True)


def site_index(shape):
    return {x: k for k, x in enumerate(itertools.product(*[range(N) for N in shape]))}


def build(shape):
    idx = site_index(shape)
    n = len(idx)
    link = lambda k, i: 3 * k + i
    d = np.zeros((3 * n, n))
    for x, k in idx.items():
        for i in range(3):
            y = list(x); y[i] = (y[i] + 1) % shape[i]
            d[link(k, i), idx[tuple(y)]] += 1.0
            d[link(k, i), k] -= 1.0
    rows = []
    for x, k in idx.items():
        for i, j in itertools.combinations(range(3), 2):
            xi = list(x); xi[i] = (xi[i] + 1) % shape[i]
            xj = list(x); xj[j] = (xj[j] + 1) % shape[j]
            r = np.zeros(3 * n)
            r[link(k, i)] += 1; r[link(idx[tuple(xi)], j)] += 1
            r[link(idx[tuple(xj)], i)] -= 1; r[link(k, j)] -= 1
            rows.append(r)
    F = np.array(rows)
    return n, d, F.T @ F


def p1_p2_p3(shape):
    n, d, M = build(shape)
    # slice basis: orthonormal complement of range d
    U, S, Vt = np.linalg.svd(d, full_matrices=True)
    rank = int(np.sum(S > 1e-9))
    slice_ = U[:, rank:]
    rec(f"P2 slice dim {shape}", slice_.shape[1] == 2 * n + 1, f"dim={slice_.shape[1]} expect {2*n+1}")
    # constant modes (orthonormal), and nonconstant slice complement
    C = np.zeros((3 * n, 3))
    for k in range(n):
        for i in range(3):
            C[3 * k + i, i] = 1 / np.sqrt(n)
    Pc = slice_ - C @ (C.T @ slice_)
    u, sv, _ = np.linalg.svd(Pc, full_matrices=False)
    W = u[:, sv > 1e-9]
    B = np.hstack([C, W])  # orthonormal basis of the slice
    for s in (0.3, 0.1):
        Ms = B.T @ M @ B
        dim = B.shape[1]
        I = np.eye(dim)
        Q = np.block([[Ms / 2 + I / s**2, -I / s**2], [-I / s**2, Ms / 2 + I / s**2]])
        keep = [0, 1, 2, dim, dim + 1, dim + 2]
        drop = [k for k in range(2 * dim) if k not in keep]
        Qs = Q[np.ix_(keep, keep)] - Q[np.ix_(keep, drop)] @ np.linalg.solve(Q[np.ix_(drop, drop)], Q[np.ix_(drop, keep)])
        # convert orthonormal coordinates a = sqrt(n) c to c: multiply by n
        Qc = Qs * n
        target = (n / s**2) * np.block([[np.eye(3), -np.eye(3)], [-np.eye(3), np.eye(3)]])
        err = np.max(np.abs(Qc - target)) / (n / s**2)
        rec(f"P1 constant-mode coefficient {shape} s={s}", err < 1e-9,
            f"kappa/n={Qc[0,0]*s**2/n:.12f}, rel.err={err:.2e}")
    # P2 eigenvalues on nonconstant slice
    ev = np.sort(np.linalg.eigvalsh(W.T @ M @ W))
    moms = [p for p in itertools.product(*[range(N) for N in shape]) if any(p)]
    mp = np.array([4 * sum(np.sin(np.pi * k / N) ** 2 for k, N in zip(p, shape)) for p in moms])
    expect = np.sort(np.repeat(mp, 2))
    ok = len(ev) == len(expect) and np.max(np.abs(ev - expect)) < 1e-9
    rec(f"P2 hard spectrum {shape}", ok, f"n_eig={len(ev)} expect {len(expect)} maxdev={np.max(np.abs(ev-expect)) if ok or len(ev)==len(expect) else 'len'}")
    E_formula = 3 * np.sum(w(mp))
    E_eig = 3 * 0.5 * np.sum(w(ev))
    rec(f"P3 E_*N {shape}", abs(E_formula - E_eig) < 1e-10, f"E*={E_formula:.10f} eig={E_eig:.10f} gap d/g=1-exp(-{w(mp.min()):.6f})")
    if shape == (2, 2, 2):
        E2 = 0.5 * (18 * w(4) + 18 * w(8) + 6 * w(12))
        rec("P3 E_* 2^3 two-site formula", abs(E2 - E_formula) < 1e-10, f"{E2:.10f}")


def esum(shape, theta):
    tot = 0.0
    for k in itertools.product(*[range(N) for N in shape]):
        m = sum(2 * (1 - np.cos(2 * np.pi * ki / N + t)) for ki, N, t in zip(k, shape, theta))
        tot += w(m)
    return tot


def p4():
    shapes = [(2, 2, 2), (3, 2, 2), (4, 3, 2), (5, 3, 3)]
    for shape in shapes:
        e0 = esum(shape, (0, 0, 0))
        nonc = rng.uniform(0, 2 * np.pi, size=(200, 3))
        diffs = np.array([esum(shape, th) - e0 for th in nonc])
        good = int(np.sum(diffs > 1e-12))
        rec(f"P4 strict winding {shape}", good == 200, f"{good}/200 qualify (non-central, strict); min diff={diffs.min():.3e}")
        cen = list(itertools.product(*[range(N) for N in shape]))
        cd = np.array([esum(shape, tuple(2 * np.pi * k / N for k, N in zip(kk, shape))) - e0 for kk in cen])
        rec(f"P4 central equality {shape}", np.max(np.abs(cd)) < 1e-10, f"{len(cen)} grid twists, max|diff|={np.max(np.abs(cd)):.1e}")
        # near-central probe: smallest deficit along axis-1 twist epsilon (measured only)
        eps = 1e-2
        print(f"  measured only {shape}: deficit at theta=(eps,0,0), eps=1e-2: {esum(shape,(eps,0,0))-e0:.3e}")


def p5():
    L, hstep = 12.0, 0.02
    y = np.arange(-L, L + hstep / 2, hstep)
    for m in (0.01, 0.1, 1.0):
        K = np.exp(-(y[:, None] - y[None, :]) ** 2 / 2) / np.sqrt(2 * np.pi) * hstep
        Wt = np.exp(-m * y ** 2 / 4)
        T = Wt[:, None] * K * Wt[None, :]
        top = np.linalg.eigvalsh(T)[-1]
        pred = np.exp(-w(m) / 2)
        alt = np.exp(-np.arcsinh(np.sqrt(m) / 2))
        rec(f"P5 oscillator m={m}", abs(top / pred - 1) < 1e-6 and abs(alt / pred - 1) < 1e-12,
            f"top={top:.10f} pred={pred:.10f}")


def p6():
    for shape in [(3, 2, 2), (3, 3, 3)]:
        moms = [k for k in itertools.product(*[range(N) for N in shape]) if any(k)]

        def E(r):
            tot = 0.0
            for k in moms:
                p = np.array([2 * np.pi * ki / N for ki, N in zip(k, shape)])
                m = lambda q: np.sum(2 * (1 - np.cos(q)))
                tot += w(m(p)) + w(m(p + 2 * r)) + w(m(p - 2 * r))
            return tot
        dirs = rng.normal(size=(5, 3))
        for dvec in dirs:
            dvec = dvec / np.linalg.norm(dvec)
            st = 1e-4
            der = (E(st * dvec) - E(-st * dvec)) / (2 * st)
            e1 = E(0.02 * dvec) - E(0 * dvec)
            e2 = E(0.01 * dvec) - E(0 * dvec)
            ratio = e1 / e2
            rec(f"P6 hard zero-point {shape} dir", abs(der) < 1e-8 and abs(ratio - 4) < 0.01,
                f"dE/dr={der:.1e} ratio={ratio:.5f} kappa_dir={e2/0.01**2:.6f}")


if __name__ == "__main__":
    for shape in [(2, 2, 2), (3, 2, 2), (3, 3, 3)]:
        p1_p2_p3(shape)
    p4(); p5(); p6()
    met = sum(1 for r in results if r[1]); failed = len(results) - met
    with open("box_checks_result.txt", "x") as fh:
        for r in results:
            fh.write(("MET   " if r[1] else "FAILED") + f" {r[0]} | {r[2]}\n")
        fh.write(f"SUMMARY met={met} failed={failed}\n")
    print(f"SUMMARY met={met} failed={failed}")
    raise SystemExit(0 if failed == 0 else 1)
