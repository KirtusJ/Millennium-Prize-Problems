"""Check the compact-group score, the action remainder and a compact U(1) cube."""
from itertools import product
import numpy as np
from scipy.linalg import expm


def pairing(a, b):
    return np.trace(a.conj().T @ b).real / len(a)


def skew(a):
    return (a - a.conj().T) / 2


def score_test(name, links, generators, project):
    worst = 0.0
    for u, x in product(links, generators):
        n = len(u)
        action = lambda v: 1 - np.trace(v).real / n
        h = 1e-5
        for sign in (1, -1):
            def varied(t):
                return expm(t*x) @ u if sign == 1 else u.conj().T @ expm(-t*x)
            base = varied(0)
            direction = x if sign == 1 else -base @ x @ base.conj().T
            grad = project(skew(base))
            direct = project(skew(direction @ base))
            fd = (action(varied(h)) - action(varied(-h))) / (2*h)
            dfield = project(skew(varied(h) - varied(-h))) / (2*h)
            worst = max(worst, abs(fd-pairing(direction, grad)), np.linalg.norm(dfield-direct))
            ident = np.eye(n)
            herm = (base + base.conj().T)/2 - ident
            normal = skew(base) - grad
            residual = 2*action(base)-pairing(grad,grad)-pairing(herm,herm)-pairing(normal,normal)
            assert abs(residual) < 1e-12
    assert worst < 2e-8, (name,worst)
    print(name, 2*len(links)*len(generators), 'signed tests, max error', format(worst,'.2g'))


def cube():
    # Positive oriented links, lifts measured in units of pi/3.
    links = {((0,0,0),0):-4, ((0,0,0),1):-1, ((0,0,1),0):-5,
             ((0,1,0),0):-1, ((1,0,0),1):1}
    angles = []
    for i, side in product(range(3), (0,1)):
        j, k = (i+1)%3, (i+2)%3
        x = tuple(side if axis == i else 0 for axis in range(3))
        step = lambda axis: tuple(a+(b==axis) for b,a in enumerate(x))
        boundary = (((x,j),1), ((step(j),k),1), ((step(k),j),-1), ((x,k),-1))
        angles.append((2*side-1)*sum(s*links.get(e,0) for e,s in boundary))
    assert angles == [1,1,1,1,1,-5] and [(a+3)%6-3 for a in angles] == [1]*6
    print('cube: six principal outward fluxes of pi/3')


if __name__ == '__main__':
    rng = np.random.default_rng(105)
    def traceless(a):
        return a - np.eye(len(a))*np.trace(a)/len(a)
    generators = [traceless(skew(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))) for _ in range(6)]
    score_test('SU(3)', [expm(x) for x in generators], generators, traceless)
    h = 1j*np.diag([1.,2.])
    project = lambda a: h*pairing(h,a)/pairing(h,h)
    score_test('weighted circle', [expm(t*h) for t in (0,.2,1,np.pi/2,3)], [h], project)
    u = np.diag([1j,-1])
    s = 1-np.trace(u).real/2
    q = project(skew(u))
    assert np.isclose(2*s-pairing(q,q)-s*s,13/20)
    j = np.array([[0.,-1.],[1.,0.]])
    project_o2 = lambda a: j*pairing(j,a)
    o2 = [expm(t*j) @ np.diag([1.,sign]) for t,sign in product((0,.7,2.),(1,-1))]
    score_test('O(2)', o2, [j], project_o2)
    cube()
