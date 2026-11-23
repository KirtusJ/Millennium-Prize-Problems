"""A2 rerun of the (3) power count on a larger torus (hodge.py failed H3 on 40^4; suspected pre-asymptotic/torus size).
Same definitions as hodge.py; N=80, L = 2,4,8,12,16, undisplaced test (disp=0).
PREDICATES (fixed before first run):
 H2': ||h||_inf max/min over L <= 1.5.
 H3': the local exponent log(||h||_(1,sqrt w)(L2)/||h||_(1,sqrt w)(L1))/log(L2/L1) for the last pair (12->16) is <= 1.5 + 0.25
      (tolerance: the expected correction to L^{3/2} is a lower-order L^1 term, which raises the local exponent at
       small L; 0.25 is my allowance, chosen before the run).
 Measured only: ||h||_1 / L (target: ||h||_1 = O(L) implicitly), all local exponents.
"""
import numpy as np, sys
N = 80
k = 2*np.pi*np.fft.fftfreq(N); kr = 2*np.pi*np.fft.rfftfreq(N)
s = lambda v: 4*np.sin(v/2)**2
lap = (s(k)[:, None, None, None] + s(k)[None, :, None, None] + s(k)[None, None, :, None] + s(kr)[None, None, None, :])
lap[0, 0, 0, 0] = 1.0
x = np.minimum(np.arange(N), N-np.arange(N)).astype(float)
sw = np.sqrt(1 + x[:, None, None] + x[None, :, None] + x[None, None, :])   # spatial axes 1,2,3
out = []; res = {}
for L in (2, 4, 8, 12, 16):
    a = np.zeros(N); a[0] = 1.0
    for _ in range(3):
        avg = sum(np.roll(a, j) for j in range(L))/L
        a = a - avg
    g = np.zeros((N,)*4); g[0, :, 0, 0] = a
    phi = np.fft.irfftn(np.fft.rfftn(g)/lap, s=g.shape); del g
    hinf = 0.; hw = 0.; h1n = 0.
    for ax, sg in ((2, 1), (1, -1)):
        hh = np.abs(phi - np.roll(phi, 1, axis=ax))
        hinf = max(hinf, hh.max()); h1n += hh.sum(); hw += (hh*sw[None]).sum(); del hh
    del phi
    res[L] = (hinf, hw, h1n)
    out.append(f"L {L}: ||g||_1 {np.abs(a).sum():.4f} ||h||_inf {hinf:.4f} ||h||_1 {h1n:.4f} (/L {h1n/L:.3f}) ||h||_(1,sqrt w) {hw:.4f} (/L^1.5 {hw/L**1.5:.4f})")
    print(out[-1], flush=True)
Ls = (2, 4, 8, 12, 16)
ex = [np.log(res[b][1]/res[a_][1])/np.log(b/a_) for a_, b in zip(Ls, Ls[1:])]
ex1 = [np.log(res[b][2]/res[a_][2])/np.log(b/a_) for a_, b in zip(Ls, Ls[1:])]
hi = [res[L][0] for L in Ls]
H2 = max(hi)/min(hi) <= 1.5; H3 = ex[-1] <= 1.75
out.append("local exponents ||h||_(1,sqrt w): " + " ".join(f"{e:.3f}" for e in ex))
out.append("local exponents ||h||_1: " + " ".join(f"{e:.3f}" for e in ex1))
out.append(f"H2' {'MET' if H2 else 'FAILED'} (sup ratio {max(hi)/min(hi):.3f}); H3' {'MET' if H3 else 'FAILED'} (last exponent {ex[-1]:.3f})")
open("../results/hodge2.txt", "x").write("\n".join(out)+"\n"); print("\n".join(out[-3:]))
sys.exit(0 if H2 and H3 else 1)
