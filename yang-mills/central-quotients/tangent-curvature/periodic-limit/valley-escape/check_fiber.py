"""Direct Ritz challenge for the four-coordinate transverse Hamiltonian."""
from functools import reduce
import numpy as np
from scipy.sparse import diags, eye, kron
from scipy.sparse.linalg import eigsh


def fiber_ritz(radius, axial_length, levels):
    outer = np.hypot(radius, axial_length)
    frequencies = (2*radius, 2*radius, 2*outer, 2*outer)
    states = np.indices((levels,)*4)
    energies = sum(w*(n+0.5) for n, w in zip(states, frequencies))
    identity = eye(levels+1, levels, format="csr")

    # Multiplication lands in levels+1 states. Squaring the square truncation
    # instead would discard the raising paths out of the top occupied state.
    def coordinate(w):
        start = np.arange(levels)
        return (diags([np.sqrt(start+1), np.sqrt(start[1:])],
                      [-1, 1], shape=(levels+1, levels))/np.sqrt(2*w)).tocsr()

    def product(i, j):
        return reduce(lambda a, b: kron(a, b, format="csr"),
                      (coordinate(w) if k in (i, j) else identity
                       for k, w in enumerate(frequencies)))

    area = product(0, 3) - product(1, 2)
    h = diags(energies.ravel()) + 2*(area.T @ area)
    # Ground symmetry permits a start in the even sector.
    initial = np.zeros(h.shape[0])
    initial[0] = 1
    value = eigsh(h, k=1, which="SA", v0=initial, tol=1e-12,
                  return_eigenvectors=False)[0]
    harmonic = 2*(radius+outer)
    correction = 1/(4*radius*outer)
    separation = 2*radius-correction
    lower = max(0, correction-5*correction**2/separation) if separation > 0 else 0
    return lower, value-harmonic, correction


if __name__ == "__main__":
    for radius, axial in ((0.5, 0), (1, 0), (2, 0), (4, 0), (4, 3), (8, 6)):
        low, coarse, high = fiber_ritz(radius, axial, 4)
        _, fine, _ = fiber_ritz(radius, axial, 6)
        assert low-1e-10 <= fine <= coarse+1e-10 <= high+2e-10
        print(f"r={radius:g} z={axial:g}  Temple={low:.9g}  "
              f"Ritz4={coarse:.9g}  Ritz6={fine:.9g}  Gaussian={high:.9g}")
