"""Second, independent computation for the compact U(1) toy of u1toy.py (same model, same definitions), by flux
sectors. The transfer operator commutes with translations of the two coarse holonomies, so it is a direct sum over
the flux w = (w1, w2) of operators T_w = M K_w M on functions of the three plaquette angles; the vacuum Omega is in
the sector w = 0 and does not depend on the holonomies, so the coarse projection acts in each sector as the
rank-one projection on Omega, and
   1/gamma_opt = max_w || Q (I - That_w^2)^{-1} Q ||,   Q = I - |Omega><Omega|   (in the sector w = 0 this is the
   inverse on the complement of Omega).
The code shares with u1toy.py only the generator matrix B (copied here) and the Bessel routine. (A first trial of this
program took the real part after the Fourier multiplier; in a sector w != 0 the multiplier is not even, the operator
is complex Hermitian, and the control S1 failed. The trial output is kept as u1sector_trial_failed.txt.)
PREDICATES (fixed before the first run):
 S1 (control, known answer, first) with M = 1, beta = 1, n = 16: gamma_opt = 1 - max over (h != 0, |w_i| <= 2) of
    (kappa/kappa_0)^2, to 1e-8.
 S2 (cross-check) for every coupling at which the result file of u1toy.py (given as second argument) reports
    gamma_opt on its finer grid, the value here on the finer grid agrees with it to relative 1e-5.
 S3 (convergence) relative difference of gamma_opt between grids n1 and n2 below 10 I_{n1/2}(beta)/I_0(beta), or
    below 1e-6 if that is smaller than 1e-7.
 S4 sectors: the maximum over |w1|,|w2| <= 2 is attained in a sector with |w1|+|w2| <= 1 at every coupling
    (so that the cut at 2 is not what decides it).
Reported without threshold: gamma_opt, the sector that attains it, the energy of one unit of flux, its weight in
the fine detail, and their ratio, next to the expectation recorded in PREDICTION.md.
Usage: python3 u1sector.py OUT U1TOY_RESULT beta:n1:n2 ...   (OUT is not overwritten)"""
import sys, re, itertools, numpy as np, scipy.fft as sf, scipy.special as sp
from scipy.sparse.linalg import LinearOperator, eigsh, cg
B=np.array([[1,-1,-1,0,0,1,0,0],[0,1,0,0,1,-1,-1,0],[-1,0,1,-1,0,0,0,1],[1,0,0,0,1,0,0,0],[0,1,0,1,0,0,0,0]])
class Sec:
    def __init__(s,beta,n,magnetic=True):
        s.beta,s.n,s.N=beta,n,n**3; a=2*np.pi*np.arange(n)/n; a0,a1,a2=np.meshgrid(a,a,a,indexing='ij')
        V=np.cos(a0)+np.cos(a1)+np.cos(a2)+np.cos(a0+a1+a2)-4
        s.M=np.exp(0.5*beta*V) if magnetic else np.ones_like(V)
        f=sf.fftfreq(n,1/n).astype(int); s.H=np.meshgrid(f,f,f,indexing='ij'); s.kc={}
    def kap(s,w):
        if w not in s.kc:
            lk=0
            for j in range(8):
                ne=sum(B[i,j]*s.H[i] for i in range(3))+B[3,j]*w[0]+B[4,j]*w[1]
                lk=lk+np.log(sp.ive(np.abs(ne),s.beta)/sp.ive(0,s.beta))
            s.kc[w]=np.exp(lk)
        return s.kc[w]
    def T(s,w,v):
        return (sf.ifftn(s.kap(w)*sf.fftn(v.reshape((s.n,)*3)*s.M))*s.M).reshape(-1)   # complex: kappa(.,w) is not even in h when w != 0
    def vacuum(s):
        v=np.ones(s.N)/np.sqrt(s.N); lam=0
        for it in range(20000):
            x=s.T((0,0),v).real; new=np.linalg.norm(x); x/=new
            if abs(new-lam)<1e-15*new and np.linalg.norm(x-v)<1e-13: break
            lam=new; v=x
        s.Om=x.real/np.linalg.norm(x.real); s.L0=float((s.Om@s.T((0,0),s.Om)).real)
    def top(s,w):
        op=LinearOperator((s.N,s.N),matvec=lambda v:s.T(w,v)/s.L0,dtype=complex)
        vals,vecs=eigsh(op,k=2,which='LA',tol=1e-12,v0=(s.Om+1e-3*np.random.default_rng(5).normal(size=s.N)).astype(complex))
        o=np.argsort(-vals); return vals[o],vecs[:,o]
    def sup(s,w):
        Q=lambda v: v-s.Om*(s.Om@v)
        if w==(0,0):
            A=lambda v:(lambda u: u-s.T(w,s.T(w,u))/s.L0**2+s.Om*(s.Om@v))(Q(v))
        else:
            A=lambda v: v-s.T(w,s.T(w,v))/s.L0**2
        Aop=LinearOperator((s.N,s.N),matvec=A,dtype=complex)
        def S(v):
            x,info=cg(Aop,Q(v),rtol=1e-13,atol=0,maxiter=20000); assert info==0
            return Q(x)
        g=np.random.default_rng(7)
        return eigsh(LinearOperator((s.N,s.N),matvec=S,dtype=complex),k=1,which='LA',tol=1e-10,
                     v0=Q(g.normal(size=s.N)+1j*g.normal(size=s.N)))[0][0]
