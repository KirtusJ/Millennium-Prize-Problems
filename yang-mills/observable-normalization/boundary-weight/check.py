"""Integer Dirichlet trials for the diagonals of nested open cubes."""
from fractions import Fraction
import numpy as np
from scipy.fft import dstn, idstn


def excess(side):
    mid = side // 2
    source = np.zeros((side,) * 3)
    source[mid - 1, mid - 1, mid - 1] = 1
    source[mid, mid - 1, mid - 1] = -1
    freq = 2 - 2 * np.cos(np.pi * np.arange(1, side + 1) / (side + 1))
    eigenvalues = freq[:, None, None] + freq[None, :, None] + freq[None, None, :]
    trial = idstn(dstn(source, type=1) / eigenvalues, type=1)
    scale = 10**7
    values = np.rint(scale * trial).astype(np.int64)
    padded = np.pad(values, 1)
    # Use Python integers for each square and the sum. Zero padding includes
    # each exterior bond once. The resulting certificate tolerates rounding.
    energy = sum(int(x)**2 for axis in range(3) for x in np.diff(padded, axis=axis).flat)
    dipole = int(values[mid - 1, mid - 1, mid - 1]) - int(values[mid, mid - 1, mid - 1])
    resistance = Fraction(2 * scale * dipole - energy, scale**2)
    return 2 - 6 * resistance


if __name__ == "__main__":
    for side, bound in [(4, Fraction(28739, 10**6)), (8, Fraction(3812, 10**6)),
                        (16, Fraction(532, 10**6)), (32, Fraction(72, 10**6))]:
        epsilon = excess(side)
        print(side, epsilon, float(epsilon))
        assert 0 <= epsilon < bound
