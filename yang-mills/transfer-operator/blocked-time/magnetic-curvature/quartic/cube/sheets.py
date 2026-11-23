"""Enumerate the ordered time layers of the four insertions in a cube sheet."""
from collections import Counter
from itertools import combinations, product

import sympy as sp


def cut(mask):
    return sum(((mask >> i) ^ (mask >> j)) & 1
               for i, j in combinations(range(6), 2) if i//2 != j//2)


def layer_counts(sink):
    inner = [i for i in range(1,6) if i != sink]
    histogram = Counter()
    for layers in range(1,5):
        for order in product(range(layers), repeat=4):
            if len(set(order)) != layers:
                continue
            mask = 1
            powers = []
            for h in range(layers-1):
                for face, height in zip(inner,order):
                    if height == h:
                        mask |= 1 << face
                powers.append(cut(mask)-4)
            histogram[tuple(sorted(powers))] += 1
    assert sum(histogram.values()) == 75
    return histogram


def weight(hist, x):
    return sum(n*sp.prod(x**(p//2)/(1-x**(p//2)) for p in powers)
               for powers,n in hist.items())


if __name__ == "__main__":
    x = sp.symbols("x")  # q^2
    total=0
    for sink, count in [(1,2),(2,8)]:
        h=layer_counts(sink)
        print("sink",sink,"cut histogram",sorted(h.items()))
        val=sp.factor(weight(h,x))
        print(val)
        total+=count*val
    coefficient=sp.factor(-total/256)
    print("cube coefficient",coefficient)
    print("small q",sp.series(coefficient,x,0,3))
    print("scaled by (1-q)^3 at q=1",sp.limit((1-x)**3*coefficient,x,1)/8)
    print("q=1/2",coefficient.subs(x,sp.Rational(1,4)))
