"""Check boundary corner weights and the four-axis window inequalities."""
from itertools import product
from math import cos, pi

import numpy as np


def boundary_checks():
    corners = np.array(list(product((0, 1), repeat=4)))
    tested = 0
    for n in (2, 3, 4, 7):
        totals = np.zeros(len(corners), dtype=int)
        for y in product(range(-1, n), repeat=4):
            point = np.array(y)
            shifted = point + corners
            weights = (np.all((shifted >= 0) & (shifted < n), axis=1).astype(int)
                       - int(all(0 <= a < n for a in y)))
            totals += weights
            for axis in range(4):
                if 0 <= y[axis] <= n - 2:
                    toggled = np.arange(16) ^ (1 << (3 - axis))
                    assert np.array_equal(weights, weights[toggled])
                    tested += 16
        assert np.all(totals == 0)
    return tested


def corner_terms(links, lower):
    side = links.shape[1]
    terms = []
    for corner in product((0, 1), repeat=4):
        signs = 1 - 2 * np.array(corner)
        fields = []
        for i, j in ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)):
            x = np.array(lower) + corner
            word = np.eye(2, dtype=complex)
            for axis, step in ((i, signs[i]), (j, signs[j]),
                               (i, -signs[i]), (j, -signs[j])):
                if step < 0:
                    x[axis] -= 1
                link = links[(axis,) + tuple(x % side)]
                word = word @ (link if step > 0 else link.conj().T)
                if step > 0:
                    x[axis] += 1
            fields.append((word - word.conj().T) / (2j))
        charge = sum(sign * np.trace(fields[i] @ fields[5-i]).real / 2
                     for i, sign in enumerate((1, -1, 1)))
        terms.append(charge * np.prod(signs) / 16)
    return np.array(terms)


def reflection_checks():
    rng = np.random.default_rng(91427)
    side = 5
    q = rng.normal(size=(4, side, side, side, side, 4))
    q /= np.linalg.norm(q, axis=-1, keepdims=True)
    links = np.empty(q.shape[:-1] + (2, 2), dtype=complex)
    links[..., 0, 0] = q[..., 0] + 1j*q[..., 1]
    links[..., 0, 1] = q[..., 2] + 1j*q[..., 3]
    links[..., 1, 0] = -links[..., 0, 1].conj()
    links[..., 1, 1] = links[..., 0, 0].conj()
    lower = np.array([1, 0, 3, 2])
    original = corner_terms(links, lower)
    for axis in range(4):
        reflected = np.take(links, -np.arange(side) % side, axis=axis+1)
        reflected[axis] = np.roll(reflected[axis], -1, axis=axis).conj().swapaxes(-2, -1)
        target = lower.copy()
        target[axis] = -lower[axis] - 1
        values = corner_terms(reflected, target)
        toggle = np.arange(16) ^ (1 << (3-axis))
        np.testing.assert_allclose(values, -original[toggle], rtol=0, atol=2e-15)
        assert np.max(abs(values + original)) > .01
    print("64 reflected noncommuting SU(2) corner terms; omitting the toggle fails")


def window_checks():
    for h in range(2, 65):
        v = np.sin(pi * np.arange(1, h + 1) / (h + 1))
        ac = np.correlate(v, v, 'full')[h - 1:] / np.dot(v, v)
        np.testing.assert_allclose(ac[1], cos(pi / (h + 1)), atol=1e-14)
        lag = np.arange(1, h)
        assert np.all(1 - ac[1:] <= lag**2 * (1 - ac[1]) + 1e-12)
        n = int(np.ceil(np.max(lag / (1 - ac[1:])))) + 1
        assert np.all(1 - lag / n >= ac[1:])
        # Positive spectrum 1 + sum_i 2(1-cos(p_i)); compare all four
        # normalized variances at the same h and at the dominating box n.
        box = 1 + 8 / h
        tapered = 1 + 8 * (1 - ac[1])
        big_box = 1 + 8 / n
        assert big_box <= tapered + 1e-12
        if h in (8, 16, 32, 64):
            print(h, "box excess", box-1, "tapered excess", tapered-1,
                  "h squared times tapered excess", h**2 * (tapered-1))


if __name__ == "__main__":
    print("corner toggles in boundary partition", boundary_checks())
    reflection_checks()
    window_checks()
