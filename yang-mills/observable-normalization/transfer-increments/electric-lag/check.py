"""Numerical controls for the Haar moments and two-lag Gaussian comparison."""
from math import cos, pi, sin, sqrt, tanh

import numpy as np
from scipy.integrate import quad
from scipy.stats import binom, norm


def haar_trace_moment(k):
    def integrand(angle):
        return (2 / pi) * sin(angle)**2 * (2 * cos(angle))**k

    return quad(integrand, 0, pi)[0]


def two_tilts(size, high, low):
    counts = np.arange(size + 1)
    score = (2 * counts - size) / sqrt(size)
    probs = [(1 + tanh(h / sqrt(size))) / 2 for h in (high, low)]
    first, second = (binom.pmf(counts, size, p) for p in probs)
    diff = first - second
    midpoint = diff[score > (high + low) / 2].sum()
    tv = np.abs(diff).sum() / 2
    p = probs[0]
    information = size * (p * np.log(2*p) + (1-p) * np.log(2*(1-p)))
    return tv, midpoint, information


if __name__ == "__main__":
    moments = [haar_trace_moment(k) for k in range(5)]
    np.testing.assert_allclose(moments, [1, 0, 1, 0, 2], atol=1e-12)
    for high, low in [(0.95, 0.25), (1.3, 0), (0.8, 0.8)]:
        target = 2 * norm.cdf((high - low) / 2) - 1
        for size in (64, 256, 1024, 16384):
            tv, midpoint, information = two_tilts(size, high, low)
            assert midpoint <= tv + 1e-12
            print(size, high, low, *(f"{x:.8f}" for x in (tv, midpoint, information)))
        np.testing.assert_allclose([tv, midpoint, information],
                                   [target, target, high**2/2], atol=2e-4, rtol=0)
