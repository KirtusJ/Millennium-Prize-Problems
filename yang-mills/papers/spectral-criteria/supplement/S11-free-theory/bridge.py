"""Free theory: the sufficient form (b) of the remark on Hypothesis h:mix. beta*P = largest eigenvalue of the covariance of the
transverse potential conditioned on the coarse observation (units 1/beta); beta*L = max_p exp(-w_p) (covariance of the next slice
given the present one). Reports beta^2 P L and the bound 1/(1+beta^2 P L) next to the exact gamma, r=2.
PREDICATE (fixed before the run): for N in {4,8,16,32}: 1/(1+beta^2 P L) <= gamma_exact + 1e-9 (the bridge is a valid lower bound)."""
import numpy as np, itertools
src=open('blockr.py').read(); exec(src[src.index("def omega"):src.index("def block")])
def blk(N,q):
    r=2; k=np.array([2*np.pi*q[i]/N for i in range(3)]); drk=np.exp(1j*r*k)-1
    PT=None if np.linalg.norm(drk)<1e-11 else np.eye(3)-np.outer(drk,drk.conj())/np.vdot(drk,drk).real
    Fs=[];Rs=[];cs=[]
    for eta in itertools.product(range(r),repeat=3):
        p=k+2*np.pi*np.array(eta)/r
        if all(abs(np.sin(x/2))<1e-12 for x in p): continue
        d=np.exp(1j*p)-1; w=omega(p)
        U,_,_=np.linalg.svd(np.eye(3)-np.outer(d,d.conj())/np.vdot(d,d).real); Bp=U[:,:2]
        D=np.diag(1+np.exp(1j*p))
        Fs.append(np.zeros((3,2),complex) if PT is None else PT@D@Bp/np.sqrt(2*np.sinh(w)))
        Rs+=[np.exp(-w)]*2; cs+=[1/(2*np.sinh(w))]*2
    F=np.hstack(Fs); Rs=np.array(Rs); cs=np.array(cs)
    _,s,Vh=np.linalg.svd(F); rank=int((s>1e-10*max(s.max(),1e-300)).sum()) if s.max()>0 else 0
    ker=Vh[rank:].conj().T
    T=ker.conj().T@np.diag(1/(1-Rs**2))@ker; gam=1/np.linalg.eigvalsh((T+T.conj().T)/2).max()
    Pm=ker.conj().T@np.diag(cs)@ker; P=np.linalg.eigvalsh((Pm+Pm.conj().T)/2).max()
    return gam,P,Rs.max()
out=[];ok=True
for N in (4,8,16,32):
    g=np.inf;P=0;L=0
    for q in itertools.product(range(N//2),repeat=3):
        a,b,c=blk(N,q); g=min(g,a); P=max(P,b); L=max(L,c)
    bound=1/(1+P*L); ok&=bound<=g+1e-9
    out.append("N=%d beta*P=%.5f beta*L=%.5f beta^2PL=%.5f bridge bound=%.5f exact gamma=%.5f"%(N,P,L,P*L,bound,g))
out.append("predicate %s"%("MET" if ok else "FAILED"))
open('bridge_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
