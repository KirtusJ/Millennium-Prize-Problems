"""Spatial SU(2) Wilson flow on one periodic 4^3 slice -- predicate check.

CONVENTION (fixed before the first run, g_0^2 = 1)
---------------------------------------------------
S(V) = sum_x sum_{i<j} (1 - 1/2 Re tr U_ij(x)),
U_ij(x) = V(x,i) V(x+i,j) V(x+j,i)^dag V(x,j)^dag.
Staple A(x,i) = sum_{j!=i} [ V(x+i,j) V(x+j,i)^dag V(x,j)^dag
                           + V(x+i-j,j)^dag V(x-j,i)^dag V(x-j,j) ],
so that S = const - (1/2) Re tr(V(x,i) A(x,i)) as a function of V(x,i).
Derivation: perturb V -> exp(tX) V, X in su(2).  dS/dt = -(1/2) Re tr(X V A).
For anti-Hermitian X, Re tr(X M) = Re tr(X P_ah(M)) (the Hermitian part of M
pairs to an imaginary trace, the trace part to tr X = 0).
Choose Z(x,i) = P_ah(V(x,i) A(x,i)),  dV/ds = -Z V.  Then
   dS/ds = -(1/2) sum Re tr(-Z * Z) = (1/2) sum tr(Z Z) = -(1/2) sum ||Z||_F^2 <= 0
(tr(Z Z) = -||Z||_F^2 for anti-Hermitian Z).  const = 1/2, Frobenius norm.

Integrators (both act by left multiplication with exp of an su(2) element, so
they preserve SU(2) exactly up to roundoff):
  Euler:  V <- exp(-eps Z(V)) V
  RK3 (Luscher 2010, with Luscher's Z_k := -eps Z(W_k)):
    W1 = exp(Z0/4) W0; W2 = exp(8/9 Z1 - 17/36 Z0) W1;
    W3 = exp(3/4 Z2 - 8/9 Z1 + 17/36 Z0) W2.
Initial config: Haar-random links (normalized Gaussian quaternions), seed 20261123.

PREDICATES AND TOLERANCES (fixed before the first run)
------------------------------------------------------
P1  max over links of ||V^dag V - 1||_max and |det V - 1| <= 1e-12 after the
    flow to s=1 (all integrators, all eps).  Source: each step is one product of
    2x2 matrices with an analytic exp; roundoff ~1e-16 per step, <= 400 steps ->
    ~1e-13; 1e-12 leaves one order of margin.  No reunitarization is done.
P2  S(V_{s+eps}) <= S(V_s) + 1e-12 at every step, s in [0,1], for Euler and RK3
    with eps = 0.01 and eps = 0.005.  Tolerance 1e-12: absolute roundoff on a sum
    of 192 O(1) terms (~192*1e-16 ~ 2e-14), times margin.
P3  Gauge covariance: random g(x) in SU(2); flow g.V (V(x,i)->g(x)V(x,i)g(x+i)^dag)
    and compare with g.(flowed V), max entry difference <= 1e-11, Euler and RK3,
    eps=0.01, s=1.  Source: Z(g.V)(x,i) = g(x) Z(V)(x,i) g(x)^dag exactly, so
    every step is exactly covariant; the discrepancy is pure roundoff, ~1e-15
    per step amplified over 100 steps (flow is smoothing, not chaotic) -> ~1e-13;
    1e-11 gives margin, and is far below O(eps)=1e-2 (would expose a
    non-covariant staple/ordering error).
P4  (a) Structural: the field array holds only the 3 spatial directions of one
    slice; Z is built only from np.roll shifts within the slice (no temporal
    links exist in the data structure).  (b) Numerical: at s=0,
    D_fd = [S(exp(-hZ)V) - S(exp(+hZ)V)]/(2h), h=1e-4, must equal
    -(1/2) sum||Z||^2 with relative error <= 1e-6.  Source: central-difference
    truncation ~h^2 * S'''/S' ~ 1e-8 relative (S''' = O(|S'|) for this
    O(1)-curvature action), roundoff ~ 1e-16*S/h ~ 2e-10 absolute; 1e-6 margin.
P5  Convergence: with eps in {0.01, 0.005, 0.0025}, d1 = S_eps - S_{eps/2},
    d2 = S_{eps/2} - S_{eps/4} at s=1; measured order p = log2(d1/d2).
    Euler: p in [0.8, 1.2]; RK3: p in [2.6, 3.4].  Source: leading-error
    Richardson ratio 2^p, with O(eps) next-order corrections at these eps
    (eps*|S''|/|S'| ~ few %) -> +-0.2 for Euler; RK3 higher-order terms and
    smaller d's -> +-0.4.  Also requires |d2| > 1e-11 (above roundoff).

Exit code 0 iff all predicates hold, 1 otherwise.  Results written to a NEW
json file results_runN.json (never overwrites).
"""
import json
import os
import sys

