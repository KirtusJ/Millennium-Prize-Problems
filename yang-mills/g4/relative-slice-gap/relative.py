"""Rational enclosures of the first excited to vacuum Gibbs ratio.

Input is a normalized symmetric table of joint probabilities, one nonnegative
one-sided log-oscillation bound per cell, and the full physical period. The
optional relative_error bounds operator error relative to the measured root
matrix norm. For unequal-cell masking set error_kind to "entrywise_envelope"
only when the same bound holds for the operator norm of the absolute error.
"""
import argparse
from fractions import Fraction as Q
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "paired-slice-spectrum"))
from histogram import spectrum_brackets


def rational(value):
    return Q(str(value))


def relative_bounds(measured, z, error):
    """Uniform geometry and signed operator error. Both output endpoints are rational."""
    low, high = measured
    raw_lo = max(0, (low - error) / (1 + error))
    raw_hi = min(1, (high + error) / (1 - error)) if error < 1 else Q(1)
    h = max(0, 1 - z*z/2)
    d = 1 - h
    a = min(1, z/2)
    lower = max(0, raw_lo - d)**2
    upper = min(1, ((raw_hi + d)**2 + 2*a*a) / h**2) if h else Q(1)
    return lower, upper


def masked_norm(table, weight, bits):
    weighted = [[v*weight(i,j)**2 for j,v in enumerate(row)] for i,row in enumerate(table)]
    return spectrum_brackets(weighted, bits)[0]


def estimate(data, bits=48):
    table = [[rational(x) for x in row] for row in data["probabilities"]]
    z = [rational(x) for x in data["log_oscillations"]]
    period = rational(data["physical_period"])
    error = rational(data.get("relative_error", 0))
    kind = data.get("error_kind", "operator")
    size = len(table)
    if (not 2 <= bits <= 256 or not size or len(z) != size or min(z) < 0
            or period <= 0 or error < 0 or kind not in ("operator", "entrywise_envelope")
            or any(len(row) != size for row in table)
            or any(v < 0 or v != table[j][i] for i,row in enumerate(table) for j,v in enumerate(row))
            or sum(map(sum, table)) != 1):
        raise ValueError("Invalid symmetric probability table, geometry, period, precision, or error")
    (b_lo,b_hi),(v_lo,v_hi) = spectrum_brackets(table, bits)
    measured = (v_lo/b_hi, min(1,v_hi/b_lo) if b_lo else Q(1))
    lower, upper = relative_bounds(measured, max(z), error)
    bound = "uniform"
    if min(z) != max(z) and (not error or kind == "entrywise_envelope"):
        def h(i,j):
            return max(0, 1 - (z[i]+z[j])**2/8)
        ell = masked_norm(table, h, bits)[0]
        e = masked_norm(table, lambda i,j: 1-h(i,j), bits)[1]
        t = masked_norm(table, lambda i,j: min(1,z[i]/2), bits)[1]
        allowance = error*b_hi
        low = (max(0,v_lo-e-2*allowance)/(b_hi+allowance))**2
        high = ((v_hi+e+2*allowance)**2+2*(t+allowance)**2)/(ell-allowance)**2 if ell > allowance else Q(1)
        lower, upper = max(lower,low), min(upper,high)
        bound = "uniform and cellwise"
    if not 0 <= lower <= upper <= 1:
        raise ArithmeticError("Inconsistent spectral bounds")
    return {"probability_ratio": [str(lower),str(upper)], "physical_period": str(period),
            "geometry_used": bound}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=argparse.FileType("r", encoding="utf8"))
    parser.add_argument("--bits", type=int, default=48)
    args = parser.parse_args()
    print(json.dumps(estimate(json.load(args.input), args.bits), indent=2))
