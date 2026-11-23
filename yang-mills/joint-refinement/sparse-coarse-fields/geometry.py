"""Check coarse-edge incidence, clearance, and likelihood-ratio comparison."""
from collections import defaultdict
from itertools import combinations, product
import numpy as np

ONE = np.array([1., 0., 0., 0.])
CONJ = np.array([1., -1., -1., -1.])


def multiply(q, r):
    return np.r_[q[0]*r[0] - q[1:] @ r[1:],
                 q[0]*r[1:] + r[0]*q[1:] + np.cross(q[1:], r[1:])]


def check(side, radius, rng):
    n = side//2
    sites = list(product(range(n), repeat=3))
    def step(x, i, dx):
        return tuple((v + dx*(j == i)) % n for j,v in enumerate(x))
    tree = set()
    for x in sites[1:]:
        i = next(d for d,v in enumerate(x) if v)
        tree.add((step(x,i,-1), i))
    links = {(x,i): ONE.copy() if (x,i) in tree else (-1)**int(rng.integers(2))*ONE
             for x in sites for i in range(3)}
    by_edge = defaultdict(list)
    paths = []
    for x in sites:
        for i,j in combinations(range(3),2):
            loop = [(x,i),(step(x,i,1),j),(step(x,j,1),i),(x,j)]
            for e in loop:
                by_edge[e].append(len(paths))
            paths.append(loop)
    assert all(len(faces)==4 for faces in by_edge.values())
    colours = []
    for f, path in enumerate(paths):
        used = {colours[g] for e in path for g in by_edge[e] if g<f}
        colours.append(next(c for c in range(13) if c not in used))
    assert all(len({colours[f] for f in faces}) == 4 for faces in by_edge.values())

    def clear(f):
        a,b,c,d = [links[e] for e in paths[f]]
        return multiply(multiply(a,b),multiply(CONJ*c,CONJ*d))[0] > -np.cos(radius)
    bad = [f for f in range(len(paths)) if not clear(f)]
    chosen = sorted({next(e for e in paths[f] if e not in tree) for f in bad})
    order = {e:j for j,e in enumerate(chosen)}
    last = defaultdict(list)
    for f,path in enumerate(paths):
        touched = [e for e in path if e in order]
        if touched:
            last[max(touched,key=order.get)].append(f)
    for e in chosen:
        old = links[e]
        assert len(last[e]) <= 4
        for attempt in range(2000):
            angle = 2*radius * rng.random()**(1/3)
            if rng.random() > np.sinc(angle/np.pi)**2:
                continue
            axis = rng.normal(size=3)
            links[e] = multiply(old, np.r_[np.cos(angle), np.sin(angle)*axis/np.linalg.norm(axis)])
            if all(clear(f) for f in last[e]):
                break
        else:
            raise AssertionError("No clearing move found")
    assert all(clear(f) for f in range(len(paths)))
    assert all(np.array_equal(links[e], ONE) for e in tree)
    print(f"N={side}, theta={radius}, faces={len(paths)}, bad={len(bad)}, "
          f"links moved={len(chosen)}, colours used={max(colours)+1}")


def ratio(law, f):
    loss = 0
    for axis in (0,1):
        predictor = np.sum(law*f,axis=axis,keepdims=True)/law.sum(axis=axis,keepdims=True)
        loss += np.sum(law*(f-predictor)**2)/2
    return loss/np.sum(law*(f-np.sum(law*f))**2)


if __name__ == "__main__":
    rng=np.random.default_rng(837601)
    for side in (6,8,10,12):
        check(side, .18, rng)
    for i in range(200):
        law = rng.dirichlet(np.ones(12)).reshape(3,4)
        tilt = rng.uniform(-1.5,1.5,(3,4))
        new = law*np.exp(tilt)
        new /= new.sum()
        f = rng.normal(size=law.shape)
        assert abs(np.log(ratio(law,f)/ratio(new,f))) <= np.ptp(tilt)+1e-12
    print("200 fixed-coordinate variance comparisons passed")
