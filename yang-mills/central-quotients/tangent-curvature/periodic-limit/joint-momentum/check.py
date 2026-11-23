"""Independent controls for spatial parallel transport and momentum unfolding."""
from functools import lru_cache
from itertools import product
from math import comb, factorial, pi

import numpy as np


def quaternion(a, b):
    return np.r_[a[0]*b[0] - a[1:] @ b[1:],
                 a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:], b[1:])]


def ordered_path(displacement):
    return [int(np.sign(n))*(i+1) for i, n in enumerate(displacement)
            for _ in range(abs(n))]


def path_control():
    rng = np.random.default_rng(71933)

    @lru_cache(None)
    def edge(position, axis):
        q = rng.standard_normal(4)
        return q/np.linalg.norm(q)

    def holonomy(steps):
        h = np.array([1., 0., 0., 0.])
        position = [0]*3
        for step in steps:
            i = abs(step)-1
            if step < 0:
                position[i] -= 1
            u = edge(tuple(position), i)
            if step < 0:
                u = u*np.array([1., -1., -1., -1.])
            else:
                position[i] += 1
            h = quaternion(h, u)
        return h

    first = changed = 0
    for _ in range(160):
        z, v = rng.integers(-3, 4, (2, 3))
        if _ % 4 == 0:
            z[1:] = 0
        word = ordered_path(z)+ordered_path(v)
        initial = holonomy(word)
        area = sum(abs(z[i]*v[j]) for i in range(3) for j in range(i))
        total_error = 0.
        swaps = 0
        for i in range(1, len(word)):
            j = i
            while j and abs(word[j-1]) > abs(word[j]):
                before = holonomy(word)
                word[j-1], word[j] = word[j], word[j-1]
                total_error += np.linalg.norm(before-holonomy(word))
                swaps += 1
                j -= 1
        direct = holonomy(ordered_path(z+v))
        np.testing.assert_allclose(holonomy(word), direct, atol=1e-13)
        error = np.linalg.norm(initial-direct)
        assert swaps == area and error <= total_error+1e-12
        if np.all(z[1:] == 0):
            assert error < 1e-13
            first += 1
        if area and error > .1:
            changed += 1
    assert first >= 40 and changed >= 85
    print(f"160 signed path pairs; {first} first-axis identities, {changed} off-axis changes above 0.1")


def spline(t):
    """Centered eightfold convolution of the uniform density on [-1/2,1/2]."""
    if abs(t) >= 4:
        return 0.
    return sum((-1)**j*comb(8, j)*max(0, t+4-j)**7
               for j in range(9))/factorial(7)


def fourier_control():
    # Fourier transform of the centered spline is sinc(y/2)^8.
    positions = np.array([.4, 2*pi+.4, -2*pi+.4, 0., 2.3])
    shift = .25
    actual = np.array([spline(p-shift) for p in positions])
    for radius in (3, 5, 11):
        z = np.arange(-80*radius, 80*radius+1)
        y = z/radius
        coeff = np.sinc(y/(2*pi))**8/(2*pi*radius)
        phase = np.exp(1j*np.outer(positions-shift, y))
        approx = (phase @ coeff).real
        np.testing.assert_allclose(approx, actual, rtol=0, atol=2e-11)
        # The periodized bump has no extra copies inside its representative cube.
        # Keeping only stride-R offsets instead identifies P and P+2π.
        mask = z % radius == 0
        coarse = (phase[:, mask] @ (radius*coeff[mask])).real
        assert abs(coarse[0]-coarse[1]) < 1e-12
        assert abs(approx[0]-approx[1]) > .4
        # Independent signs and offsets in three directions use the product test.
        exact_3d = np.array([actual[i]*actual[j]*actual[k]
                             for i, j, k in product(range(5), repeat=3)])
        approx_3d = np.einsum("i,j,k->ijk", approx, approx, approx).ravel()
        np.testing.assert_allclose(approx_3d, exact_3d, rtol=0, atol=3e-11)
    print("375 three-dimensional periodization controls; stride-only sampling aliases P and P+2π")


if __name__ == "__main__":
    path_control()
    fourier_control()
