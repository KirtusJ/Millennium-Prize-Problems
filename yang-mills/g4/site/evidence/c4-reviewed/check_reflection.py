"""Site-reflection seam controls and an independent single-face Fourier integration."""
from collections import Counter
from itertools import combinations, product
from math import pi, factorial
import numpy as np
from numpy.polynomial.legendre import leggauss


def site_seams():
    # A transverse triangle in Z2, with all longitudinal seam links integrated.
    signs = np.array(list(product((-1, 1), repeat=3)))
    index = {tuple(row): i for i, row in enumerate(signs)}
    perms = np.array([[index[tuple(row*g*np.roll(g, -1))] for row in signs]
                      for g in signs])
    beta = 0.8
    weights = np.exp(beta*np.prod(signs, axis=1))
    proj = np.eye(len(signs))[perms].mean(axis=0)
    kinetic = np.exp(beta*(signs @ signs.T))
    transfer = weights[:, None]**0.5*(kinetic @ proj)*weights[None, :]**0.5
    assert np.linalg.eigvalsh(transfer).min() > -1e-12
    # Fix the base slice and retain the far boundary of each half.
    rng = np.random.default_rng(991)
    f = rng.normal(size=(8, 8))
    half = transfer*f
    even = np.sum(half*half)
    odd = np.sum((half @ transfer)*half)
    # Sum the unsplit triangle-in-time history with a reflection-paired half test.
    direct = sum(transfer[x, y]*transfer[y, z]*transfer[z, x]*f[x, y]*f[x, z]
                 for x, y, z in product(range(8), repeat=3))
    np.testing.assert_allclose(direct, odd)
    assert even > 0 and odd > 0
    assert np.linalg.norm(kinetic @ proj-kinetic) > 1
    print("even and odd site reflection forms", even, odd, "odd direct sum", direct)


def reflected_blocks():
    # Reflect the lower-corner face of each orientation in boxes of mixed parity.
    for lengths in [(3, 3, 3, 4), (5, 7, 11, 12), (16, 19, 18, 32)]:
        for orientation in combinations(range(4), 2):
            copies = [(0, 0, 0, 0)]
            widths = [1]*4
            for axis, length in enumerate(lengths):
                while 4*widths[axis] <= length:
                    width = widths[axis]
                    mirrored = []
                    for vertex in copies:
                        base = list(vertex)
                        base[axis] = 2*width-base[axis]-(axis in orientation)
                        mirrored.append(tuple(base))
                    copies += mirrored
                    widths[axis] *= 2
            assigned = Counter(copies)
            assert max(assigned.values()) <= 4
            assert len(copies) == np.prod(widths)
            assert 256*len(copies) > np.prod(lengths)
    print("all six face orientations in dyadic subblocks of three mixed-parity boxes passed")


def constant_mode():
    # Wrong sign or even tests would fail to rule out an independent offset.
    nodes, weights = np.polynomial.hermite.hermgauss(60)
    weights = weights / np.sqrt(pi)  # N(0,1/2) at nodes
    shift, t = 0.7, 0.9
    negative_pair = -(np.dot(weights, np.sin(t*(nodes+shift))))**2
    exact = -np.exp(-t*t/2)*np.sin(t*shift)**2
    np.testing.assert_allclose(negative_pair, exact)
    assert negative_pair < -0.2
    print("reflected sine pair with forbidden constant offset", negative_pair)


def one_face(order):
    z, w = leggauss(order)
    u = (z+1)/2
    q, weight = 4*np.sin(pi*u*u/2)**2, w*u
    xy = q[:, None, None]+q[None, :, None]
    energy = 2*np.arcsinh(np.sqrt(xy+q[None, None, :])/2)
    density = (weight[:, None, None]*weight[None, :, None]*weight[None, None, :]
               *xy/(2*np.sinh(energy)))
    return np.array([np.sum(density*np.exp(-n*energy)) for n in (0, 1, 64, 128, 256)])


def spectrum():
    c = one_face(108)
    np.testing.assert_allclose(c, one_face(136), rtol=1e-8)
    np.testing.assert_allclose(c[0], 0.5, atol=5e-12)
    coeff = c[-3:]*np.array([64., 128., 256.])**4
    assert abs(coeff[-1]*pi**2-1) < 3e-4
    s, d = 0.37, 1.37
    corr = d**-3*np.expm1(-1.5*np.log1p(-(2*s*c/d)**2))
    ratio = corr[-1]*256.**8/(6*s*s/d**5/pi**4)
    assert abs(ratio-1) < 6e-4
    nodes, w = leggauss(16)
    u = (1+nodes)/2
    simplex = np.dot(w/2, u**3*(1-u)**4/4)/factorial(3)**2
    np.testing.assert_allclose(simplex*factorial(8), 1)
    print("single face C(0), C(1)", c[:2], "n^4 C(n)", coeff, "limit", 1/pi**2)
    print("bounded spectral asymptotic ratio at n=256", ratio, "simplex factor", simplex)


if __name__ == "__main__":
    site_seams()
    reflected_blocks()
    constant_mode()
    spectrum()
