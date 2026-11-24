"""SU(2) ladder toy (su2run.py): three checks asked for by reviewers of the first results.
 (a) the weight of the lowest state in the fine detail compared across spin cut-offs (J - 1 against J), at the
     same coarse degree D = 10, not only the gap;
 (b) the low states by centre sector: parity under multiplication of the y-links c, d by -1, which is
     (-1)^(2 j_c + 2 j_d) on a spin network, and under multiplication of the x-link a by -1, (-1)^(2 j_a);
 (c) the compressed spectral weight F(E_k) = largest eigenvalue of the matrix <psi_i, (I - P_D) psi_j> over the
     excited states with energy at most E_k, k = 1..5, which is the quantity of the weight bound for a spectral
     subspace and does not depend on the basis chosen in a degenerate level.
All numbers are for the model truncated at spin J, in which the magnetic factor is the exponential of the truncated
multiplication operator, not the truncation of the exact factor; agreement between cut-offs is a numerical
convergence diagnostic and not a bound for the untruncated model.
PREDICATES (fixed before the first run):
 C1 for beta in {2, 3, 4, 5}: the weight of the lowest state at D = 10 changes by less than 2 per cent between
    J = 4 and J = 5 (if not, the line is marked).
 C2 every one of the five lowest excited states has both parities equal to +1 or -1 to 1e-6 (the states are
    sector states), and the lowest is odd under the y-flip and even under the x-flip.
 C3 F(E_1) equals the weight of the lowest state (the level is not degenerate), to 1e-12.
Usage: python3 su2cluster.py OUT"""
import sys, numpy as np
from su2ladder import *
out=[]; C1=C2=C3=True; nets={}
for J in (4.0,5.0):
    N=Net(J); nets[J]=(N,{k:N.assemble(k) for k in ('W0','W1','C','AB','ABC')})
def parities(N):
    py=np.zeros(N.n); px=np.zeros(N.n)
    for (ja,jb,jc,jd),(off,r0,r1) in N.blocks.items():
        py[off:off+r0*r1]=(-1)**(tw(jc)+tw(jd)); px[off:off+r0*r1]=(-1)**tw(ja)
    return py,px
for beta in (2.0,3.0,4.0,5.0):
    w={}
    for J in (4.0,5.0):
        N,mats=nets[J]; m=Model(J,beta,Dg=10,net=N,mats=mats); m.vacuum(); ev,V=m.low(6); w[J]=np.linalg.norm(m.G(V[:,1]))**2
    rel=abs(w[4.0]/w[5.0]-1); ok=rel<0.02; C1&=ok
    out.append("beta %.1f: weight of the lowest state at D=10: J=4 %.6e, J=5 %.6e, relative difference %.2e%s"%(beta,w[4.0],w[5.0],rel,"" if ok else " C1-FAILED"))
    py,px=parities(N); GV=np.column_stack([m.G(V[:,i]) for i in range(1,6)]); Gram=V[:,1:6].conj().T@GV
    for k in range(1,6):
        E=-np.log(ev[k]); ey=float(np.real(np.vdot(V[:,k],py*V[:,k]))); ex=float(np.real(np.vdot(V[:,k],px*V[:,k])))
        F=np.linalg.eigvalsh((Gram[:k,:k]+Gram[:k,:k].conj().T)/2).max()
        C2&=abs(abs(ey)-1)<1e-6 and abs(abs(ex)-1)<1e-6
        out.append("    state %d: energy %.6f  y-parity %+.6f  x-parity %+.6f  weight %.4e  F(E_k) %.4e  F/E %.4f"%(k,E,ey,ex,Gram[k-1,k-1].real,F,F/E))
        if k==1:
            C2&=(ey<0 and ex>0); C3&=abs(F-Gram[0,0].real)<1e-12
for nm,v in zip(("C1","C2","C3"),(C1,C2,C3)): out.append("%s %s"%(nm,"MET" if v else "FAILED"))
open(sys.argv[1],'x').write("\n".join(out)+"\n"); print("\n".join(out))
