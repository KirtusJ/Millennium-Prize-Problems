"""Variational scalar vacuum of -Delta/2 + 2 sum of squared cross products.

Ordered singular values reduce the Gaussian integrals to two angles and an
associated Laguerre radial rule. Trial polynomials use the three elementary
symmetric polynomials of the squared singular values. The even scalar vacuum
has identical density on both determinant signs. Reported moments apply to
the bounded tensor with denominator 1 + trace(Y Y.T) in unit-box coordinates.
Run with OPENBLAS_NUM_THREADS=1. Numerical estimates have no certified errors.
"""
import numpy as np
from scipy.special import roots_genlaguerre, roots_legendre
from scipy.linalg import eigh

def estimate(deg, a, order, angular=16):
    nodes, weights = roots_legendre(angular)
    azimuth = (nodes + 1) * np.pi / 8
    top = np.arctan(1 / np.cos(azimuth))
    polar = (nodes[:, None] + 1) * top / 2
    unit = np.stack(np.broadcast_arrays(np.sin(polar) * np.sin(azimuth), np.sin(polar) * np.cos(azimuth), np.cos(polar)), -1)
    squared_directions = unit ** 2
    jacobian = (squared_directions[:, :, 1] - squared_directions[:, :, 0]) * (squared_directions[:, :, 2] - squared_directions[:, :, 0]) * (squared_directions[:, :, 2] - squared_directions[:, :, 1])
    angular_weights = weights[:, None] * weights * top * np.sin(polar) * jacobian
    u, radial_weights = roots_genlaguerre(order, 3.5)
    X = (np.sqrt(u[:, None, None, None] / a) * unit).reshape(-1, 3)
    weight = (radial_weights[:, None, None] * angular_weights).ravel()
    weight /= weight.sum()
    squares = X ** 2
    t = squares.sum(1)
    pair_sum = (t * t - (squares * squares).sum(1)) / 2
    product = squares.prod(1)
    invariants = np.array([t, pair_sum, product])
    invariant_gradients = np.array([2 * X, 2 * (t[:, None] - squares) * X, 2 * X * np.roll(squares, 1, 1) * np.roll(squares, 2, 1)])
    basis = []
    gradients = []
    for k in range(deg // 3 + 1):
        for j in range((deg - 3 * k) // 2 + 1):
            for i in range(deg - 3 * k - 2 * j + 1):
                power = np.array([i, j, k])
                f = np.prod(invariants ** power[:, None], 0)
                b = f[:, None] * (-a * X + np.sum(power[:, None, None] * invariant_gradients / invariants[:, :, None], 0))
                norm = np.sqrt(weight @ (f * f))
                basis.append(f / norm)
                gradients.append(b / norm)
    B = np.array(basis).T
    G = np.array(gradients)
    H = sum((G[:, :, i] * weight @ G[:, :, i].T / 2 for i in range(3))) + B.T @ ((2 * pair_sum * weight)[:, None] * B)
    S = B.T @ (weight[:, None] * B)
    overlap_eigenvalues, U = eigh(S)
    live = overlap_eigenvalues > 1e-12
    T = U[:, live] / np.sqrt(overlap_eigenvalues[live])
    energies, C = eigh(T.T @ H @ T)
    vacuum_weights = weight * (B @ (T @ C[:, 0])) ** 2
    tensor_average = ((squares * squares).sum(1) - t * t / 3) / (10 * (1 + t) ** 2)
    var = vacuum_weights @ tensor_average
    slope = vacuum_weights @ (2 * (t / 6 - (2 + t) * tensor_average) / (1 + t) ** 2)
    print(deg, a, order, round(energies[0], 8), round(var, 8), round(slope, 8), round(slope / var, 6))
print('degree, Gaussian precision, radial order, vacuum energy, variance, first moment, mean energy')
for a in [2.0, 2.6]:
    for degree in [3, 5, 7, 9]:
        estimate(degree, a, 72)
estimate(9, 2.6, 104, 24)
