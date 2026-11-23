"""test_c.py -- TEST (iii) for claim (C) of A1_REDUCTION.md (worker a3-C).

Usage: python3 test_c.py <result_file> [res]   res in {1,2}: quadrature resolution
(res=2 doubles every grid; the difference res1-res2 is the stated tolerance).
The result file is opened with mode "x" (never overwritten). No randomness (no seed needed).

Definitions. C(n) = int exp(-n eps) dnu(eps), xi = 1/m, m = bottom of spec(H).
R(xi) := C(xi/2)/C(xi)  [(C) says sup_beta R <= D].
(C') := xi * (1 - C(1)/C(0)) bounded  [sufficient condition, PROOF.md step 4].

Systems.
 F0: free massive scalar, 4D hypercubic lattice, observable phi(0) (lattice-local).
     G(n) by the Schwinger representation G(n)=int_0^inf e^{-a M^2} ive(n,2a) ive(0,2a)^3 da
     (ive = e^{-x} I_n(x)), with M^2 = 2(cosh(1/xi)-1) so that the transfer-matrix gap is exactly 1/xi.
     (The child recomputes R1 by the momentum integral: an independent method.)
 F2: phi(0)^2 - <phi^2>: C2 = 2 G^2.
 FS: slice-smeared phi_s(0)^2 at flow time s*xi^2 (spatial modes damped by exp(-s xi^2 phat^2)):
     C(n) = 2 G_s(n)^2, G_s(n) = (2pi)^-3 int e^{-2 s xi^2 phat^2} e^{-n w}/(2 sinh w) d^3k, s = 0.1.
 H2: two-atom family nu = w delta_m + delta_1, w = exp(-xi/2) (lattice scale 1, gap m=1/xi).
 HH: "hole" family nu = w delta_m + eps^2 1[sqrt(m), 3] d eps, w = m^4: no weight between m and sqrt(m).
 DK: mechanism (d): psi = T^{xi} phi with phi of two-atom type w = exp(-2 xi):
     R_psi = C_phi(2.5 xi)/C_phi(3 xi).

PREDICATES (fixed before the first run).
 P1  F0: R1(xi) <= 10 for all xi in {4,8,16,32,64,128,256} and |R1(256)/5.503975 - 1| < 0.03.
     (5.503975 = 2K1(1/2)/K1(1), continuum; 0.03 = own guess for O(1/xi) lattice + quadrature error.)
 P2  F2: R2 = R1^2 <= 100 for all xi and |R2(256)/30.293739 - 1| < 0.06.
 P3  FS: (C') holds: xi*(1-C(1)/C(0)) <= 20 for all xi in {8,...,256}; R <= (C(0)/C(1))^(xi/2) for all xi
     (log-convexity bound, PROOF.md step 2); R <= e^10 for all xi. (20: own expectation, free M1/M0 ~ c/sqrt(s).)
 P4  F2 (lattice-local): (C') FAILS: xi*(1-C2(1)/C2(0)) at xi=256 is > 10 times its value at xi=16.
 P5  H2: R(xi) >= exp(xi/2)/3 for all xi in {4,...,256} (so (C) fails, unbounded).
 P6  HH: R(4096)/R(64) > 100 ((C) fails for the hole family).
 P7  DK: R_psi(xi) >= exp(xi/2)/3 for all xi (Euclidean-time smearing by one xi does not make (C) automatic).
 P8  measured only: F0 and F2: smallest integer n with log(C(n)/C(n+1)) <= 1.5 * (bottom of the sector)
     (m for F0, 2m for F2); report n/xi.
 Every "for all" is reported with the number of qualifying cases.
"""
import sys, math
import numpy as np

out = sys.argv[1]
res = int(sys.argv[2]) if len(sys.argv) > 2 else 1
f = open(out, "x")
def w(s=""):
    print(s); f.write(s + "\n"); f.flush()

XIS = [4, 8, 16, 32, 64, 128, 256]
NT = 400 * res      # theta points for ive
NA = 3000 * res     # alpha points (log grid)

def ive_vec(ns, x):
    """e^{-x} I_n(x) for array ns, scalar x>0: (1/pi) int_0^pi e^{x(cos t -1)} cos(n t) dt (trapezoid)."""
    tmax = min(math.pi, math.sqrt(80.0 / x))
    t = np.linspace(0.0, tmax, NT + 1)
    g = np.exp(x * (np.cos(t) - 1.0))
    wts = np.full(NT + 1, tmax / NT); wts[0] *= 0.5; wts[-1] *= 0.5
    return (np.cos(np.outer(ns, t)) * g) @ wts / math.pi

