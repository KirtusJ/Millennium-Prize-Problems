"""Random finite-dimensional test of the one-step criterion (the proposition after the remark on where the infrared
problem sits). H symmetric positive definite, P a projection, Q = I - P, t > 0;
kappa = ||Q H^-1 Q|| (the best constant in Q <= kappa H), b = 1 - ||P exp(-tH) P||, d = 1 - ||exp(-tH)||.
PREDICATES (fixed before the first run), 20000 instances, seed 12, tolerance 1e-10:
 C1 d >= b / (1 + kappa/t)
 C2 (converse, with Delta the smallest eigenvalue) kappa <= 1/Delta and b >= d
 C3 (minorisation) for a random reversible finite Markov chain with stationary law pi and a random partition into
    coarse classes: with eps = min over pairs of classes (I,J) of Prob(C_0=I, C_n=J)/(pi(I) pi(J)), the norm of
    P A^n P on centred functions is at most 1 - eps. (2000 chains, n random in 1..5.)
Reported: smallest slack in C1 and the largest ratio (b/(1+kappa/t))/d, which shows how sharp C1 can be.
Output onestepcrit_result.txt (not overwritten). Command: python3 onestepcrit.py"""
import numpy as np
rng=np.random.default_rng(12); out=[]; f1=f2=f3=0; s1=np.inf; best=0
for it in range(20000):
    n=int(rng.integers(3,25)); lo=10**rng.uniform(-3,1); ev=np.sort(lo*10**rng.uniform(0,rng.uniform(0.3,3),size=n)); ev[0]=lo
    U,_=np.linalg.qr(rng.normal(size=(n,n))); t=10**rng.uniform(-2,2)
    W,_=np.linalg.qr(U+10**rng.uniform(-3,0.5)*rng.normal(size=(n,n))) if rng.random()<0.6 else np.linalg.qr(rng.normal(size=(n,n)))
    r=int(rng.integers(1,n)); Pp=W[:,:r]@W[:,:r].T; Q=np.eye(n)-Pp
    kap=np.linalg.norm(Q@(U/ev)@U.T@Q,2); b=1-np.linalg.norm(Pp@(U*np.exp(-t*ev))@U.T@Pp,2); d=1-np.exp(-t*ev[0])
    v=d-b/(1+kap/t); s1=min(s1,v); f1+=v<-1e-10; best=max(best,(b/(1+kap/t))/d)
    f2+=(kap>1/ev[0]+1e-10) or (b<d-1e-10)
for it in range(2000):
    n=int(rng.integers(4,16)); Wt=rng.random((n,n))**rng.uniform(1,4); Wt=Wt+Wt.T; pi=Wt.sum(1)/Wt.sum(); Pm=Wt/Wt.sum(1)[:,None]
    k=int(rng.integers(2,min(n,5)+1)); lab=np.concatenate([np.arange(k),rng.integers(0,k,size=n-k)]); rng.shuffle(lab)
    nn=int(rng.integers(1,6)); Pn=np.linalg.matrix_power(Pm,nn)
    Z=np.zeros((n,k)); Z[np.arange(n),lab]=1; piC=Z.T@pi; J=Z.T@(pi[:,None]*Pn)@Z; eps=(J/np.outer(piC,piC)).min()
    S=np.sqrt(pi)[:,None]*Pn/np.sqrt(pi)[None,:]                      # symmetric form of A^n on L2(pi)
    B=(np.sqrt(pi)[:,None]*Z)/np.sqrt(piC)[None,:]                    # orthonormal basis of coarse functions
    M=B.T@S@B; one=np.sqrt(piC); M=M-np.outer(one,one)                # remove constants
    f3+=np.linalg.norm(M,2)>1-eps+1e-10
out.append("C1 failures %d, smallest slack %.3e, largest (bound/d) %.4f : %s"%(f1,s1,best,"MET" if f1==0 else "FAILED"))
out.append("C2 failures %d : %s"%(f2,"MET" if f2==0 else "FAILED"))
out.append("C3 failures %d : %s"%(f3,"MET" if f3==0 else "FAILED"))
open('onestepcrit_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
