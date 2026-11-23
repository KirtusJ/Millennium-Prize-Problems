"""Q1: -ln(I_n(b)/I_0(b)), b in {4,16}, n in {1,2}.
Predicates (fixed before first run):
 P1 control: I1(1)/I0(1) rounds to 0.446390 (known answer).
 P2 power series (Python Fraction-free, decimal 50 digits) vs integral (periodic trapezoid
    I_n=(1/pi)int_0^pi e^{b cos t}cos(nt)dt, N=256 nodes, float64) agree in -ln ratio to rel 1e-11.
    Tolerance source: float64 eps 2.2e-16 amplified by cancellation in ln of ratio ~0.9 -> <1e-13; 1e-11 is a safe margin.
 P3 recurrence I_{n-1}-I_{n+1}=2n/b I_n holds to rel 1e-12 (series values).
Output: q1_result.txt (mode x)."""
import numpy as np
from decimal import Decimal, getcontext
getcontext().prec = 60
def I_series(n,b):
    b=Decimal(b); t=(b/2)**n
    for k in range(1,n+1): t/=k
    s=t; k=0
    while True:
        k+=1; t*= (b/2)**2/(k*(k+n)); s+=t
        if t< Decimal(10)**-50: break
    return s
def I_int(n,b,N=256):
    th=np.pi*(np.arange(N)+0.5)/N   # midpoint = exact-convergent for even periodic integrand
    return np.mean(np.exp(b*np.cos(th))*np.cos(n*th))
out=[]
r=I_series(1,1)/I_series(0,1)
out.append(f"P1 control {float(r):.6f} {'PASS' if f'{float(r):.6f}'=='0.446390' else 'FAIL'}")
for b in (4,16):
    for n in (1,2):
        s=-(I_series(n,b)/I_series(0,b)).ln()
        q=-np.log(I_int(n,float(b))/I_int(0,float(b)))
        rel=abs(float(s)-q)/abs(float(s))
        rec=abs((I_series(n-1,b)-I_series(n+1,b))-Decimal(2*n)/b*I_series(n,b))/I_series(n,b) if True else 0
        out.append(f"b={b} n={n} series={s:.15} integral={q:.15g} rel_diff={rel:.2e} 10sf={float(s):.9e} P2={'PASS' if rel<1e-11 else 'FAIL'} P3 rec_rel={float(rec):.1e} {'PASS' if rec<Decimal('1e-12') else 'FAIL'}")
with open("q1_result.txt","x") as f: f.write("\n".join(out)+"\n")
print("\n".join(out))
