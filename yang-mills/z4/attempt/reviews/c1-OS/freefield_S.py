"""freefield_S.py -- known-answer test of THEOREM S on the 4D lattice free massive scalar field.

Model: Gaussian field on Z^4, covariance G_m = (m^2 - Delta)^{-1}, Delta the nearest-neighbour Laplacian.
Theorem S scale choice: a := lattice gap = E0(m) = 2*asinh(m/2) (exact transfer-matrix gap, zero spatial momentum).
xi := 1/a, N := 2*floor(xi/2) (even, so Z^2 = G(N e0) = ||T^{N/2} psi||^2 > 0).
Rescaled normalized two-point function of phi:   S2b(a n) = G_m(n)/G_m(N e0).
Of :phi^2: :  2 G_m(n)^2 / (2 G_m(N e0)^2).
Continuum prediction (free field of mass 1, normalized at |x| = 1): S2(x) = K1(|x|)/(|x| K1(1)),
and the same at finite beta with the exact normalization point: S2N(x) = [K1(|x|)/|x|] / [K1(aN)/(aN)].

Numerics: G_m(n) = int_0^inf e^{-m^2 t} prod_mu h(n_mu,t) dt, h(n,t) = e^{-2t} I_n(2t) computed as the
inverse DFT of exp(-4t sin^2(k/2)) on K = 16384 points (aliasing error ~ h(K-n,t), negligible for
t <= t_max); t-integral by trapezoid in u = log t on [log 1e-8, log(60/m^2)] with 6000 nodes.
K1 by K1(z) = int_0^inf e^{-z cosh u} cosh u du (trapezoid, 4000 nodes on [0,12]).

PREDICATES (fixed before the first run; tolerances and their origin stated):
 P0 control: G_1(0) = 0.1271118504 to 1e-9 (value from my own heat-kernel Gauss-Legendre + momentum sums N=32,48,
    which agreed to 1e-15; tolerance 1e-9 allows quadrature error of this method).
 P0b child cross-check: with a = m (child's scale), m = 1/16: m^-2 G_m(16,0,0,0) = 1.53350636e-02 and
    m^-2 G_m(8,8,8,8) = 1.51966668e-02 (child report) to relative 1e-7 (child reported 8 digits).
 P1 (H1, gap): the 1D zero-momentum correlator int e^{-m^2 t} h(n0,t) dt equals e^{-E0 n0}/(2 sinh E0),
    E0 = 2 asinh(m/2), relative 1e-8, for n0 in {0,1,N/2,N} and every m (exact formula; tolerance = quadrature).
 P2 (H2): a(m) strictly decreasing to 0 along m = 1/4..1/32 (trivial; recorded).
 P3 (convergence of S2b to S2 at fixed normalization): for every test point x (list below; n = round(x/a)),
    rel err E(m) = |S2b(an) - S2N(an)|/S2N(an) decreases as m halves from 1/8 to 1/32, and E(1/32) < 0.02.
    (0.02: the child's measured errors at a ~ 1/16 were <= 0.6%; lattice artefacts are O(a^2), and our
    points rounded to the lattice have |an| down to 0.3 where artefacts are larger; factor ~3 margin.)
 P4 (full limit with normalization at 1): |S2b(an) - S2(an)| / S2(an) < 0.05 at m = 1/32 for every test point
    (extra O(a) error from aN != 1: |aN - 1| <= 2a ~ 0.06, times |d log(K1(r)/r)/dr| at r=1 ~ 2.2; so a bound
    ~0.13a*... we take 0.05 as the expectation; if it fails, it is my tolerance, check P3).
 P5 (H4, rotation): for x = (0,1,0,0) and Rx = (0, cos 1, sin 1, 0) (irrational rotation in the (1,2)-plane),
    and for x=(1,0,0,0) vs (.5,.5,.5,.5): D(m) = |S2b(a n_Rx) - S2b(a n_x)| decreases as m halves (1/8 -> 1/32)
    and D(1/32) < 0.05 * S2(1)=0.05 (rounding to the lattice moves |x| by up to a: O(a) effect expected).
 P6 (H3a, growth bound): sup over lattice points n with 1 <= |n|_inf <= 2 xi on the axis, the (1,1,0,0) and
    (1,1,1,1) diagonals of |an|^2 S2b(an) is <= 2.5 for every m, and the sups for m=1/8,1/16,1/32 agree within 10%.
    (2.5: continuum sup is 1/K1(1) = 1.656; lattice artefact at |n|=1 is G0(e1)*4pi^2 = 1.18 times the continuum
    short-distance law; 1.656*1.18 = 1.96, plus margin.)
 P7 (H3b, Lipschitz at delta = 1/2): max over axis points with |an| >= 1/2 of |S2b(a(n+e0)) - S2b(an)|/a
    <= 1.5 * sup_{r >= 1/2} |d/dr [K1(r)/(r K1(1))]| for every m. (1.5: margin for O(a) artefacts.)
 P8 (H0, reflection positivity, numerical illustration only): for 40 random lattice points in t >= 1
    (seed 12345, |n_i| <= 2xi), the matrix M_ij = G(theta n_i - n_j) (theta: t -> -t) has min eigenvalue
    >= -1e-12 * max|M| (round-off) for m = 1/8.
 P9 (:phi^2:): rel err of 2G^2/(2G(N)^2) against S2N^2 is < 2*(P3 error)+1e-6 at m=1/32 for every point (Wick).
Results written to freefield_S.out (mode "x"); fixed seed 12345.
"""
import numpy as np, math, json, sys

