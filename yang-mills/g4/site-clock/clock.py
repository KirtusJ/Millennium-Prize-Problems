"""Enclose two buffered Wilson transfer moments from certified rational input intervals."""
import argparse
from fractions import Fraction
import json
from math import comb
from pathlib import Path


def rational(value):
    if type(value) not in (int, str):
        raise ValueError("Use integers or quoted rational/decimal strings.")
    return Fraction(value)


def shifted_terms(degree):
    """Yield the monomial coefficients of T_l(2u - 1), in ascending order."""
    previous = []
    current = [1]
    for order in range(degree + 1):
        yield current
        if order == degree:
            return
        if order == 0:
            previous, current = current, [-1, 2]
            continue
        following = [0] * (len(current) + 1)
        for r, coefficient in enumerate(current):
            following[r] -= 2 * coefficient
            following[r + 1] += 4 * coefficient
        for r, coefficient in enumerate(previous):
            following[r] -= coefficient
        previous, current = current, following


def approximation(target, degree):
    """Return the shifted Chebyshev truncation and its exact uniform error."""
    if not 0 <= degree <= target:
        raise ValueError("The degree must lie between zero and the target index.")
    if degree == target:
        return [Fraction(0)] * target + [Fraction(1)], Fraction(0)
    scale = 4 ** target
    binomial = comb(2 * target, target)
    kept = 0
    numerators = [0] * (degree + 1)
    for order, term in enumerate(shifted_terms(degree)):
        weight = binomial if order == 0 else 2 * binomial
        kept += weight
        for r, coefficient in enumerate(term):
            numerators[r] += weight * coefficient
        binomial = binomial * (target - order) // (target + order + 1)
    return [Fraction(x, scale) for x in numerators], Fraction(scale - kept, scale)


def best_anchor(known, last):
    anchors = [(known[r][0] / known[r - 1][1], r)
               for r in range(1, min(last + 1, len(known))) if known[r][0] > 0]
    return max(anchors, default=None)


def moment_interval(target, known):
    """Use only the supplied prefix. Intersect spectral, polynomial and ratio bounds."""
    degree = min(target, len(known) - 1)
    if degree == target:
        return known[target]
    coefficients, tail = approximation(target, degree)
    error = known[0][1] * tail
    lower, upper = -error, error
    for coefficient, (lo, hi) in zip(coefficients, known):
        if coefficient < 0:
            lo, hi = hi, lo
        lower += coefficient * lo
        upper += coefficient * hi
    lower = max(Fraction(0), lower)
    upper = min(upper, known[degree][1])
    # Log-convexity makes each certified adjacent ratio a lower bound at later times.
    anchor = best_anchor(known, degree)
    if anchor:
        ratio, r = anchor
        lower = max(lower, known[r][0] * ratio ** (target - r))
    if lower > upper:
        raise ValueError("The supplied intervals violate necessary moment inequalities.")
    return lower, upper


def moment_prefix(rows):
    if not isinstance(rows, list) or not rows:
        raise ValueError("Supply a nonempty moment list beginning with M_0.")
    known = []
    previous_upper = None
    for row in rows:
        if not isinstance(row, (list, tuple)) or len(row) != 2:
            raise ValueError("Each moment requires a pair of inclusive endpoints.")
        lo, hi = map(rational, row)
        if previous_upper is not None:
            hi = min(hi, previous_upper)
        lo = max(Fraction(0), lo)
        if lo > hi:
            raise ValueError("The bounds contradict positivity or moment monotonicity.")
        known.append((lo, hi))
        previous_upper = hi
    return known


def enclose(payload):
    target = payload["target_index"]
    if type(target) is not int or target < 1:
        raise ValueError("target_index must be an integer of at least one.")
    tolerance = rational(payload.get("relative_width", "1/100"))
    if not 0 < tolerance <= 1:
        raise ValueError("relative_width must belong to (0, 1].")
    known = moment_prefix(payload["moments"])
    midpoint = (target - 1) // 2
    available = min(len(known) - 1, target)
    degree = 0
    while True:
        prefix = known[:degree + 1]
        middle = moment_interval(midpoint, prefix)
        clock = moment_interval(target, prefix)
        reached = all(lo > 0 and hi <= (1 + tolerance) * lo for lo, hi in (middle, clock))
        if reached or degree == available:
            break
        degree = min(available, max(1, 2 * degree))
    ratio = None
    if clock[0] > 0:
        lower = max(Fraction(1), middle[0] / clock[1])
        upper = middle[1] / clock[0]
        anchor = best_anchor(prefix, midpoint + 1)
        if anchor:
            upper = min(upper, 1 / anchor[0] ** (target - midpoint))
        if lower > upper:
            raise ValueError("The supplied intervals contradict moment log-convexity.")
        ratio = [str(lower), str(upper)]
    return {"target_index": target, "midpoint_index": midpoint, "degree_used": degree,
            "midpoint_moment": list(map(str, middle)), "clock_moment": list(map(str, clock)),
            "midpoint_ratio": ratio, "width_reached": reached}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON file containing certified moment intervals")
    args = parser.parse_args()
    try:
        result = enclose(json.loads(args.input.read_text(encoding="utf-8")))
    except (KeyError, ValueError, TypeError, ZeroDivisionError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
