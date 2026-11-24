"""Position-space check of the block computation in maxwell.py for N=4 and N=6 (dense matrices).
PREDICATE (fixed before run): gamma and b from position space agree with the Fourier-block values to 1e-8."""
import numpy as np, itertools, sys
src=open('maxwell.py').read(); exec(src[:src.index("Ns=[int")].replace('import sys, numpy as np, itertools',''))
def pos(N,m):
    sites=list(itertools.product(range(N),repeat=3)); idx={s:i for i,s in enumerate(sites)}; n=len(sites)
    def cov(tau):
        S=np.zeros((3*n,3*n),complex)
        for q in itertools.product(range(N),repeat=3):
            p=[2*np.pi*x/N for x in q]
            if all(x==0 for x in q): continue
            w=omega(p); M=Mmat(p)*np.exp(-w*tau)/(2*np.sinh(w))
            ph=np.array([np.exp(1j*sum(p[i]*s[i] for i in range(3))) for s in sites])/np.sqrt(n)
            for r in range(3):
                for c in range(3):
                    S[r*n:(r+1)*n, c*n:(c+1)*n]+=M[r,c]*np.outer(ph,ph.conj())
        return S.real
    S0,S1,Sm=cov(0),cov(1),cov(m)
    rows=[]
    for r,(i,j) in enumerate(PL):
        for s in sites:
            if all(x%2==0 for x in s):
                v=np.zeros(3*n)
                for di,dj in itertools.product((0,1),repeat=2):
                    t=list(s); t[i]=(t[i]+di)%N; t[j]=(t[j]+dj)%N; v[r*n+idx[tuple(t)]]=1
                rows.append(v)
    K=np.array(rows)
    C0=K@S0@K.T; Cm=K@Sm@K.T
    b=1-np.sqrt(topcc(C0,Cm,C0))
    G=pinv_h(C0); KS0=K@S0; KS1=K@S1
    g=1-topcc(S0-KS0.T@G@KS0, S1-KS0.T@G@KS1, S0-KS1.T@G@KS1)
    return b,g
out=[]
for N in (4,6):
    m=N//2; rc,r2,_=level(N,m); b,g=pos(N,m)
    out.append("N=%d position b=%.9f gamma=%.9f | block b=%.9f gamma=%.9f | %s"%(N,b,g,1-rc,1-r2,"MET" if abs(b-(1-rc))<1e-8 and abs(g-(1-r2))<1e-8 else "FAILED"))
open('poscheck_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
