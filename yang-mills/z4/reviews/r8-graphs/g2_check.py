"""G2 known-answer test (r8-graphs challenger). Predicates fixed BEFORE first run.

Model: three independent Gaussian colour components of the flux through a square,
Phi_a(t), a=1..3, each with covariance K(t) (K = Z4's g-independent flux kernel G).
SU(2) at Gaussian order: (1/2)Tr W = cos(g|Phi|/2), beta = 4/g^2.

P0 (control, known answer): int_{-pi}^{pi} dk/2pi e^{ikn}/(a+4 sin^2(k/2)) = e^{-En}/(2 sinh E),
    cosh E = 1 + a/2, for a=0.7, n=0..3. Tolerance 1e-10 (quadrature with 4096 midpoint
    nodes of a periodic analytic integrand converges exponentially; 1e-10 is far above it).
P1: Monte Carlo (seed 20261123, 4e6 samples), g = 0.1, K0 = 1, K(t) in {0.3, 0.6}:
    beta^2 Cov(cos(g|Phi0|/2), cos(g|Phit|/2)) / (1.5 K^2) within 1 +- tol,
    tol = 4 standard errors (MC) + 3 g^2 K0 (bound on next order relative bias: next
    cosine term is O(g^2 |Phi|^2) relative). Tests D4's coefficient 3/2 with K = G.
P1b: the same with K replaced by g^2 G must FAIL (ratio off by g^-4) -- i.e. the 3/2 is
    tied to K=G. Predicate: |ratio_alt - 1| > 0.5.
P2: Order-difference observable O = eps_abc Phi1_a Phi2_b Phi3_c (leading term of
    (1/2)Tr(W1W2W3) - (1/2)Tr(W3W2W1) up to a constant factor). For a random positive-definite
    6x6 covariance of (Phi1,Phi2,Phi3 at time 0, same at time t), per colour identical and
    colours independent, E[O(0) O(t)] = 6 det Kx, Kx = 3x3 cross-time block.
    MC 4e6 samples, tolerance 4 SE.
P3: Free lattice flux kernel for D4's setting (4D isotropic Euclidean lattice, integer time n):
    K4(n) = int_{BZ^3} d^3k/(2pi)^3 |f_R(k)|^2 (khat1^2+khat2^2) e^{-E n}/(2 sinh E),
    cosh E = 1 + khat_s^2/2;  Hamiltonian (continuous time, Z4's D_t):
    KH(t) = int |f_R|^2 (khat1^2+khat2^2) e^{-t khat}/(2 khat).
    |f_R|^2 = prod_{i=1,2} sin^2(R k_i/2)/sin^2(k_i/2).  R = 1, 2; n = t = 1..4.
    P3a: grid convergence: relative change between M=96 and M=160 midpoint grids < 1e-3
         for n >= 1 (tolerance: integrand has a |k| cusp at 0 times k^2 -> O(M^-4)-ish;
         1e-3 is a loose engineering tolerance, I state it as my expectation).
    P3b: K4(n) > 0 and strictly decreasing in n for both R.
    P3c: |K4(n)/KH(n) - 1| strictly decreasing in n (both kernels share the IR limit).
    P3d (expectation): K4(1)/KH(1) differs from 1 by more than 5% (the two time
         conventions are not interchangeable at cutoff-scale separations).
Measured only: values of K, 1.5 K^2, 6 det K for the three-plaquette row geometry.
Result file: results_g2_<timestamp>.txt, never overwritten (exclusive create).
"""
import numpy as np, time, sys, os

out = []
fails = []
def rec(name, ok, msg):
    out.append(f"{name}: {'MET' if ok else 'FAILED'} | {msg}")
    if not ok: fails.append(name)
def meas(msg): out.append("MEASURED: " + msg)

# P0
a = 0.7; E = np.arccosh(1 + a/2); Mq = 4096
k = -np.pi + (np.arange(Mq)+0.5)*2*np.pi/Mq
ok = True; worst = 0
for n in range(4):
    num = np.mean(np.cos(k*n)/(a + 4*np.sin(k/2)**2))
    ex = np.exp(-E*n)/(2*np.sinh(E)); worst = max(worst, abs(num-ex))
rec("P0", worst < 1e-10, f"max err {worst:.2e}")

