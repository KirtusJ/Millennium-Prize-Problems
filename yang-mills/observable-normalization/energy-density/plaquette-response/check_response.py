"""Finite-torus incidence and a two-square nonabelian Hamiltonian check."""
from collections import defaultdict
from itertools import combinations, product

import numpy as np
from scipy.linalg import eigh
from scipy.special import roots_chebyu, roots_legendre
from scipy.sparse import coo_matrix, eye
from scipy.sparse.linalg import eigsh


def torus(side):
    def shift(x, i):
        xs = list(x)
        xs[i] = (xs[i]+1) % side
        return tuple(xs)
    incident = defaultdict(list)
    for x in product(range(side), repeat=3):
        for i, j in combinations(range(3), 2):
            square = frozenset([(x, i), (x, j), (shift(x, j), i), (shift(x, i), j)])
            for edge in square:
                incident[edge].append(square)
    boundaries = set()
    for edge, faces in incident.items():
        assert len(faces) == 4
        for p, q in combinations(faces, 2):
            ring = p ^ q
            assert p & q == {edge} and len(ring) == 6 and ring not in boundaries
            boundaries.add(ring)
    seen, stack = set(), [next(iter(incident))]
    while stack:
        edge = stack.pop()
        if edge in seen:
            continue
        seen.add(edge)
        stack.extend(e for p in incident[edge] for e in p if e not in seen)
    assert len(seen) == 3*side**3 and len(boundaries) == 6*len(seen)
    # Build the pair defect independently of the incidence polynomial.
    edge_number = {e: i for i, e in enumerate(incident)}
    face_number = {p: i for i, p in enumerate(dict.fromkeys(
        p for faces in incident.values() for p in faces))}
    e_rows, p_cols, rows, cols, data = [], [], [], [], []
    row = 0
    for edge, faces in incident.items():
        for face in faces:
            e_rows.append(edge_number[edge])
            p_cols.append(face_number[face])
        for p, q in combinations(faces, 2):
            rows.append(row)
            cols.append(edge_number[edge])
            data.append(1.)
            for face in (p, q):
                for e in face:
                    rows.append(row)
                    cols.append(edge_number[e])
                    data.append(-1/8)
            row += 1
    incidence = coo_matrix((np.ones(len(e_rows)), (e_rows, p_cols)),
                           shape=(len(seen), len(face_number))).tocsr()
    defects = coo_matrix((data, (rows, cols)), shape=(row, len(seen))).tocsr()
    D = 4*eye(len(seen))-incidence @ incidence.T / 4
    J = defects.T @ defects
    residual = J-D/2-D @ D/4
    assert residual.nnz == 0
    s = np.cos(np.pi/side)
    d = 8*np.sin(np.pi/side)**2/(4-s*s+s*np.sqrt(s*s+8))
    expected = d/2+d*d/4
    v0 = np.random.default_rng(79).normal(size=len(seen))
    lowest = np.sort(eigsh(J, k=3, which='SA', v0=v0, tol=1e-11,
                           return_eigenvectors=False))
    assert abs(lowest[0]) < 1e-13 and np.max(abs(lowest[1:]-expected)) < 1e-11
    return len(seen), len(boundaries), lowest[1], expected


def polynomials(exponents, coords):
    result = np.ones((coords.shape[1], len(exponents)))
    for i, exponent in enumerate(exponents):
        for k in range(3):
            result[:, i] *= coords[k]**exponent[k]
    return result


def casimir(exponents, coords, active):
    # On a sphere coordinate pair a,b, grad(a).grad(b)=s-ab.
    # For C_X take a=x, b=z, s=y. For C_Y exchange x and y.
    # For the common link take a=x,b=y,s=z; z is invariant.
    i, j, k = active
    a, b, s = coords[[i, j, k]]

    def derivative(p, di, dj):
        ex = np.array(p)
        factor = 1
        for axis in [i]*di + [j]*dj:
            factor *= ex[axis]
            if not factor:
                return 0.
            ex[axis] -= 1
        return factor*np.prod(coords**ex[:, None], axis=0)

    columns = []
    for p in exponents:
        lap = ((1-a*a)*derivative(p, 2, 0)+(1-b*b)*derivative(p, 0, 2)
               +2*(s-a*b)*derivative(p, 1, 1)
               -3*a*derivative(p, 1, 0)-3*b*derivative(p, 0, 1))
        columns.append(-lap/4)
    return np.array(columns).T


def two_faces(degree, couplings):
    x1, wx = roots_chebyu(degree+4)
    u1, wu = roots_legendre(degree+4)
    x, y, u = (q.ravel() for q in np.meshgrid(x1, x1, u1, indexing='ij'))
    z = x*y+np.sqrt((1-x*x)*(1-y*y))*u
    coords = np.array([x, y, z])
    weights = np.einsum("i,j,k->ijk", wx*2/np.pi, wx*2/np.pi, wu/2).ravel()
    indices = [p for p in product(range(degree+1), repeat=3) if sum(p) <= degree]
    basis = polynomials(indices, coords)
    integrate = basis.T*weights
    metric = integrate @ basis
    Cx, Cy, Ccommon = (integrate @ casimir(indices, coords, pair) for pair
                       in [(0, 2, 1), (1, 2, 0), (0, 1, 2)])
    S = integrate @ ((x+y)[:, None]*basis)
    kinetic = 3*Cx+3*Cy+Ccommon
    assert max(np.max(np.abs(M-M.T)) for M in (Cx, Cy, Ccommon, S)) < 1e-12
    expected = np.array([1/144, 3/2704])*(3/4)**2/9
    rows = []
    for lam in couplings:
        energies, vectors = eigh(kinetic-lam*S, metric)
        energies -= energies[0]
        # Only the shared electric link has unit weight. Both faces have weight 1/4.
        outputs = vectors.T @ (Ccommon-lam*S/4) @ vectors[:, 0]
        outputs[0] = 0.
        squares = (outputs/lam**2)**2
        bands = np.array([squares[np.abs(energies-h)<.2].sum() for h in (4.5, 6.5)])
        moment = squares @ energies
        rows.append([lam, *bands, moment])
    assert np.max(np.abs(bands/expected-1)) < .001
    assert abs(moment/((3/4)**2/234)-1) < .001
    return np.array(rows)


def main():
    for n in (5, 6, 7):
        print("torus", n, *torus(n))
    levels = [.16, .08, .04, .02]
    primary = two_faces(4, levels)
    repeat = two_faces(5, levels)
    assert np.max(np.abs(primary-repeat)) < 4e-8
    print("lambda, spin-zero and spin-one band weights, first moment (all divided by lambda^4)")
    for row in primary:
        print(" ".join(f"{x:.10g}" for x in row))
    print("predicted", *((3/4)**2*np.array([1/(9*144), 3/(9*2704), 1/234])))


if __name__ == '__main__':
    main()
