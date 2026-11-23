"""Independent signed-incidence, compact Haar, Fourier and threshold controls."""
from itertools import combinations, product
from math import factorial, pi
import numpy as np
from numpy.polynomial.legendre import leggauss


def cubical_complex():
    cells = [[c for c in product((0, 1, 2), repeat=4) if c.count(2) == k]
             for k in range(5)]
    boundaries = []
    for k in range(1, 5):
        low = {cell: i for i, cell in enumerate(cells[k-1])}
        matrix = np.zeros((len(low), len(cells[k])), dtype=int)
        for j, high in enumerate(cells[k]):
            free = [axis for axis in range(4) if high[axis] == 2]
            for offset, axis in enumerate(free):
                for end in (0, 1):
                    face = high[:axis] + (end,) + high[axis+1:]
                    matrix[low[face], j] = (-1)**offset * (2*end-1)
        boundaries.append(matrix)
    ranks = [np.linalg.matrix_rank(m) for m in boundaries]
    assert ranks == [15, 17, 7, 1]
    assert all(not (a @ b).any() for a, b in zip(boundaries, boundaries[1:]))
    print("signed real boundary ranks", ranks, "all successive products zero")


def multiply(a, b):
    scalar = a[..., 0]*b[..., 0] - np.sum(a[..., 1:]*b[..., 1:], axis=-1)
    vector = (a[..., :1]*b[..., 1:] + b[..., :1]*a[..., 1:]
              + np.cross(a[..., 1:], b[..., 1:]))
    return np.concatenate((scalar[..., None], vector), axis=-1)


def ward(n, order):
    # Haar on S^3 in two polar planes. Each face contains the varied link once.
    u, wu = leggauss(order)
    u, wu = (1+u)/2, wu/2
    t = 2*pi*np.arange(n)/n
    h, a, b = np.meshgrid(u, t, t, indexing="ij")
    q = np.stack((np.sqrt(h)*np.cos(a), np.sqrt(h)*np.sin(a),
                  np.sqrt(1-h)*np.cos(b), np.sqrt(1-h)*np.sin(b)), axis=-1)
    gen = np.array([0., 0.6, -0.8, 0.])
    tangent = multiply(gen, q)
    bar = np.array([1., -1., -1., -1.])
    rng = np.random.default_rng(742)
    beta = 3.
    x = np.zeros(q.shape[:-1])
    dx, arg, darg = [np.zeros_like(x) for _ in range(3)]
    reversed_part = np.zeros_like(x)
    for j in range(6):
        endpoints = rng.normal(size=(2, 4))
        left, right = endpoints / np.linalg.norm(endpoints, axis=1)[:, None]
        test = rng.normal(size=3)/3
        sign = 1 if j % 2 == 0 else -1
        face = multiply(multiply(left, q if sign == 1 else q*bar), right)
        df = multiply(multiply(left, tangent if sign == 1 else tangent*bar), right)
        x += face[..., 0]
        dx += df[..., 0]
        if sign < 0:
            reversed_part += df[..., 0]
        arg += np.sqrt(beta)*(face[..., 1:] @ test)
        darg += np.sqrt(beta)*(df[..., 1:] @ test)
    weight = wu[:, None, None]*np.exp(beta*x-(beta*x).max())
    weight /= weight.sum()
    lhs = np.sum(weight*np.cos(arg)*darg)
    rhs = -beta*np.sum(weight*np.sin(arg)*dx)
    wrong = -beta*np.sum(weight*np.sin(arg)*(dx-2*reversed_part))
    return lhs, rhs, wrong


def projector():
    rng = np.random.default_rng(587)
    faces = list(combinations(range(4), 2))
    for k in rng.uniform(-pi, pi, (25, 4)):
        p = np.expm1(1j*k)
        exterior = np.zeros((6, 4), complex)
        for idx, (i, j) in enumerate(faces):
            exterior[idx, j], exterior[idx, i] = p[i], -p[j]
        proj = exterior @ exterior.conj().T / np.vdot(p, p).real
        assert np.allclose(proj @ proj, proj)
        assert np.linalg.matrix_rank(proj) == 3
        for m, (i, j) in enumerate(faces):
            assert abs(proj[m, m]-(abs(p[i])**2+abs(p[j])**2)/np.vdot(p, p)) < 1e-12
    for energy in (0.08, 0.7, 2.2):
        angle = 2*pi*np.arange(4096)/4096
        for n in (0, 1, 5, 13):
            value = np.mean(np.cos(n*angle)/(2*(np.cosh(energy)-np.cos(angle))))
            assert abs(value-np.exp(-n*energy)/(2*np.sinh(energy))) < 1e-12
    print("rank-three complex projections and periodic temporal Green coefficients passed")


def dipole(order):
    nodes, weights = leggauss(order)
    v = (nodes+1)/2
    k, w = pi*v*v, weights*v  # positive octant normalized by pi^3
    square = 4*np.sin(k/2)**2
    s12 = square[:, None, None]+square[None, :, None]
    s3 = square[None, None, :]
    energy = 2*np.arcsinh(np.sqrt(s12+s3)/2)
    measure = w[:, None, None]*w[None, :, None]*w[None, None, :]*s12*s3/(2*np.sinh(energy))
    return np.array([np.sum(measure*np.exp(-n*energy)) for n in (0, 1, 2, 64, 128, 256)])


def low_spectrum():
    values = dipole(92)
    higher = dipole(124)
    np.testing.assert_allclose(values, higher, rtol=3e-8)
    a = 4/pi**2
    scaled = np.array([float(n)**6*c for n, c in zip((64, 128, 256), values[-3:])])
    assert abs(scaled[-1]/a-1) < 7e-4
    assert all(np.diff(abs(scaled-a)) < 0)
    s = 0.37
    d = 1+2*s*values[0]
    connected = d**-3*np.expm1(-1.5*np.log1p(-(2*s*values/d)**2))
    assert abs(connected[0]-((1+4*s*values[0])**-1.5-d**-3)) < 1e-12
    ratio = connected[-1]*256.**12 / (6*s*s*d**-5*a*a)
    assert abs(ratio-1) < 2e-3
    # Integrate the leading two-energy density over the unit simplex directly.
    t, weights = leggauss(20)
    t, weights = (1+t)/2, weights/2
    coef = np.dot(weights, t**5*(1-t)**6/6)/factorial(5)**2
    assert abs(coef*factorial(12)-1) < 1e-12
    print("C(0), C(1), C(2)", values[:3], "n^6 C(n)", scaled, "limit", a)
    print("bounded spectral asymptotic ratio at n=256", ratio, "simplex factor", coef)


if __name__ == "__main__":
    cubical_complex()
    results = [ward(32, 24), ward(48, 36)]
    for left, right, wrong in results:
        assert abs(left-right) < 2e-9
        assert abs(left-wrong) > 0.01
    np.testing.assert_allclose(results[0], results[1], atol=2e-9)
    print("conditional Haar Ward left/right and flipped inverse", results[-1])
    projector()
    low_spectrum()
