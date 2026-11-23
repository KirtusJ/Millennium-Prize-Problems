"""Correlated post-hoc thermal transition diagnostics on Z4's frozen rows."""
from fractions import Fraction
from math import comb
from pathlib import Path

import numpy as np

DATA = Path(__file__).resolve().parents[2] / "z4/reviews/ext-match/predeclared"


def moment(corr, t, j):
    return sum((-1)**(j-k) * comb(2*j, j+k) * corr[(t+k) % len(corr)]
               for k in range(-j, j+1))


def exact_control():
    for side in (6, 8, 12):
        for roots in [(Fraction(1, 2),), (Fraction(1, 2), Fraction(2, 3))]:
            def value(t):
                return 3 + sum(z**t + z**(side-t) for z in roots)
            corr = [value(t) for t in range(side)]
            for t in (2, 3):
                for j in range(t+1):
                    target = 3 * (j == 0) + sum(
                        (z**t + z**(side-t)) * (z+1/z-2)**j for z in roots)
                    assert moment(corr, t, j) == target
            q = [moment(corr, 3, j) for j in (1, 2, 3)]
            assert (q[0]*q[2]-q[1]**2 > 0) == (len(roots) == 2)


def evaluate(sums, n, side):
    mean = sums[0] / n
    corr = sums[1:] / (n * mean**2) - 1
    # Ordinary determinant tests a single frequency, including zero.
    h = [moment(corr, 2, j) for j in range(3)]
    # The shifted determinant ignores any time-independent contribution.
    q = [moment(corr, 3, j) for j in (1, 2, 3)]
    return np.array([h[0]*h[2]-h[1]**2, q[0]*q[2]-q[1]**2])


def check(side, block):
    blocks = []
    for path in sorted(DATA.glob(f"meas_L{side}_*.txt")):
        raw = np.loadtxt(path)[10:, -(side+1):-1]
        raw = raw[:len(raw)//block*block]
        stats = np.column_stack([raw.mean(1)] +
            [(raw*np.roll(raw, t, axis=1)).mean(1) for t in range(side)])
        blocks.extend(stats.reshape(-1, block, side+1).sum(1))
    blocks = np.array(blocks)
    total = blocks.sum(0)
    count = len(blocks)
    est = evaluate(total, count*block, side)
    replicas = np.array([evaluate(total-b, (count-1)*block, side) for b in blocks])
    error = replicas.std(0)*np.sqrt(count-1)
    corrected = est - (count-1)*(replicas.mean(0)-est)
    print(side, block, count, *[f"{a:.8g} ({b:.8g})" for a,b in zip(corrected,error)])


if __name__ == "__main__":
    exact_control()
    for side, block in [(6,11), (8,17), (12,25)]:
        check(side,block)
        check(side,2*block)
