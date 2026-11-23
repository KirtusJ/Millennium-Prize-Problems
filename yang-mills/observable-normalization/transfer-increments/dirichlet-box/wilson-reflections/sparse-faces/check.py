"""Four attached Wilson cubes, their noncommuting holonomies and local sharpness."""
from math import sin

import numpy as np
import sympy as sp


def moved(x, i, sign=1):
    return tuple(v + sign * (j == i) for j, v in enumerate(x))


def faces(x, axes):
    for j, axis in enumerate(axes):
        others = axes[:j] + axes[j+1:]
        for high in (False, True):
            yield (moved(x, axis) if high else x, others), (-1)**j * (1 if high else -1)


def boundary(face):
    x, (a, b) = face
    return [((x, a), 1), ((moved(x, a), b), 1),
            ((moved(x, b), a), -1), ((x, b), -1)]


center = ((1, 1, 2, 2), (0, 1))
patch = []
targets = {center: sp.Integer(1)}
for axis in (2, 3):
    for anchor in (center[0], moved(center[0], axis, -1)):
        disk = dict(faces(anchor, (0, 1, axis)))
        center_sign = disk.pop(center)
        assert not (targets.keys() & disk.keys())
        targets.update({face: -sp.Rational(center_sign * sign, 5)
                        for face, sign in disk.items()})
        patch.append(list(disk))
assert len(targets) == 21

# Realize the sharp tangent data as curls of shared link angles, exactly.
edges = sorted({edge for face in targets for edge, _ in boundary(face)})
curl = sp.zeros(len(targets), len(edges))
for row, face in enumerate(targets):
    for edge, sign in boundary(face):
        curl[row, edges.index(edge)] = sign
angles, params = curl.gauss_jordan_solve(sp.Matrix(list(targets.values())))
angles = angles.subs(dict.fromkeys(params, 0))
assert curl * angles == sp.Matrix(list(targets.values()))
for eps in (0.3, 0.1, 0.03, 0.01):
    ratio = 1 + 20 * (sin(eps / 10) / sin(eps / 2))**2
    assert ratio >= 9/5 and ratio - 9/5 < eps**2
    print(f"Abelian patch: angle {eps:g}, ratio {ratio:.9f}")


def matrix(q):
    a, b, c, d = q
    return np.array([[a+1j*b, c+1j*d], [-c+1j*d, a-1j*b]])


rng = np.random.default_rng(293)
for _ in range(256):
    links = {}
    for edge in edges:
        q = rng.normal(size=4)
        links[edge] = matrix(q / np.linalg.norm(q))
    action = {}
    for face in targets:
        u = np.eye(2)
        for edge, sign in boundary(face):
            u = u @ (links[edge] if sign == 1 else links[edge].conj().T)
        action[face] = 1 - np.trace(u).real/2
    for disk in patch:
        assert action[center] <= 5 * sum(action[f] for f in disk) + 1e-13
print("Exact curl realization and 1,024 noncommuting disk comparisons passed.")
