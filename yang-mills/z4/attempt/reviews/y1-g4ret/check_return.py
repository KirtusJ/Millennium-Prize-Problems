"""y1-g4ret: independent checks of return.md (items a, b, d, e).

Predicates (fixed before the first run):
 R1  p_k(theta), k = 6*3.399810242, by composite Simpson (my method; not Gauss-Legendre) with
     n = 20000 and 40000 panels agree to 1e-11, and equal the target's printed values
     0.003072388, 0.156180437, 0.934803630 to 6e-10 (half a unit in the 9th printed decimal + 1e-10 quadrature slack).
 R2  C = pi^2 sqrt(e)/4 and for k in a grid [0, 1e4]: e^{-k} Z(k) >= 8/(3 pi^3 sqrt e) (1+k)^{-3/2}
     (Z normalised by Haar, Z = (2/pi) int sin^2 r e^{k cos r} dr) and p_k(theta) <= min(1, C (1+k)^{3/2} theta^3)
     on a theta grid. Tolerance 1e-12 relative (float64 + Simpson error).
 R3  (rearrangement) for 400 random (k in [0,60], theta in (0,pi), alpha in [0,pi]) the probability of the
     cap of radius theta centred at angle alpha from v is <= the aligned cap probability, + 1e-12.
     Formula: (2/pi) int_0^theta sin^2 r e^{k cos r cos alpha} sinhc(k sin r sin alpha) dr / Z(k).
 R4  (monotone in k) p_k(theta) nondecreasing in k on grid k = 0..200 step 0.5, for 12 thetas (tol 1e-13).
 R5  (holonomy -> cap, Monte Carlo) 40 random one-link problems: 6 random SU(2) staples, beta in [0,4],
     random fixed parts X, Y of the loop h = X U Y; the conditional probability that d(h,-I) <= theta,
     estimated by 200000 Haar samples with importance weights e^{k u.v}, agrees with the quadrature cap
     formula at alpha = angle(v, -X^{-1} Y^{-1}) within 5 standard errors + 1e-4, and quadrature <= p_{6 beta}(theta).
     Seed 4401.
 R6  dyadic cost: for N in {8,...,2^12}, beta in {0,1,3.4,50}, c in {0.1,1,2}: with theta = c(1+6b)^{-1/2}N^{-4/3}
     and M = 3(N/2)^3, M * C (1+6b)^{3/2} theta^3 == (3C/8) c^3 / N to rel 1e-12, and theta <= pi.
 R7  (operator step, toy) 200 random reversible finite two-slice laws nu (symmetric positive matrix,
     normalised) and random event A: ||R S R|| <= max_{x in A} P(y in A | x), + 1e-12, where S is the
     kernel operator on L^2(marginal). Seed 4402.
"""
import numpy as np

out = open("results_return.txt", "x")
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.write(s + "\n"); out.flush()

fails = []
def pred(name, ok, info=""):
    log(f"{name}: {'MET' if ok else 'FAILED'} {info}")
    if not ok: fails.append(name)

def simpson(f, lo, hi, n):
    x = np.linspace(lo, hi, n + 1); y = f(x); h = (hi - lo) / n
    return h / 3 * (y[0] + y[-1] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum())

def num(theta, k, n=20000):  # scaled by e^{-k}
    return simpson(lambda r: np.sin(r)**2 * np.exp(k*(np.cos(r)-1)), 0, theta, n)

def p(k, theta, n=20000):
    return num(theta, k, n) / num(np.pi, k, n)

# R1
beta = 3.399810242; k = 6*beta
target = {0.05: 0.003072388, 0.2: 0.156180437, 0.6: 0.934803630}
ok = True
for th, tv in target.items():
    a1, a2 = p(k, th, 20000), p(k, th, 40000)
    log(f"  theta={th} p20000={a1:.12f} p40000={a2:.12f} target={tv}")
    ok &= abs(a1-a2) < 1e-11 and abs(a2-tv) < 6e-10
pred("R1", ok)

# R2
C = np.pi**2*np.sqrt(np.e)/4
log(f"  C = {C:.12f}")
ok = True
for kk in np.concatenate([np.linspace(0, 10, 41), np.geomspace(10, 1e4, 30)]):
    zs = (2/np.pi)*num(np.pi, kk, 40000)
    lb = 8/(3*np.pi**3*np.sqrt(np.e))*(1+kk)**-1.5
    ok &= zs >= lb*(1-1e-12)
    for th in np.linspace(0.001, np.pi, 60):
        ok &= p(kk, th, 4000) <= min(1, C*(1+kk)**1.5*th**3) + 1e-12
pred("R2", ok)

# R3
rng = np.random.default_rng(4403)
def cap_off(k, theta, alpha, n=4000):
    def f(r):
        s = k*np.sin(r)*np.sin(alpha)
        sh = np.where(np.abs(s) > 1e-12, np.sinh(np.minimum(s, 700))/np.where(s == 0, 1, s), 1.0)
        # scale by e^{-k}: e^{k cos r cos alpha - k} sinh(s)/s
        return np.sin(r)**2*np.exp(k*np.cos(r)*np.cos(alpha) - k)*sh
    return simpson(f, 0, theta, n)/num(np.pi, k, n)
