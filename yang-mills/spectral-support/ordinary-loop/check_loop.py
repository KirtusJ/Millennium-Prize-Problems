"""Independent controls for sharp ordinary traces, current kernels, and Wick contractions."""
from functools import lru_cache
from itertools import permutations, product
from math import factorial, pi

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss


def qmul(a, b):
    return np.r_[a[0]*b[0] - a[1:]@b[1:], a[0]*b[1:] + b[0]*a[1:] + np.cross(a[1:], b[1:])]


def inv(q):
    return q * [1, -1, -1, -1]


def group_control():
    rng = np.random.default_rng(49393)

    def haar():
        v = rng.normal(size=4)
        return v/np.linalg.norm(v)

    def test_words(a, b, c):
        direct = (qmul(qmul(a, c), b)[0] - qmul(qmul(a, b), c)[0])/2
        np.testing.assert_allclose(direct, np.linalg.det([a[1:], b[1:], c[1:]]), atol=2e-15)
        np.testing.assert_allclose((qmul(a, inv(b))[0] - qmul(a, b)[0])/2, a[1:]@b[1:], atol=2e-15)
        np.testing.assert_allclose((qmul(a, inv(b))[0] + qmul(a, b)[0])/2, a[0]*b[0], atol=2e-15)
        return direct

    peak = max(abs(test_words(haar(), haar(), haar())) for _ in range(256))
    assert peak > .5
    # Two adjacent plaquettes. Transport the right face using the bottom shared-root path.
    e, f, g, h, k, l, m = [haar() for _ in range(7)]
    def word(*qs):
        q = np.array([1., 0., 0., 0.])
        for x in qs:
            q = qmul(q, x)
        return q
    left = word(e, k, inv(g), inv(h))
    right = word(f, m, inv(l), inv(k))
    perimeter = word(e, f, m, inv(l), inv(g), inv(h))
    np.testing.assert_allclose(word(e, right, inv(e), left), perimeter, atol=2e-15)
    # Six independent vertex gauge rotations on the same rectangle.
    h0, h1, h2, h3, h4, h5 = [haar() for _ in range(6)]
    def change(a, edge, b):
        return word(a, edge, inv(b))
    edges = [change(a,x,b) for a,x,b in [(h0,e,h1),(h1,f,h2),(h2,m,h5),
                                         (h4,l,h5),(h3,g,h4),(h0,h,h3)]]
    rotated = word(*edges[:3], *(inv(x) for x in edges[3:]))
    np.testing.assert_allclose(rotated, word(h0, perimeter, inv(h0)), atol=2e-15)
    print(f"256 signed quaternion words; largest order difference / 2 = {peak:.6f}; adjacent-face and vertex-gauge controls passed")


def wick_control():
    # Direct Isserlis recursion on (vertex, component) slots, including internal edges.
    cov = np.array([[4,1,-2],[1,5,2],[-2,2,6]], dtype=int)
    @lru_cache(None)
    def moment(slots):
        if not slots:
            return 1
        i, color = slots[0]
        return sum(cov[i,j]*moment(slots[1:k]+slots[k+1:]) for k,(j,c) in enumerate(slots)
                   if k and c == color)
    # Expand centered squares using the actual single-vertex variances.
    def centered(vertices):
        result = 0
        for use in product((0,1), repeat=len(vertices)):
            chosen = [v for v, u in zip(vertices,use) if u]
            discard = [v for v, u in zip(vertices,use) if not u]
            for colors in product(range(3), repeat=len(chosen)):
                slots = tuple(x for pair in zip(chosen, colors) for x in (pair,pair))
                result += int(np.prod([-3*cov[v,v] for v in discard], dtype=int))*moment(slots)
        return result/2**len(vertices)
    assert centered([0,1]) == 1.5*cov[0,1]**2
    assert centered([0,1,2]) == 3*cov[0,1]*cov[1,2]*cov[2,0]
    # A general nonsymmetric cross covariance. Each color is independent.
    k = np.array([[1,2,3],[4,-2,1],[0,2,3]],dtype=int)
    def sign(p):
        return (-1)**sum(x>y for i,x in enumerate(p) for y in p[i+1:])
    value = sum(sign(a)*sign(b)*int(np.prod([k[a[i],b[i]] for i in range(3)]))
                for a in permutations(range(3)) for b in permutations(range(3)))
    assert value == 6*round(np.linalg.det(k)) != 0
    print(f"square pair {centered([0,1]):g}, signed triangle {centered([0,1,2]):g}, nonsymmetric cubic {value}")


