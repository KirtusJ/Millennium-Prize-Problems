"""T74 check of claims A, B, C. Predicates fixed BEFORE first run:
 Bessel: Is_n(x)=I_n(x)e^-x=(1/pi)int_0^pi e^{x(cos t-1)}cos(nt)dt, trapezoid (periodic/even => spectral),
  N=4096 and 2N=8192 points. Error of Is_n estimated e_n=|Is_n(N)-Is_n(2N)|+2e-16 (doubling + roundoff floor); value from 2N.
 A: slack=min(r-lo, hi-r), r=Is_{nu+1}/Is_nu. B: slack=log rhs-log lhs. C: same, only pairs with n+1/2<=x.
 Case error tol = 4*(relerr)*|quantity| in the compared scale (rel error of ratio = e_a/a+e_b/b; for log: that rel error),
  plus 1e-13 relative floor. met: slack>=tol_case... precisely: met if slack>=-tol_abs? NO: strict:
  met if slack > tol ; failed if slack < -tol ; else 'measured only' (undecided, slack within error).
  Cases where a value Is<=0 or relerr>1e-6 are 'measured only' (unreliable quadrature, e.g. underflow regime).
 Tolerances come from the doubling estimate above, nothing else. Output file results.txt opened with mode 'x'."""
import numpy as np, sys
XS=[0.5,1,2,4,8,16,32,64,128,256,512]
def Is(x,N,nmax=202):
    t=np.linspace(0,np.pi,N+1); w=np.ones(N+1); w[[0,-1]]=.5
    f=w*np.exp(x*(np.cos(t)-1))
    n=np.arange(nmax+1)[:,None]
    return (np.cos(n*t[None,:])*f).sum(1)/N
out=open("results.txt","x")
def P(*a): print(*a,file=out); 
cnt={k:[0,0,0,0] for k in "ABC"}  # tested, met, failed, measured-only
worst={k:(np.inf,None) for k in "ABC"}
def judge(k,slack,tol,ok,key):
    cnt[k][0]+=1
    if not ok: cnt[k][3]+=1; P(k,key,"MEASURED-ONLY unreliable slack=%.3e"%slack); return
    if slack>tol: cnt[k][1]+=1
    elif slack<-tol: cnt[k][2]+=1; P(k,key,"FAIL slack=%.3e tol=%.1e"%(slack,tol))
    else: cnt[k][3]+=1; P(k,key,"MEASURED-ONLY within tol slack=%.3e tol=%.1e"%(slack,tol))
    if ok and slack<worst[k][0]: worst[k]=(slack,key,tol)
for x in XS:
    a=Is(x,4096); b=Is(x,8192); e=np.abs(a-b)+2e-16
    rel=e/np.maximum(np.abs(b),1e-300); good=(b>0)&(rel<1e-6)
    for nu in range(0,201):
        ok=good[nu] and good[nu+1]; r=b[nu+1]/b[nu] if b[nu]>0 else np.nan
        lo=x/(nu+1+np.sqrt((nu+1)**2+x*x)); hi=x/(nu+.5+np.sqrt((nu+.5)**2+x*x))
        rr=rel[nu]+rel[nu+1]; tol=4*rr*abs(r)+1e-13*abs(r) if ok else 0
        judge("A",min(r-lo,hi-r) if ok else np.nan,tol,ok,(nu,x))
    for n in range(1,201):
        ok=good[n+1] and good[1]
        lhs=b[n+1]/b[1]
        rhs=-(n*(n+2)/2)/(x+n+.5)
        if ok:
            sl=rhs-np.log(lhs); tol=4*(rel[n+1]+rel[1])+1e-13
        else: sl=np.nan; tol=0
        judge("B",sl,tol,ok,(n,x))
        if n+.5<=x:
            rhs2=-(n*(n+2)/2)/(2*x)
            sl=rhs2-np.log(lhs) if ok else np.nan
            judge("C",sl,tol,ok,(n,x))
for k in "ABC":
    P(k,"tested,met,failed,measured_only =",cnt[k],"worst reliable slack,case,tol=",worst[k])
out.close()
print(open("results.txt").read()[-3000:])
