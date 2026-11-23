"""Check the local differential identities and the adjoint spectral band on a rotor."""
from itertools import combinations, product

import numpy as np
from scipy.linalg import eigh_tridiagonal


def multiply(a, b):
    return np.r_[a[0]*b[0] - a[1:] @ b[1:],
                 a[0]*b[1:] + b[0]*a[1:] + np.cross(a[1:], b[1:])]


def inverse(a):
    return a * np.array([1., -1., -1., -1.])


def shifted(p, i, side):
    return tuple((v+int(j == i)) % side for j, v in enumerate(p))


def square(p, i, j, side):
    return (((p, i), 1), ((shifted(p, i, side), j), 1),
            ((shifted(p, j, side), i), -1), ((p, j), -1))


def value_and_gradient(face, links, selected):
    factors = [links[e] if sign == 1 else inverse(links[e]) for e, sign in face]
    prefix = [np.array([1., 0., 0., 0.])]
    for u in factors:
        prefix.append(multiply(prefix[-1], u))
    postfix = np.array([1., 0., 0., 0.])
    grad = np.zeros((len(selected), 3))
    for j in reversed(range(4)):
        e, sign = face[j]
        if e in selected:
            # Scalar part is invariant under cyclic permutation. A left
            # variation on an inverted link inserts the generator on the right.
            cyclic = multiply(multiply(factors[j], postfix), prefix[j])
            if sign == -1:
                cyclic = multiply(multiply(postfix, prefix[j]), factors[j])
            grad[selected.index(e)] = -sign * cyclic[1:]
        postfix = multiply(factors[j], postfix)
    return prefix[-1][0], grad


def step(links, edges, tangent, delta):
    updated = links.copy()
    for e, v in zip(edges, tangent):
        n = np.linalg.norm(v)
        shift = np.r_[np.cos(delta*n), delta*np.sinc(delta*n/np.pi)*v]
        updated[e] = multiply(shift, links[e])
    return updated


def faces_test(side, rng):
    origin = (0, 0, 0)
    own = square(origin, 0, 1, side)
    edges = [e for e, _ in own]
    all_faces = [square(p, i, j, side) for p in product(range(side), repeat=3)
                 for i, j in combinations(range(3), 2)]
    neighbors = [f for f in all_faces if f != own and any(e in edges for e, _ in f)]
    assert len(neighbors) == 12 and all(sum(e in edges for e, _ in f) == 1 for f in neighbors)
    patch = [own] + neighbors
    keys = sorted({e for f in patch for e, _ in f})
    err = wrong = 0.
    for _ in range(12):
        links = {e: (v := rng.normal(size=4)) / np.linalg.norm(v) for e in keys}
        x, grad = value_and_gradient(own, links, edges)
        S = 1-x*x
        np.testing.assert_allclose(np.sum(grad**2, axis=1), S, atol=1e-12)
        h = 1e-5
        plus, minus = (step(links, edges, grad, a) for a in (h, -h))
        gp = value_and_gradient(own, plus, edges)[1]
        gm = value_and_gradient(own, minus, edges)[1]
        for f in patch:
            y, dy = value_and_gradient(f, links, edges)
            cross = np.sum(dy*grad)
            numerical = (np.sum(gp*value_and_gradient(f, plus, edges)[1]) -
                         np.sum(gm*value_and_gradient(f, minus, edges)[1])) / (2*h)
            expected = -32*x*S if f == own else -y*S-4*x*cross
            err = max(err, abs(numerical-expected))
            if f != own:
                wrong = max(wrong, abs(numerical - (-y*S+4*x*cross)))
    assert err < 5e-8 and wrong > 0.05
    print(f"period {side}: 12 single-edge neighbors, max residual {err:.3e}, sign control {wrong:.3f}")


def rotor(size, g):
    n = np.arange(size)
    F = np.diag(np.ones(size-1), 1) + np.diag(np.ones(size-1), -1)
    pos = np.eye(size)
    energy, states = eigh_tridiagonal(n*(n+2)+g, np.full(size-1, -g/2))
    omega = states[:, 0]
    Q = lambda v: states @ ((energy-energy[0]) * (states.T @ v))
    A = F@F-pos
    psi = A@omega - (omega @ A @ omega)*omega
    mass = (states.T @ psi)**2
    E = energy-energy[0]
    m1, m2 = mass @ E, mass @ (E**2)
    J = omega @ ((F/2)@(F/2)) @ (pos - (F/2)@(F/2)) @ omega
    chain_error = np.linalg.norm(Q(psi) - (2*F@Q(F@omega) - 8*(pos-F@F/4)@omega))
    fundamental_first = (states.T @ (F @ omega))**2 @ E
    cross_error = abs(mass.sum()+m1/4 - (4*fundamental_first-fundamental_first**2))
    assert cross_error < 1e-8
    B = min(g, 17*np.sqrt(g)/8+3/16)
    low = 4/(1+np.sqrt(B))**2
    D = min((24+16*np.sqrt(B))**2, (4*np.sqrt(86401)+8)**2)
    K = min(4, 576/(1+np.sqrt(B))**2)
    assert mass.sum() <= K and mass.sum()/m1 <= 144+1e-10
    lower_endpoint = max(low/16, 1/576)
    np.testing.assert_allclose(lower_endpoint, low/(4*K), rtol=1e-12)
    weight = mass[(E >= lower_endpoint) & (E <= 2*D/low)].sum()
    assert low <= m1+1e-10 and m2 <= D and weight+1e-10 >= low**2/(2*D)
    assert abs(m1-64*J) < 1e-8 and chain_error < 1e-8
    if g == 0:
        np.testing.assert_allclose([m1,m2,mass.sum()], [8,64,1],atol=1e-10)
    return np.array([m1,m2,mass.sum(),weight]), chain_error


if __name__ == "__main__":
    rng = np.random.default_rng(271828)
    for side in (3, 4):
        faces_test(side, rng)
    for g in (0, 1, 16, 256, 4096, 65536):
        # The 72-character cutoff misses the product-rule residual at the largest coupling.
        coarse, fine = (120, 160) if g == 65536 else (72, 120)
        a, _ = rotor(coarse, g)
        b, residual = rotor(fine, g)
        np.testing.assert_allclose(a, b, rtol=1e-8, atol=1e-10)
        print(f"rotor g={g}, characters {coarse}/{fine}: M1={b[0]:.8f}, M2={b[1]:.8f}, mass={b[2]:.8f}, chain residual={residual:.2e}")
