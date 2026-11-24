"""y1-g4ret: independent checks of inheritance.md (items f, g, h, i, j, k).

Setting: reversible Markov generator on states (coarse label c, fine label f) with stationary pi;
Hilbert space L^2(pi) written in the orthonormal basis e_s/sqrt(pi_s); 'centered' = orthogonal to sqrt(pi).
P = conditional expectation on coarse label, R = multiplication by 1_A for a set A of coarse labels.

Predicates (fixed before the first run):
 I1 (f)  For 300 random structured examples (seed 5501): ||RP - PR|| < 1e-12 and B = RQ satisfies
         B = B^T = B^2 (tol 1e-12), B and G = Q - B annihilate sqrt(pi) (map centered to centered).
 I2 (i)  'for all' claim d >= (b - kappa)_+/(1 + 2a/(gamma t)). Qualification per case: gamma > 1e-12 and
         rank B >= 1 and tau <= t. Report qualifying count. Failure if slack < -1e-10
         (tolerance: float64 eigensolver error ~1e-13 times condition numbers <= 1e3 of the spectral factors).
         Family S (structured, 2000 cases, seed 5502), family U (generic: random PSD H, random
         orthogonal projections P, B with PB = 0; 2000 cases, seed 5503).
 I3 (g,h) intermediate inequalities in each structured case, for L = lambda_min + 1e-9 ... actually for
         L in {lambda_1, lambda_2} (the two lowest centered eigenvalues) and v = each unit eigenvector
         in E: gamma||Gv||^2 <= 1 - e^{-2aL}; ||Bv||^2 <= e^{tau L} kappa; 1 - b >= e^{-tL}(1 - ||Qv||^2). tol 1e-10.
 I4 adversarial: 40 Nelder-Mead-free random-search descents (seed 5504) minimising the slack over
         generic 3-dim examples (H diag + rotation, P, B rank one): min slack >= -1e-10. Report min slack.
 I5 (k)  reset process, 2 coarse labels, event mass eps in {1e-1,1e-3,1e-6}, two equiprobable fine labels:
         ||B S_t B|| = e^{-l t} to 1e-12 for l t in {0.1, 1, 3}.
 I6 (j)  accumulation: for 2000 random sequences (seed 5505) of length n<=8 with K_i>=1, eps_i, kappa_i >=0,
         d_0 in (0,1], the worst-case recursion d_i = (d_{i-1} - eps_i - kappa_i)_+/K_i satisfies
         d_n >= M_n^{-1}(d_0 - sum M_{i-1}(eps_i+kappa_i))_+ - 1e-14.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np

out = open("results_inherit.txt", "x")
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.write(s + "\n"); out.flush()
fails = []
def pred(name, ok, info=""):
    log(f"{name}: {'MET' if ok else 'FAILED'} {info}")
    if not ok: fails.append(name)

def fexp(h, V, s): return (V*np.exp(-s*h))@V.T

def structured(rng):
    nc = int(rng.integers(2, 5)); nf = int(rng.integers(2, 4)); n = nc*nf
    pi = rng.dirichlet(np.full(n, 1.0)) + 1e-3; pi /= pi.sum()
    sq = np.sqrt(pi)
    Wt = rng.uniform(0, 1, (n, n)) * (rng.random((n, n)) < 0.7); Wt = np.triu(Wt, 1); Wt += Wt.T
    # reversible rates q(x,y) = Wt(x,y)/pi(x); symmetric generator in L^2(pi) basis
    scale = 10**rng.uniform(-1.5, 1)
    L = (np.diag(Wt.sum(1)) - Wt)*scale
    H = L/np.outer(sq, sq)
    lab = np.repeat(np.arange(nc), nf)
    Cm = np.zeros((n, nc))
    for c in range(nc): Cm[lab == c, c] = sq[lab == c]
    Cm /= np.linalg.norm(Cm, axis=0)
    P = Cm@Cm.T
    Aset = rng.random(nc) < 0.5
    if not Aset.any(): Aset[0] = True
    R = np.diag(Aset[lab].astype(float))
    return n, H, P, R, sq

def evaluate(H, P, B, sq, a, t, tau, centred=True):
    n = len(H)
    if centred:
        Z = np.eye(n) - np.outer(sq, sq)
        # orthonormal basis of centered space
        w, V = np.linalg.eigh(Z); Bas = V[:, w > 0.5]
        H, P, B = (Bas.T@X@Bas for X in (H, P, B))
    h, V = np.linalg.eigh(H)
    Q = np.eye(len(H)) - P; G = Q - B
    M = fexp(-h, V, 1)*0  # placeholder
    mvals = -np.expm1(-2*a*h)
    if mvals.min() <= 0: return None
    Mih = (V/np.sqrt(mvals))@V.T
    top = np.linalg.eigvalsh(Mih@G@Mih)[-1]
    gamma = 1/top if top > 1e-14 else np.inf
    kappa = np.linalg.norm(B@fexp(h, V, tau)@B, 2)
    b = 1 - np.linalg.norm(P@fexp(h, V, t)@P, 2)
    lam = h[0]; d = -np.expm1(-t*lam)
    K = 1 + 2*a/(gamma*t)
    return dict(h=h, V=V, P=P, B=B, G=G, Q=Q, gamma=gamma, kappa=kappa, b=b, d=d, lam=lam,
                slack=d - max(b-kappa, 0)/K)

# I1 + family S
rng = np.random.default_rng(5501); ok = True
for _ in range(300):
    n, H, P, R, sq = structured(rng)
    Q = np.eye(n) - P; B = R@Q; G = Q - B
    ok &= np.linalg.norm(R@P - P@R) < 1e-12 and np.abs(B - B.T).max() < 1e-12 and np.abs(B@B - B).max() < 1e-12
    ok &= np.abs(B@sq).max() < 1e-12 and np.abs(G@sq).max() < 1e-12
pred("I1", ok)

rng = np.random.default_rng(5502)
qual = nf_ = 0; minslack = np.inf; ok3 = True; nI3 = 0
for _ in range(2000):
    n, H, P, R, sq = structured(rng)
    B = R@(np.eye(n) - P)
    a = 10**rng.uniform(-3, 0.5); t = 10**rng.uniform(-1.3, 0.7); tau = t*rng.uniform(0.01, 1)
    e = evaluate(H, P, B, sq, a, t, tau)
    if e is None or not np.isfinite(e["gamma"]) or e["gamma"] <= 1e-12 or np.linalg.matrix_rank(e["B"], 1e-9) < 1:
        continue
    qual += 1
    minslack = min(minslack, e["slack"])
    if e["slack"] < -1e-10: nf_ += 1
    # I3 on the two lowest eigenvectors
    for j in range(2):
        Lv = e["h"][j]; v = e["V"][:, j]
        g1 = e["gamma"]*np.linalg.norm(e["G"]@v)**2 <= -np.expm1(-2*a*Lv) + 1e-10
        g2 = np.linalg.norm(e["B"]@v)**2 <= np.exp(tau*Lv)*e["kappa"] + 1e-10
        g3 = 1 - e["b"] >= np.exp(-t*Lv)*(1 - np.linalg.norm(e["Q"]@v)**2) - 1e-10
        ok3 &= g1 and g2 and g3; nI3 += 1
pred("I2-S", nf_ == 0, f"qualifying={qual} failures={nf_} min slack={minslack:.3e}")
pred("I3", ok3, f"eigenvector tests={nI3}")

rng = np.random.default_rng(5503)
qual = nf_ = 0; minslack = np.inf
for _ in range(2000):
    n = int(rng.integers(3, 9))
    X = rng.normal(size=(n, n)); H = X@X.T/n
    if rng.random() < 0.5:
        h, V = np.linalg.eigh(H); H = (V*(h - h[0] + 10**rng.uniform(-8, -1)))@V.T
    O, _ = np.linalg.qr(rng.normal(size=(n, n)))
    rp = int(rng.integers(1, n-1)); rb = int(rng.integers(1, n-rp))
    P = O[:, :rp]@O[:, :rp].T; B = O[:, rp:rp+rb]@O[:, rp:rp+rb].T
    a = 10**rng.uniform(-3, 0.5); t = 10**rng.uniform(-1.3, 0.7); tau = t*rng.uniform(0.01, 1)
    e = evaluate(H, P, B, None, a, t, tau, centred=False)
    if e is None or not np.isfinite(e["gamma"]) or e["gamma"] <= 1e-12: continue
    qual += 1; minslack = min(minslack, e["slack"])
    if e["slack"] < -1e-10: nf_ += 1
pred("I2-U", nf_ == 0, f"qualifying={qual} failures={nf_} min slack={minslack:.3e}")

# I4 adversarial random search on 3x3
rng = np.random.default_rng(5504)
def build(x):
    h = np.abs(x[:3]); ang = x[3:6]; pv = x[6:9]; bv = x[9:12]
    def rot(a, i, j):
        Rm = np.eye(3); c, s = np.cos(a), np.sin(a); Rm[i, i] = Rm[j, j] = c; Rm[i, j] = -s; Rm[j, i] = s; return Rm
    O = rot(ang[0], 0, 1)@rot(ang[1], 1, 2)@rot(ang[2], 0, 2)
    H = (O*h)@O.T
    p = pv/np.linalg.norm(pv); bb = bv - p*(p@bv); bb /= np.linalg.norm(bb)
    a, t, fr = np.exp(x[12]), np.exp(x[13]), 1/(1+np.exp(-x[14]))
    return H, np.outer(p, p), np.outer(bb, bb), a, t, t*fr
def score(x):
    try:
        H, P, B, a, t, tau = build(x)
        e = evaluate(H, P, B, None, a, t, tau, centred=False)
        if e is None or not np.isfinite(e["gamma"]): return np.inf
        K = 1 + 2*a/(e["gamma"]*t)
        return e["d"]*K - (e["b"] - e["kappa"])
    except Exception:
        return np.inf
best_all = np.inf
for run in range(40):
    x = rng.normal(size=15); f = score(x); step = 1.0
    for it in range(600):
        y = x + step*rng.normal(size=15); g = score(y)
        if g < f: x, f = y, g
        elif it % 50 == 49: step *= 0.6
    best_all = min(best_all, f)
pred("I4", best_all >= -1e-10, f"min over searches of d*K-(b-kappa) = {best_all:.3e}")

# I5 reset
ok = True
for eps in (1e-1, 1e-3, 1e-6):
    pi = np.array([eps/2, eps/2, (1-eps)/2, (1-eps)/2]); sq = np.sqrt(pi)
    lab = np.array([0, 0, 1, 1]); Cm = np.zeros((4, 2))
    for c in range(2): Cm[lab == c, c] = sq[lab == c]
    Cm /= np.linalg.norm(Cm, axis=0); P = Cm@Cm.T
    R = np.diag([1., 1., 0., 0.]); B = R@(np.eye(4) - P)
    for lt in (0.1, 1, 3):
        S = np.exp(-lt)*np.eye(4) + (1-np.exp(-lt))*np.outer(sq, sq)
        ok &= abs(np.linalg.norm(B@S@B, 2) - np.exp(-lt)) < 1e-12
pred("I5", ok)

# I6 accumulation
rng = np.random.default_rng(5505); ok = True
for _ in range(2000):
    n = int(rng.integers(1, 9)); K = 1 + rng.exponential(0.3, n)
    eps = rng.exponential(0.01, n); kap = rng.exponential(0.01, n); d0 = rng.uniform(0, 1)
    d = d0
    for i in range(n): d = max(d - eps[i] - kap[i], 0)/K[i]
    Mp = np.concatenate([[1], np.cumprod(K)])
    bound = max(d0 - np.sum(Mp[:-1]*(eps + kap)), 0)/Mp[-1]
    ok &= d >= bound - 1e-14
pred("I6", ok)
log(f"SUMMARY met={8-len(fails)} failed={len(fails)} {fails}")
raise SystemExit(1 if fails else 0)
