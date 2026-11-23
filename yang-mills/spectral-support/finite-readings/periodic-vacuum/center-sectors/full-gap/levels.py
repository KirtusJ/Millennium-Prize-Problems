"""Enclose the extremal eigenvalue in the two required folded Wilson sectors."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import sys
import numpy as np
from scipy.linalg import eigh

sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from certify import (CUTOFF, I, interval_matrices, mat, quad, rowsum, states,
                     upper_abs, verify_selection)


def enclose(m,eta,neutral):
    size=len(m.lo)
    _,vectors=eigh((m.lo+m.hi)/2)
    highest=I(vectors[:,-1,None].copy())
    ident=I(np.eye(size))
    lower=(quad(highest,m,highest)/quad(highest,ident,highest)-eta).lo.item()
    upper=[]
    for n in ((size,size-1,size-3) if neutral else (size,)):
        test=I(vectors[:,:n].copy())
        defect=rowsum(upper_abs(mat(test.T,test)-I(np.eye(n))))
        assert defect<1
        q=mat(test.T,mat(m,test))
        upper.append((I(rowsum(upper_abs(q)))/(1-I(defect))+eta+I.rational(CUTOFF)).hi.item())
    endpoints=list(map(F.from_float,(lower,*upper)))
    if neutral:
        # Min-max lower bound for the third eigenvalue from a three-column trial space.
        top=I(vectors[:,-3:].copy())
        d=rowsum(upper_abs(mat(top.T,top)-I(np.eye(3))))
        assert d<1
        q=mat(top.T,mat(m,top))
        diagonal=I(np.diag(q.lo),np.diag(q.hi))
        off=upper_abs(q)
        np.fill_diagonal(off,0)
        smallest=(I(diagonal.lo.min())-rowsum(off))/(1+I(d))-eta
        endpoints.append(F.from_float(smallest.lo.item()))
    return endpoints


def exp_bounds(x):
    terms=[x**n/factorial(n) for n in range(24)]
    lo=sum(terms)
    return lo,lo+x**24/factorial(24)/(1-x/25)


if __name__=="__main__":
    if not __debug__:
        raise RuntimeError("run with assertions enabled")
    np.seterr(over="raise",invalid="raise",divide="raise")
    groups=[(0,0,0),(1,0,0)]
    bases=[states(p,float(CUTOFF)) for p in groups]
    weights=[verify_selection(p,b) for p,b in zip(groups,bases)]
    # Uniform Haar-versus-quadrature estimate from the parent calculation.
    err=F(2,20000)*F(6**19,factorial(19))/(1-F(6,20))
    matrices=interval_matrices(bases,weights)
    (v_lo,v_hi,e_hi,fourth_hi,e_lo)=enclose(matrices[0][0],I.rational(2*err),True)
    o_lo,o_hi=enclose(matrices[1][0],I.rational(2*err),False)
    print(f"vacuum top: {float(v_lo):.9f} .. {float(v_hi):.9f}; "
          f"one odd top: {float(o_lo):.9f} .. {float(o_hi):.9f}")
    print(f"neutral inversion-even second and third: {float(e_lo):.9f} .. {float(e_hi):.9f}; "
          f"fourth <= {float(fourth_hi):.9f}")
    assert e_hi<F(207,10000) and e_lo>F(195,10000) and o_lo>F(494,10000)
    assert fourth_hi < v_lo/3 and v_hi/3 < e_lo <= e_hi < 3*v_lo/7
    for name,lo,hi,gmin,gmax in (
            ("full",o_lo,o_hi,F(543,10000),F(695,10000)),
            ("neutral",e_lo,e_hi,F(9499,10000),F(9772,10000))):
        print(f"{name} energy interval: {np.log(float(v_lo/hi)):.9f} .. {np.log(float(v_hi/lo)):.9f}")
        assert exp_bounds(gmin)[1]<v_lo/hi and v_hi/lo<exp_bounds(gmax)[0]
    assert fourth_hi < F(16503,10**6) and e_lo > F(19988,10**6)
    for t, bound in ((6,F(9615,10000)),(12,F(9875,10000))):
        fraction = 1/(1+F(112,888)*F(16503,19988)**t)
        assert fraction > bound
        print(f"vacuum correlator fraction at lag {t} > {float(bound):.4f}")
