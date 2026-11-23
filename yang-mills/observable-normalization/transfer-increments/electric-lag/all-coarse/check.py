"""Independently enumerate Fourier characters of a binary electric regulator."""
from itertools import combinations, product
from math import exp, expm1, log, sqrt

import numpy as np


def shift(p, axis, amount, L):
    return tuple((x+amount*(j == axis)) % L for j, x in enumerate(p))


def edge(p, axis, L):
    x, y, z = p
    return 1 << (axis+3*(x+L*(y+L*z)))


def square(p, a, b, width, L):
    result = 0
    for i in range(width):
        for axis, other in ((a, b), (b, a)):
            start = shift(p, axis, i, L)
            result ^= edge(start, axis, L) ^ edge(shift(start, other, width, L), axis, L)
    return result


def lattice(mesh):
    L = 4*mesh
    sites = list(product(range(L), repeat=3))
    faces = [square(p, a, b, 1, L) for p in sites for a, b in combinations(range(3), 2)]
    mesh_edges = sum(edge(p, j, L) for p in sites for j in range(3)
                     if all(p[i] % mesh == 0 for i in range(3) if i != j))
    plus_mesh = [p & ~mesh_edges for p in faces]
    assert all(v.bit_count() >= 2 for v in plus_mesh)
    assert len(set(plus_mesh)) == len(faces)
    # B4's center background flips every face and fixes all even segments.
    negative = sum(edge(p, j, L) for p in sites for j in range(3) if sum(p[:j]) % 2)
    assert all((negative & f).bit_count() % 2 for f in faces)
    if mesh % 2 == 0:
        for p in product(range(0, L, mesh), repeat=3):
            for j in range(3):
                path = sum(edge(shift(p, j, i, L), j, L) for i in range(mesh))
                assert (negative & path).bit_count() % 2 == 0
    return L, faces, mesh_edges


def controls(mesh, q=0.95, n=3):
    L, faces, mesh_edges = lattice(mesh)
    origins = [(0, 0, 0), (mesh, 0, 0)]
    generators = [square(p, a, b, mesh, L)
                  for p in origins for a, b in combinations(range(3), 2)]
    columns = [0]
    for g in generators:
        columns += [col ^ g for col in columns]
    assert len(columns) == len(set(columns))
    rows, coordinates = {}, []
    for j, col in enumerate(columns[1:]):
        E = col.bit_count()
        r = q**E
        for face in faces:
            target = col ^ face
            if not col & face:
                assert target.bit_count() == E+4
                assert abs(q**target.bit_count() - q**4*r) < 2e-15
                continue
            assert target & ~mesh_edges
            t = q**target.bit_count()
            assert t <= r
            h = sum(t**i*r**(n-1-i) for i in range(n))
            value = h*(t-q**4*r)/((1-q**4)*sqrt((1-r**n)*(1-t**n)))
            row = rows.setdefault(target, len(rows))
            coordinates.append((row, j, value))
    from scipy.sparse import coo_matrix
    i, j, v = zip(*coordinates)
    operator = coo_matrix((v, (i, j)), shape=(len(rows), len(columns)-1)).tocsr()
    gram = (operator.T @ operator).toarray()
    np.testing.assert_allclose(gram, np.diag(np.diag(gram)), atol=1e-14)
    optimum = sqrt(np.linalg.eigvalsh(gram)[-1])
    upper = 4*sqrt(mesh)*(1/(1-q**4)+n)/expm1(-4*mesh*n*log(q))
    assert 0 < optimum <= upper
    print(f"mesh {mesh}: {len(rows)} output characters, {len(columns)-1} columns, "
          f"relative norm {optimum:.9f}, bound {upper:.9f}")


def time_check(tau):
    for ell in (2, 4, 8, 16):
        k = 4*ell
        factor = sqrt(k)*exp(-k*tau)
        low = factor*(-expm1(-2*tau))/(16*sqrt(expm1(-k*tau)*expm1(-(k+2)*tau)))
        high = 2*sqrt(k)*(tau+1/4)/expm1(k*tau)
        assert 0 < low < high
        q, n = exp(-tau/100000), 100000
        finite = (1-q)*sqrt(k)*q**(k*n+2)*(1-q**(2*n))/(4*(1-q**4)*
                      sqrt((1-q**(k*n))*(1-q**((k+2)*n))))
        np.testing.assert_allclose(low, finite, rtol=2e-5, atol=0)


if __name__ == "__main__":
    for spacing in (2, 3, 4):
        controls(spacing)
    for tau in (0.05, 0.2, 0.5):
        time_check(tau)
