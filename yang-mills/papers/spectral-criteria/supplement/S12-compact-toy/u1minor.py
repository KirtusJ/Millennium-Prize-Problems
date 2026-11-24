"""Compact U(1) toy: the minorisation of the one-step criterion (the proposition on a gap from two statements) for
the two coarse holonomies. The vacuum does not depend on them, so their law at one time is uniform on the 2-torus,
and the density of their joint law at lags 0 and n against the product of the marginals is
   R_n(delta) = sum over fluxes w of m_w(n) cos(w . delta),   m_w(n) = <Omega, That_w^n Omega>,
a function of the difference delta of the holonomies. The true decorrelation of the coarse variables is
b(n) = 1 - max_{w != 0} m_w(n); the minorisation constant is eps(n) = min_delta R_n(delta).
PREDICATES (fixed before the first run), beta in {2, 4}, n in {1, 2, 4, 8, 16, 32}, fluxes |w_i| <= 12:
 N1 0 <= m_w(n) <= 1, non-increasing in n for each w, and m_w = m_{-w} to 1e-10.
 N2 eps(n) <= b(n) + 1e-9 (the minorisation is a sufficient condition, so it cannot exceed the truth).
 N3 the neglected fluxes do not matter: sum over the outermost shell (max |w_i| = 12) of m_w(n) is below 1e-8.
Reported: eps(n), b(n) and their ratio. Grid 16 points per angle (beta <= 4; see u1sector_result.txt for the
convergence at these couplings). Output u1minor_result.txt (not overwritten). Command: python3 u1minor.py"""
import sys, numpy as np
sys.argv=['x']; import u1sector as u
out=[]; N1=N2=N3=True; W=12; ns=(1,2,4,8,16,32)
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
            N1&=all(-1e-12<=x<=1+1e-12 for x in vals) and all(vals[i+1]<=vals[i]+1e-12 for i in range(len(vals)-1))
    N1&=all(abs(M[w][i]-M[(-w[0],-w[1])][i])<1e-10 for w in M for i in range(len(ns)))
    for i,n in enumerate(ns):
        R=sum(M[w][i]*np.cos(w[0]*D1+w[1]*D2) for w in M); eps=R.min()
        b=1-max(M[w][i] for w in M if w!=(0,0)); shell=sum(M[w][i] for w in M if max(abs(w[0]),abs(w[1]))==W)
        N2&=eps<=b+1e-9; N3&=shell<1e-8
        out.append("beta %.0f n %2d: eps = %.6e  b = %.6e  eps/b = %.4f  (outer shell %.1e)"%(beta,n,eps,b,eps/b if b>0 else float('nan'),shell))
for nm,v in zip(("N1","N2","N3"),(N1,N2,N3)): out.append("%s %s"%(nm,"MET" if v else "FAILED"))
open('u1minor_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
