"""Verify signed boundaries, colour multiplicities, and the weighted row bound."""
from collections import Counter, defaultdict
from itertools import combinations, product
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "full-complement"))
from retraction import surface


def check(side):
    sites = list(product(range(side), repeat=3))
    multiplicity, rows = Counter(), Counter()
    columns = {}
    def step(x, axis):
        return tuple((v + (j == axis)) % side for j, v in enumerate(x))

    for x in sites:
        for i, j in combinations(range(3), 2):
            multiplicity[x if x[j] % 2 else step(x, j), i] += 1
            multiplicity[x if x[i] % 2 else step(x, i), j] += 1
    for x in sites:
        for i in range(3):
            e = (x, i)
            pos, neg = surface(x, i)
            faces = Counter()
            for sign, chain in [(1, pos), (-1, neg)]:
                for (z, a, b), number in chain.items():
                    faces[tuple(v % side for v in z), a, b] += sign * number
            boundary = Counter()
            for (z, a, b), value in faces.items():
                boundary[z, a] += value
                boundary[step(z, a), b] += value
                boundary[step(z, b), a] -= value
                boundary[z, b] -= value
            y = step(x, i)
            root = tuple(v - v % 2 for v in x)
            for sign, word in [(1, [d for d in range(3) if x[d] % 2] + [i]),
                               (-1, [i] * (2 * (x[i] % 2)) + [d for d in range(3) if y[d] % 2])]:
                z = root
                for axis in word:
                    boundary[z, axis] -= sign
                    z = step(z, axis)
                assert z == y
            assert not any(boundary.values())
            columns[e] = {f: abs(v) for f, v in faces.items() if v}
            rows.update(columns[e])

    types = defaultdict(set)
    for (x, i), column in columns.items():
        m = multiplicity[x, i]
        assert m == 2 * sum(v % 2 for axis, v in enumerate(x) if axis != i)
        weight = sum(rows[f] * count for f, count in column.items())
        assert weight <= 3 * m
        types[tuple(v % 2 for v in x), i].add((m, weight))
    assert all(len(values) == 1 for values in types.values())
    return {key: values.pop() for key, values in types.items()}


if __name__ == "__main__":
    # Side two counts incidences modulo period two for the all-size parity table.
    table = check(2)
    assert max(w / m for m, w in table.values() if m) == 3
    total = 0
    for side in (6, 8, 10, 12):
        assert check(side) == table
        total += 3 * side**3
    assert total == 10368
    print(f"{total} periodic edges and signed boundaries checked")
    for x in product(range(2), repeat=3):
        print("".join(map(str, x)), [table[x, i] for i in range(3)])
