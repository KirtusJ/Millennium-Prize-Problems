"""Numerical checks of SU(2) cylinder norms and neutral power sums."""
from functools import lru_cache
import numpy as np


@lru_cache(maxsize=None)
def grid(order):
    x, w = np.polynomial.legendre.leggauss(order)
    angle = np.pi*(1+x)/2
    return w, angle


def ratios(beta, multiples, order):
    w, angle = grid(order)
    tilted = w*np.exp(-2*beta*np.sin(angle/2)**2)
    return (np.cos(np.outer(multiples,angle)) @ tilted)/(tilted @ np.cos(angle))


def fundamental_match(B, order):
    target = ratios(B,[2],order)[0]
    low,high = B,8*B
    assert ratios(high,[2],order)[0]**4>target
    for _ in range(46):
        middle=(high+low)/2
        if ratios(middle,[2],order)[0]**4 < target: low=middle
        else: high=middle
    return (low+high)/2


def compare(B,order):
    area = B//4
    dimensions = np.arange(3,16,2)
    F = fundamental_match(B,order)
    coarse = ratios(B,dimensions,order)**area
    naive = ratios(4*B,dimensions,order)**(4*area)
    fine = ratios(F,dimensions,order)**(4*area)
    # Explicit tail using the positive Bessel series and monotonicity by steps of two.
    next_value = abs(ratios(F,[17],order)[0])**(4*area)
    def bracket(p):
        m = np.sum(fine**p)
        tail = (np.ceil(F)+2)*next_value**p
        return np.sum(fine**(p+1))/(m+tail), (m+tail)**(1/p)
    lo,hi = bracket(4)
    assert lo<=fine[0]+1e-14 and fine[0]<=hi+1e-14
    assert naive[0]>coarse[0]>fine[0]
    upper8=bracket(8)[1]
    assert upper8 < coarse[0]
    return np.array([F,coarse[0],naive[0]-coarse[0],fine[0]-coarse[0],hi-lo,upper8-coarse[0]])


if __name__ == "__main__":
    for B in (16,64,256):
        row=compare(B,256)
        np.testing.assert_allclose(row,compare(B,384),rtol=2e-8,atol=2e-12)
        print(f"B={B:3d} F={row[0]:.9f} coarse={row[1]:.9f} "
              f"bare drift={row[2]:+.9g} tuned drift={row[3]:+.9g} p4 width={row[4]:.7g} p8 certificate margin={row[5]:+.7g}")
