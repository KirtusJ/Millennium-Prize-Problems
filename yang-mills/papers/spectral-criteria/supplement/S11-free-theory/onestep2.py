"""Follow-up to onestep.py, whose predicate O2 FAILED (result kept): with coarse links that are sums of r fine links
along a line, the constant c_r of I - P_r <= c_r a H grows like r^2 at the lowest axial momentum of a large lattice
(c_r / r^2 = 0.36, 0.37, 0.39, 0.42, 0.43 for r = 2, 3, 4, 6, 8), so in units of the coarse mesh it grows like r.
Reading: a line sum does not average over the directions transverse to the line, and modes of low energy with a
transverse momentum that is a multiple of 2 pi / r alias into it.
Here the coarse variables are instead block averages of the plaquette field: for each plane, the flux through an
r x r face, averaged over the r parallel faces of the block. In momentum space this multiplies the fine plaquette
field at every alias by the scalar S(p_1) S(p_2) S(p_3) / r, S(x) = sum_{l<r} e^{i l x}, which vanishes at every
non-zero alias as k -> 0. These variables are gauge invariant; they are not products of links.
Stipulation written before the first run: with these variables c_r <= 2 r for r in {2,3,4,6,8}, at all coarse momenta
for N = 4r (and 8r for r <= 4) and at the lowest axial momentum for N = 1024 r. Against it: growth faster than r.
PREDICATE P1: the stipulation. Reported: c_r / r. Output onestep2_result.txt (not overwritten)."""
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
        s=np.prod([sum(np.exp(1j*l*x) for l in range(r)) for x in p])/r
        curl=np.array([[0,-d[2],d[1]],[d[2],0,-d[0]],[-d[1],d[0],0]])
        Fs.append(s*curl@Bp/np.sqrt(2*np.sinh(w))); ws+=[w]*2
    F=np.hstack(Fs); ws=np.array(ws)
    _,sv,Vh=np.linalg.svd(F); rank=int((sv>1e-10*max(sv.max(),1e-300)).sum()) if sv.max()>0 else 0
    ker=Vh[rank:].conj().T; T=ker.conj().T@(ker/ws[:,None])
    return np.linalg.eigvalsh((T+T.conj().T)/2).max()
def sup(N,r): return max(val(N,r,q) for q in itertools.product(range(N//r),repeat=3))
out=[]; P1=True
for r in (2,3,4,6,8):
    for N in ([4*r,8*r] if r<=4 else [4*r]):
        c=sup(N,r); P1&=c<=2*r; out.append("r=%d N=%d all momenta: c_r=%.6f c_r/r=%.6f"%(r,N,c,c/r))
    c=val(1024*r,r,(1,0,0)); P1&=c<=2*r; out.append("r=%d N=%d lowest axial momentum: c=%.6f c/r=%.6f"%(r,1024*r,c,c/r))
out.append("P1 %s"%("MET" if P1 else "FAILED"))
open('onestep2_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
