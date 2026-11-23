"""Independent four-tensor and positive-time tests with one compact spatial bump."""
from itertools import combinations

import numpy as np
from sympy import Matrix, Rational
from numpy.polynomial.legendre import leggauss

METRIC = np.diag([1., -1., -1., -1.])


def boost(direction, rapidity):
    n = np.asarray(direction, dtype=float)
    c, h = np.cosh(rapidity), np.sinh(rapidity)
    matrix = np.eye(4)
    matrix[0, 0] = c
    matrix[0, 1:] = matrix[1:, 0] = h*n
    matrix[1:, 1:] += (c-1)*np.outer(n, n)
    return matrix


def tensor_check():
    rng = np.random.default_rng(814)
    worst = 0.
    for _ in range(60):
        n = rng.normal(size=3)
        n /= np.linalg.norm(n)
        eta = rng.uniform(-1.5, 1.5)
        m = rng.uniform(.25, 4)
        transform = boost(n, eta)
        assert np.allclose(transform.T @ METRIC @ transform, METRIC)
        rest = rng.normal(size=(3, 3))
        rest = (rest + rest.T)/2
        tensor = np.zeros((4, 4))
        tensor[1:, 1:] = rest
        moving = transform @ tensor @ transform.T
        p = transform @ np.array([m, 0., 0., 0.])
        expected = p[1:] @ p[1:] / m**2 * (n @ rest @ n)
        worst = max(worst, abs(moving[0, 0] - expected), np.linalg.norm(p @ METRIC @ moving))

        # The longitudinal null Ward identities allow transverse entries here.
        null = np.zeros((4, 4))
        null[1:, 1:] = rest
        null[1:, 0] = null[0, 1:] = rest @ n
        null[0, 0] = n @ rest @ n
        moving = transform @ null @ transform.T
        worst = max(worst, abs(moving[0, 0] - np.exp(2*eta)*null[0, 0]))
    if worst > 2e-12:
        raise AssertionError(worst)
    return worst


def observer_check():
    basis = Matrix.eye(4)
    rest = basis.col(0)
    axes = [basis.col(i) for i in range(1, 4)]
    directions = [rest]
    for axis in axes:
        directions.extend([rest + axis/2, rest - axis/2])
    directions.extend(rest + (a+b)/2 for a, b in combinations(axes, 2))
    rows = []
    for v in directions:
        assert v[0]**2 > sum(x**2 for x in v[1:])
        rows.append([x**2 for x in v] +
                    [2*v[i]*v[j] for i, j in combinations(range(4), 2)])
    observations = Matrix(rows)
    inverse = observations.inv()
    norm = max(sum(abs(x) for x in inverse.row(i)) for i in range(10))
    determinant = abs(observations.det())
    axial_rank = observations[:7, :].rank()
    assert (determinant, axial_rank, norm) == (Rational(1, 64), 7, 8)
    return determinant, axial_rank, norm


def interval(order, a, b):
    x, w = leggauss(order)
    return (a+b)/2 + (b-a)/2*x, (b-a)/2*w


def core(order, L, mass, rank):
    # phi(x)=exp(-1/(1-|x|²)) on the unit ball, with zero extension.
    # Fourier convention is unnormalized. Here only the annulus 1 ≤ |k|/L ≤ 2 is integrated.
    r, wr = interval(order, 0., 1.)
    q, wq = interval(order, 1., 2.)
    radial = np.exp(-1/(1-r*r))*r**2
    ft = 4*np.pi*(np.sinc(np.outer(q, r)/np.pi) @ (wr*radial))
    energy_in_test_units = np.sqrt(q*q + (mass/L)**2)
    detector = np.exp(-energy_in_test_units)*np.expm1(-energy_in_test_units)**2
    # With unit mass and unit spectral coefficient, rank one gives a conserved Proca
    # time component. Rank two uses the scalar improvement tensor at either mass.
    density = 4*np.pi*q**(2+2*rank)*ft**2*detector/(2*energy_in_test_units)
    return L**(2*rank-4) * (wq @ density)


if __name__ == "__main__":
    print("observer determinant magnitude, axial rank, inverse row norm", *observer_check())
    print("maximum matrix residual", f"{tensor_check():.3g}")
    for L in (1., 4., 16., 64.):
        cases = [(1., 2), (0., 2), (1., 1)]
        values = [core(96, L, m, r) for m, r in cases]
        high = [core(192, L, m, r) for m, r in cases]
        if not np.allclose(values, high, rtol=1e-10, atol=1e-13):
            raise AssertionError((values, high))
        print(int(L), *(f"{v:.10g}" for v in values))
    tensor_ratio = core(96, 64., 1., 2)/core(96, 16., 1., 2)
    current_ratio = core(96, 64., 1., 1)/core(96, 16., 1., 1)
    if not (.99 < tensor_ratio < 1.01 and .061 < current_ratio < .064):
        raise AssertionError((tensor_ratio, current_ratio))
