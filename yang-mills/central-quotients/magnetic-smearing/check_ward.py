"""Conditional Haar variation of moving rooted faces in a four-dimensional Wilson box."""
from itertools import product
from pathlib import Path
import sys
import numpy as np
from numpy.polynomial.legendre import leggauss

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tangent-curvature"))
from checks import multiply

ONE = np.array([1., 0., 0., 0.])
CONJ = np.array([1., -1., -1., -1.])
ORIGIN = (0, 0, 0, 0)


def walk(x, axis, delta):
    out = list(x)
    out[axis] = (x[axis]+delta+1) % 3 - 1
    return tuple(out)


def face(x, i, j):
    return [(x, i, 1), (walk(x, i, 1), j, 1), (walk(x, j, 1), i, -1), (x, j, -1)]


def path(x):
    steps, at = [], ORIGIN
    for axis, value in enumerate(x):
        if value:
            end = walk(at, axis, value)
            steps.append((at if value > 0 else end, axis, value))
            at = end
    return steps


def check(sign, order, phases):
    rng = np.random.default_rng(142)
    beta = 1.7
    fixed = {}
    for x in product((-1, 0, 1), repeat=4):
        for axis in range(4):
            q = rng.normal(size=4)
            fixed[x, axis] = q / np.linalg.norm(q)
    at = ORIGIN if sign == 1 else (-1, 0, 0, 0)
    nodes, weights = leggauss(order)
    a = 2*np.pi*np.arange(phases)/phases
    u, v, w = np.meshgrid((nodes+1)/2, a, a, indexing="ij")
    q = np.stack((np.sqrt(u)*np.cos(v), np.sqrt(u)*np.sin(v),
                  np.sqrt(1-u)*np.cos(w), np.sqrt(1-u)*np.sin(w)), axis=-1)
    gen = np.array([0., 0.48, 0.64, 0.6])
    dq = multiply(gen, q) if sign == 1 else multiply(q, gen)
    def word(steps):
        val, derivative = ONE, np.zeros(4)
        for site, axis, orientation in steps:
            varied = (site, axis) == (at, 0)
            link = q if varied else fixed[site, axis]
            dl = dq if varied else np.zeros(4)
            if orientation < 0:
                link, dl = link*CONJ, dl*CONJ
            derivative = multiply(derivative, link)+multiply(val, dl)
            val = multiply(val, link)
        return val, derivative

    action = np.zeros_like(u)
    score = np.zeros_like(u)
    for axis in (1, 2, 3):
        for base in [at, walk(at, axis, -1)]:
            hol, dh = word(face(base, 0, axis))
            action += hol[..., 0]
            score -= dh[..., 0]
    haar = (weights/2)[:, None, None]
    prob = haar*np.exp(beta*(action-action.max()))
    prob /= prob.sum()

    angle, direct, frame = (np.zeros_like(u) for _ in range(3))
    probes = [(at, 0, 1), (walk(at, 2, -1), 0, 2),
              ((sign, 0, 0, 0), 1, 2), ((sign, 1, 0, 0), 2, 3)]
    for site, i, j in probes:
        color = rng.normal(size=3)/2
        p, dp = word(path(site))
        hol, dh = word(face(site, i, j))
        rooted = multiply(multiply(p, hol), p*CONJ)
        inside = multiply(multiply(p, dh), p*CONJ)
        outside = multiply(multiply(dp, hol), p*CONJ)+multiply(multiply(p, hol), dp*CONJ)
        angle += np.sqrt(beta)*(rooted[..., 1:] @ color)
        direct += np.sqrt(beta)*(inside[..., 1:] @ color)
        frame += np.sqrt(beta)*(outside[..., 1:] @ color)
    left = np.sum(prob*np.cos(angle)*(direct+frame))
    right = beta*np.sum(prob*np.sin(angle)*score)
    dropped = np.sum(prob*np.cos(angle)*direct)
    return np.array([left, right, dropped])


if __name__ == "__main__":
    for orientation in (1, -1):
        lower = check(orientation, 18, 28)
        high = check(orientation, 25, 40)
        np.testing.assert_allclose(lower, high, atol=4e-8, rtol=0)
        assert abs(high[0]-high[1]) < 2e-9
        assert abs(high[0]-high[2]) > 1e-3
        print("orientation, full derivative, Wilson score, frozen frame", orientation, *high)
