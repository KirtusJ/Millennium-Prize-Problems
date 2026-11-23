"""T181 numerical recheck. Predicates fixed BEFORE first run (tolerances in brackets):
(1) c* = int_0^pi sqrt(4 asinh(sin a)) da via Gauss-Legendre after a=(pi/2)v^2 on each half (n=100 and 200 must agree
    to 1e-12 [convergence]); claim MET if |c*-4.6054132|<5e-8 [claim has 8 sig digits, half-unit of last place].
(2) L=sqrt(4 asinh 1); MET if floor(L*1e4)/1e4 == 1.8776 [claim '1.8776...'].
(3) D(1) in [0.0389,0.0390) [claim '0.0389...']; D'>0 on log grid beta in [1,1e8] 2000 pts using analytic derivative
    and finite-difference D(b+h)>D(b) [exact; no tol], plus analytic argument noted.
(4) grid 200 deltas in (0,1] x 200 t in (0,delta]: 1-cos t - (t^2/2)(1-5d^2/48) >= -1e-16*t^2 [double rounding, using 2sin^2(t/2)].
(5) z log grid 600 pts [0.01,700]: ive1(z)-[(1-1/2z)/sqrt(2 pi z) - 0.5 e^{-z}] >= -1e-12 [quadrature tol: N vs 2N agree <1e-13].
(6) 60 deltas (0,1] x 500 z log [1e-3,1e4]: RHS-LHS >= -1e-12 [same quadrature tol].
(7) r in 0..1 (201 pts), c in {0..10} (201 pts) + extra c: RHS-LHS >= -1e-10 [max over phi by 40001-pt grid then golden refine, error<1e-12].
(8) 2asinh(cos .5)>1.3 exact margin.
(9) A(1)<5.83 ; A(s)>=1+2s - 1e-15 on 10001 pts.
(10) beta log grid [1,1e12] 2000 pts: lhs-rhs >= -1e-16*lhs-scale (use 2sin^2 form, tol 1e-12 relative to rhs).
(11) |A-exp(2asinh s)|<=1e-13*A and |alpha/2-s^2-c/A|<=1e-13 on 2000 pts s in (0,1].
(12) measurement only (log-domain evaluation, beta>64 needed for 1-4tau>0).
Results go to a file opened with mode 'x'.
"""
import numpy as np, math, sys
out=open(sys.argv[1],'x')
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n'); out.flush()
GL={n:np.polynomial.legendre.leggauss(n) for n in (100,200,400)}
def gl(f,a,b,n):
    x,w=GL[n]; return (b-a)/2*np.sum(w*f((b-a)/2*(x+1)+a))
def cstar(n):
    # half [0,pi/2], a=(pi/2)v^2, v in [0,1]; symmetric about pi/2
    f=lambda v: np.sqrt(4*np.arcsinh(np.sin(np.pi/2*v*v)))*np.pi*v
    return 2*gl(f,0,1,n)
c100,c200,c400=cstar(100),cstar(200),cstar(400)
P('(1) c*',repr(c200),repr(c100),repr(c400),'conv',abs(c200-c400)); 
P('(1) verdict','MET' if abs(c200-c400)<1e-12 and abs(c200-4.6054132)<5e-8 else 'FAILED','diff to claim',c200-4.6054132)
L=math.sqrt(4*math.asinh(1)); P('(2) L',repr(L),'MET' if math.floor(L*1e4)/1e4==1.8776 else 'FAILED')
D=lambda b:1-1/(2*b)-math.sqrt(2*math.pi*b)*math.exp(-b)/2
P('(3) D(1)',repr(D(1)),'MET' if 0.0389<=D(1)<0.0390 else 'FAILED')
bs=np.exp(np.linspace(0,math.log(1e8),2000)); bad=0
for b in bs:
    dD=1/(2*b*b)-math.sqrt(2*math.pi)*math.exp(-b)*(0.5/math.sqrt(b)-math.sqrt(b))/2
    if not(dD>0 and D(b*(1+1e-6))>D(b)): bad+=1
