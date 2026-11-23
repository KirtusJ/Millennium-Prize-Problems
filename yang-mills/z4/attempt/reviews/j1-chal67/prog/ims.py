"""ims.py -- exact check of the L3/L7-step-2 IMS localisation for a NON-LOCAL convolution K
on discretised rings (U(1)_N and U(1)_N x U(1)_N, a finite group), with the sin/cos partition of L7,
plus a quadrature check of the SU(2) second moment L2.

Setting (two links): t_i = 2 pi x_i / N, kernel k(t) = e^{b cos t}/Z_N normalised to sum 1 over the ring,
K2 = k (x) k (convolution), s_i = |sin t_i|, theta_i = (pi/2) clip(s_i/sigma - 1, 0, 1),
chi0 = cos th1 cos th2, chi1 = sin th1 cos th2, chi2 = sin th2, D(U,W) = sum_a (chi_a(U)-chi_a(W))^2,
d_i = ring geodesic distance |t_i - t_i'| mod 2pi in [0,pi].

PREDICATES (fixed before the first run):
 I1 partition: max |sum chi_a^2 - 1| <= 1e-12 (double rounding).
 I2 identity with the SIGN of LIMINF L3:
      sum_a <chi_a g,(1-K)chi_a g> - <g,(1-K)g> = + 1/2 sum_{U,W} k2(U,W) g(U) g(W) D(U,W)
    for 5 random real g (seed 12345): |difference| <= 1e-10 * ||g||^2 (rounding of N^4-term sums).
 I3 Schur: the operator E with kernel 1/2 k2 D has ||E||_op <= 1/2 max_U sum_W k2 D (exact eigenvalues, N=24).
    tolerance 1e-12 relative.
 I4 pointwise: D(U,W) <= (pi/(2 sigma))^2 (d1^2 + d2^2) for all pairs (N=24, all N^4 pairs). tol 1e-12.
 I5 consequence: 1/2 max_U sum_W k2 D <= 1/2 (pi/(2 sigma))^2 * 2 * sum_t k(t) d(t)^2 . tol 1e-12.
 I6 SU(2) L2: for beta in {2,5,10,30,100,300,1000,1e4}: int k a^2 dHaar <= pi^2/beta and 1 - E[cos a] <= 2/beta
    (quadrature on [0,pi], density (2/pi) sin^2 a e^{b(cos a-1)}, 200001-point Simpson; tol 1e-9 relative).
 Grid for I1-I5: N=24, b in {2, 8, 32}, sigma in {0.15, 0.3}.
 MEASURED ONLY: ratio ||E||_op / Schur bound; ratio Schur bound / (pi^2/(4 sigma^2)) * 2 E[d^2].
Exit 0 iff all predicates hold.
"""
import json, math, sys
import numpy as np
rng = np.random.default_rng(12345)
res = {"cases": [], "L2": []}
met = {k: 0 for k in ["I1", "I2", "I3", "I4", "I5", "I6"]}; fail = dict(met)
def rec(k, ok):
    if ok: met[k] += 1
    else: fail[k] += 1
N = 24
t = 2 * np.pi * np.arange(N) / N
dd = np.abs(t[:, None] - t[None, :]); dd = np.minimum(dd, 2 * np.pi - dd)
for b in [2.0, 8.0, 32.0]:
    kr = np.exp(b * (np.cos(t) - 1)); kr /= kr.sum()
    k1 = kr[(np.arange(N)[:, None] - np.arange(N)[None, :]) % N]  # k(U W^-1)
    K2 = np.kron(k1, k1)
    D1sq = np.kron(dd ** 2, np.ones((N, N))) ; D2sq = np.kron(np.ones((N, N)), dd ** 2)
    for sig in [0.15, 0.3]:
        T1, T2 = np.meshgrid(t, t, indexing="ij")
        th = lambda s: (np.pi / 2) * np.clip(s / sig - 1, 0, 1)
        h1 = th(np.abs(np.sin(T1))).ravel(); h2 = th(np.abs(np.sin(T2))).ravel()
        chis = [np.cos(h1) * np.cos(h2), np.sin(h1) * np.cos(h2), np.sin(h2)]
        e1 = float(np.max(np.abs(sum(c ** 2 for c in chis) - 1))); rec("I1", e1 <= 1e-12)
        D = sum((c[:, None] - c[None, :]) ** 2 for c in chis)
        A = np.eye(N * N) - K2
        worst2 = 0.0
        for _ in range(5):
            g = rng.standard_normal(N * N)
            lhs = sum((c * g) @ A @ (c * g) for c in chis) - g @ A @ g
            rhs = 0.5 * g @ (K2 * D) @ g
            dif = abs(lhs - rhs) / (g @ g); worst2 = max(worst2, dif); rec("I2", dif <= 1e-10)
        E = 0.5 * K2 * D
        op = float(np.max(np.abs(np.linalg.eigvalsh(E))))
        schur = float(0.5 * np.max(E.sum(axis=1) * 2))  # 1/2 max row sum of k2 D
        rec("I3", op <= schur * (1 + 1e-12))
        bound = (np.pi / (2 * sig)) ** 2 * (D1sq + D2sq)
        rec("I4", bool(np.all(D <= bound * (1 + 1e-12) + 1e-15)))
        m2 = float(kr @ (dd[0] ** 2))
        b5 = 0.5 * (np.pi / (2 * sig)) ** 2 * 2 * m2
        rec("I5", schur <= b5 * (1 + 1e-12))
        res["cases"].append({"beta": b, "sigma": sig, "partition_err": e1, "identity_err": worst2,
                             "op_norm": op, "schur": schur, "lip_bound": b5,
                             "op/schur": op / schur if schur else None, "schur/lip": schur / b5})
# I6
for b in [2.0, 5.0, 10.0, 30.0, 100.0, 300.0, 1000.0, 1e4]:
    n = 200001; a = np.linspace(0, np.pi, n); h = a[1] - a[0]
    w = np.ones(n); w[1:-1:2] = 4; w[2:-1:2] = 2; w *= h / 3
    dens = (2 / np.pi) * np.sin(a) ** 2 * np.exp(b * (np.cos(a) - 1))
    Zs = w @ dens
    m2 = (w @ (dens * a ** 2)) / Zs; omc = (w @ (dens * (1 - np.cos(a)))) / Zs
    ok = m2 <= np.pi ** 2 / b * (1 + 1e-9) and omc <= 2 / b * (1 + 1e-9)
    rec("I6", ok)
    res["L2"].append({"beta": b, "E_a2": m2, "pi2_over_b": np.pi ** 2 / b, "one_minus_Ecos": omc, "2_over_b": 2 / b, "ok": bool(ok)})
res["met"] = met; res["failed"] = fail
with open(sys.argv[1], "x") as fh: json.dump(res, fh, indent=1)
print("met", met); print("failed", fail)
for c in res["cases"]: print(c)
for c in res["L2"]: print(c)
sys.exit(0 if sum(fail.values()) == 0 else 1)
