"""Deterministic free-field packet and spectral window controls. Requires NumPy."""
from math import pi
import numpy as np
from numpy.polynomial.legendre import leggauss


def rule(lo, hi, order, width=pi):
    points, weights = leggauss(order)
    cuts = np.linspace(lo, hi, int(np.ceil((hi-lo)/width)) + 1)
    half = np.diff(cuts)[:, None]/2
    return ((cuts[:-1, None] + half*(1+points)).ravel(),
            (half*weights).ravel())


def packet_moments(radius, order, cutoff=48):
    """One-color Fourier integrals at offsets 0,1,2 and scaled lags 0,1,2."""
    end = pi*radius if radius is not None else cutoff
    p, w = rule(0., end, order)
    spatial = np.sinc(p/(2*pi))
    if radius is None:
        h = p
    else:
        spatial /= np.sinc(p/(2*pi*radius))
        h = 2*radius*np.sin(p/(2*radius))
    weights = w*spatial**8/pi
    yz = weights[:, None]*(weights*(2*np.sin(p/2))**6)[None, :]
    result = np.zeros((3, 3))
    for x, hx, wx in zip(p, h, weights):
        length = np.sqrt(hx**2+h[:, None]**2+h[None, :]**2)
        if radius is None:
            scaled_energy, denominator = length, 2*length
        else:
            scaled_energy = 2*radius*np.arcsinh(length/(2*radius))
            denominator = 2*length*np.sqrt(1+(length/(2*radius))**2)
        mass = wx*yz*(hx**2+h[:, None]**2)/denominator
        decay = np.exp(-scaled_energy)
        moments = [mass.sum(), (mass*decay).sum(), (mass*decay**2).sum()]
        result += np.outer(np.cos(np.arange(3)*x), moments)
    return result


def connected(covariance, variance, s=4.):
    d = 1+2*s*variance
    # expm1 preserves accuracy when the off-diagonal covariance is small.
    return np.expm1(-1.5*np.log1p(-(2*s*covariance/d)**2))/d**3


def band_submeasure(order, variance, s=4.):
    """Lower matrix for the band (2,4.2), restricting both momenta to boxes."""
    box = [(0.18, 0.93), (0.62, 0.92), (1.11, 1.52)]
    extrema = np.asarray(box)
    assert 2*np.linalg.norm(extrema[:, 0]) > 2
    assert 2*np.linalg.norm(extrema[:, 1]) < 4.2
    pts, ws = zip(*(rule(lo, hi, order) for lo, hi in box))
    x, y, z = np.meshgrid(*pts, indexing="ij", sparse=True)
    # All eight reflections of each box are included independently.
    w = ws[0][:, None, None]*ws[1][None, :, None]*ws[2][None, None, :]/pi**3
    w = w*(x*x+y*y)/(2*np.sqrt(x*x+y*y+z*z))*(2*np.sin(z/2))**6
    for coord in (x, y, z):
        w *= np.sinc(coord/(2*pi))**8
    positions = np.arange(4)
    differences = positions[:, None]-positions[None, :]
    first = np.array([(w*np.cos(j*x)).sum() for j in positions])
    b1 = 6*s*s/(1+2*s*variance)**5
    band = b1*first[np.abs(differences)]**2
    # Deliberately duplicate the last displacement to destroy full rank.
    duplicated = band[np.ix_([0, 1, 2, 2], [0, 1, 2, 2])]
    eig = np.linalg.eigvalsh(band)
    assert eig[0] > .001*eig[-1]
    assert abs(np.linalg.eigvalsh(duplicated)[0]) < 1e-12*eig[-1]
    return eig


def main():
    free = packet_moments(None, 12)
    np.testing.assert_allclose(free, packet_moments(None, 9, 36),
                               rtol=5e-7, atol=2e-10)
    print("Continuum packet variance and lag 1,2 covariances", free[0])
    print("Connected packet at lag 0,1,2", connected(free[0], free[0, 0]))
    errors = []
    for radius in [4, 8, 16, 32]:
        result = packet_moments(radius, 12)
        if radius == 8:
            np.testing.assert_allclose(result, packet_moments(radius, 16),
                                       rtol=2e-6, atol=2e-9)
        errors.append(np.max(np.abs(result-free)))
        print(f"R={radius:2} maximum absolute discrepancy, nine moments: {errors[-1]:.6g}")
    assert all(3.4 < x/y < 4.6 for x, y in zip(errors, errors[1:]))
    low = band_submeasure(8, free[0, 0])
    high = band_submeasure(14, free[0, 0])
    np.testing.assert_allclose(low, high, rtol=1e-10)
    print("Two-leg restricted band (2,4.2), four eigenvalues", high)


if __name__ == "__main__":
    main()
