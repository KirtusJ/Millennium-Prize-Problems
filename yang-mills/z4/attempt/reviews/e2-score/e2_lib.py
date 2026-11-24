import numpy as np, math
def qm(a, b):
    a0,a1,a2,a3 = np.moveaxis(a,-1,0); b0,b1,b2,b3 = np.moveaxis(b,-1,0)
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0], -1)
def cj(a): return a * np.array([1,-1,-1,-1.])
def rq(rng, k):
    q = rng.standard_normal((k, 4)); return q / np.linalg.norm(q, axis=1, keepdims=True)
E = np.eye(4)
def prod(*qs):
    r = qs[0]
    for q in qs[1:]: r = qm(r, q)
    return r

rng = np.random.default_rng(20261124)
K = 100000
C, u, M, w, N = (rq(rng, K) for _ in range(5))
Y = prod(C, u, M, w, N)[:, 0]
S = np.zeros(K)
for a in range(1, 4):
    for b in range(1, 4):
        S += prod(C, u, np.broadcast_to(E[a], (K,4)), M, w, np.broadcast_to(E[b], (K,4)), N)[:, 0]**2
err = np.max(np.abs(S - 2 - Y**2))
pred("A1 sum A^2 = 2+Y^2", err <= 1e-12 and S.min() >= 2 - 1e-12, f"maxerr={err:.2e} min={S.min():.6f} max={S.max():.6f}")

# A2: F as function of the four free links; frozen factors random
def expq(v):  # v: pure imaginary 3-vector
    th = np.linalg.norm(v)
    if th == 0: return np.array([1.,0,0,0])
    return np.concatenate([[math.cos(th)], math.sin(th) * v / th])
def Fval(L, fr):
    u, v, w, z = L
    B, X00, X10, Y00, Y01, Y20, Y21, X02, X12 = fr
    g0 = prod(X00, w, cj(u), cj(Y00))
    g1 = prod(X00, X10, Y20, cj(v), cj(w), cj(X00))
    g2 = prod(Y00, u, z, cj(X02), cj(Y01), cj(Y00))
    g3 = prod(X00, w, v, Y21, cj(X12), cj(z), cj(w), cj(X00))
    gs = [g0, g1, g2, g3]
    return [prod(B, g)[0] for g in gs]
