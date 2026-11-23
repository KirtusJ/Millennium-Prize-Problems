"""Enclose the buffered midpoint ratio using strided ordinary-moment intervals."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import sys

G4_CLOCK = Path(__file__).resolve().parents[4] / "g4" / "site-clock"
sys.path.insert(0, str(G4_CLOCK))
from clock import moment_interval, moment_prefix


def strided(target, known, stride):
    """Apply the ordinary-moment enclosure to u^r dν pushed forward by u ↦ u^s."""
    if target < len(known):
        return known[target]
    quotient, residue = divmod(target, stride)
    subsequence = known[residue::stride]
    return moment_interval(quotient, subsequence)


def enclose(payload):
    target, stride = payload["target_index"], payload["stride"]
    if type(target) is not int or target < 1:
        raise ValueError("target_index must be a positive integer.")
    known = moment_prefix(payload["moments"])[:target + 1]
    if type(stride) is not int or not 1 <= stride <= len(known):
        raise ValueError("stride must be between one and the length of the usable prefix.")
    h = (target - 1) // 2
    middle = strided(h, known, stride)
    clock = strided(target, known, stride)
    ratio = None
    if clock[0] > 0:
        lo, hi = max(Fraction(1), middle[0]/clock[1]), middle[1]/clock[0]
        if lo > hi:
            raise ValueError("The supplied intervals contradict moment monotonicity.")
        ratio = list(map(str, (lo, hi)))
    return {"target_index": target, "midpoint_index": h, "stride": stride,
            "last_supplied_index": len(known)-1,
            "clock_moment": list(map(str, clock)), "midpoint_moment": list(map(str, middle)),
            "midpoint_ratio": ratio}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        result = enclose(json.loads(args.input.read_text(encoding="utf-8")))
    except (ValueError, KeyError, TypeError, ZeroDivisionError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))
