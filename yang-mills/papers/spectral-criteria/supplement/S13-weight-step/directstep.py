"""Check of two statements proposed by a reviewing model after the baseline of 42 pages: direct forms of the
refinement step from a weight bound and of the one-step criterion, proved from spectral subspaces.
Setting: H symmetric, P, B, G = I - P - B mutually orthogonal projections, t > 0, 0 < s <= t,
b = 1 - ||P exp(-tH) P||, kappa = ||B exp(-sH) B||, d = 1 - ||exp(-tH)||.
PREDICATES (fixed before the first run), 20000 random instances, seed 21, tolerance 1e-10:
 D1 (the three vector inequalities of the proof) for a random unit vector v in the span of the eigenvectors with
    energy <= u, u an eigenvalue: ||Pv||^2 <= (1-b) exp(tu), ||Bv||^2 <= kappa exp(su), ||Gv||^2 <= F(u),
    F(u) = ||G E([0,u]) G||.
 D2 (weight form) with a > 0, m = t/a, c_w the smallest constant with F(u) <= c_w a u for the eigenvalues
    u <= 1/a (0 if none) and C = max(1, c_w):  d >= (b - kappa)_+ / (1 + C/m); H positive definite here.
 D3 (one-step form) with K = ||G H^-1 G||:  d >= (b - kappa)_+ / (1 + K/t), s/t an arbitrary real ratio.
 D4 (kernel) the same as D3 when H has a one-dimensional kernel on which G vanishes (2000 further instances; K is
    then the norm of G H^+ G with the pseudo-inverse); the left side is 0, so the claim is b <= kappa.
 D5 (comparison) the bound of D2 is never smaller than the bound of the 42-page Proposition 5.7,
    (b - kappa - c_w/(e m)) / (1 + (3 + c_w log m)/m), when m >= 1 (reported: how often it is larger).
Output directstep_result.txt (not overwritten). Command: python3 directstep.py"""
import numpy as np
rng=np.random.default_rng(21); out=[]; f=[0]*6; slack=[np.inf]*6; pos=0; larger=0
def inst(kernel=False):
    n=int(rng.integers(4,22)); lo=10**rng.uniform(-3,1); ev=np.sort(lo*10**rng.uniform(0,rng.uniform(0.3,3),size=n)); ev[0]=0.0 if kernel else lo
    U,_=np.linalg.qr(rng.normal(size=(n,n)))
    W,_=np.linalg.qr(U+10**rng.uniform(-3,0.5)*rng.normal(size=(n,n))) if rng.random()<0.6 else np.linalg.qr(rng.normal(size=(n,n)))
    if kernel: W[:,0]=U[:,0]; W,_=np.linalg.qr(W)            # the kernel vector lies in the range of P
    r=int(rng.integers(1,n-1)); sB=int(rng.integers(0,n-r)) if rng.random()<0.6 else 0
    P=W[:,:r]@W[:,:r].T; B=W[:,r:r+sB]@W[:,r:r+sB].T; G=np.eye(n)-P-B
    t=10**rng.uniform(-2,2); s=t*rng.uniform(0.01,1.0); return n,ev,U,P,B,G,t,s,sB
nrm=lambda M: np.linalg.norm(M,2)
for it in range(20000):
    n,ev,U,P,B,G,t,s,sB=inst(); fn=lambda g:(U*g(ev))@U.T
    b=1-nrm(P@fn(lambda e:np.exp(-t*e))@P); kap=nrm(B@fn(lambda e:np.exp(-s*e))@B) if sB else 0.0; d=1-np.exp(-t*ev[0])
    k=int(rng.integers(0,n)); u=ev[k]; V=U[:,:k+1]; c=rng.normal(size=k+1); v=V@(c/np.linalg.norm(c)); F=np.linalg.eigvalsh(V.T@G@V).max()
    for i,val in enumerate(((1-b)*np.exp(t*u)-v@P@v, kap*np.exp(s*u)-v@B@v, F-v@G@v)):
        if i<1 or True: slack[0]=min(slack[0],val); f[0]+=val<-1e-10
    a=10**rng.uniform(-2.5,0.5); m=t/a; cw=0.0
    for kk in range(n):
        if ev[kk]<=1/a: Vk=U[:,:kk+1]; cw=max(cw,np.linalg.eigvalsh(Vk.T@G@Vk).max()/(a*ev[kk]))
    C=max(1.0,cw); rhs=max(b-kap,0)/(1+C/m); val=d-rhs; slack[1]=min(slack[1],val); f[1]+=val<-1e-10; pos+=rhs>0
    K=nrm(G@fn(lambda e:1/e)@G); val=d-max(b-kap,0)/(1+K/t); slack[2]=min(slack[2],val); f[2]+=val<-1e-10
    if m>=1:
        old=(b-kap-cw/(np.e*m))/(1+(3+cw*np.log(m))/m); val=rhs-old; slack[4]=min(slack[4],val); f[4]+=val<-1e-10; larger+=val>1e-12
for it in range(2000):
    n,ev,U,P,B,G,t,s,sB=inst(kernel=True); fn=lambda g:(U*g(ev))@U.T
    b=1-nrm(P@fn(lambda e:np.exp(-t*e))@P); kap=nrm(B@fn(lambda e:np.exp(-s*e))@B) if sB else 0.0
    val=kap-b; slack[3]=min(slack[3],val); f[3]+=val<-1e-10
out.append("D1 failures %d, smallest slack %.3e : %s"%(f[0],slack[0],"MET" if f[0]==0 else "FAILED"))
out.append("D2 failures %d, smallest slack %.3e, right side positive in %d instances : %s"%(f[1],slack[1],pos,"MET" if f[1]==0 else "FAILED"))
out.append("D3 failures %d, smallest slack %.3e : %s"%(f[2],slack[2],"MET" if f[2]==0 else "FAILED"))
out.append("D4 failures %d, smallest slack %.3e : %s"%(f[3],slack[3],"MET" if f[3]==0 else "FAILED"))
out.append("D5 failures %d, smallest difference %.3e, strictly larger in %d instances : %s"%(f[4],slack[4],larger,"MET" if f[4]==0 else "FAILED"))
open('directstep_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
