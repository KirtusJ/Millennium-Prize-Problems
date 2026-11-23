"""harnack_check.py -- numerical checks of the new inequalities used in HARNACK.md (Lemma H4).

Notation: SU(2) = unit quaternions, a = class angle (geodesic distance to 1), u = vector part,
s = |u| = sin a.  V(x) = 2 beta |u1 x u2|^2.  k(U,U') = exp(beta cos theta)/Z, Z = 2 I1(beta)/beta,
theta = geodesic distance.  Haar = probability measure.

PREDICATES (fixed before the first run; tolerances in brackets with their source):
 P1  I1(z) <= (pi/2) e^z / sqrt(2 pi z) for all z on a log grid in [1e-3, 1e5]   [rel. slack 1e-12: float64 rounding of scipy ive]
 P2  v(r) := (2r - sin 2r)/(2pi) (Haar prob. volume of a geodesic ball of radius r in S^3)
     >= 11 r^3/(24 pi) for r in (0, 1/2]                                           [rel. slack 1e-12: rounding]
     P2b: v(r) agrees with a Monte Carlo Haar estimate at r = 0.3, 0.5 within 4 SE  [4 SE: MC error]
 P3  k(theta) >= sqrt(2/pi) beta^{3/2} exp(-R^2/2) for theta <= R/sqrt(beta),
     beta in {4,16,...,4096}, R in {1,2,3,4}                                       [rel. 1e-12]
 P4  phase 0 (rotate the axis of the link with smaller s, by conjugation, towards the line of
     the other axis): V(t) nonincreasing in t on a 41-point grid, V(1) = 0, path length
     s*psi <= (pi/2) (V/(2beta))^{1/4}; 2e4 random pairs, seed 1                     [abs 1e-12*beta: rounding]
 P5  phase 1 (commuting pair, shrink U2 along its one-parameter subgroup): V(t) = 0;
     phase 3 (U2 grows from 1 to U2(y) along its subgroup, a2(y) <= pi/2): V(t) <= V(y)  [abs 1e-9]
 P6  ball inflation: z with geodesic distance <= rho/sqrt(beta) to p in each link:
     sqrt(V(z)/2) <= sqrt(V(p)/2) + rho (s1(p)+s2(p)) + rho^2/sqrt(beta); 2e4 random, seed 2 [abs 1e-9]
 P7  k_sup = beta e^beta/(2 I1(beta)) <= beta sqrt(2 pi beta)/(2D), D = 1 - 1/(2beta) - sqrt(2pi beta)e^{-beta}/2,
     beta in {2,...,1e5}                                                             [rel 1e-12]
 P8  two-step chain bound, Monte Carlo: T^2(x,y) >= e^{-V(x)/2-V(y)/2} kmin^4 e^{-supV(B1)} v(rho/sqrt b)^2
     for x,y at per-link distance d/sqrt(beta) (d=1, rho=0.5) near the valley, beta in {64, 256};
     MC estimate minus 4 SE must exceed the bound                                    [4 SE: MC error]
MEASURED ONLY: optimal (d, rho) for the per-unit-length chain cost l(K0)/d; the coefficient
 C_tot(eta) of sqrt(beta) in -log g on the junction for eta in {0.05, 0.1, 0.2, 0.4}.
Results go to results_harnack_<tag>.txt opened with mode "x" (never overwritten).
"""
import sys, math
import numpy as np

def _ive1(zz):  # I1(z) e^{-z} = (1/pi) int_0^pi e^{z(cos t - 1)} cos t dt, trapezoid, 400001 nodes
    t = np.linspace(0, math.pi, 400001); c = np.cos(t); out = []
    for z in np.atleast_1d(zz):
        f = np.exp(z * (c - 1)) * c
        out.append((np.sum(f) - 0.5 * (f[0] + f[-1])) * (t[1] - t[0]) / math.pi)
    return np.array(out) if np.ndim(zz) else out[0]
