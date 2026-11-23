"""Enclose the static floor and the finite-period midpoint of the one-site tensor trace."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import eigh

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import certify as cert
from enclosure import I, mat, stack
from exterior import exterior_bounds
from contrast import MULTIPLICITIES, SECTORS

CUTOFF = cert.CUTOFF


def quadrature_errors():
    # Positive exponential partial sums certify e^10>20000 and e^18>60000000.
    for exponent,lower in [(10,20000),(18,60000000)]:
        assert sum(F(exponent**j,factorial(j)) for j in range(60))>lower
    limits=[]
    for radius,degree,exp_lower in [(12,18,20000),(24,23,60000000)]:
        next_index=degree+1
        assert F(-radius)+F(radius**2,4*(degree+2)) <= (-10 if degree==18 else -18)
        t=F(radius,2)
        # Twice the uniform geometric tail bounds the quadrature-to-Haar error.
        limits.append(I.rational(4*t**next_index /
                                 (exp_lower*factorial(next_index)*(1-t/(degree+2)))))
    return limits


def lower_norm(vec):
    values=np.maximum(0,np.maximum(vec.lo,-vec.hi))
    col=I(values.reshape(-1,1))
    lower=max(0.0,mat(col.T,col).lo.item())
    return max(0.0,I(lower).sqrt().lo.item())


def complement_upper(M, U, eta):
    defect=cert.rowsum(cert.upper_abs(mat(U.T,U)-I(np.eye(U.lo.shape[1]))))
    assert defect<1
    top_on_complement=cert.rowsum(cert.upper_abs(mat(U.T,mat(M,U))))
    return I(top_on_complement)/(1-I(defect))+eta+I.rational(CUTOFF)


def trial_bounds(basis, kin, M, G, v, a, eta, eta2):
    vnorm=I(cert.norm(v))
    norm2=mat(v.T,v)[0,0]
    mv=mat(M,v)
    N=mat(v.T,mv)[0,0]+I(-eta.hi,eta.hi)*norm2
    inv_sqrt=stack([I(1)/kin[ns] for ns,_,_ in basis]).reshape(-1,1)
    projected=I(lower_norm(inv_sqrt*mv))-eta*vnorm/I.rational(CUTOFF).sqrt()
    assert projected.lo>0
    full=cert.quad(v,G,v)+eta2*norm2
    tail=(full-projected.square())/N
    assert 0<=tail.hi
    loss=I(min(1.0,tail.hi.item()))
    residual=(I(cert.norm(mv-v*a))+eta*vnorm)/N.sqrt()+I.rational(CUTOFF)*loss.sqrt()
    Rlow=N/norm2
    Rhi=(I(cert.norm(mv))+eta*vnorm).square()/N+I.rational(CUTOFF)*loss
    return N,residual,Rlow,Rhi


def certify_ground(basis, kin, measured, squared, eta, eta2):
    M,J = measured[0],measured[1]
    vals,V = eigh((M.lo+M.hi)/2)
    rest=complement_upper(M,I(V[:,:-1]),eta)
    v,a=I(V[:,-1,None]),I(vals[-1])
    N,residual,Rlow,Rhi=trial_bounds(basis,kin,M,squared[0],v,a,eta,eta2)
    norm2=mat(v.T,v)[0,0]
    assert a.lo>rest.hi
    sine=residual/(a-rest)
    trial=cert.quad(v,J,v)/N+I(-eta.hi,eta.hi)*norm2/N
    shift=I(2).sqrt()*sine
    diag=trial+I(-shift.hi,shift.hi)

    # Temple bound on the simple top eigenvalue of the full symmetry block.
    assert Rlow.lo>rest.hi
    high=Rhi+residual.square()/(Rlow-rest)
    return I(Rlow.lo,high.hi),diag,rest.hi.item()


def center_bounds():
    bases=[cert.states(p,float(CUTOFF)) for p in SECTORS]
    kinetics=[cert.verify_selection(p,b) for p,b in zip(SECTORS,bases)]
    matrices=cert.interval_matrices(bases,kinetics,include_square=True,include_average=True)
    squares=cert.interval_matrices(bases,kinetics,squared_weight=True)
    values=summarize(bases,kinetics,matrices,squares)
    blocks=[(b,k,m,g[0]) for b,k,m,g in zip(bases,kinetics,matrices,squares)]
    return values,blocks


def summarize(bases,kinetics,matrices,squares):
    eta,eta2=quadrature_errors()
    values=[]
    for p,b,k,m,g in zip(SECTORS,bases,kinetics,matrices,squares):
        lam,diag,rest=certify_ground(b,k,m,g,eta,eta2)
        print(f"{p} lambda [{lam.lo:.10f},{lam.hi:.10f}] "
              f"diagonal [{diag.lo:+.8f},{diag.hi:+.8f}] second <= {rest:.8f}")
        values.append((lam,diag,rest))
    return values


def bounds(values, exterior, T):
    vacuum=values[0][0]
    ratios=[I(1)]+[lam/vacuum for lam,_,_ in values[1:]]
    second=max(rest for _,_,rest in values)
    h=I(max(second,exterior))/I(vacuum.lo)
    # Unnormalized in units of lambda_vac^T.
    tail=1402*h**(T-1)
    z8=sum(mult*r**T for mult,r in zip(MULTIPLICITIES,ratios))
    Z=z8+I(0,tail.hi)
    terms=[2*ratios[k]**T*values[k][1].square() for k in (1,2)]
    static=sum(terms)/Z
    rest_floor=tail/(2*I(z8.lo))
    across=(I(second)/I(vacuum.lo))**(T//2)*sum(
        mult*r**(T//2) for mult,r in zip(MULTIPLICITIES,ratios))/I(z8.lo)
    remainder=rest_floor+across
    midpoint=static+I(0,remainder.hi)
    share=I(static.lo)/(I(static.lo)+I(remainder.hi))
    print(f"T={T}: Z/lambda0^T [{Z.lo:.9f},{Z.hi:.9f}], "
          f"eight-state static [{static.lo:.9f},{static.hi:.9f}], "
          f"midpoint [{midpoint.lo:.9f},{midpoint.hi:.9f}], "
          f"midpoint excess <= {remainder.hi:.5g}, static share >= {share.lo:.9f}")
    return static,midpoint,remainder,share,Z


def full_gap(values, exterior):
    # Only the three images of the single-odd top remain at the first excited level.
    roots=[row[0] for row in values]
    assert all(roots[k].lo>roots[k+1].hi for k in range(3))
    assert min(float(x.lo) for x in roots)>max(exterior,max(row[2] for row in values))
    ratio=roots[0]/roots[1]
    x,y=F(61,1000),F(63,1000)
    exp_x_hi=sum(x**k/factorial(k) for k in range(20))+x**20/factorial(20)/(1-x/21)
    exp_y_lo=sum(y**k/factorial(k) for k in range(20))
    assert exp_x_hi<F.from_float(float(ratio.lo)) and F.from_float(float(ratio.hi))<exp_y_lo
    print("full one-site gap in (0.061,0.063), multiplicity three")


def period_ratio(values, results):
    """Keep the shared one-odd energy and common matrix elements in the ratio."""
    lam0,lam1,lam2=(s[0] for s in values[:3])
    static24,_,rem24,_,z24=results[24]
    static48,_,rem48,_,z48=results[48]
    v=(values[2][1]/values[1][1]).square()
    x=(lam2/lam1)**24
    correction=(1+v*x)/(1+v*x.square())*(z48/z24)
    correction*= (1+I(0,rem24.hi)/static24)/(1+I(0,rem48.hi)/static48)
    ratio=correction*(lam0/lam1)**24
    print(f"C24(12)/C48(24) [{ratio.lo:.7f},{ratio.hi:.7f}]")
    print(f"ratio times (lambda1/lambda0)^24 [{correction.lo:.7f},{correction.hi:.7f}]")
    assert F.from_float(float(correction.hi)) < F(9,10)
    return ratio


def kernel_range(low,high,T):
    # x^s plus the backward image for each of the four lags, including x=0.
    assert 0<=low<=high<1
    grid=np.linspace(low,high,2049)
    assert grid[0]==low and grid[-1]==high and np.all(np.diff(grid)>0)
    x=I(grid[:-1],grid[1:])
    c=I.rational(F(13,3))
    forward=x*(-1+x*(c+x*(-c+x)))
    backward=x**(T-4)*(1+x*(-c+x*(c-x)))
    value=forward+backward
    return I(value.lo.min(),value.hi.max())


def vacuum_contrast(basis,kin,measured,G,values,periods):
    M,J,J2=measured[0],measured[1],measured[2]
    eta,eta2=quadrature_errors()
    vals,V=eigh((M.lo+M.hi)/2)
    vacuum=values[0][0]
    second=I(values[0][2])
    fourth=complement_upper(M,I(V[:,:-3]),eta)
    Q=I(V[:,-3:])
    defect=cert.rowsum(cert.upper_abs(mat(Q.T,Q)-I(np.eye(3))))
    assert defect<1
    small=mat(Q.T,mat(M,Q))
    gersh=min((small[i,i]-sum(I(cert.upper_abs(small[i,j]))
                               for j in range(3) if j!=i)).lo for i in range(3))
    assert gersh>0
    third=I(gersh)/(1+I(defect))-eta
    assert fourth.hi<third.lo<=second.hi<vacuum.lo
    q0=I(V[:,-1,None])
    sub=V[:,-3:-1]
    vec=sub@(sub.T@((J.lo+J.hi)/2)@q0.lo)
    qE=I(vec/np.linalg.norm(vec))
    a0,aE=I(vals[-1]),I(vals[-2])
    n0,r0,_,_=trial_bounds(basis,kin,M,G,q0,a0,eta,eta2)
    nE,rE,_,_=trial_bounds(basis,kin,M,G,qE,aE,eta,eta2)
    sine0=r0/(a0-second)
    gap=min((aE-fourth).lo,(I(vacuum.lo)-aE).lo)
    assert gap>0
    sineE=rE/I(gap)
    # The spectral width of O^2 is at most 1/2.
    variance=(cert.quad(q0,J2,q0)+eta*I(cert.norm(q0)).square())/n0+sine0/2
    cross=cert.quad(qE,J,q0)
    assert cross.lo>0
    amp=(cross-eta*cert.norm(q0)*cert.norm(qE))/(n0*nE).sqrt()
    weight=(amp-sine0-sineE*I(variance.hi).sqrt())
    assert weight.lo>0
    weight=I(weight.lo).square()
    outside=I(variance.hi)-weight
    assert outside.hi>=0
    xlow=(third/I(vacuum.hi)).lo
    xhigh=(second/I(vacuum.lo)).hi
    other=(fourth/I(vacuum.lo)).hi
    print(f"neutral levels 2,3 transfer ratios [{xlow:.8f},{xhigh:.8f}]; others <= {other:.8f}")
    print(f"vacuum doublet-subspace weight >= {weight.lo:.7f}, total variance <= {variance.hi:.7f}")
    terms = {}
    for T,result in periods.items():
        Z=result[-1]
        band=kernel_range(xlow,xhigh,T)
        rest=kernel_range(0.0,other,T)
        assert band.lo>0
        lower=(weight*I(band.lo)+I(outside.hi)*min(0.0,rest.lo))/Z
        upper=(I(variance.hi)*max(band.hi,rest.hi))/Z
        assert lower.lo>0
        terms[T]=I(lower.lo,upper.hi)
        print(f"T={T}: signed vacuum pairs [{lower.lo:.9f},{upper.hi:.9f}]")
    return terms

def contrast_balance(blocks,values,periods,vacuum,exterior):
    eta,eta2=quadrature_errors()
    var=[]
    for (basis,k,m,g),(_,_,second) in zip(blocks[1:],values[1:]):
        M=m[0]
        vals,V=eigh((M.lo+M.hi)/2)
        v,a=I(V[:,-1,None]),I(vals[-1])
        n,residual,_,_=trial_bounds(basis,k,M,g,v,a,eta,eta2)
        sine=residual/(a-I(second))
        avg=(cert.quad(v,m[3],v)+eta*I(cert.norm(v)).square())/n+sine/3
        var.append(I(avg.hi))
    for T,result in periods.items():
        Z=result[-1]
        top=I(0)
        for ((lam,_,second),avg,mult) in zip(values[1:],var,MULTIPLICITIES[1:]):
            hi=(I(second)/lam).hi
            kernel=kernel_range(0.0,hi,T)
            occ=mult*(lam/values[0][0])**T/Z
            top+=occ*avg*I(min(0.0,kernel.lo),max(0.0,kernel.hi))
        rest=max(exterior,max(x[2] for x in values))
        pob=1402*(I(rest)/values[0][0])**(T-1)/Z
        error=(I.rational(F(32,9))*pob).hi
        thermal=top+I(-error,error)
        total=vacuum[T]+thermal
        if total.lo>0:
            share=(I(vacuum[T].lo)/(I(vacuum[T].lo)+I(max(0.,thermal.hi)))).lo
            share_text=f">= {share:.7f}"
        else:
            share_text="unresolved"
        print(f"T={T}: signed excited pairs [{thermal.lo:+.8f},{thermal.hi:+.8f}], "
              f"total W [{total.lo:+.8f},{total.hi:+.8f}], vacuum signed share {share_text}")
        if T==48:
            assert total.lo>0 and F.from_float(float(share))>F(74,100)
            assert F.from_float(float(thermal.hi))<F(391,1000000)
            assert F.from_float(float(vacuum[T].lo))>F(1132,1000000)


def main():
    if not __debug__:
        raise RuntimeError("validation requires assertions enabled")
    np.seterr(over="raise", invalid="raise", divide="raise")
    limits=exterior_bounds()
    assert len(limits)==16 and max(limits.values())<0.021
    print(f"inversion-odd largest upper {max(limits.values()):.9f}")
    values,blocks=center_bounds()
    full_gap(values,max(limits.values()))
    results={T:bounds(values,max(limits.values()),T) for T in (16,24,48)}
    static,midpoint,remainder,share,_=results[48]
    assert F.from_float(float(static.lo))>F(250,1000000)
    assert F.from_float(float(midpoint.hi))<F(335,1000000)
    assert F.from_float(float(share.lo))>F(999999,1000000)
    assert F.from_float(float(results[24][3].lo))>F(976,1000)
    period_ratio(values, results)
    vacuum=vacuum_contrast(*blocks[0],values,results)
    contrast_balance(blocks,values,results,vacuum,max(limits.values()))


if __name__=="__main__":
    main()
