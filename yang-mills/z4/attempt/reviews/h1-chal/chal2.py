"""chal2.py -- repairs of two of MY checks in chal.py (run3), predicates fixed before first run.
Q1 (C1, replaces P9): first zero a' of Ai by shooting -u''+ru=Eu backward from r=14 with step h
    chosen so that r lands exactly on 0 (h = 14/28000); |a'-2.33810741| < 1e-6 and
    E0_lower = 2*4^{-1/3} a' satisfies |E0_lower - 2.94583| < 1e-5 and E0_lower < 3.3505330.
    Tolerance: RK4 error O(h^4) ~ 1e-12; starting-value error damped by exp(-2/3*14^{3/2}) ~ 1e-15.
Q2 (replaces the CF-vs-quadrature cross-check): for x in {0.5,3,40,700}, v in {0,1,3,10,25} where
    e^{-x} I_v(x) > 1e-8 (quadrature cancellation floor ~1e-16 absolute => rel error < 1e-8),
    |CF ratio / quadrature ratio - 1| < 1e-8.
"""
import math, json, sys
import numpy as np
from numpy.polynomial.legendre import leggauss
def u0(E, Nst=28000):
    h = 14.0 / Nst; r = 14.0; y = np.array([1e-12, -math.sqrt(14 - E) * 1e-12])
    f = lambda rr, y: np.array([y[1], (rr - E) * y[0]])
    for i in range(Nst):
        k1 = f(r, y); k2 = f(r - h/2, y - h/2*k1); k3 = f(r - h/2, y - h/2*k2); k4 = f(r - h, y - h*k3)
        y = y - h/6*(k1 + 2*k2 + 2*k3 + k4); r = 14.0 - (i + 1) * h
    return y[0]
lo, hi = 2.3, 2.4; flo = u0(lo)
for _ in range(30):
    m = 0.5*(lo+hi); fm = u0(m)
    if (fm > 0) == (flo > 0): lo, flo = m, fm
    else: hi = m
ap = 0.5*(lo+hi); E0l = 2*4**(-1/3)*ap
out = {"Q1": dict(a_prime=ap, E0_lower=E0l, holds=bool(abs(ap-2.33810741) < 1e-6 and abs(E0l-2.94583) < 1e-5 and E0l < 3.3505330))}
def Iv(v, x, M=4000):
    t, w = leggauss(M); t = (t+1)*math.pi/2; w = w*math.pi/2
    return float(np.sum(np.exp(x*(np.cos(t)-1))*np.cos(v*t)*w)/math.pi)
def ratios(x, nmax):
    N = int(math.sqrt(nmax**2 + 60*x + 400)) + nmax + 20
    r = x/(N+0.5+math.sqrt((N+1.0)**2+x*x)); res = {}
    for v in range(N-1, -1, -1):
        r = x/(2.0*(v+1)+x*r)
        if v <= nmax: res[v] = r
    return res
worst = 0; q = 0; skipped = 0
for x in [0.5, 3.0, 40.0, 700.0]:
    rr = ratios(x, 30)
    for v in [0, 1, 3, 10, 25]:
        a, b = Iv(v+1, x), Iv(v, x)
        if a > 1e-8 and b > 1e-8:
            q += 1; worst = max(worst, abs(rr[v]/(a/b)-1))
        else: skipped += 1
out["Q2"] = dict(qualify=q, skipped=skipped, worst_rel=worst, holds=worst < 1e-8)
print(json.dumps(out))
with open(sys.argv[1], "x") as fh: json.dump(out, fh)
