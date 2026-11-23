"""mc.py -- y1-rect (T194). Own SU(2) 4D Wilson Monte Carlo, numpy only, 1 core, fixed seed.
Usage: python3 mc.py OUTFILE L beta n_therm n_meas seed

Weight exp(beta * sum_p (1/2)Tr U_p); links as unit quaternions; checkerboard
(direction, parity) heatbath with Kennedy-Pendleton sampling of a0.
Measured per configuration: W11 = mean (1/2)Tr U_p over all sites and 6 planes;
W12 = mean (1/2)Tr of the 1x2 rectangle over all sites and all 12 ordered (long, short) pairs.
Errors: binned (bins of 1/20 of the measured series), standard error of bin means.

Predicates fixed before the first run:
 M1 (per beta) W12 > 0 with significance W12/err > 5. (Tolerance: 5 sigma, my choice.)
 M2 (beta=0.5 only) |W11 - u| < 3 err + 4u^5 and |W12 - u^2| < 3 err + 10 u^6 with
    u = I2/I1(0.5) = 0.12371793 (from analytic.py); 4u^5, 10u^6 = generous allowance for the
    first strong-coupling corrections (coefficients my estimate, not derived).
 M3 (per beta) W12 < W11 (expectation, not a theorem).
 M4 (measured only) comparison with weak-coupling LO 1-3/(4beta), 1-1.7245*3/(4beta).
Exit code 0 if all applicable predicates met, 1 otherwise.
"""
import sys, numpy as np, math

def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return np.stack([a0*b0 - a1*b1 - a2*b2 - a3*b3,
                     a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1,
                     a0*b3 + a1*b2 - a2*b1 + a3*b0])
def qconj(a): return a * np.array([1, -1, -1, -1]).reshape((4,) + (1,)*(a.ndim-1))
def sh(a, mu, s):  # value at x + s*e_mu ; array axes: comp, x0..x3
    return np.roll(a, -s, axis=1+mu)

out_path, L, beta, nth, nme, seed = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
rng = np.random.default_rng(seed)
U = np.zeros((4, 4, L, L, L, L)); U[:, 0] = 1.0   # U[mu] = quaternion field
par = np.indices((L,)*4).sum(0) % 2

def staple(mu):
    K = np.zeros((4, L, L, L, L))
    for nu in range(4):
        if nu == mu: continue
        Un, Um = U[nu], U[mu]
        K += qmul(qmul(sh(Un, mu, 1), qconj(sh(Um, nu, 1))), qconj(Un))
        b = sh(Un, nu, -1)
        K += qmul(qmul(qconj(sh(b, mu, 1)), qconj(sh(Um, nu, -1))), b)
    return K

def sample_a0(alpha):
    n = alpha.size; res = np.empty(n); todo = np.arange(n)
    while todo.size:
        al = alpha[todo]
        r1, r2, r3, r4 = rng.random((4, todo.size))
        x1 = -np.log(1 - r1)/al; x2 = -np.log(1 - r2)/al
        d = x2 + x1*np.cos(2*np.pi*r3)**2
        acc = (r4**2 <= 1 - d/2)
        res[todo[acc]] = 1 - d[acc]; todo = todo[~acc]
    return res

def sweep():
    for mu in range(4):
        for p in (0, 1):
            K = staple(mu)
            m = (par == p)
            Kp = K[:, m]; k = np.sqrt((Kp**2).sum(0))
            V = Kp/k
            a0 = sample_a0(beta*k)
            v = rng.normal(size=(3, a0.size)); v /= np.sqrt((v**2).sum(0))
            W = np.vstack([a0, v*np.sqrt(np.maximum(0, 1 - a0**2))])
            # action term for this link: Re(U K) (K = sum of closing staples); set U = W conj(V)
            # => Re(W conj(V) V k) = k W0, so W0 has density ~ sqrt(1-W0^2) exp(beta k W0)
            Unew = qmul(W, qconj(V))
            U[mu][:, m] = Unew

def measure():
    w11 = 0.0; w12 = 0.0; n11 = 0; n12 = 0
    for mu in range(4):
        for nu in range(4):
            if nu == mu: continue
            # plaquette (mu,nu) counted once per unordered pair
            if mu < nu:
                P = qmul(qmul(U[mu], sh(U[nu], mu, 1)), qmul(qconj(sh(U[mu], nu, 1)), qconj(U[nu])))
                w11 += P[0].mean(); n11 += 1
            # rectangle: 2 steps mu, 1 step nu, 2 back mu, 1 back nu
            a = qmul(U[mu], sh(U[mu], mu, 1))
            b = qmul(a, sh(sh(U[nu], mu, 2), mu, 0))
            c = qmul(b, qconj(sh(sh(U[mu], mu, 1), nu, 1)))
            d = qmul(c, qconj(sh(U[mu], nu, 1)))
            e = qmul(d, qconj(U[nu]))
            w12 += e[0].mean(); n12 += 1
    return w11/n11, w12/n12

def is_unit():
    return np.max(np.abs((U**2).sum(1) - 1))

for i in range(nth): sweep()
series = []
for i in range(nme):
    sweep(); series.append(measure())
series = np.array(series)
nb = 20; bl = len(series)//nb
bm = series[:bl*nb].reshape(nb, bl, 2).mean(1)
mean = bm.mean(0); err = bm.std(0, ddof=1)/math.sqrt(nb)
u = None
fails = []
with open(out_path, "x") as f:
    def log(s): print(s); f.write(s + "\n")
    log(f"L={L} beta={beta} therm={nth} meas={nme} seed={seed} unitarity_dev={is_unit():.2e}")
    log(f"W11 = {mean[0]:.6f} +- {err[0]:.6f}")
    log(f"W12 = {mean[1]:.6f} +- {err[1]:.6f}")
    if not mean[1]/err[1] > 5: fails.append("M1")
    log(f"M1 W12/err = {mean[1]/err[1]:.1f}")
    if abs(beta - 0.5) < 1e-12:
        u = 0.12371793
        ok1 = abs(mean[0]-u) < 3*err[0] + 4*u**5; ok2 = abs(mean[1]-u*u) < 3*err[1] + 10*u**6
        log(f"M2 W11-u = {mean[0]-u:+.6f}, W12-u^2 = {mean[1]-u*u:+.6f} -> {ok1 and ok2}")
        if not (ok1 and ok2): fails.append("M2")
    if not mean[1] < mean[0]: fails.append("M3")
    log(f"M4 weak LO: W11 {1-0.75/beta:.4f}, W12 {1-1.7245*0.75/beta:.4f}")
    log(f"FAILED: {fails if fails else 'none'}")
sys.exit(1 if fails else 0)