rng = np.random.default_rng(20261123)
S = 4_000_000
# P1
g = 0.1; beta = 4/g**2
for Kt in (0.3, 0.6):
    Z1 = rng.standard_normal((S, 3)); Z2 = rng.standard_normal((S, 3))
    X = Z1; Y = Kt*Z1 + np.sqrt(1-Kt**2)*Z2
    u = np.cos(g*np.linalg.norm(X, axis=1)/2); v = np.cos(g*np.linalg.norm(Y, axis=1)/2)
    uc = u - u.mean(); vc = v - v.mean(); prod = uc*vc
    cov = prod.mean(); se = prod.std()/np.sqrt(S)
    pred = 1.5*Kt**2/beta**2
    ratio = cov/pred; tol = 4*se/pred + 3*g**2
    rec(f"P1(K={Kt})", abs(ratio-1) < tol, f"beta^2 Cov={cov*beta**2:.5f} pred 1.5K^2={1.5*Kt**2:.5f} ratio={ratio:.4f} tol={tol:.4f}")
    Kalt = g**2*Kt  # if 'K' meant g^2 G
    ratio_alt = cov/(1.5*Kalt**2/beta**2)
    rec(f"P1b(K={Kt})", abs(ratio_alt-1) > 0.5, f"ratio with K=g^2G: {ratio_alt:.3e}")
    # mean-normalized covariance
    meas(f"K={Kt}: mean-normalized Cov/M^2 * beta^2 = {cov/u.mean()/v.mean()*beta**2:.5f} (O(1/beta^2), not 1/beta)")

# P2
A = rng.standard_normal((6, 6)); C6 = A@A.T/6 + 0.5*np.eye(6)
L = np.linalg.cholesky(C6)
Kx = C6[:3, 3:]
acc = [];
chunks = 8; n = S//chunks
vals = []
for _ in range(chunks):
    Z = rng.standard_normal((n, 3, 6)) @ L.T  # colours a=0..2, 6 variables
    P = Z  # P[:, a, i]
    def eps(p1, p2, p3):
        return np.einsum('sa,sb,sc,abc->s', p1, p2, p3, LC)
    LC = np.zeros((3, 3, 3))
    for (i, j, l), s in {(0,1,2):1,(1,2,0):1,(2,0,1):1,(0,2,1):-1,(2,1,0):-1,(1,0,2):-1}.items(): LC[i,j,l]=s
    O0 = eps(P[:,:,0], P[:,:,1], P[:,:,2]); Ot = eps(P[:,:,3], P[:,:,4], P[:,:,5])
    vals.append(O0*Ot)
vals = np.concatenate(vals)
m = vals.mean(); se = vals.std()/np.sqrt(len(vals)); pred = 6*np.linalg.det(Kx)
rec("P2", abs(m-pred) < 4*se, f"E[O0 Ot]={m:.4f} 6detK={pred:.4f} SE={se:.4f}")

# P3
def kernels(R, M, times):
    k1 = -np.pi + (np.arange(M)+0.5)*2*np.pi/M
    K1, K2, K3 = np.meshgrid(k1, k1, k1, indexing='ij')
    h = lambda q: 4*np.sin(q/2)**2
    hs = h(K1)+h(K2)+h(K3)
    f2 = (np.sin(R*K1/2)**2/np.sin(K1/2)**2)*(np.sin(R*K2/2)**2/np.sin(K2/2)**2)
    w = f2*(h(K1)+h(K2))
    En = np.arccosh(1+hs/2); kh = np.sqrt(hs)
    K4 = [np.mean(w*np.exp(-En*t)/(2*np.sinh(En))) for t in times]
    KH = [np.mean(w*np.exp(-kh*t)/(2*kh)) for t in times]
    return np.array(K4), np.array(KH)
times = [1, 2, 3, 4]
res = {}
for R in (1, 2):
    a4, aH = kernels(R, 96, times); b4, bH = kernels(R, 160, times)
    rel = max(np.max(np.abs(a4/b4-1)), np.max(np.abs(aH/bH-1)))
    rec(f"P3a(R={R})", rel < 1e-3, f"max rel change M=96->160: {rel:.2e}")
    rec(f"P3b(R={R})", bool(np.all(b4 > 0) and np.all(np.diff(b4) < 0)), f"K4(n)={np.array2string(b4, precision=6)}")
    d = np.abs(b4/bH-1)
    rec(f"P3c(R={R})", bool(np.all(np.diff(d) < 0)), f"|K4/KH-1|={np.array2string(d, precision=4)}")
    rec(f"P3d(R={R})", d[0] > 0.05, f"K4(1)/KH(1)={b4[0]/bH[0]:.4f}")
    meas(f"R={R}: KH(t)={np.array2string(bH, precision=6)}; (3/2)K4(n)^2={np.array2string(1.5*b4**2, precision=8)}")
    res[R] = (b4, bH)
# equal-time variance for unit plaquette (n=0) in 4D: <theta^2>/g^2 per colour; known 1/4*... measured only
a0, _ = kernels(1, 160, [0])
meas(f"R=1 K4(0) (per-colour equal-time flux variance, lattice units) = {a0[0]:.6f} (exact free value 1/4 for theta_12 with 4D Feynman propagator -> check: 2*(1/4)... see notes)")
summary = f"met={sum(1 for o in out if ': MET' in o)} failed={len(fails)} measured={sum(1 for o in out if o.startswith('MEASURED'))}"
out.append(summary)
fn = f"results_g2_{time.strftime('%Y%m%d_%H%M%S')}.txt"
with open(fn, 'x') as fh: fh.write("\n".join(out)+"\n")
print("\n".join(out)); print("written", fn)
sys.exit(1 if fails else 0)
