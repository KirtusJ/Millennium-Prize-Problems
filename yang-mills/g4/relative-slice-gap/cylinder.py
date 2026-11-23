"""Outward rational SU(2) Wilson cylinder controls in simultaneous spatial/time refinement."""
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "paired-slice-spectrum"))
from rotor import Interval, SCALE, ZERO, ONE, PI, cell_gram, ceildiv
from relative import estimate


def power(x, exponent):
    result = ONE
    while exponent:
        if exponent % 2:
            result = result * x
        exponent //= 2
        if exponent:
            x = x * x
    return result


@lru_cache(None)
def bessel_series(d, beta):
    term = (beta/2)**d/factorial(d)
    partial = term
    k = 0
    while True:
        ratio = (beta/2)**2 / ((k+1)*(k+d+1))
        term *= ratio
        if ratio <= Q(1,2) and term * 2**125 <= partial:
            return partial, partial + 2*term
        partial += term
        k += 1


def modes(side, degree):
    if side is None:
        partial = sum((Q(1,factorial(k)) for k in range(36)),Q(0))
        inv_e = Interval.rational(1/(partial+Q(2,factorial(36))),1/partial)
        return [power(inv_e,d*d-1) for d in range(1,degree+1)]
    beta = Q(side*side,2)
    den_lo,den_hi = bessel_series(1,beta)
    out = [ONE]
    for d in range(2,degree+1):
        low,high = bessel_series(d,beta)
        out.append(power(Interval.rational(low/den_hi,high/den_lo),side*side))
    return out


def millionths(low,high):
    return [int(low*10**6//1),ceildiv((high*10**6).numerator,(high*10**6).denominator)]


@lru_cache(None)
def gram(bins, degree):
    pairs = [(d,e) for d in range(1,degree+1) for e in range(1,d+1)]
    return pairs, [[cell_gram(i,bins,d,e) for d,e in pairs] for i in range(bins)]


def cylinder(side, bins=32, degree=16, bits=38):
    if side is not None and (type(side) != int or side < 3):
        raise ValueError("At least three spatial links are needed for the stated uniform bound")
    if bins < 2 or bins % 2 or degree < 2:
        raise ValueError("Use an even partition and at least two character modes")
    coeff = modes(side,degree)
    q = Q(8,11)**8
    tail = Interval.rational(0, q**degree/(1-q))
    norm = sum((v*v for v in coeff), ZERO) + tail*tail
    truncation = (Interval.rational(2)*sum(coeff,ZERO) + tail)*tail
    uncertainty = Interval(-truncation.high,truncation.high)
    pairs, cells = gram(bins,degree)
    weights = [coeff[d-1]*coeff[e-1]*Interval.rational(1 if d==e else 2) for d,e in pairs]
    weighted = [[x*w for x,w in zip(row,weights)] for row in cells]
    roots = [[Q(0)]*bins for _ in range(bins)]
    width = Q(0)
    for i in range(bins):
        for j in range(i+1):
            cell = (sum((a*b for a,b in zip(weighted[i],cells[j])),ZERO) + uncertainty)/norm
            if cell.low <= 0:
                raise ArithmeticError("Character cutoff or interval precision insufficient for this bin")
            root = cell.sqrt()
            roots[i][j] = roots[j][i] = Q(root.low+root.high,2*SCALE)
            width = max(width,Q(root.high-root.low,SCALE))
    # True root matrix has HS norm 1. Normalization moves its approximation
    # by at most its original HS error. Measured operator norm is at least 1/bins.
    eta = 2*bins*bins*width
    total = sum(v*v for row in roots for v in row)
    table = [[v*v/total for v in row] for row in roots]
    kernel_min = 2-(1+q)/(1-q)**3
    deriv = q*(4+2*q)/(1-q)**4
    z = Q(PI.high,SCALE)*deriv/(bins*kernel_min)
    cert = estimate({"probabilities":table, "log_oscillations":[z]*bins,
                     "relative_error":eta, "physical_period":2},bits)
    lower,upper = map(Q,cert["probability_ratio"])
    exact = coeff[1]*coeff[1]
    char_lo,char_hi = Q(exact.low,SCALE),Q(exact.high,SCALE)
    assert lower < char_lo <= char_hi < upper < Q(1,100)
    return {"spatial_links":side if side is not None else "continuum",
            "ratio_millionths":millionths(lower,upper),
            "character_millionths":millionths(char_lo,char_hi),
            "relative_operator_error_below_1e_9":eta < Q(1,10**9),
            "oscillation_below_0_072":z < Q(72,1000)}
