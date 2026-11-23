"""Enumerate the quadratic center-parity diagrams and integrate their local Haar factor."""
from collections import Counter
from fractions import Fraction
from itertools import product
import mpmath as mp

PLANES = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]


def move(x, axis, step):
    y = list(x)
    y[axis] += step
    return tuple(y)


def face(x, i, j, s, t):
    lower = move(x, i, -1) if s < 0 else x
    lower = move(lower, j, -1) if t < 0 else lower
    return frozenset(((lower, i), (lower, j), (move(lower, i, 1), j), (move(lower, j, 1), i)))


def figures(x):
    for i, j, k, l in PLANES:
        for s, t, u, v in product((-1, 1), repeat=4):
            yield frozenset((face(x, i, j, s, t), face(x, k, l, u, v)))


def touching(edges):
    return {face(x, i, j, 1, t) for x, i in edges for j in range(4)
            if j != i for t in (-1, 1)}


def geometry():
    fixed = next(figures((0, 0, 0, 0)))
    support = frozenset.union(*fixed)
    assert len(touching(support)) == 38
    overlap, retained = Counter(), Counter()
    for x in product(range(-2, 3), repeat=4):
        for other in figures(x):
            edges = frozenset.union(*other)
            shared = len(support & edges)
            if shared < 4:
                continue
            overlap[shared] += 1
            difference = support ^ edges
            if not difference:
                assert other == fixed and x == (0, 0, 0, 0)
                continue
            candidates = touching(difference)
            pairs = {frozenset((p, difference ^ p)) for p in candidates
                     if (difference ^ p) in candidates}
            for pair in pairs:
                assert pair == fixed ^ other and len(fixed & other) == 1
                retained[shared] += 1
    assert overlap == {4: 28, 5: 4, 8: 1} and retained == {4: 26, 5: 4}
    print("Overlap candidates:", dict(sorted(overlap.items())))
    print("Distinct parity-compatible pairs:", sum(retained.values()))


def tilted_pair(beta):
    def integral(power):
        return mp.quad(lambda angle: mp.sin(angle)**2 * mp.cos(angle)**power
                       * mp.exp(beta * mp.cos(angle)), [0, mp.pi])
    imag_square = 1 - integral(2)/integral(0)
    return 48 * imag_square**2 / (3*256)


if __name__ == "__main__":
    geometry()
    v = Fraction(3, 4096)
    connected = (Fraction(1, 4) - Fraction(1, 8))/(4*256) - v/4
    assert 48*connected == Fraction(-3, 1024)
    mp.mp.dps = 55
    for beta in map(mp.mpf, ("0.1", "0.01", "0.001")):
        reading = (tilted_pair(beta) - mp.mpf(9)/256)/beta**2
        print("Two-face tilt at beta", mp.nstr(beta), "quadratic coefficient", mp.nstr(reading, 16))
    assert abs(reading + mp.mpf(3)/1024) < mp.mpf("3e-10")
