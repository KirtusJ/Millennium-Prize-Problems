"""Exact eight-edge support and quaternion quadrature controls."""
from fractions import Fraction
from itertools import product


def face(root, i, j, signs, size):
    x = list(root)
    edges = []
    for direction, step in ((i, signs[i]), (j, signs[j]), (i, -signs[i]), (j, -signs[j])):
        x[direction] = (x[direction] + min(step, 0)) % size
        edges.append((tuple(x), direction))
        x[direction] = (x[direction] + max(step, 0)) % size
    return edges


def supports(size):
    located = {}
    counts = {}
    axes = set(range(4))
    for root in product(range(size), repeat=4):
        for signs in product((-1, 1), repeat=4):
            cell = tuple((x-(1-s)//2) % size for x, s in zip(root, signs))
            for j in (1, 2, 3):
                k, l = sorted(axes - {0, j})
                shape = frozenset(face(root, 0, j, signs, size) + face(root, k, l, signs, size))
                assert len(shape) == 8 and shape not in located
                located[shape] = root
                counts[cell] = counts.get(cell, 0) + 1
    assert len(located) == size**4 * 48 and set(counts.values()) == {48}
    return len(located)


def haar_quadrature():
    # The uniform eight quaternion units reproduce Haar moments through degree two.
    group = [tuple(s*int(i == j) for i in range(4)) for j in range(4) for s in (-1, 1)]
    rows = []
    for u, v in product(group, repeat=2):
        h = Fraction(sum(a*b for a, b in zip(u[1:], v[1:])), 16)
        # An exactly summable conditional weight with a mixed interaction.
        exponent = u[0] + v[0] + sum(a*b for a, b in zip(u, v))
        rows.append((h, Fraction(2)**exponent, u[1]))
    total = sum(w for _, w, _ in rows)
    mixed = average_dual = one_leg = ordinary = 0
    for h, w, leg in rows:
        prob = w/total
        dual = h/(64*prob)
        mixed += prob*h*dual
        average_dual += prob*dual
        one_leg += prob*leg*dual
        ordinary += prob*h*h
    assert mixed == Fraction(3, 4096) and average_dual == one_leg == 0
    assert ordinary != mixed
    return mixed, ordinary


if __name__ == '__main__':
    print('Distinct supports on side 5:', supports(5))
    mixed, ordinary = haar_quadrature()
    print('Mixed norm, tilted norm, site contact:', mixed, ordinary, 48*mixed)
