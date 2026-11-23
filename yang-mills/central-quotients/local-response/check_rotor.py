"""Finite character-cutoff checks of the one-square formulas in rotor.md."""
import numpy as np
from scipy.linalg import eigh_tridiagonal


def low_modes(size, coupling):
    n = np.arange(size, dtype=float)
    energies, states = eigh_tridiagonal(n*(n+2), np.full(size - 1, -coupling/2),
                                        select="i", select_range=(0, 1))
    ground, first = states.T.copy()
    for state, pivot in ((ground, 0), (first, 1)):
        if state[pivot] < 0:
            state *= -1

    # Exact compressed multiplication by chi_2 via SU(2) character products.
    adjoint_ground = ground.copy()
    adjoint_ground[0] = 0
    adjoint_ground[2:] += ground[:-2]
    adjoint_ground[:-2] += ground[2:]
    return energies[1]-energies[0], float(first @ adjoint_ground)


if __name__ == "__main__":
    for coupling in (0., 0.001, 0.01, 0.5, 2., -0.5):
        small = np.array(low_modes(18, coupling))
        large = np.array(low_modes(32, coupling))
        if np.max(np.abs(small-large)) > 2e-12:
            raise ValueError("cutoff comparison failed")
        gap, amplitude = large
        if coupling == 0 and (abs(gap-3) > 1e-12 or abs(amplitude) > 1e-15):
            raise ValueError("free center selection failed")
        if coupling and abs(coupling) <= .01 and abs(amplitude/coupling-4/15) > 1e-5:
            raise ValueError("wrong first-order adjoint amplitude")
        print(f"lambda={coupling:g}  gap={gap:.11f}  adjoint amplitude={amplitude:.11f}")
