"""loop_bench.py -- free lattice Maxwell, U(1) Wilson loop of a planar R x R square (statements W1-W5).

No randomness (the Stokes check uses a deterministic field A = sin of an affine function of x).
l = 1, b = 1/N.  G_b(t) = l^-3 sum_{k!=0} |F|^2 (kh1^2+kh2^2)/kh^2 * kh/2 * e^{-t kh},
|F|^2 = prod_{i=1,2} b^2 sin^2(k_i R/2)/sin^2(k_i b/2), M = R/b plaquettes per side (R N must be an integer).

PREDICATES (fixed before the first run; tolerance source in brackets)
P0a Stokes: sum of plaquette angles over the M x M square = oriented link sum on its boundary, |diff| < 1e-12
    [float64 roundoff on ~4M^2 terms of size 1].
P0b Momentum form = position form b^4 sum_{p,p'} D_t(p-p') with D_t from a 3D FFT of the stated mode sum, N = 16, both R,
    t in {0, 0.05}: relative difference < 1e-10 [roundoff of FFT on 16^3 points].
Q1  (W2) For each R, fit G_b(0) = c1*(4R)*N + c2*ln N + c3 on N = 16..128 (3 params, 4 points, 1 dof) and on 16..256.
    P1a: c1(R=0.25) and c1(R=0.125) agree within 5% [my tolerance: 1 dof fit, c1 instability measured by the two N-ranges].
    P1b: local exponent ln(G(256)/G(128))/ln 2 in [0.9, 1.1] for both R [perimeter ~1, area law would be 2; the band allows
         the log correction: c2/(c1 4R N) at N=256 is expected below 10%].
Q2  (W3) For each R and t in {0.02, 0.05, 0.1, 0.2}: d_N = G_N - G_{N/2}.
    P2a: |d_128| < |d_64| < |d_32| (successive differences shrink).
    P2b: |d_64|/|d_128| >= 3 [O(b^2) predicts 4; 3 allows subleading terms].
    P2c: |d_128|/G_128 < 1e-2 [my choice for "converged"].  Expectation: t=0.02 may fail (t*kh_max = 0.02*2*128*sqrt3 = 8.9 at N=128).
    Extrapolated G(t) = G_128 + (G_128 - G_64)/3 (Richardson, assumes O(b^2)).
Q3  (W2 last sentence) corr_N = expm1(g^2 G_N(0.05))/expm1(g^2 G_N(0)), computed in logs, g = 1, 0.5:
    P3: strictly decreasing in N (16..256).  Value at N = 256 measured only.
Q4  (W4) x = g^2 G, rho/g^2 = expm1(x)/g^2, g in {1, .5, .25, .125}, N = 128, t in {0.05, 0.1, 0.2}:
    P4: relative deviation (rho/g^2 - G)/G lies in [x/2, x e^x/2] [elementary bounds of expm1(x)/x - 1], and decreases as g decreases.
Q5  (W5) N = 128 (and 64), both R.
    P5a: the lowest mode energy with nonzero weight (weight > 1e-14 * max weight) is 2N sin(pi/N)/l (one photon, |n|=1), exact to 1e-12.
    P5b: effective rate ln(G(5)/G(6)) agrees with 2N sin(pi/N) to relative 1e-5 [contamination by the next level, gap ~2.6,
         weight ratio O(1): ~ e^{-2.6*5} ~ 2e-6].
    P5c (expected to FAIL, i.e. the W5 wording): the rate equals 2 pi/l to relative 1e-5. Lattice value is below 2pi by pi^2 b^2/6
         (1.0e-4 at N=128), so I expect failure at N <= 128: a precision defect of the wording, as S4 defect 1.
    Measured only: per-axis form-factor zeros n with sin(pi n R/l) = 0 for n = 1..8.
"""
import numpy as np, os, sys, math

OUT = "results_L1.txt"
if os.path.exists(OUT):
    print("result file exists; refusing to overwrite"); sys.exit(3)
lines = []
def out(s=""):
    print(s); lines.append(s)
met = failed = measured = 0
fails = []
def pred(name, ok, info=""):
    global met, failed
    if ok: met += 1
    else: failed += 1; fails.append(name + " " + info)
    out(f"[{'MET' if ok else 'FAIL'}] {name} {info}")

def axis(N, R):
    b = 1.0 / N; M = round(R * N); assert abs(M - R * N) < 1e-12
    n = np.arange(N); q = 2 * np.pi * n  # k_i, l = 1
    kh = 2 * N * np.abs(np.sin(np.pi * n / N))
    with np.errstate(invalid="ignore", divide="ignore"):
        f2 = b**2 * np.sin(q * R / 2)**2 / np.sin(q * b / 2)**2
    f2[0] = R**2
    return kh, f2

