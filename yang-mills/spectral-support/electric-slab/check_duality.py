"""Exact Wick pairing counts and Hodge-conjugation checks in three-color Maxwell theory."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product, permutations
from math import prod
import numpy as np


def pairings(slots):
    if not slots:
        yield []
        return
    for i in range(1,len(slots)):
        if slots[0]//2!=slots[i]//2:
            for rest in pairings(slots[1:i]+slots[i+1:]):
                yield [(slots[0]//2,slots[i]//2)]+rest


def collinear():
    dates=[0,1,3,7]
    def ker(i,j): return F(1,abs(dates[i]-dates[j])**4)
    cov=lambda i,j:36*ker(i,j)**2
    count=Counter()
    connected=F(0)
    for graph in pairings(list(range(8))):
        if len(set(graph))<4:
            continue
        cycle=tuple(sorted(graph))
        count[cycle]+=1
        connected+=18*prod(ker(i,j) for i,j in graph)
    assert sorted(count.values())==[16,16,16]
    denom=sum(36**2*prod(ker(i,j) for i,j in cycle) for cycle in count)
    assert connected/denom==F(2,9)
    tri=list(pairings(list(range(6))))
    assert len(tri)==8
    moment=9*sum(prod(ker(i,j) for i,j in graph) for graph in tri)
    squared=moment**2/prod(F(18)*ker(i,j)**2 for i,j in combinations(range(3),2))
    assert squared==F(8,9)
    print("labeled Wick enumeration; 3 scalar four-cycles with 16 assignments each; normalized 2/9 and squared electric triangle 8/9")


def arbitrary():
    rng=np.random.default_rng(988312)
    x=rng.integers(-6,7,size=(5,4)).astype(float)
    indices=list(combinations(range(4),2))
    J=np.zeros((6,6))
    for i,(a,b) in enumerate(indices):
        c,d=sorted(set(range(4))-{a,b})
        order=(a,b,c,d)
        J[i,indices.index((c,d))]=(-1)**sum(z>w for k,z in enumerate(order) for w in order[k+1:])
    ins=[np.eye(6)]+[np.diag([float(a in pair)-.5 for pair in indices]) for a in range(4)]
    kernels={}
    for a,b in permutations(range(5),2):
        y=x[a]-x[b]
        inv=np.eye(4)-2*np.outer(y,y)/(y@y)
        ker=np.array([[inv[i,k]*inv[j,l]-inv[i,l]*inv[j,k] for k,l in indices] for i,j in indices])
        assert np.max(abs(J@ker@J+ker))<1e-14
        kernels[a,b]=ker
    nchecked=0
    for size in (2,3,4,5):
        for vertices in product(range(3), repeat=size):
            if vertices.count(0)%2==0:
                continue
            word=np.eye(6)
            for i,vertex in enumerate(vertices):
                word=word@ins[vertex]@kernels[i,(i+1)%size]
            assert np.max(abs(J@word@J+word))<2e-14 and abs(np.trace(word))<1e-13
            nchecked+=1
    assert abs(np.trace(ins[0]@kernels[0,1]@ins[0]@kernels[1,0])-6)<1e-13
    print(nchecked,"noncollinear cycles with odd scalar count, Hodge sign and a nonzero even control passed")


if __name__=="__main__":
    collinear()
    arbitrary()