def square(t, side=1):
    t, side = mp.mpf(t), mp.mpf(side)
    def integral(s):
        return 2*side/s*mp.atan(side/s)-mp.log1p((side/s)**2)
    return (integral(t)-integral(mp.sqrt(t*t+side*side)))/mp.pi**2


def lattice(n, t, order):
    # Infinite spatial lattice, original temporal dispersion, unit physical square.
    # theta = p/n. Bound the finite quadrature box at large physical momenta.
    upper = min(pi*n, 80/t)
    x,w = leggauss(order)
    p = (x+1)*upper/2
    w = w*upper/2
    s = np.sin(p/(2*n))
    end = np.sin(p/2)
    geom = end/s
    square_current = 4*(geom[:,None]**2*end[None,:]**2 + end[:,None]**2*geom[None,:]**2)
    total = 0.
    for sk, wk in zip(s,w):
        omega = 2*np.arcsinh(np.sqrt(s[:,None]**2+s[None,:]**2+sk*sk))
        density = np.exp(-round(n*t)*omega)/(2*np.sinh(omega))
        total += wk * np.einsum('i,ij,j->',w,density*square_current,w)
    return total/(pi*n)**3


def angular_density(energy):
    z,w = leggauss(30)
    phi = np.arange(96)*2*pi/96
    a = energy*np.sqrt(1-z[:,None]**2)
    x,y = a*np.cos(phi), a*np.sin(phi)
    length = 4*(np.sin(y/2)**2*np.sinc(x/(2*pi))**2 + np.sin(x/2)**2*np.sinc(y/(2*pi))**2)
    return energy * (2*pi/length.shape[1]) * np.sum(w[:,None]*length)/(2*(2*pi)**3)


def kernel_control():
    mp.mp.dps = 65
    peer = {1: [.068875,.011153,.002262,.000605], 2: [.264069,.061446,.017644,.006224]}
    for n, values in peer.items():
        readings = [lattice(n,k/n,96) for k in range(1,5)]
        assert max(abs(a-b) for a,b in zip(readings,values)) < 1.1e-6, readings
        print(f"Z4 comparison, {n} by {n} lattice square at lags 1..4:", [round(float(x),8) for x in readings])
    for t in (.5,1,2):
        exact = float(square(t))
        values = [lattice(n,t,96) for n in (8,16,32,64)]
        errors = [float(abs(v/exact-1)) for v in values]
        assert all(a>b for a,b in zip(errors,errors[1:]))
        assert errors[-1] < .0015, errors
        doubled = lattice(64,t,144)
        assert abs(doubled/values[-1]-1)<2e-6
        print(f"t={t:g} exact={exact:.12g} N=8,16,32,64 relative errors={errors}; quadrature refinement {abs(doubled/values[-1]-1):.3g}")
    for r in (.25, 1, 3):
        for t in (.03,.5,2,100):
            integrated = 2*r**2/mp.pi**2*mp.quad(lambda x:(r-x)/((t*t+x*x)*(t*t+x*x+r*r)),[0,r])
            assert abs(integrated/square(t,r)-1)<2e-13
            assert square(2*t,r)/square(t,r) >= mp.mpf(1)/16
    for e in (.1,.01,.001):
        value = angular_density(e)/(e**3/(6*pi**2))
        assert abs(value-1) < e*e/6
    near = mp.mpf('0.000001')
    assert abs(square(near)*mp.pi*near-1) < 2e-5
    assert abs(square(1/near)*mp.pi**2/near**4 -1)<3e-12
    assert abs(square(1/near)**2/square(1/(2*near))**2-1/256)<1e-12
    # Integrate monomials instead of applying a low-energy fit.
    for copies in (2,3):
        simplex = mp.mpf(factorial(3))**copies/factorial(4*copies)
        coeff = (mp.mpf(3)/2 if copies==2 else 6) * simplex/(6*mp.pi**2)**copies
        assert mp.almosteq(coeff, (mp.mpf(3)/2 if copies==2 else 6)/(mp.pi**(2*copies)*factorial(4*copies)))
    print("closed contour integral, time doubling, infrared angular density, endpoint asymptotics and both band coefficients passed")


if __name__ == "__main__":
    group_control()
    wick_control()
    kernel_control()
