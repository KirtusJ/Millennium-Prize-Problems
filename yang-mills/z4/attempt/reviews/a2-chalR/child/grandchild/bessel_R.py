"""
Recompute R=C(xi/2)/C(xi) at m=0.1 via Schwinger/Bessel representation
C(t)=int_0^inf dtau exp(-tau(m^2+8)) I_0(2tau)^3 I_t(2tau).

PREDICATES (fixed before first run):
 P1 Bessel impl vs power series (x<=30, nu in {0,.5,1,5.008}): rel err < 1e-11
    (origin: double-precision quadrature, 12 digits expected from GL).
 P2 Method validation at m=1.0, t in {0.7,2.5}: Bessel-Schwinger C(t) vs direct 3D
    periodic trapezoid N=64 (exponentially convergent, error ~exp(-64*M)~1e-27,
    so limit is roundoff): rel diff < 1e-9.
 P3 m=0.1 convergence: R changes < 1e-9 (relative) on refining tau and angle nodes.
 P4 cutoff: R changes < 1e-9 rel when tau_max raised from 60/m^2 to 90/m^2
    (tail ~ e^{-60}).
 P5 0<R<1 sanity.
Tolerance for reported R: 1e-8 relative (limited by P3/P4 demonstrated agreement).
"""
import numpy as np, math, sys
def gl(n,a,b):
    x,w=np.polynomial.legendre.leggauss(n); return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w
def Ie(nu,x,nth=200,ns=300):
    """exp(-x) I_nu(x), real nu>=0, x>0"""
    if x<=40: return Iseries(nu,x)
    thmax=min(math.pi,14/math.sqrt(x))
    th,w=gl(nth,0,thmax)
    r=(w*np.exp(x*(np.cos(th)-1))*np.cos(nu*th)).sum()/math.pi
    sn=math.sin(nu*math.pi)
    if abs(sn)>1e-15:
        smax=min(45/nu if nu>0 else 45, math.acosh(1+45/x))
        s,ws=gl(ns,0,smax)
        r-=sn/math.pi*(ws*np.exp(-x*(1+np.cosh(s))-nu*s)).sum()
    return r
_c={}
def _lg(nu):
    if nu not in _c:
        from math import lgamma
        _c[nu]=(np.array([lgamma(j+1) for j in range(300)]),np.array([lgamma(j+nu+1) for j in range(300)]))
    return _c[nu]
def Iseries(nu,x):
    k=np.arange(300.0)
    from math import lgamma
    lg,lgn=_lg(nu)
    return float(np.exp((2*k+nu)*math.log(x/2)-lg-lgn-x).sum())
def C(t,m,nt=6000,nth=200,ns=300,taumax_fac=60,umin=-40):
    A=m*m
    umax=math.log(taumax_fac/A)
    u,wu=gl(nt,umin,umax)   # composite below
    # composite GL: split into panels
    panels=40; us=[];ws=[]
    edges=np.linspace(umin,umax,panels+1)
    for a,b in zip(edges[:-1],edges[1:]):
        x_,w_=gl(nt//panels,a,b); us.append(x_);ws.append(w_)
    u=np.concatenate(us);wu=np.concatenate(ws)
    tau=np.exp(u);tot=0.0
    for ti,wi in zip(tau,wu):
        x=2*ti
        tot+=wi*ti*math.exp(-ti*A)*Ie(0,x,nth,ns)**3*Ie(t,x,nth,ns)
    return tot
def direct(t,m,N=64):
    p=2*np.pi*(np.arange(N)+0.5)/N-np.pi
    s=4*np.sin(p/2)**2
    S=s[:,None,None]+s[None,:,None]+s[None,None,:]
    om=np.arccosh(1+(m*m+S)/2)
    return (np.exp(-t*om)/(2*np.sinh(om))).mean()
if __name__=="__main__":
    res={}
    # P1
    worst=0
    for nu in (0,.5,1,5.008):
        for x in (0.01,0.5,3,10,30,45,80):
            worst=max(worst,abs(Ie(nu,x)-Iseries(nu,x))/Iseries(nu,x))
    print("P1 worst rel",worst,"PASS" if worst<1e-11 else "FAIL")
    # P2
    w2=0
    for t in (0.7,2.5):
        a=C(t,1.0,nt=1200,taumax_fac=60);b=direct(t,1.0)
        print("  m=1 t=%g bessel %.15g direct %.15g"%(t,a,b)); w2=max(w2,abs(a-b)/b)
    print("P2 worst rel",w2,"PASS" if w2<1e-9 else "FAIL")
    # main
    m=0.1; M=math.acosh(1+m*m/2); xi=1/M
    C1=C(xi,m,nt=1200);C2=C(xi/2,m,nt=1200)
    R=C2/C1
    print("m",m,"M",M,"xi",xi)
    print("C(xi/2)=%.15g C(xi)=%.15g R=%.15g"%(C2,C1,R))
    # P3
    D1=C(xi,m,nt=2400,nth=300,ns=400);D2=C(xi/2,m,nt=2400,nth=300,ns=400)
    R3=D2/D1; print("refined R=%.15g diff %.2e"%(R3,abs(R3-R)/R),"P3","PASS" if abs(R3-R)/R<1e-9 else "FAIL")
    # P4
    E1=C(xi,m,nt=1200,taumax_fac=90);E2=C(xi/2,m,nt=1200,taumax_fac=90)
    R4=E2/E1; print("cutoff90 R=%.15g diff %.2e"%(R4,abs(R4-R)/R),"P4","PASS" if abs(R4-R)/R<1e-9 else "FAIL")
    print("P5","PASS" if 0<R<1 else "FAIL")
