"""Check the noncommuting cube, discrete Hodge identity and infrared powers."""
import importlib.util
from itertools import combinations, permutations
from math import factorial, pi
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

source = importlib.util.spec_from_file_location("wilson_controls", Path(__file__).resolve().parents[1]/"check.py")
quaternion = importlib.util.module_from_spec(source)
source.loader.exec_module(quaternion)
word, inverse = quaternion.word, quaternion.inverse
identity = np.array([1.,0.,0.,0.])


def cube_checks():
    rng = np.random.default_rng(6712)
    largest = 0.
    for _ in range(24):
        edges = {}
        for i in range(3):
            for base in range(8):
                if not base & (1<<i):
                    q = rng.normal(size=4)
                    edges[base,i] = q/np.linalg.norm(q)
        def path(base, order):
            result = identity
            for axis in order:
                result = word(result,edges[base,axis])
                base |= 1<<axis
            return result
        for initial in permutations(range(3)):
            axes = list(initial)
            total = identity
            for pos in (0,1,0,1,0,1):
                prefix = axes[:pos]
                base = sum(1<<i for i in prefix)
                i,j = axes[pos:pos+2]
                face = word(path(base,(min(i,j),max(i,j))),inverse(path(base,(max(i,j),min(i,j)))))
                transport = path(0,prefix)
                expected = word(transport,face if i<j else inverse(face),inverse(transport))
                first = path(0,axes)
                axes[pos],axes[pos+1] = axes[pos+1],axes[pos]
                ratio = word(first,inverse(path(0,axes)))
                largest = max(largest, np.linalg.norm(ratio-expected))
                total = word(total,expected)
            largest = max(largest,np.linalg.norm(total-identity))
    assert largest < 1e-13
    print(f"144 oriented noncommuting cube cycles, maximum word error {largest:.3g}")


def rooted_insertions():
    """Vary an edge traversed backwards by the root path, including remote faces."""
    beta, delta = 19., 1e-5
    origin = (0,0,0,0)
    edge = ((-1,0,0,0),0)
    rng = np.random.default_rng(9931)
    links = {}
    def add(x, axis, step):
        return tuple(v+step*(axis==i) for i,v in enumerate(x))
    def path(x, moves):
        pieces = []
        for axis, direction in moves:
            end = add(x,axis,direction)
            key = (x if direction==1 else end,axis)
            if key not in links:
                q = rng.normal(size=4)
                links[key] = q/np.linalg.norm(q)
            pieces.append((key,direction))
            x = end
        return pieces
    def factors(p, value=None):
        for key,orientation in p:
            u = value if key==edge and value is not None else links[key]
            yield u if orientation==1 else inverse(u)
    def value(p,changed=None):
        return word(*factors(p,changed))
    detour = path(origin,[(1,1),(0,-1),(1,-1)])
    frame = value(detour)
    assert all(e!=edge for e,_ in detour)
    X = word(inverse(frame),np.array([0.,1.,0.,0.]),frame)/np.sqrt(beta)
    def logarithmic(p):
        deriv = np.zeros(4)
        prefix = identity
        for ((key,orientation),step) in zip(p,factors(p)):
            updated = word(prefix,step)
            if key==edge:
                start = prefix if orientation==1 else updated
                deriv += orientation*word(start,X,inverse(start))
            prefix = updated
        return deriv
    max_error, path_effect = 0.,0.
    for t,i,j in ((-1,0,1),(-1,1,2),(-7,1,2),(-3,0,3),(0,1,0)):
        start = (t,0,0,0)
        rootpath = path(origin,[(0,-1)]*(-t))
        face = path(start,[(i,1),(j,1),(i,-1),(j,-1)])
        R,P = value(rootpath),value(face)
        rooted = word(R,P,inverse(R))
        Xr,Xp = logarithmic(rootpath),logarithmic(face)
        direct = word(R,Xp,P,inverse(R))
        extra = word(Xr,rooted)-word(rooted,Xr)
        expected = np.sqrt(beta)*(direct+extra)[1:]
        def evaluation(h):
            generator = np.r_[np.cos(h/np.sqrt(beta)),np.sqrt(beta)*X[1:]*np.sin(h/np.sqrt(beta))]
            new = word(generator,links[edge])
            modR = value(rootpath,new)
            return np.sqrt(beta)*word(modR,value(face,new),inverse(modR))[1:]
        fd = (evaluation(delta)-evaluation(-delta))/(2*delta)
        max_error = max(max_error,np.linalg.norm(fd-expected))
        path_effect = max(path_effect,np.sqrt(beta)*np.linalg.norm(extra[1:]))
    assert max_error<2e-9 and path_effect>.1
    print(f"Five root-dependent insertions, maximum derivative error {max_error:.3g}; "
          f"omitting path differentiation changes a derivative by {path_effect:.3g}")