def ive(nu, z):
    assert nu == 1
    return _ive1(z)

tag = sys.argv[1] if len(sys.argv) > 1 else "run1"
out = open(f"results_harnack_{tag}.txt", "x")
def pr(*a):
    s = " ".join(str(x) for x in a); print(s); out.write(s + "\n"); out.flush()
summary = {}
def verdict(name, ok, info=""):
    summary[name] = ok; pr(f"{name}: {'MET' if ok else 'FAILED'} {info}")

# ---------- quaternion helpers ----------
def qmul(p, q):
    a0, a = p[..., 0], p[..., 1:]; b0, b = q[..., 0], q[..., 1:]
    s = a0 * b0 - np.sum(a * b, -1)
    v = a0[..., None] * b + b0[..., None] * a + np.cross(a, b)
    return np.concatenate([s[..., None], v], -1)
def qexp(X):
    th = np.linalg.norm(X, axis=-1)
    with np.errstate(invalid="ignore", divide="ignore"):
        f = np.where(th > 0, np.sin(th) / np.where(th > 0, th, 1), 1.0)
    return np.concatenate([np.cos(th)[..., None], f[..., None] * X], -1)
def geod(p, q):
    return np.arccos(np.clip(np.sum(p * q, -1), -1, 1))
def Vof(U1, U2, beta):
    c = np.cross(U1[..., 1:], U2[..., 1:]); return 2 * beta * np.sum(c * c, -1)
def rand_unit(rng, n):
    v = rng.normal(size=(n, 3)); return v / np.linalg.norm(v, axis=1, keepdims=True)
def rot(v, axis, ang):  # Rodrigues, axis unit
    c, s = np.cos(ang)[..., None], np.sin(ang)[..., None]
    return v * c + np.cross(axis, v) * s + axis * np.sum(axis * v, -1, keepdims=True) * (1 - c)

# ---------- P1 ----------
z = np.logspace(-3, 5, 401)
lhs = ive(1, z)  # I1 e^{-z}
rhs = (math.pi / 2) / np.sqrt(2 * math.pi * z)
r = lhs / rhs
verdict("P1", np.all(r <= 1 + 1e-12), f"max I1/bound = {r.max():.6f} at z={z[r.argmax()]:.3g}; cases {len(z)}")

# ---------- P2 ----------
rr = np.linspace(1e-4, 0.5, 5001)
v = (2 * rr - np.sin(2 * rr)) / (2 * math.pi)
b = 11 * rr ** 3 / (24 * math.pi)
verdict("P2", np.all(v >= b * (1 - 1e-12)), f"min v/bound = {(v/b).min():.6f}; cases {len(rr)}")
rng = np.random.default_rng(0)
ok = True
for r0 in (0.3, 0.5):
    Q = rng.normal(size=(400000, 4)); Q /= np.linalg.norm(Q, axis=1, keepdims=True)
    hit = (np.arccos(np.clip(Q[:, 0], -1, 1)) <= r0).astype(float)
    m, se = hit.mean(), hit.std() / math.sqrt(len(hit))
    ex = (2 * r0 - math.sin(2 * r0)) / (2 * math.pi)
    ok &= abs(m - ex) <= 4 * se
    pr(f"  P2b r={r0}: MC {m:.6f} +- {se:.1e}, formula {ex:.6f}")
verdict("P2b", ok)

# ---------- P3, P7 ----------
ok3 = True; cnt = 0
for beta in [4, 16, 64, 256, 1024, 4096]:
    lkZ = math.log(beta / 2) - math.log(ive(1, beta))  # log(e^beta / Z) - beta... : 1/Z = beta/(2 I1); e^{beta cos th}/Z
    for R in [1, 2, 3, 4]:
        th = np.linspace(0, min(R / math.sqrt(beta), math.pi), 201)
        logk = beta * (np.cos(th) - 1) + lkZ  # since I1 = ive*e^beta
        bnd = 0.5 * math.log(2 / math.pi) + 1.5 * math.log(beta) - R * R / 2
        ok3 &= bool(np.all(logk >= bnd - 1e-12)); cnt += 1
