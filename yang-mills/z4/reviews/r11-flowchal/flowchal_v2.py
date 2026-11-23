"""r11-flowchal (v2: only change = projector/pseudo-inverse via eigh, predicates unchanged): independent reproduction of C4/Z4 flow statements T1-T6.

Predicates (fixed before first run):
 P1  T1: full-flow normalized form at tau=6, 40-digit Decimal, equals -0.00986495781679569
     to all printed digits: |ours - printed| < 1e-17 (one unit of the last printed digit).
 P2  T2: spatial-flow form at tau=6 equals 0.0573332378047662: |diff| < 1e-16 (one unit last digit).
 P3a 4^4 lattice: projector d pinv(d) restricted to 12-plaquettes equals the L=4 formula
     (q1^2+q2^2)/A kernel: max abs diff < 1e-10 (float64 eigen/pinv roundoff ~1e-13 on 1536-dim).
 P3b full flow tau=0.7: d expm(-tau d^T d) pinv(d) P (...)^T on 12-plaquettes equals formula with
     exp(-2 tau A): max abs diff < 1e-10.
 P3c spatial flow tau=0.7 (link flow by spatial plaquettes only) equals formula with exp(-2 tau S),
     denominator A: max abs diff < 1e-10.
 P4a full form numerator N(tau)=K2^2-2K3^2+K4^2 over 32*16^-8 e^{-6 tau a} 2cos3w(cos w-1) -> 1:
     |ratio-1| < 1e-3 at tau=50 (next correction ~ e^{-2 tau a} ~ 3e-7).
 P4b smallest tau where full form < 0: MEASURED ONLY (bisection, float64 difference form).
 P4c spatial form > 0 for all tau in grid 0,0.05,...,50 (1001 cases): count of positive cases = 1001.
 P5  continuum (a),(b) by numerical quadrature at t=1: rel diff < 1e-8 (trapezoid on smooth decaying
     integrand, fine grid); (c) ratios exact by rational arithmetic.
 P6  spectral exponents by quadrature: log-log slope of mass(eps) for eps in [1e-3,1e-2]:
     |slope-8| < 0.05 (point), |slope-5| < 0.05 (zero momentum). tolerance: e^{-4tp^2} corrections O(eps^2).
"""
import sys, math, itertools
from decimal import Decimal as D, getcontext
import numpy as np

getcontext().prec = 45
L = 16
out = open(sys.argv[1], "x")
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.write(s + "\n"); out.flush()
fails = []
def pred(name, ok, info):
    log(f"[{'PASS' if ok else 'FAIL'}] {name}: {info}")
    if not ok: fails.append(name)

# ---- Decimal pi, cos, exp
def dpi():
    getcontext().prec += 10
    def atan_inv(x):
        x = D(x); s = D(0); t = 1 / x; k = 0; x2 = x * x
        while True:
            term = t / (2 * k + 1)
            if term == 0 or abs(term) < D(10) ** (-(getcontext().prec + 2)): break
            s += term if k % 2 == 0 else -term
            t /= x2; k += 1
        return s
    p = 16 * atan_inv(5) - 4 * atan_inv(239)
    getcontext().prec -= 10
    return +p
PI = dpi()
def dcos(x):
    getcontext().prec += 10
    s = D(1); t = D(1); x2 = x * x; k = 0
    while True:
        k += 2; t = -t * x2 / (k * (k - 1))
        if abs(t) < D(10) ** (-(getcontext().prec + 2)): break
        s += t
    getcontext().prec -= 10
    return +s

cosk = [dcos(2 * PI * l / L) for l in range(L)]
q2 = [2 - 2 * c for c in cosk]
cosnk = [[dcos(n * 2 * PI * l / L) for l in range(L)] for n in range(5)]

def Kdec(tau, spatial):
    tau = D(tau)
    E = [(-2 * tau * x).exp() for x in q2]
    K = [D(0)] * 5
    for l1, l2, l3, l4 in itertools.product(range(L), repeat=4):
        if l1 == l2 == l3 == l4 == 0: continue
        num = q2[l1] + q2[l2]
        if num == 0: continue
        A = num + q2[l3] + q2[l4]
        e = E[l1] * E[l2] * E[l3] * (1 if spatial else E[l4])
        w = num / A * e
        for n in range(5): K[n] += w * cosnk[n][l4]
    return [k / D(L) ** 4 for k in K]

