"""Enclose the isolated vacuum tensor line at one site, beta=4."""
import sys
from fractions import Fraction as F
from math import factorial
from pathlib import Path

import numpy as np
from scipy.linalg import eigh

sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
import certify as c
from enclosure import I, mat, stack
from spectrum import states


def chebyshev_error(half_range, degree):
    """Two positive integration rules, each with its own uniform tail allowance."""
    z = F(half_range,2)
    n = degree+1
    exponent = half_range-z*z/(n+1)
    assert exponent>0 and z<n+1
    exp_lower = sum(exponent**j/factorial(j) for j in range(60))
    return I.rational(4*z**n/(factorial(n)*exp_lower*(1-z/(n+1))))


def eigenvalue_cap(M,Q,rank,eta):
    """Min-max on a trial subspace of codimension rank-1."""
    S = I(Q[:,:Q.shape[0]-rank+1].copy())
    gram = mat(S.T,S)-I(np.eye(S.lo.shape[1]))
    defect = I(c.rowsum(c.upper_abs(gram)))
    assert defect.hi<1
    block = mat(S.T,mat(M,S))
    return I(c.rowsum(c.upper_abs(block)))/(1-defect)+eta


def magnitude(v):
    return I(c.norm(v))


def trial(M,H,q,a,kin,eta,eta2):
    # All denominators refer to this same, possibly nonunit, q.
    q2 = c.quad(q,I(np.eye(q.lo.shape[0])),q)
    qnorm = magnitude(q)
    quad = c.quad(q,M,q)
    length2 = I((quad-eta*q2).lo,(quad+eta*q2).hi)
    assert length2.lo>0
    length = length2.sqrt()
    action = mat(M,q)
    residual = magnitude(action-a*q)+eta*qnorm
    # P A² sqrt(K) q is K_P^(-1/2) Mq. Enclose its norm from below.
    captured = action/kin
    abs_lower = np.maximum(0,np.maximum(captured.lo,-captured.hi)).reshape(-1,1)
    norm2_lower = mat(I(abs_lower.T),I(abs_lower))[0,0]
    assert norm2_lower.lo>0
    retained = norm2_lower.sqrt() - eta*qnorm/I(float(kin.lo.min()))
    assert retained.lo>0
    tail = I.rational(F(".00022"))
    defect = c.quad(q,H,q)+eta2*q2 - I(retained.lo).square()
    assert defect.hi>0
    shift = I((tail*defect/length2).hi)
    # Cauchy-Schwarz lower bound and the variance identity for the finite Rayleigh quotient.
    finite_lower = (length2/q2).lo
    finite_upper = (length2/q2 + residual.square()/length2).hi
    mu = I(finite_lower,(I(finite_upper)+shift).hi)
    sd = I.rational(F(".23"))*residual/length + (tail*shift).sqrt()
    print(f"trial {float(a.lo):.7f}: omitted mean < {shift.hi:.9g}, SD < {sd.hi:.9g}",flush=True)
    return mu, I(sd.square().hi)


def exp_bounds(x):
    # x is a positive rational below two. Bound the tail by a geometric series.
    assert 0<x<2
    terms = [x**j/factorial(j) for j in range(31)]
    lower = sum(terms)
    return lower,lower+terms[-1]*x/31/(1-x/32)


def scalar_trials(basis,M,eta):
    # Radial-only product states have l=(0,0,0). Summing an orbit fixes all permutations.
    keys = sorted({tuple(sorted(ns)) for ns,ls,_ in basis if ls==(0,0,0)})
    S = np.array([[float(ls==(0,0,0) and tuple(sorted(ns))==key) for key in keys]
                  for ns,ls,_ in basis])
    S /= np.sqrt(S.sum(axis=0))
    rotated = eigh(S.T@((M.lo+M.hi)/2)@S)[1][:,-2:]
    # Round to dyadic orbit coefficients. Equal rows stay exactly equal.
    rows = np.rint(1024*(S@rotated))/1024
    for key in keys:
        orbit=[i for i,(ns,ls,_) in enumerate(basis) if ls==(0,0,0) and tuple(sorted(ns))==key]
        assert np.all(rows[orbit]==rows[orbit[0]])
    V=I(rows)
    gram=mat(V.T,V)
    form=mat(V.T,mat(M,V))-(I.rational(F(".013"))+eta)*gram
    det=form[0,0]*form[1,1]-form[0,1].square()
    assert form[0,0].lo>0 and det.lo>0
    print("two invariant radial trials above .013; determinant lower",float(det.lo),flush=True)


