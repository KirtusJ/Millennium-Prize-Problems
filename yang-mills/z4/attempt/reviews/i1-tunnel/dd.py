"""dd.py -- vectorised double-double arithmetic on numpy arrays (pairs (hi, lo)). Own code.
Error-free transformations: Knuth two-sum, Dekker split/two-prod. Unit roundoff ~ 2^-104 ~ 4.9e-32 per op.
Tested in ddmeas.py controls (D1..D3)."""
import numpy as np

SPL = 134217729.0  # 2^27+1


def two_sum(a, b):
    s = a + b
    bb = s - a
    return s, (a - (s - bb)) + (b - bb)


def split(a):
    t = SPL * a
    hi = t - (t - a)
    return hi, a - hi


def two_prod(a, b):
    p = a * b
    ah, al = split(a); bh, bl = split(b)
    return p, ((ah * bh - p) + ah * bl + al * bh) + al * bl


def add(x, y):
    s, e = two_sum(x[0], y[0])
    e = e + x[1] + y[1]
    return two_sum_fast(s, e)


def two_sum_fast(a, b):
    s = a + b
    return s, b - (s - a)


def mul(x, y):
    p, e = two_prod(x[0], y[0])
    e = e + (x[0] * y[1] + x[1] * y[0])
    return two_sum_fast(p, e)


def mul_d(x, d):
    p, e = two_prod(x[0], d)
    e = e + x[1] * d
    return two_sum_fast(p, e)


def neg(x):
    return (-x[0], -x[1])


def sub(x, y):
    return add(x, neg(y))


def div(x, y):
    q1 = x[0] / y[0]
    r = sub(x, mul_d(y, q1))
    q2 = r[0] / y[0]
    r = sub(r, mul_d(y, q2))
    q3 = r[0] / y[0]
    q = two_sum_fast(q1, q2)
    return add(q, (q3, q3 * 0))


def div_d(x, d):
    return div(x, (np.asarray(d, float) + 0 * x[0], 0 * x[0]))


def sqrt(x):
    s0 = np.sqrt(x[0])
    s0 = np.where(s0 == 0, 0.0, s0)
    sq = (s0, 0 * s0)
    r = sub(x, mul(sq, sq))
    with np.errstate(divide='ignore', invalid='ignore'):
        corr = np.where(s0 == 0, 0.0, r[0] / (2 * s0))
    return add(sq, (corr, 0 * corr))


def const(v, like=None):
    """dd from a python Fraction/int via exact rational -> two doubles."""
    from fractions import Fraction
    f = Fraction(v)
    hi = float(f)
    lo = float(f - Fraction(hi))
    return (np.float64(hi), np.float64(lo))


PI = (np.float64(3.141592653589793), np.float64(1.2246467991473532e-16))
LN2 = (np.float64(0.6931471805599453), np.float64(2.3190468138462996e-17))


def exp(x):
    """exp of dd array, x <= ~ 0 (used for exp(-V)). ln2 reduction, /16, Taylor 22 terms, 4 squarings."""
    k = np.round(x[0] / LN2[0])
    r = sub(x, (k * LN2[0], k * LN2[1]))  # k*LN2[0] exact? k<2^10, LN2[0] 53 bits -> use two_prod
    p, e = two_prod(k, LN2[0] + 0 * k)
    r = sub(x, two_sum_fast(p, e + k * LN2[1]))
    r = (r[0] / 16, r[1] / 16)
    one = (np.ones_like(x[0]), np.zeros_like(x[0]))
    s = one
    for n in range(22, 0, -1):
        s = add(one, div_d(mul(s, r), float(n)))
    for _ in range(4):
        s = mul(s, s)
    return (np.ldexp(s[0], k.astype(int)), np.ldexp(s[1], k.astype(int)))


def sin_small(y, nterms=30):
    """sin(y) for |y|<=pi/2 by Taylor (dd)."""
    y2 = mul(y, y)
    one = (np.ones_like(y[0]), np.zeros_like(y[0]))
    s = one
    for n in range(nterms, 0, -1):
        s = sub(one, div_d(mul(s, y2), float((2 * n) * (2 * n + 1))))
    return mul(s, y)


def cos_small(y, nterms=30):
    y2 = mul(y, y)
    one = (np.ones_like(y[0]), np.zeros_like(y[0]))
    s = one
    for n in range(nterms, 0, -1):
        s = sub(one, div_d(mul(s, y2), float((2 * n - 1) * (2 * n))))
    return s
