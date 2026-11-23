"""Mixed-orientation paths, free clover covariances and four-point controls."""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import pi
from pathlib import Path
from runpy import run_path

import numpy as np
from scipy.integrate import quad
from scipy.special import ive, k1

planes = list(combinations(range(4), 2))
basis = np.eye(4, dtype=int)


def line_words():
    words = run_path(str(Path(__file__).resolve().parents[2] / "spatial-packet/strip/check_strip.py"))
    path, invert, reduced = (words[k] for k in ("path", "invert", "reduced"))
    count = 0
    for (i, j), height, sign in product(planes, range(8), (-1, 1)):
        for axis in (i, j):
            # Reflect about the site plane at the origin, including the sign of
            # each normal link, then compare with the inverse positive-base face.
            face = [i+1, j+1, -i-1, -j-1]
            trunk = ([axis+1] if sign == 1 else [-axis-1])*height
            start = (0, 0, 0, 0)
            reflected_steps = [-s if abs(s) == axis+1 else s for s in trunk+face+[-q for q in trunk[::-1]]]
            a, end = path(start, reflected_steps)
            target = -sign*height-1
            to_base = ([axis+1] if target >= 0 else [-axis-1])*abs(target)
            b, end2 = path(start, to_base+face+[-q for q in to_base[::-1]])
            assert end == end2 == start and reduced(a) == reduced(invert(b))
            count += 1
    print(f"{count} exact reflected positive-base words across all six face types")


def reordered_segments():
    words = run_path(str(Path(__file__).resolve().parents[2] / "spatial-packet/strip/check_strip.py"))
    path, invert, reduce, segments = (words[k] for k in ("path", "invert", "reduced", "segments"))
    origin = (0, 0, 0, 0)
    count = 0
    for base in product((-2, 0, 3), repeat=4):
        for axis, stride in product(range(1, 4), (-4, -1, 1, 5)):
            blocks = segments(base) + [[(axis+1 if stride > 0 else -axis-1)]*abs(stride)]
            for j in range(3, axis, -1):
                prefix, at = path(origin, sum(blocks[:j], []))
                a, b = blocks[j:j+2]
                old, _ = path(origin, sum(blocks, []))
                loop, end = path(at, a+b+[-u for u in a[::-1]]+[-u for u in b[::-1]])
                blocks[j:j+2] = [b, a]
                new, _ = path(origin, sum(blocks, []))
                assert at == end and reduce(old+invert(new)) == reduce(prefix+loop+invert(prefix))
            word, end = path(origin, sum(blocks, []))
            assert reduce(word) == path(origin, sum(segments(end), []))[0]
            count += 1
    print(f"{count} displaced four-dimensional roots checked by rectangular word reduction")


def spectral_check():
    for radius in (.4, 1., 2.6, 5.):
        def integrand(s):
            mass = np.sqrt(s)
            return s**2*mass*k1(mass*radius)/(768*radius)
        integral, error = quad(integrand, 0., np.inf, epsabs=1e-13, epsrel=1e-10)
        np.testing.assert_allclose(integral*radius**8, 1., rtol=3e-10, atol=2e-11)
        assert error*radius**8 < 3e-8
    print("Four positive mass-squared integrals reproduced the normalized power law")


@lru_cache(None)
def green(sorted_abs):
    # Heat kernel of the infinite four-dimensional lattice. Rescaling the
    # time integral keeps its peak away from the quadrature endpoints.
    n = np.array(sorted_abs)
    scale = 1 + n @ n
    def integrand(u):
        t = scale*u/(1-u)
        return np.prod(ive(n, 2*t))*scale/(1-u)**2
    g, err = quad(integrand, 0., 1., epsabs=4e-14, epsrel=1e-11)
    assert err < 2e-12
    return g


