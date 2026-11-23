"""Independent spatial, nonabelian and spectral controls for the locality note."""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, product
from math import comb, exp, pi, sqrt
import numpy as np


def face(x, i, j, side):
    def step(axis):
        return tuple((z + (axis == k)) % side for k, z in enumerate(x))
    return ((x, i, 1), (step(i), j, 1), (step(j), i, -1), (x, j, -1))


def incidence(side):
    faces = [face(x, i, j, side) for x in product(range(side), repeat=3)
             for i, j in combinations(range(3), 2)]
    rows = defaultdict(Counter)
    for boundary in faces:
        edges = [(x, i) for x, i, _ in boundary]
        for e in edges:
            rows[e].update(edges)
    for e, row in rows.items():
        assert sum(row.values()) == 16
        assert sum(w * rows[a][e] for a, w in row.items()) == 28
    origin = ((0, 0, 0), 0)
    hits = Counter({origin: 1})
    for n in range(1, min(4, (side-1)//2)+1):
        nxt = Counter()
        for e, paths in hits.items():
            for a, w in rows[e].items():
                nxt[a] += w*paths
        target = ((0, n, 0), 0)
        assert hits[target] == 0 and nxt[target] == 1
        assert sum(nxt.values()) == 16**n
        hits = nxt
    return len(rows)


def shift(n, j):
    return tuple(a+(i == j) for i, a in enumerate(n))


def rotor_control(distance, electric=False):
    # Exact unrestricted Fourier modes on (S¹)^(distance+1), kappa=lambda=2.
    zero = (0,)*(distance+1)

    @lru_cache(None)
    def hpow(n, k):
        if k == 0:
            return {n: 1}
        result = Counter()
        for m, c in hpow(n, k-1).items():
            result[m] += 2*sum(a*a for a in m)*c
            for e in range(distance):
                for sign in (-1, 1):
                    q = list(m)
                    q[e] += sign
                    q[e+1] -= sign
                    result[tuple(q)] -= c
        return {key: val for key, val in result.items() if val}

    def derivative(n, order):
        out = Counter()
        for k in range(order+1):
            coeff = (-1)**k * comb(order, k)
            for m, a in hpow(n, k).items():
                source = m if electric else shift(m, 0)
                sign = (-1 if m[0] % 2 else 1) if electric else 1
                for j, b in hpow(source, order-k).items():
                    out[j] += sign*coeff*a*b
        return out

    final_order = 2*distance-1 if electric else 2*distance+1
    for order in range(final_order+1):
        if electric:
            out = derivative(zero, order)
            for m in out:
                out[m] *= 2 if m[distance] % 2 else 0
        else:
            out = derivative(shift(zero, distance), order)
            for m, a in derivative(zero, order).items():
                out[shift(m, distance)] -= a
        nonzero = sorted(c for c in out.values() if c)
        if order < final_order:
            assert not nonzero
    assert nonzero
    if distance == 1 and not electric:
        assert nonzero == [-16, -16]
    return order, len(nonzero), sum(abs(c) for c in nonzero)


I = np.eye(2, dtype=complex)
X = [0.5j * np.array(a, dtype=complex) for a in (
    [[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]])]


def loop_value(word, links, deriv=None):
    deriv = deriv or {}
    out = I
    for v, d, sign in word:
        e = v, d
        u = links[e]
        m = u if sign > 0 else u.conj().T
        if e in deriv:
            t = X[deriv[e]]
            m = u @ t if sign > 0 else -t @ u.conj().T
        out = out @ m
    return np.trace(out).real / 2


def cube(angle, gauge=False):
    side = 4
    p, q = (face((0, 0, z), 0, 1, side) for z in (0, 1))
    walls = [face((0, j, 0), 0, 2, side) for j in (0, 1)]
    walls += [face((j, 0, 0), 1, 2, side) for j in (0, 1)]
    links = {(v, d): I for w in [p, q, *walls] for v, d, _ in w}
    diag = np.diag([np.exp(1j*angle), np.exp(-1j*angle)])
    for z in (0, 1):
        links[((0, 0, z), 0)] = diag
    if gauge:
        rng = np.random.default_rng(173)
        at = {}
        for v in product(range(2), repeat=3):
            quaternion = rng.normal(size=4)
            a, b, c, d = quaternion / np.linalg.norm(quaternion)
            at[v] = np.array([[a+1j*b, c+1j*d], [-c+1j*d, a-1j*b]])
        for (v, axis), u in links.copy().items():
            w = tuple(j+(i == axis) for i, j in enumerate(v))
            links[v, axis] = at[v] @ u @ at[w].conj().T
    ep, eq = ({(v, d) for v, d, _ in w} for w in (p, q))
    value = 0.
    for w in walls:
        ew = {(v, d) for v, d, _ in w}
        e, = ep & ew
        a, = eq & ew
        for i, j in product(range(3), repeat=2):
            value -= 4*loop_value(p, links, {e:i})*loop_value(q, links, {a:j})*loop_value(w, links, {e:i, a:j})
    adjoint = value*(8/3)**2*loop_value(p, links)*loop_value(q, links)
    assert abs(value+np.sin(angle)**2) < 1e-12
    return value, adjoint


def time_comparison():
    rng = np.random.default_rng(417)
    v, _ = np.linalg.qr(rng.normal(size=(7, 7)))
    w, _ = np.linalg.qr(rng.normal(size=(7, 7)))
    psi = rng.normal(size=7)
    psi /= np.linalg.norm(psi)
    energies = np.array([0., .001, .01, .1, 1., 10., 1000.])
    other = energies*1.2 + .01
    def op(u, vals):
        return (u * vals) @ u.T
    tested = 0
    for t, s in product([0., .03, 2., -1.], [.001, .2, 1.]):
        eps = np.linalg.norm(op(v,np.exp(-s*energies))-op(w,np.exp(-s*other)), 2)
        actual = np.linalg.norm((op(v,np.exp(-1j*t*energies))-op(w,np.exp(-1j*t*other))) @ psi)
        energy = psi @ op(v,energies) @ psi
        cost = 8*(s+sqrt(abs(t)*s))
        upper = sqrt(cost*energy)+abs(t)*eps/s+sqrt(cost*(energy+eps/s))
        assert actual <= upper+1e-12
        tested += 1
    # Single high-energy level at a fixed physical time defeats unweighted real-time norm transfer.
    assert abs(np.exp(-1j*100)-np.exp(-1j*(100+pi))) > 1.99999
    assert abs(exp(-100)-exp(-(100+pi))) < 4e-44
    return tested


if __name__ == "__main__":
    for side in (3, 5, 9):
        print("torus", side, "verified rows", incidence(side))
    for distance in (1, 2, 3):
        print("rotor distance, first order, modes, coefficient norm₁", distance, *rotor_control(distance))
    for distance in (1, 2, 3):
        print("electric distance, first order, modes, coefficient norm₁", distance, *rotor_control(distance, electric=True))
    for angle in (0., pi/4, pi/2):
        before = cube(angle)
        assert np.allclose(before, cube(angle, gauge=True), rtol=0, atol=1e-12)
        print("cube angle, fundamental and normalized adjoint third derivatives / i", angle, *before)
    print("real-time comparisons", time_comparison())
