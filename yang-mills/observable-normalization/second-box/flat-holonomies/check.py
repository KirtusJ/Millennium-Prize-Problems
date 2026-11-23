"""Numerical cross-check in the position basis on the periodic cube (NumPy)."""
from itertools import product
from math import asinh, cos, fsum, pi, sin, sqrt

import numpy as np

MASKS = tuple(product(range(2), repeat=3))
ORIGIN = (0, 0, 0)


def symbol(mask, q):
    return sum(sin((pi * bit + angle) / 2) ** 2 for bit, angle in zip(mask, q))


def omega(s):
    return 2 * asinh(sqrt(s))


def position_spectrum(q):
    # One charged complex color, three complex link components at each site.
    # The conjugate color has the same spectrum for this two-site period.
    ident = np.eye(8)
    diffs = []
    for axis, angle in enumerate(q):
        perm = [i ^ (1 << (2 - axis)) for i in range(8)]
        diffs.append(np.exp(1j * angle) * ident[perm] - ident)
    curl = np.zeros((24, 24), dtype=complex)
    for row, (i, j) in enumerate(((0, 1), (0, 2), (1, 2))):
        block = slice(8 * row, 8 * (row + 1))
        curl[block, 8*j:8*(j+1)] = diffs[i]
        curl[block, 8*i:8*(i+1)] = -diffs[j]
    return np.linalg.eigvalsh(curl.conj().T @ curl)


def trace_energy(q, omit_zero):
    return 2 * fsum(omega(symbol(mask, q)) for mask in MASKS
                    if not omit_zero or mask != ORIGIN)


def main():
    for q in [ORIGIN, (.31, -.47, .83), (pi, 0, pi), (.2, pi, -.4)]:
        eigenvalues = [4 * symbol(mask, q) for mask in MASKS for _ in range(2)]
        np.testing.assert_allclose(position_spectrum(q), sorted([0]*8 + eigenvalues),
                                   atol=3e-14, rtol=2e-14)
    # Integrate the temporal log determinant for every hard shell.
    for s in (1, 2, 3):
        mean_log = fsum(np.log(2 + 4*s - 2*cos(2*pi*j/128)) for j in range(128)) / 128
        assert abs(mean_log - omega(s)) < 2e-14
    coeff = (1/sqrt(2) - 1/sqrt(6) - 1/sqrt(12)) / 2
    hard0 = trace_energy(ORIGIN, True)
    for direction in ((1, 0, 0), (.6, .8, 0), (1/3, 2/3, -2/3)):
        eps = .004
        def curvature(t):
            return (trace_energy(tuple(t*x for x in direction), True) - hard0) / t**2
        extrapolated = (4*curvature(eps/2) - curvature(eps))/3
        assert abs(extrapolated - coeff) < 3e-9
    full0 = trace_energy(ORIGIN, False)
    m = 7 / (2 * 12**1.5)
    for indices in product(range(9), repeat=3):
        q = tuple(pi*j/8 for j in indices)
        rise = trace_energy(q, False) - full0
        assert rise + 1e-13 >= 2*m*sum(sin(x)**2 for x in q)
    print(f"Position-space curl, temporal determinant, curvature {coeff:.12g} and 729 barrier checks passed.")


if __name__ == "__main__":
    main()
