"""Independent cubical incidence, quaternion action, and Dirichlet spectrum checks."""
from itertools import combinations, product

import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh


def step(x, axis):
    y = list(x)
    y[axis] += 1
    return tuple(y)


def complex_data(L):
    def inside(x):
        return all(0 < j < L for j in x)

    vertices = list(product(range(L+1), repeat=4))
    links = [(x, i) for x in vertices for i in range(4) if x[i] < L]
    shell, free = [], []
    for x, i in links:
        if not (inside(x) or inside(step(x, i))):
            shell.append((x, i))
        elif i != 0 or not inside(x):
            free.append((x, i))
    # Tree links have no column. Shell columns are kept for nonzero boundary data.
    numbered = {e: j for j, e in enumerate(free + shell)}
    faces, rows, cols, vals = [], [], [], []
    for x in vertices:
        for i, j in combinations(range(4), 2):
            if x[i] == L or x[j] == L:
                continue
            xi, xj = step(x, i), step(x, j)
            if not any(inside(v) for v in (x, xi, xj, step(xi, j))):
                continue
            keys = [(x, i), (xi, j), (xj, i), (x, j)]
            for k, e in enumerate(keys):
                if e in numbered:
                    rows.append(len(faces))
                    cols.append(numbered[e])
                    vals.append(1. if k < 2 else -1.)
            faces.append([numbered.get(e, len(numbered)) for e in keys])
    D = coo_matrix((vals, (rows, cols)), shape=(len(faces), len(numbered))).tocsr()
    return D, len(free), np.array(faces)


def scalar_root(L):
    s = 12*np.sin(np.pi/(2*L))**2
    diagonal = np.r_[s, np.full(L-1, 2.)]
    off = np.r_[-np.sqrt(s), -np.ones(L-2)]
    return eigh_tridiagonal(diagonal, off, select='i', select_range=(0, 0),
                            eigvals_only=True, tol=1.e-17)[0]


def multiply(a, b):
    s, x = a[:, :1], a[:, 1:]
    t, y = b[:, :1], b[:, 1:]
    return np.concatenate((s*t-(x*y).sum(1, keepdims=True), s*y+t*x+np.cross(x, y)), axis=1)


def actions(D, n, faces, phi, psi, beta):
    field = np.concatenate((phi, psi))
    size = np.linalg.norm(field, axis=1)
    a = size/np.sqrt(beta)
    assert np.max(a) < np.pi
    u = np.c_[np.cos(a), np.sinc(a/np.pi)[:, None]*field/np.sqrt(beta)]
    u = np.vstack((u, [1., 0, 0, 0]))  # all fixed tree edges
    inv = u * np.array([1., -1, -1, -1])
    word = multiply(multiply(u[faces[:, 0]], u[faces[:, 1]]),
                    multiply(inv[faces[:, 2]], inv[faces[:, 3]]))
    compact = beta * np.square(word - [1., 0, 0, 0]).sum()/2
    linear = np.square(D @ field).sum()/2
    jacobian_log = 2*np.log(np.sinc(a[:n]/np.pi)).sum()
    return compact, linear, linear-compact+jacobian_log


def run():
    rng = np.random.default_rng(471382)
    for L in (2, 3, 4, 5, 6):
        D, n, faces = complex_data(L)
        active = D[:, :n]
        gram = active.T @ active
        low = eigsh(gram, k=1, which='SA', v0=rng.normal(size=n),
                    return_eigenvectors=False, tol=1.e-11)[0]
        reduced = scalar_root(L)
        np.testing.assert_allclose(low, reduced, rtol=1.e-9)
        print('side, variables, full minimum, reduced minimum:', L, n, low, reduced)
        # Test the global bound well outside the small-angle region.
        for _ in range(3):
            coords = rng.normal(size=(D.shape[1], 3))
            coords /= np.linalg.norm(coords, axis=1)[:, None]
            coords *= rng.uniform(0, np.pi-1.e-6, size=(len(coords), 1))
            phi, psi = coords[:n], coords[n:]
            for exterior in (psi, np.zeros_like(psi)):
                compact, linear, _ = actions(D, n, faces, phi, exterior, 1.)
                bound = 32*L**3 * (np.pi**2 * compact/2 + np.square(exterior).sum())
                assert np.square(phi).sum() <= bound
                assert np.square(phi).sum() <= 32*L**3*(2*linear+np.square(exterior).sum())
        if L == 2:
            # A fixed, noncommuting interior and shell test on the scaled chart.
            phi, psi = rng.normal(size=(n, 3)), rng.normal(size=(D.shape[1]-n, 3))
            err = [actions(D, n, faces, phi, psi, 2.**k)[2] for k in (10, 16, 22, 28)]
            assert abs(err[-1]) < abs(err[0])/100
            print('pointwise log density differences at beta=2^(10,16,22,28):', *err)
    for L in (16, 64, 256, 1024):
        r = scalar_root(L)
        ratio = L**3*r/(3*np.pi**2)
        assert abs(1-ratio) < 12/L
        print('side, L^3 lambda/(3 pi^2):', L, ratio)


if __name__ == '__main__':
    run()