def certify_line(basis,kin,M,H):
    rational = lambda value:I.rational(F(value))
    eta,eta2 = chebyshev_error(12,18),chebyshev_error(24,25)
    Q = eigh((M.lo+M.hi)/2)[1]
    caps = {r:eigenvalue_cap(M,Q,r,eta)+rational(".00022") for r in (4,5)}
    print("fourth/fifth upper",*(float(v.hi) for v in caps.values()),flush=True)
    assert caps[4].hi < (rational(".0526")/3).lo
    assert caps[5].hi < rational(".0077").lo
    scalar_trials(basis,M,eta)
    roots = stack([kin[ns] for ns,_,_ in basis]).reshape(-1,1)
    m0,v0 = trial(M,H,I(Q[:,-1,None].copy()),rational(".0526954"),roots,eta,eta2)
    mE,vE = trial(M,H,I(Q[:,-2,None].copy()),rational(".0199955"),roots,eta,eta2)
    lower_E = I(caps[4].hi)
    upper_E = rational(".0526")
    upper_excited = rational(".02062")
    assert m0.lo>upper_excited.hi and lower_E.hi<mE.lo<=mE.hi<upper_E.lo
    # Temple at the top and Kato-Temple on the isolated doublet.
    vac = I(m0.lo,(m0+v0/(m0-upper_excited)).hi)
    line = I((mE-vE/(upper_E-mE)).lo,(mE+vE/(mE-lower_E)).hi)
    ms,vs = trial(M,H,I(Q[:,-4,None].copy()),rational(".0161245"),roots,eta,eta2)
    assert caps[5].hi<ms.lo<=ms.hi<line.lo
    scalar = I((ms-vs/(I(line.lo)-ms)).lo,(ms+vs/(ms-I(caps[5].hi))).hi)
    scalar_ratio = vac/scalar
    scalar_lo = F.from_float(float(scalar_ratio.lo))
    scalar_hi = F.from_float(float(scalar_ratio.hi))
    print("scalar",scalar.lo,scalar.hi,"mass ratio",float(scalar_lo),float(scalar_hi),flush=True)
    assert exp_bounds(F("1.1830"))[1]<scalar_lo<=scalar_hi<exp_bounds(F("1.1847"))[0]
    ratio = vac/line
    print("vacuum",vac.lo,vac.hi,"tensor",line.lo,line.hi,"mass ratio",ratio.lo,ratio.hi,flush=True)

    # Verify logarithmic bounds by rational Taylor enclosures, without a floating-point logarithm.
    ratio_lo = F.from_float(float(ratio.lo))
    ratio_hi = F.from_float(float(ratio.hi))
    lower,upper = F(".9681"),F(".9694")
    assert exp_bounds(lower)[1]<ratio_lo<=ratio_hi<exp_bounds(upper)[0]
    print("energy",float(lower),float(upper),flush=True)

    rel = F.from_float(float((caps[5]/line).hi))
    assert 0<rel<F(39,100)
    # The 88.8% lower bound on equal-time weight was established by the parent audit.
    odds = (1-F(".888"))/F(".888")
    for t in (0,1,2,4,8):
        remaining = odds*rel**t
        print("lag",t,"minimum line fraction",float(1/(1+remaining)),
              "maximum effective-energy excess",float(remaining),flush=True)
    assert 1/(1+odds*rel**4)>F(".9972")
    assert odds*rel**8<F(".000059")
    signed_period48(vac,line)


def signed_period48(vac,line):
    # Decimal inputs here are the outward endpoints of C4's period-48 certificate.
    v = F.from_float(float(vac.lo))
    x = F.from_float(float(line.lo))/F.from_float(float(vac.hi))
    y = F.from_float(float(line.hi))/v
    assert F(1,3)<x<y<1
    z = 1 + sum(mult*(F(top)/v)**48 for mult,top in
                ((3,".0495658"),(3,".0464010"),(1,".0431873")))
    z += 1402*(F(".020764")/v)**47
    kernel = (x-y**44)*(1-y)*(3-y)*(x-F(1,3))
    doublet = F(".0736")*kernel/z
    share = doublet/(doublet+F(".000391"))
    assert doublet>F(".001789") and share>F(".8206")
    print("signed period-48 doublet contribution lower",float(doublet),
          "signed share lower",float(share),flush=True)


def main():
    if not __debug__:
        raise RuntimeError("enable Python assertions")
    np.seterr(over="raise",invalid="raise",divide="raise")
    even=states((0,0,0),float(c.CUTOFF))
    kinetics=c.verify_selection((0,0,0),even)
    assert 2*max(max(ns) for ns,_,_ in even)+2*25<=2*c.ORDER-1
    assert 2*max(max(ls) for _,ls,_ in even)+2*25<=2*c.ORDER-1
    regular,=c.interval_matrices([even],[kinetics])
    squared,=c.interval_matrices([even],[kinetics],squared_weight=True)
    certify_line(even,kinetics,regular[0],squared[0])


if __name__=="__main__":
    main()