worst = -np.inf; ok = True
for _ in range(400):
    kk, th, al = rng.uniform(0, 60), rng.uniform(0.01, np.pi), rng.uniform(0, np.pi)
    diff = cap_off(kk, th, al) - p(kk, th, 4000)
    worst = max(worst, diff); ok &= diff <= 1e-12
pred("R3", ok, f"max(off-centre - aligned) = {worst:.3e}")
log(f"  sanity alpha=0 reproduces aligned: {cap_off(5.0,0.7,0.0)-p(5.0,0.7,4000):.2e}")

# R4
ok = True
for th in np.linspace(0.05, 3.1, 12):
    vals = np.array([p(kk, th, 4000) for kk in np.arange(0, 200.5, 0.5)])
    ok &= np.all(np.diff(vals) >= -1e-13)
pred("R4", ok)

# R5  quaternions (w,x,y,z) <-> SU(2); 1/2 Tr(UV) = (u * v) real part; unit-quaternion product.
def qmul(a, b):
    w1, x1, y1, z1 = np.moveaxis(a, -1, 0); w2, x2, y2, z2 = np.moveaxis(b, -1, 0)
    return np.stack([w1*w2-x1*x2-y1*y2-z1*z2, w1*x2+x1*w2+y1*z2-z1*y2,
                     w1*y2-x1*z2+y1*w2+z1*x2, w1*z2+x1*y2-y1*x2+z1*w2], -1)
def qinv(a): return a*np.array([1, -1, -1, -1])
def haar(rng, n): v = rng.normal(size=(n, 4)); return v/np.linalg.norm(v, axis=1, keepdims=True)
rng = np.random.default_rng(4401)
ok = True; maxz = 0
for trial in range(40):
    b = rng.uniform(0, 4); staples = haar(rng, 6); X, Y = haar(rng, 2)
    # Re Tr-part: sum_p 1/2 Tr(U V_p) = u . conj-structure: 1/2Tr(U V) = Re(u v) = u . conj(v)
    Wv = qinv(staples).sum(0)          # Re(u v_p) = <u, conj(v_p)>
    kk = b*np.linalg.norm(Wv); vdir = Wv/np.linalg.norm(Wv)
    th = rng.uniform(0.2, 2.5)
    U = haar(rng, 200000)
    w = np.exp(b*(U @ Wv) - kk)
    h = qmul(qmul(np.broadcast_to(X, U.shape), U), np.broadcast_to(Y, U.shape))
    dist = np.arccos(np.clip(-h[:, 0], -1, 1))     # round distance to -I: cos d = <h, -1>
    ind = dist <= th
    est = (w*ind).sum()/w.sum()
    # SE by ratio delta method
    m = w.mean(); r = w*(ind - est)
    se = np.sqrt((r**2).mean()/len(w))/m
    c = -qmul(qinv(X), qinv(Y))
    alpha = np.arccos(np.clip(c @ vdir, -1, 1))
    quad = cap_off(kk, th, alpha)
    z = abs(est-quad)/(se+1e-300)
    maxz = max(maxz, z if se > 0 else 0)
    ok &= abs(est-quad) <= 5*se + 1e-4 and quad <= p(6*b, th, 4000) + 1e-12 and kk <= 6*b + 1e-12
pred("R5", ok, f"max |MC-quad|/SE = {maxz:.2f}")

# R6
ok = True
for N in [2**j for j in range(3, 13)]:
    for b in (0, 1, 3.4, 50):
        for c in (0.1, 1, 2):
            th = c*(1+6*b)**-0.5*N**(-4/3); M = 3*(N/2)**3
            lhs = M*C*(1+6*b)**1.5*th**3; rhs = 3*C/8*c**3/N
            ok &= abs(lhs-rhs) <= 1e-12*rhs and th <= np.pi
pred("R6", ok)

# R7
rng = np.random.default_rng(4402)
ok = True; worst = -np.inf
for _ in range(200):
    n = int(rng.integers(3, 10)); Wm = rng.uniform(0, 1, (n, n)); Wm = Wm + Wm.T; Wm /= Wm.sum()
    mu = Wm.sum(1); A = rng.random(n) < 0.5
    if not A.any(): A[0] = True
    K = Wm/np.sqrt(np.outer(mu, mu))           # S in orthonormal basis of L^2(mu)
    Rm = np.diag(A.astype(float))
    lhs = np.abs(np.linalg.eigvalsh(Rm@K@Rm)).max()
    rhs = max((Wm[x][A].sum()/mu[x]) for x in np.where(A)[0])
    worst = max(worst, lhs-rhs); ok &= lhs <= rhs + 1e-12
pred("R7", ok, f"max(||RSR|| - row sup) = {worst:.3e}")

log(f"SUMMARY met={7-len(fails)} failed={len(fails)} {fails}")
raise SystemExit(1 if fails else 0)
