"""Independent numerical controls of the effective potential and half-line energy."""
from itertools import product

import mpmath as mp
import numpy as np
from scipy.linalg import eigh_tridiagonal


def jacobian(x, a, b, c, d):
    squared_norm = a*a + b*b + c*c + d*d
    return x**4 - x*x*squared_norm + (a*d-b*c)**2


def control_measure():
    mp.mp.dps = 55
    largest = mp.mpf(0)
    for entries in product((-1, 0, 1), repeat=4):
        coordinates = (mp.mpf(4), *map(mp.mpf, entries))
        x = coordinates[0]
        weight = jacobian(*coordinates)
        root = mp.sqrt(weight)
        potential = mp.mpf(0)
        gradient_sq = mp.mpf(0)
        for k, value in enumerate(coordinates):
            def weight_on_line(t):
                return jacobian(*(coordinates[:k] + (t,) + coordinates[k+1:]))
            gradient_sq += mp.diff(weight_on_line, value)**2
            potential += mp.diff(lambda t: mp.sqrt(weight_on_line(t)), value, 2)/(2*root)
        predicted = x*x/weight - gradient_sq/(8*weight**2)
        assert abs(potential-predicted) < mp.mpf('1e-50')
        assert abs(potential) <= 13/x**2
        largest = max(largest, abs(x*x*potential))
    print("81 slice Jacobian controls; largest dimensionless magnitude", mp.nstr(largest, 14))


def control_airy():
    target = float(-2*mp.airyaizero(1))
    print("Airy constant", mp.nstr(-2*mp.airyaizero(1), 35))
    previous_error = None
    for intervals in (512, 1024, 2048, 4096):
        step = 12/intervals
        points = step*np.arange(1, intervals)
        diagonal = 1/step**2 + 4*points
        off_diagonal = np.full(len(points)-1, -0.5/step**2)
        energy = eigh_tridiagonal(diagonal, off_diagonal, eigvals_only=True,
                                  select='i', select_range=(0, 0))[0]
        error = abs(energy-target)
        if previous_error is not None:
            assert 3.9 < previous_error/error < 4.1
        print(f"{intervals:4d} intervals: {energy:.10f}, absolute error {error:.4g}")
        previous_error = error
    assert previous_error < 1e-5


if __name__ == '__main__':
    control_measure()
    control_airy()
