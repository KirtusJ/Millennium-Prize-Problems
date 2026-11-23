"""T175 grid check. Predicates fixed BEFORE first run (margin = RHS-LHS, 'met' iff margin >= -TOL):
A1 rho(e)<=max(e-eta,0), e in [0,2] (N=400001 pts incl. kinks)      TOL=1e-12 (double rounding of O(1) values)
A2 rho(e)>=e-2eta, e in [3eta,2]                                    TOL=1e-12
A3 |g'(e)|<=3/sqrt(2eta), e in [0,2]; analytic g' (also central diff max deviation reported) TOL=1e-12
A4 c*-pi*sqrt(6eta) <= c_rho <= c*  (composite Gauss-Legendre 4000x20 with a=t^2 substitution; scipy not installed)  TOL=1e-8
B1 f-L*tau/2<=ftilde<=f on [0,pi/2], N=2e6+1 grid, f-ftilde=cumtrapz(p(1-chi))   TOL=1e-9 (trapezoid error bound ~h^2)
B2 |ftilde''|<=6/sqrt(eta)+3L/tau, analytic ftilde''=p'chi+p chi'  TOL=1e-12
B3 ftilde=f on [0,pi/2-tau/2]: |f-ftilde|<=1e-12 (met iff)
   Hypothesis (rule 4): per case tau/2<=pi/2 and 3eta<=2 and eps max<=2.
C1 S2 in 400 pts of (0.01,2], D in 101 pts of [0,S2/2], d in 41 pts of [-D,D]; margin=bound-|diff|, TOL=1e-12
   Hypothesis: S2-D>0 and S2+d>0 per (S2,D) case -> count qualifying.
D1,D2: x in [0,1): 200000 uniform + 200 geometric points toward 1 (1-x down to 1e-12); c in 1..10 step .25. TOL=1e-12
Results written to results.json (mode x).
"""
import numpy as np, json, math, sys

_x,_w=np.polynomial.legendre.leggauss(20)
def gl(F,lo,hi,m=4000):
    # composite Gauss-Legendre, F vectorised; substitution a=lo+(hi-lo)t^2 removes sqrt endpoint singularity
    edges=np.linspace(0,1,m+1); mid=(edges[1:]+edges[:-1])/2; hw=(edges[1:]-edges[:-1])/2
    t=(mid[:,None]+hw[:,None]*_x[None,:]); w=hw[:,None]*_w[None,:]
    a=lo+(hi-lo)*t*t; return float(np.sum(F(a)*2*(hi-lo)*t*w))
TOL=1e-12
res={}
def Sm(s):
    s=np.clip(s,0,1); return 3*s*s-2*s**3
def dSm(s):
    inside=(s>0)&(s<1); return np.where(inside,6*s*(1-s),0.0)
def g(e,eta):
    u=np.maximum(e-eta,0); return np.sqrt(u)*Sm((u/eta-0.5)/1.5)
def dg(e,eta):
    u=np.maximum(e-eta,0); s=(u/eta-0.5)/1.5
    with np.errstate(divide='ignore',invalid='ignore'):
        t=np.where(u>0,Sm(s)/(2*np.sqrt(u)),0.0)
    return t+np.sqrt(u)*dSm(s)/(1.5*eta)
eps=lambda a: 2*np.arcsinh(np.sin(a))
deps=lambda a: 2*np.cos(a)/np.sqrt(1+np.sin(a)**2)
def rec(name,margins,extra=None,tol=TOL):
    m=np.asarray(margins); met=int((m>=-tol).sum()); r=dict(n=int(m.size),met=met,failed=int(m.size-met),worst=float(m.min()),tol=tol)
    if extra: r.update(extra)
    res[name]=r; print(name,r)
