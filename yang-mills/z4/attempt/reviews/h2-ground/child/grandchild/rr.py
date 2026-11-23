"""T97: Rayleigh-Ritz estimate of e_0 for h_2 = -1/2 Lap + 2|Y1 x Y2|^2 on SO(3)-invariant L^2(R^6).

PREDICATE (fixed before first run): AGREE iff |E_best - 3.3505330| <= TOL, where
  E_best = lowest variational eigenvalue at the largest basis (min over omega scan), and
  TOL = max(2*(E_{N-1}-E_N), spread of E_N over the omega scan(top 3 omegas), 1e-6) --
  i.e. tolerance comes from the observed convergence step and omega sensitivity, not chosen by hand.
  Since Rayleigh-Ritz is an upper bound, E_best >= e_0 up to roundoff/ill-conditioning (cutoff reported).
Method: invariants basis a^i b^j c^k exp(-w(a+b)/2), k even (even under Y2->-Y2; the ground state
  is expected in this sector, which is a restriction => still an upper bound for the full l=0 problem
  only if ground state lies there; checked at small N with all k). Matrices are exact (Gamma functions),
  in reduced variables (r1,r2,c=cos theta), measure r1^2 r2^2 dr1 dr2 dc.
Results: results.txt opened with mode 'x' (never overwritten; use RESULTS env to name a new file).
Run: python3 rr.py   (deterministic, no randomness; numpy only)
"""
import numpy as np, math, os, sys
from math import gamma
def I(m,w): return gamma((m+1)/2)/(2*w**((m+1)/2))   # int_0^inf r^m exp(-w r^2) dr
def cint(n):  # int_-1^1 c^n dc
    return 0.0 if n%2 else 2.0/(n+1)
def basis(N,kstep):
    return [(i,j,k) for k in range(0,N+1,kstep) for i in range(N+1) for j in range(N+1) if i+j+k<=N]
def build(N,w,kstep=2,mode='h2',W=1.0,cut=1e-12):
    B=basis(N,kstep); n=len(B)
    p=np.array([2*i+k for i,j,k in B]); q=np.array([2*j+k for i,j,k in B]); kk=np.array([k for i,j,k in B])
    P=p[:,None]+p[None,:]; Q=q[:,None]+q[None,:]; K=kk[:,None]+kk[None,:]
    vI=np.vectorize(lambda m: I(m,w)); 
    S1=vI(P+2); S2=vI(Q+2)
    # overlap-type radial: int r^{m+2} e^{-w r^2}; c: int c^K
    C0=np.vectorize(cint)(K)
    pp=p[:,None]*p[None,:]; qq=q[:,None]*q[None,:]
    # do A elementwise with explicit sums (p p' r^{P} - w (p+p') r^{P+2} + w^2 r^{P+4}) * g^2 (the r^2 included)
    A1=pp*vI(P)-w*(p[:,None]+p[None,:])*vI(P+2)+w*w*vI(P+4)
    A2=qq*vI(Q)-w*(q[:,None]+q[None,:])*vI(Q+2)+w*w*vI(Q+4)
    # angular: int (1-c^2) d_c(c^k) d_c(c^k') = k k' (cint(K-2)-cint(K))
    Cc=(kk[:,None]*kk[None,:])*(np.vectorize(cint)(np.maximum(K-2,0))-C0)
    Cc=np.where(K>=2,Cc,0.0)
    B1=vI(P); B2=vI(Q)
    Kin=0.5*(A1*S2*C0+S1*A2*C0+(B1*S2+S1*B2)*Cc)
    Ov=S1*S2*C0
    if mode=='h2':
        Cs=np.vectorize(lambda n: cint(n)-cint(n+2))(K)   # int (1-c^2) c^K
        V=2.0*vI(P+4)*vI(Q+4)*Cs
    else: # harmonic test: 1/2 W^2 (r1^2+r2^2)
        V=0.5*W*W*(vI(P+4)*S2*C0+S1*vI(Q+4)*C0)
    H=Kin+V
    # canonical orthogonalisation
    d=np.sqrt(np.diag(Ov)); Ovn=Ov/np.outer(d,d); Hn=H/np.outer(d,d)
    ev,U=np.linalg.eigh(Ovn); keep=ev>cut*ev.max()
    X=U[:,keep]/np.sqrt(ev[keep])
    E=np.linalg.eigvalsh(X.T@Hn@X)
    return E[0],n,int(keep.sum()),E[:3]
if __name__=='__main__':
    out=open(os.environ.get('RESULTS','results.txt'),'x')
    def log(s): print(s); out.write(s+'\n'); out.flush()
    e,n,m,_=build(4,1.0,2,'harm',1.0); log(f'TEST harmonic W=1 (exact 3): {e:.10f} n={n} kept={m}')
    e,n,m,_=build(4,0.7,2,'harm',1.3); log(f'TEST harmonic W=1.3 w=.7 (exact 3.9, not exact basis): {e:.10f}')
    for kst in (1,2):
        e,n,m,_=build(6,1.0,kst); log(f'k-step {kst} N=6 w=1: {e:.8f} n={n}')
    log('N  dim kept  | E(w) for w in scan ; best')
    ws=[0.6,0.8,1.0,1.25,1.5,2.0,2.5]
    hist={}
    for N in range(2,23,2):
        r=[build(N,w,2) for w in ws]
        es=[x[0] for x in r]; j=int(np.argmin(es)); hist[N]=(es,j)
        log(f'N={N:2d} dim={r[0][1]:4d} kept={r[j][2]:4d} best={es[j]:.8f} w*={ws[j]} scan='+' '.join(f'{e:.6f}' for e in es))
    Ns=sorted(hist); Ebest={N:min(hist[N][0]) for N in Ns}
    EN=Ebest[Ns[-1]]; step=Ebest[Ns[-2]]-EN
    top3=sorted(hist[Ns[-1]][0])[:3]; spread=top3[-1]-top3[0]
    TOL=max(2*step,spread,1e-6)
    log(f'E_best={EN:.8f} last step={step:.3e} omega spread(top3)={spread:.3e} TOL={TOL:.3e}')
    log(f'|E-3.3505330|={abs(EN-3.3505330):.3e}  AGREE={abs(EN-3.3505330)<=TOL}')
