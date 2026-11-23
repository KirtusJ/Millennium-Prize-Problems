"""p11b.py -- recheck P11 (|khat_i-k_i| <= b^2|k_i|^3/24) in 50-digit arithmetic (mpmath) on the
same seed-1 sample, because the float64 run fails only at y=k b<2e-4 where y-sin y suffers cancellation.
Predicate P11b: holds for all 100000 samples with exact-ish arithmetic (tolerance: none, 50 digits)."""
import sys, numpy as np, mpmath as mp
mp.mp.dps = 50
out = open(sys.argv[1], 'x')
rng = np.random.default_rng(1); bb = rng.uniform(0.01, 1, 100000); y = rng.uniform(-np.pi, np.pi, 100000); y[:10] = np.pi
bad = 0; mx = mp.mpf(0)
for b, yy in zip(bb, y):
    b = mp.mpf(b); k = mp.mpf(yy)/b
    if k == 0: continue
    d = abs((2/b)*mp.sin(k*b/2) - k); r = d/(b**2*abs(k)**3/24); mx = max(mx, r); bad += r > 1
out.write(f"P11b bad={bad} maxratio={mp.nstr(mx, 12)}\n"); out.close(); print(f"P11b bad={bad} maxratio={mp.nstr(mx,12)}")
