"""Exact controls for the finite-period ambiguity and the fourth-moment test."""
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from math import ceil


def interpolate(nodes, targets):
    """Coefficients in ascending degree, with constant coefficient zero."""
    out = [F(0)] * (len(nodes) + 1)
    for i, node in enumerate(nodes):
        basis = [0, targets[i] / node]
        for j, other in enumerate(nodes):
            if i == j:
                continue
            basis = [(a - other * b) / (node - other)
                     for a, b in zip([0] + basis, basis + [0])]
        out = [a + b for a, b in zip(out, basis)]
    return out[1:]


def compare_periods(periods, gap_multiple):
    x = [F(1, 2**t) for t in periods]
    c = interpolate([v**gap_multiple for v in x], [1 / (1 + v) for v in x])
    d = [max(1, ceil(abs(v))) for v in c]
    amplitudes = [(1 + v / n) / 2 for v, n in zip(c, d)]
    assert all(0 <= a <= 1 for a in amplitudes)
    for t, v in zip(periods, x):
        w = [n * v**(j * gap_multiple) for j, n in enumerate(d, 1)]
        z = 1 + (1 + v) * sum(w)
        scale = sum(a * b for a, b in zip(w, amplitudes)) / z
        assert scale == 1 / (2 * (1 + v))
        for s in range(t + 1):
            kernel = F(1, 2**s) + F(1, 2**(t-s))
            assert kernel * scale == kernel / (2 * (1 + v))
    return c, d


def moment_checks():
    transfer = [F(1), F(1, 4), F(1, 8)]
    weights = [v**4 / sum(w**4 for w in transfer) for v in transfer]
    separation = F(7, 16)
    pairs = list(combinations_with_replacement(range(3), 2))
    for entries in product((-1, 0, 1), repeat=len(pairs)):
        a = [[0] * 3 for _ in range(3)]
        for (i, j), value in zip(pairs, entries):
            a[i][j] = a[j][i] = value
        mu = sum(weights[i] * a[i][i] for i in range(3))
        for i in range(3):
            a[i][i] -= mu
        squared = [[sum(a[i][k] * a[k][j] for k in range(3))
                    for j in range(3)] for i in range(3)]
        b = sum(weights[i] * squared[i][i] for i in range(3))
        kappa = sum(weights[i] * sum(v*v for v in squared[i])
                    for i in range(3)) - b*b
        cor = [sum(weights[i] * (transfer[j]/transfer[i])**s * a[i][j]**2
                   for i in range(3) for j in range(3)) for s in range(5)]
        residual = sum(c*v for c, v in zip([1,-5,F(33,4),-5,1], cor))
        assert residual >= weights[0] * squared[0][0] * separation**2
        shortfall = max(0, weights[0] * b - residual / separation**2)
        assert shortfall**2 <= weights[0] * kappa


if __name__ == "__main__":
    for multiple in (2, 3, 9):
        for periods in ((1, 2, 3), (1, 3, 4, 7, 10)):
            compare_periods(periods, multiple)
    c, d = compare_periods((1, 2, 3), 2)
    assert c == [F(v, 405) for v in (30488, -500608, 1531904)]
    assert 1 + 2 * sum(d) == 10193
    v = F(1, 16)
    assert (1 + v)*sum(a*v**(2*j) for j, a in enumerate(c, 1))-1 == F(-347683,491520)
    moment_checks()
    print("Six interpolation designs and 729 fourth-moment controls passed.")
