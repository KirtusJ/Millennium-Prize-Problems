"""Compact U(1) lattice gauge theory in 2+1 dimensions on a 2 x 2 spatial torus, blocked to a 1 x 1 torus:
the exact form of the mixing hypothesis (the remark on its exact and sufficient forms, part (a)) and the
low-energy weight of the fine detail, computed numerically in an interacting compact model. A toy: it is not
SU(2), not four-dimensional, and the coarse lattice has a single site. Nothing here bears on the open hypotheses.

Model. Eight links with angles th_e; weight exp(beta sum_p cos th_p) over space-time and spatial plaquettes.
Gauge-invariant functions of a slice are the functions on the 5-torus with coordinates
 (th_p0, th_p1, th_p2, Th_1, Th_2): three plaquette angles (the fourth is minus their sum) and the holonomies of
 the two lines through the origin. The coarse links are those two lines, so the coarse field is (Th_1, Th_2).
Transfer operator on L^2 of the 5-torus:  T = M K M,  M = exp((beta/2) sum_{p} cos th_p)  (multiplication),
 K = Fourier multiplier kappa(h) = prod_e I_{n_e(h)}(beta), n(h) = h^T B the integer current of the character h.
Vacuum Omega = top eigenvector, Lambda_0 its eigenvalue, That = T/Lambda_0. In the vacuum representation
 A f = That(f Omega)/Omega; here everything is done on psi = f Omega. Coarse projection: (P psi) =
 Omega * (int psi Omega dth_p)/(int Omega^2 dth_p) at fixed (Th_1,Th_2); G = I - P.
 gamma_opt = 1/||G (I - That^2)^{-1} G||  (inverse on the complement of Omega).
 Fine-detail weight of an eigenvector psi_k of That: ||G psi_k||^2; energy E_k = -log(lambda_k).

PREDICATES (fixed before the first run):
 U0 (control) the five generators B are a basis of the divergence-free integer currents: every row has zero
    divergence, rank 5, and the gcd of the 5x5 minors of B is 1.
 U1 (control, known answer, answered first) with M replaced by 1 (no spatial plaquettes), beta = 1, n = 8:
    Omega is constant, the eigenfunctions are the characters, G keeps those with (h0,h1,h2) != 0, so
    gamma_opt = 1 - max_{(h0,h1,h2) != 0} (kappa(h)/kappa(0))^2 exactly; the program's value agrees to 1e-8.
 U2 Omega > 0 at every grid point; every computed eigenvalue of That lies in [-1e-10, 1+1e-10].
 U3 (convergence) the relative difference of gamma_opt between the two grids given for a coupling is below
    10 * I_{n1/2}(beta)/I_0(beta), n1 the coarser grid (the size of the first Fourier coefficient of the
    kernel that the coarser grid drops), or below 1e-6 if that is smaller than 1e-7.
 No threshold is set on gamma_opt itself: the run reports it, with the lattice gap and the weights.
 Reported as well (added after a trial run at beta = 1, n = 8 and 10, before the runs deposited): F(E_k), the
 largest eigenvalue of the matrix <psi_i, G psi_j> over the excited states with energy at most E_k, which is the
 quantity F(u) of the remark on the low-energy weight at u = E_k, for the eight lowest states computed.
Free-theory value for comparison (same geometry, winding modes left out): 1 - (3 - sqrt 8)^2 = 0.970563.
Usage: python3 u1toy.py OUT beta:n1:n2 [beta:n1:n2 ...]   (result file OUT is not overwritten)
"""
import sys, itertools, math, numpy as np, scipy.fft as sf, scipy.special as sp
from scipy.sparse.linalg import LinearOperator, eigsh, cg
def e(x,y,mu): return 2*(2*(x%2)+(y%2))+mu
def plaq(x,y):
    v=np.zeros(8,int); v[e(x,y,0)]+=1; v[e(x+1,y,1)]+=1; v[e(x,y+1,0)]-=1; v[e(x,y,1)]-=1; return v
B=np.array([plaq(0,0),plaq(1,0),plaq(0,1),
            [1 if i in (e(0,0,0),e(1,0,0)) else 0 for i in range(8)],
            [1 if i in (e(0,0,1),e(0,1,1)) else 0 for i in range(8)]])
def control_U0():
    div=np.zeros((4,8),int)
    for x in range(2):
        for y in range(2):
            s=2*x+y
            for mu,(dx,dy) in enumerate(((1,0),(0,1))):
                div[s,e(x,y,mu)]+=1; div[2*((x+dx)%2)+((y+dy)%2),e(x,y,mu)]-=1
    ok=not (B@div.T).any() and np.linalg.matrix_rank(B)==5
    g=0
    for c in itertools.combinations(range(8),5): g=math.gcd(g,int(round(np.linalg.det(B[:,c]))))
    # the plaquette p3 must be minus the sum of the others
    ok&= not (plaq(1,1)+B[0]+B[1]+B[2]).any()
    return ok and g==1, g
