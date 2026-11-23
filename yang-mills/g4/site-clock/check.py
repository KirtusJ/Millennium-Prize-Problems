"""Exact rational controls for the buffered Wilson clock moment calculator."""
from fractions import Fraction as F
import json
from math import comb
from clock import approximation, enclose, moment_interval, moment_prefix


def value(coefficients, x):
    total = F(0)
    for coefficient in reversed(coefficients):
        total = total * x + coefficient
    return total


def polynomial_controls():
    count = 0
    for target in range(14):
        for degree in range(target + 1):
            coefficients, tail = approximation(target, degree)
            independent = sum(comb(2 * target, j) for j in range(2 * target + 1)
                              if abs(j - target) > degree)
            assert tail == F(independent, 4 ** target)
            assert 1 - value(coefficients, F(1)) == tail
            for i in range(17):
                x = F(i, 16)
                assert abs(x ** target - value(coefficients, x)) <= tail
                count += 1
    return count


def integral_controls():
    spectra = [[(F(0), F(7))], [(F(1), F(3, 7))],
               [(F(0), F(1, 9)), (F(1, 4), F(3)), (F(4, 5), F(2, 3))]]
    count = 0
    for spectrum in spectra:
        moments = [sum(weight * u ** r for u, weight in spectrum) for r in range(35)]
        for delta in (F(0), F(1, 10 ** 15), F(1, 40)):
            prefix = moment_prefix([[str(x - delta), str(x + delta)] for x in moments])
            for target in (0, 1, 2, 7, 15, 34):
                for degree in range(min(9, target) + 1):
                    lo, hi = moment_interval(target, prefix[:degree + 1])
                    assert lo <= moments[target] <= hi
                    count += 1
    assert moment_interval(63, [(F(1), F(1)), (F(1, 2), F(1, 2))])[0] == F(1, 2 ** 63)
    return count


def clock_controls():
    # X=exp(-G), G~Gamma(8, rate 1), has E[X^r]=(1+r)^-8.
    target = 255
    middle = (target - 1) // 2
    data = [[str(F(1, (r + 1) ** 8))] * 2 for r in range(target + 1)]
    measured = enclose({"target_index": target, "moments": data, "relative_width": "1/1000"})
    assert measured["width_reached"] and measured["degree_used"] < target
    lo, hi = map(F, measured["midpoint_ratio"])
    assert lo <= F(target + 1, middle + 1) ** 8 <= hi
    assert hi <= F(1001, 1000) ** 2 * lo
    zero = enclose({"target_index": 10, "moments": [[0, 0]]})
    assert zero["midpoint_ratio"] is None and not zero["width_reached"]
    incomplete = enclose({"target_index": 63, "moments": [[1, 1], ["1/2", "1/2"]]})
    assert not incomplete["width_reached"] and incomplete["midpoint_ratio"] is not None
    assert incomplete["midpoint_ratio"] == ["1", str(2 ** 32)]
    # An invisible denominator at degree zero and a nonintegral midpoint in clock units.
    partial = enclose({"target_index": 4, "moments": [[1, 1]]})
    assert partial["midpoint_index"] == 1 and partial["midpoint_ratio"] is None
    for bad in ({"target_index": 0, "moments": [[1, 1]]},
                {"target_index": 2, "moments": [[1, 1], [2, 2]]},
                {"target_index": 2, "moments": [[0.1, 1]]}):
        try:
            enclose(bad)
        except ValueError:
            continue
        raise AssertionError("An invalid input passed.")
    return {"target_index": target, "degree_used": measured["degree_used"],
            "exact_midpoint_ratio": str(F(target + 1, middle + 1) ** 8)}


def resolution_control():
    # Rational cutoff, shared top atom and three increasingly separated clocks.
    cutoff = F(7, 8)
    weight = (1 - cutoff) ** 8
    counts = []
    for target in (512, 1024, 2048):
        middle = (target - 1) // 2
        edge = F(target, target + 1)
        plus = weight * cutoff ** (target // 4)
        minus = weight * cutoff ** (2 * target)

        def moment(k, light):
            return F(1, 2) ** k + weight * cutoff ** k + light * edge ** k

        bounded = moment(middle, plus) / moment(target, plus)
        divergent = moment(middle, minus) / moment(target, minus)
        assert 1 < bounded < 3
        assert divergent >= cutoff ** (middle - target) / (1 + cutoff ** target)
        for k in (0, 1, middle, target, 2 * target):
            assert 0 <= moment(k, plus) - moment(k, minus) <= plus
        counts.append(divergent.numerator.bit_length() - divergent.denominator.bit_length())
    assert counts[0] < counts[1] < counts[2]
    return counts


def secant_controls():
    count = 0
    for nodes in ((F(0), F(1, 4), F(4, 5)), (F(1, 5), F(1, 2), F(9, 10)), (F(1, 3),)):
        def moment(i):
            return sum(u ** i for u in nodes)

        for target in (17, 33, 65):
            middle = (target - 1) // 2
            ratio = moment(middle) / moment(target)
            for k in (1, 2, 3):
                # Physical lags r=2+2k and 2r have moment indices k and 2k+1.
                assert 2 * k + 1 <= middle
                assert 1 / max(nodes) ** (target - middle) <= ratio
                assert ratio ** (k + 1) <= (moment(k) / moment(2 * k + 1)) ** (target - middle)
                count += 1
    return count


if __name__ == "__main__":
    print(json.dumps({"polynomial_points": polynomial_controls(),
                      "spectral_enclosures": integral_controls(),
                      "gamma_control": clock_controls(),
                      "resolution_ratio_binary_orders": resolution_control(),
                      "two_sided_secants": secant_controls()}, indent=2))
