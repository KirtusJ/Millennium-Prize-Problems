"""Outward-rounded SU(2) class rotor control using only the Python standard library."""
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial, isqrt
import json

SCALE = 1 << 90


def ceildiv(a, b):
    return -((-a)//b)


@dataclass(frozen=True)
class Interval:
    low: int
    high: int

    @classmethod
    def rational(cls, a, b=None):
        a = Q(a)
        b = a if b is None else Q(b)
        return cls(a.numerator*SCALE//a.denominator, ceildiv(b.numerator*SCALE,b.denominator))

    def __add__(self, other):
        return Interval(self.low+other.low,self.high+other.high)

    def __neg__(self):
        return Interval(-self.high,-self.low)

    def __sub__(self, other):
        return self+(-other)

    def __mul__(self, other):
        ends = [u*v for u in (self.low,self.high) for v in (other.low,other.high)]
        return Interval(min(ends)//SCALE,ceildiv(max(ends),SCALE))

    def __truediv__(self, other):
        assert other.low > 0
        return self * Interval(SCALE**2//other.high,ceildiv(SCALE**2,other.low))

    def sqrt(self):
        assert 0 <= self.low <= self.high
        upper = isqrt(SCALE*self.high)
        return Interval(isqrt(SCALE*self.low),upper+int(upper**2 != SCALE*self.high))


ZERO = Interval.rational(0)
ONE = Interval.rational(1)


def atan_bounds(q, terms=24):
    series = sum((Q((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(terms)),Q(0))
    next_term = Q((-1)**terms,(2*terms+1)*q**(2*terms+1))
    return Interval.rational(min(series,series+next_term),max(series,series+next_term))


PI = Interval.rational(16)*atan_bounds(5) - Interval.rational(4)*atan_bounds(239)


@lru_cache(None)
def sin_grid(j, bins):
    j %= 2*bins
    if j > bins:
        return -sin_grid(2*bins-j,bins)
    if j > bins//2:
        return sin_grid(bins-j,bins)
    x = PI*Interval.rational(Q(j,bins))
    center = Q(x.low,SCALE)
    # Alternating sine on [0,pi/2], enlarged by the argument uncertainty.
    partial = sum(((-1)**i * center**(2*i+1)/factorial(2*i+1) for i in range(18)),Q(0))
    extra = center**37/factorial(37)
    width = Q(x.high-x.low,SCALE)
    return Interval.rational(partial-width,partial+extra+width)


def bessel(d):
    # I_d(2), with the positive tail dominated by twice the next term.
    main = sum((Q(1,factorial(i)*factorial(i+d)) for i in range(26)),Q(0))
    tail = Q(2,factorial(26)*factorial(26+d))
    return Interval.rational(main,main+tail)


def cell_gram(i, bins, d, e):
    def integral_cosine(freq):
        freq = abs(freq)
        if freq == 0:
            return Interval.rational(Q(1,bins))
        return (sin_grid(freq*(i+1),bins)-sin_grid(freq*i,bins))/(PI*Interval.rational(freq))
    return integral_cosine(d-e)-integral_cosine(d+e)


def rayleigh(matrix, v):
    return sum((v[i]*v[j]*matrix[i][j] for i in range(len(v)) for j in range(len(v))),ZERO)


def outward_millionths(low, high):
    return [low.low*10**6//SCALE,ceildiv(high.high*10**6,SCALE)]


def calculate(bins=32, degree=15):
    assert bins % 2 == 0 and degree >= 3
    modes = range(1,degree+1)
    pairs = [(d,e) for d in modes for e in modes if e <= d]
    r = {d:bessel(d) for d in modes}
    tail = Interval.rational(0,Q(4,factorial(degree+1)))
    Z = sum((v*v for v in r.values()),ZERO) + tail*tail
    omitted = (Interval.rational(2)*sum(r.values(),ZERO)+tail)*tail
    error = Interval(-omitted.high,omitted.high)
    coeff = [r[d]*r[e]*Interval.rational(1 if d == e else 2) for d,e in pairs]
    gram = [[cell_gram(i,bins,d,e) for d,e in pairs] for i in range(bins)]
    weighted = [[v*w for v,w in zip(row,coeff)] for row in gram]
    B = [[ZERO]*bins for _ in range(bins)]
    for i in range(bins):
        for j in range(i+1):
            cell = (sum((a*b for a,b in zip(weighted[i],gram[j])),ZERO)+error)/Z
            assert cell.low > 0
            B[i][j] = B[j][i] = cell.sqrt()

    even = [cell_gram(i,bins,1,1).sqrt() for i in range(bins)]
    odd = [cell_gram(i,bins,1,2)/even[i] for i in range(bins)]
    odd_norm = sum((v*v for v in odd),ZERO).sqrt()
    odd = [v/odd_norm for v in odd]
    a,b = rayleigh(B,even),rayleigh(B,odd)
    z = PI*Interval.rational(Q(2,bins))
    loss = z*z*Interval.rational(Q(1,2))
    first = (ONE-loss)*a
    second = Interval(min(a.low,b.low),min(a.high,b.high))-loss
    assert 0 < second.low <= first.low and first.high < SCALE
    first_upper = (ONE-second*second).sqrt()
    second_upper = (ONE-first*first).sqrt()
    ratio_lo,ratio_hi = second/first_upper,second_upper/first
    check_ratio = r[2]/r[1]
    check_vac = r[1]*r[1]/Z
    assert ratio_lo.high < check_ratio.low and check_ratio.high < ratio_hi.low < SCALE
    assert (first*first).high < check_vac.low and check_vac.high < (first_upper*first_upper).low
    return {"bins":bins,"character_cutoff":degree,"units":"millionths, rounded outward",
            "vacuum_probability":outward_millionths(first*first,first_upper*first_upper),
            "transfer_ratio":outward_millionths(ratio_lo,ratio_hi),
            "character_vacuum":outward_millionths(check_vac,check_vac),
            "character_ratio":outward_millionths(check_ratio,check_ratio)}


if __name__ == "__main__":
    print(json.dumps(calculate(),indent=2))
