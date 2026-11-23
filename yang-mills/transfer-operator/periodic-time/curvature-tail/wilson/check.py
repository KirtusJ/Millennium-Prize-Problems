"""Free radial total variation and a one-link compact Wilson conditional control."""
from math import exp, pi, sin, sqrt
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.stats import ncx2


def log_sinhc(z):
    z = np.atleast_1d(np.asarray(z, dtype=float))
    out = np.empty_like(z)
    small = z < .08
    w = z[small]**2
    out[small] = w*(1/6+w*(-1/180+w*(1/2835-w/37800)))
    v = z[~small]
    out[~small] = v-np.log(2*v)+np.log(-np.expm1(-2*v))
    return out


def radial_coefficient(u, order):
    # Independent chi_3 radii. Splitting at sqrt(3) resolves the leading cusp.
    cuts = [0, 1, sqrt(3), 2.6, 4, 6, 10, 14]
    nodes, weights = leggauss(order)
    radii = np.concatenate([(lo+hi+(hi-lo)*nodes)/2 for lo, hi in zip(cuts, cuts[1:])])
    wr = np.concatenate([(hi-lo)*weights/2 for lo, hi in zip(cuts, cuts[1:])])
    wr *= sqrt(2/pi)*radii**2*np.exp(-radii**2/2)
    rr = radii[:, None]
    z = sqrt(u)*rr*radii/(1-u)
    log_ratio = -1.5*np.log1p(-u)-u*(rr**2+radii**2)/(2*(1-u))+log_sinhc(z)
    signed = np.expm1(log_ratio)
    assert abs(np.sum(wr[:, None]*wr*signed)) < 3e-14
    return np.sum(wr[:, None]*wr*np.abs(signed))/2


def one_link(beta, magnitude, stiffness):
    # Haar link tilted by exp[stiffness*beta*Re(S^-1 U)] with a deterministic
    # staple S at class angle magnitude/sqrt(beta). Work in the exact action y.
    theta = magnitude/sqrt(beta)
    def raw(y):
        radial = sqrt(max(0., y*(2-y/beta)))
        z = stiffness*sqrt(beta)*sin(theta)*radial
        return radial*exp(-stiffness*np.cos(theta)*y+float(log_sinhc(z)[0]))
    def scaled_gaussian(y):
        return 2*stiffness*ncx2.pdf(2*stiffness*y, 3, stiffness*magnitude**2)
    def integrate(f):
        return quad(f, 0, 2*beta, points=[1, 4, 10], epsabs=1e-11, limit=300)[0]
    mass = integrate(raw)
    return (integrate(lambda y: abs(raw(y)/mass-scaled_gaussian(y)))
            + ncx2.sf(4*stiffness*beta, 3, stiffness*magnitude**2))/2


def main():
    expected = 18*exp(-3)/pi
    print(f"Analytical small-u coefficient {expected:.10f}")
    for u in [.25, .0625, .015625, .001, .00001]:
        a = radial_coefficient(u, 48)
        b = radial_coefficient(u, 80)
        assert abs(a-b) < max(2e-5*u, 1e-11)
        print(f"u={u:.6g}: TV={b:.10g}, TV/u={b/u:.9f}")
        if u < .0001:
            assert abs(b/u-expected) < 1e-5
    for size in [0., .75]:
        distances = []
        for beta in [16, 64, 256]:
            value = one_link(beta, size, 2.)
            distances.append(value)
            print(f"one link, scaled staple={size:g}, beta={beta}, TV={value:.9g}")
        assert all(3.7 < x/y < 4.4 for x, y in zip(distances, distances[1:]))


if __name__ == "__main__":
    main()
