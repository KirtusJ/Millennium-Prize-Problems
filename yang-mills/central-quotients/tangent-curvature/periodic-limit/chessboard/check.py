"""Exact reflection checks with an asymmetric two-site observable and shared spins."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import prod


def arc_products(side, observable):
    # Symmetric bond weights factor through two common site spins at every cut.
    weights = ((3, 2), (2, 5))
    totals = [[0]*side for _ in range(side+1)]
    mass = 0
    for spin in product((0,1), repeat=side):
        pairs = [(spin[i], spin[(i+1)%side]) for i in range(side)]
        weight = prod(weights[x][y] for x,y in pairs)
        mass += weight
        values = [observable[y][x] if i%2 else observable[x][y]
                  for i,(x,y) in enumerate(pairs)]
        for start in range(side):
            value = weight
            totals[0][start] += value
            for width in range(1, side+1):
                value *= values[(start+width-1)%side]
                totals[width][start] += value
    return [Fraction(max(row),mass) for row in totals]


def reflected_face_counts(side):
    """Build the four image vertices, retaining their torus coordinates."""
    for axes in combinations(range(4), 2):
        hits = Counter()
        for cell in product(range(side), repeat=4):
            vertices = []
            for bit0,bit1 in product((0,1), repeat=2):
                vertex = [0]*4
                vertex[axes[0]],vertex[axes[1]] = bit0,bit1
                vertices.append(tuple((t+(1-x if t%2 else x))%side
                                      for t,x in zip(cell,vertex)))
            hits[tuple(sorted(vertices))] += 1
        assert len(hits) == side**4//4 and set(hits.values()) == {4}


if __name__ == '__main__':
    for side in (4,6,8):
        reflected_face_counts(side)
    print('18 four-dimensional oriented-plane censuses passed')
    tests = 0
    for side in (4,6,8,10):
        for f in (((4,1),(3,2)), ((0,3),(1,0)), ((1,0),(0,0))):
            m = arc_products(side, f)
            assert m[1]**2 <= m[2]
            for width in range(2,side,2):
                assert m[width]**2 <= m[width-2]*m[width+2]
            assert m[1]**side <= m[side]
            tests += 1
    print(tests, 'finite-state rings passed with exact rational expectations')
