"""Recover every shell edge by independent square elimination in SU(2)."""
from collections import defaultdict, deque
from itertools import combinations, product

import numpy as np

IDENTITY = np.eye(2, dtype=complex)


def step(x, axis):
    y = list(x)
    y[axis] += 1
    return tuple(y)


def cells(L, dimension):
    for x in product(range(L + 1), repeat=4):
        for axes in combinations(range(4), dimension):
            if all(x[i] < L for i in axes) and any(
                x[i] in (0, L) for i in range(4) if i not in axes
            ):
                yield x, axes


def in_tree(x, j, L):
    if j == 0:
        return True  # Every time edge of the shell is a side column.
    if x[0] == 0:
        return all(v == 0 for v in x[j + 1:])
    return (x[0] == L and j == 1 and x[1] < L - 1
            and all(0 < v < L for v in x[2:]))


def random_su2(rng):
    q = rng.normal(size=4)
    a, b, c, d = q / np.linalg.norm(q)
    return np.array([[a + 1j*b, c + 1j*d], [-c + 1j*d, a - 1j*b]])


def tree_frame(links, L):
    adj = defaultdict(list)
    for (x, j), u in links.items():
        if in_tree(x, j, L):
            y = step(x, j)
            adj[x].append((y, u))
            adj[y].append((x, u.conj().T))
    root = (0, 0, 0, 0)
    frame = {root: IDENTITY}
    queue = deque([root])
    while queue:
        x = queue.popleft()
        for y, u in adj[x]:
            if y not in frame:
                frame[y] = frame[x] @ u
                queue.append(y)
    assert len(frame) == (L+1)**4 - (L-1)**4
    assert sum(map(len, adj.values())) == 2*(len(frame)-1)
    return {(x, j): frame[x] @ u @ frame[step(x, j)].conj().T
            for (x, j), u in links.items()}


def signed(m, sign):
    return m if sign == 1 else m.conj().T


def word_value(terms, links):
    result = IDENTITY
    for edge, sign in terms:
        result = result @ signed(links[edge], sign)
    return result


def peel(plaquettes, tree):
    known = dict.fromkeys(tree, IDENTITY)
    remaining = list(plaquettes)
    while remaining:
        pending = []
        discoveries = 0
        for face in remaining:
            indices = [i for i, (edge, _) in enumerate(face) if edge not in known]
            if len(indices) > 1:
                pending.append(face)
            elif indices:
                i, = indices
                edge, sign = face[i]
                left = word_value(face[:i], known)
                right = word_value(face[i+1:], known)
                known[edge] = signed(left.conj().T @ plaquettes[face] @ right.conj().T, sign)
                discoveries += 1
        assert discoveries or not pending
        remaining = pending
    return known


def check(L):
    rng = np.random.default_rng(4700 + L)
    raw = {(x, j): random_su2(rng) for x, (j,) in cells(L, 1)}
    fixed = tree_frame(raw, L)
    faces = {}
    for x, (i, j) in cells(L, 2):
        face = (((x, i), 1), ((step(x, i), j), 1),
                ((step(x, j), i), -1), ((x, j), -1))
        faces[face] = word_value(face, fixed)
    tree = [edge for edge in raw if in_tree(*edge, L)]
    solved = peel(faces, tree)
    assert solved.keys() == fixed.keys()
    # Normalize the starting data to a tree-gauge representative numerically.
    error = max(np.linalg.norm(solved[e] - fixed[e]) for e in solved)
    assert error < 1e-8, (L, error)

    theta = 0.5 / L**2
    def phase(angle):
        return np.diag(np.exp(1j * np.array([angle, -angle])))
    cartan = {e: phase(e[0][0]*theta) if e[1] == 1 else IDENTITY for e in raw}
    peak = max(abs(np.angle(word_value(face, cartan)[0, 0])) for face in faces)
    cartan_fixed = tree_frame(cartan, L)
    seam = cartan_fixed[((L, L-1, 1, 1), 1)]
    ratio = np.angle(seam[0, 0]) / peak
    assert abs(ratio - L**2) < 1e-10
    print(f"L={L} edges={len(raw)} faces={len(faces)} max_error={error:.2e} angle_ratio={ratio:.0f}")


if __name__ == "__main__":
    for size in (2, 3, 4, 6):
        check(size)
