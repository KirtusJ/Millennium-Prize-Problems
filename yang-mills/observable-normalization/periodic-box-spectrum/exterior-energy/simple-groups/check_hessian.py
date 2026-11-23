"""Differentiate the commutators directly on trace-orthonormal Hermitian matrices."""
from itertools import combinations

import numpy as np


def generators(n):
    basis = []
    for i, j in combinations(range(n), 2):
        for phase in (1, 1j):
            matrix = np.zeros((n, n), dtype=complex)
            matrix[i, j] = phase/np.sqrt(2)
            matrix[j, i] = phase.conjugate()/np.sqrt(2)
            basis.append(matrix)
    for j in range(1,n):
        basis.append(np.diag([1]*j+[-j]+[0]*(n-j-1))/np.sqrt(j*(j+1)))
    return np.array(basis)


def check(points):
    points = points-points.mean(axis=0)
    points /= np.linalg.norm(points)
    n = len(points)
    basis = generators(n)
    # The same fixed unitary conjugation keeps the background commuting while
    # taking it out of the diagonal basis used for the root-distance formula.
    unitary = np.fft.fft(np.eye(n))/np.sqrt(n)
    background = [unitary @ np.diag(col) @ unitary.conj().T for col in points.T]
    columns = []
    for direction in range(3):
        for gen in basis:
            variations = [gen if i == direction else np.zeros_like(gen) for i in range(3)]
            components = []
            for i, j in combinations(range(3), 2):
                term = variations[i]@background[j]+background[i]@variations[j]
                term = (term-term.conj().T)/1j
                components.extend(np.einsum('kij,ji->k', basis, term).real)
            columns.append(components)
    singular = np.linalg.svd(np.array(columns), compute_uv=False)
    distances = [np.linalg.norm(a-b) for a,b in combinations(points, 2)]
    expected = [v for v in distances for _ in range(4)]
    expected += [0.0]*(len(singular)-len(expected))
    np.testing.assert_allclose(singular, sorted(expected, reverse=True), atol=2e-13, rtol=2e-13)
    return np.sum(singular)/np.sqrt(2)


if __name__ == '__main__':
    rng = np.random.default_rng(742)
    for n in (2, 3, 4, 5):
        wall = np.zeros((n, 3))
        wall[-1, 0] = 1
        cost = check(wall)
        predicted = np.sqrt(8*n*(n-1))
        assert abs(cost-predicted) < 2e-12
        generic = check(rng.normal(size=(n,3)))
        assert generic >= predicted-2e-12
        print(f"SU({n})  wall {cost:.10f}  generic {generic:.10f}")
