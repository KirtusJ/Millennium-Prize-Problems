"""Free (non-compact U(1)) lattice gauge theory in 3+1 dimensions, infinite time, spatial torus of side N:
exact test of the refinement architecture (Theorem t:inh, Corollary c:acc, Proposition p:pred of the paper).
Sector: gauge-invariant functions of the spatial plaquettes of one slice (no winding modes). Gaussian, so
maximal correlations are top canonical correlations of linear functionals.
Slice covariance of plaquette fields at spatial momentum p, lag tau: M(p) exp(-w tau)/(2 sinh w), cosh w = 1 + phat^2/2,
M(p) = d d^dagger restricted to spatial plaquettes (12),(13),(23).  Coarse plaquette = sum of its 4 fine plaquettes.
Quantities for fine side N (mesh L/N), physical time t = L/2 (m = N/2 steps), coarse side N/2 (m/2 steps):
  d_f = 1 - exp(-m w_min(N)),  d_c = 1 - exp(-(m/2) w_min(N/2)),
  b   = 1 - max canonical correlation of coarse plaquettes of the fine lattice at lag m,
  gamma = 1 - max squared canonical correlation of (slice, next slice) given the coarse plaquettes of the slice,
  eps = d_c - b,  K = 1 + 2/(m gamma).
PREDICATES fixed before the first run:
  P1 (theorem, must hold) d_f >= b/K - 1e-9 for every N.
  P2 (model facts) 0 < gamma <= 1, b <= 1.
  Q1 (question) is gamma bounded below as N grows?  reported: gamma(N), min over momenta.
  Q2 (question) does the budget sum_i M_{i-1} eps_i stay below d_0 along N0 -> 2N0 -> ... ?  reported.
Args: list of N (even).  Output: maxwell_result_<tag>.txt (not overwritten)."""
import sys, numpy as np, itertools
PL=[(0,1),(0,2),(1,2)]
def Mmat(p):
    k=np.exp(1j*np.array(p))-1
    d=np.zeros((3,3),complex)   # plaquette (i,j): F = k_i A_j - k_j A_i
    for r,(i,j) in enumerate(PL): d[r,j]+=k[i]; d[r,i]-=k[j]
    return d@d.conj().T
def omega(p):
    ph2=sum(4*np.sin(x/2)**2 for x in p)
    return np.arccosh(1+ph2/2)
def pinv_h(A,tol=1e-10):
    w,V=np.linalg.eigh((A+A.conj().T)/2); s=np.where(w>tol*max(w.max(),1e-300),1/np.where(w>0,w,1),0)
    return (V*s)@V.conj().T
def topcc(Sxx,Sxy,Syy):
    """max squared canonical correlation"""
    w,V=np.linalg.eigh((Sxx+Sxx.conj().T)/2); keep=w>1e-10*max(w.max(),1e-300)
    if not keep.any(): return 0.0
    Wx=V[:,keep]/np.sqrt(w[keep])
    w2,V2=np.linalg.eigh((Syy+Syy.conj().T)/2); keep2=w2>1e-10*max(w2.max(),1e-300)
    if not keep2.any(): return 0.0
    Wy=V2[:,keep2]/np.sqrt(w2[keep2])
    C=Wx.conj().T@Sxy@Wy
    return float(np.linalg.svd(C,compute_uv=False)[0]**2)
def level(N,m):
    rho_coarse=0.0; rho_fib2=0.0; arg=None
    for q in itertools.product(range(N//2),repeat=3):
        S0=np.zeros((24,24),complex); S1=np.zeros((24,24),complex); Sm=np.zeros((24,24),complex); K=np.zeros((3,24),complex)
        for a,n in enumerate(itertools.product((0,1),repeat=3)):
            p=[2*np.pi*(q[i]+n[i]*N//2)/N for i in range(3)]
            if all(abs(np.sin(x/2))<1e-12 for x in p): continue
            w=omega(p); M=Mmat(p); c=1/(2*np.sinh(w))
            sl=slice(3*a,3*a+3)
            S0[sl,sl]=M*c; S1[sl,sl]=M*c*np.exp(-w); Sm[sl,sl]=M*c*np.exp(-w*m)
            for r,(i,j) in enumerate(PL): K[r,3*a+r]=(1+np.exp(1j*p[i]))*(1+np.exp(1j*p[j]))
        # coarse canonical correlation at lag m (same marginal at both times)
        C0=K@S0@K.conj().T; Cm=K@Sm@K.conj().T
        rc=np.sqrt(topcc(C0,Cm,C0)); rho_coarse=max(rho_coarse,rc)
        # fibre: condition on coarse plaquettes of slice X
        G=pinv_h(C0); KS0=K@S0; KS1=K@S1
        Sxx=S0-KS0.conj().T@G@KS0
        Sxy=S1-KS0.conj().T@G@KS1
        Syy=S0-KS1.conj().T@G@KS1
        r2=topcc(Sxx,Sxy,Syy)
        if r2>rho_fib2: rho_fib2=r2; arg=q
    return rho_coarse, rho_fib2, arg
def wmin(N): return omega([2*np.pi/N,0,0])
Ns=[int(x) for x in sys.argv[1:]]
out=[]; rows=[]
for N in Ns:
    m=N//2
    rc,r2,arg=level(N,m)
    d_f=1-np.exp(-m*wmin(N)); d_c=1-np.exp(-(m//2)*wmin(N//2)) if N>=4 and (m%2==0) else float('nan')
    b=1-rc; gam=1-r2; K=1+2/(m*gam)
    rows.append((N,m,d_f,d_c,b,gam,K,arg))
    out.append("N=%d m=%d d_f=%.6f d_c=%.6f b=%.6f gamma=%.6f (worst coarse momentum %s) K=%.6f b/K=%.6f eps=d_c-b=%.6f  P1 %s  P2 %s"%(N,m,d_f,d_c,b,gam,arg,K,b/K,d_c-b,"MET" if d_f>=b/K-1e-9 else "FAILED","MET" if (0<gam<=1+1e-12 and b<=1+1e-12) else "FAILED"))
# budget along the chain given
if len(rows)>1:
    d0=rows[0][3]; Mprev=1.0; s=0.0
    for (N,m,d_f,d_c,b,gam,K,arg) in rows:
        eps=d_c-b; s+=Mprev*max(eps,0); Mprev*=K
        out.append("chain up to N=%d: sum M_{i-1} eps_i^+ = %.6f, d_0 = %.6f, product M = %.4f, corollary bound on d_f: %.6f (true %.6f)"%(N,s,d0,Mprev,(d0-s)/Mprev,d_f))
tag="_".join(map(str,Ns)); open("maxwell_result_%s.txt"%tag,"x").write("\n".join(out)+"\n"); print("\n".join(out))