def G_schwinger(ns, xi):
    M2 = 2.0 * (math.cosh(1.0 / xi) - 1.0)
    u = np.linspace(math.log(1e-6), math.log(60.0 / M2 + 1e3), NA)
    acc = np.zeros(len(ns))
    du = u[1] - u[0]
    for i, ui in enumerate(u):
        a = math.exp(ui)
        v = ive_vec(np.array(ns, dtype=float), 2 * a)
        i0 = ive_vec(np.array([0.0]), 2 * a)[0]
        term = a * math.exp(-a * M2) * v * i0 ** 3
        acc += term * (0.5 if i in (0, NA - 1) else 1.0)
    return acc * du

def omega(p2, M2):
    return np.arccosh(1.0 + (M2 + p2) / 2.0)

def G_smeared(ns, xi, s):
    M2 = 2.0 * (math.cosh(1.0 / xi) - 1.0)
    K = min(math.pi, 7.0 / (xi * math.sqrt(2 * s)))
    N = 120 * res + 1
    k = np.linspace(-K, K, N)
    h = k[1] - k[0]
    wk = np.full(N, h); wk[0] *= 0.5; wk[-1] *= 0.5   # trapezoid
    s1 = 4 * np.sin(k / 2) ** 2
    p2 = s1[:, None, None] + s1[None, :, None] + s1[None, None, :]
    W = wk[:, None, None] * wk[None, :, None] * wk[None, None, :]
    om = omega(p2, M2)
    base = W * np.exp(-2 * s * xi ** 2 * p2) / (2 * np.sinh(om)) / (2 * math.pi) ** 3
    return np.array([np.sum(base * np.exp(-n * om)) for n in ns])

