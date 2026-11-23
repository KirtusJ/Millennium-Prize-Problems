"""Independent Lie-basis, cube-covariance and original-matrix checks."""
from itertools import product
from math import pi
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import expm


def basis(n):
    matrices = []
    for i in range(n):
        for j in range(i):
            m = np.zeros((n, n), complex)
            m[i, j], m[j, i] = 1, -1
            matrices.extend([np.sqrt(n/2)*m, 1j*np.sqrt(n/2)*abs(m)])
    for j in range(1, n):
        diagonal = np.array([1]*j+[-j]+[0]*(n-j-1))
        matrices.append(1j*np.sqrt(n/(j*(j+1)))*np.diag(diagonal))
    return np.array(matrices)


def comm(x, y):
    return x @ y-y @ x


def charge(t):
    n, d = t.shape[1], len(t)
    np.testing.assert_allclose(np.einsum("aij,bij->ab", t.conj(), t).real/n, np.eye(d), atol=1e-13)
    f = np.einsum("abij,cij->abc", comm(t[:, None], t), t.conj()).real/n
    casimir = np.einsum("abi,abj->ij", f, f)
    c = np.trace(casimir)/d
    np.testing.assert_allclose(casimir, c*np.eye(d), atol=1e-12)
    tensor = np.einsum("abi,cdi->abcd", f, f)
    swapped = tensor.transpose(0, 3, 2, 1)
    np.testing.assert_allclose(tensor-swapped, tensor.transpose(0, 2, 1, 3), atol=1e-12)
    cubic = np.vdot(f, f).real
    quartic = np.vdot(tensor+swapped, tensor+swapped).real
    np.testing.assert_allclose([cubic, quartic], [d*c, 3*d*c*c])
    return c, cubic, quartic


def compact_groups():
    for n in (2, 3, 4):
        c, cubic, quartic = charge(basis(n))
        np.testing.assert_allclose(c, 2*n*n)
        print("SU", n, "Casimir, cubic and quartic", c, cubic, quartic)
    so = []
    for i in range(3):
        m = np.zeros((3, 3))
        m[(i+1)%3, (i+2)%3], m[(i+2)%3, (i+1)%3] = 1, -1
        so.append(np.sqrt(3/2)*m)
    np.testing.assert_allclose(charge(np.array(so)), [3, 9, 81])
    z = np.eye(3)*np.exp(2j*pi/3)
    adj = (abs(np.trace(z))**2-1)/8
    np.testing.assert_allclose([adj, np.trace(z).real/3], [1, -0.5])
    print("SO(3) defining trace", charge(np.array(so)), "center adjoint/fundamental", adj, -0.5)


FACES = [(0, 1, None, 1), (0, 2, 1, 1), (1, 2, None, 1),
         (0, 1, 2, -1), (0, 2, None, -1), (1, 2, 0, -1)]


def face_cov(side):
    axis = 2*pi*np.arange(side)/side
    k = np.stack(np.meshgrid(axis, axis, axis, axis, indexing="ij"), axis=-1).reshape(-1, 4)
    p = np.expm1(1j*k)
    denominator = np.sum(abs(p)**2, axis=1)
    denominator[0] = 1
    # Stream matrix columns to keep even the larger torus within a small working set.
    c = np.zeros((6, 6))
    for direction in range(4):
        rows = np.zeros((len(k), 6), complex)
        for face, (i, j, off, sign) in enumerate(FACES):
            coeff = -p[:, j] if direction == i else p[:, i] if direction == j else 0
            phase = 1 if off is None else np.exp(1j*k[:, off])
            rows[:, face] = sign*phase*coeff
        assert abs(rows.sum(axis=1)).max() < 3e-14
        c += (rows.conj().T @ (rows/denominator[:, None])).real/len(k)
    return c