etas=[0.5,0.2,0.05,0.01]; taus=[0.5,0.1,0.02]
cstar=2*gl(lambda a:np.sqrt(4*np.arcsinh(np.sin(a))),0,math.pi/2)
res['cstar']=cstar; print('c*',cstar)
for eta in etas:
    e=np.unique(np.concatenate([np.linspace(0,2,400001),[eta,1.5*eta,3*eta,eta*1.5,2*eta]]))
    rho=g(e,eta)**2
    rec(f'A1 eta={eta}',np.maximum(e-eta,0)-rho)
    k=e>=3*eta; rec(f'A2 eta={eta}',rho[k]-(e[k]-2*eta))
    B=3/math.sqrt(2*eta); gp=dg(e,eta)
    h=1e-7; cd=(g(e+h,eta)-g(np.maximum(e-h,0),eta))/(e+h-np.maximum(e-h,0))
    rec(f'A3 eta={eta}',B-np.abs(gp),dict(max_abs_gprime=float(np.abs(gp).max()),bound=B,fd_max=float(np.abs(cd).max()),maxdev_analytic_vs_fd_interior=float(np.abs(cd-gp)[e>h].max())))
    r2=lambda a: 2*g(eps(a),eta)**2
    crho=2*gl(lambda a:np.sqrt(r2(a)),0,math.pi/2)
    lo=cstar-math.pi*math.sqrt(6*eta)
    rec(f'A4 eta={eta}',[crho-lo,cstar-crho],dict(c_rho=crho,lower=lo,upper=cstar),tol=1e-8)
L=math.sqrt(4*math.asinh(1))
N=2000001; a=np.linspace(0,math.pi/2,N); ha=a[1]-a[0]
for eta in etas:
  for tau in taus:
    hyp=(tau/2<=math.pi/2) and (3*eta<=2) and eps(a).max()<=2
    p=np.sqrt(2)*g(eps(a),eta); chi=Sm((math.pi/2-a)/(tau/2))
    diff=np.concatenate([[0],np.cumsum((p*(1-chi))[1:]+(p*(1-chi))[:-1])*ha/2])  # f-ftilde
    rec(f'B1a ftilde<=f eta={eta} tau={tau}',diff,dict(hypothesis_ok=bool(hyp)),tol=1e-9)
    rec(f'B1b f-ftilde<=L tau/2 eta={eta} tau={tau}',L*tau/2-diff,dict(maxdiff=float(diff.max()),bound=L*tau/2),tol=1e-9)
    gp=dg(eps(a),eta)
    pp=np.sqrt(2)*gp*deps(a); dchi=-dSm((math.pi/2-a)/(tau/2))*2/tau
    f2=pp*chi+p*dchi; Bd=6/math.sqrt(eta)+3*L/tau
    rec(f'B2 eta={eta} tau={tau}',Bd-np.abs(f2),dict(max_abs=float(np.abs(f2).max()),bound=Bd))
    k=a<=math.pi/2-tau/2
    rec(f'B3 eta={eta} tau={tau}',1e-12-np.abs(diff[k]),dict(max_abs_diff=float(np.abs(diff[k]).max())),tol=0)
h=lambda s2:1+np.sqrt(1+1/s2)
ms=[];qual=0;tot=0
for S2 in np.linspace(0.01,2,401)[1:]:
  for D in np.linspace(0,S2/2,101):
    tot+=1
    if S2-D>0: qual+=1
    d=np.linspace(-D,D,41)
    bound=D/(2*(S2-D)**2*np.sqrt(1+1/(S2-D)))
    ms.append(bound-np.abs(h(S2+d)-h(S2)))
ms=np.concatenate(ms); rec('C1',ms,dict(cases_S2_D=tot,hypothesis_qualifying=qual))
x=np.unique(np.concatenate([np.arange(200000)/200000,1-np.geomspace(1e-12,1e-1,200)]))
x=x[x<1]
rec('D1',x/(2*(1-x))+0.5*np.log1p(-x),dict(note='margin=x/(2(1-x))-(-0.5log(1-x)), tail pts to 1-x=1e-12'))
cs=np.arange(1,10.01,0.25); mm=np.concatenate([c*x/2-0.5*np.log1p(c*x) for c in cs])
rec('D2',mm,dict(n_c=len(cs)))
with open('results.json','x') as fh: json.dump(res,fh,indent=1)
bad=[k for k,v in res.items() if isinstance(v,dict) and v['failed']>0]
print('FAILED ITEMS:',bad); sys.exit(0)
