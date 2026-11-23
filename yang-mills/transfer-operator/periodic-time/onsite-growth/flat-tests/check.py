"""Independent lattice time-slice quadratures and scaled temporal mesh sums."""
from math import pi, sqrt

import numpy as np
from numpy.polynomial.legendre import leggauss


def lattice_slice(mass, y, order):
    # Resolve the exceptional low-momentum region but include the full cube.
    limit = pi * sqrt(y) / mass
    nodes, weights = leggauss(order)
    length = limit / (1 + limit)
    u = (nodes + 1) * length / 2
    q = u / (1 - u)
    p = mass * q / sqrt(y)
    w = length * weights / (2 * (1 - u) ** 2)
    h = (2 * np.sin(p / 2)) ** 2
    h2 = h[:, None, None] + h[None, :, None] + h[None, None, :]
    omega = 2 * np.arcsinh(np.sqrt((2 * np.sinh(mass / 2)) ** 2 + h2) / 2)
    delta = 2 * np.arcsinh(h2 / (4 * np.sinh((omega + mass) / 2)))
    density = np.exp(-2 * y * delta / mass) * (mass / (2 * np.sinh(omega))) ** 2
    weights3 = w[:, None, None] * w[None, :, None] * w[None, None, :]
    integral = np.sum(weights3 * density)
    sin2 = np.sin(p) ** 2
    grad2 = ((y + mass / np.tanh(omega)) / sqrt(y) / np.sinh(omega)) ** 2 * (
        sin2[:, None, None] + sin2[None, :, None] + sin2[None, None, :])
    return integral / pi ** 3, np.sum(weights3 * density * grad2) / integral


def temporal_sum(d, a, spacing):
    center = sqrt(a * d / 2)
    y = spacing * np.arange(1, int((6 * center + 32) / spacing))
    # Evaluate after division by the leading exponential.
    weights = y ** -1.5 * np.exp(-2 * (y - center) ** 2 / y)
    exact = sqrt(pi / (a * d))
    return spacing * weights.sum() / exact, weights[abs(y-center) <= d**.25].sum() / weights.sum()


def full_time_sum(mass, d, order):
    # Sum actual three-momentum integrals across the time saddle. Factor out
    # the dominant exponential before summation to retain relative precision.
    scale = mass / d ** .25
    upper = pi / scale
    nodes, weights = leggauss(order)
    u = (nodes + 1) * upper / (2 * (1 + upper))
    p = scale * u / (1 - u)
    w = scale * weights * upper / (2 * (1 + upper) * (1 - u) ** 2)
    h = (2 * np.sin(p / 2)) ** 2
    h2 = h[:, None, None] + h[None, :, None] + h[None, None, :]
    omega = 2 * np.arcsinh(np.sqrt((2 * np.sinh(mass / 2)) ** 2 + h2) / 2)
    delta = 2 * np.arcsinh(h2 / (4 * np.sinh((omega + mass) / 2)))
    amplitude = (w[:, None, None] * w[None, :, None] * w[None, None, :]
                 / (4 * pi ** 3 * np.sinh(omega) ** 2))
    multiplier = np.exp(-2 * delta)
    integrand = amplitude.copy()
    a = np.array([.25, .5, 1.])
    centers = np.sqrt(a * d / 2)
    total = np.zeros_like(a)
    for n in range(1, int((6 * centers.max() + 32) / mass) + 1):
        integrand *= multiplier
        y = n * mass
        total += integrand.sum() * np.exp(-2 * (y - centers) ** 2 / y)
    reference = np.sqrt(pi / (a * d)) / (32 * pi ** 1.5)
    return total / reference


if __name__ == "__main__":
    mass = 1 / 16
    continuum = 1 / (32 * pi ** 1.5)
    for y in (4, 16, 64, 256):
        low, high = [lattice_slice(mass, y, n) for n in (40, 60)]
        np.testing.assert_allclose(low, high, rtol=5e-6)
        print("Mn =", y, "slice/continuum =", high[0] / continuum,
              "scaled spatial second moment =", high[1])
    assert abs(high[0] / continuum - 1) < .01 and abs(high[1] - 1.5) < .03
    for a in (.25, .5, 1.):
        logs = []
        for d in (256, 1024, 4096):
            ratio, fraction = temporal_sum(d, a, mass)
            assert abs(ratio - 1) < 1e-10 and fraction > .8
            logs.append(np.log(ratio * sqrt(pi / (a * d))) + (2-2*sqrt(2*a))*sqrt(d))
        print("a =", a, "log heavy weights", np.round(logs, 4))
        assert (logs[-1] > logs[0]) == (a < .5)
    print("nine temporal mesh sums, including critical a = 1/2")
    for d in (256, 1024, 4096):
        low, high = [full_time_sum(.125, d, n) for n in (32, 48)]
        np.testing.assert_allclose(low, high, rtol=3e-5)
        assert np.all(abs(high - 1) < .15)
        print("full lattice heavy sum, d =", d, "ratios to saddle", np.round(high, 6))
