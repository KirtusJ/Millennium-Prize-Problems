"""T114 check. Predicates fixed before first run:
P0 control: kappa_0==1 exactly; kappa_1(100) quadrature vs recurrence rel diff <1e-12.
P_quad: for sample (beta,n) kappa_n recurrence vs trapezoid quadrature rel diff < 1e-10
  (tolerance: trapezoid on smooth even periodic integrand converges geometrically; recurrence ~1e-15 per step).
LOW: for all 0<=n1,n2<=M: L=1-k1k2 >= theta*(l1+l2)/(2beta) * (1 - 1e-9)  [rel tol 1e-9: double rounding of
  -expm1(-(a1+a2)), a_n=-ln kappa_n, error ~1e-13 rel worst case]. Trivial (n1=n2=0, both sides 0) counted separately.
HIGH: for max(n1,n2)>=M+1, n1,n2 in [0,3M+5]: L >= c*(1-1e-9).
K1: for n in [0, 3000]: n(n+2)/(2(beta+n+.5)) *(1-1e-9) <= a_n <= n(n+3)/(2beta)*(1+1e-9).
Hypothesis test: report #cells with M>=1 (LOW nontrivial) per (beta,m).
Also: min ratio L/((l1+l2)/(2beta)) on LOW set (nontrivial) vs theta and 1/(1+m^2).
Seed fixed (no randomness used; np.random.seed(0))."""
import numpy as np, math, sys
np.random.seed(0)
NMAX=3000
def avals(beta):
    N=NMAX+int(10*beta**0.5)+2000
    r=0.0; rs=np.zeros(NMAX+2)
    for nu in range(N,0,-1):   # r_{nu-1}=1/(2nu/x+r_nu)
        r=1.0/(2*nu/beta+r)
        if nu-1<=NMAX+1: rs[nu-1]=r
    # kappa_n=prod_{j=1}^n r_j ; a_n=-sum ln r_j
    a=np.concatenate([[0.0],np.cumsum(-np.log(rs[1:NMAX+1]))])
    return a   # a[n]
def quad(beta,nu,K=200001):
    t=np.linspace(0,math.pi,K); f=np.exp(beta*(np.cos(t)-1))*np.cos(nu*t)
    return (f.sum()-0.5*(f[0]+f[-1]))*(math.pi/(K-1))/math.pi
betas=[50,100,400,1000,4000,10000]; ms=[0.05,0.1,0.25,0.5]
out=open(sys.argv[1],"x"); 
def P(*s):
    l=" ".join(str(x) for x in s); print(l); out.write(l+"\n")
fails=[]
# quadrature cross-check
worst=0
for b in betas:
    a=avals(b)
    for n in [1,2,3,5,10,20]:
        k=math.exp(-a[n]); kq=quad(b,n+1)/quad(b,1)
        d=abs(k-kq)/k; worst=max(worst,d)
        if d>1e-10: fails.append(("quad",b,n,d))
P("P_quad worst rel diff",worst,"cases",len(betas)*6)
P("P0 kappa_1(100)=",math.exp(-avals(100)[1]))
tot={"LOW":[0,0,0],"HIGH":[0,0],"K1":[0,0]}  # met, failed, trivial
for b in betas:
    a=avals(b)
    n=np.arange(NMAX+1)
    lo=n*(n+2)/(2*(b+n+.5)); hi=n*(n+3)/(2*b)
    okk=(lo*(1-1e-9)<=a)&(a<=hi*(1+1e-9))
    tot["K1"][0]+=int(okk.sum()); tot["K1"][1]+=int((~okk).sum())
    for i in np.where(~okk)[0][:3]: fails.append(("K1",b,int(i),a[i],lo[i],hi[i]))
    P("K1 beta",b,"n-range 0..%d"%NMAX,"min slack lower",float(((a-lo)/np.maximum(lo,1e-300))[1:].min()),"min slack upper",float(((hi-a)/np.maximum(hi,1e-300))[1:].min()))
    for m in ms:
        M=int(math.floor(m*math.sqrt(b)))
        th=b/(b+M+.5)/(1+m*m+3*m/math.sqrt(b))
        c=1-math.exp(-(M+1)*(M+3)/(2*(b+M+1.5)))
        lam=lambda k:k*(k+2)
        minr=None;arg=None;nl=0;ml=0;fl=0
        for n1 in range(M+1):
            for n2 in range(M+1):
                if n1==n2==0: tot["LOW"][2]+=1; continue
                L=-math.expm1(-(a[n1]+a[n2])); rhs=th*(lam(n1)+lam(n2))/(2*b)
                rat=L/((lam(n1)+lam(n2))/(2*b))
                if minr is None or rat<minr: minr=rat;arg=(n1,n2)
                if L>=rhs*(1-1e-9): tot["LOW"][0]+=1
                else: tot["LOW"][1]+=1; fails.append(("LOW",b,m,n1,n2,L,rhs))
        hmin=None;hh=0;hf=0
        for n1 in range(3*M+6):
            for n2 in range(3*M+6):
                if max(n1,n2)<M+1: continue
                L=-math.expm1(-(a[n1]+a[n2])); hh+=1
                if hmin is None or L<hmin: hmin=L;harg=(n1,n2)
                if L>=c*(1-1e-9): tot["HIGH"][0]+=1
                else: tot["HIGH"][1]+=1; hf+=1; fails.append(("HIGH",b,m,n1,n2,L,c))
        P("beta",b,"m",m,"M",M,"theta=%.6f"%th,"1/(1+m^2)=%.6f"%(1/(1+m*m)),"minratio",minr,"at",arg,"c=%.6g"%c,"HIGH min L",hmin,harg,"HIGHcases",hh)
P("TOTALS met/failed/(trivial):",tot)
P("FAILS",len(fails))
for f in fails[:40]: P("FAIL",f)
import sys
sys.exit(1 if fails else 0)