def form(K): return (K[2] ** 2 - 2 * K[3] ** 2 + K[4] ** 2) / K[0] ** 2

# ---------- T1, T2
Kf = Kdec(6, False); Rf = form(Kf)
log("T1 K_full(0..4) tau=6:", [f"{k:.25e}" for k in Kf]); log("T1 R_full =", f"{Rf:.30f}")
pred("P1", abs(Rf - D("-0.00986495781679569")) < D("1e-17"), f"diff={Rf - D('-0.00986495781679569'):.3e}")
Ks = Kdec(6, True); Rs = form(Ks)
log("T2 K_spat(0..4) tau=6:", [f"{k:.25e}" for k in Ks]); log("T2 R_spat =", f"{Rs:.30f}")
pred("P2", abs(Rs - D("0.0573332378047662")) < D("1e-16"), f"diff={Rs - D('0.0573332378047662'):.3e}")

# ---------- T3 on 4^4
def build_d(N):
    V = N ** 4
    idx = lambda x: sum(x[i] * N ** i for i in range(4))
    link = lambda x, mu: mu * V + idx(x)
    planes = [(m, n) for m in range(4) for n in range(m + 1, 4)]
    d = np.zeros((6 * V, 4 * V)); spat = np.zeros(6 * V, bool)
    for x in itertools.product(range(N), repeat=4):
        for pi_, (m, n) in enumerate(planes):
            r = pi_ * V + idx(x)
            xm = list(x); xm[m] = (xm[m] + 1) % N
            xn = list(x); xn[n] = (xn[n] + 1) % N
            d[r, link(x, m)] += 1; d[r, link(xn, m)] -= 1
            d[r, link(x, n)] -= 1; d[r, link(xm, n)] += 1
            spat[r] = (n != 3)
    return d, spat, idx, V
N = 4
d, spat, idx, V = build_d(N)
# v2: run1 used np.linalg.pinv (default rcond) -> non-symmetric P (own defect). Use eigh with cutoff 1e-8
# (nonzero eigenvalues of d d^T on 4^4 are >= 2-2cos(pi/2)=2; zero ones are O(1e-13)).
lamP, UP = np.linalg.eigh(d @ d.T); UPe = UP[:, lamP > 1e-8]; P = UPe @ UPe.T
lamL, UL = np.linalg.eigh(d.T @ d); keep = lamL > 1e-8
def pinv_d():  # d^+ = (d^T d)^+ d^T
    return (UL[:, keep] / lamL[keep]) @ UL[:, keep].T @ d.T
def formula_L(N, tau, mode):
    """kernel K(x) for 12-plaquettes on N^4 lattice, x = displacement (4-tuple)"""
    ks = 2 * np.pi * np.arange(N) / N; qq = 2 - 2 * np.cos(ks)
    Q = np.meshgrid(qq, qq, qq, qq, indexing="ij"); A = sum(Q)
    num = Q[0] + Q[1]
    with np.errstate(invalid="ignore", divide="ignore"):
        w = np.where(A > 0, num / A, 0.0)
    if mode == "full": w = w * np.exp(-2 * tau * A)
    if mode == "spat": w = w * np.exp(-2 * tau * (Q[0] + Q[1] + Q[2]))
    return np.real(np.fft.ifftn(w))  # (1/N^4) sum_k w e^{ikx}
def compare(M, ker):
    rows = np.arange(V)  # plane index 0 = (0,1) = orientation 12
    sub = M[np.ix_(rows, rows)]
    err = 0.0
    for x in itertools.product(range(N), repeat=4):
        i = idx(x)
        for y in itertools.product(range(N), repeat=4):
            dx = tuple((y[k] - x[k]) % N for k in range(4))
            err = max(err, abs(sub[i, idx(y)] - ker[dx]))
    return err
