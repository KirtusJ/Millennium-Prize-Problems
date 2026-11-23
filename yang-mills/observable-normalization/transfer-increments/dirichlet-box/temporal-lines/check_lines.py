"""Independent marginal, sine projection, noncommuting product and exchange controls."""
from itertools import product
from pathlib import Path
import runpy

import numpy as np
from scipy.sparse import diags, eye, kron
from scipy.sparse.linalg import splu

box = runpy.run_path(str(Path(__file__).resolve().parents[1] / "check_box.py"))


def marginal(side):
    matrix, count, _ = box["complex_data"](side)
    hessian = (matrix[:, :count].T @ matrix[:, :count]).tocsc()
    interior = range(1, side)
    vertices = list(product(interior, repeat=3))
    # All free bottom time links precede every other free variable in
    # the full incidence assembly (its vertex order starts with time).
    n = len(vertices)
    forcing = np.zeros((count, n))
    forcing[:n, :] = np.eye(n)
    covariance = splu(hessian).solve(forcing)[:n]
    t = diags([-np.ones(side-2), 2*np.ones(side-1), -np.ones(side-2)], [-1, 0, 1])
    ident = eye(side-1)
    spatial = kron(kron(t, ident), ident) + kron(kron(ident, t), ident) + kron(kron(ident, ident), t)
    defect = np.max(np.abs(spatial @ covariance - side*np.eye(n)))
    assert defect < 1.e-11 and np.max(np.diag(covariance)) < 6*side
    indices = np.array(vertices)
    modes = np.array([(2/side)**1.5*np.prod(np.sin(np.pi*indices*k/side), axis=1) for k in indices])
    eig = 4*np.sum(np.sin(np.pi*indices/(2*side))**2, axis=1)
    wh = np.sqrt(eig/side)[:, None]*modes
    assert np.max(np.abs(wh @ covariance @ wh.T - np.eye(n))) < 1.e-11
    print(f'L={side}: {count} free links, {n} modes, inverse residual {defect:.3g}, '
          f'maximum spatial Green diagonal {np.max(np.diag(covariance))/side:.6f}')


def qexp(v):
    norm = np.linalg.norm(v, axis=1)
    return np.column_stack((np.cos(norm), np.sinc(norm/np.pi)[:, None]*v))


def group_control():
    rng = np.random.default_rng(813907)
    b, c, root = rng.normal(size=(3, 120, 3))
    root = qexp(root)
    conj = lambda q: q * [1., -1., -1., -1.]
    mul = box["multiply"]
    diffs = []
    for beta in (16., 256., 4096., 65536.):
        u, v = qexp(b/np.sqrt(beta)), qexp(c/np.sqrt(beta))
        relative = mul(u, conj(v))
        first = mul(mul(root, u), conj(root))
        second = mul(mul(root, v), conj(root))
        np.testing.assert_allclose(mul(first, conj(second)), mul(mul(root, relative), conj(root)),
                                   atol=2.e-14)
        error = np.linalg.norm(np.sqrt(beta)*relative[:, 1:] - (b-c), axis=1)
        bound = (np.linalg.norm(b, axis=1)+np.linalg.norm(c, axis=1))**2/(2*np.sqrt(beta))
        assert np.all(error <= bound + 1.e-13)
        diffs.append(np.max(error))
    assert diffs[-1] < diffs[0]/30
    print('maximum nonabelian linearization errors:', *[round(x, 6) for x in diffs])


def exchange_control():
    rng = np.random.default_rng(917)
    for _ in range(200):
        # The Wilson density is zero at the last atom. The other
        # bad atom has positive mass for both measures.
        f = np.r_[rng.uniform(.1, 3., 6), 0.]
        g = rng.uniform(.1, 3., 7)
        p, q = f/f.sum(), g/g.sum()
        good = np.arange(7) < 5
        z = np.outer(p, q)
        tv = np.abs(p-q).sum()/2
        swapped = np.maximum(z-z.T, 0).sum()
        h = np.log(f[good]/g[good])
        upper = p[~good].sum()+q[~good].sum() + (p[good]+q[good]) @ np.abs(h)
        assert tv <= swapped+1.e-14 and swapped <= upper+1.e-14
    print('200 exchanged-density tests with unequal supports')


if __name__ == "__main__":
    for L in range(2, 8):
        marginal(L)
    group_control()
    exchange_control()
