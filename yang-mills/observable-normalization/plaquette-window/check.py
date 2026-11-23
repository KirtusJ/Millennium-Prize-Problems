"""Rational certificates for the tilted one-link variance and inverse moment."""
from fractions import Fraction as Q
from math import factorial


def bessel(order, argument, terms):
    x = Q(argument, 2)
    term = x**order / factorial(order)
    total = term
    for j in range(1, terms):
        term *= x*x / (j*(order+j))
        total += term
    ratio = x*x / (terms*(order+terms))
    assert ratio < 1
    return total, total + term*ratio/(1-ratio)


def main():
    h_upper = bessel(2,6,21)[1] / bessel(1,6,21)[0]
    assert h_upper < Q(762727,10**6)
    longitudinal = 1-h_upper**2-h_upper/2
    assert longitudinal > Q(7376,200000)

    stop = 18
    lo, hi = zip(*(bessel(n,1,13) for n in range(stop+2)))
    i1 = lo[1]
    head = sum((n+1)**2 * hi[n+1]**2 / (i1*lo[n+2]) for n in range(stop))
    first = Q(9*factorial(stop+2), 2**stop * factorial(stop)**2)
    # For n >= stop the squared majorant ratio is (n+3)/(2*(n+1)^2) < 1/2.
    assert head+2*first < 14
    e_upper = sum(Q(1,factorial(j)) for j in range(8)) + Q(9,8*factorial(8))
    assert e_upper*2*hi[1] < Q(25,8)
    assert 16*(14*Q(25,8))**4 < 2**26
    d = Q(7376,200000)
    r = Q(1,39)
    w = (d-r)/(1-r)-Q(1,256)
    assert w > Q(3,400)
    assert (1-r)/(1+r) == Q(19,20)
    assert (Q(1,20)+Q(1,32))**2 < Q(3,400)
    print("certified longitudinal lower bound", float(longitudinal))
    print("inverse block sum upper bound", float(head+2*first))
    print("bare window weight floor", w)


if __name__ == "__main__":
    main()