fails = []; met = []
w(f"# test_c.py res={res} NT={NT} NA={NA}")
# ---------- F0, F2
w("## F0/F2 free lattice-local phi(0), phi(0)^2 (Schwinger)")
w("xi  G(0) G(1) G(xi/2) G(xi)  R1  R2  xi*(1-C2(1)/C2(0))")
R1s, R2s, cp = {}, {}, {}
for xi in XIS:
    G = G_schwinger([0, 1, xi // 2, xi], xi)
    R1 = G[2] / G[3]; R2 = R1 ** 2
    c = xi * (1 - (G[1] / G[0]) ** 2)
    R1s[xi], R2s[xi], cp[xi] = R1, R2, c
    w(f"{xi} {G[0]:.8e} {G[1]:.8e} {G[2]:.8e} {G[3]:.8e} {R1:.6f} {R2:.6f} {c:.4f}")
q1 = sum(R1s[x] <= 10 for x in XIS)
ok1 = q1 == len(XIS) and abs(R1s[256] / 5.503975 - 1) < 0.03
w(f"P1: {q1}/{len(XIS)} cases R1<=10; R1(256)/5.503975-1 = {R1s[256]/5.503975-1:+.5f} -> {'MET' if ok1 else 'FAILED'}")
(met if ok1 else fails).append("P1")
q2 = sum(R2s[x] <= 100 for x in XIS)
ok2 = q2 == len(XIS) and abs(R2s[256] / 30.293739 - 1) < 0.06
w(f"P2: {q2}/{len(XIS)} cases R2<=100; R2(256)/30.293739-1 = {R2s[256]/30.293739-1:+.5f} -> {'MET' if ok2 else 'FAILED'}")
(met if ok2 else fails).append("P2")
ok4 = cp[256] > 10 * cp[16]
w(f"P4: xi(1-C2(1)/C2(0)) at 256 = {cp[256]:.3f}, at 16 = {cp[16]:.3f}, ratio {cp[256]/cp[16]:.3f} -> {'MET' if ok4 else 'FAILED'}")
(met if ok4 else fails).append("P4")
# ---------- P8 measured only
w("## P8 (measured only): first n with discrete m_eff(n) <= 1.5 x bottom of sector")
for xi in [8, 16, 32, 64]:
    ns = list(range(0, 4 * xi + 2))
    G = G_schwinger(ns, xi)
    m = 1.0 / xi
    me1 = np.log(G[:-1] / G[1:]); me2 = 2 * me1
    n1 = next((n for n in range(len(me1)) if me1[n] <= 1.5 * m), None)
    n2 = next((n for n in range(len(me2)) if me2[n] <= 1.5 * 2 * m), None)
    w(f"xi={xi}: F0 n/xi = {n1/xi if n1 is not None else 'none<=4'}; F2 n/xi = {n2/xi if n2 is not None else 'none<=4'};"
      f" m_eff(xi/2)/m F0 = {me1[xi//2]/m:.4f}, F2 = {me2[xi//2]/m:.4f}")
# ---------- FS
w("## FS slice-smeared phi_s^2, flow time s*xi^2, s=0.1")
w("xi  C(1)/C(0)  xi*(1-C1/C0)  R  bound (C0/C1)^(xi/2)")
qa = qb = qc = 0; XS = XIS[1:]
for xi in XS:
    Gs = G_smeared([0, 1, xi // 2, xi], xi, 0.1)
    C = 2 * Gs ** 2
    cpr = xi * (1 - C[1] / C[0]); R = C[2] / C[3]; bd = (C[0] / C[1]) ** (xi / 2)
    qa += cpr <= 20; qb += R <= bd * (1 + 1e-9); qc += R <= math.e ** 10
    w(f"{xi} {C[1]/C[0]:.8f} {cpr:.5f} {R:.6f} {bd:.6f}")
ok3 = qa == qb == qc == len(XS)
w(f"P3: (C') {qa}/{len(XS)}, log-convexity bound {qb}/{len(XS)}, R<=e^10 {qc}/{len(XS)} -> {'MET' if ok3 else 'FAILED'}")
(met if ok3 else fails).append("P3")
# ---------- H2, HH, DK
w("## H2 two-atom, w = exp(-xi/2)")
q5 = 0
for xi in XIS:
    m = 1.0 / xi; wt = math.exp(-xi / 2)
    C = lambda n: wt * math.exp(-m * n) + math.exp(-n)
    R = C(xi / 2) / C(xi); q5 += R >= math.exp(xi / 2) / 3
    # mu_beta: weight at E=1 vs E=xi
    pa = wt * math.exp(-1); pb = math.exp(-xi)
    w(f"xi={xi} R={R:.4e} exp(xi/2)/3={math.exp(xi/2)/3:.4e} mu(E=1)={pa/(pa+pb):.4f} mu(E=xi)={pb/(pa+pb):.4f}")
ok5 = q5 == len(XIS); w(f"P5: {q5}/{len(XIS)} -> {'MET' if ok5 else 'FAILED'}"); (met if ok5 else fails).append("P5")
w("## HH hole family")
RH = {}
for xi in [64, 256, 1024, 4096]:
    m = 1.0 / xi; eh = math.sqrt(m); wt = m ** 4
    e = np.linspace(eh, 3.0, 200000 * res)
    def C(n):
        y = e ** 2 * np.exp(-n * e)
        return wt * math.exp(-m * n) + float(np.sum((y[1:] + y[:-1]) / 2) * (e[1] - e[0]))
    RH[xi] = C(xi / 2) / C(xi)
    w(f"xi={xi} R={RH[xi]:.4e}  C(1)/C(0)={C(1)/C(0):.4f}")
ok6 = RH[4096] / RH[64] > 100
w(f"P6: R(4096)/R(64) = {RH[4096]/RH[64]:.3e} -> {'MET' if ok6 else 'FAILED'}"); (met if ok6 else fails).append("P6")
w("## DK psi = T^xi phi, phi two-atom with w = exp(-2 xi)")
q7 = 0
for xi in XIS:
    m = 1.0 / xi; wt = math.exp(-2 * xi)
    C = lambda n: wt * math.exp(-m * n) + math.exp(-n)
    R = C(2.5 * xi) / C(3 * xi); q7 += R >= math.exp(xi / 2) / 3
    w(f"xi={xi} R_psi={R:.4e}")
ok7 = q7 == len(XIS); w(f"P7: {q7}/{len(XIS)} -> {'MET' if ok7 else 'FAILED'}"); (met if ok7 else fails).append("P7")
w(f"SUMMARY met={len(met)} {met} failed={len(fails)} {fails} measured_only=1 [P8]")
f.close()
sys.exit(0 if not fails else 1)
