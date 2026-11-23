"""Face-word, broad-average, and free single-plaquette spectral controls."""
from fractions import Fraction
from itertools import product
from math import pi
from pathlib import Path
from runpy import run_path

import numpy as np
from numpy.polynomial.legendre import leggauss


def reflection_words():
    words = run_path(str(Path(__file__).resolve().parents[1] / "spatial-packet/strip/check_strip.py"))
    path, invert, reduce = (words[k] for k in ("path", "invert", "reduced"))
    count = 0
    for j, k in product(range(-6, 7), repeat=2):
        if j >= k:
            continue
        midpoint = j+k+1
        for base in (2*k, 2*k+1):
            trunk = [1]*(base-midpoint)
            reflected = [-1]*len(trunk)+[-1, 2, 1, -2]+[1]*len(trunk)
            other = 2*midpoint-base-1
            negative_trunk = [-1]*(midpoint-other)
            positive_word = negative_trunk+[1, 2, -1, -2]+[1]*len(negative_trunk)
            w1, end1 = path((midpoint, 0), reflected)
            w2, end2 = path((midpoint, 0), positive_word)
            assert end1 == end2 == (midpoint, 0)
            assert reduce(w1) == reduce(invert(w2))
            assert 2*j <= other <= 2*j+1
            count += 1
    print(f"{count} individual rooted words reflected to exact inverses")


def convolution(a, b):
    c = [Fraction(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def filter_checks():
    for length in range(2, 25, 2):
        averaging = [Fraction(1, length)]*length
        defect = [-x for x in averaging]
        defect[0] += 1
        primitive = [Fraction(length-1-j, length) for j in range(length-1)]
        assert convolution([1, -1], primitive) == defect
        test = convolution(convolution(defect, defect), defect)
        assert sum(test) == 0
        assert all(sum(Fraction(k)**m*v for k, v in enumerate(test)) == 0 for m in (1, 2))
        assert sum(abs(v) for v in test) <= 8
        third = convolution(convolution(primitive, primitive), primitive)
        assert sum(third) == Fraction(length-1, 2)**3
        assert convolution([1, -3, 3, -1], third) == test
    print("12 even averaging lengths, exact triple differences and primitive mass")


def scaled_cov(n, order):
    # Rescale the three spatial momenta by n before cubature.
    end = min(pi*n, 96.)
    nodes, weights = leggauss(order)
    u, w = (nodes+1)*end/2, weights*end/2
    h = 2*n*np.sin(u/(2*n))
    a, b, c = np.meshgrid(h*h, h*h, h*h, indexing="ij", sparse=True)
    r = np.sqrt(a+b+c)
    amp = (a+b)/(2*r*np.sqrt(1+(r/(2*n))**2))
    exponent = -2*n*np.arcsinh(r/(2*n))
    return np.einsum("i,j,k,ijk->", w, w, w, amp*np.exp(exponent))/pi**3


def spectral_checks():
    values = {}
    for n in (2, 4, 8, 16, 32, 64, 128):
        a, b = scaled_cov(n, 56), scaled_cov(n, 84)
        assert abs(a-b) < 2e-6
        values[n] = 1.5*b*b
    coefficient = 1.5/pi**4
    assert abs(values[128]/coefficient-1) < .001
    ratio = (values[128]/values[64])/256
    assert abs(256*ratio-1) < .002
    print(f"n=128 scaled free action covariance {values[128]:.10f}, limit {coefficient:.10f}")
    print(f"free tilt moment at n=64: {ratio:.9f}, limit {1/256:.9f}")


if __name__ == "__main__":
    reflection_words()
    filter_checks()
    spectral_checks()