def G_lat(N, R, ts):
    kh, f2 = axis(N, R)
    ts = np.asarray(ts, float)
    W = f2[:, None] * f2[None, :]
    kp2 = kh[:, None]**2 + kh[None, :]**2
    acc = np.zeros(len(ts))
    for i3 in range(N):
        k2 = kp2 + kh[i3]**2
        if i3 == 0:
            k2 = k2.copy(); k2[0, 0] = 1.0
        khat = np.sqrt(k2)
        base = W * kp2 / k2 * khat / 2
        if i3 == 0: base[0, 0] = 0.0
        for j, t in enumerate(ts):
            acc[j] += np.sum(base * np.exp(-t * khat))
    return acc

def lowest_energy(N, R):
    kh, f2 = axis(N, R)
    W = f2[:, None] * f2[None, :]; kp2 = kh[:, None]**2 + kh[None, :]**2
    best = np.inf; wmax = 0
    for i3 in range(N):
        k2 = kp2 + kh[i3]**2
        w = W * kp2 / np.where(k2 > 0, k2, 1)
        wmax = max(wmax, w.max())
    for i3 in range(N):
        k2 = kp2 + kh[i3]**2
        w = W * kp2 / np.where(k2 > 0, k2, 1)
        m = (w > 1e-14 * wmax) & (k2 > 0)
        if m.any(): best = min(best, np.sqrt(k2[m]).min())
    return best

# ---- P0a Stokes
for N, R in [(16, 0.25), (32, 0.125)]:
    M = round(R * N); x = np.arange(N)
    X, Y = np.meshgrid(x, x, indexing="ij")
    A1 = np.sin(1.3 * X + 0.7 * Y + 0.1); A2 = np.sin(0.4 * X - 1.9 * Y + 2.0)
    x0 = (N - M) // 2
    th = 0.0
    for i in range(x0, x0 + M):
        for j in range(x0, x0 + M):
            th += A1[i, j] + A2[(i+1) % N, j] - A1[i, (j+1) % N] - A2[i, j]
    ls = 0.0
    for i in range(x0, x0 + M): ls += A1[i, x0]            # bottom, +1
    for j in range(x0, x0 + M): ls += A2[x0 + M, j]        # right, +2
    for i in range(x0, x0 + M): ls -= A1[i, x0 + M]        # top, -1
    for j in range(x0, x0 + M): ls -= A2[x0, j]            # left, -2
    pred(f"P0a Stokes N={N} R={R}", abs(th - ls) < 1e-12, f"diff={abs(th-ls):.2e}")

# ---- P0b position vs momentum, N=16
N = 16; b = 1 / N; n = np.arange(N); kh1 = 2 * N * np.abs(np.sin(np.pi * n / N))
K1, K2, K3 = np.meshgrid(kh1, kh1, kh1, indexing="ij")
K = np.sqrt(K1**2 + K2**2 + K3**2); K[0, 0, 0] = 1
for t in [0.0, 0.05]:
    S = (K1**2 + K2**2) / K**2 * K / 2 * np.exp(-t * K); S[0, 0, 0] = 0
    D = np.real(np.fft.ifftn(S)) * N**3  # sum_k e^{2pi i n.x/N} S, l^-3 = 1
    for R in [0.25, 0.125]:
        M = round(R * N); pts = [(i, j) for i in range(M) for j in range(M)]
        Gp = b**4 * sum(D[(p[0]-q[0]) % N, (p[1]-q[1]) % N, 0] for p in pts for q in pts)
        Gm = G_lat(N, R, [t])[0]
        pred(f"P0b pos=mom N=16 R={R} t={t}", abs(Gp - Gm) / abs(Gm) < 1e-10, f"pos={Gp:.12g} mom={Gm:.12g}")

# ---- main table
Ns = [16, 32, 64, 128, 256]
ts = [0.0, 0.02, 0.05, 0.1, 0.2]
tl = [1.0, 2.0, 3.0, 5.0, 6.0]
G = {}
out("\nG_b(t) table (l=1):  R  N  " + "  ".join(f"t={t}" for t in ts))
for R in [0.25, 0.125]:
    for N in Ns:
        tt = ts + (tl if N in (64, 128) else [])
        v = G_lat(N, R, tt)
        for t, g in zip(tt, v): G[(R, N, t)] = g
        out(f"{R} {N} " + " ".join(f"{G[(R,N,t)]:.10e}" for t in ts))
measured += 1

# ---- Q1
out("\nQ1 fit G_b(0) = c1*(4R)*N + c2*ln N + c3")
c1s = {}
for R in [0.25, 0.125]:
    for rng in [Ns[:4], Ns]:
        A = np.array([[4 * R * N, math.log(N), 1] for N in rng]); y = np.array([G[(R, N, 0.0)] for N in rng])
        c, *_ = np.linalg.lstsq(A, y, rcond=None); res = y - A @ c
        out(f"R={R} N={rng}: c1={c[0]:.6f} c2={c[1]:.6f} c3={c[2]:.6f} residuals={np.array2string(res, precision=3)}")
        c1s[(R, len(rng))] = c
    out(f"R={R} G(0)*b/(4R): " + " ".join(f"{G[(R,N,0.0)]/(4*R*N):.6f}" for N in Ns))
