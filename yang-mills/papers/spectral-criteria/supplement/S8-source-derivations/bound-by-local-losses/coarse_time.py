"""Equal-physical-time transfer comparison on transverse Wilson Gaussian fibres."""
from itertools import product

import numpy as np

from spectrum import PARITY, transverse


def energy_step(q):
    return 2 * np.arcsinh(np.linalg.norm(np.sin(q / 2)))


def compare_cell(k, side, times):
    coarse_frame = transverse(k)
    blocks, energies = [], []
    for ell in PARITY:
        q = k / 2 + np.pi * np.array(ell)
        step_energy = energy_step(q)
        adjoint_filter = np.conj(1 + np.exp(1j * q))[:, None]
        frame = transverse(q)
        block = frame.conj().T @ (adjoint_filter * coarse_frame)
        blocks.append(block / np.sqrt(2 * np.sinh(step_energy)))
        energies.extend([side * step_energy] * frame.shape[1])
    observation = np.vstack(blocks)
    gram = observation.conj().T @ observation
    values, vectors = np.linalg.eigh(gram)
    assert np.min(values) > 0
    isometry = observation @ ((vectors / np.sqrt(values)) @ vectors.conj().T)
    np.testing.assert_allclose(isometry.conj().T @ isometry, np.eye(2), atol=1e-12)
    coarse_energy = side / 2 * energy_step(k)
    assert min(energies) + 1e-12 >= coarse_energy
    ratios = []
    for t in times:
        # Scale out the common coarse multiplier to test the order relatively.
        multipliers = np.exp(-t * (np.array(energies) - coarse_energy))
        matrix = isometry.conj().T @ (multipliers[:, None] * isometry)
        ratios.append(np.linalg.eigvalsh(matrix)[-1])
    # Give the coarse system twice the physical time at t=1/4.
    wrong_clock = ratios[-1] * np.exp(times[-1] * coarse_energy)
    return np.array(ratios), wrong_clock


if __name__ == "__main__":
    times = (0, 1 / 16, 1 / 4)
    for side in (6, 8, 12, 16, 24):
        coarse_side = side // 2
        maximum = np.zeros(len(times))
        wrong_max = 0
        for indices in product(range(coarse_side), repeat=3):
            if not any(indices):
                continue
            k = 2 * np.pi * np.array(indices) / coarse_side
            ratios, wrong = compare_cell(k, side, times)
            maximum = np.maximum(maximum, ratios)
            wrong_max = max(wrong_max, wrong)
        assert abs(maximum[0] - 1) < 1e-12
        assert all(maximum[1:] <= 1 + 1e-12) and wrong_max > 1.01
        print(f"N={side}, largest normalized eigenvalues {maximum}, wrong clock {wrong_max:.6g}")
