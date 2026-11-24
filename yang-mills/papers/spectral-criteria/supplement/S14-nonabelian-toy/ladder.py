"""A non-abelian toy for the exact form of the mixing hypothesis and for the weight of slow states in the fine
detail: lattice gauge theory in 2+1 dimensions on a spatial torus of 2 x 1 sites, with gauge group a finite
subgroup of SU(2) (binary tetrahedral 2T, 24 elements; binary octahedral 2O, 48; binary icosahedral 2I, 120) and
the Wilson weight exp(beta sum_p (1/2) Tr U_p). A finite subgroup stands in for SU(2) only while beta is small
enough that the group does not resolve the lattice of group elements; agreement between two subgroups is the test.
It is a toy: one dimension less, four links, a finite group. Nothing here bears on the open hypotheses.

Links: a (site 0 -> 1), b (site 1 -> 0) along x; c, d the closed y-links at sites 0, 1. Spatial plaquettes
a d a^-1 c^-1 and b c b^-1 d^-1. Gauge-invariant functions of a slice are the functions of (b, c, d) at a = 1
invariant under simultaneous conjugation; they are handled as functions on the orbits. Transfer operator
T = M K M, M = exp((beta/2)(sum of the two plaquette traces)), K = convolution on each of the four links with
the kernel exp(beta (1/2) Tr u) (normalised); on invariant functions the link a acts by
(b, c, d) -> (u b, c, u d u^-1). Blocking by two in the x direction: the coarse links are X = a b and Y = c, so
the coarse-measurable functions are the conjugation-invariant functions of (b, c), and the fine detail is what
depends on d. Vacuum Omega, That = T / Lambda_0, P = coarse projection in the vacuum representation, G = I - P.
Quantities: lattice gap E_1; weight of the first excited state(s) in the fine detail; gamma_opt =
1/||G (I - That^2)^-1 G||; and, where the matrix is diagonalised in full, kappa = ||G H^-1 G||, H = -log That.

PREDICATES (fixed before the first run):
 L0 (control) each group is closed under multiplication and inversion and has the stated order; the kernel is a
    class function; the orbit-space matrix of K is symmetric in the weighted inner product to 1e-12.
 L1 (control, known answer, first) with M = 1: the vacuum is constant; the largest eigenvalue of That on centred
    functions is lambda_f = sum_u k(u) (1/2)Tr(u) (the function Tr c); and gamma_opt = 1 - lambda_f^2 (the function
    Tr d is fine detail and has that eigenvalue). Both to 1e-10, for 2T at beta = 1.
 L2 Omega has one sign; eigenvalues of That in [0, 1 + 1e-10].
 L3 (the test of the stand-in) at each beta given for two groups, gamma_opt and the gap agree between them to the
    relative tolerance stated on the command line for that beta (no tolerance is claimed in advance for beta
    beyond the first disagreement; the run reports where the groups part).
Stipulation under test (Path A of the working notes, written before the run): the weight of the lowest excited
state in the fine detail divided by its energy stays bounded as beta grows, as in the abelian toy. What would
count against it: a ratio that grows with beta while the two groups still agree.
Usage: python3 ladder.py OUT group:beta[,beta...] [group:beta,...]   (OUT is not overwritten)
"""
import sys, itertools, numpy as np, scipy.sparse as sps
from scipy.sparse.linalg import LinearOperator, eigsh, cg
def qmul(p,q):
    a1,b1,c1,d1=p; a2,b2,c2,d2=q
    return np.array([a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2, a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2])
def group(name):
    el=[]
    for i in range(4):
        for s in (1,-1):
            v=np.zeros(4); v[i]=s; el.append(v)
    for s in itertools.product((1,-1),repeat=4): el.append(np.array(s)/2)
    if name=='2O':
        for i,j in itertools.combinations(range(4),2):
            for s in itertools.product((1,-1),repeat=2):
                v=np.zeros(4); v[i]=s[0]; v[j]=s[1]; el.append(v/np.sqrt(2))
    if name=='2I':
        phi=(1+np.sqrt(5))/2; base=[0,1,1/phi,phi]
        for perm in itertools.permutations(range(4)):
            sign=1
            for i in range(4):
                for j in range(i+1,4):
                    if perm[i]>perm[j]: sign=-sign
            if sign!=1: continue
            for s in itertools.product((1,-1),repeat=3):
                v=np.zeros(4); k=0
                for pos in range(4):
                    x=base[perm[pos]]
                    if x!=0: v[pos]=s[k]*x; k+=1
                el.append(v/2)
    E=np.array(el); n=len(E)
    key=lambda v: tuple(np.round(v*1e6).astype(np.int64)+0)
    idx={key(v):i for i,v in enumerate(E)}
    assert len(idx)==n
    mt=np.zeros((n,n),int)
    for i in range(n):
        for j in range(n): mt[i,j]=idx[key(qmul(E[i],E[j]))]          # KeyError if not closed
    inv=np.array([idx[key(E[i]*np.array([1,-1,-1,-1]))] for i in range(n)])
    return E,mt,inv
