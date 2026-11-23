"""Killed Hodge kernel, signed cubic complex, compact-profile transfer and mass checks."""
from itertools import combinations
from math import factorial, pi
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad


def stopped_walk():
    # Radius-three exit and seven steps on a large enough torus to avoid aliasing.
    n, s, radius = 17, 7, 3
    shape = (n,)*4
    center = (n//2,)*4
    delta = np.zeros(shape)
    delta[center] = 1
    live, eta, green = delta.copy(), np.zeros(shape), np.zeros(shape)
    outside = np.zeros(shape, dtype=bool)
    for axis in range(4):
        k = np.arange(n).reshape(tuple(n if a == axis else 1 for a in range(4)))
        outside |= abs(k-center[axis]) >= radius

    def shift_sum(arr):
        return sum(np.roll(arr, d, axis=a) for a in range(4) for d in (-1, 1))

    for _ in range(s):
        green += live/16
        after = 0.5*live+shift_sum(live)/16
        eta += np.where(outside, after, 0)
        live = np.where(outside, 0, after)
    eta += live
    np.testing.assert_allclose(8*green-shift_sum(green), delta-eta, atol=1e-14)
    assert eta.sum() == 1
    missing = np.sum(abs(8*green-shift_sum(green)-delta+live))
    assert missing > 0.01
    hats = [np.expm1(2j*pi*np.arange(n)/n).reshape(tuple(n if a == i else 1 for a in range(4)))
            for i in range(4)]
    g = np.zeros((6,)+shape)
    rng = np.random.default_rng(913)
    g[:, 7:10, 7:10, 7:10, 7:10] = rng.normal(size=(6, 3, 3, 3, 3))
    faces = list(combinations(range(4), 2))
    fg = np.fft.fftn(g, axes=(1, 2, 3, 4))
    gamma = np.fft.fftn(np.fft.ifftshift(green))
    # Incidence matrix of d on one-forms, its adjoint, and d on two-forms.
    one = np.zeros((4,)+shape, complex)
    for j, (a, b) in enumerate(faces):
        one[a] -= hats[b].conj()*fg[j]*gamma
        one[b] += hats[a].conj()*fg[j]*gamma
    dh = np.stack([hats[a]*one[b]-hats[b]*one[a] for a, b in faces])
    coexact = np.zeros_like(dh)
    for ijk in combinations(range(4), 3):
        coeff = np.zeros(shape, complex)
        for pos, a in enumerate(ijk):
            f = tuple(i for i in ijk if i != a)
            coeff += (-1)**pos*hats[a]*fg[faces.index(f)]*gamma
        for pos, a in enumerate(ijk):
            f = tuple(i for i in ijk if i != a)
            coexact[faces.index(f)] += (-1)**pos*hats[a].conj()*coeff
    residual = fg*np.fft.fftn(np.fft.ifftshift(eta))
    max_error = np.max(abs(dh+coexact+residual-fg))
    assert max_error < 3e-13
    print("stopped mass", eta.sum(), "discarded exit error", missing, "Hodge error", max_error)


def profile_hat(p):
    # Three-dimensional profile is a tensor product of fourfold convolutions
    # of this real compact smooth bump, normalized to have integral one.
    x, wx = leggauss(260)
    measure = wx*np.exp(1-1/(1-x*x))
    measure /= measure.sum()
    return (np.cos(np.outer(p, x)) @ measure)**4


def covariance(m, r, order, alias=2):
    z, w = leggauss(order)
    bound = 32 if r is None else pi*r
    p, wp = bound*(1+z)/2, bound*w/(2*pi)
    if r is None:
        q = p
        form = profile_hat(p)
    else:
        q = 2*r*np.sin(p/(2*r))
        form = sum(profile_hat(p+2*pi*r*j) for j in range(-alias, alias+1))
    wprofile = wp*form**2
    mass = wprofile[:, None, None]*wprofile[None, :, None]*wprofile[None, None, :]
    transverse = q[:, None, None]**2+q[None, :, None]**2
    length = np.sqrt(transverse+q[None, None, :]**2)
    if r is None:
        frequency, denom = length, 2*length
    else:
        frequency = 2*r*np.arcsinh(length/(2*r))
        denom = 2*r*np.sinh(frequency/r)
    mu = mass*q[None, None, :]**(2*m)*transverse/denom
    return np.array([np.sum(mu*np.exp(-t*frequency)) for t in (0, 1, 2)])


def signed_reflection():
    # Axis-one line of a center-sampled even plaquette profile with nonzero mass.
    x = np.arange(-250, 250)
    profile = np.maximum(0, 36-(2*x+1)**2)
    j = np.array([11, 22, 33])
    block = sum(2*np.roll(profile, k)-np.roll(profile, 2*k) for k in j)
    reflection = block[::-1]  # array index x becomes -1-x
    difference = 3*profile-block
    flip = block-reflection
    for row in (difference, flip):
        assert row.sum() == 0 and x @ row == 0
        primitive = row.cumsum().cumsum()
        assert np.all(primitive[-10:] == 0)
        assert np.array_equal(primitive-2*np.roll(primitive, 1)+np.roll(primitive, 2), row)
    wrong_base = block-np.roll(reflection, 1)
    assert x @ wrong_base != 0
    print("two compact second primitives; wrong base leaves first moment", x @ wrong_base)


def spacetime_symbol():
    rng = np.random.default_rng(762)
    momenta = rng.normal(size=(40, 4))
    faces = list(combinations(range(4), 2))
    def symbol(p):
        matrix = np.zeros((6, 4), dtype=complex)
        for index, (a, b) in enumerate(faces):
            matrix[index, a], matrix[index, b] = -p[b], p[a]
        return (matrix @ matrix.conj().T)/np.vdot(p, p)
    target = [symbol(p) for p in momenta]
    errors = []
    for r in (4, 8, 16, 32):
        matrices = [symbol(np.expm1(1j*p/r)) for p in momenta]
        for matrix in matrices:
            np.testing.assert_allclose(matrix @ matrix, matrix, atol=1e-13)
            assert np.linalg.matrix_rank(matrix) == 3
        errors.append(max(np.linalg.norm(a-b, ord=2) for a, b in zip(matrices, target)))
    assert all(np.diff(errors) < 0) and errors[-1] < 0.052
    print("four-dimensional curvature multiplier: maximal projection errors", errors)


def profile_test():
    for m in (0, 1, 2):
        exact = covariance(m, None, 106)
        np.testing.assert_allclose(exact, covariance(m, None, 130), rtol=2e-8)
        errors = []
        for r in (2, 4, 8, 16):
            vals = covariance(m, r, 104)
            np.testing.assert_allclose(vals, covariance(m, r, 136, alias=3), rtol=2e-8)
            errors.append(np.max(abs(vals/exact-1)))
        assert all(np.diff(errors) < 0) and errors[-1] < 0.006
        sig = 1/(2*exact[0])
        bounded = 2.**-3*np.expm1(-1.5*np.log1p(-(sig*exact)**2))
        print("order", m, "continuum C(0,1,2)", exact, "relative errors", errors)
        print("bounded mean-normalized t=1,2", bounded[1:]*8,
              "positive-time ratio", bounded[2]/bounded[1])
        assert 0 < bounded[2] < bounded[1] < bounded[0]
        dimension = 2*m+4
        angular = 2*pi*quad(lambda t: t**(2*m)*(1-t*t), -1, 1)[0]
        np.testing.assert_allclose(angular, 8*pi/((2*m+1)*(2*m+3)))
        simplex = quad(lambda x: x**(dimension-1)*(1-x)**dimension/dimension, 0, 1)[0]
        np.testing.assert_allclose(simplex*factorial(2*dimension)/factorial(dimension-1)**2, 1)


if __name__ == "__main__":
    stopped_walk()
    signed_reflection()
    spacetime_symbol()
    profile_test()
