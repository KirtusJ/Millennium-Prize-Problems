"""Free theory with integer blocking factor r (a reviewing model's proposed extension).
Whitened transverse coordinates; r^3 aliases p = k + 2 pi eta / r; link-blocking multiplier D_r(p)_jj = sum_{l<r} e^{i l p_j};
coarse observation F_eta = Pi_T(r k) D_r(p_eta)|_{d(p_eta)^perp} / sqrt(2 sinh w), defined as 0 when d(rk)=0.
gamma = 1/||Q (I-R^2)^{-1} Q||, Q = projection on ker F.
PREDICATES (fixed before the run):
 B1 r=2: gamma(N) equals the values of maxwell.py for N=4,8,16 (0.928203, 0.876241, 0.801969) to 1e-6 (full minimum over coarse momenta).
 B2 for r in {2,3,4,5} and all coarse momenta at N = r*{2,3,4} (and N=24 for r=3): gamma >= (1 + r/4 + pi^2 r^3/16)^(-1).
 B3 on ker F for every nonzero coarse momentum: largest eigenvalue of the compression of
    J = diag(I on low alias, -(pi^2 r^3/8) sinh(w_k) I on high aliases) is <= 1e-9; for r=2 also with constant 14/sqrt3.
 B4 axial values: r=3,N=24: 0.609454; r=4,N=32: 0.470448; r=5,N=40: 0.376053 (lowest axial coarse momentum), to 1e-5.
Output blockr_result.txt (not overwritten)."""
import numpy as np, itertools
def omega(p): return np.arccosh(1+sum(4*np.sin(x/2)**2 for x in p)/2)
def princ(x): return (x+np.pi)%(2*np.pi)-np.pi
def block(N,r,q,cst=None):
    k=np.array([2*np.pi*q[i]/N for i in range(3)])           # representative; aliases k + 2 pi eta / r
    drk=np.exp(1j*r*k)-1
    PT=None if np.linalg.norm(drk)<1e-11 else np.eye(3)-np.outer(drk,drk.conj())/np.vdot(drk,drk).real
    Fs=[];Rs=[];low=[];wk=None
    for eta in itertools.product(range(r),repeat=3):
        p=k+2*np.pi*np.array(eta)/r
        if all(abs(np.sin(x/2))<1e-12 for x in p): continue
        d=np.exp(1j*p)-1; w=omega(p)
        U,_,_=np.linalg.svd(np.eye(3)-np.outer(d,d.conj())/np.vdot(d,d).real); Bp=U[:,:2]
        D=np.diag([sum(np.exp(1j*l*x) for l in range(r)) for x in p])
        Fs.append(np.zeros((3,2),complex) if PT is None else PT@D@Bp/np.sqrt(2*np.sinh(w)))
        il=all(abs(princ(x))<=np.pi/r+1e-12 for x in p) and all(princ(x)< np.pi/r-1e-12 or abs(princ(x)+np.pi/r)<1e-12 or abs(princ(x))<np.pi/r-1e-12 for x in p)
        il=all(-np.pi/r-1e-12<=princ(x)<np.pi/r-1e-12 for x in p)
        Rs+=[np.exp(-w)]*2; low+=[il]*2
        if il: wk=w
    F=np.hstack(Fs); Rs=np.array(Rs); low=np.array(low)
    _,s,Vh=np.linalg.svd(F); rank=int((s>1e-10*max(s.max(),1e-300)).sum()) if s.max()>0 else 0
    ker=Vh[rank:].conj().T
    T=ker.conj().T@np.diag(1/(1-Rs**2))@ker
    gam=1/np.linalg.eigvalsh((T+T.conj().T)/2).max()
    jmax=None
    if wk is not None and PT is not None:
        c=(np.pi**2*r**3/8) if cst is None else cst
        J=np.diag(np.where(low,1.0,-c*np.sinh(wk)))
        Jc=ker.conj().T@J@ker; jmax=np.linalg.eigvalsh((Jc+Jc.conj().T)/2).max()
    return gam,jmax
def allq(N,r,cst=None):
    g=np.inf; jm=-np.inf
    for q in itertools.product(range(N//r),repeat=3):
        a,b=block(N,r,q,cst); g=min(g,a)
        if b is not None: jm=max(jm,b)
    return g,jm
out=[]
ref={4:0.928203,8:0.876241,16:0.801969}
ok=True
for N,v in ref.items():
    g,_=allq(N,2); ok&=abs(g-v)<1e-6; out.append("r=2 N=%d gamma=%.6f (maxwell.py %.6f)"%(N,g,v))
out.append("B1 %s"%("MET" if ok else "FAILED"))
ok2=True; ok3=True
for r in (2,3,4,5):
    bound=1/(1+r/4+np.pi**2*r**3/16)
    for mult in ((2,3,4,8) if r==3 else (2,3,4)):
        N=r*mult; g,jm=allq(N,r)
        ok2&=g>=bound; ok3&=(jm<=1e-9)
        out.append("r=%d N=%d min gamma=%.6f bound=%.6f max eig J-compression=%.6f"%(r,N,g,bound,jm))
g,jm=allq(16,2,14/np.sqrt(3)); ok3&=(jm<=1e-9); out.append("r=2 N=16 with constant 14/sqrt3: max eig J-compression=%.6f"%jm)
g,jm=allq(32,2,14/np.sqrt(3)); ok3&=(jm<=1e-9); out.append("r=2 N=32 with constant 14/sqrt3: max eig J-compression=%.6f"%jm)
out.append("B2 %s"%("MET" if ok2 else "FAILED")); out.append("B3 %s"%("MET" if ok3 else "FAILED"))
ax={(3,24):0.609454,(4,32):0.470448,(5,40):0.376053}; ok4=True
for (r,N),v in ax.items():
    g,_=block(N,r,(1,0,0)); ok4&=abs(g-v)<1e-5; out.append("axial r=%d N=%d gamma=%.6f (claimed %.6f)"%(r,N,g,v))
out.append("B4 %s"%("MET" if ok4 else "FAILED"))
open('blockr_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
