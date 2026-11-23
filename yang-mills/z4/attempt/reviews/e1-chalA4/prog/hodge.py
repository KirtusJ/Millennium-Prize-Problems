"""A2 numerical check of the power count (3) of the target, M -> infinity limit (S_inf = Delta^{-1}).
g = (I - A_L)^3 u on 12-faces along axis 1, u = unit face at the origin (or displaced by L along axis 2);
h = d* Delta^{-1} g (components 1 and 2 only), computed by FFT on a 40^4 torus.
w(x) = 1 + |x_spatial|_1 (spatial distance from the root at the origin, torus-minimal coordinates).
PREDICATES (fixed before first run):
 H1: ||g||_1 <= 8 for L=2,4,8 (exact).
 H2: ||h||_inf bounded: max over L=2,4,8 / min <= 1.5   (target: ||h||_inf <= C).
 H3: ||h||_{1,sqrt w} grows no faster than L^{3/2}: ratio(L=8)/ratio(L=4) of ||h||_{1,sqrt w}/L^{3/2} <= 1.2
     (tolerance: torus truncation of the r^-6 tail is <1e-2 relative at N=40; 1.2 leaves room for subleading terms).
 Measured only: the local exponent log2(||h||_{1,sqrt w}(2L)/||h||_{1,sqrt w}(L)).
"""
import numpy as np, sys
N = 40
k = 2*np.pi*np.fft.fftfreq(N)
K = np.meshgrid(k, k, k, k, indexing="ij", sparse=True)
lap = sum(4*np.sin(kk/2)**2 for kk in K)
lap = np.where(lap == 0, 1.0, lap)
x = np.minimum(np.arange(N), N-np.arange(N))
X = np.meshgrid(x, x, x, x, indexing="ij", sparse=True)
w = 1 + X[1] + X[2] + X[3]
out = []
res = {}
for disp in (0, 1):
    for L in (2, 4, 8):
        a = np.zeros(N); a[0] = 1.0
        for _ in range(3):
            avg = np.zeros(N)
            for j in range(L): avg += np.roll(a, j)/L
            a = a - avg
        g = np.zeros((N,)*4); g[0, :, (L*disp) % N, 0] = a
        assert abs(np.abs(a).sum()) <= 8+1e-12
        phi = np.real(np.fft.ifftn(np.fft.fftn(g)/lap))
        h1 = phi - np.roll(phi, 1, axis=2)   # backward difference along axis 2
        h2 = -(phi - np.roll(phi, 1, axis=1))
        hinf = max(np.abs(h1).max(), np.abs(h2).max())
        hw = ((np.abs(h1)+np.abs(h2))*np.sqrt(w)).sum()
        h1n = (np.abs(h1)+np.abs(h2)).sum()
        res[(disp, L)] = (hinf, hw, h1n, np.abs(a).sum())
        out.append(f"disp {disp*L} L {L}: ||g||_1 {np.abs(a).sum():.4f} ||h||_inf {hinf:.4f} ||h||_1 {h1n:.4f} ||h||_(1,sqrt w) {hw:.4f} /L^1.5 {hw/L**1.5:.4f}")
fails = 0
for disp in (0, 1):
    H1 = all(res[(disp, L)][3] <= 8+1e-12 for L in (2, 4, 8))
    hi = [res[(disp, L)][0] for L in (2, 4, 8)]; H2 = max(hi)/min(hi) <= 1.5
    r4 = res[(disp, 4)][1]/4**1.5; r8 = res[(disp, 8)][1]/8**1.5; H3 = r8/r4 <= 1.2
    e1 = np.log2(res[(disp, 4)][1]/res[(disp, 2)][1]); e2 = np.log2(res[(disp, 8)][1]/res[(disp, 4)][1])
    out.append(f"disp={disp}: H1 {'MET' if H1 else 'FAILED'}; H2 {'MET' if H2 else 'FAILED'} (sup ratio {max(hi)/min(hi):.3f}); H3 {'MET' if H3 else 'FAILED'} (ratio {r8/r4:.3f}); local exponents {e1:.3f}, {e2:.3f}")
    fails += (not H1) + (not H2) + (not H3)
open("../results/hodge.txt", "x").write("\n".join(out)+"\n"); print("\n".join(out))
sys.exit(1 if fails else 0)
