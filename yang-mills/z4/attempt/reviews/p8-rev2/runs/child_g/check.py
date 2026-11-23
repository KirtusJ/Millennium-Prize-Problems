"""
Predicates (stated before running):
P1: 6*(pi/3) == 2*pi exactly (symbolic if sympy, else |diff|<1e-45 at 60 digits).
P2: 1-cos(pi/3) == 1/2 exactly (symbolic if sympy, else |diff|<1e-45).
P3: double 1-math.cos(math.pi/3) == 0.4999999999999999 and (>=0.5) is False.
P4: smallest double theta with 1-cos(theta)>=0.5 found by bisection on math.cos
    then refined by nextafter stepping; predicate assumed monotone near pi/3.
"""
import math
from decimal import Decimal, getcontext
out = open('results.txt','x')
def w(*a):
    s=' '.join(map(str,a)); print(s); out.write(s+'\n')
getcontext().prec=70
# pi via Machin
def arctan_inv(x):
    x=Decimal(x); t=1/x; s=t; n=1; x2=x*x
    while abs(t)>Decimal(10)**-68:
        t=-t/x2; n+=2; s+=t/n
    return s
PI=4*(4*arctan_inv(5)-arctan_inv(239))
def cos(x):
    t=Decimal(1); s=t; k=0
    while abs(t)>Decimal(10)**-68:
        k+=2; t=-t*x*x/((k-1)*k); s+=t
    return s
a=PI/3
w('pi(70d)=',PI)
d1=6*a-2*PI; w('(1) 6*(pi/3)-2pi =',d1,' within 1e-45:',abs(d1)<Decimal(10)**-45)
d2=(1-cos(a))-Decimal('0.5'); w('(2) 1-cos(pi/3)-0.5 =',d2,' within 1e-45:',abs(d2)<Decimal(10)**-45)
try:
    import sympy as sp
    w('sympy exact: 6*(pi/3)==2pi',sp.simplify(6*(sp.pi/3)-2*sp.pi)==0,'; 1-cos(pi/3)=',1-sp.cos(sp.pi/3))
except ImportError: w('sympy not installed; exactness rests on tolerance + known identity cos(pi/3)=1/2')
v=1-math.cos(math.pi/3)
w('(3) double 1-cos(pi/3)=',repr(v),' >=0.5:',v>=0.5, ' math.pi/3=',repr(math.pi/3),' cos=',repr(math.cos(math.pi/3)))
f=lambda t:1-math.cos(t)>=0.5
lo,hi=1.0,1.1
assert not f(lo) and f(hi)
while True:
    m=(lo+hi)/2
    if m in (lo,hi): break
    if f(m): hi=m
    else: lo=m
w('(4) bisection theta=',repr(hi),' prev double',repr(lo),' f(hi)',f(hi),' f(lo)',f(lo))
w('    hi.hex=',hi.hex(),' ulps above math.pi/3:',round((hi-math.pi/3)/math.ulp(hi)),' diff',hi-math.pi/3)
# monotonic check over few ulps below
t=hi; ok=True
for _ in range(50):
    t=math.nextafter(t,0); ok&=not f(t)
w('    50 doubles below hi all False:',ok)
