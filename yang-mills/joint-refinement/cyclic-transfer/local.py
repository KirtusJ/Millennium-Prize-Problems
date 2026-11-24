"""Exact ball-moment bounds and geometry of the two matched Wilson probes."""
from fractions import Fraction as F
from itertools import product
from math import prod,pi,exp


def moment(powers):
    if any(e%2 for e in powers):return F(0)
    top=prod(prod(range(1,e,2)) for e in powers)
    return F(top,prod(range(5,sum(powers)+4,2)))


def gram_floor(d,threshold):
    exponents=[p for p in product(range(2*d+1),repeat=3) if sum(p)<=2*d]
    size=len(exponents)
    a=[[moment([x+y for x,y in zip(u,v)])-threshold*(i==j)
        for j,v in enumerate(exponents)] for i,u in enumerate(exponents)]
    # Exact positive pivots of the Schur complements prove G > threshold I.
    for i in range(size):
        pivot=a[i][i]
        assert pivot>0
        for j in range(i+1,size):
            for k in range(j,size):
                a[j][k]-=a[i][j]*a[i][k]/pivot
    c=4/pi**2*exp(-2)/10*2**(-3-2*d)*(4*pi/3)*float(threshold)/size
    print(f"d={d} monomials={size} rational Gram floor={threshold} c={c:.8g}")
    return c


def probe_support(n):
    def step(v,i):
        return tuple((a+(j==i))%n for j,a in enumerate(v))
    def free(edge):
        v,i=edge
        return any(a%2 for j,a in enumerate(v) if j!=i)
    groups=[set() for _ in range(24)]
    for v in product(range(n),repeat=3):
        parity=sum((a%2)<<i for i,a in enumerate(v))
        for o,(i,j) in enumerate([(0,1),(0,2),(1,2)]):
            groups[8*o+parity].update([(v if v[j]%2 else step(v,j),i),
                                        (v if v[i]%2 else step(v,i),j)])
    degrees={}
    for x,y in product(range(2),repeat=2):
        v=(x,y,0)
        face=[(v,0),(step(v,0),1),(step(v,1),0),(v,1)]
        path=[((0,0,0),0)]*x+[((x,0,0),1)]*y
        factors=[e for e in path+face+path if free(e)]
        if x==y==0: first=set(factors)
        for e in factors:
            degrees[e]=max(degrees.get(e,0),factors.count(e))
    def active(edges):
        return [i for i,g in enumerate(groups) if g.intersection(edges)]
    assert active(first)==[0,1,2] and active(degrees)==[0,1,2,3]
    assert sorted(degrees.values())==[1,1,1,2]
    assert all(sum(e in g for g in groups)==2 for e in degrees)
    print(f"side {n}: one-face colours {active(first)}, four-face colours {active(degrees)}")


if __name__=="__main__":
    c1=gram_floor(1,F(1,1000))
    c2=gram_floor(2,F(1,100000))
    print("four-face mixing prefactor",c1**3*c2/(12*1750))
    for n in (6,8,10):probe_support(n)
