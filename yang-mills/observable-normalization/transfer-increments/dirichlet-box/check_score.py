"""Test the projected Wilson score against central differences in three representations."""
import numpy as np
from scipy.linalg import expm


def inner(a, b):
    return np.vdot(a, b).real / len(a)


def check(group, raw_basis, other_component=None):
    basis = []
    for x in raw_basis:
        for y in basis:
            x = x - inner(x, y)*y
        basis.append(x / np.sqrt(inner(x, x)))

    def projection(a):
        return sum(inner(x, a)*x for x in basis)

    n = len(basis[0])
    identity = np.eye(n)
    rng = np.random.default_rng(612)
    beta = 13.

    def action(u):
        return beta*(1-np.trace(u).real/n)

    def score(u):
        return np.sqrt(beta)*projection(u-identity)

    for i in range(24):
        z = sum(a*x for a, x in zip(rng.normal(size=len(basis)), basis))
        u = expm(z)
        if other_component is not None and i%2:
            u = other_component @ u
        w = expm(sum(a*x for a, x in zip(rng.normal(size=len(basis)), basis)))
        for x in basis:
            dt = 1.e-5
            e = expm(dt*x/np.sqrt(beta))
            diff = (action(e@u)-action(e.conj().T@u))/(2*dt)
            np.testing.assert_allclose(diff, inner(x, score(u)), atol=2.e-9)
        remainder = u-identity-projection(u-identity)
        np.testing.assert_allclose(inner(score(u), score(u))+beta*inner(remainder, remainder),
                                   2*action(u), atol=1.e-13)
        np.testing.assert_allclose(score(u.conj().T), -score(u), atol=1.e-13)
        np.testing.assert_allclose(score(w@u@w.conj().T), w@score(u)@w.conj().T, atol=1.e-13)
    print(f'{group}: 24 samples, {24*len(basis)} directional derivatives')


if __name__ == '__main__':
    m = np.eye(3)
    su3 = [1j*np.diag([1,-1,0]), 1j*np.diag([1,1,-2])]
    for i, j in [(0,1),(0,2),(1,2)]:
        e = np.outer(m[i], m[j])
        su3.extend([e-e.T, 1j*(e+e.T)])
    check('SU(3)', su3)
    check('U(1), weights 1 and 5', [1j*np.diag([1,5])])
    check('O(2)', [np.array([[0.,-1.],[1.,0.]])], np.diag([1.,-1.]))