class Ladder:
    def __init__(s,name,beta,magnetic=True):
        E,mt,inv=group(name); n=len(E); s.n=n; re=E[:,0]; s.re=re
        cj=np.array([[mt[mt[h,g],inv[h]] for g in range(n)] for h in range(n)])            # cj[h][g] = h g h^-1
        B,C,D=np.meshgrid(np.arange(n),np.arange(n),np.arange(n),indexing='ij'); B=B.ravel();C=C.ravel();D=D.ravel()
        lab=np.full(n**3,np.iinfo(np.int64).max,dtype=np.int64)
        for h in range(n): lab=np.minimum(lab,(cj[h][B]*n+cj[h][C])*n+cj[h][D])
        reps,orb,cnt=np.unique(lab,return_inverse=True,return_counts=True)
        s.m=len(reps); s.cnt=cnt.astype(float); s.orb=orb.reshape(n,n,n)
        rb,rc,rd=reps//(n*n),(reps//n)%n,reps%n; s.rb,s.rc,s.rd=rb,rc,rd
        k=np.exp(beta*(re-1)); k/=k.sum(); s.k=k
        assert all(abs(k[cj[h]]-k).max()<1e-14 for h in range(n))
        rows=np.repeat(np.arange(s.m),n); kk=np.tile(k,s.m)
        def fac(cols): return sps.csr_matrix((kk,(rows,cols.ravel())),shape=(s.m,s.m))
        Kb=fac(s.orb[mt[rb][:, :], rc[:,None], rd[:,None]])                         # (b v, c, d)
        Kc=fac(s.orb[rb[:,None], mt[rc][:, :], rd[:,None]])
        Kd=fac(s.orb[rb[:,None], rc[:,None], mt[rd][:, :]])
        Ka=fac(s.orb[mt[:,rb].T, rc[:,None], cj[:,rd].T])                           # (u b, c, u d u^-1)
        s.Ks=[Ka,Kb,Kc,Kd]
        p0=re[mt[rd,inv[rc]]]; p1=re[mt[mt[mt[rb,rc],inv[rb]],inv[rd]]]
        s.M=np.exp(0.5*beta*(p0+p1-2)) if magnetic else np.ones(s.m)
        s.sq=np.sqrt(s.cnt)
        # coarse classes: orbits of pairs (b, c)
        Bp,Cp=np.meshgrid(np.arange(n),np.arange(n),indexing='ij'); lp=np.full(n*n,np.iinfo(np.int64).max,dtype=np.int64)
        for h in range(n): lp=np.minimum(lp,cj[h][Bp.ravel()]*n+cj[h][Cp.ravel()])
        _,po=np.unique(lp,return_inverse=True); s.cls=po.reshape(n,n)[rb,rc]; s.ncls=po.max()+1
    def K(s,f):
        for A in s.Ks: f=A@f
        return f
    def S(s,v):                                # symmetric form on l2: v = sqrt(cnt) * psi
        return s.sq*(s.M*s.K(s.M*(v/s.sq)))
    def vacuum(s):
        v=s.sq/np.linalg.norm(s.sq); lam=0
        for it in range(200000):
            w=s.S(v); new=np.linalg.norm(w); w/=new
            if abs(new-lam)<1e-15*new and np.linalg.norm(w-v)<1e-13: break
            lam=new; v=w
        s.Om=w; s.L0=float(w@s.S(w)); s.den=np.bincount(s.cls,weights=w*w,minlength=s.ncls)
    def That(s,v): return s.S(v)/s.L0
    def P(s,v): return s.Om*(np.bincount(s.cls,weights=v*s.Om,minlength=s.ncls)/s.den)[s.cls]
    def G(s,v): return v-s.P(v)
    def symcheck(s):
        g=np.random.default_rng(0); x=g.normal(size=s.m); y=g.normal(size=s.m)
        return abs(x@s.S(y)-y@s.S(x))/abs(x@s.S(y))
    def dense(s):
        I=np.eye(s.m); return np.column_stack([s.That(I[:,i]) for i in range(s.m)])
    def gamma(s):
        def A(v):
            v0=s.Om*(s.Om@v); u=v-v0; return u-s.That(s.That(u))+v0
        Aop=LinearOperator((s.m,s.m),matvec=A,dtype=float)
        def Sop(v):
            x,info=cg(Aop,s.G(v),rtol=1e-13,atol=0,maxiter=50000); assert info==0
            return s.G(x)
        mu=eigsh(LinearOperator((s.m,s.m),matvec=Sop,dtype=float),k=1,which='LA',tol=1e-10,v0=s.G(np.random.default_rng(1).normal(size=s.m)))[0][0]
        return 1/mu
