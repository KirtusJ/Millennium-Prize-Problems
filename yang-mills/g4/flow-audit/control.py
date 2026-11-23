"""Check actual periodic plaquette incidences, constants, and a finite Fourier fixture."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import cos, exp, fsum, pi
import json


def peeling(d, side):
    """Return fixed tree links and ordered (pivot link, plaquette) pairs."""
    if d == 1:
        return {((t,),0) for t in range(side-1)}, []
    axis = d-1
    sites = list(product(range(side), repeat=axis))
    tree = {((*x,t),axis) for x in sites for t in range(side-1)}
    order = []
    for x in sorted(sites, key=sum, reverse=True):
        if any(x):
            i = next(i for i in range(axis) if x[i])
            parent = tuple(v-int(j==i) for j,v in enumerate(x))
            order.append((((*x,side-1),axis),((*parent,side-1),i,axis)))
    for t in reversed(range(1,side)):
        for x,i in product(sites,range(axis)):
            order.append((((*x,t),i),((*x,t-1),i,axis)))
    base_tree, base_order = peeling(axis,side)
    tree.update(((*x,0),i) for x,i in base_tree)
    order.extend((((*x,0),i),((*y,0),j,k)) for (x,i),(y,j,k) in base_order)
    return tree,order


def count_peeling(d,side):
    def step(x,i):
        return tuple((t+int(j==i))%side for j,t in enumerate(x))
    def edges(face):
        x,i,j = face
        return {(x,i),(step(x,i),j),(step(x,j),i),(x,j)}
    tree, order = peeling(d,side)
    available = {f:edges(f)-tree for _,f in order}
    counts = Counter(link for links in available.values() for link in links)
    assert len(tree) == side**d-1
    assert len(order) == len(available) == (d-1)*(side**d-1)
    for pivot,face in order:
        assert pivot in available[face] and counts[pivot] == 1
        counts.subtract(available[face])
    assert all(n==0 for n in counts.values())
    return [d,side,len(order),d*side**d-len(tree)-len(order)]


def moment_bounds():
    # (12/11)^(5/2) < 5/4 by squaring. For s=40, the exponential
    # terms use e>2, pi<4 and 40^(3/2)<256.
    assert Q(12,11)**5 < Q(5,4)**2 and 40**3 < 256**2
    ratio = (Q(3,80)*Q(5,4) + Q(4*512*256,2**36))/(1-Q(3,2**20))
    assert ratio < Q(1,20)
    return str(ratio)


def torus(full):
    n = 16
    aq = [2-2*cos(2*pi*i/n) for i in range(n)]
    modes = [(x,y,z) for x,y,z in product(aq, repeat=3) if x+y>0]
    shells = [fsum((x+y)/(x+y+z+t)*exp(-12*((x+y+z+t) if full else (x+y+z)))
                   for x,y,z in modes) for t in aq]
    total = fsum(shells)
    def cov(lag):
        return (fsum(w*cos(2*pi*j*lag/n) for j,w in enumerate(shells))/total)**2
    return round(cov(2)-2*cov(3)+cov(4),11)


if __name__ == '__main__':
    # In two-dimensional Z/2 the Haar plaquette law is uniform on even flux.
    z = Q(2,3)
    assert z**16 + (1-z)**16 <= z**15
    print(json.dumps({'counts':[count_peeling(d,n) for d,n in product((2,3,4),(3,4,5))],
                      'moment_ratio_upper':moment_bounds(),
                      'torus_16_full':torus(True),'torus_16_spatial':torus(False)},indent=2))
