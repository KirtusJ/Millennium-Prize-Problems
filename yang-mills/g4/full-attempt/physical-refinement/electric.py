"""Physical-scale electric controls and isotropic minorization. Requires only Python."""
from decimal import Decimal as D, localcontext
from math import factorial
from calibration import TABLE, tune

def bessel(n,x):
    """Positive I_n series. Its tail after term k is <= next/(1-next/current)."""
    half=x/2
    term=half**n/factorial(n)
    total=term
    k=0
    while True:
        k+=1
        term*=half**2/(k*(k+n))
        total+=term
        if term < total*D("1e-43") and half**2 < k*(k+n)/2:
            return total

def ratios(beta):
    i1=bessel(1,beta)
    return bessel(2,beta)/i1,bessel(3,beta)/i1

def control(n,s):
    target=(-s/n**2).exp()
    lo,hi=D(0),2*n**2/s+2
    assert ratios(hi)[0]>target
    for _ in range(72):
        mid=(lo+hi)/2
        if ratios(mid)[0]>target:hi=mid
        else:lo=mid
    u,v=ratios((lo+hi)/2)
    assert abs(u-target)<D("1e-17")
    return float((lo+hi)/2),float(-4*n*u.ln()),float(-n*n*v.ln()),float(-n*n*u.ln())

def report():
    with localcontext() as ctx:
        ctx.prec=52
        for k in (4,8,16,32):
            beta,cell,circle,area=control(D(k),D(1))
            assert abs(cell-4/k)<1e-13 and abs(area-1)<1e-14
            print(f"electric {k} {beta:.11f} {cell:.9f} {circle:.11f} {area:.9f}")
        for n,points in TABLE.items():
            beta=D(str(round(tune(points),9)))
            x=6*beta
            z=2*bessel(1,x)/x
            log10floor=D(n).log10()-D(n**3)/2*z.log10()
            print(f"isotropic {n} {beta:f} {log10floor:.7f}")

if __name__=="__main__":report()
