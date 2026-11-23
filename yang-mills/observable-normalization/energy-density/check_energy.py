"""Independent checks of a local-energy sum rule, conservation, and the radius in space."""
from itertools import combinations
from pathlib import Path
import runpy
import numpy as np
from scipy.linalg import eigh_tridiagonal

GEOMETRY = Path(__file__).resolve().parent.parent / "smeared-plaquettes" / "moment-bounds" / "check_geometry.py"


def rotor(size, g):
    n = np.arange(size)
    laplace = np.diag(n*(n+2))
    x = (np.diag(np.ones(size-1), 1) + np.diag(np.ones(size-1), -1))/2
    potential = g*(np.eye(size)-x)
    energies, vec = eigh_tridiagonal(np.diag(laplace) + g, np.full(size-1, -g/2))
    vacuum = vec[:, 0]
    energies -= energies[0]
    local = [laplace/4]*4 + [potential]
    excitations = np.column_stack([vec[:, 1:].T @ (o @ vacuum) for o in local])
    gram = excitations.T @ (energies[1:, None] * excitations)
    weights = np.array([0.2, 0.7, -1, 2, 0.5])
    approx = -np.sum(gram*(weights[:, None]-weights[None, :])**2)/2
    exact = weights @ gram @ weights
    double = (np.diag(laplace)[:, None]-np.diag(laplace)[None, :])**2*x
    if not np.array_equal(double, 2*(laplace @ x + x @ laplace)+3*x):
        raise AssertionError("one-link coordinate Casimir identity")
    electric = g*(vacuum @ double @ vacuum)/32
    expected = np.array([1, 1, 1, 1, -4])
    if not np.allclose(gram, electric*np.outer(expected, expected), rtol=1e-8, atol=1e-9):
        raise AssertionError("magnetic/electric sign or link normalization")
    if not np.allclose(exact, approx) or np.max(np.abs(gram.sum(axis=1))) > 1e-8:
        raise AssertionError("conserved mode")
    return np.array([gram[0, 0], gram[-1, -1], exact])


def neighborhood(side):
    geometry = runpy.run_path(str(GEOMETRY))
    words = geometry["faces"](side)
    incidence, _ = geometry["incidence"](words)
    edges = list(incidence)
    id_of = {e: i for i, e in enumerate(edges)}
    face_ids = [len(edges)+i for i in range(len(words))]
    pairs = set()
    centers = []
    for x, axis in edges:
        center = 2*np.array(x)
        center[axis] += 1
        centers.append(center)
    for i, word in enumerate(words):
        ids = [id_of[e] for e, _ in word]
        center = 2*np.array(word[0][0][0])
        center[word[0][0][1]] += 1
        center[word[1][0][1]] += 1
        centers.append(center)
        pairs.update(tuple(sorted(p)) for p in combinations(ids+[face_ids[i]], 2))
    for star in incidence.values():
        pairs.update(tuple(sorted((face_ids[i], face_ids[j]))) for i,j in combinations(star, 2))
    degree = np.zeros(len(centers), int)
    radius_squared = 0
    offsets = []
    for i,j in pairs:
        delta = (centers[i]-centers[j]+side) % (2*side)-side
        radius_squared = max(radius_squared, delta @ delta)
        if np.all(centers[i] < 2):
            offsets.append(-delta/2)
        if np.all(centers[j] < 2):
            offsets.append(delta/2)
        degree[i] += 1
        degree[j] += 1
    assert degree.max() <= 16 and radius_squared <= 4
    print("side, maximum degree, maximum center distance (mesh units)", side, degree.max(), np.sqrt(radius_squared)/2)
    return np.array(offsets)


def stencil(offsets):
    # Synthetic symmetric graph Laplacian with off-diagonal entries -1/b³.
    tensor = offsets.T @ offsets/2
    rho = tensor.trace()/3
    assert np.array_equal(tensor, rho*np.eye(3))
    limit = 2*np.pi**2*rho
    errors = []
    for L in (8, 16, 32, 64):
        b = 1/L
        # Exact sampled energy for cos(2πx), summing all translates of each pair.
        moment = np.sum(np.sin(np.pi*b*offsets[:, 0])**2)/b**2
        errors.append(abs(moment-limit))
    if not all(a/b > 3.8 for a, b in zip(errors, errors[1:])):
        raise AssertionError(errors)
    print("synthetic coefficient, four Fourier errors", rho, *(f"{x:.6g}" for x in errors))


if __name__ == "__main__":
    for side in (3, 4, 5):
        offsets = neighborhood(side)
    stencil(offsets)
    for g in (0, 1, 16, 256):
        low, high = rotor(48,g), rotor(96,g)
        if not np.allclose(low, high, rtol=1e-8, atol=1e-9):
            raise AssertionError((g, low, high))
        print(g, *(f"{v:.9g}" for v in high))
