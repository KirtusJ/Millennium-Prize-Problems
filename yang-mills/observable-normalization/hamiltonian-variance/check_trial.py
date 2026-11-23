"""Independent quadrature of the one-link trial moments and kinetic normalization."""
from fractions import Fraction
import numpy as np
from scipy.special import roots_jacobi


def trial(m):
    kinetic = Fraction(3*m*m, 4*(4*m+1))
    mean = Fraction(2*m, 2*m+3)
    variance = Fraction(12*(4*m+3), (2*m+3)**2*(2*m+4))
    return kinetic, mean, variance


def main():
    x, w = roots_jacobi(256, 0.5, 0.5)
    worst = 0.
    wrong = 0.
    for m in (0, 1, 2, 5, 16, 64):
        weights = w * ((1+x)/2)**(2*m)
        weights /= weights.sum()
        mean = weights @ x
        variance = weights @ ((2*(x-mean))**2)
        kinetic = (m*m/4) * (weights @ ((1-x)/(1+x)))
        expected = trial(m)
        worst = max(worst, *(abs(val-float(ref)) for val, ref in
                             zip((kinetic, mean, variance), expected)))
        wrong = max(wrong, abs(4*kinetic - float(expected[0])))
    if worst > 1e-9 or wrong < 1:
        raise ValueError((worst, wrong))
    print(f"maximum absolute residual {worst:.4g}; wrong generator residual {wrong:.4g}")
    for g in (Fraction(1,4), Fraction(1), Fraction(4), Fraction(16)):
        m = int(6*float(g)**0.5)
        kinetic, mean, _ = trial(m)
        energy = kinetic + g*(1-mean**4)
        if energy > Fraction(17,8)*Fraction(m,6)+Fraction(3,16):
            raise ValueError((g, m, energy))


if __name__ == "__main__":
    main()
