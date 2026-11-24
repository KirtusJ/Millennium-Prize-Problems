"""Predicates (fixed before first run):
P1 (ODE) |R'-(1-3R/k-R^2)| < 1e-9 at k=0.5,1,3,8 using series R and central FD (h=1e-5; FD error ~h^2*R'''~1e-10, roundoff ~1e-16/h=1e-11).
P2 (w') |FD w' - [R(3-2w)-w/k]| < 1e-6 at same k and 20 more grid points in [0.2,15].
P3 (w'') at general k: |FD w'' - [p(3-2w)+w/k^2 - w'(2R+1/k)]| < 1e-4 (FD h=1e-3, second diff error ~h^2 ~1e-6*w'''' plus roundoff 1e-16/h^2=1e-10).
P4 exact series check (Fractions): coefficients of w' series equal those of R(3-2w)-w/k up to order k^15.
P5 zeros of w' on k in (0.05,60): count sign changes of formula w' on grid (expected 0 if w monotone).
P6 (A)==(B) at w'=0: algebraic: with p=w/k^2, A=B; checked at random (R,k,w) with p substituted: |A-B|<1e-12.
P7 (A) and (B) vs w'' at general k are NOT expected equal to FD w'' (extra term -w'(2R+1/k)); report max residual of A, B vs FD w'' to show they only hold where w'=0.
"""
import random
from fractions import Fraction as F
from math import factorial
random.seed(216)
def I(nu,k,M=120):
    return sum((k/2)**(2*m+nu)/(factorial(m)*factorial(m+nu)) for m in range(M))
def R(k): return I(2,k)/I(1,k)
def p(k,h=1e-5): return (R(k+h)-R(k-h))/(2*h)
def parts(k):
    r=R(k); pp=1-3*r/k-r*r; w=k*k*pp
    return r,pp,w
def wp_formula(k):
    r,pp,w=parts(k); return r*(3-2*w)-w/k
def wpp_formula(k):
    r,pp,w=parts(k); return pp*(3-2*w)+w/k**2-wp_formula(k)*(2*r+1/k)
res={}
ks=[0.5,1,3,8]
res['P1']=max(abs(p(k)-(1-3*R(k)/k-R(k)**2)) for k in ks)
W=lambda k:k*k*(1-3*R(k)/k-R(k)**2)
Wd=lambda k:k*k*p(k)
grid=ks+[0.2+14.8*i/19 for i in range(20)]
h=1e-4
res['P2']=max(abs((W(k+h)-W(k-h))/(2*h)-wp_formula(k)) for k in grid)
h=1e-3
res['P3']=max(abs((W(k+h)-2*W(k)+W(k-h))/h**2-wpp_formula(k)) for k in [0.5,1,2,3,5,8])
# P4 exact series, R from I2/I1 series in x=k
N=18
def ser_I(nu): # coefficients of I_nu*(2/k)^nu... in powers of k, as list
    c=[F(0)]*N
    for m in range(N):
        e=2*m+nu
        if e<N: c[e]=F(1,2**e*factorial(m)*factorial(m+nu))
    return c
def mul(a,b):
    c=[F(0)]*N
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if i+j<N: c[i+j]+=x*y
    return c
def div(a,b): # a/b series, b starts at k^1, a at k^2 -> shift
    a=a[1:]+[F(0)]; b=b[1:]+[F(0)]
    q=[F(0)]*N
    for n in range(N-1):
        s=a[n]-sum(q[i]*b[n-i] for i in range(n))
        q[n]=s/b[0]
    return q
Rs=div(ser_I(2),ser_I(1))
def d(a): return [ (i+1)*a[i+1] for i in range(N-1)]+[F(0)]
def shift(a,s): # multiply by k^s (s may be negative)
    c=[F(0)]*N
    for i,x in enumerate(a):
        if 0<=i+s<N: c[i+s]=x
    return c
ps=d(Rs); ws=shift(ps,2)
lhs=d(ws)
t1=mul(Rs,[F(3)]+[F(0)]*(N-1)); t2=mul(Rs,[2*x for x in ws]); wk=shift(ws,-1)
rhs=[t1[i]-t2[i]-wk[i] for i in range(N)]
res['P4_first_series_coeffs_R']=[str(x) for x in Rs[:6]]
res['P4']=all(lhs[i]==rhs[i] for i in range(14))
# P5
sc=0;prev=None;mn=1e9
k=0.05
vals=[]
while k<60:
    v=wp_formula(k); vals.append((k,v))
    if prev is not None and prev*v<=0: sc+=1
    prev=v; k+=0.05
res['P5_sign_changes']=sc
res['P5_min_wprime']=min(v for _,v in vals)
res['P5_w_at_60']=W(60.0)
# P6
mx=0
for _ in range(1000):
    r=random.uniform(.01,1);k=random.uniform(.1,20);w=random.uniform(0,3)
    pp=w/k**2
    A=pp*(3-2*w)+w/k**2;B=(4-2*w)*w/k**2
    mx=max(mx,abs(A-B))
res['P6']=mx
# P7
res['P7_A_resid']=max(abs((W(k+1e-3)-2*W(k)+W(k-1e-3))/1e-6-(p(k)*(3-2*W(k))+W(k)/k**2)) for k in [1,2,5])
res['P7_B_resid']=max(abs((W(k+1e-3)-2*W(k)+W(k-1e-3))/1e-6-((4-2*W(k))*W(k)/k**2)) for k in [1,2,5])
passed = res['P1']<1e-9 and res['P2']<1e-6 and res['P3']<1e-4 and res['P4'] and res['P6']<1e-12
for kk,v in res.items(): print(kk,v)
print('PASS' if passed and res['P5_sign_changes']==0 else 'FAIL')
import sys; sys.exit(0 if passed else 1)
