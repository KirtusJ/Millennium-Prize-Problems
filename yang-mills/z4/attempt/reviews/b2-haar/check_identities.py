"""check_identities.py -- exact/rational checks for brief b2-haar.

No sympy/mpmath/scipy installed; everything is done with exact rational
power series (fractions.Fraction) in k, truncated at order N=40.

Objects: I1(k) = sum_m (k/2)^(2m+1)/(m!(m+1)!), I2(k) = sum_m (k/2)^(2m+2)/(m!(m+2)!)
 (DLMF 10.25.2).  R = I2/I1 as a power series (R is odd, R/k analytic).

PREDICATES (fixed before first run):
 P1  The series of R' equals the series of 1 - 3R/k - R^2 up to order N-3
     (exact rational equality, tolerance 0: exact arithmetic).
 P2  R = k/4 - k^3/96 + O(k^5) (coefficients exactly 1/4, -1/96).
 P3  q' == (p-q)/k as series (exact).
 P4  p' == -(2R+3/k)p + 3R/k^2 as series (exact).
 P5  p'' == -2p^2 + 6p/k^2 - (2R+3/k)p' - 6R/k^3 as series (exact)  [general identity;
     at p'=0 it reduces to -2p^2 + 6(p-q)/k^2].
 P6  w' == 3R - (2R+1/k)w as series (exact), w = k^2 p.
 P7  w'' == p(3-2w) + w/k^2 - (2R+1/k)w' as series (exact) [general identity].
 P8  p(3-2w) + w/k^2 == (4-2w)w/k^2 as series (exact) -- both auditor formulas agree identically.
 P9  leading terms: p-q = -k^2/48 + O(k^4) (strictly negative leading coeff, order 2);
     p' = -k/16 + O(k^3) (order 1, negative); w' = k/2 + O(k^3) (order 1, positive);
     R - s = +k^3/192 + O(k^5) with s = (sqrt(4+k^2)-2)/k (series of s computed exactly).
 P10 s' == 2 s / (k sqrt(4+k^2)) and 1 - s^2 - 4 s/k == 0 as series (exact).
Results appended to identities_result.txt opened with mode "x".
"""
from fractions import Fraction as F
from math import factorial
import sys

N = 40  # truncation order in k (series kept as coefficient lists of length N)

def ser(coeffs):
    c = [F(0)] * N
    for i, v in coeffs.items():
        if i < N:
            c[i] = F(v)
    return c

def add(a, b): return [x + y for x, y in zip(a, b)]
def sub(a, b): return [x - y for x, y in zip(a, b)]
def scal(c, a): return [F(c) * x for x in a]
def mul(a, b):
    r = [F(0)] * N
    for i, x in enumerate(a):
        if x == 0: continue
        for j in range(N - i):
            r[i + j] += x * b[j]
    return r
def inv(a):  # a[0] != 0
    r = [F(0)] * N
    r[0] = 1 / a[0]
    for n in range(1, N):
        s = sum(a[i] * r[n - i] for i in range(1, n + 1))
        r[n] = -s / a[0]
    return r
def deriv(a): return [ (i + 1) * a[i + 1] for i in range(N - 1)] + [F(0)]
def shift_down(a, m):  # divide by k^m; requires a[0..m-1]==0
    assert all(x == 0 for x in a[:m]), "division by k^m of non-divisible series"
    return a[m:] + [F(0)] * m
def shift_up(a, m): return [F(0)] * m + a[:N - m]
def sqrt_ser(a):  # a[0] > 0 perfect square rational
    import math
    r = [F(0)] * N
    a0 = a[0]
    n0, d0 = a0.numerator, a0.denominator
    rn, rd = math.isqrt(n0), math.isqrt(d0)
    assert rn * rn == n0 and rd * rd == d0
    r[0] = F(rn, rd)
    for n in range(1, N):
        s = sum(r[i] * r[n - i] for i in range(1, n))
        r[n] = (a[n] - s) / (2 * r[0])
    return r

def eq_upto(a, b, M):
    return all(a[i] == b[i] for i in range(M))

# Bessel series
I1 = ser({2*m+1: F(1, 2**(2*m+1) * factorial(m) * factorial(m+1)) for m in range(N)})
I2 = ser({2*m+2: F(1, 2**(2*m+2) * factorial(m) * factorial(m+2)) for m in range(N)})
I1k = shift_down(I1, 1)          # I1/k, nonzero constant term
I2k = shift_down(I2, 1)
R = mul(I2k, inv(I1k))           # R = I2/I1
M = N - 6                        # orders trusted after divisions by k^3 etc.
one = ser({0: 1})
q = shift_down(R, 1)             # R/k
p = deriv(R)
out = []
def rec(name, ok, info=""):
    out.append(f"{name}: {'MET' if ok else 'FAILED'} {info}")
    print(out[-1])