e = compare(P, formula_L(N, 0, "none"))
pred("P3a", e < 1e-10, f"max|P_num - (q1^2+q2^2)/A kernel| = {e:.2e}; rank d = {np.linalg.matrix_rank(d)}")
tau = 0.7
dtd = d.T @ d
lam, U = np.linalg.eigh(dtd)
flow = (U * np.exp(-tau * lam)) @ U.T
dp = pinv_d()
Ft = d @ flow @ dp
e = compare(Ft @ P @ Ft.T, formula_L(N, tau, "full"))
pred("P3b", e < 1e-10, f"full flow tau=0.7 max diff = {e:.2e}")
# also wrong-factor alternative exp(-tau A) must fail (sensitivity)
e_alt = compare(Ft @ P @ Ft.T, formula_L(N, tau / 2, "full"))
log(f"  sensitivity: with exp(-tau A) instead of exp(-2tau A): diff = {e_alt:.2e}")
ds = d * spat[:, None]
lam, U = np.linalg.eigh(ds.T @ ds)
flows = (U * np.exp(-tau * lam)) @ U.T
Fs = d @ flows @ dp
e = compare(Fs @ P @ Fs.T, formula_L(N, tau, "spat"))
pred("P3c", e < 1e-10, f"spatial flow tau=0.7 max diff = {e:.2e}")
# check gauge invariance used: ds @ d-image of gradients is zero, temporal links not flowed
log(f"  temporal links untouched by spatial flow: max|flows-1| on temporal block = {np.abs(flows[3*V:,3*V:]-np.eye(V)).max():.2e}")

# ---------- T4
w = math.pi / 8; a = 2 - 2 * math.cos(w)
log(f"T4 sign factor 2cos3w(cos w-1) = {2*math.cos(3*w)*(math.cos(w)-1):.6e}")
for t in (20, 30, 50):
    K = Kdec(t, False)
    N_ = K[2] ** 2 - 2 * K[3] ** 2 + K[4] ** 2
    pred_ = D(32) / D(16) ** 8 * (D(-6 * t) * D(a)).exp() * D(2 * math.cos(3 * w) * (math.cos(w) - 1))
    r = N_ / pred_
    log(f"  tau={t}: N/leading = {r:.12f}")
    if t == 50: pred("P4a", abs(r - 1) < D("1e-3"), f"ratio at 50 = {r:.10f}")
ks = 2 * np.pi * np.arange(L) / L; qq = 2 - 2 * np.cos(ks)
Q = np.meshgrid(qq, qq, qq, qq, indexing="ij"); A = sum(Q); num = Q[0] + Q[1]
with np.errstate(invalid="ignore", divide="ignore"):
    W0 = np.where(A > 0, num / A, 0.0)
c = [np.cos(n * ks)[None, None, None, :] for n in range(5)]
def form_np(t, mode):
    ex = np.exp(-2 * t * (A if mode == "full" else Q[0] + Q[1] + Q[2]))
    Wt = W0 * ex
    K = [np.sum(Wt * c[n]) for n in range(5)]
    d23 = np.sum(Wt * (c[2] - c[3])); d34 = np.sum(Wt * (c[3] - c[4]))
    return (d23 * (K[2] + K[3]) - d34 * (K[3] + K[4])) / K[0] ** 2
log(f"  float64 check at tau=6: full {form_np(6,'full'):.15e}, spat {form_np(6,'spat'):.15e}")
grid = np.arange(0, 50.0001, 0.05)
fv = np.array([form_np(t, "full") for t in grid])
neg = np.where(fv < 0)[0]
log(f"  full form at tau=0: {fv[0]:.6e}; first grid tau with form<0: {grid[neg[0]] if len(neg) else None}; "
    f"negative for all later grid points: {bool(len(neg) and np.all(fv[neg[0]:] < 0))}")
lo, hi = grid[neg[0] - 1], grid[neg[0]]
for _ in range(60):
    mid = (lo + hi) / 2
    if form_np(mid, "full") < 0: hi = mid
    else: lo = mid
log(f"P4b MEASURED: smallest tau with full form < 0 = {hi:.6f} (to 2 digits {hi:.2g})")
sv = np.array([form_np(t, "spat") for t in grid])
npos = int(np.sum(sv > 0))
pred("P4c", npos == len(grid), f"spatial form > 0 in {npos}/{len(grid)} grid cases; min = {sv.min():.4e} at tau={grid[sv.argmin()]}")

