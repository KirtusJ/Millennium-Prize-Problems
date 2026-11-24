"""The weight of a slow state in the fine detail, divided by its energy: one constant for the free soft photon and
for the compact flux state. Conjectured closed form (quadratic approximation, written before this program ran):
    weight / energy  ->  sum over the non-zero momenta k in {0, pi}^(d-1) transverse to the slow direction of
                         1 / sinh(w_k),   cosh(w_k) = 1 + 2 (number of components equal to pi),
which is 1/sqrt 8 = 0.353553 in two space dimensions and 2/sqrt 8 + 1/sqrt 24 = 0.911237 in three.
PREDICATES (fixed before the first run):
 P1 free theory, three space dimensions, blocking factor 2 (function blk of ../S11-free-theory/matrixbridge.py):
    one-particle weight of the soft mode in the fine detail divided by sinh(w_k), at coarse momentum (1,0,0) and
    side 2^28, is within 1e-6 of 0.911237 (the earlier runs showed an error proportional to 1/N: 1.3e-3 at 2^12,
    8.6e-5 at 2^16, so about 2e-8 is expected at 2^28).
 P2 compact U(1) toy of u1sector.py (two space dimensions), sector of one unit of flux: with r(beta) =
    weight/energy, the extrapolation 2 r(128) - r(64) is within 1e-4 of 0.353553 (the values at beta = 8 and 16
    differ from it by 7.1e-3 and 3.4e-3, an error proportional to 1/beta; the next order, estimated from those two,
    is 2.6e-4 at beta = 16 and should be 64 times smaller here).
 P3 same runs: beta * energy extrapolated in the same way is within 1e-4 of 1/2.
Two corrections made after the first run, which is kept as softweight_firstrun.txt (its numbers are those of the
deposited run): (i) the decimal 0.911237 above is an addition slip; 2/sqrt 8 + 1/sqrt 24 = 0.911231, and the
program compares with the closed form, not with the decimal. Against the decimal as written P1 FAILS (6e-6);
against the closed form it is met (1.8e-8). (ii) In the free case the three momenta are not all transverse to the
soft direction: for the polarisation e_2 of a soft photon along e_1 they are the aliases shifted by pi in
direction 1, in direction 3, and in both (a short calculation, given in the paper); the sum is the same.
Output softweight_result.txt (not overwritten). Command: python3 softweight.py   (run in this folder)"""
import numpy as np, itertools, sys
src=open('../S11-free-theory/matrixbridge.py').read(); exec(src[src.index("def omega"):src.index("out=[];res={}")])
out=[]; c3=2/np.sqrt(8)+1/np.sqrt(24); c2=1/np.sqrt(8)
r=[]
for e in (20,24,28):
    a,b,c,gm,wl,wk=blk(2**e,(1,0,0)); r.append(wl/np.sinh(wk)); out.append("free, N=2^%d: weight/sinh(w_k) = %.9f"%(e,r[-1]))
P1=abs(r[-1]-c3)<1e-6; out.append("closed form %.9f ; difference at 2^28: %.2e : P1 %s"%(c3,r[-1]-c3,"MET" if P1 else "FAILED"))
sys.argv=['x']; import u1sector as u
vals={}
for beta,n in ((64.0,96),(128.0,128)):
    m=u.Sec(beta,n); m.vacuum(); v,vec=m.top((1,0)); E=-np.log(v[0]); wt=1-abs(m.Om@vec[:,0])**2; vals[beta]=(E,wt)
    out.append("compact, beta=%g n=%d: energy %.10f beta*energy %.8f weight %.8e weight/energy %.8f"%(beta,n,E,beta*E,wt,wt/E))
ex=2*vals[128.0][1]/vals[128.0][0]-vals[64.0][1]/vals[64.0][0]; P2=abs(ex-c2)<1e-4
out.append("extrapolated weight/energy %.8f ; closed form %.8f : P2 %s"%(ex,c2,"MET" if P2 else "FAILED"))
ex=2*128*vals[128.0][0]-64*vals[64.0][0]; P3=abs(ex-0.5)<1e-4
out.append("extrapolated beta*energy %.8f : P3 %s"%(ex,"MET" if P3 else "FAILED"))
open('softweight_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
