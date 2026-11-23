"""Validate the fixed beta=4 cutoff and vacuum/center-odd tests using outward enclosures."""
from fractions import Fraction as F
from functools import lru_cache
import sys
from itertools import product
from math import factorial
import numpy as np
from scipy.linalg import eigh
from enclosure import I, down, up, stack, mat, exp_negative
from spectrum import harmonics, states, moment

ORDER = 32
DEGREE = 18
CUTOFF = F(3,10000)
# Exact decimal/rational statements below use short outward dyadic comparisons or Fraction.
def brackets(lo,hi):
    return I(down(float(lo)),up(float(hi)))


def orth(family,n,x):
    a=F(1)
    if n==0:
        return a
    b=2*x if family=="U" else x
    for j in range(1,n):
        if family=="P":
            a,b=b,((2*j+1)*x*b-j*a)/(j+1)
        else:
            a,b=b,2*x*b-a
    return b


def rule(family):
    n=ORDER
    if family=="P":
        guesses=np.polynomial.legendre.leggauss(n)[0]
    elif family=="U":
        guesses=np.cos(np.pi*np.arange(1,n+1)/(n+1))
    else:
        guesses=np.cos(np.pi*(np.arange(n)+0.5)/n)
    roots,weights=[],[]
    last=F(-2)
    for g in sorted(guesses):
        if g<0 and family!="T":
            continue
        lo,hi=F(float(g))-F(1,2**40),F(float(g))+F(1,2**40)
        pos=orth(family,n,lo)>0
        assert (orth(family,n,hi)>0)!=pos and -1<lo and last<lo and hi<1
        for _ in range(48):
            mid=(lo+hi)/2
            if (orth(family,n,mid)>0)==pos:
                lo=mid
            else:
                hi=mid
        last=hi
        roots.append(brackets(lo,hi))
        if family=="T":
            w=I.rational(F(1,n))
        elif family=="U":
            w=brackets(4*(1-hi*hi)/(n+1),4*(1-lo*lo)/(n+1))
        else:
            # Markov's inequality, |P_(n-1)| <= 1 on [-1,1].
            val=abs(orth("P",n-1,(lo+hi)/2))
            err=(n-1)**2*(hi-lo)/2
            assert val>err
            w=brackets(2*(1-hi*hi)/(n*(val+err))**2,
                       2*(1-lo*lo)/(n*(val-err))**2)
        weights.append(w)
    assert len(roots)==(n if family=="T" else n//2)
    return stack(roots),stack(weights)


@lru_cache(None)
def bessel(n):
    term=F(2**n,factorial(n))
    s=term
    for k in range(1,32):
        term*=F(4,k*(n+k))
        s+=term
    rem=term*F(4,32*(n+32))*2
    return s,s+rem


def kinetic(n):
    a,b=bessel(n)
    c,d=bessel(1)
    return a/d,b/c


def verify_selection(parity,basis):
    weights={n:kinetic(n+1) for n in range(17)}
    assert weights[16][1]<CUTOFF and weights[0][0]<=1<=weights[0][1]
    chosen={tuple(zip(ns,ls)) for ns,ls,_ in basis}
    links=[[(n,l) for n in range(p,16,2) for l in range(0,n+1,2)] for p in parity]
    assert len(chosen) == len(basis)
    verified = set()
    ks={}
    for row in product(*links):
        ns,ls=zip(*row)
        if not abs(ls[0]-ls[1])<=ls[2]<=ls[0]+ls[1]:
            continue
        a,b,c=(weights[n] for n in ns)
        lo,hi=a[0]*b[0]*c[0],a[1]*b[1]*c[1]
        if row in chosen:
            assert lo>CUTOFF
            verified.add(row)
            ks[ns]=brackets(lo,hi).sqrt()
        else:
            assert hi<CUTOFF
    assert chosen == verified
    return ks


def cart(a,b,c):
    ix=np.indices((a.lo.size,b.lo.size,c.lo.size)).reshape(3,-1)
    return a[ix[0]],b[ix[1]],c[ix[2]]


def radial(n,l,x):
    a,b=I(np.ones_like(x.lo)),2*(l+1)*x
    for j in range(1,n-l):
        a,b=b,(2*(j+l+1)*x*b-(j+2*l+1)*a)/(j+1)
    g=a if n==l else b
    norm=F(factorial(n+l+1),4**l*factorial(n-l)*(n+1)*factorial(l)**2)
    return (1-x.square())**(l//2)*g/I.rational(norm).sqrt()


def interval_matrices(bases,kinetics):
    labels=sorted({ls for basis in bases for _,ls,_ in basis},key=lambda x:(sum(x),x))
    index={l:i for i,l in enumerate(labels)}
    max_n=max(max(ns) for basis in bases for ns,_,_ in basis)
    max_l=max(max(l) for l in labels)
    assert 2*max_n+2*DEGREE+2<=2*ORDER-1 and 2*max_l+2*DEGREE<=2*ORDER-1

    v,w=rule("P")
    z,wz=rule("T")
    x,y,z=cart(v,v,z)
    w1,w2,w3=cart(w,w,wz)
    cross=x*y+((1-x.square())*(1-y.square())).sqrt()*z
    angular=stack([1-x.square(),1-y.square(),1-cross.square()])
    shapes,norms=harmonics(labels)
    fields=[sum(I.rational(c)*(x**i)*(y**j)*(cross**k) for (i,j,k),c in f.items())
            /I.rational(norm).sqrt() for f,norm in zip(shapes,norms)]
    fields=stack(fields)
    ai,aj=np.tril_indices(len(labels))
    aw=(fields[ai]*fields[aj]*(w1*w2*w3)).T
    slots=np.empty((len(labels),len(labels)),dtype=int)
    slots[ai,aj]=slots[aj,ai]=np.arange(len(ai))

    v,w=rule("U")
    pts=cart(v,v,v)
    w1,w2,w3=cart(w,w,w)
    wr=(w1*w2*w3).sqrt()
    s=[1-x.square() for x in pts]
    pairs=stack([s[0]*s[1],s[0]*s[2],s[1]*s[2]],axis=1)
    lo=np.empty((len(wr.lo),len(ai)))
    hi=np.empty_like(lo)
    for start in range(0,len(lo),48):
        sl=slice(start,start+48)
        # Three outward elementwise products preserve the precision of the exponent.
        pot=sum(pairs[sl,i,None]*angular[i,None,:] for i in range(3))
        val=mat(exp_negative(-8*pot),aw)
        lo[sl],hi[sl]=val.lo,val.hi
    integral=I(lo,hi)
    obs=(s[0]-s[1])/I(2).sqrt()
    results=[]
    for basis,kin in zip(bases,kinetics):
        tags=np.array([index[ls] for _,ls,_ in basis])
        cache={(i,n,l):radial(n,l,pts[i]) for ns,ls,_ in basis
               for i,(n,l) in enumerate(zip(ns,ls))}
        radial_basis=stack([wr*kin[ns]*cache[0,ns[0],ls[0]]*cache[1,ns[1],ls[1]]
                            *cache[2,ns[2],ls[2]] for ns,ls,_ in basis])
        shape=(2,len(basis),len(basis))
        lower,upper=np.empty(shape),np.empty(shape)
        for i in np.unique(tags):
            rows=np.flatnonzero(tags==i)
            for j in np.unique(tags[tags<=i]):
                cols=np.flatnonzero(tags==j)
                block=integral[:,slots[i,j]]*radial_basis[rows]
                for k,fac in enumerate((1,obs)):
                    val=mat(block*fac,radial_basis[cols].T)
                    ij,ji=np.ix_(rows,cols),np.ix_(cols,rows)
                    lower[k][ij],upper[k][ij]=val.lo,val.hi
                    lower[k][ji],upper[k][ji]=val.lo.T,val.hi.T
        results.append(I(lower,upper))
    return results


def upper_abs(a):
    return np.maximum(abs(a.lo),abs(a.hi))


def rowsum(a):
    # Positive sum, each step rounded outward.
    s=np.zeros(a.shape[0])
    for col in a.T:
        s=up(s+col)
    return float(max(s))


def norm(a):
    magnitudes = I(upper_abs(a).reshape(-1, 1))
    squared = mat(magnitudes.T, magnitudes)
    return I(squared.hi).sqrt().hi.item()


def quad(v,M,w):
    return mat(v.T,mat(M,w))[0,0]


def check():
    if not __debug__:
        raise RuntimeError("validation requires Python assertions enabled")
    np.seterr(over="raise", invalid="raise", divide="raise")
    assert sys.float_info.radix == 2 and sys.float_info.mant_dig == 53
    assert np.finfo(np.float64).nmant == 52
    assert moment(2,0,0) == F(1,3) and moment(1,1,1) == F(1,9)
    parities=[(0,0,0),(1,0,0)]
    bases=[states(p,float(CUTOFF)) for p in parities]
    kinetics=[verify_selection(p,b) for p,b in zip(parities,bases)]
    (Ms,Mo)=interval_matrices(bases,kinetics)
    # Uniform Chebyshev error: 2 exp(-12) sum_{j>d} I_j(12);
    # I_j(12) <= 6^j/j! exp(36/(j+1)).
    # exp(-12+36/20) < exp(-10) < 1/20000, verified by a positive Taylor partial sum.
    assert sum(F(10**j,factorial(j)) for j in range(23))>20000
    err=F(2,20000)*F(6**19,factorial(19))/(1-F(6,20))
    assert err < F(1,1000000)
    # Both the exact Haar integral and quadrature incur this error, in operator norm.
    eta=I.rational(2*err)
    M,J=Ms[0],Ms[1]
    A=Mo[0]
    mid=lambda a:(a.lo+a.hi)/2
    vals,Q=eigh(mid(M))
    # Q need not be computed accurately for these interval tests.
    # For bound on second largest eigenvalue restrict to span of Q without final column.
    for size,limit in ((len(vals),0.0529),(len(vals)-1,0.0204)):
        S=I(Q[:,:size].copy())
        defect=rowsum(upper_abs(mat(S.T,S)-I(np.eye(size))))
        G=mat(S.T,mat(M,S))
        bound=(I(rowsum(upper_abs(G)))/(1-I(defect))+eta).hi.item()
        print(f"even projected lambda upper (subspace dimension {size}): {bound:.10f}",flush=True)
        assert defect<1 and F.from_float(bound)<F(str(limit))

    q0=I(Q[:,-1,None].copy())
    # Choose the linear combination with maximal coupling to this observable.
    doublet=Q[:,-3:-1]
    v=doublet@(doublet.T@mid(J)@q0.lo)
    qE=I((v/np.linalg.norm(v)).reshape(-1,1))
    _,vo=eigh(mid(A),subset_by_index=(len(A.lo)-1,len(A.lo)-1))
    vodd=I(vo)
    odd=(quad(vodd,A,vodd)/quad(vodd,I(np.eye(len(A.lo))),vodd)-eta).lo.item()
    assert F.from_float(odd)>F(494,10000)
    print(f"odd lambda lower {odd:.10f}",flush=True)

    # Exact matrix errors are operator-norm errors, keeping residual estimates dimension-free.
    n0=quad(q0,M,q0)-eta*quad(q0,I(np.eye(len(vals))),q0)
    lambda0_lower=I.rational(F(526,10000))
    assert (n0/quad(q0,I(np.eye(len(vals))),q0)).lo > lambda0_lower.hi
    nE=quad(qE,M,qE)-eta*quad(qE,I(np.eye(len(vals))),qE)
    ampl=quad(qE,J,q0)
    en0,enE=I.rational(F(52695,1000000)),I.rational(F(2,100))
    errs=[]
    for q,a,denom in ((q0,en0,n0),(qE,enE,nE)):
        err=(I(norm(mat(M,q)-q*a))+eta*norm(q))/denom.sqrt()+I.rational(CUTOFF)
        errs.append(err)
    # ||A P sqrt(K)|| <= 1; exact denominator lower bounds above.
    amp_min=min(abs(ampl.lo),abs(ampl.hi)) if ampl.lo*ampl.hi>0 else 0
    n0hi=quad(q0,M,q0)+eta*quad(q0,I(np.eye(len(vals))),q0)
    nEhi=quad(qE,M,qE)+eta*quad(qE,I(np.eye(len(vals))),qE)
    amp=(I(amp_min)-eta*norm(qE)*norm(q0))/(n0hi*nEhi).sqrt()
    lambda0_upper=I.rational(F(529,10000)+CUTOFF)
    lambda2_upper=I.rational(F(204,10000)+CUTOFF)
    leakage0=I(2).sqrt()*errs[0]/(en0-lambda2_upper)
    below=enE-lambda0_upper/3
    above=3*lambda0_lower/7-enE
    distance=I(min(below.lo,above.lo))
    assert distance.lo>0
    leakageE=errs[1]/distance
    low=amp-(leakage0+leakageE)/I(2).sqrt()
    assert low.lo>0
    weight=low.square().lo.item()
    print(f"trial amplitude lower {amp.lo:.8f}, residual upper {errs[0].hi:.8f}, {errs[1].hi:.8f}")
    print(f"first tensor component vacuum weight in (log(7/3),log 3) lower {weight:.8f}")
    assert F.from_float(weight)>F(24,1000)
    assert F.from_float(float(amp.lo))>F(278,1000)
    assert F.from_float(float(errs[0].hi))<F(318,1000000)
    assert F.from_float(float(errs[1].hi))<F(353,1000000)
    # Three orthogonal center-character sectors have the certified odd eigenvalue.
    ratio=F(494,10000)/(F(529,10000)+CUTOFF)
    odds=3*ratio**48
    assert odds/(1+odds)>F(78,1000)
    print(f"period-48 excited probability lower {float(odds/(1+odds)):.8f} from rational endpoints")


if __name__=="__main__":
    check()
