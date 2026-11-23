"""Periodic cubic Wilson faces, opposite integration links and third-moment support."""
from collections import defaultdict
from itertools import combinations, product


def step(point, direction, side):
    p = list(point)
    p[direction] = (p[direction] + 1) % side
    return tuple(p)


def certify(side):
    faces = {}
    around = defaultdict(set)
    for x in product(range(side), repeat=3):
        for i, j in combinations(range(3), 2):
            p = x, i, j
            edges = ((x, i), (step(x, i, side), j), (step(x, j, side), i), (x, j))
            if len(set(edges)) != 4:
                raise ValueError("face repeats a link")
            faces[p] = edges
            for edge in edges:
                around[edge].add(p)
    for edge, incident in around.items():
        if len(incident) != 4:
            raise ValueError("missing incident face")
        opposites = {p: faces[p][(faces[p].index(edge)+2) % 4] for p in incident}
        if len(set(opposites.values())) != 4:
            raise ValueError("opposite integration links coincide")
        if any(opposites[p] in faces[q] for p in incident for q in incident if p != q):
            raise ValueError("another incident face uses the integration variable")
    neighbors = {p: set.union(*(around[edge] for edge in edges)) for p, edges in faces.items()}
    sizes = {(len(near), len(set.union(*(neighbors[q] for q in near))))
             for near in neighbors.values()}
    if len(sizes) != 1:
        raise ValueError("row count depends on position or orientation")
    return len(faces), *sizes.pop()


if __name__ == "__main__":
    for length in (3, 4, 5, 7, 9):
        print(length, *certify(length))
    try:
        certify(2)
    except ValueError as e:
        print("rejected side two:", e)
    else:
        raise ValueError("side two lost the opposite-link obstruction")
