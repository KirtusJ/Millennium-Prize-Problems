"""Exact strong-coupling coefficients for two entries of the projected SU(2) kernel.

Run with Python 3.10+ and no packages. Fractions are retained through enclosure.
"""
from collections import Counter
from fractions import Fraction as Q
from functools import cache
from itertools import combinations
from math import comb, factorial

PAIRS = list(combinations(range(4), 2))
ZERO = (0,) * len(PAIRS)
ODD = [1, 2, 4, 7]


@cache
def gram_moment(edges):
    """Integrate a monomial of six pairwise dot products of four Haar S^3 spins."""
    degrees = [sum(n for n, pair in zip(edges, PAIRS) if i in pair) for i in range(4)]
    if any(d % 2 for d in degrees):
        return Q(0)
    if not any(degrees):
        return Q(1)
    i = next(i for i, d in enumerate(degrees) if d)
    line = list(edges)
    j = next(j for j, pair in enumerate(PAIRS) if line[j] and i in pair)
    first = sum(PAIRS[j]) - i
    line[j] -= 1
    total = Q(0)
    for j, pair in enumerate(PAIRS):
        if line[j] and i in pair:
            second = sum(pair) - i
            residue = line.copy()
            residue[j] -= 1
            if first != second:
                residue[PAIRS.index(tuple(sorted((first, second))))] += 1
            total += line[j] * gram_moment(tuple(residue))
    return total / (degrees[i] + 2)


def fields(k, flux):
    for x in [0, 3, 5, 6]:
        signs = {}
        for axis in range(k):
            neighbor = x ^ (1 << axis)
            parity = (x & ((1 << axis) - 1)).bit_count()
            signs[ODD.index(neighbor)] = (-1) ** (parity if flux else 0)
        yield k, [(j, 2 * signs[a] * signs[b]) for j, (a, b) in enumerate(PAIRS)
                  if a in signs and b in signs]


def times_linear(poly, constant, terms):
    result = Counter()
    for monomial, coefficient in poly.items():
        if constant:
            result[monomial] += constant * coefficient
        for index, scale in terms:
            key = monomial[:index] + (monomial[index] + 1,) + monomial[index + 1:]
            result[key] += scale * coefficient
    return {term: value for term, value in result.items() if value}


def cube_coeffs(k, flux, order):
    """Return [beta^(2n)] Z_k as fractions. Opposite directed links are both present."""
    layers = [{ZERO: 1}] + [{} for _ in range(order)]
    for constant, terms in fields(k, flux):
        result = [Counter(layer) for layer in layers]
        for base, layer in enumerate(layers):
            if not layer:
                continue
            power = layer
            for m in range(1, order - base + 1):
                power = times_linear(power, constant, terms)
                mult = comb(2 * (base + m), 2 * m) * (comb(2 * m, m) // (m + 1))
                if not power:
                    break
                for key, value in power.items():
                    result[base + m][key] += mult * value
        layers = result
    return [sum((value * gram_moment(key) for key, value in layer.items() if value), Q(0))
            / factorial(2 * n) for n, layer in enumerate(layers)]


def projected_coeffs(order):
    sides = []
    inactive = [cube_coeffs(k, False, order) for k in range(2)]
    for flux in (False, True):
        active = inactive + [cube_coeffs(k, flux, order) for k in (2, 3)]
        sides.append([sum(comb(3, k) * active[k][n] for k in range(4)) / 8
                      for n in range(order + 1)])
    return sides


def majorant_tail(k, beta, n):
    """Positive Bessel tail, then an exponential-series bound at degree 2m."""
    cutoff = n + 24
    series = [Q(1)]
    for j in range(1, cutoff + 1):
        series.append(series[-1] * (k * beta) ** 2 / (j * (j + 1)))
    product = [Q(1)] + [Q(0)] * cutoff
    for _ in range(4):
        product = [sum(product[j - i] * series[i] for i in range(j + 1))
                   for j in range(cutoff + 1)]
    m = cutoff + 1
    q = (8 * k * beta) ** 2 / ((2 * m + 1) * (2 * m + 2))
    if not q < 1:
        raise ValueError("increase the positive-tail cutoff")
    return sum(product[n + 1:]) + (8 * k * beta) ** (2 * m) / (factorial(2 * m) * (1 - q))


def ratio_bracket(coefficients, beta):
    order = len(coefficients[0]) - 1
    lower = [sum(v * beta ** (2 * n) for n, v in enumerate(side)) for side in coefficients]
    tail = sum(comb(3, k) * majorant_tail(k, beta, order) for k in range(4)) / 8
    return lower[0] / (lower[1] + tail), (lower[0] + tail) / lower[1]


def outward(interval, digits):
    scale = 10 ** digits
    lo, hi = interval
    return lo.numerator * scale // lo.denominator, -((-hi.numerator * scale) // hi.denominator)


if __name__ == "__main__":
    import argparse
    from pathlib import Path
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=9)
    parser.add_argument("--write", type=Path)
    args = parser.parse_args()
    sides = projected_coeffs(args.order)
    assert sides[0][0] == sides[1][0] == 1
    assert gram_moment((2, 0, 0, 0, 0, 0)) == Q(1, 4)
    assert gram_moment((1, 1, 0, 1, 0, 0)) == Q(1, 16)
    assert all(x >= 0 for side in sides for x in side)
    lines = ["n,diagonal,mixed"] + [f"{n},{a},{b}" for n, (a, b) in enumerate(zip(*sides))]
    if args.write:
        args.write.write_bytes(("\n".join(lines) + "\n").encode("ascii"))
    for line in lines:
        print(line)
    for b in [Q(1, 8), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)]:
        print(f"beta={b}, ratio interval, units of 1e-10:", *outward(ratio_bracket(sides, b), 10))