K = 16384
OUT = sys.argv[1] if len(sys.argv) > 1 else "freefield_S.out"
fout = open(OUT, "x")
def log(*a):
    s = " ".join(str(x) for x in a); print(s); fout.write(s + "\n"); fout.flush()

def K1(z):
    u = np.linspace(0, 12, 4001); f = np.exp(-z*np.cosh(u))*np.cosh(u)
    return np.trapezoid(f, u)
def dK1r(r, eps=1e-5):
    g = lambda s: K1(s)/s
    return (g(r+eps)-g(r-eps))/(2*eps)

def tables(m, nmax):
    tmax = 60.0/m**2
    u = np.linspace(math.log(1e-8), math.log(tmax), 6000)
    t = np.exp(u); du = u[1]-u[0]
    w = np.full_like(u, du); w[0] *= .5; w[-1] *= .5
    w = w*t*np.exp(-m*m*t)
    k = 2*np.pi*np.arange(K)/K; s = 4*np.sin(k/2)**2
    H = np.empty((len(t), nmax+1))
    for i, ti in enumerate(t):
        H[i] = np.fft.ifft(np.exp(-ti*s)).real[:nmax+1]
    return w, H

def G(w, H, n):
    p = np.ones(len(w))
    for c in n: p = p*H[:, abs(int(c))]
    return float(np.dot(w, p))

PTS = {"t-axis (1,0,0,0)": (1,0,0,0), "space-axis (0,1,0,0)": (0,1,0,0), "diag (.5,.5,.5,.5)": (.5,.5,.5,.5),
       "(.707,.707,0,0)": (2**-.5, 2**-.5, 0, 0), "rot1 (0,cos1,sin1,0)": (0, math.cos(1), math.sin(1), 0),
       "(2,0,0,0)": (2,0,0,0), "(0.3,0.4,0,0)": (0.3,0.4,0,0), "(0.6,0.8,1.2,0.4)": (0.6,0.8,1.2,0.4)}
fails = []
def pred(name, ok, detail):
    log(f"PRED {name}: {'MET' if ok else 'FAILED'} | {detail}")
    if not ok: fails.append(name)

# P0 control
w, H = tables(1.0, 4)
g0 = G(w, H, (0,0,0,0)); pred("P0", abs(g0-0.1271118504) < 1e-9, f"G_1(0)={g0:.12f}")
# P0b child cross-check (a = m = 1/16)
w, H = tables(1/16, 40)
c1 = G(w, H, (16,0,0,0))*256; c2 = G(w, H, (8,8,8,8))*256
pred("P0b", abs(c1/1.53350636e-02-1) < 1e-7 and abs(c2/1.51966668e-02-1) < 1e-7, f"{c1:.10e} {c2:.10e}")

