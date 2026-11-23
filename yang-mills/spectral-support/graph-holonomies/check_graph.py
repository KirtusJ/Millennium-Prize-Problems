"""Finite channel, graph subdivision and reflection controls."""
from collections import Counter
from itertools import permutations, product
import numpy as np


def channel():
    # Binary observations are conditionally independent given a nonuniform exterior.
    prior = np.array([0.1, 0.3, 0.6])
    for m in (1, 2, 5, 9):
        deltas = np.linspace(0.05, 0.75, m)
        patterns = np.array(list(product([-1, 1], repeat=m)))
        rows = np.stack([np.prod(1 + patterns*deltas*v, axis=1) for v in (-1., 0.25, 1.)])
        K = rows / 2**m
        joint = prior[:, None] * K
        marginal = joint.sum(axis=0)
        s = np.linalg.svd(joint / np.sqrt(prior[:, None]*marginal), compute_uv=False)
        assert s[1]**2 <= 1 - np.prod(1 - deltas**2) + 1e-13
        assert np.max((1/rows).mean(axis=1)) <= 1/np.prod(1-deltas**2) + 1e-13
        assert np.max(((rows-1)**2).mean(axis=1)) <= np.prod(1+deltas**2) - 1 + 1e-13
    d = .7
    binary = np.array([[1+d, 1-d], [1-d, 1+d]])/2
    np.testing.assert_allclose(np.linalg.svd(binary, compute_uv=False)[1], d)
    # TV convergence of joint to product cannot control an arbitrarily rare bit in L2.
    p = np.array([.99999, .00001])
    joint = np.diag(p)
    tv = np.abs(joint - np.outer(p, p)).sum()/2
    corr = np.linalg.svd(joint / np.sqrt(np.outer(p, p)), compute_uv=False)[1]
    assert tv < 2.1e-5 and corr > .99999
    print("Sharp binary channel, rare copied bit and 1–9 conditional outputs checked.")


def shared():
    P = list(permutations(range(3)))
    comp = lambda a,b: tuple(a[b[i]] for i in range(3))
    inv = lambda a: tuple(a.index(i) for i in range(3))
    counts = Counter(comp(comp(comp(a,b),inv(a)),inv(b)) for a,b in product(P, repeat=2))
    assert counts[P[0]] == 18 and sorted(counts.values()) == [9,9,18]
    trace = lambda a: sum(a[i]==i for i in range(3))-1
    assert sum(trace(a)*v for a,v in counts.items()) == 18
    assert Counter(comp(a,b) for a,b in product(P,repeat=2)) == {a:6 for a in P}
    print("Haar subdivision and nonabelian commutator histogram checked by permutations.")


def shift(x, axis, step, sides):
    t=list(x)
    t[axis]=(t[axis]+step)%sides[axis]
    return tuple(t)


def geometry(sides):
    # Lines span axis zero. A greedy proper transverse coloring works on odd periods too.
    transverse=sides[1:]
    sites=list(product(*(range(n) for n in transverse)))
    colors={}
    for x in sites:
        used={colors[y] for a in range(3) for s in (-1,1)
              if (y:=shift(x,a,s,transverse)) in colors}
        colors[x]=next(c for c in range(7) if c not in used)
    selected={((j,)+x,0) for x,c in colors.items() for j in range(sides[0]) if j%7==c}
    assert all(sum(((j,)+x,0) in selected for j in range(sides[0]))>=sides[0]//7 for x in sites)
    for x in product(*(range(n) for n in sides)):
        for i in range(4):
            for j in range(i+1,4):
                face={(x,i),(x,j),(shift(x,j,1,sides),i),(shift(x,i,1,sides),j)}
                assert len(face & selected)<=1


def reflections(sides):
    # Follow the geometric site reflections of one 01 face of the initial unit cube.
    points={(x,y,0,0) for x in (0,1) for y in (0,1)}
    canonical=lambda face: tuple(sorted(face))
    counts=Counter({canonical(points):1})
    for axis,period in enumerate(sides):
        width=1
        while width<period:
            reflected=Counter()
            for face, mult in counts.items():
                def reflect(p):
                    v=list(p)
                    v[axis]=(2*width-v[axis])%period
                    return tuple(v)
                reflected[canonical(map(reflect,face))]+=mult
            counts.update(reflected)
            width*=2
    N=int(np.prod(sides))
    assert counts.total()==N and max(counts.values())==4 and len(counts)==N//4
    print(f"Site reflection {sides}: {N} copies, {len(counts)} distinct bad faces.")


if __name__=="__main__":
    channel()
    shared()
    geometry((15,3,4,5))
    geometry((16,4,4,4))
    reflections((4,4,4,4))
    reflections((4,8,4,8))
    print("All-axis plaquette enumeration confirms the winding-line selection on both tori.")
