"""Cross-check the Fourier sum against the position-space twisted curl."""
from itertools import product
from math import asinh, dist, fsum, pi, sin, sqrt

import numpy as np

SITES = list(product(range(2), repeat=3))


def frequencies(angles):
    result = []
    for bits in SITES:
        squared = fsum(sin(pi * bit / 2 + a / 4) ** 2 for bit, a in zip(bits, angles))
        result.append(2 * asinh(sqrt(squared)))
    return sorted(result)


def real_space(angles):
    # One complex adjoint charge represents the two real charged colors.
    ident = np.eye(8)
    differences = []
    for axis, angle in enumerate(angles):
        neighbor = [SITES.index(tuple(bit ^ (i == axis) for i, bit in enumerate(site)))
                    for site in SITES]
        differences.append(np.exp(0.5j * angle) * ident[neighbor] - ident)
    curl = np.zeros((24, 24), dtype=complex)
    for row, (i, j) in enumerate(((0, 1), (1, 2), (2, 0))):
        rows = slice(8 * row, 8 * (row + 1))
        curl[rows, 8*j:8*(j+1)] = differences[i]
        curl[rows, 8*i:8*(i+1)] = -differences[j]
    return np.sort(2 * np.arcsinh(np.linalg.svd(curl, compute_uv=False) / 2))


def main():
    error = 0.
    for angles in product((0., pi / 3, pi, 2 * pi), repeat=3):
        expected = sorted([0.] * 8 + frequencies(angles) * 2)
        error = max(error, np.max(np.abs(real_space(angles) - expected)))
    assert error < 2e-13, error

    # Use the singular-value sum as an independent measurement of the barrier.
    origin = (0., 0., 0.)
    barrier = fsum(real_space((pi, 0., 0.))) - fsum(real_space(origin))
    f = lambda x: asinh(sqrt(x))
    exact = 4*(2*f(.5) + 4*f(1.5) + 2*f(2.5) - 3*f(1) - 3*f(2) - f(3))
    assert abs(barrier - exact) < 2e-13
    for direction in ((1., 0., 0.), (1., 2., -3.)):
        offset = np.array(direction) * 1.e-5
        ratio = (fsum(real_space(offset)) - fsum(real_space(origin))) / dist(offset, origin)
        assert abs(ratio - 1.) < 1.e-5, ratio
    # On the single-coordinate path, remove the endpoint square-root singularity.
    from scipy.integrate import quad
    from math import comb
    def weighted_axis(u):
        x = sin(u*u/4)**2
        value = 4*fsum(comb(2, j)*(f(j+x)-f(j) + f(j+1-x)-f(j+1)) for j in range(3))
        return 2*u*sqrt(value)
    length = 2*quad(weighted_axis, 0, sqrt(pi), epsabs=1e-12, epsrel=1e-12)[0]
    print(f"Scalar weighted axis length {length:.12f}")
    print(f"64 spectra, maximum frequency error {error:.3g}, barrier {barrier:.12f}, two cusp slopes checked")


if __name__ == "__main__":
    main()
