"""Certify the sign of supplied integer tests using rational Taylor bounds and integer endpoints."""
import json
from fractions import Fraction
from pathlib import Path

SCALE = 10**110


def floor_scaled(x):
    return x.numerator * SCALE // x.denominator


def ceil_scaled(x):
    return -floor_scaled(-x)


def exp_minus(x):
    """For x >= 0, enclose SCALE * exp(-x)."""
    assert x >= 0
    folds = 0
    while x > Fraction(1, 2):
        x /= 2
        folds += 1
    term = total = Fraction(1)
    for k in range(1, 97):
        term *= -x / k
        total += term
    low = floor_scaled(total - term*x/97)
    high = ceil_scaled(total)
    for _ in range(folds):
        low = low*low // SCALE
        high = -(-high*high // SCALE)
    return low, high


def moment(t, T, s):
    """Return an enclosure of SCALE * T^8 C(t)/B."""
    u = t*t/(8*s)
    lo, hi = exp_minus(u)
    a = 1-(1+u)*Fraction(hi, SCALE)
    b = 1-(1+u)*Fraction(lo, SCALE)
    assert 0 <= a <= b
    return floor_scaled((T/t)**8*a*a), ceil_scaled((T/t)**8*b*b)


def exact_form(row):
    T, h, s = [Fraction(row[k]) for k in ("T", "h", "s")]
    c = row["c"]
    grouped = [0]*(2*len(c)-1)
    for i, x in enumerate(c):
        for j, y in enumerate(c):
            grouped[i+j] += x*y
    lo = hi = unflowed = 0
    for n, k in enumerate(grouped):
        a, b = moment(T+n*h, T, s)
        lo += min(k*a, k*b)
        hi += max(k*a, k*b)
        unflowed += k*(T/(T+n*h))**8
    norm = sum(map(abs,c))**2
    assert lo <= hi < 0 < unflowed
    lo, hi = Fraction(lo, SCALE*norm), Fraction(hi, SCALE*norm)
    # Report a rigorous outward-rounded interval in scientific notation.
    power = 0
    while -hi < 1:
        lo, hi = 10*lo, 10*hi
        power += 1
    lower = (lo*1000).__floor__()
    upper = (hi*1000).__ceil__()
    assert upper < 0
    print(f"T={T}, h={h}, s={s}, readings={len(c)}: [{lower},{upper}] * 10^-{power+3}")


if __name__ == "__main__":
    for record in json.loads(Path(__file__).with_name("grids.json").read_text()):
        exact_form(record)
