"""Predicates (stated before first run):
R(k)=I_2(k)/I_1(k) via series with term recurrence t_m=t_{m-1}*(k/2)^2/(m*(m+nu)), 100 terms.
p=R'(k) by central difference h=1e-5; w=k^2*p.
(a) w(k) computed from the series at k=1,2,5.
(b) w'(k) > 1e-6 at k=1,2,5, using central FD of w with h=1e-4.
(c) formula w'(k)=R*(3-2w)-w/k agrees with FD within 1e-6.
Results file opened with mode 'x' (never overwritten). No randomness.
"""
import math

def I(nu, k, N=100):
    t = (k/2)**nu / math.factorial(nu)
    s = t
    for m in range(1, N+1):
        t *= (k/2)**2 / (m*(m+nu))
        s += t
    return s

def R(k): return I(2, k)/I(1, k)
def w(k, h=1e-5):
    p = (R(k+h)-R(k-h))/(2*h)
    return k*k*p

lines = []
ok = True
for k in (1, 2, 5):
    wk = w(k)
    h = 1e-4
    fd = (w(k+h)-w(k-h))/(2*h)
    fm = R(k)*(3-2*wk) - wk/k
    pb = fd > 1e-6
    pc = abs(fd-fm) < 1e-6
    ok &= pb and pc
    lines.append(f"k={k} w={wk:.10f} wprime_FD={fd:.10f} wprime_formula={fm:.10f} "
                 f"diff={abs(fd-fm):.2e} (b)={'PASS' if pb else 'FAIL'} (c)={'PASS' if pc else 'FAIL'}")
lines.append("ALL PASS" if ok else "SOME FAIL")
out = "\n".join(lines)
print(out)
with open("results.txt", "x") as f:
    f.write(out + "\n")