if __name__=='__main__':
    out=[]
    for nm,order in (('2T',24),('2O',48),('2I',120)):
        E,mt,inv=group(nm); ok=len(E)==order and all(sorted(mt[i])==list(range(order)) for i in range(order)) and all(mt[i,inv[i]]==mt[0,inv[0]] for i in range(order))
        out.append("L0 group %s order %d closed with inverses: %s"%(nm,len(E),"MET" if ok else "FAILED"))
    m=Ladder('2T',1.0,magnetic=False); m.vacuum(); lamf=float(m.k@m.re)
    vals=eigsh(LinearOperator((m.m,m.m),matvec=m.That,dtype=float),k=3,which='LA',tol=1e-12,v0=m.Om+0.01*np.random.default_rng(2).normal(size=m.m))[0]; vals=np.sort(vals)[::-1]
    gam=m.gamma(); sc=m.symcheck()
    c1=abs(vals[1]-lamf)<1e-10 and abs(gam-(1-lamf**2))<1e-10
    out.append("L0 symmetry of K on orbits (2T): %.1e : %s"%(sc,"MET" if sc<1e-12 else "FAILED"))
    out.append("L1 control (2T, beta=1, M=1, %d orbits): top centred eigenvalue %.12f, lambda_f %.12f; gamma_opt %.12f, 1-lambda_f^2 %.12f : %s"%(m.m,vals[1],lamf,gam,1-lamf**2,"MET" if c1 else "FAILED"))
    L2=True; res={}
    for spec in sys.argv[2:]:
        nm,bs=spec.split(':')
        for beta in [float(x) for x in bs.split(',')]:
            m=Ladder(nm,beta); m.vacuum(); L2&=bool((m.Om>0).all() or (m.Om<0).all())
            if m.m<=6000:
                T=m.dense(); T=(T+T.T)/2; ev,V=np.linalg.eigh(T); o=np.argsort(-ev); ev=ev[o]; V=V[:,o]
            else:
                ev,V=eigsh(LinearOperator((m.m,m.m),matvec=m.That,dtype=float),k=12,which='LA',tol=1e-12,v0=m.Om+0.01*np.random.default_rng(3).normal(size=m.m)); o=np.argsort(-ev); ev=ev[o]; V=V[:,o]
            L2&=bool(ev.min()>-1e-10 and ev.max()<1+1e-10)
            gam=m.gamma(); line="%s beta %.2f (%d orbits): gamma_opt = %.8f ; lattice gap = %.8f"%(nm,beta,m.m,gam,-np.log(ev[1]))
            if m.m<=6000:
                keep=np.arange(1,m.m); evk=np.clip(ev[keep],1e-300,1-1e-15); GV=np.column_stack([m.G(V[:,i]) for i in keep])
                A=(GV/(-np.log(evk)))@GV.T; kap=np.linalg.eigvalsh((A+A.T)/2).max(); line+=" ; kappa = %.6f"%kap
            else:
                line+=" ; kappa in [%.4f, %.4f] (from gamma_opt)"%(2*(1/gam-1),2/gam)
            out.append(line); res[(nm,beta)]=(gam,-np.log(ev[1]))
            for i in range(1,9):
                Ei=-np.log(ev[i]); w=np.linalg.norm(m.G(V[:,i]))**2
                out.append("    state %d energy %.8f fine-detail weight %.6e weight/energy %.6f"%(i,Ei,w,w/Ei))
    for (nm,beta),(g,e) in res.items():
        for nm2 in ('2O','2I'):
            if nm2!=nm and (nm2,beta) in res and (nm,nm2) in (('2T','2O'),('2O','2I'),('2T','2I')):
                g2,e2=res[(nm2,beta)]; out.append("compare beta %.2f %s vs %s: gamma_opt rel diff %.2e, gap rel diff %.2e"%(beta,nm,nm2,abs(g/g2-1),abs(e/e2-1)))
    out.append("L2 %s"%("MET" if L2 else "FAILED"))
    open(sys.argv[1],'x').write("\n".join(out)+"\n"); print("\n".join(out))
