"""ratio_check.py -- e2-chalBgen. Two checks, predicates fixed before first run.

Part A (A2, no group factor). Limit observable X_m = 1/2 (xi_m+f)^T B (xi_m+f), xi_m in R^d centred
Gaussian, colour covariance A (pos. def.), Cov(xi_0^i, xi_n^j) = G(n) A_ij, f an independent random
constant background (colours may be correlated). Exact formula (Isserlis):
   Cov(X_0,X_n) = 1/2 G(n)^2 Tr((BA)^2) + G(n) E[f^T B A B f] + 1/4 Var(f^T B f).
The builder's case is A = B = I (rho-orthonormal colours). G(0)=1/2, G(1)=0.0688747 (values quoted in
sec_proof_SU2.tex, orientation only).
  QA1: formula agrees with a direct sample estimate (seed 7, 400000 samples, d=4, U(1)xSU(2)-like
       A=B=diag(1,1,1,1) and a correlated non-Gaussian f) within 5 standard errors (std error from the
       sample, delta method not used: I compare the covariance estimate to the formula with
       se = sd(X0*Xn - ...) / sqrt(n) computed via batch means of 40 batches).
  QA2: for all 3000 random cases (d in {1,3,4,8}, random A, B, random f laws incl. correlated
       Gaussian, two-point, mixtures), ratio Cov/Var >= (G1/G0)^2 - 1e-12 (1e-12: float64 roundoff).
       Hypothesis per case: Var>0 (counted).
  QA3: with f = 0, A = B = I the ratio equals (G1/G0)^2 to 1e-12 for every d (no d-dependence).
Part B (A1 with the box gauge). Minimal box O(2), arms h_a as in box_mc.py; the box gauge sets the
interior time link x0->x0+e0 to 1, i.e. h_{+0} = 1. Minimise S over the 7 other arms from 20 random
starts in each of the 2^7 component patterns (own gradient-free coordinate descent on angles).
  QB1: the only pattern with min S < 1e-8 is the all-identity-component pattern (count reported).
  QB2: smallest min S over the other patterns >= 6 - 1e-9 (expectation: one reflection arm frustrates
       6 plaquettes, s = 1 exactly on each).
  QB0: closed-form S equals matrix-form S on 200 random configs (1e-12, roundoff); added before first run.
Output results_ratio.txt (mode 'x').
"""
import numpy as np, itertools, sys
G0, G1 = 0.5, 0.0688747
c1 = (G1 / G0) ** 2

def formula(G, A, B, fs, w):
    # fs: samples/atoms of f (k x d) with weights w
    BA = B @ A
    q = np.einsum('ki,ij,kj->k', fs, B, fs)
    r = np.einsum('ki,ij,kj->k', fs, B @ A @ B, fs)
    Eq = w @ q; Vq = w @ (q - Eq) ** 2
    return 0.5 * G ** 2 * np.trace(BA @ BA) + G * (w @ r) + 0.25 * Vq

def rand_pd(d, rng):
    M = rng.standard_normal((d, d)); return M @ M.T + 0.05 * np.eye(d)

def rand_f(d, rng):
    kind = rng.integers(4)
    if kind == 0:
        return np.zeros((1, d)), np.ones(1)
    if kind == 1:  # correlated gaussian, as 4000 samples
        L = rng.standard_normal((d, d)) * rng.exponential(2)
        fs = rng.standard_normal((4000, d)) @ L.T + rng.standard_normal(d) * rng.exponential(1)
        return fs, np.full(4000, 1 / 4000)
    if kind == 2:  # two-point
        fs = rng.standard_normal((2, d)) * rng.exponential(3); p = rng.uniform(0.01, 0.99)
        return fs, np.array([p, 1 - p])
    k = 5; fs = rng.standard_normal((k, d)) * rng.exponential(3, size=(k, 1)); w = rng.dirichlet(np.ones(k))
    return fs, w

