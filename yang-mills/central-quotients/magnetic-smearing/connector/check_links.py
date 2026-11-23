"""Original-link packet geometry and conditional SU(2) transfer coefficients."""
from itertools import product
from math import cos, exp, pi, sin
import numpy as np
from scipy.integrate import quad
from scipy.special import ive

rng = np.random.default_rng(241109)


def unit():
    x = rng.normal(size=4)
    return x/np.linalg.norm(x)


one = np.array([1., 0., 0., 0.])


def mul(a, b):
    return np.r_[a[0]*b[0]-a[1:]@b[1:], a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:], b[1:])]


def inv(a):
    return a*np.array([1, -1, -1, -1])


def adj(a, v):
    return mul(mul(a, np.r_[0., v]), inv(a))[1:]


def step(x, i):
    return tuple(c+int(i == j) for j, c in enumerate(x))


def geometry():
    sites = list(product(range(18), range(4), range(4)))
    links = {(x, i): unit() for x in sites for i in range(3)}
    marks = [((x, 0, 0), 0) for x in range(6, 10)]
    left = [((3, 1, 1), 0.9), ((4, 1, 1), -0.24), ((3, 2, 1), 0.47)]
    right = [(tuple(a+10*(i == 0) for i, a in enumerate(x)), w) for x, w in left]

    def path(U, end, start=0):
        x, p = (start, 0, 0), one
        for i, last in enumerate(end):
            while x[i] < last:
                p = mul(p, U[x, i])
                x = step(x, i)
        assert x == end
        return p

    def packet(U, terms, start=0):
        accum = np.zeros(3)
        for x, w in terms:
            face = mul(mul(U[x, 0], U[step(x, 0), 1]), inv(mul(U[x, 1], U[step(x, 1), 0])))
            accum += w*adj(path(U, x, start), face[1:])
        return accum

    def measure(U):
        f, g = packet(U, left), packet(U, right)
        a = adj(inv(path(U, (6, 0, 0))), f)
        b = packet(U, right, 10)
        w = path(U, (10, 0, 0), 6)
        den = np.linalg.norm(f)*np.linalg.norm(g)
        h = (f@g)/den
        np.testing.assert_allclose(h, (a@adj(w,b))/den, atol=3e-13)
        return a, b, h

    a, b, h = measure(links)
    moved = dict(links)
    moved.update((e, unit()) for e in marks)
    a2, b2, h2 = measure(moved)
    np.testing.assert_allclose([a2,b2], [a,b], atol=1e-14)
    assert abs(h-h2) > 0.05
    gauge = {x:unit() for x in sites}
    rotated = {(x,i):mul(mul(gauge[x], u), inv(gauge.get(step(x,i), one))) for (x,i),u in links.items()}
    np.testing.assert_allclose(measure(rotated)[2], h, atol=5e-13)
    print(f"angle {h:.9f}; replacement {h2:.9f}; endpoint and gauge tests passed")

    def overlaps(lag):
        chosen = {((x,0,0,t),0) for x in range(6,10) for t in (0,lag)}
        overlaps = []
        for coord in product(range(5,11),(-1,0,1),(-1,0,1),range(5)):
            for i in range(4):
                for j in range(i+1,4):
                    def shift(k):
                        v = list(step(coord,k))
                        v[3] %= 5
                        return tuple(v)
                    edges = {(coord,i),(shift(i),j),(shift(j),i),(coord,j)}
                    if len(edges & chosen) >= 2:
                        overlaps.append((coord,i,j))
        return len(overlaps)
    assert [overlaps(n) for n in (1,2,3,4)] == [4,0,0,4]


def character(k, h):
    norm = quad(lambda t: sin(t)**2*exp(h*(cos(t)-1)), 0, pi, epsabs=1e-14)[0]
    val = quad(lambda t: sin(t)*sin((k+1)*t)*exp(h*(cos(t)-1)), 0, pi, epsabs=1e-14)[0]
    return val/((k+1)*norm)


def conditional():
    for beta, m in [(0.5, 3),(2., 12),(8., 27)]:
        h = 6*beta
        a, b = character(2,h), character(4,h)
        np.testing.assert_allclose([a,b], [ive(3,h)/ive(1,h),ive(5,h)/ive(1,h)], atol=5e-13)
        angle = -0.4
        e1, e2 = a**m*angle, 1/3 + b**m*(angle**2-1/3)
        # Independent recursion using the transverse variance in an isotropic random rotation.
        axial = (1+2*b)/3
        first, second = angle, angle**2
        for _ in range(m):
            first *= a
            second = axial*second+(1-axial)*(1-second)/2
        np.testing.assert_allclose([first,second],[e1,e2],atol=1e-13)
        assert abs(e1-angle*a)>0.015 and abs(e2-e1**2)>0.20
        print(f"fixed exterior beta={beta:g} m={m}: first={e1:.10f} second={e2:.10f}")


if __name__ == "__main__":
    geometry()
    conditional()