P('(3) monotone: grid points 2000, violations',bad,'MET' if bad==0 else 'FAILED','(analytic: D\'=1/(2b^2)+sqrt(2pi)e^-b(sqrt b-1/(2sqrt b))/2>0 for b>=1/2)')
# (4)
n=0;bad=0;worst=1e9
for d in np.linspace(0.005,1,200):
    t=np.linspace(0,d,201)[1:]
    m=2*np.sin(t/2)**2-(t*t/2)*(1-5*d*d/48)
    n+=len(t); bad+=int(np.sum(m<-1e-16*t*t)); worst=min(worst,float(np.min(m/(t*t))))
P('(4) cases',n,'qualify(all grid points are in hypothesis)',n,'violations',bad,'min margin/t^2',worst,'MET' if bad==0 else 'FAILED')
# Bessel
def ive(nu,z):
    z=np.asarray(z,float); r=[]
    for zz in z:
        N=int(14*math.sqrt(zz))+64
        res=[]
        for M in (N,2*N):
            t=2*np.pi*np.arange(M)/M
            res.append(np.mean(np.exp(zz*(np.cos(t)-1))*np.cos(nu*t)))
        r.append((res[1],abs(res[1]-res[0])))
    return np.array(r)
# sanity vs series
def ser(nu,z):
    s=0;term=(z/2)**nu/math.gamma(nu+1);k=0
    while True:
        s+=term;k+=1;term*=(z/2)**2/(k*(k+nu))
        if term<1e-18*s: break
    return s*math.exp(-z)
P('(5) bessel sanity (quad vs series z=5): I0',ive(0,[5.])[0][0]-ser(0,5.),'I1',ive(1,[5.])[0][0]-ser(1,5.))
zs=np.exp(np.linspace(math.log(0.01),math.log(700),600))
v=ive(1,zs); lhs=v[:,0]; rhs=(1-1/(2*zs))/np.sqrt(2*np.pi*zs)-0.5*np.exp(-zs)
m=lhs-rhs; i=int(np.argmin(m))
P('(5) points',len(zs),'max quad err',v[:,1].max(),'min margin',m[i],'at z',zs[i],'violations',int(np.sum(m<-1e-12)),'MET' if np.sum(m<-1e-12)==0 else 'FAILED')
# (6)
zs=np.exp(np.linspace(math.log(1e-3),math.log(1e4),500)); i0=ive(0,zs)[:,0]; bad=0;n=0;worst=(9,0,0)
for d in np.linspace(1/60,1,60):
    rhs=1/np.sqrt(2*np.pi*zs*(1-5*d*d/48))+np.exp(-zs*2*math.sin(d/2)**2)
    m=rhs-i0; n+=len(m); bad+=int(np.sum(m<-1e-12)); j=int(np.argmin(m))
    if m[j]<worst[0]: worst=(float(m[j]),d,float(zs[j]))
P('(6) cases',n,'violations',bad,'min margin,delta,z',worst,'MET' if bad==0 else 'FAILED')
# (7)
def lhs7(r,c):
    A=1+2*c;R=math.sqrt(1-r);rho=math.sqrt(r)
    ph=np.linspace(-np.pi,np.pi,40001)
    g=lambda p:R*np.cos(p)+rho*np.sin(p)-c*np.sin(p)**2
    v=g(ph);k=int(np.argmax(v));a,b=ph[max(k-1,0)],ph[min(k+1,len(ph)-1)]
    gr=(math.sqrt(5)-1)/2
    for _ in range(80):
        x1=b-gr*(b-a);x2=a+gr*(b-a)
        if g(x1)>g(x2): b=x2
        else: a=x1
    mx=max(v[k],g((a+b)/2))
    return c/A*r-1+mx, -(r*r/64)*(1-1/A**2)**2
