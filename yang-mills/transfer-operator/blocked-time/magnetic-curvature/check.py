"""Check the coefficient using Haar quadrature and independent Bessel ratios."""
from fractions import Fraction

import numpy as np
from scipy.special import ive, roots_chebyu


def coefficients(q, t):
    lam = q**4
    def H(x):
        return (lam+x)/(lam-x)
    h = (1+lam)/(1-lam)
    j = (H(q**6)+3*H(q**6*t))/4-h
    assert j > 0 and abs(H(1)+H(lam**2)) < 1e-9
    # Calculate both log shifts separately in a box with 3*6^3 squares.
    count = 648
    pair = j+h
    diagonal = H(1)+H(t**4)+(count-13)*h+12*pair
    off_diagonal = H(1)+pair
    separate = (count*h-diagonal-12*off_diagonal)/8
    simplified = -(H(t**4)-2*h+24*j)/8
    assert np.isclose(separate, simplified, rtol=1e-8, atol=1e-9)
    return simplified


def check():
    nodes, weights = roots_chebyu(256)
    for g in (0.02, 0.25, 1, 4, 16, 64, 256):
        w = weights*np.exp(g*(nodes-1))
        w /= w.sum()
        q = w@nodes
        t = w@((4*nodes**2-1)/3)
        ref = ive([2,3], g)/ive(1,g)
        assert np.allclose((q,t),ref,atol=1e-13,rtol=1e-12)
        assert np.isclose((1+3*t)/4-q*q, w@((nodes-q)**2), atol=1e-14)
        value = coefficients(q,t)
        print(f"g={g:g}  quadratic coefficient={value:.8f}")
    shift = Fraction(1,6)-Fraction(1,12)-Fraction(3,28)
    assert (Fraction(1,3)-Fraction(1,10)+24*shift)/4 == Fraction(-71,840)


if __name__ == "__main__":
    check()