def transverse(order):
    z, w = leggauss(order)
    k = (1+z)*pi/2
    q = 4*np.sin(k/2)**2
    xy = q[:, None, None]+q[None, :, None]
    omega = 2*np.arcsinh(np.sqrt(xy+q[None, None, :])/2)
    return np.sum(w[:, None, None]*w[None, :, None]*w[None, None, :]*
                  xy*np.exp(-omega)/(16*np.sinh(omega)))


def check_covariance():
    sign = np.sign(np.arange(6)[None, :]-np.arange(6)[:, None])
    opp = np.roll(np.eye(6), 3, axis=1)
    odd = (np.eye(6)-opp)/2
    even = (np.eye(6)+opp)/2-np.ones((6, 6))/6
    k = transverse(68)
    np.testing.assert_allclose(k, transverse(106), atol=2e-10)
    a, b = 0.5+k, 1.5*(0.5-k)
    exact = 6*a*a+2*b*b/3
    errs = []
    for side in (5, 9, 16, 22):
        c = face_cov(side)
        assert np.linalg.matrix_rank(c, tol=1e-10) == 5
        af, bf = np.trace(c @ odd)/3, np.trace(c @ even)/2
        np.testing.assert_allclose(c, af*odd+bf*even, atol=3e-14)
        observed = np.trace(sign.T @ c @ sign @ c)
        np.testing.assert_allclose(observed, 6*af*af+2*bf*bf/3)
        errs.append(abs(observed-exact))
    assert all(np.diff(errs) < 0) and errs[-1] < 1e-4
    print("transverse covariance, cube ratio, SU3 signed cubic", k, exact, -144*exact/4)
    print("periodic projection errors", errs)
    return a*odd+b*even


PATHS = [(0, 1, 2), (1, 0, 2), (1, 2, 0), (2, 1, 0), (2, 0, 1), (0, 2, 1)]


def cube_product():
    rng = np.random.default_rng(908)
    t = basis(3)
    edge = {(x, a): np.einsum("k,kij->ij", rng.normal(size=8), t)
            for x in product((0, 1), repeat=3) for a in range(3) if x[a] == 0}
    def tangent(u):
        v = (u-u.conj().T)/2
        return v-np.trace(v)*np.eye(3)/3
    ratios, errors = [], []
    for scale in (0.05, 0.025, 0.0125, 0.00625, 0.003125, 0.0015625):
        links = {key: expm(scale*a) for key, a in edge.items()}
        walks = []
        for path in PATHS:
            x, w = [0, 0, 0], np.eye(3)
            for a in path:
                w = w @ links[tuple(x), a]
                x[a] = 1
            walks.append(w)
        hol = [w @ walks[(i+1)%6].conj().T for i, w in enumerate(walks)]
        np.testing.assert_allclose(np.linalg.multi_dot(hol), np.eye(3), atol=2e-13)
        f = [tangent(u)/scale for u in hol]
        d = sum(f)/scale
        b = sum(comm(f[i], f[j]) for i in range(6) for j in range(i+1, 6))
        norm = np.vdot(b, b).real
        errors.append(np.linalg.norm(d+b/2)/np.sqrt(norm))
        third = sum(np.vdot(comm(f[i], f[j]), f[k]).real
                    for i in range(6) for j in range(i+1, 6) for k in range(j+1, 6))
        np.testing.assert_allclose(third/scale, np.vdot(b, d).real, rtol=2e-12)
        ratios.append(third/(scale*norm))
        u, v = hol[:2]
        wilson = np.linalg.norm(u @ v @ u.conj().T @ v.conj().T-np.eye(3))**2
        np.testing.assert_allclose(wilson, np.linalg.norm(comm(u-np.eye(3), v-np.eye(3)))**2, atol=2e-14)
    assert all(np.diff(errors) < 0) and errors[-1] < 0.04
    assert abs(ratios[-1]+0.5) < 0.015
    print("group-word relative second-order errors", errors, "signed cubic ratios", ratios)


if __name__ == "__main__":
    compact_groups()
    check_covariance()
    cube_product()
