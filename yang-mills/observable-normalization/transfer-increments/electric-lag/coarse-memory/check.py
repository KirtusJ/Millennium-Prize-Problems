"""Three-time laws in a binary electric control and a Haar SU(2) square check."""
from itertools import combinations, product
from math import sqrt

import mpmath as mp
import numpy as np
from scipy.special import ive


def divided(t, r, lam, n):
    return (t-lam*r)/(1-lam)*sum(t**j*r**(n-1-j) for j in range(n))


def binary(shared, n, k, q):
    states = list(product((-1, 1), repeat=2))
    r, lam, t = q**k, q**4, q**(k+4-2*shared)
    D = divided(t, r, lam, n)
    expected = (D**2, D**4/(2*(1-r**(2*n))**2))

    def measure(b):
        T = mp.matrix(4)
        for i, (f, p) in enumerate(states):
            for j, (v, z) in enumerate(states):
                T[i, j] = ((1+r*f*v+lam*p*z+t*f*p*v*z)/4)*mp.exp(b*(p+z)/2)
        vals, vecs = mp.eigsy(T)
        vacuum = vecs[:, 3]
        K = mp.diag([1/v for v in vacuum])*T*mp.diag(vacuum)/vals[3]
        step = K**n
        coarse = [-1, 1]
        rows = [[sum(step[i,j] for j,(w,_) in enumerate(states) if w == u)
                 for u in coarse] for i in range(4)]
        moment = information = mp.mpf(0)
        for y in coarse:
            mids = [i for i,(v,_) in enumerate(states) if v == y]
            mass = sum(vacuum[i]**2 for i in mids)
            for z, w in product(range(2), repeat=2):
                joint = sum(vacuum[i]**2*rows[i][z]*rows[i][w] for i in mids)/mass
                pz = sum(vacuum[i]**2*rows[i][z] for i in mids)/mass
                pw = sum(vacuum[i]**2*rows[i][w] for i in mids)/mass
                moment += mass*(joint-pz*pw)*coarse[z]*coarse[w]
                information += mass*joint*mp.log(joint/(pz*pw))
        return moment, information

    for b in map(mp.mpf, ("0.05", "0.005", "0.0005")):
        vals = measure(b)
        negative = measure(-b)
        assert max(abs(x-y) for x,y in zip(vals, negative)) < mp.mpf("1e-42")
        ratios = (vals[0]/b**2, vals[1]/b**4)
    assert all(abs(x/y-1) < mp.mpf("0.00001") for x,y in zip(ratios, expected))
    print("shared edges", shared, "scaled memory and information",
          *(mp.nstr(x, 10) for x in ratios))


def moved(p, a, s=1):
    return tuple(x+s*(j==a) for j,x in enumerate(p))


def square(p, a, b, width):
    return {(moved(moved(p, axis, i), other, side), axis)
            for axis, other in ((a,b),(b,a)) for i in range(width) for side in (0,width)}


def cycle(edges):
    neighbors = {}
    for p,a in edges:
        end = moved(p,a)
        neighbors.setdefault(p, []).append((end,(p,a),1))
        neighbors.setdefault(end, []).append((p,(p,a),-1))
    start = cur = min(neighbors)
    prev = None
    word = []
    while True:
        choices = neighbors[cur]
        assert len(choices)==2
        nxt, e, sign = next(triple for triple in choices if triple[0] != prev)
        word.append((e,sign))
        prev, cur = cur,nxt
        if cur == start:
            assert len(word)==len(edges)
            return word


def multiply(a, b):
    return np.column_stack((a[:,0]*b[:,0]-(a[:,1:]*b[:,1:]).sum(axis=1),
                            a[:,:1]*b[:,1:]+b[:,:1]*a[:,1:]+np.cross(a[:,1:],b[:,1:])))


def haar_square():
    ell, n, g = 2, 2, 9
    k = 4*ell
    q, adj = ive([2,3],g)/ive(1,g)
    r, lam = q**k, q**4
    coarse = square((0,0,0),0,1,ell)
    terms, all_edges = [], set(coarse)
    predicted = 0
    for p in product(range(-1,ell+1),range(-1,ell+1),range(-1,1)):
        for a,b in combinations(range(3),2):
            face = square(p,a,b,1)
            d = len(coarse & face)
            if d:
                u = q**(k+4-2*d)
                du, dv = (divided(t,r,lam,n) for t in (u,u*adj**d))
                terms.append((cycle(face), cycle(coarse^face), du, dv))
                all_edges.update(face)
                predicted += (du**2+3*dv**2)/16
    assert len(terms)==4*k-4
    rng = np.random.default_rng(293)
    batch_means = []
    for _ in range(32):
        links = {}
        for e in sorted(all_edges):
            v = rng.normal(size=(512,4))
            links[e] = v/np.linalg.norm(v,axis=1)[:,None]

        def trace(word):
            v = np.zeros((512,4))
            v[:,0] = 1
            for e,sign in word:
                u = links[e] if sign==1 else links[e]*[1,-1,-1,-1]
                v = multiply(v,u)
            return 2*v[:,0]

        f = trace(cycle(coarse))
        residual = sum((du-dv)*trace(detour)/4+dv*f*trace(face)/2
                       for face,detour,du,dv in terms)
        batch_means.append(np.mean(residual**2))
    mean = np.mean(batch_means)
    se = np.std(batch_means,ddof=1)/sqrt(len(batch_means))
    print(f"SU(2) square: measured {mean:.8f}, batch SE {se:.8f}, predicted {predicted:.8f}")
    assert abs(mean-predicted) <= 6*se


if __name__ == "__main__":
    mp.mp.dps = 55
    for d in (1,2):
        binary(d,3,8,mp.mpf("0.85"))
    haar_square()
