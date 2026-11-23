"""Finite cubical, quaternion and integral controls for the periodic Wilson calculation."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
import json
from math import comb, pi, prod


AXES = range(4)
PLANES = tuple(combinations(AXES, 2))


def step(x, axis, side, sign=1):
    y = list(x)
    y[axis] = (y[axis] + sign) % side
    return tuple(y)


def path(x):
    return [i + 1 for i in AXES for _ in range(x[i])]


def inverse(word):
    return [-letter for letter in reversed(word)]


def reduce_word(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return stack


def plaquette(x, i, j, side):
    return [((x, i), 1), ((step(x, i, side), j), 1),
            ((step(x, j, side), i), -1), ((x, j), -1)]


def lattice(side):
    vertices = list(product(range(side), repeat=4))
    links = [(x, i) for x in vertices for i in AXES]
    tree = set()
    for x in vertices[1:]:
        i = max(j for j in AXES if x[j])
        tree.add((step(x, i, side, -1), i))
    anchors = {(tuple(side - 1 if j == i else 0 for j in AXES), i) for i in AXES}
    free = [e for e in links if e not in tree and e not in anchors]
    assert len(tree) == len(vertices) - 1 and len(free) == 3 * (len(vertices) - 1)
    return vertices, links, free


def graph_controls(side):
    vertices, _, free = lattice(side)
    filled = 0
    for x, i in free:
        word = path(x) + [i + 1] + inverse(path(step(x, i, side)))
        if x[i] == side - 1:
            word += [-(i + 1)] * side
        assert not reduce_word(sorted(word, key=abs))
        filled += 1
    for i, j in PLANES:
        axes_i, axes_j = [i + 1] * side, [j + 1] * side
        word = axes_i + axes_j + inverse(axes_i) + inverse(axes_j)
        assert not reduce_word(sorted(word, key=abs))
        filled += 1

    face_count = sheet_count = 0
    for x in vertices:
        for i, j in PLANES:
            edges = plaquette(x, i, j, side)
            background = [sign * (a + 1) for (y, a), sign in edges if y[a] == side - 1]
            expected = [i + 1, j + 1, -i - 1, -j - 1] if x[i] == x[j] == side - 1 else []
            assert reduce_word(background) == expected
            face_count += 1
            for a, b in PLANES:
                # Integer potential equals L^2 times the primitive in proof.md.
                def potential(y, direction):
                    if direction == a:
                        return y[b]
                    if direction == b:
                        return -side * y[a] * (y[b] == side - 1)
                    return 0
                curl = sum(sign * potential(*edge) for edge, sign in edges)
                target = side ** 2 * (x[i] == x[j] == side - 1) - 1 if (i, j) == (a, b) else 0
                assert curl == target
                sheet_count += 1
    return filled, face_count, sheet_count


def gram(rows, size):
    matrix = [[0] * size for _ in range(size)]
    for row in rows:
        for i, a in row.items():
            for j, b in row.items():
                matrix[i][j] += a * b
    return matrix


def determinant(matrix, prime=None):
    """Bareiss for the small positive Gram matrices; modular elimination for L=3."""
    matrix = [row[:] for row in matrix]
    n = len(matrix)
    if not n:
        return 1
    if prime is not None:
        det = 1
        for k in range(n):
            pivot = next((i for i in range(k, n) if matrix[i][k] % prime), None)
            if pivot is None:
                return 0
            if pivot != k:
                matrix[k], matrix[pivot] = matrix[pivot], matrix[k]
                det = -det
            value = matrix[k][k] % prime
            det = det * value % prime
            reciprocal = pow(value, -1, prime)
            for row in matrix[k + 1:]:
                scale = row[k] * reciprocal % prime
                if scale:
                    for j in range(k + 1, n):
                        row[j] = (row[j] - scale * matrix[k][j]) % prime
        return det
    previous = 1
    for k in range(n - 1):
        pivot = matrix[k][k]
        assert pivot > 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = matrix[i][j] * pivot - matrix[i][k] * matrix[k][j]
                matrix[i][j], remainder = divmod(numerator, previous)
                assert remainder == 0
        previous = pivot
    return matrix[-1][-1]


def determinant_control(side):
    vertices, links, free = lattice(side)
    volume = len(vertices)
    col = {e: number for number, e in enumerate(free)}
    curl_rows = []
    for x in vertices:
        for i, j in PLANES:
            row = Counter()
            for e, sign in plaquette(x, i, j, side):
                if e in col:
                    row[col[e]] += sign
            curl_rows.append(row)
    vertex_col = {v: number for number, v in enumerate(vertices[1:])}
    gradient_rows = []
    for x, i in links:
        y = step(x, i, side)
        row = Counter()
        if x in vertex_col:
            row[vertex_col[x]] -= 1
        if y in vertex_col:
            row[vertex_col[y]] += 1
        gradient_rows.append(row)
    modulus = 1000003 if side == 3 else None
    tree_count = determinant(gram(gradient_rows, volume - 1), modulus)
    normal = determinant(gram(curl_rows, len(free)), modulus)
    # At L=2 and L=3 each active coordinate costs 4 or 3 respectively.
    eigen_unit = 3 if side == 3 else 4
    fourier_tree = prod((eigen_unit * j) ** (comb(4, j) * (side - 1) ** j)
                        for j in range(1, 5)) // volume
    expected = volume * fourier_tree ** 2
    assert tree_count == (fourier_tree % modulus if modulus else fourier_tree)
    assert normal == (expected % modulus if modulus else expected)
    return {"L": side, "modulus": modulus, "tree_count": tree_count, "curl_gram": normal}


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0])


def multiply(q, p):
    v, w = q[1:], p[1:]
    return (q[0]*p[0] - dot(v,w), *(q[0]*wj + p[0]*vj + cj
                                      for vj,wj,cj in zip(v,w,cross(v,w))))


def conjugate(q):
    return (q[0], *(-c for c in q[1:]))


def quaternion_control():
    quats = []
    for v in product(range(-1, 2), repeat=3):
        r = dot(v, v)
        quats.append((F(1-r, 1+r), *(F(2*x, 1+r) for x in v)))
    for q, p in product(quats, repeat=2):
        commutator = multiply(multiply(q,p), multiply(conjugate(q),conjugate(p)))
        normal = cross(q[1:], p[1:])
        assert 1 - commutator[0] == 2 * dot(normal, normal)
    return len(quats) ** 2


def cube_control():
    """Independent Simpson integration over the eight positive octants."""
    panels = 32
    weights = [(1 if i in (0, panels) else 4 if i % 2 else 2) for i in range(panels + 1)]
    integral = 8 * sum(weights[i] * weights[j] * weights[k] /
                       (1 + (i*i + j*j + k*k) / panels**2) ** 2
                       for i,j,k in product(range(panels + 1), repeat=3)) / (3*panels)**3
    assert abs(integral - pi**2 / 4) < 2e-7
    coefficient = 4 * (4*pi) / pi**8 / 4 * (pi/2)**3 * integral
    assert abs(coefficient - 1/(8*pi**2)) < 2e-9
    return round(coefficient, 10)


if __name__ == "__main__":
    counts = [graph_controls(s) for s in (1, 2, 3, 4)]
    print(json.dumps({"based_words_faces_sheet_values": [sum(column) for column in zip(*counts)],
                      "quaternion_pairs": quaternion_control(), "one_site_coefficient": cube_control(),
                      "determinants": [determinant_control(s) for s in (1,2,3)]}, indent=2))
