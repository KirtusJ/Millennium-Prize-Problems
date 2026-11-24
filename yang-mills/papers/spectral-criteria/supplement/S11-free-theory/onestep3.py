"""Second follow-up to onestep.py. Same computation as onestep2.py with a smoother block average of the plaquette
field: the box average is applied twice in each direction (a triangular weight of width 2r - 1), so the multiplier at
each alias is (S(p_1) S(p_2) S(p_3))^2 / r^4 up to the common normalisation, S(x) = sum_{l<r} e^{i l x}. One variable
per coarse site and plane, as before; the supports of neighbouring variables overlap.
Result of onestep2.py that prompted this: c_r / r = 0.46, 0.50, 0.56, 0.65, 0.72 for r = 2, 3, 4, 6, 8 at the lowest
axial momentum, within the bound 2r and still increasing.
Stipulation written before the first run: with the triangular weight c_r / r is bounded: at the lowest axial momentum
of the lattice of side 1024 r, c_r / r <= 1 for r in {2,3,4,6,8}, and the values at r = 6 and r = 8 differ by less
than 3 per cent. Against it: continued growth of the same kind as for the box average (which rose 11 per cent from
r = 6 to r = 8).
PREDICATE P1: c_r <= 2r in all cases (as before). PREDICATE P2: the stipulation above.
Output onestep3_result.txt (not overwritten)."""
import numpy as np, itertools
def omega(p): return np.arccosh(1+sum(4*np.sin(x/2)**2 for x in p)/2)
def val(N,r,q):
    k=np.array([2*np.pi*q[i]/N for i in range(3)])
    Fs=[];ws=[]
    for eta in itertools.product(range(r),repeat=3):
        p=k+2*np.pi*np.array(eta)/r
        if all(abs(np.sin(x/2))<1e-12 for x in p): continue
        d=np.exp(1j*p)-1; w=omega(p)
        U,_,_=np.linalg.svd(np.eye(3)-np.outer(d,d.conj())/np.vdot(d,d).real); Bp=U[:,:2]
        s=np.prod([sum(np.exp(1j*l*x) for l in range(r))**2/r for x in p])/r
        curl=np.array([[0,-d[2],d[1]],[d[2],0,-d[0]],[-d[1],d[0],0]])
        Fs.append(s*curl@Bp/np.sqrt(2*np.sinh(w))); ws+=[w]*2
    F=np.hstack(Fs); ws=np.array(ws)
    _,sv,Vh=np.linalg.svd(F); rank=int((sv>1e-10*max(sv.max(),1e-300)).sum()) if sv.max()>0 else 0
    ker=Vh[rank:].conj().T; T=ker.conj().T@(ker/ws[:,None])
    return np.linalg.eigvalsh((T+T.conj().T)/2).max()
def sup(N,r): return max(val(N,r,q) for q in itertools.product(range(N//r),repeat=3))
out=[]; P1=True; AX={}
for r in (2,3,4,6,8):
    for N in ([4*r,8*r] if r<=4 else [4*r]):
        c=sup(N,r); P1&=c<=2*r; out.append("r=%d N=%d all momenta: c_r=%.6f c_r/r=%.6f"%(r,N,c,c/r))
    c=val(1024*r,r,(1,0,0)); AX[r]=c/r; P1&=c<=2*r; out.append("r=%d N=%d lowest axial momentum: c=%.6f c/r=%.6f"%(r,1024*r,c,c/r))
out.append("P1 %s"%("MET" if P1 else "FAILED"))
P2=all(v<=1 for v in AX.values()) and abs(AX[8]/AX[6]-1)<0.03; out.append("P2 %s (ratio of the values at r=8 and r=6: %.4f)"%("MET" if P2 else "FAILED",AX[8]/AX[6]))
open('onestep3_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
