"""Enumerate spatial-link conflicts and an equality case of the covariance bound."""
from fractions import Fraction as Q
from itertools import combinations, product


def shifted(p, axis, length):
    q = list(p)
    q[axis] = (q[axis] + 1) % length
    return tuple(q)


def conflicts(length):
    adjacency = {}
    for p in product(range(length), repeat=4):
        for i, j in combinations(range(4), 2):
            face = [(p, i), (p, j), (shifted(p, i, length), j), (shifted(p, j, length), i)]
            for a, b in combinations(face, 2):
                adjacency.setdefault(a, set()).add(b)
                adjacency.setdefault(b, set()).add(a)
    return adjacency


def check_lattice(length):
    graph = conflicts(length)
    start = ((0, 0, 0, 0), 1)
    spatial = {edge for edge in graph[start] if edge[0][0] == 0 and edge[1] != 0}
    planar = {edge for edge in spatial if edge[0][3] == 0 and edge[1] in (1, 2)}
    assert len(spatial) == 12 and len(planar) == 6
    for (p, axis), neighbors in graph.items():
        if axis == 0:
            continue
        other_slices = {(q, j) for q, j in neighbors if j != 0 and q[0] != p[0]}
        expected = {((time, *p[1:]), axis) for time in ((p[0]-1) % length, (p[0]+1) % length)}
        assert other_slices == expected
    print(f"{length}^4: same-slice neighbors 12, planar neighbors 6; cross-slice conflicts only at +/-1")


def check_covariance():
    # Independent signs conditioned on a shared exterior bit, with conditional
    # means 2*eps_i*G. The product bound is attained.
    a, b = Q(2, 5), Q(3, 7)
    mass = mean_x = mean_y = mean_xy = Q(0)
    for g, i, j in product((-1, 1), repeat=3):
        weight = Q(1, 2) * (1+i*a)/2 * (1+j*b)/2
        x, y = 2*g*i, 2*g*j
        mass += weight
        mean_x += weight*x
        mean_y += weight*y
        mean_xy += weight*x*y
    assert mass == 1 and mean_x == mean_y == 0 and mean_xy == 4*a*b
    print("conditional-product equality, covariance =", mean_xy)


if __name__ == "__main__":
    for size in (3, 4, 5):
        check_lattice(size)
    check_covariance()