rhs = sub(sub(one, scal(3, q)), mul(R, R))
rec("P1 R'=1-3R/k-R^2", eq_upto(p, rhs, M))
rec("P2 R=k/4-k^3/96+...", R[0] == 0 and R[1] == F(1, 4) and R[2] == 0 and R[3] == F(-1, 96),
    f"R1={R[1]} R3={R[3]} R5={R[5]} R7={R[7]}")
rec("P3 q'=(p-q)/k", eq_upto(deriv(q), shift_down(sub(p, q), 1), M))
# (2R+3/k)p = 2Rp + 3p/k ; p has nonzero constant so p/k is not a series -> compare k*(...)
# multiply P4 by k^2: k^2 p' == -(2R k^2 + 3k) p + 3R
lhs4 = shift_up(deriv(p), 2)
rhs4 = add(scal(-1, mul(add(scal(2, shift_up(R, 2)), ser({1: 3})), p)), scal(3, R))
rec("P4 k^2 p' = -(2Rk^2+3k)p + 3R", eq_upto(lhs4, rhs4, M))
pp = deriv(p); ppp = deriv(pp)
# P5 times k^3: k^3 p'' = -2p^2 k^3 + 6 p k - (2R k^3 + 3k^2) p' - 6R
lhs5 = shift_up(ppp, 3)
rhs5 = add(add(add(scal(-2, shift_up(mul(p, p), 3)), scal(6, shift_up(p, 1))),
           scal(-1, mul(add(scal(2, shift_up(R, 3)), ser({2: 3})), pp))), scal(-6, R))
rec("P5 k^3 p'' general identity", eq_upto(lhs5, rhs5, M))
w = shift_up(p, 2)
wp = deriv(w); wpp = deriv(wp)
# P6 times k: k w' = 3Rk - (2Rk+1) w
rec("P6 k w' = 3Rk-(2Rk+1)w", eq_upto(shift_up(wp, 1),
    sub(scal(3, shift_up(R, 1)), mul(add(scal(2, shift_up(R, 1)), one), w)), M))
# P7 times k^2: k^2 w'' = k^2 p(3-2w) + w - (2Rk^2+k) w'
rhs7 = add(sub(shift_up(mul(p, sub(scal(3, one), scal(2, w))), 2), scal(-1, w)),
           scal(-1, mul(add(scal(2, shift_up(R, 2)), ser({1: 1})), wp)))
rec("P7 k^2 w'' general identity", eq_upto(shift_up(wpp, 2), rhs7, M))
A = add(mul(p, sub(scal(3, one), scal(2, w))), p)            # p(3-2w) + w/k^2  (w/k^2 = p)
B = shift_down(mul(sub(scal(4, one), scal(2, w)), w), 2)     # (4-2w) w / k^2
rec("P8 auditor formulas identical", eq_upto(A, B, M))
pq = sub(p, q)
s = shift_down(sub(sqrt_ser(add(ser({0: 4}), ser({2: 1}))), ser({0: 2})), 1)
Rs = sub(R, s)
rec("P9 leading terms", pq[0] == 0 and pq[1] == 0 and pq[2] == F(-1, 48)
    and pp[0] == 0 and pp[1] == F(-1, 16) and wp[0] == 0 and wp[1] == F(1, 2)
    and Rs[1] == 0 and Rs[3] == F(1, 192),
    f"p-q[2]={pq[2]} p'[1]={pp[1]} w'[1]={wp[1]} (R-s)[3]={Rs[3]} s[1]={s[1]} s[3]={s[3]}")
sq = sqrt_ser(add(ser({0: 4}), ser({2: 1})))
rec("P10 s identities", eq_upto(sub(sub(one, mul(s, s)), scal(4, shift_down(s, 1))), ser({}), M)
    and eq_upto(mul(shift_up(deriv(s), 1), sq), scal(2, s), M))
with open("identities_result.txt", "x") as fh:
    fh.write(f"N={N}, compared orders 0..{M-1}\n" + "\n".join(out) + "\n")
sys.exit(0 if all("MET" in o for o in out) else 1)