import numpy as np

L = 4
SEED = 20261123
I2 = np.eye(2, dtype=complex)


def dag(M):
    return np.conj(np.swapaxes(M, -1, -2))


def mm(A, B):
    return A @ B


def sh(F, d, n=1):
    """F(x + n*e_d) for field of shape (L,L,L,...)"""
    return np.roll(F, -n, axis=d)


def random_su2(shape, rng):
    q = rng.normal(size=shape + (4,))
    q /= np.linalg.norm(q, axis=-1, keepdims=True)
    a, b, c, d = q[..., 0], q[..., 1], q[..., 2], q[..., 3]
    M = np.empty(shape + (2, 2), dtype=complex)
    M[..., 0, 0] = a + 1j * d
    M[..., 0, 1] = c + 1j * b
    M[..., 1, 0] = -c + 1j * b
    M[..., 1, 1] = a - 1j * d
    return M


def plaq(V, i, j):
    return mm(mm(V[..., i, :, :], sh(V[..., j, :, :], i)),
              mm(dag(sh(V[..., i, :, :], j)), dag(V[..., j, :, :])))


def action(V):
    S = 0.0
    for i in range(3):
        for j in range(i + 1, 3):
            S += np.sum(1.0 - 0.5 * np.real(np.trace(plaq(V, i, j), axis1=-2, axis2=-1)))
    return S


def staple(V):
    A = np.zeros_like(V)
    for i in range(3):
        for j in range(3):
            if j == i:
                continue
            Vi, Vj = V[..., i, :, :], V[..., j, :, :]
            up = mm(mm(sh(Vj, i), dag(sh(Vi, j))), dag(Vj))
            Vj_mj = sh(Vj, j, -1)
            down = mm(mm(dag(sh(Vj_mj, i)), dag(sh(Vi, j, -1))), Vj_mj)
            A[..., i, :, :] += up + down
    return A


def p_ah(M):
    X = 0.5 * (M - dag(M))
    tr = np.trace(X, axis1=-2, axis2=-1)
    return X - 0.5 * tr[..., None, None] * I2


def Zfield(V):
    return p_ah(mm(V, staple(V)))


def expm_su2(X):
    """exp of traceless anti-Hermitian 2x2: X^2 = -theta^2 1, theta^2 = det X."""
    th2 = np.real(X[..., 0, 0] * X[..., 1, 1] - X[..., 0, 1] * X[..., 1, 0])
    th = np.sqrt(np.maximum(th2, 0.0))
    c = np.cos(th)
    s = np.where(th > 1e-300, np.sin(th) / np.where(th > 0, th, 1.0), 1.0)
    return c[..., None, None] * I2 + s[..., None, None] * X


def step_euler(V, eps):
    return mm(expm_su2(-eps * Zfield(V)), V)


def step_rk3(V, eps):
    Z0 = -eps * Zfield(V)
    W1 = mm(expm_su2(0.25 * Z0), V)
    Z1 = -eps * Zfield(W1)
    W2 = mm(expm_su2(8 / 9 * Z1 - 17 / 36 * Z0), W1)
    Z2 = -eps * Zfield(W2)
    return mm(expm_su2(0.75 * Z2 - 8 / 9 * Z1 + 17 / 36 * Z0), W2)


STEPPERS = {"euler": step_euler, "rk3": step_rk3}


