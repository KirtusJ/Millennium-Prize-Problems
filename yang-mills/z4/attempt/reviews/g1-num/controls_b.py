"""controls_b.py -- amended predicates after controls2 (C1, C4 Lanczos sub-test failed by own test design).
PREDICATES (fixed before run):
 C1b Miller e^-b I_n vs power series sum_k (b/2)^{2k+n}/(k!(k+n)!) e^-b (60 terms, b<=2: series converges to rounding),
     relative diff < 1e-13 for n<=20, b in {0.01,0.1,1,2}. (rounding ~1e-15 x n recursion steps)
 C1c Miller vs trapezoid for b in {16,64,128}, n<=40 where e^-b I_n > 1e-6: relative diff < 1e-9
     (trapezoid absolute error ~1e-16, divided by 1e-6 -> 1e-10; x10 margin).
 C4b U(1)^2, b=4 and 16, Lanczos (same Model.matvec) top 4 Ritz values: each within 1e-10 (relative to lambda0) of some exact product I_n1 I_n2.
"""
import numpy as np, math, json, lat
rep={}; fails=[]
w=0
for b in (0.01,0.1,1.,2.):
    m=lat.besselI_scaled_miller(20,b)
    for n in range(21):
        s=sum((b/2)**(2*k+n)/math.factorial(k)/math.factorial(k+n) for k in range(60))*math.exp(-b)
        w=max(w,abs(m[n]/s-1))
rep['C1b']=w; 
if not w<1e-13: fails.append('C1b')
w=0
for b in (16.,64.,128.):
    m=lat.besselI_scaled_miller(40,b); t=lat.besselI_scaled_trap(40,b); k=m>1e-6
    w=max(w,np.abs(t[k]/m[k]-1).max())
rep['C1c']=w
if not w<1e-9: fails.append('C1c')
rep['C4b']={}
for b in (4.,16.):
    nmax=12;Nth=64
    th=2*np.pi*np.arange(Nth)/Nth; fr=[0]+[f for f in range(1,nmax+1) for _ in (0,1)]
    Fu=np.zeros((1,len(fr),Nth));Fu[0,0]=1;j=1
    for f in range(1,nmax+1): Fu[0,j]=np.sqrt(2)*np.cos(f*th);Fu[0,j+1]=np.sqrt(2)*np.sin(f*th);j+=2
    z=np.zeros(Nth); U=lat.su2(th,(z,z,z+1)); Vu=(b*(1-lat.half_tr_comm(U[:,None],U[None,:])))[:,:,None]
    kn=lat.besselI_scaled_miller(nmax,b)[np.array(fr)]
    mu=lat.Model(Fu,np.ones((1,1)),np.full(Nth,1/Nth),np.ones(1),kn,Vu,np.ones((1,25,25)))
    tl,res,_,_=lat.lanczos_top(mu.matvec,lambda c:c,(1,25,25),k=4)
    ex=np.outer(kn,kn).ravel()
    d=max(np.abs(ex-x).min() for x in tl)/tl[0]
    rep['C4b'][str(b)]=dict(ritz_over_lam0=(tl/tl[0]).tolist(),maxdev=d)
    if not d<1e-10: fails.append('C4b@%g'%b)
rep['FAILED']=fails
open('results/controls_b.json','x').write(json.dumps(rep,indent=1))
print(json.dumps(rep,indent=1)); raise SystemExit(1 if fails else 0)