verdict("P3", ok3, f"cases {cnt}")
ok7 = True; worst = 0
for beta in [2, 4, 16, 64, 256, 1024, 4096, 1e5]:
    ksup = beta / (2 * ive(1, beta))
    D = 1 - 1 / (2 * beta) - math.sqrt(2 * math.pi * beta) * math.exp(-beta) / 2
    bd = beta * math.sqrt(2 * math.pi * beta) / (2 * D)
    ok7 &= ksup <= bd * (1 + 1e-12); worst = max(worst, ksup / bd)
verdict("P7", ok7, f"max ksup/bound = {worst:.6f}")

# ---------- P4 phase 0 ----------
rng = np.random.default_rng(1)
n = 20000; beta = 1000.0
a1 = rng.uniform(0, math.pi / 2, n); a2 = rng.uniform(0, math.pi / 2, n)
n1 = rand_unit(rng, n); n2 = rand_unit(rng, n)
s1, s2 = np.sin(a1), np.sin(a2)
V0 = 2 * beta * (s1 * s2) ** 2 * np.sum(np.cross(n1, n2) ** 2, 1)
# rotate the axis of the smaller-s link towards the line of the other axis (sign chosen: angle <= pi/2)
small_is_1 = s1 <= s2
nm = np.where(small_is_1[:, None], n1, n2); nM = np.where(small_is_1[:, None], n2, n1)
sgn = np.sign(np.sum(nm * nM, 1)); sgn[sgn == 0] = 1
tgt = nM * sgn[:, None]
psi = np.arccos(np.clip(np.sum(nm * tgt, 1), -1, 1))  # in [0, pi/2]
ax = np.cross(nm, tgt); axn = np.linalg.norm(ax, axis=1)
ax = np.where(axn[:, None] > 1e-14, ax / np.maximum(axn, 1e-300)[:, None], np.array([1.0, 0, 0]))
prevV = V0.copy(); okmono = True
for t in np.linspace(0, 1, 41):
    nm_t = rot(nm, ax, t * psi)
    u1 = np.where(small_is_1[:, None], nm_t * s1[:, None], n1 * s1[:, None])
    u2 = np.where(small_is_1[:, None], n2 * s2[:, None], nm_t * s2[:, None])
    Vt = 2 * beta * np.sum(np.cross(u1, u2) ** 2, 1)
    okmono &= bool(np.all(Vt <= prevV + 1e-12 * beta)); prevV = Vt
okend = bool(np.all(prevV <= 1e-12 * beta))
sm = np.minimum(s1, s2)
okL = bool(np.all(sm * psi <= (math.pi / 2) * (V0 / (2 * beta)) ** 0.25 + 1e-12))
verdict("P4", okmono and okend and okL, f"mono {okmono}, end V=0 {okend}, length bound {okL}; cases {n}; "
        f"max (s psi)/((pi/2)(V/2b)^(1/4)) = {np.max(sm*psi/np.maximum((math.pi/2)*(V0/(2*beta))**0.25,1e-300)):.4f}")

# ---------- P5 phases 1 and 3 ----------
okp1 = True; okp3 = True
nn = rand_unit(rng, n)
b1 = rng.uniform(0, math.pi, n); b2 = rng.uniform(0, math.pi, n)  # commuting pair along common line
sg = np.where(rng.random(n) < 0.5, 1.0, -1.0)
for t in np.linspace(0, 1, 21):
    U1 = qexp(nn * b1[:, None]); U2 = qexp(sg[:, None] * nn * ((1 - t) * b2)[:, None])
    okp1 &= bool(np.all(Vof(U1, U2, beta) <= 1e-9))
