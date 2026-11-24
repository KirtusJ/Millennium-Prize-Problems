"""SU(2) itself on the two-site ladder of ladder.py (same model, same blocking), in a basis of spin networks cut off
at spin J. Edge spins (j_a, j_b, j_c, j_d) and one intertwiner label at each vertex; the kinetic part is diagonal,
prod_e I_{2j_e+1}(beta)/I_1(beta); multiplication by the plaquette traces and by the coarse loops Tr c, Tr ab,
Tr abc is assembled from Clebsch-Gordan coefficients (su2net.py; validated pointwise by su2validate.py).
The coarse projection in the vacuum representation is approximated from inside: P_D projects on the span of the
monomials of degree <= D in the three coarse loops applied to Omega, so  w_D = ||psi - P_D psi||^2  is an UPPER
bound for the weight of psi in the fine detail, decreasing in D, and gamma computed with I - P_D is a LOWER bound
for gamma_opt. (This holds up to the spin cut-off; D is kept well below what the cut-off allows.)
PREDICATES (fixed before the first run):
 R1 (control, known answer) with M = 1, beta = 1, J = 2: the largest eigenvalue on centred functions is
    I_2(1)/I_1(1) to 1e-10.
 R2 (cross-check with the icosahedral group, ladder_result.txt): the lattice gap at beta = 1 and 2 agrees with the
    2I value to relative 1e-4.
 R3 (spin cut-off) for each beta the gap at J and at J - 1 agree to relative 1e-3; where they do not, the line is
    marked and the values for that beta are not to be used.
 R4 w_D is non-increasing in D at each beta (to 1e-12).
Reported: gap; w_D / gap for D = 4, 6, 8, 10, 12; the lower bound for gamma_opt at the largest D.
Usage: python3 su2run.py OUT LADDER_RESULT J beta[,beta...] [gamma]"""
import sys, re, time, numpy as np
from su2ladder import *
out=[]
m=Model(2,1.0,magnetic=False,Dg=0); m.vacuum(); ev,V=m.low(3); lamf=spc.ive(2,1.0)/spc.ive(1,1.0)
out.append("R1 control: %.12f against %.12f : %s"%(ev[1],lamf,"MET" if abs(ev[1]-lamf)<1e-10 else "FAILED"))
ref={}
for line in open(sys.argv[2]):
    mm=re.match(r"2I beta ([\d.]+) .*lattice gap = ([\d.]+)",line)
    if mm: ref[float(mm.group(1))]=float(mm.group(2))
J=float(sys.argv[3]); betas=[float(x) for x in sys.argv[4].split(',')]; dog=len(sys.argv)>5
nets={}
for JJ in (J-1,J):
    N=Net(JJ); nets[JJ]=(N,{k:N.assemble(k) for k in ('W0','W1','C','AB','ABC')}); out.append("J = %.1f: %d basis states"%(JJ,N.n))
R2=R3=R4=True; n2=0
for beta in betas:
    gaps={}
    for JJ in (J-1,J):
        N,mats=nets[JJ]; m=Model(JJ,beta,Dg=0,net=N,mats=mats); m.vacuum(); ev,V=m.low(6); gaps[JJ]=-np.log(ev[1])
    rel=abs(gaps[J-1]/gaps[J]-1); ok3=rel<1e-3; R3&=ok3
    line="beta %.2f: gap %.8f (J-1: %.8f, rel %.1e%s)"%(beta,gaps[J],gaps[J-1],rel,"" if ok3 else " R3-FAILED")
    if beta in ref and beta<=2:
        r=abs(gaps[J]/ref[beta]-1); n2+=1; R2&=r<1e-4; line+=" ; icosahedral %.8f, rel %.1e"%(ref[beta],r)
    elif beta in ref: line+=" ; icosahedral %.8f (ratio %.3f)"%(ref[beta],ref[beta]/gaps[J])
    ws=[]
    for D in (4,6,8,10,12):
        m.coarse(D); ws.append(np.linalg.norm(m.G(V[:,1]))**2)
    R4&=all(ws[i+1]<=ws[i]+1e-12 for i in range(4))
    line+=" ; weight/gap for D=4..12: "+" ".join("%.4f"%(w/gaps[J]) for w in ws)+" (coarse dim %d)"%m.Q.shape[1]
    if dog: line+=" ; gamma_opt >= %.6f"%m.gamma(ev[1:],V[:,1:])
    out.append(line); print(line,flush=True)
out.append("R2 %s (%d compared)"%("MET" if R2 and n2 else "FAILED" if not R2 else "NOT TESTED",n2)); out.append("R3 %s"%("MET" if R3 else "FAILED")); out.append("R4 %s"%("MET" if R4 else "FAILED"))
open(sys.argv[1],'x').write("\n".join(out)+"\n"); print("\n".join(out[-3:]))
