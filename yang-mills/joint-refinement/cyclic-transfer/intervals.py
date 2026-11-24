"""Outward-rounded validations of three finite Wilson-cylinder comparisons."""
from decimal import Decimal as D, localcontext, ROUND_FLOOR, ROUND_CEILING
from functools import lru_cache
from math import factorial

@lru_cache(maxsize=None)
def bessel(n,x,upper):
    with localcontext() as ctx:
        ctx.prec = 72
        ctx.rounding = ROUND_CEILING if upper else ROUND_FLOOR
        term=(x/2)**n/D(factorial(n))
        total=term
        k=0
        while True:
            k+=1
            ratio=x*x/D(4*k*(k+n))
            term=term*ratio
            if ratio<D(".5") and term<total*D("1e-58"):
                return total+2*term if upper else total
            total+=term


def endpoints(n,lo,hi,power):
    # Every I_n is increasing for x>0 by its positive series.
    with localcontext() as ctx:
        ctx.prec=72
        ctx.rounding=ROUND_FLOOR
        low=(bessel(n,lo,False)/bessel(1,hi,True))**power
        ctx.rounding=ROUND_CEILING
        high=(bessel(n,hi,True)/bessel(1,lo,False))**power
        return low,high


def certify(B):
    area=int(B)//4
    ref_lo,ref_hi=endpoints(2,B,B,1)
    lo,hi=B,8*B
    assert endpoints(2,lo,lo,4)[1]<ref_lo and endpoints(2,hi,hi,4)[0]>ref_hi
    for _ in range(59):
        mid=(lo+hi)/2
        lower,upper=endpoints(2,mid,mid,4)
        if upper<ref_lo: lo=mid
        elif lower>ref_hi: hi=mid
        else: raise ArithmeticError("Insufficient precision to place midpoint")
    coarse_lo,coarse_hi=endpoints(3,B,B,area)
    assert endpoints(3,4*B,4*B,4*area)[0]>coarse_hi
    assert endpoints(3,lo,hi,2*area)[0]>coarse_hi
    p=8
    with localcontext() as ctx:
        ctx.prec=72
        ctx.rounding=ROUND_CEILING
        moment=sum(endpoints(n,lo,hi,p*4*area)[1] for n in range(3,16,2))
        tail=(hi.to_integral_value(rounding=ROUND_CEILING)+2)*endpoints(17,lo,hi,p*4*area)[1]
        upper=moment+tail
        ctx.rounding=ROUND_FLOOR
        lower=coarse_lo**p
    assert upper<lower
    print(f"B={B}: full neutral fine moment < coarse adjoint power, margin {(lower-upper):.6E}")


if __name__=="__main__":
    with localcontext() as ctx:
        ctx.prec=72
        for B in map(D,(16,64,256)):
            certify(B)
