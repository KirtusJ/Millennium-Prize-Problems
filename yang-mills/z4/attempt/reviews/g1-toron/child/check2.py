"""T74 pass 2: same predicates as check.py (A,B,C; met if slack>tol, failed if slack<-tol, else measured only),
 but I_n(x) by log power series sum_k (x/2)^(2k+n)/(k!(k+n)!) (all terms positive, logsumexp, K=4000 terms, tail negligible:
 terms peak near k~x/2<=256, ratio of term k+1/k <(x/2)^2/(k^2)<1e-4 beyond k=2560... ). Error tol: rel 1e-11 per I_n
 (exponent magnitude <=~3e3 times 1e-16 lgamma rounding => <=~1e-12; 10x margin), tol = 4*(2e-11)*|quantity| as in check.py form.
 Also compares log I_n with check.py trapezoid values where trapezoid reliable. results2.txt mode 'x'."""
import numpy as np, math
XS=[0.5,1,2,4,8,16,32,64,128,256,512]
K=4000; lg=np.array([math.lgamma(i+1) for i in range(K+260)])
def logI(x,nmax=202):
    k=np.arange(K); out=np.empty(nmax+1)
    for n in range(nmax+1):
        e=(2*k+n)*math.log(x/2)-lg[k]-lg[k+n]; m=e.max(); out[n]=m+math.log(np.exp(e-m).sum())
    return out
def Is(x,N,nmax=202):
    t=np.linspace(0,np.pi,N+1); w=np.ones(N+1); w[[0,-1]]=.5
    return (np.cos(np.arange(nmax+1)[:,None]*t[None,:])*(w*np.exp(x*(np.cos(t)-1)))).sum(1)/N
out=open("results2.txt","x")
def P(*a): print(*a,file=out)
cnt={k:[0,0,0,0] for k in "ABC"}; worst={k:(np.inf,None) for k in "ABC"}; maxdiff=0
def judge(k,slack,tol,key):
    cnt[k][0]+=1
    if slack>tol: cnt[k][1]+=1
    elif slack<-tol: cnt[k][2]+=1; P(k,key,"FAIL slack=%.3e tol=%.1e"%(slack,tol))
    else: cnt[k][3]+=1; P(k,key,"MEASURED-ONLY slack=%.3e tol=%.1e"%(slack,tol))
    if slack<worst[k][0]: worst[k]=(slack,key,tol)
EPS=2e-11
for x in XS:
    L=logI(x); b=Is(x,8192)
    for n in range(203):
        if b[n]>1e-3: maxdiff=max(maxdiff,abs(math.log(b[n])+x-L[n]))
    for nu in range(201):
        lr=L[nu+1]-L[nu]; r=math.exp(lr)
        lo=x/(nu+1+math.sqrt((nu+1)**2+x*x)); hi=x/(nu+.5+math.sqrt((nu+.5)**2+x*x))
        judge("A",min(r-lo,hi-r),4*2*EPS*r+1e-13*r,(nu,x))
    for n in range(1,201):
        ll=L[n+1]-L[1]; tol=4*2*EPS*abs(ll)+1e-13   # abs error of log lhs is 2*EPS (relative errs of two I's)
        tol=4*2*EPS+1e-13
        judge("B",-(n*(n+2)/2)/(x+n+.5)-ll,tol,(n,x))
        if n+.5<=x: judge("C",-(n*(n+2)/2)/(2*x)-ll,tol,(n,x))
P("max |log I_n(trapz,reliable I>1e-3 scaled) - log I_n(series)| =",maxdiff)
for k in "ABC": P(k,"tested,met,failed,measured_only =",cnt[k],"worst slack,case,tol=",worst[k])
out.close(); print(open("results2.txt").read()[-2500:])
