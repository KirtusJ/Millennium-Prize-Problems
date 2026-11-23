"""Check the third sum rule and both nested-commutator terms on an isolated SU(2) plaquette."""
import numpy as np
from scipy.linalg import eigh_tridiagonal


def bracket(a, b):
    return a @ b - b @ a


def rotor(size, g):
    n = np.arange(size)
    kinetic = np.diag(n * (n + 2))
    trace = np.diag(np.ones(size - 1), 1) + np.diag(np.ones(size - 1), -1)
    potential = g * (np.eye(size) - trace / 2)
    energies, vectors = eigh_tridiagonal(np.diag(kinetic) + g, np.full(size - 1, -g/2))
    vacuum = vectors[:, 0]
    state = trace @ vacuum
    mass = (vectors.T @ state)**2
    energy = energies - energies[0]
    first, second, third = (mass @ (energy**j) for j in (1, 2, 3))
    generator = bracket(kinetic, trace)
    terms = [vacuum @ bracket(generator, bracket(generator, part)) @ vacuum / 2
             for part in (kinetic, potential)]
    if not np.isclose(sum(terms), third, rtol=2e-10, atol=2e-9):
        raise AssertionError((size, g, third, terms))
    if second**2 > first*third + 1e-8:
        raise AssertionError((first, second, third))
    return np.array([first, second, third, *terms])


def main():
    for g in (0, 1, 16, 256, 4096):
        a, b = rotor(64, g), rotor(128, g)
        if not np.allclose(a, b, rtol=1e-9, atol=1e-8):
            raise AssertionError((g, a, b))
        if g == 0 and not np.allclose(b, [3, 9, 27, 27, 0]):
            raise AssertionError(b)
        if g >= 16 and abs(b[-1]) < b[2]/10:
            raise AssertionError("omitting the magnetic term should be detectable")
        print(g, *(f"{v:.9g}" for v in b))


if __name__ == "__main__":
    main()
