"""T102 checks. Predicates fixed before first run (results file opened mode 'x').
P1 control: midpoint quadrature (N=4e6) of 2 sqrt(sin a) on [0,pi] equals control.txt value 4.792561 to 5e-6
   (tol: 6-decimal rounding 5e-7 plus endpoint sqrt-singularity quadrature error ~h^1.5 << 1e-6).
P2 per case (beta,a) in {(50,pi/2),(50,0.3)}: grid largest eigenvalue (Nystrom, h=0.005/sqrt(beta)*... see code,
   dense symmetric eig) matches Lambda=1/(s+sqrt(1+s^2)) with rel err < 1e-9 (trapezoid on Gaussians is spectrally
   accurate; roundoff ~1e-13). Also beta-independence: beta=50 vs 200 within 1e-9.
P3 for all a in 1000-point grid on [0.05,pi-0.05]: |2 asinh(sin a) - acosh(1+2 sin^2 a)| < 1e-9
   (acosh near 1 loses ~eps/eps_val ~1e-16/0.1 precision). Hypothesis test: count qualifying cases, report n/1000.
P4 tilt identity: for Gaussian step variance 1/beta, integral sqrt(beta/2pi)exp(-beta u^2/2) exp(-sqrt(beta) S' u) du = exp(S'^2/2)
   exactly; check numerically at beta=50,S'=1.7 rel err<1e-9; and constant-eps exact: exp(-k a) eigenfn with
   k=sqrt(2 beta eps) gives eigenvalue 1 : exp(-eps)*exp(k^2/(2beta)) -1 < 1e-12.
P5 c = integral sqrt(2*2 asinh(sin a)) da reported (no predicate); compare with control-style 2 sin a version; also
   Haar sin^2: ratio sin^2(a+u)/sin^2 a = exp(2 cot a u + ...) shows O(1/sqrt(beta)) effect (reported, not predicate).
"""
import numpy as np, math
out=open("check_result.txt","x")
def log(*a):
    s=" ".join(str(x) for x in a); print(s); out.write(s+"\n")
ctrl=float(open("control.txt").read())
N=4_000_000; h=math.pi/N; a=(np.arange(N)+.5)*h
q=float(np.sum(2*np.sqrt(np.sin(a)))*h)
log("P1",q,ctrl,abs(q-ctrl)<5e-6)
def lam_grid(beta,s,hx_fac=0.1,L=12.0):
    sig=1/math.sqrt(beta); h=hx_fac*sig/ max(1,1)  # fine relative to 1/sqrt(beta)
    n=int(2*L*sig/h)+1
    x=np.linspace(-L*sig,L*sig,n); h=x[1]-x[0]
    V=2*beta*s*s*x*x; d=np.exp(-V/2)
    K=np.sqrt(beta/(2*np.pi))*np.exp(-0.5*beta*(x[:,None]-x[None,:])**2)*h
    M=d[:,None]*K*d[None,:]
    return np.linalg.eigvalsh(M)[-1], n
ok2=True; lams={}
for beta,al in [(50,math.pi/2),(50,0.3),(200,math.pi/2)]:
    s=math.sin(al); L,n=lam_grid(beta,s); Lh,_=lam_grid(beta,s,0.2)
    ex=1/(s+math.sqrt(1+s*s)); r=abs(L-ex)/ex; lams[(beta,al)]=L
    log("P2",beta,al,"grid",repr(L),"n",n,"coarse",repr(Lh),"exact",repr(ex),"rel",r,"eps1D",-math.log(L),"asinh(s)",math.asinh(s))
    if (beta,al)!=(200,math.pi/2): ok2&=r<1e-9
log("P2 pass(beta=50 cases)",ok2,"beta indep",abs(lams[(50,math.pi/2)]-lams[(200,math.pi/2)])<1e-9)
aa=np.linspace(0.05,math.pi-0.05,1000)
d=np.abs(2*np.arcsinh(np.sin(aa))-np.arccosh(1+2*np.sin(aa)**2))
log("P3 qualifying",int((d<1e-9).sum()),"/1000 maxdiff",d.max())
# small a, where acosh loses precision (hypothesis count outside tolerance)
a2=np.linspace(1e-4,0.05,200); d2=np.abs(2*np.arcsinh(np.sin(a2))-np.arccosh(1+2*np.sin(a2)**2))
log("P3b small a 1e-4..0.05 qualifying",int((d2<1e-9).sum()),"/200 maxdiff",d2.max())
beta=50;Sp=1.7;u=np.linspace(-1.5,1.5,600001);du=u[1]-u[0]
I=np.sum(np.sqrt(beta/2/np.pi)*np.exp(-beta*u*u/2-math.sqrt(beta)*Sp*u))*du
log("P4a",I,math.exp(Sp**2/2),abs(I/math.exp(Sp**2/2)-1)<1e-9)
for eps in (0.3,1.0,2.0):
    k=math.sqrt(2*beta*eps); log("P4b",eps,math.exp(-eps)*math.exp(k*k/(2*beta))-1)
c=float(np.sum(np.sqrt(4*np.arcsinh(np.sin(a)))*h))
log("P5 c(arccosh)=",c," c(control 2 sin a)=",q, "ratio",c/q)
# eps_total small-a check: eps_tot ~ 2 sin a ?
for al in (0.01,0.1,0.5,math.pi/2): log("eps_tot",al,2*math.asinh(math.sin(al)),2*math.sin(al))
out.close()
