"""Statement B. Predicates fixed before first run:
 PB0 (hypothesis per case, rule 4): K symmetric, entries>=0, max|rowsum-1|<1e-13 after Sinkhorn. Count qualifying instances.
 PB1: for qualifying instance with random F~N(0,1): |LHS-RHS| <= 1e-10*max(1,|LHS|,|RHS|)  (double rounding, n<=100, O(n^2) flops).
 Control: V=0 gives T=K, g=F, identity trivial (both sides equal); and a hand 2x2 K=[[.5,.5],[.5,.5]],V=0,F=(1,0): LHS=0.5.
 Seed 12345. Report max abs and max rel discrepancy."""
import numpy as np
rng=np.random.default_rng(12345)
def sink(n):
    A=rng.random((n,n))+0.01; A=(A+A.T)/2
    for _ in range(100000):
        r=A.sum(1); A=A/np.sqrt(np.outer(r,r))   # symmetric scaling
        A=(A+A.T)/2
        if np.abs(A.sum(1)-1).max()<1e-13: break
    return A
K0=np.array([[.5,.5],[.5,.5]]);F0=np.array([1.,0]);print("control",F0@((np.eye(2)-K0)@F0))
q=0;mabs=0;mrel=0;tot=0;bad=0
for n in (5,20,100):
    for _ in range(200):
        tot+=1;K=sink(n)
        if not(np.allclose(K,K.T,atol=0) or np.abs(K-K.T).max()<1e-15) or K.min()<0 or np.abs(K.sum(1)-1).max()>=1e-13: continue
        q+=1
        V=rng.uniform(0,3,n);F=rng.standard_normal(n);d=np.exp(-V/2)
        T=d[:,None]*K*d[None,:];g=d*F
        L=F@((np.eye(n)-T)@F);R=g@((np.eye(n)-K)@g)+g@((np.exp(V)-1)*g)
        a=abs(L-R);rl=a/max(1,abs(L),abs(R));mabs=max(mabs,a);mrel=max(mrel,rl);bad+=rl>1e-10
print("instances",tot,"qualify",q,"failed",bad,"max abs",mabs,"max rel",mrel)