# phase 3: arbitrary y with a2(y) <= pi/2
c1 = rng.uniform(0, math.pi, n); c2 = rng.uniform(0, math.pi / 2, n)
m1 = rand_unit(rng, n); m2 = rand_unit(rng, n)
Uy1 = qexp(m1 * c1[:, None]); Vy = Vof(Uy1, qexp(m2 * c2[:, None]), beta)
for t in np.linspace(0, 1, 41):
    Vt = Vof(Uy1, qexp(m2 * (t * c2)[:, None]), beta)
    okp3 &= bool(np.all(Vt <= Vy + 1e-9))
verdict("P5", okp1 and okp3, f"phase1 V=0 {okp1}, phase3 V<=V(y) {okp3}; cases {n} each")

# ---------- P6 ball inflation ----------
rng = np.random.default_rng(2)
ok6 = True; worst = -1e9; cnt = 0
for beta in [16.0, 256.0, 4096.0]:
    for rho in [0.25, 0.5, 1.0]:
        P1_ = qexp(rand_unit(rng, n) * rng.uniform(0, math.pi, n)[:, None])
        P2_ = qexp(rand_unit(rng, n) * rng.uniform(0, math.pi, n)[:, None])
        # near-valley half: make P2 commute-ish with P1 for half the samples
        h = n // 2
        ax1 = P1_[:h, 1:] / np.maximum(np.linalg.norm(P1_[:h, 1:], axis=1, keepdims=True), 1e-300)
        P2_[:h] = qexp(ax1 * rng.uniform(0, math.pi, h)[:, None] + rng.normal(size=(h, 3)) / math.sqrt(beta))
        r1 = rng.uniform(0, 1, n) ** (1 / 3) * rho / math.sqrt(beta)
        r2 = rng.uniform(0, 1, n) ** (1 / 3) * rho / math.sqrt(beta)
        Z1 = qmul(P1_, qexp(rand_unit(rng, n) * r1[:, None])); Z2 = qmul(P2_, qexp(rand_unit(rng, n) * r2[:, None]))
        lhs = np.sqrt(Vof(Z1, Z2, beta) / 2)
        rhs = np.sqrt(Vof(P1_, P2_, beta) / 2) + rho * (np.linalg.norm(P1_[:, 1:], axis=1) + np.linalg.norm(P2_[:, 1:], axis=1)) + rho ** 2 / math.sqrt(beta)
        ok6 &= bool(np.all(lhs <= rhs + 1e-9)); worst = max(worst, float(np.max(lhs - rhs))); cnt += n
verdict("P6", ok6, f"max(lhs-rhs) = {worst:.3e}; cases {cnt}")

