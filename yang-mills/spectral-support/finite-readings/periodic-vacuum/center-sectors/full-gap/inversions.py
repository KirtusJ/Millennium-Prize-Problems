"""Exact Haar trace bounds for nontrivial link inversions in both gap calculations."""
from fractions import Fraction as F
from functools import cache
from itertools import product
from math import comb, factorial
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from certify import kinetic
from spectrum import moment

# Candidate coefficients in the Chebyshev basis (argument V/12 - 1).
# Their provenance does not enter the supersolution proof.
COEFF = (1164262212, -2229285986, 1956976760, -1576960399, 1168496560,
         -797962692, 503527650, -294435042, 160020101, -81074906, 38407737,
         -17061990, 7127331, -2806957, 1044135, -365174, 111520)


def add(a, b, factor=1):
    c = list(a) + [0]*max(0,len(b)-len(a))
    for i, x in enumerate(b):
        c[i] += factor*x
    return c


def multiply(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c


def majorant():
    coeff = [F(i,10**10) for i in COEFF]
    # T_n'(y)=n U_(n-1)(y). In a T expansion of U_m, positive
    # degrees m,m-2,... have coefficient 2, and the constant (if any) has 1.
    residual = coeff.copy()
    for n in range(1,len(coeff)):
        for j in range(n-1,-1,-2):
            residual[j] += coeff[n]*F(n*(2 if j else 1),12)
    offset = max(sum(abs(x) for x in residual),
                 1-sum((-1)**i*x for i,x in enumerate(coeff)))
    assert offset < F(17,100000)
    coeff[0] += offset
    linear = [-1,F(1,12)]
    prev, term = [1], linear
    poly = add([coeff[0]],term,coeff[1])
    for c in coeff[2:]:
        prev, term = term, add([2*x for x in multiply(linear,term)],prev,-1)
        poly = add(poly,term,c)
    assert poly[0]>=1
    return poly


@cache
def haar_radial(a,b):
    """Haar expectation of x^(2a) (1-x^2)^b on the unit three-sphere."""
    return F(2*factorial(2*a)*factorial(2*b+2),
             4**(a+b+1)*factorial(a)*factorial(b+1)*factorial(a+b+1))


@cache
def radial(n,l,h):
    alpha = l+1
    q = [0]*(n-l+1)
    for j in range((n-l)//2+1):
        power = n-l-2*j
        q[power] = (-1)**j*2**power*F(factorial(alpha+n-l-j-1),
                                       factorial(alpha-1)*factorial(j)*factorial(power))
    squared = multiply(q,q)
    def integral(k):
        return sum(value*haar_radial(i//2,l+k) for i,value in enumerate(squared) if value)
    return integral(h)/integral(0)


def multivariate(f,g):
    out={}
    for (a,b,c),v in f.items():
        for (i,j,k),w in g.items():
            key=(a+i,b+j,c+k)
            out[key]=out.get(key,0)+v*w
    return {k:v for k,v in out.items() if v}


# det Gram equals the square of the oriented volume of the three angular vectors.
DET={(0,0,0):1,(1,1,1):2,(2,0,0):-1,(0,2,0):-1,(0,0,2):-1}
ONE={(0,0,0):1}
base_moment=cache(moment)


@cache
def angular(i,j,k,a,b,c):
    if a: return angular(i,j,k,a-1,b,c)-angular(i+2,j,k,a-1,b,c)
    if b: return angular(i,j,k,a,b-1,c)-angular(i,j+2,k,a,b-1,c)
    if c: return angular(i,j,k,a,b,c-1)-angular(i,j,k+2,a,b,c-1)
    return base_moment(i,j,k)


def shapes(labels,odd):
    density = DET if odd else ONE
    def inner(f,g):
        fg=multivariate(multivariate(f,g),density)
        return sum(x*base_moment(*p) for p,x in fg.items())
    result={}
    earlier=[]
    for l,m,n in sorted(labels,key=lambda v:(sum(v),v)):
        top=((l+m-n-odd)//2,(l+n-m-odd)//2,(m+n-l-odd)//2)
        assert min(top)>=0 and (l+m+n)%2==odd
        f={top:F(1)}
        for previous,norm in earlier:
            ratio=inner(f,previous)/norm
            for key,x in previous.items():
                f[key]=f.get(key,0)-ratio*x
        f={key:x for key,x in f.items() if x}
        norm=inner(f,f)
        assert norm>0 and all(inner(f,g)==0 for g,_ in earlier)
        earlier.append((f,norm))
        result[l,m,n]={key:x/norm for key,x in multivariate(multivariate(f,f),density).items()}
    return result


def sector(center,inversion,cutoff,poly):
    weights=[kinetic(n+1) for n in range(17)]
    assert weights[16][1]<cutoff and weights[0][0]<=1<=weights[0][1]
    rows=[]
    for ns in product(*(range(p,16,2) for p in center)):
        lo,hi=F(1),F(1)
        for n in ns:
            lo*=weights[n][0]
            hi*=min(F(1),weights[n][1])
        if hi<=cutoff: continue
        assert lo>cutoff
        for ls in product(*(range(p,n+1,2) for p,n in zip(inversion,ns))):
            if 2*max(ls)<=sum(ls):
                rows.append((ns,ls,hi))
    assert len({(ns,ls) for ns,ls,_ in rows})==len(rows)
    sq=shapes({ls for _,ls,_ in rows},sum(inversion)%2)

    @cache
    def direction(ls,a,b,c):
        return sum(q*angular(*p,a,b,c) for p,q in sq[ls].items())

    trace=F(0)
    for d,coef in enumerate(poly):
        for a in range(d+1):
            for b in range(d-a+1):
                c=d-a-b
                term=F(0)
                for ns,ls,weight in rows:
                    val=weight*direction(ls,a,b,c)
                    for n,l,h in zip(ns,ls,(a+b,a+c,b+c)):
                        val*=radial(n,l,h)
                    term+=val
                trace+=coef*8**d*comb(d,a)*comb(d-a,b)*term
    return len(rows),trace


if __name__=="__main__":
    if not __debug__:
        raise RuntimeError("run with assertions enabled")
    assert haar_radial(0,0)==1 and haar_radial(1,0)==F(1,4)
    assert sum(q*base_moment(*key) for key,q in DET.items()) == F(2,9)
    p=majorant()
    for j in (1,2,3):
        inversion=tuple(int(k<j) for k in range(3))
        for name,center,cutoff,limit in (
                ("all real signs even",inversion,F(6,1000),F(48,1000)),
                ("center neutral",(0,0,0),F(2,1000),F(195,10000))):
            count,tr=sector(center,inversion,cutoff,p)
            upper=tr+cutoff
            print(f"{name}, {j} odd inversions, {count} rows: trace upper {float(tr):.10f}, "
                  f"block norm upper {float(upper):.10f}",flush=True)
            assert 0<tr and upper<limit
