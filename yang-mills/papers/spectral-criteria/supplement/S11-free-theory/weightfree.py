"""Free theory, blocking factor 2: the one-particle constant c = sup over coarse momenta of || Q w^-1 Q ||, with w
the one-particle energy in lattice units and Q the projection on the fine detail (whitened coordinates). By second
quantisation (I - Gamma(p) <= dGamma(1 - p)) this is a constant in the operator inequality  G <= c a H  on the
whole space of functions, and hence in the weight bound of the proposition on the refinement step from that bound.
PREDICATES (fixed before the first run):
 F1 for N in {4,8,16,32,64} and every coarse momentum: ||Q w^-1 Q|| <= (14/sqrt3) sinh(w_k)/w_k + 1/arcosh(2)
    at that momentum (k != 0), and <= 1/arcosh(2) at k = 0; in particular c <= 15.94 (the proved bound).
 F2 for N in {8,16,32,64} the maximum is attained at a lowest axial momentum or its mirror image.
 F3 at q = (1,0,0), N = 2^20, the value is within 1e-5 of lambda_max(diag(1/arcosh 3, 1/arcosh 3, 1/arcosh 5)
    + v v^T / 2), v = (sqrt(2/sqrt8), sqrt(2/sqrt8), sqrt(2/sqrt24)) (limit conjectured before the run from the
    constraint, as for the rate).
No random numbers. Output weightfree_result.txt (not overwritten). Command: python3 weightfree.py"""
import numpy as np, itertools
def omega(p): return np.arccosh(1+0.5*sum(4*np.sin(x/2)**2 for x in p))
def islow(p): return all(((x+np.pi/2)%(2*np.pi))<np.pi for x in p)
def val(N,q):
    k=np.array([2*np.pi*q[i]/N for i in range(3)]); d2=np.exp(2j*k)-1
    PT=None if np.linalg.norm(d2)<1e-11 else np.eye(3)-np.outer(d2,d2.conj())/np.vdot(d2,d2).real
    Fs=[];ws=[];wk=None
    for eta in itertools.product(range(2),repeat=3):
        p=k+np.pi*np.array(eta)
        if all(abs(np.sin(x/2))<1e-12 for x in p): continue
        d=np.exp(1j*p)-1; w=omega(p)
        U,_,_=np.linalg.svd(np.eye(3)-np.outer(d,d.conj())/np.vdot(d,d).real); Bp=U[:,:2]
        Fs.append(np.zeros((3,2),complex) if PT is None else PT@np.diag(1+np.exp(1j*p))@Bp/np.sqrt(2*np.sinh(w)))
        ws+=[w]*2
        if islow(p): wk=w
    F=np.hstack(Fs); ws=np.array(ws)
    _,s,Vh=np.linalg.svd(F); rank=int((s>1e-10*max(s.max(),1e-300)).sum()) if s.max()>0 else 0
    ker=Vh[rank:].conj().T; T=ker.conj().T@np.diag(1/ws)@ker
    return np.linalg.eigvalsh((T+T.conj().T)/2).max(), wk
out=[]; F1=F2=True
for N in (4,8,16,32,64):
    c=0; arg=[]
    for q in itertools.product(range(N//2),repeat=3):
        v,wk=val(N,q)
        bound=1/np.arccosh(2) if (not any(q) or wk is None) else (14/np.sqrt(3))*np.sinh(wk)/wk+1/np.arccosh(2)
        F1&=v<=bound+1e-10
        if v>c+1e-12: c=v;arg=[q]
        elif abs(v-c)<=1e-12: arg.append(q)
    ok=any(sorted(min(x,N//2-x) for x in q)==[0,0,1] for q in arg)
    if N>=8: F2&=ok
    out.append("N=%d c=%.6f attained at %s"%(N,c,arg))
v=np.array([np.sqrt(2/np.sqrt(8)),np.sqrt(2/np.sqrt(8)),np.sqrt(2/np.sqrt(24))])
lim=np.linalg.eigvalsh(np.diag([1/np.arccosh(3),1/np.arccosh(3),1/np.arccosh(5)])+np.outer(v,v)/2).max()
x,_=val(2**20,(1,0,0)); F3=abs(x-lim)<1e-5
out.append("axial, N=2^20: %.8f ; conjectured limit %.8f"%(x,lim))
for n,m in zip(("F1","F2","F3"),(F1,F2,F3)): out.append("%s %s"%(n,"MET" if m else "FAILED"))
open('weightfree_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