# ---------- T5 quadrature at t=1
t = 1.0
p = np.linspace(0, 12, 400001); dp_ = p[1] - p[0]
trap = lambda f: dp_ * (np.sum(f) - 0.5 * (f[0] + f[-1]))
# (a): (1/4)*6 * int d^4k/(2pi)^4 e^{-2tk^2}; 4D measure 2pi^2 k^3 dk/(2pi)^4
Ia = 1.5 * trap(2 * np.pi ** 2 * p ** 3 * np.exp(-2 * t * p ** 2)) / (2 * np.pi) ** 4
# (b): k4 integral numerically too: int dk4/(2pi) 1/(p^2+k4^2) done by quadrature for check at p=1
k4 = np.linspace(-4000, 4000, 4000001); g = 1 / (1 + k4 ** 2)
Ik4 = (k4[1] - k4[0]) * (np.sum(g) - 0.5 * (g[0] + g[-1])) / (2 * np.pi)
log(f"T5 k4-integral at p=1: {Ik4:.8f} vs 1/2 (tail 1/(pi*4000)={1/(np.pi*4000):.2e})")
Ib = (2 / 3) * trap(4 * np.pi * p ** 2 * p ** 2 / (2 * p + 1e-300) * np.exp(-2 * t * p ** 2)) / (2 * np.pi) ** 3
ea, eb = 3 / (128 * np.pi ** 2), 1 / (48 * np.pi ** 2)
pred("P5", abs(Ia / ea - 1) < 1e-8 and abs(Ib / eb - 1) < 1e-8,
     f"(a) {Ia:.12e} vs 3/(128pi^2)={ea:.12e}; (b) {Ib:.12e} vs 1/(48pi^2)={eb:.12e}")
from fractions import Fraction as Fr
spat_mag = Fr(3, 2) * Fr(1, 48); full_B3 = Fr(1, 2) * Fr(1, 64); full_mag = Fr(3, 2) * full_B3; full_tot = Fr(3, 128)
log(f"T5c (units 1/(pi^2 t^2)): spatial mag {spat_mag}, full mag {full_mag}, full total {full_tot}; "
    f"ratios {spat_mag/full_mag}, {spat_mag/full_tot}")
log(f"   decimals: spat mag {float(spat_mag)/math.pi**2:.10f}, full mag {float(full_mag)/math.pi**2:.10f}, full tot {float(full_tot)/math.pi**2:.10f}")

# ---------- T6 spectral exponents (t=1); angular weight averaged: <k1^2+k2^2> = 2p^2/3, <(k1^2+k2^2)^2> = 8p^4/15
def mu1(pp): return 4 * np.pi * pp ** 2 * (2 * pp ** 2 / 3) / (2 * pp + 1e-300) * np.exp(-2 * pp ** 2)  # one-particle density
def mass_point(eps):
    # density of E=p+p' : int_0^E mu1(p) mu1(E-p) dp ; mass = int_0^eps
    Es = np.linspace(0, eps, 2001)
    rho = []
    for E in Es:
        pp = np.linspace(0, E, 2001); f = mu1(pp) * mu1(E - pp)
        rho.append((pp[1] - pp[0]) * (f.sum() - 0.5 * (f[0] + f[-1])) if E > 0 else 0.0)
    rho = np.array(rho); return (Es[1] - Es[0]) * (rho.sum() - 0.5 * (rho[0] + rho[-1]))
def mass_zero(eps):
    pp = np.linspace(0, eps / 2, 20001)
    f = 4 * np.pi * pp ** 2 * (8 * pp ** 4 / 15) / (4 * pp ** 2 + 1e-300) * np.exp(-4 * pp ** 2)
    return (pp[1] - pp[0]) * (f.sum() - 0.5 * (f[0] + f[-1]))
e1, e2 = 1e-3, 1e-2
s_pt = math.log(mass_point(e2) / mass_point(e1)) / math.log(e2 / e1)
s_z = math.log(mass_zero(e2) / mass_zero(e1)) / math.log(e2 / e1)
pred("P6", abs(s_pt - 8) < 0.05 and abs(s_z - 5) < 0.05, f"slopes point {s_pt:.5f}, zero-momentum {s_z:.5f}")
log("FAILED predicates:", fails if fails else "none")
out.close()
sys.exit(1 if fails else 0)
