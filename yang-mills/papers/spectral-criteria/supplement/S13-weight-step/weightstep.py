"""Random finite-dimensional test of the refinement step under a linear bound on the low-energy weight of the fine
detail (the proposition at the end of the section on the refinement inequality).
Statement tested. H symmetric with smallest eigenvalue x > 0, a > 0, A = exp(-aH), m >= j >= 1 integers, P a
projection, B a projection inside the range of I - P, G = I - P - B, kappa = ||B A^j B||, b = 1 - ||P A^m P||,
F(u) = ||G E((0,u]) G||, and K any number with F(u) <= K a u for 0 < u <= 1/a. Then with d = 1 - exp(-m a x):
 (T1) ||G H^-1 G|| <= a (1 + K log+(1/(a x)))
 (T2) 1/gamma_opt = ||G (I - A^2)^-1 G|| <= 3/2 + (K/2) log+(1/(a x))
 (T3) d (1 + (3 + K log(m/d))/m) >= b - kappa
 (T4) d >= (b - kappa - K/(e m)) / (1 + (3 + K log m)/m)
PREDICATES (fixed before the first run): over 20000 random instances (seed 11), with K taken as the smallest
admissible value, the maximum of F(u)/(a u) over the eigenvalues u <= 1/a (0 if there is none): each of T1..T4
holds with tolerance 1e-10 (relative to the larger side for T1, T2). The hypothesis is tested per instance by
construction of K; the program reports how many instances have a positive right side in T4 (the others test
nothing in T4) and the smallest slack in each inequality.
Output weightstep_result.txt (not overwritten). Command: python3 weightstep.py"""
import numpy as np
rng=np.random.default_rng(11); out=[]; fails=[0,0,0,0]; slack=[np.inf]*4; pos=0; n_inst=20000; Kmax=0
for it in range(n_inst):
    n=int(rng.integers(6,30)); a=10**rng.uniform(-2,-0.3); m=int(rng.integers(1,200)); j=int(rng.integers(1,m+1))
    lo=10**rng.uniform(-3,1); ev=np.sort(lo*10**(rng.uniform(0,rng.uniform(0.5,4),size=n))); ev[0]=lo
    Qm,_=np.linalg.qr(rng.normal(size=(n,n))); H=(Qm*ev)@Qm.T
    r=int(rng.integers(1,n)); W,_=np.linalg.qr(rng.normal(size=(n,n)))
    if rng.random()<0.5:                                   # coarse space close to the low-energy space
        W,_=np.linalg.qr(Qm+10**rng.uniform(-3,0)*rng.normal(size=(n,n)))
    Pp=W[:,:r]@W[:,:r].T; s=int(rng.integers(0,n-r+1)) if rng.random()<0.5 else 0
    Bp=W[:,r:r+s]@W[:,r:r+s].T; G=np.eye(n)-Pp-Bp
    A=(Qm*np.exp(-a*ev))@Qm.T; Aj=(Qm*np.exp(-a*j*ev))@Qm.T; Am=(Qm*np.exp(-a*m*ev))@Qm.T
    nrm=lambda M: np.linalg.norm(M,2)
    kappa=nrm(Bp@Aj@Bp) if s else 0.0; b=1-nrm(Pp@Am@Pp); x=ev[0]; d=1-np.exp(-m*a*x)
    K=0.0
    for k in range(n):
        if ev[k]<=1/a:
            V=Qm[:,:k+1]; K=max(K,np.linalg.eigvalsh(V.T@G@V).max()/(a*ev[k]))
    K=max(K,0.0); Kmax=max(Kmax,K); lp=max(0.0,np.log(1/(a*x)))
    t1l=nrm(G@(Qm/ev)@Qm.T@G); t1r=a*(1+K*lp)
    t2l=nrm(G@(Qm/(1-np.exp(-2*a*ev)))@Qm.T@G); t2r=1.5+0.5*K*lp
    t3=d*(1+(3+K*np.log(m/d))/m)-(b-kappa)
    rhs=(b-kappa-K/(np.e*m))/(1+(3+K*np.log(m))/m); t4=d-rhs; pos+=rhs>0
    for i,(v,sc) in enumerate(((t1r-t1l,max(t1r,1e-300)),(t2r-t2l,t2r),(t3,1),(t4,1))):
        slack[i]=min(slack[i],v/sc); fails[i]+=v/sc<-1e-10
out.append("instances %d ; right side of T4 positive in %d ; largest K %.3f"%(n_inst,pos,Kmax))
for i in range(4): out.append("T%d: failures %d, smallest slack %.3e : %s"%(i+1,fails[i],slack[i],"MET" if fails[i]==0 else "FAILED"))
open('weightstep_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
