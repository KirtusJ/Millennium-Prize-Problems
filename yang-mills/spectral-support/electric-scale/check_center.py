"""Construct the star from periodic plaquettes, then diagonalize its flux walk."""
from collections import Counter
from itertools import combinations, product
import numpy as np
from scipy.linalg import expm


def shift(x, axis, step, L):
    y = list(x)
    y[axis] = (y[axis] + step) % L
    return tuple(y)


def incident_masks(L):
    origin = (0, 0, 0)
    edges = [edge for i in range(3) for edge in ((origin, i), (shift(origin, i, -1, L), i))]
    rows = []
    for x in product(range(L), repeat=3):
        for a, b in combinations(range(3), 2):
            face = {(x, a), (shift(x, a, 1, L), b), (shift(x, b, 1, L), a), (x, b)}
            mask = sum(1 << i for i, edge in enumerate(edges) if edge in face)
            if mask:
                rows.append(mask)
    assert len(rows) == len(set(rows)) == 12
    return sorted(rows)


def star():
    rows = incident_masks(3)
    assert rows == incident_masks(4) == incident_masks(7)
    even = [n for n in range(64) if n.bit_count() % 2 == 0]
    generator = -len(rows) * np.eye(len(even))
    for i, n in enumerate(even):
        for r in rows:
            generator[i, even.index(n ^ r)] += 1
    spectrum = np.linalg.eigvalsh(-generator)
    np.testing.assert_allclose(spectrum, np.rint(spectrum), atol=5e-14)
    assert Counter(np.rint(spectrum).astype(int)) == {0: 1, 8: 6, 12: 16, 16: 9}
    kernel = [z for z in range(64) if all((z & r).bit_count() % 2 == 0 for r in rows)]
    assert kernel == [0, 63]
    assert Counter(n.bit_count() for n in even) == {0: 1, 2: 15, 4: 15, 6: 1}
    tau = 0.125
    P = expm(tau * generator)
    assert P.min() >= 0
    np.testing.assert_allclose(P.sum(axis=1), 1)
    char = lambda z: np.array([(-1)**((z & n).bit_count() % 2) for n in even])
    energy = lambda z: 2 * sum((z & r).bit_count() % 2 for r in rows)
    for z in range(64):
        np.testing.assert_allclose(P @ char(z), np.exp(-tau * energy(z)) * char(z), atol=4e-15)
    for z, w in [(1, 2), (5, 9), (0, 63)]:
        # Three insertions with net flat twist and two positive times.
        value = np.mean(char(z ^ w) * (P @ (char(w) * (P @ char(z)))))
        np.testing.assert_allclose(value, np.exp(-tau * (energy(z) + energy(z ^ w))), atol=2e-15)
    # Erasing the common vertex constraint predicts 64 outcomes and two components.
    assert len(even) != 64
    print("L=3,4,7 incidence identical; 32 even sectors; rates 0:1, 8:6, 12:16, 16:9.")


def group_residual():
    rng = np.random.default_rng(314159)
    for dim in (2, 3, 4):
        z = np.exp(2j * np.pi / dim)
        v = lambda h: 1 - np.trace(h).real / dim
        for _ in range(20):
            raw = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
            q, _ = np.linalg.qr(raw)
            q[:, 0] /= np.linalg.det(q)
            vz = 1 - z.real
            assert abs(v(z*q) - v(q) - vz) <= 2 * np.sqrt(vz * v(q)) + 1e-12
    print("SU(2), SU(3) and SU(4) Wilson-action residual inequality checked.")


if __name__ == "__main__":
    star()
    group_residual()
