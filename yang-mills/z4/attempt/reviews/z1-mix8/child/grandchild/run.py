import numpy as np
rng=np.random.default_rng(12345)
def haar(n):
    g=rng.standard_normal((n,4)); return g/np.linalg.norm(g,axis=1,keepdims=True)
def mul(p,q):
    a0,a1,a2,a3=p.T; b0,b1,b2,b3=q.T
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0],1)
conj=lambda q:q*np.array([1,-1,-1,-1])
se=lambda x:x.std(ddof=1)/np.sqrt(len(x))
# STEP 1
q=haar(200000); c=q[:,0]**2
open('control.txt','x').write(f"E[a0^2]={c.mean():.5f} +- {se(c):.5f} (expected 0.25, N=200000, seed 12345)\n")
# STEP 2
N=400000; B=np.tile([0,1,0,0.],(N,1))
f=lambda u,v: mul(B,mul(u,conj(v)))[:,0]
fA=f(haar(N),haar(N)); fB=f(haar(N),haar(N))
v=fA**2; Var=v.mean(); jc=0.5*(fA-fB)**2; Jc=jc.mean()
J=Jc/24
# ratio SE via delta method on per-sample (jc, v)
r=Jc/(24*Var)
infl=(jc-Jc)/(24*Var)-(r/Var)*(v-Var)
rse=se(infl)
s=(f"Var(f1)={Var:.5f} +- {se(v):.5f} (pred 0.25)\nJ_colour={Jc:.5f} +- {se(jc):.5f} (pred 0.25)\n"
   f"J (24-colour avg)={J:.6f} +- {se(jc)/24:.6f}\nJ/Var={r:.6f} +- {rse:.6f} (pred 0.041667)\n"
   "Assumption: other 23 colours use disjoint independent links, so only this colour's (u,v) enters f1; J=J_colour/24.\n"
   "Var estimated from fA only (N=400000, seed 12345).\n")
open('result.txt','x').write(s); print(s)