bad=0;n=0;worst=(9,0,0);cs=list(np.linspace(0,10,101))+[0.01,0.1,0.25,0.5,0.75,1,1.5,2,3]
for r in np.linspace(0,1,101):
    for c in cs:
        l,rr=lhs7(r,c);m=rr-l;n+=1
        if m<-1e-10: bad+=1
        if m<worst[0]: worst=(m,r,c)
P('(7) cases',n,'violations',bad,'min margin (r,c)',worst,'MET' if bad==0 else 'FAILED')
# (8)
v8=2*math.asinh(math.cos(.5)); P('(8)',repr(v8),'MET' if v8>1.3 else 'FAILED')
# (9)
A=lambda s:1+2*s*s+2*s*np.sqrt(1+s*s)
s=np.linspace(0,1,10001); P('(9) A(1)',repr(float(A(1.))),'A(s)-(1+2s) min',float(np.min(A(s)-1-2*s)),'MET' if A(1.)<5.83 and np.min(A(s)-1-2*s)>=-1e-15 else 'FAILED')
# (10)
b=np.exp(np.linspace(0,math.log(1e12),2000));eta=b**-.125
l=b*2*np.sin(eta/2)**2; r=.5*b**.75*(1-5/48*b**-.25); m=l-r
P('(10) pts',len(b),'min margin',float(m.min()),'min rel margin',float(np.min(m/r)),'violations',int(np.sum(m<-1e-12*np.abs(r))),'MET' if np.sum(m<-1e-12*np.abs(r))==0 else 'FAILED')
# (11)
s=np.linspace(1e-4,1,2000);a=2*s*np.sqrt(1+s*s);c=s*s+a/2;AA=A(s)
e1=np.max(np.abs(AA-np.exp(2*np.arcsinh(s)))/AA);e2=np.max(np.abs(a/2-s*s-c/AA))
P('(11) max rel err A',e1,'max abs err alpha',e2,'MET' if e1<1e-13 and e2<1e-13 else 'FAILED')
# (12)
def lse(xs):
    m=max(xs);return m+math.log(sum(math.exp(x-m) for x in xs))
def deficit(s,b):
    tau=b**(-1/3);d=tau;As=A(s);Dv=D(b)
    f=(1-tau)*(1-4*tau)*(1-5*d*d/48)
    if f<=0 or Dv<=0: return float('nan')
    ls=0.5*math.log(2*math.pi*b)
    lMin=-math.log(Dv)+lse([-0.5*math.log(f), ls-b*(1-5*tau)*2*math.sin(d/2)**2, ls-b*As*tau/2])
    lMo=math.log(b)+ls-math.log(2*Dv)-(b*tau*tau/64)*(1-1/As**2)**2
    return max(lMin,math.log(As)+lMo)
P('(12) deficit(0.1,1e12)',deficit(.1,1e12),'claim 24.9; deficit(1,1e11)',deficit(1.,1e11),'claim 5e-4')
ss=np.linspace(.1,1,91)
def mx(b):
    v=[deficit(x,b) for x in ss];k=int(np.argmax(v));return v[k],ss[k]
for e in range(2,17): P('(12) beta=1e%d'%e,mx(10.0**e))
lo,hi=1e10,1e16
grid=np.exp(np.linspace(math.log(lo),math.log(hi),400));first=None
for g in grid:
    if mx(g)[0]<0.2: first=g;break
if first:
    a,bb=first/1.0155,first
    for _ in range(50):
        mid=math.sqrt(a*bb)
        if mx(mid)[0]<0.2: bb=mid
        else: a=mid
    P('(12) first beta (scan upward from 1e10) with max_s deficit<0.2:',bb,mx(bb))
else: P('(12) never <0.2 in [1e10,1e16]')
# monotone check of crossing
P('(12) beta<=4096 range over s in [0.1,1], beta in 100..4096 (valid beta>64):')
vals=[(deficit(x,b),x,b) for b in np.exp(np.linspace(math.log(100),math.log(4096),60)) for x in ss]
P('   min',min(vals),'max',max(vals))
for b in (100,300,1000,4096):
    v=[deficit(x,b) for x in ss];P('   beta',b,'min',min(v),'max',max(v))
