"""Predicates (fixed before first run). N=10^6 random (p,q), seed 20260101.
Mix: 40% generic scale-ratio log-uniform |q|/|p| in [1e-3,1e3]; 15% q small (<=1e-3|p|); 15% comparable (ratio 0.3..3);
 10% p_perp=0; 5% q=0; 5% q=2p (w=0); 5% q=-2p (u=0); 5% q parallel to p (random lambda).
Tolerance: tol = 1e-12*(|p|^2+|q|^2) (a few double ulps ~2.2e-16 times ~1e3 amplification from sqrt/div/cancellation in
 |u|^2-type sums; all quantities scale like |p|^2+|q|^2). Exact-zero special cases are generated exactly.
P0 claim: L=4g(u)g(w) >= p1^2+p2^2-p3^2-(3/4)|q|^2 - tol
P1 (i): exp(-2s(|u|^2+|w|^2)) == exp(-4s|p|^2)exp(-s|q|^2), compared in log-space: |2s(|u|^2+|w|^2)-(4s|p|^2+s|q|^2)| <= 1e-12*s*(|p|^2+|q|^2), s in (0,5]
P2 (ii): |u||w| <= |p|^2+|q|^2/4 + tol
P3 (iii): |u_perp|^2|w_perp|^2 >= (|p_perp|^2-|q_perp|^2/4)^2 - tol*scale
P4 (iv): L >= |p_perp|^4/|p|^2 - (3/4)|q|^2 - tol  (p=0 -> term 0)
Hypothesis count: 'for all' cases tested only where g defined nondegenerate; report counts of u=0/w=0/p_perp=0/q=0 cases.
Also reports min of (L-RHS) absolute and relative to scale, with location.
"""
import numpy as np
rng=np.random.default_rng(20260101)
N=10**6
def unit(n):
    v=rng.normal(size=(n,3)); return v/np.linalg.norm(v,axis=1)[:,None]
pm=10.0**rng.uniform(-3,3,N)
p=unit(N)*pm[:,None]
ratio=10.0**rng.uniform(-3,3,N)
kind=rng.random(N)
q=unit(N)*(pm*ratio)[:,None]
c=kind<0.15; q[c]=unit(c.sum())*(pm[c]*1e-3*rng.random(c.sum()))[:,None]
c=(kind>=0.15)&(kind<0.30); q[c]=unit(c.sum())*(pm[c]*rng.uniform(.3,3,c.sum()))[:,None]
c=(kind>=0.30)&(kind<0.40); p[c,0]=0;p[c,1]=0
c=(kind>=0.40)&(kind<0.45); q[c]=0
c=(kind>=0.45)&(kind<0.50); q[c]=2*p[c]
c=(kind>=0.50)&(kind<0.55); q[c]=-2*p[c]
c=(kind>=0.55)&(kind<0.60); q[c]=rng.uniform(-10,10,(c.sum(),1))*p[c]
# also sub-case p_perp=0 with q random for first part of last 10%
c=(kind>=0.60)&(kind<0.62); p[c,0]=0;p[c,1]=0; q[c]=unit(c.sum())*(pm[c]*1e-2*rng.random(c.sum()))[:,None]
u=p+q/2; w=q/2-p
n=lambda v:np.linalg.norm(v,axis=1)
def g(v):
    nv=n(v); out=np.zeros(N); m=nv>0
    out[m]=(v[m,0]**2+v[m,1]**2)/(2*nv[m]); return out
L=4*g(u)*g(w)
sc=(p**2).sum(1)+(q**2).sum(1); tol=1e-12*sc
rhs=p[:,0]**2+p[:,1]**2-p[:,2]**2-0.75*(q**2).sum(1)
d=L-rhs
res={}
res['counts']=dict(N=N,u0=int((n(u)==0).sum()),w0=int((n(w)==0).sum()),pperp0=int(((p[:,0]==0)&(p[:,1]==0)).sum()),q0=int((n(q)==0).sum()),nondeg=int(((n(u)>0)&(n(w)>0)).sum()))
i=np.argmin(d/sc)
res['P0']=dict(viol=int((d<-tol).sum()),min_abs=float(d.min()),argmin_abs=int(np.argmin(d)),min_rel=float((d/sc)[i]),loc_rel=dict(p=p[i].tolist(),q=q[i].tolist(),L=float(L[i]),rhs=float(rhs[i])),
 tight_rel_lt_1em6=int((d/sc<1e-6).sum()),tight_exact_le_tol=int((np.abs(d)<=tol).sum()))
j=np.argmin(d); res['P0']['loc_abs']=dict(p=p[j].tolist(),q=q[j].tolist(),L=float(L[j]),rhs=float(rhs[j]))
s=rng.uniform(1e-3,5,N)
lhs_e=2*s*((u**2).sum(1)+(w**2).sum(1)); rhs_e=4*s*(p**2).sum(1)+s*(q**2).sum(1)
bad=np.abs(lhs_e-rhs_e)>1e-12*s*sc
res['P1']=dict(viol=int(bad.sum()),maxrel=float((np.abs(lhs_e-rhs_e)/(s*sc)).max()))
a=n(u)*n(w); b=(p**2).sum(1)+(q**2).sum(1)/4
res['P2']=dict(viol=int((a>b+tol).sum()),max_a_minus_b_rel=float(((a-b)/sc).max()),tight=int((np.abs(a-b)<=tol).sum()))
up=u[:,:2];wp=w[:,:2];pp=(p[:,:2]**2).sum(1);qp=(q[:,:2]**2).sum(1)
l3=(up**2).sum(1)*(wp**2).sum(1); r3=(pp-qp/4)**2
res['P3']=dict(viol=int((l3<r3-tol*sc).sum()),min_rel=float(((l3-r3)/sc**2).min()),tight_rel_lt_1em9=int((((l3-r3)/sc**2)<1e-9).sum()))
p2=(p**2).sum(1); r4=np.where(p2>0,pp**2/np.where(p2>0,p2,1),0)-0.75*(q**2).sum(1)
d4=L-r4
res['P4']=dict(viol=int((d4<-tol).sum()),min_abs=float(d4.min()),min_rel=float((d4/sc).min()),loc=dict(p=p[np.argmin(d4/sc)].tolist(),q=q[np.argmin(d4/sc)].tolist()),tight_rel_lt_1em6=int((d4/sc<1e-6).sum()))
import json
with open('results.json','x') as f: json.dump(res,f,indent=1)
print(json.dumps(res,indent=1))
