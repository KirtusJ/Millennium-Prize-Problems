"""Finite Gaussian determinant compared with the signed Wick-square coefficient."""
from itertools import combinations, permutations

import mpmath as mp

mp.mp.dps = 85


def centered_moment(covariance, coupling):
    count = covariance.rows
    mean = (1 + 2 * coupling * covariance[0, 0]) ** (-mp.mpf("1.5"))
    result = 0
    for size in range(count + 1):
        for subset in combinations(range(count), size):
            matrix = mp.eye(size)
            for i, row in enumerate(subset):
                for j, col in enumerate(subset):
                    matrix[i, j] += 2 * coupling * covariance[row, col]
            determinant = mp.det(matrix) if size else 1
            result += (-mean) ** (count - size) * determinant ** (-mp.mpf("1.5"))
    return result


def wick_square(weights):
    size = weights.rows
    result = 0
    for permutation in permutations(range(size)):
        if any(i == j for i, j in enumerate(permutation)):
            continue
        visited = set()
        cycles = 0
        for vertex in range(size):
            if vertex not in visited:
                cycles += 1
                while vertex not in visited:
                    visited.add(vertex)
                    vertex = permutation[vertex]
        product = mp.fprod(weights[i, j] for i, j in enumerate(permutation))
        result += 2 ** (size - cycles) * 3 ** cycles * product
    return result


def check_order(count):
    coupling = mp.mpf("0.4")
    variance = mp.mpf("1.1")
    coefficient = -coupling * (1 + 2 * coupling * variance) ** (-mp.mpf("2.5"))
    weights = mp.matrix(count)
    for i, j in combinations(range(count), 2):
        weights[i, j] = weights[j, i] = mp.mpf(i + 2) / (2 * j + 3)
    target = coefficient ** count * wick_square(weights)
    errors = []
    for epsilon in map(mp.mpf, ("0.01", "0.001", "0.0001")):
        covariance = variance * mp.eye(count) + epsilon * weights
        actual = centered_moment(covariance, coupling) / epsilon ** count
        errors.append(abs(actual / target - 1))
    assert all(current < previous / 8 for previous, current in zip(errors, errors[1:]))
    assert errors[-1] < mp.mpf("0.001")
    print(count, "signed leading coefficient", mp.nstr(target, 10),
          "final relative error", mp.nstr(errors[-1], 5))


if __name__ == "__main__":
    for number_of_sites in range(2, 7):
        check_order(number_of_sites)
