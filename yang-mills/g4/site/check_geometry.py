"""Independent exact finite controls, not proofs of a continuum gauge theory."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations,product
from math import prod
import json

def reflected_cells():
    cases=0;largest=0;witness=None
    boxes=list(product((3,4,5,7),repeat=4))+[(5,7,11,12),(16,19,18,32)]
    for lengths in boxes:
        for orient in combinations(range(4),2):
            cube=frozenset(product((0,1),repeat=4))
            face=frozenset(v for v in cube if all(v[a]==0 for a in range(4) if a not in orient))
            cells=[(cube,face)];width=[1]*4
            for axis in range(4):
                while 4*width[axis]<=lengths[axis]:
                    plane=width[axis]
                    def reflect(vertices):
                        return frozenset(tuple(2*plane-x if a==axis else x for a,x in enumerate(v)) for v in vertices)
                    cells+= [(reflect(c),reflect(f)) for c,f in cells]
                    width[axis]*=2
            counts=Counter(f for c,f in cells)
            assert len({c for c,f in cells})==len(cells)==prod(width)
            assert all(f<=c for c,f in cells)
            assert all(4*w>L and 2*w<=L for w,L in zip(width,lengths))
            assert 256*len(cells)>prod(lengths)
            assert all(0<=v[a]<=width[a]<lengths[a] for c,f in cells for v in c for a in range(4))
            overlap=max(counts.values());assert overlap<=4
            if overlap>largest:largest=overlap;witness={'lengths':lengths,'orientation':orient}
            cases+=1
    assert largest==4  # Rejects the stronger, false bound three.
    return {'cases':cases,'max_overlap':largest,'bound_three_rejected_by':witness}

def matmul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def odd_seam():
    states=list(product((-1,1),repeat=3));n=len(states)
    index={s:i for i,s in enumerate(states)}
    Pi=[[F(0) for _ in states] for _ in states]
    for i,s in enumerate(states):
        for g in states:
            t=tuple(g[a]*s[a]*g[(a+1)%3] for a in range(3))
            Pi[i][index[t]]+=F(1,n)
    K=[[prod(F(2) if a==b else F(1,2) for a,b in zip(s,t)) for t in states] for s in states]
    KP=matmul(K,Pi)
    assert KP==matmul(Pi,K)==matmul(Pi,KP) and matmul(Pi,Pi)==Pi and K!=KP
    # Exact Walsh Gram expansion; vertex projection keeps the empty/full cycles.
    coeff=[F(5,4)**3,F(3,4)**3]
    chars=[[1,prod(s)] for s in states]
    assert KP==[[sum(coeff[j]*chars[x][j]*chars[y][j] for j in range(2)) for y in range(n)] for x in range(n)]
    M=[F(2) if prod(s)==1 else F(1,2) for s in states]
    T=[[M[x]*KP[x][y]*M[y] for y in range(n)] for x in range(n)]
    # Test depends on shared slice x and need not be gauge invariant in y.
    f=[[F(((7*x+3*y+x*y)%13)-6,5) for y in range(n)] for x in range(n)]
    odd=sum(T[x][y]*T[y][z]*T[z][x]*f[x][y]*f[x][z] for x in range(n) for y in range(n) for z in range(n))
    gram=sum(coeff[j]*sum(T[x][y]*f[x][y]*M[y]*chars[y][j] for y in range(n))**2 for x in range(n) for j in range(2))
    assert odd==gram and odd>0
    return {'odd_form':str(odd),'gram_form':str(gram),'projector_omission_changes_kernel':K!=KP,'arithmetic':'exact rational'}

def boundary_reweighting():
    # Two shared-boundary states, singleton fiber, exp(S)=1 or 3; P=0 or 1.
    masses=[F(1,2),F(1,2)];Z=[F(1),F(3)];P=[F(0),F(1)]
    total=sum(m*z for m,z in zip(masses,Z))
    density=[z/total for z in Z]
    normalized=sum(m*d*p for m,d,p in zip(masses,density,P))
    wrong=sum(m*p for m,p in zip(masses,P))
    assert sum(m*d for m,d in zip(masses,density))==1
    assert normalized==F(3,4) and wrong==F(1,2) and normalized!=wrong
    return {'correct_expectation':str(normalized),'unweighted_expectation':str(wrong)}

if __name__=='__main__':
    print(json.dumps({'geometry':reflected_cells(),'odd_seam':odd_seam(),'boundary':boundary_reweighting()},indent=2))