def flow(V, eps, method, record=False):
    n = int(round(1.0 / eps))
    Ss = [action(V)] if record else None
    for _ in range(n):
        V = STEPPERS[method](V, eps)
        if record:
            Ss.append(action(V))
    return V, Ss


def su2_dev(V):
    u = np.max(np.abs(mm(dag(V), V) - I2))
    det = V[..., 0, 0] * V[..., 1, 1] - V[..., 0, 1] * V[..., 1, 0]
    return float(u), float(np.max(np.abs(det - 1)))


def gauge(V, g):
    W = np.empty_like(V)
    for i in range(3):
        W[..., i, :, :] = mm(mm(g, V[..., i, :, :]), dag(sh(g, i)))
    return W


def main():
    rng = np.random.default_rng(SEED)
    V0 = random_su2((L, L, L, 3), rng)
    g = random_su2((L, L, L), rng)
    res = {"seed": SEED, "L": L, "S0": action(V0),
           "convention": "Z=P_ah(V A), dV/ds=-Z V, dS/ds=-(1/2) sum ||Z||_F^2"}
    ok = {}

    # P1, P2, P5 data
    finals = {}
    p1 = []
    p2 = []
    for m in ("euler", "rk3"):
        for eps in (0.01, 0.005, 0.0025):
            V1, Ss = flow(V0, eps, m, record=True)
            finals[(m, eps)] = Ss[-1]
            u, d = su2_dev(V1)
            p1.append({"method": m, "eps": eps, "unitarity": u, "det": d})
            if eps in (0.01, 0.005):
                inc = np.diff(Ss)
                p2.append({"method": m, "eps": eps, "max_increase": float(inc.max()),
                           "S_0": Ss[0], "S_1": Ss[-1]})
    res["P1"] = p1
    ok["P1"] = all(r["unitarity"] <= 1e-12 and r["det"] <= 1e-12 for r in p1)
    res["P2"] = p2
    ok["P2"] = all(r["max_increase"] <= 1e-12 for r in p2)

    # P3
    p3 = []
    for m in ("euler", "rk3"):
        A, _ = flow(V0, 0.01, m)
        B, _ = flow(gauge(V0, g), 0.01, m)
        p3.append({"method": m, "eps": 0.01, "max_diff": float(np.max(np.abs(B - gauge(A, g))))})
    res["P3"] = p3
    ok["P3"] = all(r["max_diff"] <= 1e-11 for r in p3)

    # P4
    Z = Zfield(V0)
    h = 1e-4
    analytic = -0.5 * float(np.sum(np.abs(Z) ** 2))
    fd = (action(mm(expm_su2(-h * Z), V0)) - action(mm(expm_su2(h * Z), V0))) / (2 * h)
    rel = abs(fd - analytic) / abs(analytic)
    res["P4"] = {"structural": "field shape (4,4,4,3,2,2): spatial links of one slice only; "
                               "staples use np.roll on the 3 spatial axes",
                 "dSds_analytic": analytic, "dSds_fd": fd, "h": h, "rel_err": rel}
    ok["P4"] = V0.shape == (L, L, L, 3, 2, 2) and rel <= 1e-6

    # P5
    p5 = []
    bounds = {"euler": (0.8, 1.2), "rk3": (2.6, 3.4)}
    for m in ("euler", "rk3"):
        a, b, c = finals[(m, 0.01)], finals[(m, 0.005)], finals[(m, 0.0025)]
        d1, d2 = a - b, b - c
        p = float(np.log2(abs(d1 / d2))) if d2 != 0 else float("nan")
        lo, hi = bounds[m]
        p5.append({"method": m, "S1": [a, b, c], "d1": d1, "d2": d2, "order": p,
                   "ok": bool(lo <= p <= hi and abs(d2) > 1e-11 and d1 * d2 > 0)})
    res["P5"] = p5
    ok["P5"] = all(r["ok"] for r in p5)

    res["ok"] = ok
    n = 1
    while os.path.exists(f"results_run{n}.json"):
        n += 1
    fn = f"results_run{n}.json"
    with open(fn, "w") as f:
        json.dump(res, f, indent=1, default=float)
    print(json.dumps(res, indent=1, default=float))
    print("written", fn)
    print("PREDICATES", ok)
    sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
