"""Free theory, blocking by an integer factor r in one step (a coarse link is the sum of r consecutive fine links):
the one-particle constant c_r = sup over coarse momenta of || Q_r w^-1 Q_r ||, in lattice units of the FINE lattice.
By second quantisation I - P_r <= c_r a H on all functions. Question: does c_r grow like r (so that the constant is
of the order of the COARSE mesh r a, whatever the fine mesh), or faster?
Stipulation written before the first run: c_r <= 2 r. Reason: the fine detail just below the scale r has energy of
order 1/r in fine lattice units. What would count against it: growth faster than linear in r.
PREDICATES (fixed before the first run):
 O1 (known answer) r = 2: c at N = 8 and 16 equals 0.894242 and 1.086453 (weightfree_result.txt) to 1e-6.
 O2 c_r <= 2 r for r in {2,3,4,6,8}: over all coarse momenta at N = 4r (and N = 8r for r <= 4), and at the lowest
    axial coarse momentum for N = 1024 r.
Reported: c_r / r in each case. No random numbers. Output onestep_result.txt (not overwritten)."""
import numpy as np, itertools
def omega(p): return np.arccosh(1+sum(4*np.sin(x/2)**2 for x in p)/2)
def val(N,r,q):
    k=np.array([2*np.pi*q[i]/N for i in range(3)]); drk=np.exp(1j*r*k)-1
    PT=None if np.linalg.norm(drk)<1e-11 else np.eye(3)-np.outer(drk,drk.conj())/np.vdot(drk,drk).real
    Fs=[];ws=[]
    for eta in itertools.product(range(r),repeat=3):
        p=k+2*np.pi*np.array(eta)/r
        if all(abs(np.sin(x/2))<1e-12 for x in p): continue
        d=np.exp(1j*p)-1; w=omega(p)
        U,_,_=np.linalg.svd(np.eye(3)-np.outer(d,d.conj())/np.vdot(d,d).real); Bp=U[:,:2]
        D=np.diag([sum(np.exp(1j*l*x) for l in range(r)) for x in p])
        Fs.append(np.zeros((3,2),complex) if PT is None else PT@D@Bp/np.sqrt(2*np.sinh(w))); ws+=[w]*2
    F=np.hstack(Fs); ws=np.array(ws)
    _,s,Vh=np.linalg.svd(F); rank=int((s>1e-10*max(s.max(),1e-300)).sum()) if s.max()>0 else 0
    ker=Vh[rank:].conj().T; T=ker.conj().T@(ker/ws[:,None])
    return np.linalg.eigvalsh((T+T.conj().T)/2).max()
def sup(N,r): return max(val(N,r,q) for q in itertools.product(range(N//r),repeat=3))
out=[]
a,b=sup(8,2),sup(16,2); O1=abs(a-0.894242)<1e-6 and abs(b-1.086453)<1e-6
out.append("O1 r=2: N=8 %.6f N=16 %.6f : %s"%(a,b,"MET" if O1 else "FAILED"))
O2=True
for r in (2,3,4,6,8):
    for N in ([4*r,8*r] if r<=4 else [4*r]):
        c=sup(N,r); O2&=c<=2*r; out.append("r=%d N=%d all momenta: c_r=%.6f c_r/r=%.6f"%(r,N,c,c/r))
    c=val(1024*r,r,(1,0,0)); O2&=c<=2*r; out.append("r=%d N=%d lowest axial momentum: c=%.6f c/r=%.6f"%(r,1024*r,c,c/r))
out.append("O2 %s"%("MET" if O2 else "FAILED"))
open('onestep_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
