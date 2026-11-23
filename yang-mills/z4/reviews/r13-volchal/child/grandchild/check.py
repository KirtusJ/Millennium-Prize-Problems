"""Predicates (stated before first run):
P_A: for p=(0,0,t), L >= -t^2-(3/4)|q|^2 - tol, tol=1e-12*(1+|RHS|)
P_B: for q=lam*p, L >= p1^2+p2^2-p3^2-(3/4)|q|^2 - tol
Tolerance: ~1e-12 relative is a few thousand double ulps (eps=2.2e-16), covering
rounding of norms/products; not a mathematical slack.
Slack 'tight' = min(L-RHS) < 1e-9 (absolute) anywhere.
Analytic: A: L=rho^4/(|u||w|), rho^2=(q1^2+q2^2)/4 >=0 so L>=0>=RHS.
B: L=|lam^2-4| h^2, h=(p1^2+p2^2)/(2|p|).
"""
import numpy as np
from ctl import L
rng=np.random.default_rng(12345); N=200000
out=[]
def rep(name,p,q,rhs,Lv,extra):
    d=Lv-rhs; tol=1e-12*(1+np.abs(rhs)); viol=int((Lv<rhs-tol).sum()); i=int(np.argmin(d))
    out.append(f"{name}: min(L-RHS)={d[i]:.6e} at p={p[i].tolist()} q={q[i].tolist()} L={Lv[i]:.6e} RHS={rhs[i]:.6e}; violations={viol}; tight(<1e-9)={int((d<1e-9).sum())} samples; max|L-analytic|/(1+L)={extra:.2e}")
def mag(n):
    t=10.0**rng.uniform(-8,3,n)*rng.choice([-1,1],n)
    t[rng.random(n)<0.05]=0.0
    return t
# A
t=mag(N); p=np.zeros((N,3)); p[:,2]=t
r=np.abs(t)*10*rng.random(N); r[rng.random(N)<0.1]=0
r[rng.random(N)<0.05]=10*np.abs(t)[rng.random(N)<0.05].mean()*0  # no-op keep zero
d=rng.normal(size=(N,3)); d/=np.linalg.norm(d,axis=1)[:,None]; q=d*r[:,None]
q[rng.random(N)<0.05]=0
q[:2]=0; p[0,2]=0; p[1,2]=1.0
Lv=L(p,q); rhs=-p[:,2]**2-0.75*(q**2).sum(1)
u=p+q/2; w=q/2-p; rho2=(q[:,0]**2+q[:,1]**2)/4; nu=np.linalg.norm(u,axis=1); nw=np.linalg.norm(w,axis=1)
an=np.where(nu*nw>0,rho2**2/np.where(nu*nw>0,nu*nw,1),0)
rep("A",p,q,rhs,Lv,float(np.max(np.abs(Lv-an)/(1+Lv))))
# B
p=rng.normal(size=(N,3))*10.0**rng.uniform(-4,3,(N,1))
p[rng.random(N)<0.05]=0
lam=rng.uniform(-10,10,N); k=rng.random(N); lam[k<0.05]=2; lam[(k>=0.05)&(k<0.1)]=-2; lam[(k>=0.1)&(k<0.13)]=0
q=lam[:,None]*p
Lv=L(p,q); rhs=p[:,0]**2+p[:,1]**2-p[:,2]**2-0.75*(q**2).sum(1)
n=np.linalg.norm(p,axis=1); h=np.where(n>0,(p[:,0]**2+p[:,1]**2)/(2*np.where(n>0,n,1)),0)
an=np.abs(lam**2-4)*h**2
rep("B",p,q,rhs,Lv,float(np.max(np.abs(Lv-an)/(1+Lv))))
open_s=open("results.txt","x"); open_s.write("\n".join(out)+"\n"); open_s.close(); print("\n".join(out))
