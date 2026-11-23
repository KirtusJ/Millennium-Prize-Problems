"""Enumerate parity-admissible plaquette insertions; integrate the two surviving faces."""
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from math import pi

import numpy as np


def shift(x, i, n):
    y = list(x)
    y[i] += n
    return tuple(y)


@lru_cache(None)
def boundary(face):
    x, i, j = face
    return frozenset(((x, i), (x, j), (shift(x, j, 1), i), (shift(x, i, 1), j)))


def incident(edge):
    x, i = edge
    for j in range(4):
        if j != i:
            a, b = sorted((i, j))
            yield x, a, b
            yield shift(x, j, -1), a, b


def words(root):
    for bits in product(range(2), repeat=4):
        for j in (1, 2, 3):
            k, l = sorted({1, 2, 3} - {j})
            faces = frozenset((shift(shift(root, a, -bits[a]), b, -bits[b]), a, b)
                              for a, b in ((0, j), (k, l)))
            first, second = faces
            yield faces, boundary(first) | boundary(second)


def enumerate_pairs():
    at_origin = tuple(words((0,) * 4))
    counts = Counter()
    for root in product(range(-2, 3), repeat=4):
        for other, other_edges in words(root):
            for own, own_edges in at_origin:
                if len(own_edges & other_edges) < 4:
                    continue  # Two inserted faces cover at most eight odd edges.
                odd = own_edges ^ other_edges
                if not odd:
                    assert own == other
                    counts['identical'] += 1
                    continue
                # One inserted face must cover the first odd edge.
                solutions = set()
                for first in incident(min(odd)):
                    rest = odd ^ boundary(first)
                    if len(rest) == 4:
                        for second in incident(min(rest)):
                            if boundary(second) == rest:
                                solutions.add(frozenset((first, second)))
                for inserted in solutions:
                    assert len(own & other) == 1 and inserted == (own ^ other)
                    shared, = own & other
                    a, b = inserted
                    assert boundary(a) - (boundary(b) | boundary(shared))
                    assert boundary(b) - (boundary(a) | boundary(shared))
                    counts['overlapping'] += 1
                counts['without insertions that pass parity'] += not solutions
    assert counts['identical'] == 48 and counts['overlapping'] > 0
    print(dict(counts))


def tilted_contact():
    x, weights = np.polynomial.legendre.leggauss(100)
    theta = (x + 1) * pi / 2
    for beta in (.2, .1, .05, .025, .0125):
        density = weights * np.sin(theta)**2 * np.exp(beta * np.cos(theta))
        imag_norm = np.sum(density * np.sin(theta)**2) / np.sum(density)
        total = 48 / (3 * 256) * imag_norm**2
        observed = (total - 9 / 256) / beta**2
        print(beta, "quadratic contact coefficient", observed)
    assert abs(observed + 3 / 1024) < 1e-7


if __name__ == "__main__":
    enumerate_pairs()
    tilted_contact()
