"""Continuous Wilson shared-path convolution and a finite moving-vacuum check."""
from math import sqrt

import numpy as np
from scipy.special import ive, roots_chebyu
from scipy.sparse.linalg import LinearOperator, eigsh


def left(z):
    a, b, c, d = z
    return np.array([[a, -b, -c, -d], [b, a, -d, c],
                     [c, d, a, -b], [d, -c, b, a]])


def wilson(g, rng):
    x, weights = roots_chebyu(64)
    weights *= np.exp(g*(x-1))
    weights /= weights.sum()
    q, spin = ive([2, 3], g)/ive(1, g)
    np.testing.assert_allclose(np.dot(x, weights), q, atol=2e-14)
    rotations = np.array([left([t, *(np.sqrt(1-t*t)*axis)])
                          for t in x for axis in np.vstack((np.eye(3), -np.eye(3)))])
    weights = np.repeat(weights/6, 6)
    for _ in range(24):
        a, b = rng.normal(size=(2, 4))
        a /= np.linalg.norm(a)
        b /= np.linalg.norm(b)
        # Product of traces with the common path oriented oppositely.
        a[1:] *= -1
        form = 2*(np.outer(a, b)+np.outer(b, a))
        average = np.eye(4)*np.trace(form)/4
        evolved = form
        for d in (1, 2):
            evolved = np.einsum('n,nji,jk,nkl->il', weights, rotations, evolved,
                                rotations, optimize=True)
            np.testing.assert_allclose(evolved, average+spin**d*(form-average),
                                       rtol=0, atol=2e-13)


def finite(d, lag=3, side=3, q=0.81):
    # A plaquette and a square have three disjoint paths. Compress each
    # path to its product using independent central increments.
    k = 4*side
    points = np.vstack((np.eye(4), -np.eye(4)))
    mult = np.array([[np.argmax(points @ (left(a) @ b)) for b in points]
                     for a in points])
    inv = np.array([np.flatnonzero(mult[i] == 0)[0] for i in range(8)])
    trace = 2*points[:, 0]
    x, a, b = np.indices((8, 8, 8))
    f = trace[mult[x, a]]
    face = trace[mult[b, inv[x]]]
    singlet = trace[mult[a, b]]
    triplet = (2*f*face-singlet)/sqrt(3)
    modes = [singlet, triplet]
    np.testing.assert_allclose([[np.mean(v*w) for w in modes] for v in modes],
                               np.eye(2), atol=1e-14)

    def kinetic(v):
        for axis, count in enumerate([d, k-d, 4-d]):
            retention = q**count
            v = retention*v+(1-retention)*v.mean(axis=axis, keepdims=True)
        return v

    def measured(magnetic):
        weight = np.exp(magnetic*face/4)

        def transfer(v):
            return (weight*kinetic(weight*v.reshape(f.shape))).ravel()

        op = LinearOperator((512, 512), matvec=transfer, dtype=float)
        vals, vecs = eigsh(op, 1, which='LA', v0=np.ones(512), tol=1e-14)
        vacuum = vecs[:, 0].reshape(f.shape)
        density = vacuum**2
        evolved = f-np.sum(density*f)
        for _ in range(lag):
            evolved = transfer(vacuum*evolved).reshape(f.shape)/(vals[0]*vacuum)
        values = []
        for mode in modes:
            residual = mode.copy()
            for value in np.unique(f):
                mask = f == value
                residual[mask] -= np.sum(density[mask]*mode[mask])/density[mask].sum()
            values.append(np.sum(density*residual*evolved))
        return np.array(values)

    eps = 1e-5
    differences = (measured(eps)-measured(-eps))/(2*eps)
    r = q**k
    singlet_rate = q**(k+4-2*d)
    rates = (singlet_rate, singlet_rate*q**d)
    expected = [w*(t-q**4*r)/(1-q**4)*sum(t**j*r**(lag-1-j) for j in range(lag))
                for t, w in zip(rates, (1/4, sqrt(3)/4))]
    np.testing.assert_allclose(differences, expected, atol=1e-9, rtol=0)
    print(f"shared edges {d}: finite difference {differences}, predicted {expected}")


def normalized(g, k, n):
    q, spin = ive([2, 3], g)/ive(1, g)
    r, lam = q**k, q**4
    result = 0
    for d, count in [(1, 4*k-8), (2, 4)]:
        u = q**(k+4-2*d)
        for t, weight in [(u, 1/4), (u*spin**d, sqrt(3)/4)]:
            deriv = weight*(t-lam*r)/(1-lam)*sum(t**j*r**(n-1-j) for j in range(n))
            if t != u:
                assert deriv < 0
            result += count*deriv**2/((1-r**n)*(1-t**n))
    return (1-q)*sqrt(result)


if __name__ == "__main__":
    rng = np.random.default_rng(7106729222)
    for coupling in (0.5, 2, 8, 24):
        wilson(coupling, rng)
    for shared in (1, 2):
        finite(shared)

    k, n = 12, 3
    limit = sqrt(sum(count*d*d/(64*k)*(1/(k+4-2*d)+1/(3*(k+4+2*d/3)))
                     for d, count in ((1, 4*k-8), (2, 4))))
    for g in (1000, 10000, 100000):
        value = normalized(g, k, n)
        print(f"g={g}: scaled full slope {value:.8f}, limit {limit:.8f}")
    assert abs(value-limit) < 3e-5
