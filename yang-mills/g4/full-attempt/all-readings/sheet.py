"""Compare the height recurrence with an exact independent electric transfer on a disk."""
from fractions import Fraction as Q
from functools import cache
from itertools import product
from math import factorial
import json


def submasks(mask):
    sub = mask
    while True:
        yield sub
        if sub == 0:
            return
        sub = (sub-1)&mask


def perimeters(width, height):
    tiles = {(x,y):i for i,(x,y) in enumerate(product(range(width),range(height)))}
    out = []
    for mask in range(1<<len(tiles)):
        occupied = {p for p,i in tiles.items() if mask & (1<<i)}
        out.append(sum((x+dx,y+dy) not in occupied for x,y in occupied
                       for dx,dy in ((-1,0),(1,0),(0,-1),(0,1))))
    return out


def heights(perimeter, q):
    full = len(perimeter)-1
    f, h = [Q(1)], [Q(1)]
    for s in range(1,full+1):
        p = perimeter[s]
        z = q**p
        f.append(z/(1-z)*sum(f[t] for t in submasks(s) if t!=s))
        h.append(sum(h[s^(1<<i)] for i in range(s.bit_length()) if s & (1<<i))/p)
    return (sum(f[s]*f[t] for s in range(full+1) for t in submasks(full^s)),
            sum(h[s]*h[full^s] for s in range(full+1)))


def binary_vacuum(perimeter, q):
    """Formal perturbation of exp(b A/2) K exp(b A/2) in a Walsh basis."""
    size = len(perimeter)
    order = (size-1).bit_length()
    unit = tuple(Q(i==0) for i in range(size))
    kinetic = tuple(q**p for p in perimeter)

    @cache
    def half(power, vec):
        if power == 0:
            return vec
        prev = half(power-1,vec)
        return tuple(sum(prev[s^(1<<i)] for i in range(order))/(2*power) for s in range(size))

    def transfer(degree, vec):
        parts = [half(degree-j,tuple(k*x for k,x in zip(kinetic,half(j,vec))))
                 for j in range(degree+1)]
        return tuple(map(sum,zip(*parts)))

    vacuum, eig = [unit], [Q(1)]
    for degree in range(1,order+1):
        rhs = tuple(map(sum,zip(*(transfer(d,vacuum[degree-d]) for d in range(1,degree+1)))))
        eig.append(rhs[0])
        vacuum.append((Q(0),)+tuple(
            (rhs[s]-sum(eig[d]*vacuum[degree-d][s] for d in range(1,degree+1)))/(1-kinetic[s])
            for s in range(1,size)))
    def coeff(degree, observable):
        return sum(vacuum[d][s]*vacuum[degree-d][s^observable]
                   for d in range(degree+1) for s in range(size))
    # Divide the two series in the actual normalized stationary vacuum.
    expval = []
    for j in range(order+1):
        expval.append(coeff(j,size-1)-sum(coeff(d,0)*expval[j-d] for d in range(1,j+1)))
    assert all(v==0 for v in expval[:-1])
    return expval[-1]


def disk_contraction():
    # Quaternion subgroup of SU(2), doubled normalized Wilson traces equal the character.
    # After disk gauge fixing, four independent tile matrices have ordered boundary product.
    units = [(1,0,0,0),(-1,0,0,0),(0,1,0,0),(0,-1,0,0),
             (0,0,1,0),(0,0,-1,0),(0,0,0,1),(0,0,0,-1)]
    def mul(a,b):
        w,x,y,z=a
        v,i,j,k=b
        return (w*v-x*i-y*j-z*k,w*i+x*v+y*k-z*j,w*j-x*k+y*v+z*i,w*k+x*j-y*i+z*v)
    total=0
    for a,b,c,d in product(units,repeat=4):
        boundary=mul(mul(a,b),mul(c,d))
        total += 2*boundary[0]*a[0]*b[0]*c[0]*d[0]
    return Q(total,len(units)**4)


def run():
    gram=disk_contraction()
    assert gram==Q(1,128)
    rows=[]
    for width,height in ((1,1),(2,1),(2,2),(3,3)):
        p=perimeters(width,height)
        m=width*height
        q=Q(1,2)
        z,h=heights(p,q)
        if m<=4:
            assert binary_vacuum(p,q)==z
            assert binary_vacuum(p,Q(2,3))==heights(p,Q(2,3))[0]
        if m==1:
            assert z==(1+q**4)/(1-q**4)
        rows.append(dict(shape=[width,height], height_sum=str(z), normalized_SU2=str(z/4**m),
                         continuous_coefficient_at_kappa_1=str(h/6**m)))
    return {"quadratic_gram":str(gram), "height_coefficients":rows, "binary_transfer_comparisons":6}


if __name__=="__main__":
    print(json.dumps(run(),indent=2))
