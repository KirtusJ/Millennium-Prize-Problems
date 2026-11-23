"""Gauge singlets with one or more odd link-inversion parities."""
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from math import prod
from pathlib import Path
import sys
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from certify import I, cart, kinetic, mat, rule, stack
from spectrum import inner, moment
from certify import radial as even_radial


def singlets(center, inversion, cutoff):
    weights = [kinetic(n+1) for n in range(17)]
    assert weights[16][1] < cutoff
    choices = [[(n,l) for n in range(c,16,2) for l in range(p,n+1,2)]
               for c,p in zip(center,inversion)]
    rows = []
    for links in product(*choices):
        ns, ls = zip(*links)
        if abs(ls[0]-ls[1]) <= ls[2] <= ls[0]+ls[1]:
            lo, hi = (prod(weights[n][k] for n in ns) for k in (0,1))
            if lo > cutoff:
                rows.append((ns,ls,(lo,hi)))
            else:
                assert hi < cutoff
    return rows


def odd_inner(f, g):
    # The square of the scalar triple product is the angular Gram determinant.
    gram = {(0,0,0):1,(1,1,1):2,(2,0,0):-1,(0,2,0):-1,(0,0,2):-1}
    return sum(cv*dv*coef*moment(i+a+s,j+b+t,k+c+u)
               for (i,j,k),cv in f.items() for (a,b,c),dv in g.items()
               for (s,t,u),coef in gram.items())


def angular_shapes(labels):
    odd = sum(labels[0]) % 2
    metric = odd_inner if odd else inner
    shapes, norms = [], []
    for i,j,k in labels:
        power = ((i+j-k-odd)//2,(i+k-j-odd)//2,(j+k-i-odd)//2)
        assert min(power) >= 0
        f = {power: F(1)}
        for g, norm in zip(shapes, norms):
            coeff = metric(f,g)/norm
            if coeff:
                for key,val in g.items():
                    f[key] = f.get(key,F(0))-coeff*val
        f = {key:val for key,val in f.items() if val}
        norm = metric(f,f)
        assert norm>0 and all(metric(f,g)==0 for g in shapes)
        shapes.append(f)
        norms.append(norm)
    return shapes, norms


def blocks(cutoff):
    rows = {}
    for flags in combinations_with_replacement(range(4),3):
        center = tuple(f//2 for f in flags)
        inversion = tuple(f%2 for f in flags)
        if any(inversion):
            rows[flags] = singlets(center,inversion,cutoff)
    return rows


def exterior_bounds():
    from certify import brackets, exp_negative, rowsum, upper_abs
    from scipy.linalg import eigh
    cutoff = F(1,200)
    sectors = blocks(cutoff)
    grouped = {}
    for flags, basis in sectors.items():
        parity = tuple(f%2 for f in flags)
        grouped.setdefault(parity,set()).update(ls for _,ls,_ in basis)

    v, w = rule("P")
    z, wz = rule("T")
    x,y,z = cart(v,v,z)
    w1,w2,w3 = cart(w,w,wz)
    aw = w1*w2*w3
    cross = x*y+((1-x.square())*(1-y.square())).sqrt()*z
    gram = (1-x.square())*(1-y.square())*(1-z.square())
    angular = stack([1-x.square(),1-y.square(),1-cross.square()])
    keys, columns = {}, []
    for parity, labels in grouped.items():
        labels = sorted(labels,key=lambda s:(sum(s),s))
        shapes,norms = angular_shapes(labels)
        fields = [sum(I.rational(c)*x**i*y**j*cross**k for (i,j,k),c in f.items())
                  /I.rational(norm).sqrt() for f,norm in zip(shapes,norms)]
        gram_weight = aw*gram if sum(parity)%2 else aw
        for i,li in enumerate(labels):
            for j in range(i+1):
                lj = labels[j]
                keys[li,lj] = keys[lj,li] = len(columns)
                columns.append(fields[i]*fields[j]*gram_weight)
    angular_weights = stack(columns).T
    assert odd_inner({(0,0,0):1},{(0,0,0):1}) == F(2,9)
    free_gram = mat(I(np.ones((1,angular_weights.lo.shape[0]))),angular_weights)
    for (li,lj),column in keys.items():
        expected = int(li == lj)
        entry = free_gram[0,column]
        assert entry.lo <= expected <= entry.hi and entry.hi-entry.lo < 0.001

    v,w = rule("U")
    pts = cart(v,v,v)
    w1,w2,w3 = cart(w,w,w)
    wr = (w1*w2*w3).sqrt()
    s = [1-q.square() for q in pts]
    pairs = stack([s[0]*s[1],s[0]*s[2],s[1]*s[2]],axis=1)
    lower = np.empty((len(wr.lo),len(columns)))
    upper = np.empty_like(lower)
    for start in range(0,len(lower),48):
        sl=slice(start,start+48)
        pot=sum(pairs[sl,i,None]*angular[i,None,:] for i in range(3))
        value=mat(exp_negative(-8*pot),angular_weights)
        lower[sl],upper[sl]=value.lo,value.hi
    integrals = I(lower,upper)
    # even_radial supplies the integer power of sin(theta); the extra sine
    # is needed for odd l. Same-parity products are polynomials in cos(theta).
    all_degrees = {(i,n,l) for basis in sectors.values() for ns,ls,_ in basis
                   for i,(n,l) in enumerate(zip(ns,ls))}
    assert max(n for _,n,_ in all_degrees)*2+36<=63
    assert max(l for _,_,l in all_degrees)*2+36<=63
    radial = {(i,n,l):even_radial(n,l,pts[i])*(s[i].sqrt() if l%2 else 1)
              for i,n,l in all_degrees}
    limits = {}
    for flags,basis in sectors.items():
        size=len(basis)
        labels=[ls for _,ls,_ in basis]
        factors=stack([wr*brackets(*kin).sqrt()*prod(radial[i,n,l] for i,(n,l) in enumerate(zip(ns,ls)))
                       for ns,ls,kin in basis])
        lo,hi=np.empty((size,size)),np.empty((size,size))
        for li in set(labels):
            ii=[a for a,l in enumerate(labels) if l==li]
            for lj in set(labels):
                jj=[a for a,l in enumerate(labels) if l==lj]
                v=mat(factors[ii]*integrals[:,keys[li,lj]],factors[jj].T)
                lo[np.ix_(ii,jj)],hi[np.ix_(ii,jj)] = v.lo,v.hi
        matrix=I(lo,hi)
        _,vec=eigh((lo+hi)/2)
        Q=I(vec)
        defect=rowsum(upper_abs(mat(Q.T,Q)-I(np.eye(size))))
        assert defect<1
        numerator = rowsum(upper_abs(mat(Q.T,mat(matrix,Q))))
        bound=I(numerator)/(1-I(defect))
        limits[flags]=float((bound+I.rational(cutoff+F(2,10**6))).hi)
    return limits


if __name__=="__main__":
    for signs,value in exterior_bounds().items():
        print(signs, f"{value:.8f}")
