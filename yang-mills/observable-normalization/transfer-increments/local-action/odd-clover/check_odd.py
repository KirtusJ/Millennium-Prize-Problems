"""Wilson corner redistribution, a mixed link derivative, and free lattice contacts."""
from itertools import combinations, product

import numpy as np


PLANES = list(combinations(range(4), 2))
PAIR_SIGNS = (1, -1, 1)
AXES = tuple(range(4))


def conjugate(q):
    return q * np.array([1, -1, -1, -1])


def multiply(p, q):
    a, b = p[..., :1], p[..., 1:]
    c, d = q[..., :1], q[..., 1:]
    return np.concatenate((a*c - (b*d).sum(-1, keepdims=True),
                           a*d + c*b + np.cross(b, d)), axis=-1)


def charges(links):
    """Compute the two densities with beta=1 on a four-torus."""
    faces = {}
    for i, j in PLANES:
        for s, t in product((-1, 1), repeat=2):
            offset = [0]*4
            word = np.array([1., 0., 0., 0.])
            for axis, sign in ((i, s), (j, t), (i, -s), (j, -t)):
                offset[axis] += min(0, sign)
                link = np.roll(links[axis], tuple(-v for v in offset), AXES)
                word = multiply(word, link if sign == 1 else conjugate(link))
                offset[axis] += max(0, sign)
            faces[i, j, s, t] = word[..., 1:]
    site = np.zeros(links.shape[1:-1])
    cell = np.zeros_like(site)
    for signs in product((-1, 1), repeat=4):
        corner = tuple((1-s)//2 for s in signs)
        vectors = [faces[i, j, signs[i], signs[j]] for i, j in PLANES]
        w = sum(a*(vectors[i]*vectors[5-i]).sum(-1)
                for i, a in enumerate(PAIR_SIGNS)) * np.prod(signs)/16
        site += w
        cell += np.roll(w, tuple(-c for c in corner), AXES)
    return site, cell


def reflect(field, axis):
    return np.take(field, (-np.arange(field.shape[axis])) % field.shape[axis], axis=axis)


def geometric_checks():
    rng = np.random.default_rng(19431)
    links = rng.normal(size=(4, 5, 5, 5, 5, 4))
    links /= np.linalg.norm(links, axis=-1, keepdims=True)
    site, cell = charges(links)
    np.testing.assert_allclose(site.sum(), cell.sum(), atol=1e-12)
    for axis in AXES:
        reflected = np.stack([reflect(u, axis) for u in links])
        reflected[axis] = conjugate(np.roll(reflected[axis], -1, axis))
        p, d = charges(reflected)
        np.testing.assert_allclose(p, -reflect(site, axis), atol=2e-15)
        np.testing.assert_allclose(d, -np.roll(reflect(cell, axis), -1, axis), atol=2e-15)
    return site.sum()


def mixed_charge(t):
    coeff = 0.
    for signs in product((-1, 1), repeat=3):
        u = np.zeros((4, 5, 5, 5, 5, 4))
        u[..., 0] = 1
        for k, (axis, origin) in enumerate(((0, (0, 0, 0, 0)), (1, (0, 0, 0, 0)),
                                             (3, (0, 0, 1, 0)))):
            spin = u[(axis,) + origin]
            spin[0], spin[k+1] = np.cos(t), signs[k]*np.sin(t)
        p, _ = charges(u)
        coeff += np.prod(signs)*p.sum() / (2*t)**3
    return coeff


def gaussian_checks(n):
    freq = 2*np.pi*np.fft.fftfreq(n)
    p = np.meshgrid(*([freq]*4), indexing='ij', sparse=True)
    sine = [np.sin(x) for x in p]
    avg = [(1+np.exp(-1j*x))/2 for x in p]
    hat2 = sum(4*np.sin(x/2)**2 for x in p)
    hat2[(0,)*4] = np.inf
    legs = [{j: 1j*sine[i]*avg[j], i: -1j*sine[j]*avg[i]} for i, j in PLANES]
    cross = np.zeros((6, 6) + (n,)*4)
    for a, f in enumerate(legs):
        for b, g in enumerate(legs):
            common = f.keys() & g.keys()
            if common:
                symbol = sum(f[k]*g[k].conj() for k in common)/hat2
                val = np.fft.ifftn(symbol)
                assert np.max(abs(val.imag)) < 1e-14
                cross[a,b] = val.real
    signs = (1, -1, 1, 1, -1, 1)
    kernel = sum(1.5*s*t*cross[a,b]*cross[5-a,5-b]
                 for a,s in enumerate(signs) for b,t in enumerate(signs))
    origin = (0,)*4
    assert kernel[origin] > 0 and abs(kernel.sum()) < 1e-14
    assert all(kernel[(j,0,0,0)] < 0 for j in range(2, n//2+1))
    z = np.meshgrid(*([abs(np.fft.fftfreq(n)*n)]*4), indexing='ij', sparse=True)
    surface = -(sum(z)*kernel).sum()
    assert surface > 0 and np.fft.fftn(kernel)[1,0,0,0].real > 0
    even_covariance = 1.5*np.einsum('ab...,ab...->...', cross, cross)
    assert even_covariance.sum() > 1e-3  # removing the star changes the zero mode
    return kernel[origin], kernel.sum(), surface


if __name__ == '__main__':
    print('Random periodic total', geometric_checks())
    for t in (0.06, 0.03, 0.015):
        v = mixed_charge(t)
        print('Mixed three-link difference', t, v)
        np.testing.assert_allclose(v, -(np.sin(t)/t)**3/16, atol=1e-13, rtol=1e-12)
    for n in (12, 18, 24):
        print('Free torus: side, contact, sum, surface', n, *gaussian_checks(n))