if __name__=='__main__':
    out=[]
    m=Sec(1.0,16,magnetic=False); m.vacuum()
    ws=[(a,b) for a in range(-2,3) for b in range(-2,3)]
    got=1/max(m.sup(w) for w in ws)
    mask=(m.H[0]!=0)|(m.H[1]!=0)|(m.H[2]!=0); exact=1-max((m.kap(w)[mask].max())**2 for w in ws)
    out.append("S1 control: gamma_opt %.10f exact %.10f : %s"%(got,exact,"MET" if abs(got-exact)<1e-8 else "FAILED"))
    ref={}
    for line in open(sys.argv[2]):
        mm=re.match(r"beta ([\d.]+) n (\d+): gamma_opt = ([\d.]+)",line)
        if mm: ref[float(mm.group(1))]=(int(mm.group(2)),float(mm.group(3)))     # the later (finer) grid overwrites
    S2=S3=S4=True; n2c=0
    for spec in sys.argv[3:]:
        beta,n1,n2=spec.split(':'); beta=float(beta); res=[]
        for n in (int(n1),int(n2)):
            m=Sec(beta,n); m.vacuum(); sups={w:m.sup(w) for w in ws if w[0]>=0 and (w[0]>0 or w[1]>=0)}   # w and -w are equivalent
            wbest=max(sups,key=sups.get); gam=1/sups[wbest]; res.append(gam)
            vals,vecs=m.top((1,0)); E=-np.log(vals[0]); wt=1-abs(m.Om@vecs[:,0])**2
            v0,_=m.top((0,0))
            out.append("beta %.2f n %d: gamma_opt = %.8f in sector %s ; sector sups: w=(0,0) %.6f  (1,0) %.6f  (0,1) %.6f  (1,1) %.6f  (2,0) %.6f"%(beta,n,gam,wbest,sups[(0,0)],sups[(1,0)],sups[(0,1)],sups[(1,1)],sups[(2,0)]))
            out.append("    one unit of flux: energy %.8f (beta*energy %.6f) fine-detail weight %.6e (beta*weight %.6f) weight/energy %.6f ; plaquette gap in the sector w=0: %.6f"%(E,beta*E,wt,beta*wt,wt/E,-np.log(v0[1])))
            S4&=(abs(wbest[0])+abs(wbest[1])<=1)
        tolr=10*sp.iv(int(n1)//2,beta)/sp.iv(0,beta)
        if tolr<1e-7: tolr=1e-6
        rel=abs(res[0]-res[1])/res[1]; S3&=rel<tolr
        line="beta %.2f: relative difference between n=%s and n=%s: %.2e (tolerance %.2e)%s"%(beta,n1,n2,rel,tolr,"" if rel<tolr else " S3-FAILED")
        if beta in ref:
            r=abs(res[1]-ref[beta][1])/ref[beta][1]; n2c+=1; S2&=r<1e-5
            line+=" ; five-dimensional program (n=%d) gave %.8f, relative difference %.2e%s"%(ref[beta][0],ref[beta][1],r,"" if r<1e-5 else " S2-FAILED")
        out.append(line)
    out.append("S2 %s (%d couplings compared)"%("MET" if S2 and n2c>0 else ("FAILED" if not S2 else "NOT TESTED"),n2c))
    out.append("S3 %s"%("MET" if S3 else "FAILED")); out.append("S4 %s"%("MET" if S4 else "FAILED"))
    out.append("expectation (PREDICTION.md): beta*energy -> 0.5, weight/energy -> 0.354, gamma_opt -> at most about 0.83")
    open(sys.argv[1],'x').write("\n".join(out)+"\n"); print("\n".join(out))
