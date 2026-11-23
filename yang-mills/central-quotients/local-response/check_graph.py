"""Compute the stabilizer dimension from the actual edge and face incidence."""
from itertools import combinations, product


def basis(vectors):
    pivots = {}
    for vector in vectors:
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = vector
                break
            vector ^= pivots[pivot]
    return tuple(pivots.values())


def graph(dim, side, periodic, missing_face=None):
    vertices = list(product(range(side), repeat=dim))

    def step(x, i):
        if not periodic and x[i] == side-1:
            return None
        return x[:i] + ((x[i]+1) % side,) + x[i+1:]

    edges = {(x, i): k for k, (x, i) in enumerate(
        (x, i) for x in vertices for i in range(dim) if step(x, i) is not None)}
    stars = dict.fromkeys(vertices, 0)
    for (x, i), k in edges.items():
        stars[x] ^= 1 << k
        stars[step(x, i)] ^= 1 << k
    faces = []
    for x in vertices:
        for i, j in combinations(range(dim), 2):
            right, up = step(x, i), step(x, j)
            if right is None or up is None or (x, i, j) == missing_face:
                continue
            boundary = [(x, i), (right, j), (up, i), (x, j)]
            faces.append(sum(1 << edges[e] for e in boundary))
    if any((vertex & face).bit_count() % 2 for vertex in stars.values() for face in faces):
        raise ValueError("a vertex sign changed a plaquette")
    star_rank = len(basis(stars.values()))
    face_rank = len(basis(faces))
    if star_rank != len(vertices)-1:
        raise ValueError("graph was disconnected")
    if periodic:
        seams = [sum(1 << k for (x, j), k in edges.items() if j == i and x[i] == side-1)
                 for i in range(dim)]
        if any((s & f).bit_count() % 2 for s in seams for f in faces):
            raise ValueError("a seam sign changed a plaquette")
        if len(basis([*stars.values(), *seams])) != star_rank+dim:
            raise ValueError("winding seam signs were vertex equivalent")
    return len(vertices), len(edges), len(faces), face_rank, len(edges)-star_rank-face_rank


if __name__ == "__main__":
    for dim, periodic, hole, expected in (
            (2, False, None, 0), (2, False, ((0, 0), 0, 1), 1),
            (2, True, None, 2), (2, True, ((0, 0), 0, 1), 2),
            (3, False, None, 0), (3, True, None, 3)):
        values = graph(dim, 3, periodic, hole)
        if values[-1] != expected:
            raise ValueError((dim, periodic, hole, values))
        print(dim, "periodic" if periodic else "open", "deleted" if hole else "all", *values)
