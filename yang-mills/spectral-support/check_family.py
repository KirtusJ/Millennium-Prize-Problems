"""Exact interpolation certificate for the six E1 observations at anchor energies 1,...,6."""
from fractions import Fraction as Q


def inverse_with_determinant(matrix):
    size = len(matrix)
    augmented = [
        list(row) + [Q(i == j) for j in range(size)]
        for i, row in enumerate(matrix)
    ]
    determinant = Q(1)
    for j in range(size):
        pivot = next(i for i in range(j, size) if augmented[i][j])
        if pivot != j:
            augmented[j], augmented[pivot] = augmented[pivot], augmented[j]
            determinant = -determinant
        diagonal = augmented[j][j]
        determinant *= diagonal
        augmented[j] = [x / diagonal for x in augmented[j]]
        for i in range(size):
            if i == j:
                continue
            multiple = augmented[i][j]
            augmented[i] = [x - multiple * y for x, y in zip(augmented[i], augmented[j])]
    return determinant, [row[size:] for row in augmented]


def verify():
    anchors = range(1, 7)
    matrix = [[Q(j) ** k for j in anchors] for k in range(4)]
    matrix += [[Q(1, base) ** j for j in anchors] for base in (2, 4)]
    determinant, inverse = inverse_with_determinant(matrix)
    identity = [[sum(x * y for x, y in zip(row, col)) for col in zip(*inverse)] for row in matrix]
    expected_identity = [[Q(i == j) for j in range(6)] for i in range(6)]
    assert identity == expected_identity
    assert determinant == -Q(243, 32768)
    mean = [sum(row) / 6 for row in matrix]
    assert mean == [1, Q(7, 2), Q(91, 6), Q(147, 2), Q(21, 128), Q(455, 8192)]
    max_row_sum = max(sum(abs(x) for x in row) for row in inverse)
    assert max_row_sum == Q(58492, 27)
    minimum_anchor_weight = Q(1, 6) - max_row_sum / 32768
    assert minimum_anchor_weight > Q(1, 12)
    print(f"det(A) = {determinant}")
    print(f"A * inverse = I; maximum absolute row sum = {max_row_sum}")
    print(f"anchor weight lower bound = {minimum_anchor_weight} > 1/12")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run with assertions enabled.")
    verify()
