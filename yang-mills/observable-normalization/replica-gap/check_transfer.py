"""Enumerate a periodic 2 x 1 x 1 spatial Z2 Wilson lattice and its time slabs."""
from itertools import combinations
import math

import numpy as np


def wilson_transfer(gamma, sigma):
    vertices = range(2)
    edges = [(v, i) for v in vertices for i in range(3)]

    def step(v, i):
        return v ^ int(i == 0)

    def bit(v, i):
        return 1 << (3*v+i)

    faces = [bit(v, i) ^ bit(step(v, i), j) ^ bit(step(v, j), i) ^ bit(v, j)
             for v in vertices for i, j in combinations(range(3), 2)]
    # Every edge assignment is equiprobable under the reference product Haar law.
    states = range(1 << len(edges))
    size = len(states)
    half = np.array([math.exp(-sigma*sum((s & p).bit_count() % 2 for p in faces))
                     for s in states])
    differences = np.bitwise_xor.outer(list(states), list(states))
    kinetic = np.array([math.exp(gamma*(len(edges)-2*s.bit_count())) for s in states])
    raw = half[:, None] * kinetic[differences] * half[None, :] / size
    gauge_flip = bit(0, 0) ^ bit(1, 0)
    projected = (raw + raw[:, np.arange(size) ^ gauge_flip])/2
    # Set edge (0,0) to +1. Each orbit has exactly two representatives before fixing.
    physical = 2*projected[::2, ::2]
    seam = 0.
    for x in states:
        for y in states:
            for h0 in range(4):
                for h1 in range(4):
                    g0 = gauge_flip if h0 in (1, 2) else 0
                    g1 = gauge_flip if h1 in (1, 2) else 0
                    seam += (half[x]*half[y])**2 * kinetic[x ^ y ^ g0]*kinetic[y ^ x ^ g1]
    seam /= size**2 * 16
    assert math.isclose(seam, np.trace(physical@physical), rel_tol=2e-12)
    assert np.trace(raw@raw) > 1.01*seam
    return physical, np.trace(raw@raw)/seam


def exact_swap(k):
    # Index order is (x,u,y,v). k already incorporates the half-period integration.
    a = k[:, :, None, None]*k[None, None, :, :]
    b = a.transpose(0, 3, 2, 1)
    h = (a-b)**2/(a*a+b*b)
    law = a*a/np.sum(a*a)
    assert np.min(h) >= 0 and np.max(h) <= 1
    return np.sum(law*h), np.sum(law*h*h)


def check():
    transfer, wrong_seam = wilson_transfer(0.83, 0.21)
    eig = np.linalg.eigvalsh(transfer)
    assert eig[0] > 0
    transfer /= eig[-1]
    gap = -math.log(eig[-2]/eig[-1])
    print(f"physical dimension {len(eig)}, gap {gap:.9f}, unprojected/projected Z2 {wrong_seam:.9f}")
    for period in (2, 4, 8, 16):
        slab = np.linalg.matrix_power(transfer, period//2)
        z1 = np.linalg.norm(slab)**2
        z2 = np.linalg.norm(slab@slab)**2
        z4 = np.linalg.norm(np.linalg.matrix_power(slab, 4))**2
        p, q = z2/z1**2, z4/z2**2
        d1, second = exact_swap(slab)
        d2, _ = exact_swap(slab@slab)
        assert abs(d1-(1-p)) < 5e-14 and abs(d2-(1-q)) < 5e-14
        assert d1*d1 <= second <= d1
        lo = p*d2/d1
        hi = min(1., math.sqrt(d2/2)/p)
        actual = math.exp(-period*gap)
        assert lo <= actual <= hi
        print(f"N={period:2d}  deficit={d1:.9g}  gap interval "
              f"[{-math.log(hi)/period:.9f}, {-math.log(lo)/period:.9f}]")
    # A single soft excitation is lost by the infinite-volume entropy density.
    log_p = lambda x: math.log1p(x*x)-2*math.log1p(x)
    for v in (10, 1000, 100000):
        eps = 1/v
        n = 4
        base = log_p(math.exp(-n))
        with_soft = base + log_p(math.exp(-n*eps))/v
        assert abs(with_soft-base) <= math.log(2)/v
        print(f"V={v}  spectator gap={eps:g}  intensive shift={with_soft-base:.9g}")


if __name__ == "__main__":
    check()