# ---------- P8 two-step chain, Monte Carlo with importance sampling ----------
rng = np.random.default_rng(3)
ok8 = True
for beta in [64.0, 256.0]:
    d, rho = 1.0, 0.5
    logZinv = math.log(beta / 2) - math.log(ive(1, beta)) - beta  # log(1/Z)
    def logk(P, Q): return beta * np.sum(P * Q, -1) + logZinv
    for case in range(3):
        a1 = [0.05, 0.1, 0.3][case]; e3 = np.array([0, 0, 1.0])
        X1 = qexp(e3 * a1); X2 = qexp(np.array([1.0, 0, 0]) * 0.02)
        st = d / math.sqrt(beta)
        Y1 = qmul(X1, qexp(np.array([0, 1.0, 0]) * st)); Y2 = qmul(X2, qexp(np.array([0, 0, 1.0]) * st))
        Vx = float(Vof(X1, X2, beta)); Vy = float(Vof(Y1, Y2, beta))
        # midpoint p_1: geodesic midpoints; ball B1 radius rho/sqrt(beta) around them
        M1 = (X1 + Y1); M1 /= np.linalg.norm(M1); M2 = (X2 + Y2); M2 /= np.linalg.norm(M2)
        N = 400000; sig = 1 / math.sqrt(2 * beta)
        G1 = rng.normal(size=(N, 3)) * sig; G2 = rng.normal(size=(N, 3)) * sig
        Z1 = qmul(np.broadcast_to(M1, (N, 4)), qexp(G1)); Z2 = qmul(np.broadcast_to(M2, (N, 4)), qexp(G2))
        def lq(G):  # log density wrt Haar prob of M*exp(G)
            th = np.linalg.norm(G, axis=1)
            return (-np.sum(G * G, 1) / (2 * sig * sig) - 1.5 * math.log(2 * math.pi * sig * sig)
                    + math.log(2 * math.pi ** 2) - 2 * np.log(np.sinc(th / math.pi)))
        Vz = Vof(Z1, Z2, beta)
        lw = (-Vx / 2 - Vz - Vy / 2 + logk(X1, Z1) + logk(X2, Z2) + logk(Z1, Y1) + logk(Z2, Y2) - lq(G1) - lq(G2))
        mx = lw.max(); w = np.exp(lw - mx)
        est = w.mean(); se = w.std() / math.sqrt(N)
        # bound: sup V on B1 via P6 inequality
        sV = math.sqrt(2) * (math.sqrt(float(Vof(M1, M2, beta)) / 2) + rho * (np.linalg.norm(M1[1:]) + np.linalg.norm(M2[1:])) + rho ** 2 / math.sqrt(beta))
        supV = sV ** 2 / 1.0
        supV = 2 * (sV / math.sqrt(2)) ** 2
        R = d + 2 * rho
        lkmin = 0.5 * math.log(2 / math.pi) + 1.5 * math.log(beta) - R * R / 2
        rb = rho / math.sqrt(beta); lv = math.log(11 * rb ** 3 / (24 * math.pi))
        lbound = -Vx / 2 - Vy / 2 + 4 * lkmin - supV + 2 * lv
        lest_lo = mx + math.log(max(est - 4 * se, 1e-300))
        okc = lest_lo >= lbound
        ok8 &= okc
        pr(f"  P8 beta={beta:.0f} a1={a1}: log T2 (MC) = {mx+math.log(est):.3f} (-4SE: {lest_lo:.3f}), log bound = {lbound:.3f}, gap = {lest_lo-lbound:.2f} nats {'ok' if okc else 'FAIL'}")
verdict("P8", ok8, "cases 6")

# ---------- measured only: constants ----------
def ell(Kp, d, rho):
    return Kp + (d + 2 * rho) ** 2 + math.log(math.pi / 2) + 2 * math.log(24 * math.pi / (11 * rho ** 3))
best = None
for d in np.linspace(0.5, 8, 151):
    for rho in np.linspace(0.05, 0.5, 91):
        K0 = 2 * (2 * rho + rho * rho) ** 2
        c = ell(K0, d, rho) / d
        if best is None or c < best[0]: best = (c, d, rho)
pr(f"MEASURED: min over (d, rho<=1/2) of l(K0)/d = {best[0]:.4f} at d = {best[1]:.3f}, rho = {best[2]:.3f}")
c0, d, rho = best
K = 1.0
KK = 2 * (math.sqrt(K / 2) + 2 * rho + rho * rho) ** 2
pr(f"MEASURED: l(K_K)/d with K = 1: {ell(KK, d, rho)/d:.4f}")
pr("eta, a_-, r0, C_tot = [l0 (2a_- + r0) + lK a_-]/d, C_tot/c*   (c* = 4.6054)")
for eta in [0.05, 0.1, 0.2, 0.4]:
    am = math.asin(math.sinh(eta)); r0 = math.sqrt(eta * math.sin(am) / 4)
    Ct = (ell(2 * (2 * rho + rho * rho) ** 2, d, rho) * (2 * am + r0) + ell(KK, d, rho) * am) / d
    pr(f"  {eta}  {am:.4f}  {r0:.4f}  {Ct:.4f}  {Ct/4.6054:.4f}")
pr("SUMMARY", summary, "met", sum(summary.values()), "failed", sum(not v for v in summary.values()))
out.close()
sys.exit(0 if all(summary.values()) else 1)
