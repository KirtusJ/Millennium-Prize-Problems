"""Integer heat-polynomial and cubical-cochain checks on the full lattice."""
from collections import Counter
from itertools import product
from math import comb


def shift(pos,i,step):
    x=list(pos)
    x[i]+=step
    return tuple(x)


def nonzero(terms):
    return {key:n for key,n in terms.items() if n}


def cochain_diff(field,adjoint):
    result=Counter()
    for (pos,face),value in field.items():
        axes=face if adjoint else (i for i in range(4) if i not in face)
        for i in axes:
            target=tuple(x for x in face if x!=i) if adjoint else tuple(sorted((*face,i)))
            sign=(-1)**sum(j<i for j in face)
            result[shift(pos,i,1 if adjoint else -1),target]+=sign*value
            result[pos,target]-=sign*value
    return nonzero(result)


def heat_step(field):
    out=Counter()
    for (pos,face),value in field.items():
        out[pos,face]+=8*value
        for i in range(4):
            out[shift(pos,i,1),face]+=value
            out[shift(pos,i,-1),face]+=value
    return nonzero(out)


def coefficients(R):
    """Integer numerator of a normalized fourfold box spline on the line."""
    coeff={0:1}
    for _ in range(4):
        out=Counter()
        for x,v in coeff.items():
            for a in range(R):
                out[x+a]+=v
        coeff=out
    return coeff


def field_at(R,time=0):
    a=coefficients(R)
    # The common denominator R^10 includes the R² amplitude in three dimensions.
    assert sum(a.values())==R**4
    out=Counter()
    for x,y,z in product(a,repeat=3):
        value=a[x]*a[y]*a[z]
        for j in range(4):
            out[(time,x,y,z+j*R),(1,2)]+=(-1)**(3-j)*comb(3,j)*value
    field=nonzero(out)
    assert all(sum(n*pos[3]**d for (pos,_),n in field.items())==0 for d in range(3))
    # The third moment measures the first surviving cancellation order.
    assert sum(n*pos[3]**3 for (pos,_),n in field.items())==6*R**15
    return field


def norms(field):
    return (sum(abs(x) for x in field.values()),max((abs(x) for x in field.values()),default=0),
            sum((1+sum(map(abs,pos[1:])))*abs(v) for (pos,_),v in field.items()))


def decompose(R,M):
    g=field_at(R)
    rem=g
    partial={}
    for ell in range(M):
        partial=Counter(heat_step(partial))
        partial.update({key:16**ell*value for key,value in g.items()})
        rem=heat_step(rem)
    h=cochain_diff(partial,True)
    k=cochain_diff(partial,False)
    u=cochain_diff(h,False)
    assert {f for _,f in h} <= {(1,),(2,)} and h
    rebuilt=Counter(u)
    rebuilt.update(cochain_diff(k,True))
    rebuilt.update(rem)
    assert nonzero(rebuilt)=={key:16**M*value for key,value in g.items()}
    for q in (h,k,u):
        translated={(shift(pos,0,997),face):value for (pos,face),value in q.items()}
        assert norms(q)==norms(translated)
    return len(g)


def run():
    for N in range(65):
        coeff={j:comb(2*N,N+j) for j in range(-N,N+1)}
        differences={j:abs(coeff.get(j,0)-coeff.get(j-1,0)) for j in range(-N,N+2)}
        assert sum(differences.values())==2*coeff[0]
        assert sum(abs(j)*v for j,v in differences.items())==4**N
    supports=[decompose(r,m) for r,m in ((1,3),(2,4),(3,2))]
    return {"exact_binomial_first_moments":65,"hodge_examples":3,
            "face_support_sizes":supports,"only_spatial_potential":True}
