"""p11c.py -- recheck P11 (|khat_i-k_i| <= b^2|k_i|^3/24) in 50-digit Decimal arithmetic (Taylor sin)
on the same seed-1 sample as chal.py (float64 fails only at k b < 2e-4 by cancellation in y - sin y).
p11b.py failed to start (no mpmath installed): its exit 1 is a defect of my program, not of the target.
Predicate P11c: zero violations among 100000 samples (no tolerance; 50 digits)."""
import sys, numpy as np
from decimal import Decimal as D, getcontext
getcontext().prec = 50
def dsin(x):
    s, term, n = D(0), x, 1
    while abs(term) > D(10)**-60:
        s += term; term = -term*x*x/((n+1)*(n+2)); n += 2
    return s
out = open(sys.argv[1], 'x')
rng = np.random.default_rng(1); bb = rng.uniform(0.01, 1, 100000); y = rng.uniform(-np.pi, np.pi, 100000); y[:10] = np.pi
bad = 0; mx = D(0)
for b, yy in zip(bb, y):
    b = D(float(b)); k = D(float(yy))/b
    if k == 0: continue
    d = abs((2/b)*dsin(k*b/2) - k); r = d/(b**2*abs(k)**3/24); mx = max(mx, r); bad += r > 1
msg = f"P11c bad={bad} maxratio={float(mx):.12f}"
out.write(msg+"\n"); out.close(); print(msg)
