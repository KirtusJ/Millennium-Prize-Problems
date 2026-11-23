"""Independent hard-leg Fourier marks, finite lattice slabs, and aliases."""
from math import comb, factorial, pi
import numpy as np
from numpy.polynomial.legendre import leggauss


def spline(n, x, derivative=0):
    # Even splines and their even derivatives; evaluate on the left half.
    power = n-1-derivative
    return sum((-1)**j*comb(n,j)*max(n/2-abs(x)-j, 0.)**power
               for j in range(n+1))/factorial(power)


def hard_mark(a, b):
    return ((spline(8,a,2)*spline(8,b)+spline(8,a)*spline(8,b,2))
            /(2*spline(8,0,2)*spline(8,0)))


def period_nodes(first, last):
    x, w = leggauss(20)
    return (((2*np.arange(first,last)+1)[:,None]*pi+x*pi).ravel(),
            np.tile(w*pi,last-first))


def slab(k):
    x, wx = period_nodes(k, 2*k)
    q, wq = period_nodes(0, 8)
    r = int(np.ceil(x[0]**2))
    hq = q*np.sinc(q/(2*pi*r))
    wq *= (2*np.sin(q/2)/hq)**8
    h2 = hq[:,None]**2+hq**2
    weights = h2*wq[:,None]*wq
    targets = [(0.,0.), (1.,.5), (4.5,0.)]
    marks = [np.cos(a*q)[:,None]*np.cos(b*q) for a,b in targets]
    mass = np.zeros_like(weights)
    for p, w in zip(x,wx):
        hp = p*np.sinc(p/(2*pi*r))
        length = np.sqrt(h2+hp**2)
        mass += (w*(2*np.sin(p/2))**14/hp**8
                 /(length*np.sqrt(1+(length/(2*r))**2)))
    vals = np.array([np.sum(weights*mass*mark) for mark in marks])
    return vals/vals[0]


def aliases():
    for r in [4, 9, 23]:
        shifts = np.arange(-6*r,6*r+1)
        weights = np.array([spline(12,z/r) for z in shifts])/r
        for p in [0., 2.3, .9*pi*r, -pi*r, pi*r-.01]:
            actual = np.sum(weights*np.cos(shifts*p/r))
            direct = sum(np.sinc((p+2*pi*r*j)/(2*pi))**12 for j in range(-4,5))
            np.testing.assert_allclose(actual,direct,rtol=0,atol=2e-12)


if __name__ == "__main__":
    expected = np.array([1,hard_mark(1,.5),hard_mark(4.5,0)])
    print("Hard-leg characteristic function targets", expected)
    readings = [slab(k) for k in [4,12,24]]
    for k,reading in zip([4,12,24],readings):
        print("Normal slab, H/(2 pi) =",k,reading)
    assert abs(readings[-1][1]-expected[1]) < 2e-4
    assert abs(readings[-1][2]) < 1e-7
    assert abs(readings[-1][1]-expected[1]) < abs(readings[0][1]-expected[1])
    aliases()
    print("15 transverse periodizations, including both representative seams")