def lattice_covariance(displacement):
    def g(x):
        return green(tuple(sorted(abs(i) for i in x)))
    def dd(z, i, j):
        return g(z+basis[i]-basis[j])-g(z+basis[i])-g(z-basis[j])+g(z)
    def offsets(i, j):
        return [a*basis[i]+b*basis[j] for a, b in product((-1, 0), repeat=2)]
    total = 0.
    for i, j in planes:
        for k, l in planes:
            for a, b in product(offsets(i, j), offsets(k, l)):
                z = displacement+a-b
                c = ((dd(z, i, k) if j == l else 0.) -
                     (dd(z, i, l) if j == k else 0.) -
                     (dd(z, j, k) if i == l else 0.) +
                     (dd(z, j, l) if i == k else 0.))
                total += c*c
    return 3*total/32


def lattice_checks():
    directions = np.array([(5, 0, 0, 0), (4, 3, 0, 0), (4, 2, 2, 1)])
    errors = []
    for stride in (1, 2, 4, 8):
        radius = 5*stride
        rows = [lattice_covariance(stride*v)*radius**8*pi**4/9 for v in directions]
        errors.append(max(abs(x-1) for x in rows))
        print(f"radius {radius:2d} normalized covariance", *(f"{v:.8f}" for v in rows))
    assert errors[-1] < .012 and all(b < a for a, b in zip(errors, errors[1:]))


def exterior_matrix(z):
    d = z/np.linalg.norm(z)
    rot = np.eye(4)-2*np.outer(d, d)
    return np.array([[rot[i,k]*rot[j,l]-rot[i,l]*rot[j,k] for k,l in planes] for i,j in planes])


def cross(a, b):
    return exterior_matrix(a-b)/np.linalg.norm(a-b)**4


def fourth(vertices):
    s = 0.
    for i, j, k in permutations((1, 2, 3)):
        if i > k:
            continue
        a, b, c, d = vertices[[0, i, j, k]]
        s += np.trace(cross(a,b) @ cross(b,c) @ cross(c,d) @ cross(d,a))/27
    return s


def clock_checks():
    states = ((Fraction(1, 3), Fraction(3, 4), 2),
              (Fraction(1, 2), Fraction(1, 2), 5))
    count = 0
    for low, high, weight in states:
        def moment(n):
            return low**(n-2) + weight*high**(n-2)
        for r in range(3, 10):
            ratio = moment(2*r)/moment(r)
            for n in range(2*r, 4*r+1):
                # Raise to r to keep comparisons for nonmultiple lags exact.
                assert (moment(n)/moment(r))**r >= ratio**(n-r)
                assert moment(n) <= moment(2*r)
                count += 1
    print(f"{count} exact buffered clock bounds for mixed and point spectra")


def geometry_checks():
    rng = np.random.default_rng(55419)
    max_odd = 0.
    for _ in range(128):
        x = rng.normal(size=(4, 4))
        a, b, c = x[:3]
        z = (a-b, b-c, c-a)
        mats = [exterior_matrix(v) for v in z]
        max_odd = max(max_odd, abs(np.trace(mats[0]@mats[1]@mats[2])))
        rot, _ = np.linalg.qr(rng.normal(size=(4, 4)))
        np.testing.assert_allclose(fourth(x), fourth(x@rot), rtol=2e-11, atol=1e-13)
    assert max_odd < 2e-14
    x = np.outer(np.array([0., 1., 2., 3.]), basis[0])
    denom = sum(np.prod([abs(x[a,0]-x[b,0])**-4 for a, b in zip(p,p[1:]+p[:1])])
                for p in [(0,1,2,3), (0,1,3,2), (0,2,1,3)])
    np.testing.assert_allclose(fourth(x)/denom, 2/9)
    # Omitting one face orientation spoils the trace cancellation.
    projector = np.diag([1., 1., 1., 1., 1., 0.])
    r = exterior_matrix(x[1]-x[0])
    assert abs(np.trace((projector@r)@(projector@r)@(projector@r))) == 1
    print(f"128 rotated quadrilaterals, largest absolute odd trace {max_odd:.2g}, collinear ratio {fourth(x)/denom:.8f}")


if __name__ == "__main__":
    line_words()
    reordered_segments()
    spectral_check()
    lattice_checks()
    geometry_checks()
    clock_checks()