def d(form):
    size = len(next(iter(form)))
    out = {}
    for axes in combinations(range(4),size+1):
        terms = []
        for pos,i in enumerate(axes):
            a = form[axes[:pos]+axes[pos+1:]]
            terms.append((-1)**pos*(np.roll(a,-1,axis=i)-a))
        out[axes] = sum(terms)
    return out


def adjoint(form):
    degree = len(next(iter(form)))
    out = {}
    for axes in combinations(range(4),degree-1):
        terms = []
        for i in range(4):
            if i not in axes:
                parent = tuple(sorted((*axes,i)))
                a = form[parent]
                terms.append((-1)**parent.index(i)*(np.roll(a,1,axis=i)-a))
        out[axes] = sum(terms)
    return out


def heat(a):
    return a/2+sum(np.roll(a,s,axis=i) for s in (-1,1) for i in range(4))/16


def hodge_checks():
    size = 11
    axes = (0,1)
    for order in (1,2,3):
        initial = np.zeros((size,)*4)
        initial[0,0,0,0] = 1.
        for _ in range(order):
            initial -= np.roll(initial,1,axis=2)
        a, accumulated = initial.copy(), np.zeros_like(initial)
        for m in range(1,13):
            accumulated += a/16
            a = heat(a)
            potential = {ij:accumulated if ij==axes else np.zeros_like(a)
                         for ij in combinations(range(4),2)}
            u,k = d(adjoint(potential)), adjoint(d(potential))
            for ij in potential:
                expected = initial-a if ij==axes else 0.
                np.testing.assert_allclose(u[ij]+k[ij],expected,atol=3e-15)
    print("36 four-dimensional Hodge decompositions in all six face orientations")


def free_scaled(order,n,rule):
    # Octant cube split into three sectors by its largest component.
    x,w = leggauss(rule)
    u, wu = (x+1)/2,w/2
    # Radial variable is n*max|q_i|. Split the growing domain near its mass.
    cuts = sorted({0.,min(8.,n*pi),min(24.,n*pi),min(64.,n*pi),n*pi})
    total = 0.
    for lo,hi in zip(cuts[:-1],cuts[1:]):
        r = (lo+(hi-lo)*u)[:,None,None]
        wm = ((hi-lo)*wu[:,None,None])*wu[None,:,None]*wu[None,None,:]
        for leading in range(3):
            comps = [r/n*np.ones((1,1,1)),r/n*u[None,:,None],r/n*u[None,None,:]]
            comps = comps[leading:]+comps[:leading]
            h2 = [(2*np.sin(q/2))**2 for q in comps]
            energy = 2*np.arcsinh(np.sqrt(sum(h2))/2)
            weight = h2[2]**order*(h2[0]+h2[1])/(2*np.sinh(energy))
            total += np.sum(wm*r*r*weight*np.exp(-n*energy))
    return total*n**(1+2*order)/pi**3


if __name__ == "__main__":
    cube_checks()
    rooted_insertions()
    hodge_checks()
    for order in (1,2,3):
        asymptotic = factorial(2*order+3)/(2*pi**2*(2*order+1)*(2*order+3))
        for n in (8,32,128):
            measured = free_scaled(order,n,24)
            checked = free_scaled(order,n,36)
            np.testing.assert_allclose(measured,checked,rtol=3e-9)
            if n==128:
                assert abs(checked/asymptotic-1)<.006
            print(f"order {order}, lag {n:3}, scaled free covariance {checked:.9g}, limit {asymptotic:.9g}")
