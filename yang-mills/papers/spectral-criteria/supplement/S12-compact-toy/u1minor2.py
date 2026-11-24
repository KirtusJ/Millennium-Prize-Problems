"""Follow-up to u1minor.py, in which N1 and N3 FAILED (result kept in u1minor2_result.txt). Diagnosis: N1 compared
m_0(n) = 1 and the monotonicity with an absolute tolerance of 1e-12, below the rounding of the iteration (the values
printed for several fluxes are symmetric and decreasing to ten figures); N3 used an absolute threshold of 1e-8 for the
outermost shell of fluxes, which at beta = 4, n = 1 is of the same size as eps itself (1.0e-8 against 1.4e-8), so that
value of eps was not converged in the flux cut-off. Same quantities and model as u1minor.py. Changes: fluxes
|w_i| <= 20; N1 with tolerance 1e-9; N3 relative: the outermost shell is below 1e-6 times eps(n).
PREDICATES (fixed before the first run), beta in {2, 4}, n in {1, 2, 4, 8, 16, 32}:
 N1 -1e-9 <= m_w(n) <= 1 + 1e-9, non-increasing in n to 1e-9, m_w = m_{-w} to 1e-9.
 N2 eps(n) <= b(n) + 1e-9.
 N3 outer shell (max |w_i| = 20) of m_w(n) summed is below 1e-6 eps(n).
Output u1minor2_result.txt (not overwritten). Command: python3 u1minor2.py"""
import sys, numpy as np
sys.argv=['x']; import u1sector as u
out=[]; N1=N2=N3=True; W=20; ns=(1,2,4,8,16,32)
dl=2*np.pi*np.arange(64)/64; D1,D2=np.meshgrid(dl,dl,indexing='ij')
for beta in (2.0,4.0):
    m=u.Sec(beta,16); m.vacuum(); M={}
    for w1 in range(-W,W+1):
        for w2 in range(-W,W+1):
            v=m.Om.astype(complex); vals=[]; k=0
            for n in range(1,33):
                v=m.T((w1,w2),v)/m.L0
                if n in ns: vals.append((m.Om@v).real)
            M[(w1,w2)]=vals
            N1&=all(-1e-9<=x<=1+1e-9 for x in vals) and all(vals[i+1]<=vals[i]+1e-9 for i in range(len(vals)-1))
    N1&=all(abs(M[w][i]-M[(-w[0],-w[1])][i])<1e-9 for w in M for i in range(len(ns)))
    for i,n in enumerate(ns):
        R=sum(M[w][i]*np.cos(w[0]*D1+w[1]*D2) for w in M); eps=R.min()
        b=1-max(M[w][i] for w in M if w!=(0,0)); shell=sum(M[w][i] for w in M if max(abs(w[0]),abs(w[1]))==W)
        N2&=eps<=b+1e-9; N3&=shell<1e-6*eps
        out.append("beta %.0f n %2d: eps = %.6e  b = %.6e  eps/b = %.4f  (outer shell %.1e)"%(beta,n,eps,b,eps/b if b>0 else float('nan'),shell))
for nm,v in zip(("N1","N2","N3"),(N1,N2,N3)): out.append("%s %s"%(nm,"MET" if v else "FAILED"))
open('u1minor2_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