measured += 1
for L in [4, 5]:
    a, bb = c1s[(0.25, L)][0], c1s[(0.125, L)][0]
    pred(f"P1a c1 equal for both R (fit on {L} N)", abs(a - bb) / abs(a) < 0.05, f"c1={a:.6f},{bb:.6f} rel={abs(a-bb)/abs(a):.3%}")
for R in [0.25, 0.125]:
    e = math.log(G[(R, 256, 0.0)] / G[(R, 128, 0.0)]) / math.log(2)
    pred(f"P1b local exponent R={R}", 0.9 <= e <= 1.1, f"exp={e:.4f}")

# ---- Q2
out("\nQ2 convergence at t>0; Richardson G(t) = G128 + (G128-G64)/3")
Gext = {}
for R in [0.25, 0.125]:
    for t in [0.02, 0.05, 0.1, 0.2]:
        d = {N: G[(R, N, t)] - G[(R, N // 2, t)] for N in [32, 64, 128, 256]}
        Gext[(R, t)] = G[(R, 128, t)] + d[128] / 3
        out(f"R={R} t={t}: d32={d[32]:.3e} d64={d[64]:.3e} d128={d[128]:.3e} d256={d[256]:.3e} "
            f"G128={G[(R,128,t)]:.10e} Gext={Gext[(R,t)]:.10e} G256={G[(R,256,t)]:.10e}")
        pred(f"P2a shrink R={R} t={t}", abs(d[128]) < abs(d[64]) < abs(d[32]))
        pred(f"P2b ratio>=3 R={R} t={t}", abs(d[64]) / abs(d[128]) >= 3, f"ratio={abs(d[64])/abs(d[128]):.3f}")
        pred(f"P2c rel d128<1e-2 R={R} t={t}", abs(d[128]) / G[(R, 128, t)] < 1e-2, f"rel={abs(d[128])/G[(R,128,t)]:.2e}")

# ---- Q3
def lexpm1(x): return x + math.log1p(-math.exp(-x)) if x > 30 else math.log(math.expm1(x))
out("\nQ3 corr = expm1(g^2 G(0.05))/expm1(g^2 G(0)) (log10)")
for R in [0.25, 0.125]:
    for g in [1.0, 0.5]:
        lc = [(lexpm1(g*g*G[(R, N, 0.05)]) - lexpm1(g*g*G[(R, N, 0.0)])) / math.log(10) for N in Ns]
        out(f"R={R} g={g}: log10 corr over N={Ns}: " + " ".join(f"{v:.4f}" for v in lc))
        pred(f"P3 corr decreasing R={R} g={g}", all(lc[i+1] < lc[i] for i in range(len(lc)-1)))
measured += 1

# ---- Q4
out("\nQ4 rho_b(t)/g^2 at N=128 vs G_128(t)")
for R in [0.25, 0.125]:
    for t in [0.05, 0.1, 0.2]:
        Gt = G[(R, 128, t)]; prev = None; ok = True; row = []
        for g in [1.0, 0.5, 0.25, 0.125]:
            x = g*g*Gt; r = math.expm1(x) / (g*g); dev = (r - Gt) / Gt
            ok &= (x/2 - 1e-15 <= dev <= x*math.exp(x)/2 + 1e-15)
            if prev is not None: ok &= dev < prev
            prev = dev; row.append(f"g={g}: {r:.6e} (dev {dev:.3e})")
        out(f"R={R} t={t} G={Gt:.6e}: " + "; ".join(row))
        pred(f"P4 R={R} t={t}", ok)

# ---- Q5
out("\nQ5 decay")
for R in [0.25, 0.125]:
    out(f"R={R} per-axis zeros sin(pi n R)=0 for n=1..8: " + str([nn for nn in range(1, 9) if abs(math.sin(math.pi*nn*R)) < 1e-12]))
    for N in [64, 128]:
        Elat = 2 * N * math.sin(math.pi / N)
        E0 = lowest_energy(N, R)
        pred(f"P5a lowest weighted energy N={N} R={R}", abs(E0 - Elat) < 1e-12 * Elat, f"E0={E0:.12f} 2N sin(pi/N)={Elat:.12f}")
        rate = math.log(G[(R, N, 5.0)] / G[(R, N, 6.0)])
        r23 = math.log(G[(R, N, 2.0)] / G[(R, N, 3.0)])
        out(f"  N={N} rate(2->3)={r23:.8f} rate(5->6)={rate:.10f}  2pi={2*math.pi:.10f}")
        pred(f"P5b rate=lattice N={N} R={R}", abs(rate - Elat) / Elat < 1e-5, f"rel={abs(rate-Elat)/Elat:.2e}")
        pred(f"P5c rate=2pi N={N} R={R}", abs(rate - 2*math.pi) / (2*math.pi) < 1e-5, f"rel={abs(rate-2*math.pi)/(2*math.pi):.2e}")
measured += 1

out(f"\nCOUNTS met={met} failed={failed} measured_only={measured}")
for f in fails: out("FAILED: " + f)
with open(OUT, "w") as fh: fh.write("\n".join(lines) + "\n")
sys.exit(0 if failed == 0 else 1)
