"""Enclose a change of sign of the cubic-box mass curvature using rational arithmetic."""
from fractions import Fraction as F
from math import factorial


def bessel(order, gamma, terms=15):
    half = gamma/2
    term = half**order/factorial(order)
    partial = term
    for k in range(1,terms):
        term *= half**2/(k*(k+order))
        partial += term
    ratio = half**2/(terms*(terms+order))
    assert 0 < ratio < 1
    return partial, partial + term*ratio/(1-ratio)


def bound(gamma):
    i1,i2,i3 = (bessel(j,gamma) for j in range(1,4))
    u = (i2[0]/i1[1], i2[1]/i1[0])
    v = (i3[0]/i1[1], i3[1]/i1[0])

    def f(z):
        assert 0 < z < 1
        return (1+z)/(1-z)

    c = [f(x**4) for x in u]
    h = [f((v[i]/u[1-i])**4) for i in (0,1)]
    g = [(f(u[i]**2)+3*f(u[i]**2*v[i]))/4 for i in (0,1)]
    return tuple((26*c[i]-h[1-i]-24*g[1-i])/4 for i in (0,1))


if __name__ == "__main__":
    left, right = F("1.30638009"), F("1.30638010")
    low, high = bound(left), bound(right)
    assert low[0] > 0 and high[1] < 0
    assert bound(F(1))[0] > 0 and bound(F(2))[1] < 0
    for gamma,interval in ((left,low), (right,high)):
        print(f"gamma {float(gamma):.8f}, sign {1 if interval[0]>0 else -1}, "
              f"curvature near {float(interval[0]):.12g}, enclosure width {float(interval[1]-interval[0]):.3g}")
