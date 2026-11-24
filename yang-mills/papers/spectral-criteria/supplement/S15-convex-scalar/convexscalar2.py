"""Follow-up to convexscalar.py, whose expectation X1 was not met: the on-site double wells did not push the constant
above the free value (0.78 and 0.28 of it). Reading: in those potentials the slow motion is a common flip of both
sites, which the block variable phi1 + phi2 sees. Here the well is put in the fine direction instead.
System A of convexscalar.py (two sites, m^2 = 0.25, k = 1, block variable phi1 + phi2, lambda_N = 1.5), with
  V = lam * ((phi1 - phi2)^2 - v^2)^2   (not convex; two wells that differ only in the fine variable).
The two lowest states are then even and odd in phi1 - phi2; the odd one is orthogonal to every function of the block
variable times the vacuum, so kappa_exact >= 1/(E1 - E0).
PREDICATES (fixed before the first run).
  W1 (control) at lam = 0 the value is 1/1.5 to relative 2e-3.
  W2 (expectation) for (lam, v) in {(0.25, 2), (0.5, 2.5), (1, 3)}: kappa_exact > 1/lambda_N, and kappa_exact agrees
     with 1/(E1 - E0) to relative 1e-2 (the odd state carries the constant).
Usage: python3 convexscalar2.py OUT"""
import sys, numpy as np, scipy.sparse as sps, scipy.sparse.linalg as spl
import convexscalar_lib as C
out=[]; W1=W2=True
S=C.system('A',227,8.0)
for lam,v in ((0.0,0.0),(0.25,2.0),(0.5,2.5),(1.0,3.0)):
    p=S['phis']; V=lam*((p[0]-p[1])**2-v*v)**2
    kap,E0=C.kappa(S,V); U=(S['quad']+V).ravel(); H=(-0.5*S['Lap']+sps.diags(U)).tocsc()
    ev=np.sort(spl.eigsh(H,k=3,sigma=U.min()-1.0,which='LM')[0]); gap=ev[1]-ev[0]
    line="lam %.2f v %.1f: kappa_exact %.6f  1/lambda_N %.6f  ratio %.3f  E1-E0 %.6e  kappa*(E1-E0) %.4f"%(lam,v,kap,1/S['lamN'],kap*S['lamN'],gap,kap*gap)
    if lam==0: W1=abs(kap*1.5-1)<2e-3
    else: W2&=(kap>1/S['lamN']) and abs(kap*gap-1)<1e-2
    out.append(line); print(line,flush=True)
out.append("W1 %s"%("MET" if W1 else "FAILED")); out.append("W2 %s"%("as expected" if W2 else "NOT as expected"))
open(sys.argv[1],'x').write("\n".join(out)+"\n"); print("\n".join(out[-2:]))
