"""SU(2) ladder toy: a check of the coarse space, asked for by a reviewer. The coarse space of su2run.py is generated
by applying spin-truncated multiplication matrices to the truncated vacuum, and products of truncated matrices are
not truncations of products (a four-dimensional example shows the difference can be real). Here the space generated
at cut-off J is compared with the space obtained the other way round: embed the same vacuum vector in the model with
the larger cut-off J' = J + D/2, where every monomial of degree <= D acts on it exactly (a multiplication by one
coarse loop raises a spin by at most 1/2), apply the monomials there, and project the results back to cut-off J.
Quantities, for the lowest excited state psi of the cut-off-J model:
  w_trunc = ||psi - P_trunc psi||^2 (as in su2run.py),  w_exact = ||psi - P_exact psi||^2,
  theta   = largest principal angle between the two spaces (radians),
  leak    = largest norm, over the exact monomial vectors, of the part lying above cut-off J (before projection).
PREDICATES (fixed before the first run):
 K1 for (J, D, beta) in {(3, 6, 2), (3, 6, 3), (4, 4, 3), (4, 4, 4)}: |w_trunc - w_exact| <= 0.02 w_exact.
 If K1 fails at some point, that point is reported and the corresponding entries of su2run are to be read as weights
 relative to the generated space only.
Reported without threshold: theta and leak.
Output su2coarsecheck_result.txt (not overwritten). Command: python3 su2coarsecheck.py"""
import numpy as np, scipy.linalg as sl
from su2ladder import *
def monomials(D):
    return [(p,q,r) for deg in range(D+1) for p in range(deg,-1,-1) for q in range(deg-p,-1,-1) for r in [deg-p-q]]
def embed(N,Np,v):
    w=np.zeros(Np.n,dtype=v.dtype)
    for key,(off,r0,r1) in N.blocks.items():
        offp,_,_=Np.blocks[key]; w[offp:offp+r0*r1]=v[off:off+r0*r1]
    return w
def restrict(N,Np,w):
    v=np.zeros(N.n,dtype=w.dtype)
    for key,(off,r0,r1) in N.blocks.items():
        offp,_,_=Np.blocks[key]; v[off:off+r0*r1]=w[offp:offp+r0*r1]
    return v
out=[]; K1=True; cache={}
def net(J):
    if J not in cache:
        N=Net(J); cache[J]=(N,{k:N.assemble(k) for k in ('W0','W1','C','AB','ABC')})
    return cache[J]
for J,D,beta in ((3.0,6,2.0),(3.0,6,3.0),(4.0,4,3.0),(4.0,4,4.0)):
    N,mats=net(J); Jp=J+D/2; Np,matsp=net(Jp)
    m=Model(J,beta,Dg=D,net=N,mats=mats); m.vacuum(); ev,V=m.low(4); psi=V[:,1]
    wt=np.linalg.norm(m.G(psi))**2; Qt=m.Q
    mp=Model(Jp,beta,Dg=0,net=Np,mats=matsp)          # only its multiplication matrices are used
    Om=embed(N,Np,m.Om); vecs={(0,0,0):Om}; ops=(mp.W['C'],mp.W['AB'],mp.W['ABC']); leak=0; cols=[]
    for (p,q,r) in monomials(D):
        if (p,q,r)!=(0,0,0):
            for k,(dp,dq,dr) in enumerate(((1,0,0),(0,1,0),(0,0,1))):
                prev=(p-dp,q-dq,r-dr)
                if min(prev)>=0: vecs[(p,q,r)]=ops[k]@vecs[prev]; break
        x=vecs[(p,q,r)]; low=restrict(N,Np,x); leak=max(leak,np.sqrt(max(np.vdot(x,x).real-np.vdot(low,low).real,0))/np.linalg.norm(x)); cols.append(low/np.linalg.norm(x))
    A=np.array(cols).T; U,s,_=np.linalg.svd(A,full_matrices=False); Qe=U[:,s>1e-9*s[0]]
    we=np.linalg.norm(psi-Qe@(Qe.conj().T@psi))**2
    sv=np.linalg.svd(Qe.conj().T@Qt,compute_uv=False); kmin=min(Qe.shape[1],Qt.shape[1]); theta=float(np.arccos(np.clip(sv[:kmin].min(),-1,1)))
    ok=abs(wt-we)<=0.02*we; K1&=ok
    out.append("J=%.0f D=%d beta=%.0f (J'=%.0f): w_trunc %.6e  w_exact %.6e  rel diff %.2e  dims %d/%d  theta %.3e  leak %.3e%s"%(J,D,beta,Jp,wt,we,abs(wt/we-1),Qt.shape[1],Qe.shape[1],theta,leak,"" if ok else " K1-FAILED"))
    print(out[-1],flush=True)
out.append("K1 %s"%("MET" if K1 else "FAILED"))
open('su2coarsecheck_result.txt','x').write("\n".join(out)+"\n"); print(out[-1])