out = open('results_ratio.txt', 'x')
def W(s): print(s); out.write(s + '\n'); out.flush()
fails = 0
# QA1
rng = np.random.default_rng(7)
d = 4; n = 400000; A = np.eye(d); B = np.eye(d)
z0 = rng.standard_normal((n, d)); z1 = rng.standard_normal((n, d))
rho = G1 / G0
xi0 = np.sqrt(G0) * z0; xin = np.sqrt(G0) * (rho * z0 + np.sqrt(1 - rho ** 2) * z1)
fcorr = np.where(rng.random((n, 1)) < 0.3, 1.0, -0.5) * np.array([1.0, 0.8, 0.8, 0.0]) + 0.3 * rng.standard_normal((n, 1)) * np.ones(d)
X0 = 0.5 * np.sum((xi0 + fcorr) ** 2, 1); Xn = 0.5 * np.sum((xin + fcorr) ** 2, 1)
est = np.cov(X0, Xn)[0, 1]
bat = [np.cov(X0[i::40], Xn[i::40])[0, 1] for i in range(40)]
se = np.std(bat, ddof=1) / np.sqrt(40)
pred = formula(G1, A, B, fcorr, np.full(n, 1 / n))
ok = abs(est - pred) <= 5 * se
fails += not ok
W(f"QA1 sample Cov={est:.5f} formula={pred:.5f} se={se:.5f} -> {'MET' if ok else 'FAILED'}")
# QA2
worst = np.inf; worst_case = None; nq = 0; npos = 0
for case in range(3000):
    d = int(rng.choice([1, 3, 4, 8]))
    A = rand_pd(d, rng) if case % 2 else np.eye(d)
    B = rand_pd(d, rng) if case % 3 else A.copy() if case % 2 == 0 else np.linalg.inv(A)
    fs, w = rand_f(d, rng)
    cv = formula(G1, A, B, fs, w); vr = formula(G0, A, B, fs, w)
    if vr > 0:
        npos += 1; r = cv / vr
        if r < worst: worst, worst_case = r, (d, case)
        if r < c1 - 1e-12: nq += 1
fails += nq > 0
W(f"QA2 cases with Var>0: {npos}/3000; violations of ratio>=c(1)={c1:.6e}: {nq} -> {'MET' if nq == 0 else 'FAILED'}; worst ratio {worst:.6e} at (d,case)={worst_case}")
# QA3
for d in [1, 3, 4, 8, 248]:
    r = formula(G1, np.eye(d), np.eye(d), np.zeros((1, d)), np.ones(1)) / formula(G0, np.eye(d), np.eye(d), np.zeros((1, d)), np.ones(1))
    ok = abs(r - c1) <= 1e-12; fails += not ok
    W(f"QA3 d={d} ratio={r:.12e} c1={c1:.12e} -> {'MET' if ok else 'FAILED'}")
# Part B
rng = np.random.default_rng(11)
PAIRS = [(a, b) for a in range(8) for b in range(8) if a < b and a // 2 != b // 2]
def mat(t, dt):
    c, s = np.cos(t), np.sin(t)
    return np.array([[c, -s], [s, c]]) @ np.diag([1.0, dt])
def S_mat(th, dets):
    hs = [np.eye(2)] + [mat(th[i], dets[i]) for i in range(7)]  # arm 0 = +0 gauge-fixed to 1
    return sum(1 - np.trace(hs[a] @ hs[b].T) / 2 for a, b in PAIRS)
PA = np.array(PAIRS)
def S(th, dets):  # closed form: Tr(h_a h_b^T)/2 = cos(t_a-t_b) if same det, 0 otherwise
    t = np.concatenate([[0.0], th]); dd = np.concatenate([[1.0], dets])
    same = dd[PA[:, 0]] == dd[PA[:, 1]]
    return float(np.sum(1 - same * np.cos(t[PA[:, 0]] - t[PA[:, 1]])))
dmax = max(abs(S_mat(th, dt) - S(th, dt)) for th, dt in ((rng.uniform(-4, 4, 7), rng.choice([1.0, -1.0], 7)) for _ in range(200)))
ok = dmax < 1e-12; fails += not ok
W(f"QB0 closed form vs matrix form, 200 random configs: max diff {dmax:.2e} -> {'MET' if ok else 'FAILED'} (tol 1e-12 roundoff)")
def minimize(dets, th):
    f = S(th, dets); step = 0.5
    while step > 1e-9:
        imp = False
        for i in range(7):
            for sg in (1, -1):
                t2 = th.copy(); t2[i] += sg * step; f2 = S(t2, dets)
                if f2 < f - 1e-15: th, f, imp = t2, f2, True
        if not imp: step *= 0.5
    return f
res = {}
for dets in itertools.product([1.0, -1.0], repeat=7):
    res[dets] = min(minimize(dets, rng.uniform(-np.pi, np.pi, 7)) for _ in range(20))
zero = [k for k, v in res.items() if v < 1e-8]
ok = zero == [tuple([1.0] * 7)]; fails += not ok
W(f"QB1 patterns with min S<1e-8: {len(zero)} {zero} -> {'MET' if ok else 'FAILED'}")
other = min(v for k, v in res.items() if k != tuple([1.0] * 7))
ok = other >= 6 - 1e-9; fails += not ok
W(f"QB2 smallest min S over the 127 other patterns = {other:.9f} -> {'MET' if ok else 'FAILED'}")
W(f"distinct minima (rounded 1e-6): {sorted(set(round(v, 6) for v in res.values()))}")
W(f"failures: {fails}")
out.close(); sys.exit(1 if fails else 0)