class Model:
    def __init__(s,beta,n,magnetic=True):
        s.beta,s.n=beta,n; ang=2*np.pi*np.arange(n)/n
        a0,a1,a2=np.meshgrid(ang,ang,ang,indexing='ij')
        V=np.cos(a0)+np.cos(a1)+np.cos(a2)+np.cos(a0+a1+a2)-4
        s.M=(np.exp(0.5*beta*V) if magnetic else np.ones_like(V))[:,:,:,None,None]
        f=sf.fftfreq(n,1/n).astype(int); H=np.meshgrid(f,f,f,f,f,indexing='ij')
        lk=np.zeros((n,)*5)
        for j in range(8):
            ne=sum(B[i,j]*H[i] for i in range(5)); lk+=np.log(sp.ive(np.abs(ne),beta)/sp.ive(0,beta))
        s.kap=np.exp(lk); s.H=H; s.N=n**5
    def T(s,v):
        w=v.reshape((s.n,)*5)*s.M
        w=sf.ifftn(s.kap*sf.fftn(w,workers=-1),workers=-1).real*s.M
        return w.reshape(-1)
    def vacuum(s):
        v=np.ones(s.N)/np.sqrt(s.N); lam=0
        for it in range(5000):
            w=s.T(v); new=np.linalg.norm(w); w/=new
            if abs(new-lam)<1e-14*new and np.linalg.norm(w-v)<1e-12: break
            lam=new; v=w
        s.Om=w; s.L0=float(w@s.T(w)); s.den=(w.reshape((s.n,)*5)**2).sum((0,1,2))
        return s.L0
    def That(s,v): return s.T(v)/s.L0
    def P(s,v):
        O=s.Om.reshape((s.n,)*5); num=(v.reshape((s.n,)*5)*O).sum((0,1,2))
        return (O*(num/s.den)[None,None,None]).reshape(-1)
    def G(s,v): return v-s.P(v)
    def gamma(s):
        def A(v):
            v=v-s.Om*(s.Om@v); w=s.That(s.That(v)); return v-w+s.Om*(s.Om@v)   # identity on Omega: keeps CG well posed
        Aop=LinearOperator((s.N,s.N),matvec=A,dtype=float)
        def S(v):
            g=s.G(v); x,info=cg(Aop,g,rtol=1e-12,atol=0,maxiter=2000)
            assert info==0
            return s.G(x)
        mu=eigsh(LinearOperator((s.N,s.N),matvec=S,dtype=float),k=1,which='LA',tol=1e-9,
                 v0=s.G(np.random.default_rng(1).normal(size=s.N)))[0][0]
        return 1/mu
    def spectrum(s,k=8):
        vals,vecs=eigsh(LinearOperator((s.N,s.N),matvec=s.That,dtype=float),k=k,which='LA',tol=1e-11,v0=s.Om+1e-3*np.random.default_rng(2).normal(size=s.N))
        o=np.argsort(-vals); return vals[o],vecs[:,o]
if __name__=='__main__':
    out=[]; ok0,g=control_U0(); out.append("U0 gcd of minors %d : %s"%(g,"MET" if ok0 else "FAILED"))
    m=Model(1.0,8,magnetic=False); m.vacuum(); gam=m.gamma()
    mask=(m.H[0]!=0)|(m.H[1]!=0)|(m.H[2]!=0); exact=1-(m.kap[mask].max())**2
    out.append("U1 control: gamma_opt %.10f exact %.10f : %s"%(gam,exact,"MET" if abs(gam-exact)<1e-8 else "FAILED"))
    out.append("free-theory value for comparison %.6f"%(1-(3-np.sqrt(8))**2))
    U2=U3=True
    for spec in sys.argv[2:]:
        beta,n1,n2=spec.split(':'); beta=float(beta); res=[]
        for n in (int(n1),int(n2)):
            m=Model(beta,n); L0=m.vacuum(); U2&=bool((m.Om>0).all() or (m.Om<0).all())
            vals,vecs=m.spectrum(); U2&=bool(vals.min()>-1e-10 and vals.max()<1+1e-10)
            gam=m.gamma(); res.append(gam)
            out.append("beta %.2f n %d: Lambda0-normalised eigenvalues %s"%(beta,n," ".join("%.8f"%x for x in vals)))
            GV=np.stack([m.G(vecs[:,k]) for k in range(1,len(vals))],1); Gram=vecs[:,1:].T@GV
            for k in range(1,len(vals)):
                E=-np.log(vals[k]); w=Gram[k-1,k-1]; F=np.linalg.eigvalsh((Gram[:k,:k]+Gram[:k,:k].T)/2).max()
                out.append("   state %d energy %.6f fine-detail weight %.6e ; F(energy) = %.6e, F/energy = %.6f"%(k,E,w,F,F/E))
            out.append("beta %.2f n %d: gamma_opt = %.8f   lattice gap = %.6f"%(beta,n,gam,-np.log(vals[1])))
        tolr=10*sp.iv(int(n1)//2,beta)/sp.iv(0,beta)
        if tolr<1e-7: tolr=1e-6
        rel=abs(res[0]-res[1])/res[1]; u3=rel<tolr; U3&=u3
        out.append("beta %.2f: relative difference of gamma_opt between n=%s and n=%s: %.2e (tolerance %.2e) %s"%(beta,n1,n2,rel,tolr,"" if u3 else "U3-FAILED"))
    out.append("U2 %s"%("MET" if U2 else "FAILED")); out.append("U3 %s"%("MET" if U3 else "FAILED"))
    open(sys.argv[1],'x').write("\n".join(out)+"\n"); print("\n".join(out))
