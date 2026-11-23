"""One-color tail constants from deterministic quadrature on long coordinate slabs."""
from math import pi
import numpy as np
from numpy.polynomial.legendre import leggauss


def quadrature(start_period, stop_period, order):
    nodes, weights = leggauss(order)
    centers = (2*np.arange(start_period, stop_period)+1)*pi
    return (centers[:,None]+pi*nodes).ravel(), np.tile(pi*weights, len(centers))


def slab(k, axis, finite, order=20):
    h = 2*pi*k
    radius = int(np.ceil(h*h)) if finite else None
    x, wx = quadrature(k, 4*k, order)
    y, wy = quadrature(0, 5, order)

    def factors(p):
        scaled = p if radius is None else p*np.sinc(p/(2*pi*radius))
        box = (2*np.sin(p/2)/scaled)**8
        return scaled**2, box, (2*np.sin(p/2))**6

    xs, xb, xd = factors(x)
    ys, yb, yd = factors(y)
    yz = ys[:,None]+ys[None,:]
    weights = np.outer(wy*yb, wy*yb)
    if axis == 1:
        weights *= yd[None,:]
    total = 0.
    for large, mass, difference in zip(xs, wx*xb, xd):
        norm = np.sqrt(large+yz)
        denom = 2*norm if radius is None else 2*norm*np.sqrt(1+(norm/(2*radius))**2)
        numerator = large+ys[:,None] if axis == 1 else difference*yz
        total += mass*np.sum(weights*numerator/denom)
    # Integrate both tail signs and all four transverse sign choices.
    return h**(6 if axis == 1 else 8)*total/pi**3


if __name__ == "__main__":
    for axis, power, target in [(1,6,25217/(3240*pi)), (3,8,43186/(315*pi))]:
        expected = target*(1-4**(-power))
        for finite in [False, True]:
            values = [slab(k,axis,finite) for k in [4,12,24]]
            assert abs(values[-1]/expected-1) < .012
            assert abs(values[-1]-expected) < abs(values[0]-expected)
            assert abs(slab(24,axis,finite,24)-values[-1]) < 2e-7*expected
            print("axis",axis,"finite",finite,"scaled slabs",np.round(values,7),"limit",expected)
