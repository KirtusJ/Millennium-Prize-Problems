"""Independent quadratures for the shared-clock moving magnetic threshold."""
from math import pi, sqrt
import numpy as np
from numpy.polynomial.legendre import leggauss


def nodes(order, lower, upper):
    x, w = leggauss(order)
    return lower + (upper-lower)*(x+1)/2, w*(upper-lower)/2


def segmented(stop, breaks, order):
    intervals = sorted({0., stop, *(v for v in breaks if 0 < v < stop),
                        *np.arange(1., stop, 1.)})
    x, w = nodes(order, 0, 1)
    width = np.diff(intervals)[:, None]
    return (np.array(intervals[:-1])[:, None]+width*x).ravel(), (width*w).ravel()


def filter_squared(x, m):
    # x is m times the unscaled squared radial coordinate.
    n = 2*(m-1)
    angle = np.arcsin(np.sqrt(-np.expm1(-3*x/(2*n*m))))
    ratio = np.sinc(m*angle/np.pi) / np.sinc(angle/np.pi)
    return np.exp(-x/m)*ratio**8


def pushed(m, k, cutoff=4., order=20):
    r = k*sqrt(m)
    y, dy = segmented(sqrt(55*m), [r, sqrt(cutoff), np.hypot(r, sqrt(cutoff))], order)
    x = y*y
    weight = dy*2*y*filter_squared(x, m)
    if k == 0:
        w = weight*y**3
        return np.array([w.sum(), w @ x, w[x < cutoff].sum()])
    top = np.minimum(r, y)
    v, dv = nodes(48, 0., 1.)

    def angular(bottom):
        width = np.maximum(0., top-bottom)
        z = bottom[:, None] + width[:, None]*v
        excess = x[:, None] - z*z
        density = (excess**2 + (r*r-z*z)**2) / np.sqrt(r*r+excess)
        return width/r*(density @ dv), width/r*((density*excess) @ dv)

    density, moment = angular(np.zeros_like(x))
    inside, _ = angular(np.sqrt(np.maximum(0., x-cutoff)))
    return np.array([weight @ density, weight @ moment, weight @ inside])


def direct(m, k, cutoff=4.):
    # Integrate first in |z|/k and then in sqrt(m(E^2-k^2)).
    r = sqrt(m)*k
    t, dt = segmented(sqrt(55*m), [sqrt(cutoff)], 24)
    v, dv = nodes(100, 0, 1)
    z = r*v
    h = t[:, None]**2
    weight = (2*dt*t/np.hypot(t, r)) * (
        ((h**2+(r*r-z*z)**2)*filter_squared(h+z*z,m)) @ dv)
    return np.array([sum(weight), weight @ t**2, sum(weight[t*t < cutoff])])


def geometry():
    v, w = nodes(80, 0, 1)
    worst = 0.
    margins = []
    for x in np.geomspace(1e-8, 1e6, 181):
        top = min(1., sqrt(x))

        def mass(lo):
            if lo >= top:
                return 0.
            z = lo+(top-lo)*v
            excess = x-z*z
            return (top-lo)*w @ ((excess**2+(1-z*z)**2)/np.sqrt(1+excess))

        full = mass(0.)
        margins.append(full/(sqrt(x)*(1+x)))
        for fraction in (0.5, 0.25, 0.1, 0.01, 0.001):
            near = mass(sqrt(x*(1-fraction)))
            worst = max(worst, near/(fraction*full))
    assert min(margins) >= 1/32 and max(margins) <= 5 and worst <= 48
    return min(margins), max(margins), worst


if __name__ == "__main__":
    print("dimensionless density min/max and largest conditional ratio", geometry())
    for m in (8, 32):
        for k in (0., .125, 1., 3.):
            np.testing.assert_allclose(pushed(m,k), direct(m,k), rtol=2e-6, atol=1e-10)
    print("Eight direct energy integrals agree with the pushed radial calculations.")
    for k in (0., 1.):
        for m in (16, 64, 256, 1024, 4096):
            mass, moment, band = pushed(m,k)
            print(f"k={k:g} m={m:4} scaled squared excess={moment/mass:.8f} "
                  f"fraction below scaled cutoff 4={band/mass:.8f}")
    # Check the three limiting integrals separately, including a tail bound.
    stop = 128*pi
    v, dv = segmented(stop, [], 14)
    for denominator_power, expected in ((2, 5*pi/32), (4, pi/12), (6, pi/12)):
        partial = dv @ (np.sin(v)**8 / v**denominator_power)
        tail = stop**(1-denominator_power)/(denominator_power-1)
        assert partial-1e-13 <= expected <= partial+tail+1e-13
    print("Three trigonometric integrals agree within quadrature and analytic tail allowances.")