K1_1 = K1(1.0)
ms = [1/4, 1/8, 1/16, 1/32]
res = {}
for m in ms:
    a = 2*math.asinh(m/2); xi = 1/a; N = 2*int(xi//2)
    nmax = int(2*xi)+3
    w, H = tables(m, max(nmax, N)+2)
    E0 = a
    # P1 gap via 1D zero-momentum correlator
    ok = True; det = []
    for n0 in (0, 1, N//2, N):
        v = float(np.dot(w, H[:, n0])); ex = math.exp(-E0*n0)/(2*math.sinh(E0))
        ok &= abs(v/ex-1) < 1e-8; det.append(f"{n0}:{v/ex-1:.1e}")
    pred(f"P1 m={m}", ok, "rel dev " + " ".join(det))
    GN = G(w, H, (N,0,0,0)); aN = a*N
    r = {"a": a, "N": N, "pts": {}}
    for name, x in PTS.items():
        n = tuple(int(round(c/a)) for c in x); xn = np.array(n)*a; rr = float(np.linalg.norm(xn))
        sb = G(w, H, n)/GN
        sN = (K1(rr)/rr)/(K1(aN)/aN); s1 = K1(rr)/(rr*K1_1)
        r["pts"][name] = dict(n=n, r=rr, Sb=sb, SN=sN, S1=s1, e3=abs(sb-sN)/sN, e4=abs(sb-s1)/s1,
                              e9=abs(sb**2-sN**2)/sN**2)
        log(f"m={m:.5f} a={a:.6f} N={N} {name:24s} n={n} |an|={rr:.4f} Sb={sb:.6e} SN={sN:.6e} S1={s1:.6e} "
            f"errN={abs(sb-sN)/sN:.2e} err1={abs(sb-s1)/s1:.2e}")
    # P6 growth, P7 Lipschitz
    sup = 0; lip = 0
    for kk in range(1, int(2*xi)+1):
        for n in ((kk,0,0,0), (kk,kk,0,0), (kk,kk,kk,kk)):
            if max(n) > nmax: continue
            sb = G(w, H, n)/GN; sup = max(sup, (a*a*sum(c*c for c in n))*sb)
        if a*kk >= 0.5 and kk+1 <= nmax:
            lip = max(lip, abs(G(w, H, (kk+1,0,0,0))-G(w, H, (kk,0,0,0)))/GN/a)
    r["sup"] = sup; r["lip"] = lip
    log(f"m={m:.5f} sup|x|^2 S2b={sup:.4f}  Lipschitz(delta=1/2)={lip:.4f}")
    res[m] = r

pnames = list(PTS)
# P2
pred("P2", all(res[ms[i]]["a"] > res[ms[i+1]]["a"] for i in range(3)), str([round(res[m]["a"], 6) for m in ms]))
# P3
for p in pnames:
    e = [res[m]["pts"][p]["e3"] for m in ms[1:]]
    pred(f"P3 {p}", e[0] > e[1] > e[2] and e[2] < 0.02, "errN m=1/8,1/16,1/32: " + " ".join(f"{v:.2e}" for v in e))
# P4
for p in pnames:
    e = res[ms[-1]]["pts"][p]["e4"]; pred(f"P4 {p}", e < 0.05, f"err vs S normalized at 1, m=1/32: {e:.3e}")
# P5 rotation
for (p, q) in (("space-axis (0,1,0,0)", "rot1 (0,cos1,sin1,0)"), ("t-axis (1,0,0,0)", "diag (.5,.5,.5,.5)")):
    D = [abs(res[m]["pts"][p]["Sb"]-res[m]["pts"][q]["Sb"]) for m in ms[1:]]
    pred(f"P5 {p} vs {q}", D[0] > D[1] > D[2] and D[2] < 0.05, " ".join(f"{v:.3e}" for v in D))
# P6
sups = [res[m]["sup"] for m in ms]
pred("P6", max(sups) <= 2.5 and (max(sups[1:])/min(sups[1:])-1) < 0.10, " ".join(f"{v:.4f}" for v in sups))
# P7
rg = np.linspace(0.5, 8, 400); Lc = max(abs(dK1r(x))/K1_1 for x in rg)
lips = [res[m]["lip"] for m in ms]
pred("P7", all(l <= 1.5*Lc for l in lips), f"continuum sup {Lc:.4f}; lattice " + " ".join(f"{v:.4f}" for v in lips))
# P8 RP illustration
rng = np.random.default_rng(12345); m = 1/8; a = 2*math.asinh(m/2); xi = 1/a
w, H = tables(m, 2*int(2*xi)+4)
P = [(int(rng.integers(1, int(2*xi)+1)),) + tuple(int(v) for v in rng.integers(-int(xi), int(xi)+1, 3)) for _ in range(40)]
M = np.array([[G(w, H, (-p[0]-q[0], p[1]-q[1], p[2]-q[2], p[3]-q[3])) for q in P] for p in P])
M = (M+M.T)/2; ev = np.linalg.eigvalsh(M)
pred("P8", ev.min() >= -1e-12*abs(M).max(), f"min eig {ev.min():.3e} max|M| {abs(M).max():.3e}")
# P9
for p in pnames:
    e9 = res[ms[-1]]["pts"][p]["e9"]; e3 = res[ms[-1]]["pts"][p]["e3"]
    pred(f"P9 {p}", e9 < 2*e3+1e-6, f"phi^2 err {e9:.3e} vs 2*phi err {2*e3:.3e}")
log("FAILED PREDICATES:", fails)
log(f"COUNT met={sum(1 for l in open(OUT).read().splitlines() if ' MET ' in l)} failed={len(fails)}")
fout.close()
