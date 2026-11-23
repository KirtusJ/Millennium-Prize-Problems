"""Numerically differentiate the full periodic plaquette map in quaternion angles."""
from itertools import product

import numpy as np


def multiply(p, q):
    a, b = p[..., :1], p[..., 1:]
    c, d = q[..., :1], q[..., 1:]
    return np.concatenate((a*c-np.sum(b*d, axis=-1, keepdims=True),
                           a*d+c*b+np.cross(b, d)), axis=-1)


def inverse(p):
    return p*np.array([1, -1, -1, -1])


def plaquettes(links):
    rows = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        a, b = links[..., i, :], links[..., j, :]
        rows.append(multiply(multiply(a, np.roll(b, -1, axis=i)),
                             inverse(multiply(b, np.roll(a, -1, axis=j)))))
    return np.concatenate([row.ravel() for row in rows])


def compare(shape, angles):
    links = np.zeros((*shape, 3, 4))
    links[..., 0] = np.cos(angles)
    links[..., 3] = np.sin(angles)
    # Scramble the flat representative by a periodic gauge transformation.
    rng = np.random.default_rng(624)
    g = rng.normal(size=(*shape, 4))
    g /= np.linalg.norm(g, axis=-1, keepdims=True)
    for i in range(3):
        links[..., i, :] = multiply(multiply(g, links[..., i, :]),
                                    inverse(np.roll(g, -1, axis=i)))
    columns = []
    h = 1e-4
    for site in np.ndindex(*links.shape[:-1]):
        original = links[site].copy()
        for k in range(3):
            q = np.zeros(4)
            q[0], q[k+1] = np.cos(h), np.sin(h)
            links[site] = multiply(original, q)
            plus = plaquettes(links)
            links[site] = multiply(original, inverse(q))
            # Each oriented face contains a given link at most once here.
            columns.append((plus-plaquettes(links))/(2*np.sin(h)))
        links[site] = original
    observed = np.linalg.svd(np.array(columns), compute_uv=False)
    expected = []
    for p in product(*(2*np.pi*np.arange(n)/n for n in shape)):
        for charge in (-1, 0, 1):
            value = 2*np.linalg.norm(np.sin(np.asarray(p)/2+charge*angles))
            expected.extend((value, value, 0))
    expected = np.sort(expected)[::-1]
    error = np.max(np.abs(observed-expected))
    assert error < 5e-10
    return error


if __name__ == "__main__":
    for shape in ((2, 2, 2), (3, 2, 2)):
        for angles in (np.zeros(3), np.pi/np.array(shape), np.array([.21, -.13, .33])):
            print(shape, angles, compare(shape, angles))
