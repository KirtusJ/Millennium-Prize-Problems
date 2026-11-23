"""T182 checks. Predicates fixed BEFORE first run (tolerances in brackets, with origin):
Q1: |c*-4.6054132|<5e-7 (claim given to 7 decimals => half-unit 5e-8, I allow 5e-7 since
    my quadrature is verified only to ~1e-9); two quadratures agree <1e-8.
Q2: max|e(S)-log A(S)|<1e-12 rel on grid S in logspace(-6,6,2001) (double rounding);
    max|(h-2)(1+2S^2h)-h|/h < 1e-9 (cancellation in h-2 for large S: h->2).
Q3: |MA2-claim|<=0.5*last-digit of claim (rounded claims: 0.005,0.005,0.005,0.005,0.05);
    eta*MA2 -> 3.497 : |eta*MA2(1e-6)-log(1/m1)|<1e-3; m1 rounds to 0.0303 (<5e-5);
    switch point = solve m0=m1 exactly => 1/12; claim "approx 1/12" AGREES if |sw-1/12|<1e-12.
Q4: Mc12 same rounding rule (0.005,0.005,0.05,0.05,0.05); min(Mc12-MA2)>=5.98 on 4005
    equispaced points of (0,0.4] (eta_i=0.4*i/4005,i=1..4005); sqrt2(e(sqrt2)+1) rounds to 4.656.
Q5: (a) sqrt2/4+1/16<1/2; (b) 4r/S^2+4sqrt2 r^2/S^3<=5r/S^2 on grid (0<r<=S/8,0<S<=sqrt2);
    (c) arcsin r<=1.003 r, arcsin r - r<=0.17 r^3 on (0,1/8]; (d) subadditivity random x,y seed 0;
    (e) c*(eta)<=c*+pi sqrt(2eta) on 400 etas.  Float slack 1e-15 allowed.
Q6: m/2 at 0.4 rounds to 0.0151; 1-exp(-3eta/4)>=0.555 eta ; sinh eta<=1.03 eta on (0,0.4] grid 4000.
Q7: min slack over grid of both inequalities >=0 (float tol -1e-12). Grid: eta 60 log pts in [1e-3,.4],
    S 80 pts (log) in [sinh eta, sqrt(1+r0^2)], xc 201 pts in [0,1].
Result file opened with 'x'.
"""
import numpy as np, math
from numpy import sqrt, log, exp, arcsinh as asinh, sinh, sin, pi
out=[]
def say(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)
def quad(f,a,b,n):
    x,w=np.polynomial.legendre.leggauss(n); return ((b-a)/2*w*f((b-a)/2*x+(a+b)/2)).sum()
# Q1
eps=lambda a:2*asinh(sin(a))
g=lambda t: 2*t*sqrt(2*eps(t*t))          # a=t^2 on [0,pi/2], smooth
def cstar(n): return 2*quad(g,0,sqrt(pi/2),n)
c1,c2=cstar(200),cstar(400)
# method 2: midpoint-free: a=pi/2*u^2 style via different substitution, a=(pi/2) s^2
g2=lambda s: (pi/2)*2*s*sqrt(2*eps((pi/2)*s*s))
c3=2*quad(g2,0,1,300)
cs=c2
say('Q1 c*',repr(c1),repr(c2),repr(c3),'claim 4.6054132 diff',cs-4.6054132)
say('Q1 pred', abs(cs-4.6054132)<5e-7, max(abs(c1-c2),abs(c2-c3))<1e-8)
# Q2
S=np.logspace(-6,6,2001)
al=2*S*sqrt(1+S*S);A=1+2*S*S+al
r1=np.max(np.abs(2*asinh(S)-log(A))/np.maximum(1,np.abs(2*asinh(S))))
h=1+sqrt(1+S*S)/S
r2=np.max(np.abs((h-2)*(1+2*S*S*h)-h)/h)
say('Q2 max err e=logA',r1,' max rel err (h-2)(1+2S^2h)=h',r2, r1<1e-12, r2<1e-9)
# per-range detail for second identity
for lo,hi in [(1e-6,1),(1,1e2),(1e2,1e4),(1e4,1e6)]:
    m=(S>=lo)&(S<=hi); say('  Q2b range',lo,hi,np.max(np.abs((h[m]-2)*(1+2*S[m]**2*h[m])-h[m])/h[m]))
# Q3
m1=(1-exp(-1/16))/2
def pars(eta):
    am=np.arcsin(sinh(eta)); r0=sqrt(eta*sin(am)/4); m0=(1-exp(-3*eta/4))/2
    return am,r0,m0
def MA2(eta):
    am,r0,m0=pars(eta); ct=1/np.tanh(eta)
    return 2*sqrt(2+r0**2)+np.maximum(ct*log(1/m1),0.75*eta*ct+log(1/m0))
e2=2*asinh(sqrt(2))
def Mc12(eta):
    return sqrt(2)*(e2+1)/sinh(eta)+log(4)+log(1/(exp(eta/2)-1))+e2+eta+0.125+1
