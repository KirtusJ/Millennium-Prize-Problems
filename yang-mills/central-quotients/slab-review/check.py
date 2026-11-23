"""Independent matrix and quadrature controls. Run with NumPy and SciPy."""
from itertools import product

import numpy as np
from scipy.integrate import quad
from scipy.special import ive


def check_twists():
    largest_error = 0.0
    for side in (4, 6, 8):
        axes = np.indices((side,) * 3)
        for twist in product(range(2), repeat=3):
            angles = np.pi * np.tensordot(twist, axes, axes=(0, 0)) / side
            spins = np.exp(1j * angles)
            measured = 0.0
            spectral_bound = 0.0
            for axis, bit in enumerate(twist):
                hop = np.roll(np.eye(side), 1, axis=1)
                hop[-1, 0] = (-1) ** bit
                maximum = np.linalg.eigvalsh((hop + hop.T) / 2)[-1]
                spectral_bound += side**3 * (1 - maximum)
                seams = np.ones((side,) * 3)
                seams[axes[axis] == side - 1] = (-1) ** bit
                product_on_links = spins.conj() * np.roll(spins, -1, axis=axis)
                measured += np.sum(1 - seams * product_on_links.real)
            formula = sum(twist) * side**3 * (1 - np.cos(np.pi / side))
            largest_error = max(largest_error, abs(measured-formula), abs(spectral_bound-formula))
    assert largest_error < 1e-10
    return largest_error


def check_interpolation():
    # Symmetric, strictly positive stochastic matrix with two distinct decay rates.
    transition = np.array([[0.7, 0.2, 0.1], [0.2, 0.5, 0.3], [0.1, 0.3, 0.6]])
    f = np.array([-2., 0.5, 1.5])
    assert abs(np.sum(f)) < 1e-14
    values, basis = np.linalg.eigh(transition)
    assert np.all(values > 0)
    masses = (basis.T @ f)**2 / 3
    for lag in (1, 2, 5):
        step = np.linalg.matrix_power(transition, lag)
        g = np.linalg.solve(np.eye(3) + step @ step, step @ f)
        error = joint_error = 0.
        for left, right in product(range(3), repeat=2):
            weights = step[left, :] * step[:, right] / 3
            bridge = weights @ f / np.sum(weights)
            error += weights @ (f - g[left] - g[right])**2
            joint_error += weights @ (f - bridge)**2
        powers = values**(2*lag)
        predicted = masses @ ((1 - powers) / (1 + powers))
        np.testing.assert_allclose(error, predicted, atol=1e-13, rtol=1e-13)
        assert joint_error < error < masses @ (1 - powers)


def check_tilt():
    # Independent angular Haar quadrature for the transverse one-link variance.
    for tilt in (0.01, 0.2, 1., 6., 40., 160.):
        def integral(power):
            return quad(lambda angle: np.exp(tilt*(np.cos(angle)-1)) * np.sin(angle)**power,
                        0, np.pi, epsabs=1e-14, epsrel=1e-13)[0]
        variance = integral(4) / (3*integral(2))
        bessel = ive(2, tilt) / (tilt*ive(1, tilt))
        np.testing.assert_allclose(variance, bessel, atol=1e-13, rtol=1e-13)
        assert variance > 1 / (4 + tilt)


if __name__ == "__main__":
    print(f"24 compact twist controls, largest absolute discrepancy {check_twists():.3g}")
    check_interpolation()
    print("Three Markov lags distinguish additive from unrestricted conditional prediction.")
    check_tilt()
    print("Six one-link quadratures reproduce the transverse variance and its lower bound.")
