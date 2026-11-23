"""Independent exact check using coordinate tuples and one starting orientation."""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product

steps = [(s*(i == 0), s*(i == 1), s*(i == 2)) for i in range(3) for s in (-1, 1)]


def endpoints():
    counts = Counter()
    visited = {(-1, 0, 0), (0, 0, 0)}
    def visit(point, left):
        if not left:
            counts[point] += 1
            return
        for step in steps:
            new = tuple(a+b for a,b in zip(point,step))
            if new in visited:
                continue
            visited.add(new)
            visit(new, left-1)
            visited.remove(new)
    visit((0, 0, 0), 8)
    return counts


if __name__ == "__main__":
    counts = endpoints()
    assert sum(counts.values()) == 308981
    r = Fraction(9, 8)
    powers = {k:r**k for k in range(-8, 9)}
    for m in (1, 2, 3):
        axes = set(permutations((1,)*m+(0,)*(3-m)))
        tilts = {tuple(a*b for a,b in zip(axis, signs))
                 for axis in axes for signs in product((-1,1), repeat=3)}
        rows = []
        for tilt in tilts:
            rows.append(sum(n*powers[sum(a*b for a,b in zip(tilt, point))]
                            for point,n in counts.items()))
        ratio = max(rows)/5**8
        print(m, ratio, float(ratio))
        assert ratio < Fraction(9, 10)
    assert Fraction(9, 10)*Fraction(101, 100)**8 < 1
