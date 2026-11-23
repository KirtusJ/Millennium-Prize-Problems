"""Quadrature for the Fourier review. Integrates in units of the tilt time."""
import numpy as np
from numpy.polynomial.legendre import leggauss

PI = np.pi
LEADING = 2880/PI**2


def covariance(radius, time, offset, order=7, cutoff=72):
    """Return t^10 C(t, t*offset) and its discrete counterpart at R."""
    end = cutoff if radius is None else min(cutoff, PI*radius*time)
    edges = np.linspace(0, end, 1+int(np.ceil(end/4)))
    nodes, weights = leggauss(order)
    half = np.diff(edges)[:, None]/2
    p = (edges[:-1, None]+(1+nodes)*half).ravel()
    weights = (half*weights).ravel()
    if radius is None:
        h = p
        filter_base = np.sinc(p/(2*PI*time))
    else:
        h = p*np.sinc(p/(2*PI*time*radius))
        filter_base = np.sinc(p/(2*PI*time))/np.sinc(p/(2*PI*time*radius))
    base = weights*filter_base**8/PI
    axes = [base*np.cos(u*p) for u in offset]
    yz = axes[1][:, None]*(axes[2]*(2*time*np.sin(p/(2*time)))**6)[None, :]
    total = 0.
    for x, mass in zip(h, axes[0]):
        radial = np.sqrt(x*x+h[:, None]**2+h[None, :]**2)
        energy, correction = radial, 1.
        if radius is not None:
            scaled = radial/(2*radius*time)
            energy = 2*time*radius*np.arcsinh(scaled)
            correction = np.sqrt(1+scaled**2)
        total += mass*np.sum(yz*(x*x+h[:, None]**2)/(2*radial*correction)*np.exp(-energy))
    return total


if __name__ == "__main__":
    for offset in [(0, 0, 0), (.3, -.25, .5)]:
        for radius in [1, 3]:
            scaled_errors = []
            for time in [16, 32, 64]:
                lattice = covariance(radius, time, offset)
                limit = covariance(None, time, offset)
                scaled_errors.append((lattice-limit)*radius**2*time**2)
                if offset == (0, 0, 0) and time == 64:
                    assert abs(lattice/LEADING-1) < .04
                refined = covariance(radius, time, offset, 9, 84)
                assert abs(refined-lattice) < 3e-6
            print("offset", offset, "R", radius, "R²t¹²(C_R−C)", np.round(scaled_errors, 4))
            assert abs(scaled_errors[-1]/scaled_errors[-2]-1) < .22
    print("Leading scalar coefficient", LEADING)