et=[0.4,0.2,0.1,0.05,0.01]
cl3=[12.06,20.55,37.91,72.82,352.5]; tol3=[.005]*4+[.05]
for e,c,t in zip(et,cl3,tol3): say('Q3 MA2',e,MA2(e),'claim',c,abs(MA2(e)-c)<=t)
say('Q3 eta*MA2 at 1e-2,1e-4,1e-6',[e*MA2(e) for e in (1e-2,1e-4,1e-6)],'log(1/m1)',log(1/m1))
say('Q3 m1',m1,round(m1,4)==0.0303)
sw=-log(1-2*m1)*4/3; say('Q3 switch eta (m0=m1) =',sw,'1/12=',1/12,'diff',sw-1/12)
# also where the max() in MA2 switches branch
f=lambda e: (1/np.tanh(e))*log(1/m1)-(0.75*e/np.tanh(e)+log(1/pars(e)[2]))
lo,hi=1e-3,0.4
say('Q3 MA2 branch signs f(1e-3),f(.4)',f(1e-3),f(.4))
for _ in range(200):
    mid=(lo+hi)/2
    if f(lo)*f(mid)<=0: hi=mid
    else: lo=mid
say('Q3 MA2 max-branch switch eta ~',lo, 'f there',f(lo))
# Q4
cl4=[18.05,30.38,54.36,101.6,475.7]; tol4=[.005,.005,.05,.05,.05]
for e,c,t in zip(et,cl4,tol4): say('Q4 Mc12',e,Mc12(e),'claim',c,abs(Mc12(e)-c)<=t)
ee=0.4*np.arange(1,4006)/4005
d=Mc12(ee)-MA2(ee); i=d.argmin()
say('Q4 min(Mc12-MA2) on 4005 pts',d.min(),'at eta',ee[i],'>=5.98',d.min()>=5.98)
ef=np.logspace(-8,np.log10(.4),200000); df=Mc12(ef)-MA2(ef)
say('Q4 min over 2e5 log pts [1e-8,.4]',df.min(),'at',ef[df.argmin()])
say('Q4 sqrt2(e(sqrt2)+1)',sqrt(2)*(e2+1))
# Q5
say('Q5a',sqrt(2)/4+1/16,sqrt(2)/4+1/16<.5)
worst=-1e9;cnt=0
for Sv in np.linspace(1e-3,sqrt(2),400):
    r=np.linspace(1e-6,Sv/8,400); lhs=4*r/Sv**2+4*sqrt(2)*r*r/Sv**3; rhs=5*r/Sv**2
    worst=max(worst,((lhs-rhs)/rhs).max())
say('Q5b max rel (lhs-rhs)/rhs',worst,worst<=1e-15)
# note: reduces to 4 sqrt2 r/S <= 1 -> r<=S/(4sqrt2)=0.177S ; r<=S/8 ok
r=np.linspace(1e-9,1/8,100000)
say('Q5c max arcsin r/r',(np.arcsin(r)/r).max(),'max (arcsin r-r)/r^3',((np.arcsin(r)-r)/r**3).max())
rng=np.random.default_rng(0);x=rng.random(10**6)*10;y=rng.random(10**6)*10
say('Q5d min slack',(sqrt(2*x)+sqrt(2*y)-sqrt(2*(x+y))).min())
def cse(eta,n=300): return 2*quad(lambda t:2*t*sqrt(2*(eps(t*t)+eta)),0,sqrt(pi/2),n)
ets=np.logspace(-6,np.log10(.4),400)
sl=[cs+pi*sqrt(2*e)-cse(e) for e in ets]
say('Q5e min slack',min(sl),'at',ets[int(np.argmin(sl))],'(slack>=0:',min(sl)>=-1e-9,')')
# Q6
say('Q6 m at .4: m0,m1',pars(.4)[2],m1,'m/2',min(pars(.4)[2],m1)/2)
e=np.linspace(1e-6,.4,4000)
say('Q6 min (1-exp(-3e/4))/e',((1-exp(-.75*e))/e).min(),' max sinh/e',(sinh(e)/e).max())
# Q7
mins1=mins2=1e9;arg1=arg2=None;bad=0;tot=0
xc=np.linspace(0,1,201)
for eta in np.logspace(-3,np.log10(.4),60):
    am,r0,m0=pars(eta); M2=MA2(eta);a=exp(-.75*eta);b=exp(-1/16)
    for Sv in np.exp(np.linspace(log(sinh(eta)),log(sqrt(1+r0*r0)),80)):
        k=sqrt(1+Sv*Sv)/Sv; gam=1-1/k; P=exp(2*asinh(Sv)-M2/k)
        t=P*xc**gam
        s1=(1-m0)-(a*(1-xc)+t); s2=(1-m1)-(t+b)
        tot+=2*len(xc); bad+=(s1<-1e-12).sum()+(s2<-1e-12).sum()
        if s1.min()<mins1: mins1=s1.min();arg1=(eta,Sv,xc[s1.argmin()])
        if s2.min()<mins2: mins2=s2.min();arg2=(eta,Sv,xc[s2.argmin()])
say('Q7 min slack ineq1',mins1,arg1,' ineq2',mins2,arg2,' violations',bad,'of',tot)
with open('results_q.txt','x') as f: f.write('\n'.join(out)+'\n')
