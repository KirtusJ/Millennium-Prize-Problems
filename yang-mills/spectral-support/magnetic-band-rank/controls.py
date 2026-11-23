"""Exact moment witnesses and quadrature for a compact smooth magnetic profile."""
from fractions import Fraction as F
import json
import math
from pathlib import Path

import numpy as np
from scipy.special import roots_genlaguerre, roots_legendre


def determinant(a):
    if len(a)==1:
        return a[0][0]
    return sum((-1)**j*v*determinant([row[:j]+row[j+1:] for row in a[1:]])
               for j,v in enumerate(a[0]))


def moment_checks():
    lower,upper=F(1,1024),F(1,2)
    limit=[F(1,(j+1)**8) for j in range(7)]
    def matrix(m):
        return [[-m[i+j+2]+(lower+upper)*m[i+j+1]-lower*upper*m[i+j]
                 for j in range(3)] for i in range(3)]
    G=matrix(limit)
    gap=F(1,70000000)
    shifted=[[g-gap*(i==j) for j,g in enumerate(row)] for i,row in enumerate(G)]
    minors=[determinant([row[:k] for row in shifted[:k]]) for k in (1,2,3)]
    l1=1+lower+upper+lower*upper
    allowance=3*l1*F(1,400000000)
    if min(minors)<=0 or allowance>=gap:
        raise AssertionError("exact matrix margin")
    # Two in-band energies and a heavy exterior atom: its annihilator must be negative.
    atoms=[(F(1,32),F(2,10)),(F(1,4),F(4,10)),(F(3,4),F(4,10))]
    G2=matrix([sum(w*x**j for x,w in atoms) for j in range(7)])
    poly=[atoms[0][0]*atoms[1][0],-atoms[0][0]-atoms[1][0],F(1)]
    quadratic=sum(v*w*G2[i][j] for i,v in enumerate(poly) for j,w in enumerate(poly))
    explicit=sum(weight*(x-lower)*(upper-x)*(x-atoms[0][0])**2*(x-atoms[1][0])**2
                 for x,weight in atoms)
    if quadratic!=explicit or quadratic>=0:
        raise AssertionError("two-energy rejection")
    epsilon=F(1,12800000)
    bump_error=((1-epsilon)**-2-1)/256
    if bump_error>=F(1,1000000000):
        raise AssertionError("uniform profile bound")
    return {"interval":[str(lower),str(upper)],"matrix_min_eigenvalue_numeric":float(np.linalg.eigvalsh(np.array(G,float))[0]),
            "shifted_leading_minors":[str(v) for v in minors],
            "error_budget":str(allowance),"strict_margin_after_error":str(gap-allowance),
            "two_atom_polynomial_quadratic":str(quadratic),
            "profile_error_at_16000_radii":float(bump_error)}


def bump_moments(nr,nu,T):
    r,w=roots_legendre(nr); r=(r+1)/2
    radial=w*r*r*np.exp(-1/(1-r*r))
    radial/=radial.sum()
    u,laguerre=roots_genlaguerre(nu,3)
    def scaled_C(t):
        fourier=np.sinc(np.outer(u/t,r)/np.pi)@radial
        return (laguerre@(fourier*fourier))/6
    c=scaled_C(T)
    return np.array([(scaled_C((j+1)*T)/c)**2/(j+1)**8 for j in range(7)])


def run(out: Path):
    exact=moment_checks()
    rows=[]
    j=np.arange(7,dtype=float)
    for T in (1,4,64,1024,16000):
        vals=bump_moments(100,64,T)
        check=bump_moments(160,96,T)
        err=float(max(abs(vals-check)))
        if err>1e-10:
            raise AssertionError(("radial quadrature",T,err))
        rows.append({"time_in_support_radii":T,"max_difference_from_universal_moments":float(max(abs(check-(1+j)**-8))),
                     "quadrature_change":err})
    if rows[-1]["max_difference_from_universal_moments"]>=exact["profile_error_at_16000_radii"]:
        raise AssertionError("profile radius inequality")
    (out/"checks.json").write_text(json.dumps({"exact":exact,"bump":rows},indent=2)+'\n')
    lower,upper=map(F,exact["interval"])
    l1=1+lower+upper+lower*upper
    (out/"geometry").write_text(f"theorem sevenReadings : (3:ℝ)*({l1.numerator}/{l1.denominator})*(1/400000000) < margin := by norm_num [margin]\n")
    (out/"counts.bin").write_bytes(bytes([lower.denominator.bit_length()-1,
                                         upper.denominator.bit_length()-1,8]))
