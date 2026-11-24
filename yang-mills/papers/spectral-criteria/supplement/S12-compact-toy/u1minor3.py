"""Second follow-up to u1minor.py. In u1minor2.py N1 FAILED again (result kept): at beta = 4 the values m_w and m_{-w}
differ for fluxes with |w_i| >= 6. Diagnosis: on a grid of 16 points per angle the Fourier frequencies run from -8 to 7,
which is not symmetric, and in a sector of flux w the multiplier is centred near -w, so for |w| comparable to 8 the
cut-off of the plaquette frequencies is no longer harmless. The values of eps at beta = 4 and n = 1, 2, which are
sums of many small terms with alternating signs, were therefore not reliable; those at larger n and at beta = 2 were.
Same quantities and model. Changes: 40 points per angle; fluxes |w_i| <= 12, so the plaquette frequencies reach
well beyond the flux; N3 relative as in u1minor2.py.
PREDICATES (fixed before the first run), beta in {2, 4}, n in {1, 2, 4, 8, 16, 32}:
 N1 -1e-9 <= m_w(n) <= 1 + 1e-9, non-increasing in n to 1e-9, m_w = m_{-w} to 1e-9.
 N2 eps(n) <= b(n) + 1e-9.
 N3 outer shell (max |w_i| = 12) summed is below 1e-6 eps(n).
 N4 (agreement with the earlier run where it was reliable) eps at beta = 2, all n, and at beta = 4, n >= 8, agree
    with u1minor3_result.txt to relative 1e-5.
Output u1minor3_result.txt (not overwritten). Command: python3 u1minor3.py"""
import sys, numpy as np
sys.argv=['x']; import u1sector as u
out=[]; N1=N2=N3=True; W=12; ns=(1,2,4,8,16,32)
dl=2*np.pi*np.arange(64)/64; D1,D2=np.meshgrid(dl,dl,indexing='ij')
for beta in (2.0,4.0):
    m=u.Sec(beta,40); m.vacuum(); M={}
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
import re
old={}
for line in open('u1minor2_result.txt'):
    mm=re.match(r"beta (\d+) n\s+(\d+): eps = ([0-9.e+-]+)",line)
    if mm: old[(float(mm.group(1)),int(mm.group(2)))]=float(mm.group(3))
N4=True
for line in out:
    mm=re.match(r"beta (\d+) n\s+(\d+): eps = ([0-9.e+-]+)",line)
    if mm:
        key=(float(mm.group(1)),int(mm.group(2)))
        if key[0]==2 or key[1]>=8: N4&=abs(float(mm.group(3))/old[key]-1)<1e-5
for nm,v in zip(("N1","N2","N3","N4"),(N1,N2,N3,N4)): out.append("%s %s"%(nm,"MET" if v else "FAILED"))
open('u1minor3_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
