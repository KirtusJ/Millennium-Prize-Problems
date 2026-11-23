"""Finite checks of the mask geometry, parity obstruction and Wick row bound."""
from fractions import Fraction
from itertools import combinations, product
import json


def mask_check(length, width):
    sites = list(product(range(length), repeat=4))
    directions = range(4)
    selected = set()
    for x in sites:
        slab, layer = divmod(x[0], width)
        if (slab+1)*width > length or not 0 < layer < width-1:
            continue
        if any(t in (0, length-1) for t in x):
            continue
        i = slab % 4
        if sum(x[j] for j in directions if j != i) % 2 == 0:
            selected.add((x,i))
    def step(x,k):
        return tuple((v+1) % length if j==k else v for j,v in enumerate(x))
    hits = 0
    for x in sites:
        for i,j in combinations(directions,2):
            face = ((x,i),(step(x,j),i),(x,j),(step(x,i),j))
            count = sum(edge in selected for edge in face)
            assert count <= 1
            hits += count
    assert hits == 6*len(selected)
    return {'side':length,'width':width,'links':len(selected),'incident_faces':hits}


def wick_check(k):
    # F_x is a second difference of iid standard Gaussians on axis one.
    stencil = {0:1, 1:-2, 2:1}
    def cov(delta):
        if any(delta[1:]):
            return 0
        return sum(v*stencil.get(j-delta[0],0) for j,v in stencil.items())
    sites = list(product(range(0,2*k,2),repeat=4))
    total = sum(2*cov(tuple(i-j for i,j in zip(x,y)))**2 for x in sites for y in sites)
    scaled = Fraction(total,len(sites))
    assert scaled == 76-Fraction(4,k)
    return str(scaled)


def parity_check():
    # A symmetric random sign S times (-1)^x is stationary and centered.
    # A parity mask sees S at every selected site. Full-shift averages miss it.
    n = 64
    mask = [Fraction(2,n) if i%2==0 else 0 for i in range(n)]
    phase = [(-1)**i for i in range(n)]
    def defect(u):
        return sum(abs(mask[x]-mask[(x-u)%n]) for x in range(n))
    reading = sum(a*b for a,b in zip(mask,phase))
    assert (reading,sum(phase),defect(1),defect(2)) == (1,0,2,0)
    return {'masked_amplitude':int(reading),'unit_shift_defect':int(defect(1)),
            'even_shift_defect':int(defect(2))}


if __name__ == '__main__':
    print(json.dumps({'masks':[mask_check(16,4),mask_check(17,4)],
                      'K4_times_variance':[wick_check(k) for k in (1,2,3,4)],
                      'parity':parity_check()},indent=2))
