"""ang.py -- angular algebra (own code, exact rational Racah formulas).
w3j000(a,b,c): 3j symbol (a b c;0 0 0). sixj(...): Racah formula, exact sum in integers.
redC(l,k,lp) = <l||C^k||lp> = (-1)^l sqrt((2l+1)(2lp+1)) (l k lp;000)   (Edmonds 5.4.5)
pairA(la,lb,lap,lbp,L,k) = <(la lb)L| C^k(a).C^k(b) |(lap lbp)L>
   = (-1)^(lap+lb+L) {la lb L; lbp lap k} <la||C^k||lap><lb||C^k||lbp>   (Edmonds 7.1.6)
and P_k(na.nb) = C^k(a).C^k(b).
"""
from functools import lru_cache
from fractions import Fraction
from math import factorial as F, sqrt

def tri(a,b,c): return abs(a-b)<=c<=a+b and (a+b+c)==int(a+b+c)

@lru_cache(maxsize=None)
def w3j000(a,b,c):
    J=a+b+c
    if J%2 or not tri(a,b,c): return 0.0
    g=J//2
    v=Fraction(F(J-2*a)*F(J-2*b)*F(J-2*c),F(J+1))
    r=sqrt(v)*F(g)/(F(g-a)*F(g-b)*F(g-c))
    return (-1)**g*r

def _d2(a,b,c): return Fraction(F(a+b-c)*F(a-b+c)*F(-a+b+c),F(a+b+c+1))

@lru_cache(maxsize=None)
def sixj(j1,j2,j3,j4,j5,j6):
    if not (tri(j1,j2,j3) and tri(j1,j5,j6) and tri(j4,j2,j6) and tri(j4,j5,j3)): return 0.0
    a=[j1+j2+j3,j1+j5+j6,j4+j2+j6,j4+j5+j3]; b=[j1+j2+j4+j5,j2+j3+j5+j6,j3+j1+j6+j4]
    s=0
    for t in range(max(a),min(b)+1):
        den=1
        for x in a: den*=F(t-x)
        for y in b: den*=F(y-t)
        s+=Fraction((-1)**t*F(t+1),den)
    pre=_d2(j1,j2,j3)*_d2(j1,j5,j6)*_d2(j4,j2,j6)*_d2(j4,j5,j3)
    return float(s)*sqrt(pre) if s>=0 else -float(-s)*sqrt(pre)

def redC(l,k,lp): return (-1)**l*sqrt((2*l+1)*(2*lp+1))*w3j000(l,k,lp)

@lru_cache(maxsize=None)
def pairA(la,lb,lap,lbp,L,k):
    c=redC(la,k,lap)*redC(lb,k,lbp)
    if c==0: return 0.0
    return (-1)**(lap+lb+L)*sixj(la,lb,L,lbp,lap,k)*c
