"""Exact strip coefficients, a bracket for the first dispersion root, and spatial transfer tests."""
from fractions import Fraction as Q
from math import factorial, log, sqrt, exp
from pathlib import Path
import json
import runpy

import numpy as np


def strip_recurrence(n):
    h,ordered = [Q(1)], [Q(1)]
    for k in range(1,n+1):
        h.append(sum(h[j]*h[k-1-j] for j in range(k))/(2*(k+1)))
        ordered.append(sum(h[j]*ordered[k-j] for j in range(1,k+1)))
    return [Q(1)]+[2*x for x in ordered[1:]]


def bessel_quotient(n):
    # Coefficient arrays of J1(sqrt(2z))/sqrt(2z) and J1'(sqrt(2z)).
    top=[Q((-1)**k,2**(k+1)*factorial(k)*factorial(k+1)) for k in range(n+1)]
    bottom=[(2*k+1)*x for k,x in enumerate(top)]
    quotient=[]
    for k in range(n+1):
        quotient.append((top[k]-sum(bottom[i]*quotient[k-i] for i in range(1,k+1)))/bottom[0])
    return quotient


def derivative_interval(x):
    terms=[Q((2*k+1)*(-1)**k,2**(2*k+1)*factorial(k)*factorial(k+1))*x**(2*k)
           for k in range(26)]
    assert 0<x<2 and all(abs(b)<abs(a) for a,b in zip(terms[1:],terms[2:]))
    return sum(terms),sum(terms[:-1])


def transfer(epsilon, radius=8):
    cutoff=round(radius/epsilon)
    sites=np.arange(-cutoff,cutoff+1)
    q=exp(-epsilon)
    K=epsilon*q**(np.abs(sites[:,None])+np.abs(sites[None,:]-sites[:,None])+np.abs(sites[None,:]))
    v=np.exp(-epsilon*np.abs(sites))
    for _ in range(35):
        nxt=K@v
        v=nxt/np.linalg.norm(nxt)
    ratios=(K@v)/v
    largest=float(v@(K@v))
    assert np.min(ratios)<=largest+1e-13 and np.max(ratios)>=largest-1e-13
    assert np.ptp(ratios)<1e-12
    mass=(1+q**2)/(1-q**2)
    tail=2*q**(2*(cutoff+1))/(1-q**2)
    return largest,epsilon*sqrt(2*mass*tail)


def run():
    base=runpy.run_path(str(Path(__file__).resolve().parent.parent/"all-readings/sheet.py"))
    coef=strip_recurrence(40)
    assert coef==bessel_quotient(40) and coef[:3]==[1,Q(1,2),Q(7,24)]
    e4,e6=6,9  # Fundamental square and two-tile rectangle at kappa=1.
    assert coef[1]/6==Q(1,2*e4)
    assert coef[2]/6**2==Q(1,4*e4*e6)+Q(1,8*e4**2)
    for n in range(1,10):
        perimeter=base["perimeters"](n,1)
        assert base["heights"](perimeter,Q(1,2))[1]==coef[n]
    lo,hi=Q(184118378134065,10**14),Q(184118378134067,10**14)
    assert derivative_interval(lo)[0]>0 and derivative_interval(hi)[1]<0
    root=float((lo+hi)/2)
    growth=2/root**2
    prefactor=2/(root**2-1)
    assert abs(float(coef[40])/growth**40-prefactor)<1e-12
    table=[]
    for eps in (.4,.2,.1,.05,.025):
        largest,tail=transfer(eps)
        assert largest>growth*exp(-2*eps)-tail and largest<growth*exp(2*eps)
        table.append({"epsilon":eps,"scaled_truncated_eigenvalue":largest,"tail_norm_upper":tail})
    errors=[abs(row["scaled_truncated_eigenvalue"]-growth) for row in table]
    assert all(b<a for a,b in zip(errors,errors[1:])) and errors[-1]<.0004
    examples=[]
    for width,height in ((1,6),(2,2),(3,2),(3,3)):
        p=base["perimeters"](width,height)
        for q in (Q(1,2),Q(9,10),Q(99,100)):
            z,c=base["heights"](p,q)
            m=width*height
            eps=-log(float(q))
            delta=log(eps)+(log(z.numerator)-log(z.denominator)-log(float(c)))/m
            assert abs(delta)<=2*eps and c<=1 and z<=((1+q*q)/(1-q*q))**m
            examples.append(dict(shape=[width,height],q=str(q),per_tile_log_difference=delta))
    # The pointwise exponent constant is attained in the limit from inside a zero-centered cell.
    for width,height in ((1,1),(1,5),(2,3),(3,3)):
        m=width*height
        inside=(width-1)*height+(height-1)*width
        outer=2*(width+height)
        amplitude=Q(499,1000)
        assert amplitude*(2*inside+outer)/m==4*amplitude>Q(199,100)
    return dict(exact_series_terms=len(coef),subset_checks=9,root_bracket=[str(lo),str(hi)],
                growth=growth,prefactor=prefactor,spatial_transfer=table,
                cubature=examples,strip_C4=str(coef[4]))


if __name__=="__main__":
    print(json.dumps(run(),indent=2))
