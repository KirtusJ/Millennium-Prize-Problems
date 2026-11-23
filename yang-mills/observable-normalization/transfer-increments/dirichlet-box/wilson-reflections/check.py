"""Check face copies, reflected layers, gauge projection and SU(2) pressure constants."""
from collections import Counter
from itertools import combinations, product
from math import cos, exp, log, pi, sin, sqrt

import numpy as np
from scipy.integrate import quad
from scipy.special import ive


def geometry():
    shape = (4, 6, 8, 10)
    anchors = list(product(*(range(n) for n in shape)))
    for face in combinations(range(4), 2):
        for only_site in (False, True):
            copies = Counter()
            for a in anchors:
                # A site-reflected interval of length one starts at a.
                # A point at its lower vertex reflects to a+1 for odd a.
                corner = tuple((x + int(only_site and j not in face and x%2))%shape[j]
                               for j, x in enumerate(a))
                copies[corner] += 1
            multiplicity = 4 if only_site else 1
            assert set(copies.values()) == {multiplicity}
            assert len(copies)*multiplicity == len(anchors)
    for side in range(4, 66, 2):
        for n in [1, *range(2, side-1, 2)]:
            r = 0 if n == 1 else n//2-1
            reflect = lambda x: (2*r-1-x)%side
            halves = [set((r+i)%side for i in range(side//2)),
                      set((r-1-i)%side for i in range(side//2))]
            for half, length in zip(halves, (2 if n == 1 else n+2, 0 if n == 1 else n-2)):
                part = half.intersection(range(n))
                copied = part.union(reflect(x) for x in part)
                assert len(copied) == length
                if 0 < length < side:
                    assert sum((x-1)%side not in copied for x in copied) == 1
    print('6 plaquette orientations, both reflection rules, and 31 even periods')


def group_table():
    # Signed quaternion basis; multiplication is computed from basis vector
    # cross products, independently of the transfer and gauge projection.
    vals = np.vstack((np.eye(4), -np.eye(4)))
    table = np.empty((8, 8), int)
    for a, (s, *x) in enumerate(vals):
        for b, (t, *y) in enumerate(vals):
            xy = np.r_[s*t-np.dot(x,y), s*np.array(y)+t*np.array(x)+np.cross(x,y)]
            table[a,b] = np.where(np.all(vals == xy, axis=1))[0][0]
    inv = np.array([np.where(row == 0)[0][0] for row in table])
    return vals, table, inv


def bond_kernel():
    vals, mul, inv = group_table()
    real = vals[:,0]
    # beta=log(2) makes the kernel rational up to the Haar factor.
    k = 2.**real[mul[:, inv]]
    k /= k.sum(axis=1, keepdims=True)
    full = np.kron(k,k)
    project = np.zeros((64,64))
    for u,v,a,b in product(range(8), repeat=4):
        up = mul[mul[a,u],inv[b]]
        vp = mul[mul[b,v],inv[a]]
        project[8*u+v,8*up+vp] += 1/64
    np.testing.assert_allclose(project, project.T)
    np.testing.assert_allclose(project@project, project)
    np.testing.assert_allclose(project@full, full@project, atol=1.e-14)
    transfer = project@full@project
    np.testing.assert_allclose(transfer@np.repeat(real,8), 0., atol=1.e-14)
    spectrum = np.linalg.eigvalsh(transfer)
    assert np.sum(spectrum>1.e-12)==5 and spectrum.min()>-1.e-12
    print('two-link Q8 transfer: 5 positive eigenvalues, 59 zero eigenvalues')


def pressure():
    # Scaled Bessel values give the exact SU(2) one-link integral.
    z = lambda b: 2*ive(1,b)/b
    for b in (.01, .3, 1., 2.3, 16.):
        integral = quad(lambda a: 2/pi*sin(a)**2*exp(-b*(1-cos(a))), 0, pi)[0]
        assert abs(z(b)-integral)<1.e-13
    for b in np.geomspace(.001, 1.e5, 101):
        ratio = z(b)/z(6*b)
        assert 1 <= ratio <= 6**1.5
    d = 48+3*log((pi/2)**2.5*2**1.5)-3*log(2*sin(1)**2/(3*pi))
    assert 60.19 < d < 60.2
    print(f'original log tail constant {d:.8f}, endpoint log moment bound {4.5*log(6):.8f}')
    print(f'one-link ratio at beta=100000: {z(1.e5)/z(6.e5):.8f}, limit {6*sqrt(6):.8f}')


if __name__ == '__main__':
    geometry()
    bond_kernel()
    pressure()
