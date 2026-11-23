"""Check the spectral crossing and axis-aligned corner geometry with exact arithmetic."""
from collections import Counter
from fractions import Fraction as Q
from math import factorial, prod


def bessel_interval(order, coupling):
    half = coupling / 2
    term = half**order / factorial(order)
    total = term
    for k in range(1, 13):
        term *= half**2 / (k * (k + order))
        total += term
    ratio = half**2 / (13 * (13 + order))
    return total, total + term * ratio / (1 - ratio)


def crossing_sign(coupling):
    (l1, u1), (l2, u2), (l3, u3) = [
        bessel_interval(n, coupling) for n in (1, 2, 3)
    ]
    if l3**3 * l1**4 > u2**7:
        return 1
    if u3**3 * u1**4 < l2**7:
        return -1
    raise ArithmeticError("Bessel intervals overlap")


def cell_moves(side):
    """Enumerate the actual retained-cell square, with no partition data."""
    cells = [(x, y) for y in range(side) for x in range(side)]
    bits = {cell: 1 << i for i, cell in enumerate(cells)}
    square = (1 << len(cells)) - 1
    neighbors = [
        tuple(bits.get((x + dx, y + dy), 0)
              for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        for x, y in cells
    ]
    walks = Counter({square: 1})
    for level in range(1, side):
        after = Counter()
        for state, count in walks.items():
            for i, (r, l, u, d) in enumerate(neighbors):
                cell = 1 << i
                full = bool(state & cell)
                horizontal = (bool(state & r) != full) + (bool(state & l) != full)
                vertical = (bool(state & u) != full) + (bool(state & d) != full)
                if horizontal + vertical >= 2:
                    assert horizontal == vertical == 1
                    after[state ^ cell] += count
        walks = after
        assert sum(v*v for v in walks.values()) == 4**level * prod(range(1, 2*level, 2))
    # At depth side-1 exactly one cell can remain in the top row, at the right.
    row = sum(bits[x, side-1] for x in range(side-1))
    assert square ^ row in walks
    return len(walks)


if __name__ == "__main__":
    for arg, sign in (("1", 1), ("1.44014227", 1), ("1.44014228", -1), ("2", -1)):
        assert crossing_sign(Q(arg)) == sign
    for side in range(2, 10):
        print(f"side {side}, depth {side-1}, {cell_moves(side)} distinct boundaries")
