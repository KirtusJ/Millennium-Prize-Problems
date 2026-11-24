"""Fine detail bounded by the energy for a scalar lattice field with a convex interaction: a numerical test of the
statement  I - P <= kappa (H - E0),  kappa = 1 / lambda_min(omega compressed to N),  for
  H = -(1/2) Laplacian + (1/2) <phi, K phi> + V(phi),  K positive definite, omega = K^(1/2), V convex,
P = projection on { g(B phi) Omega } (functions of the block variables B phi, in the vacuum representation),
N = ker B.  The statement is claimed for every convex V with the constant of the free bound.
Two systems, on a grid with a fourth-order difference Laplacian, in rotated coordinates in which the block
variables are grid axes (so P is exact on the grid):
  A: two sites, K = m^2 + k [[1,-1],[-1,1]], block variable phi1 + phi2; N = span (1,-1).
  B: three sites (open chain), K = m^2 + k * path Laplacian, block variables phi1 + phi2 and phi3; N = span (1,-1,0).
m^2 = 0.25, k = 1. kappa_exact = largest eigenvalue of Q (H - E0)^-1 Q, Q = I - P.
PREDICATES (fixed before the first run).
 Controls with known answers (free field, V = 0; the constant on the whole space equals the one-particle constant
 sup over n in N of <n, omega n>/<n, omega^2 n>):
  V1 system A: kappa_exact = 1/sqrt(m^2 + 2k) to relative 2e-3.
  V2 system B: kappa_exact = <e, omega e>/<e, omega^2 e>, e = (1,-1,0)/sqrt2, to relative 2e-3.
 The statement under test:
  V3 for each convex V in the list below and both systems, kappa_exact <= (1 + 2e-3) / lambda_N, lambda_N = <e, omega e>.
     V list: quartic lam * sum phi_x^4 with lam in {0.1, 1, 10}; lam * sum (cosh phi_x - 1), lam = 1;
     non-local convex: (phi_1 - phi_2)^4 ; (phi_1 + phi_2)^4 ; and |phi_1| + |phi_2| (convex, not smooth).
  V4 grid convergence: every kappa_exact changes by less than 2e-3 relative between the two grids used.
 Expectation outside the hypothesis (either outcome kept):
  X1 for the double well V = lam * sum (phi_x^2 - v^2)^2 - (1/2) m^2 sum phi_x^2 ... with lam = 0.5, v = 1.5 and with
     lam = 1, v = 2 (not convex), kappa_exact exceeds 1/lambda_N in system A.
The tolerance 2e-3 is the size of the discretisation error seen between grids of this kind; V4 measures it.
Numerical note (added after a first trial, kept as convexscalar_trial1.py with its progress log). The first version
factorised H directly for both systems; for the three-dimensional grid of system B the factorisation exhausted the
memory and the process was killed before any number for B was produced (the numbers for A are in the progress log
and are reproduced by this version). For system B the solves are now iterative: inverse iteration for the ground
state and conjugate gradients on the complement of the ground state, both with the diagonal as preconditioner and
relative tolerance 1e-11. Nothing else was changed; the predicates are as first written.
Usage: python3 convexscalar.py OUT"""
import sys, numpy as np, scipy.sparse as sps, scipy.sparse.linalg as spl
m2=0.25; k=1.0
def lap1(n,h):
    c=np.array([-1,16,-30,16,-1])/(12*h*h)
    return sps.diags([c[0]*np.ones(n-2),c[1]*np.ones(n-1),c[2]*np.ones(n),c[3]*np.ones(n-1),c[4]*np.ones(n-2)],[-2,-1,0,1,2],format='csr')
def system(which,n,L):
    x=np.linspace(-L,L,n); h=x[1]-x[0]; I=sps.identity(n,format='csr'); D=lap1(n,h)
    if which=='A':
        Y,Z=np.meshgrid(x,x,indexing='ij'); p1=(Y+Z)/np.sqrt(2); p2=(Y-Z)/np.sqrt(2); phis=(p1,p2)
        K=m2*np.eye(2)+k*np.array([[1,-1],[-1,1.]]); e=np.array([1,-1])/np.sqrt(2)
        Lap=sps.kron(D,I)+sps.kron(I,D); shape=(n,n); fib=1
    else:
        Y,Z,W=np.meshgrid(x,x,x,indexing='ij'); p1=(Y+Z)/np.sqrt(2); p2=(Y-Z)/np.sqrt(2); phis=(p1,p2,W)
        K=m2*np.eye(3)+k*np.array([[1,-1,0],[-1,2,-1],[0,-1,1.]]); e=np.array([1,-1,0])/np.sqrt(2)
        Lap=sps.kron(sps.kron(D,I),I)+sps.kron(sps.kron(I,D),I)+sps.kron(sps.kron(I,I),D); shape=(n,n,n); fib=1
    quad=0.5*sum(K[i,j]*phis[i]*phis[j] for i in range(len(phis)) for j in range(len(phis)))
    w,U=np.linalg.eigh(K); om=(U*np.sqrt(w))@U.T
    return dict(phis=phis,quad=quad,Lap=Lap,shape=shape,fib=fib,lamN=e@om@e,free=(e@om@e)/(e@K@e),h=h)
def kappa(S,V):
    U=(S['quad']+V).ravel(); H=(-0.5*S['Lap']+sps.diags(U)).tocsc(); shape=S['shape']
    if len(shape)==3: return kappa_iter(S,H,U)
    E0,Om=spl.eigsh(H,k=1,sigma=U.min()-1.0,which='LM'); E0=E0[0]; Om=np.abs(Om[:,0])
    A=Om.reshape(shape); nrm=np.sqrt((A*A).sum(axis=S['fib'],keepdims=True)); F=A/np.where(nrm>0,nrm,1)   # unit vector along the fibre axis for each value of the block variables
    def P(v): a=v.reshape(shape); return (F*(F*a).sum(axis=S['fib'],keepdims=True)).ravel()
    lu=spl.splu(H-(E0-1e-7)*sps.identity(H.shape[0],format='csc'))
    def Sop(v): g=v-P(v); return (lambda y: y-P(y))(lu.solve(g))
    mu=spl.eigsh(spl.LinearOperator(H.shape,matvec=Sop,dtype=float),k=1,which='LA',tol=1e-9,v0=np.random.default_rng(5).normal(size=H.shape[0]))[0][0]
    return mu,E0
def kappa_iter(S,H,U):
    shape=S['shape']; n=H.shape[0]; H=H.tocsr(); d=H.diagonal()
    def solve(sig,b,x0=None,proj=None):
        if proj is None: A=spl.LinearOperator((n,n),matvec=lambda v: H@v-sig*v,dtype=float)
        else: A=spl.LinearOperator((n,n),matvec=lambda v: H@v-sig*v+proj*(proj@v),dtype=float)
        Mi=spl.LinearOperator((n,n),matvec=lambda v: v/(d-sig),dtype=float)
        x,info=spl.cg(A,b,x0=x0,rtol=1e-11,atol=0,maxiter=20000,M=Mi); assert info==0
        return x
    x=np.exp(-0.5*(U-U.min())/max(1.0,np.sqrt(abs(U).max()))); x/=np.linalg.norm(x); sig=U.min()-1.0
    for it in range(200):
        y=solve(sig,x); y/=np.linalg.norm(y); rq=y@(H@y); res=np.linalg.norm(H@y-rq*y); x=y
        if it==14: sig=rq-0.2
        if it>14 and res<1e-9: break
    assert res<1e-8, res
    E0=rq; Om=np.abs(x)
    A=Om.reshape(shape); nrm=np.sqrt((A*A).sum(axis=S['fib'],keepdims=True)); F=A/np.where(nrm>0,nrm,1)
    def P(v): a=v.reshape(shape); return (F*(F*a).sum(axis=S['fib'],keepdims=True)).ravel()
    def Sop(v):
        g=v-P(v); g=g-Om*(Om@g); y=solve(E0,g,proj=Om); y=y-Om*(Om@y); return y-P(y)
    mu=spl.eigsh(spl.LinearOperator((n,n),matvec=Sop,dtype=float),k=1,which='LA',tol=1e-8,v0=np.random.default_rng(5).normal(size=n))[0][0]
    return mu,E0
grids={'A':((161,8.0),(227,8.0)),'B':((49,6.0),(61,6.0))}
cases=[("free",lambda p: 0*p[0],True),
 ("quartic 0.1",lambda p: 0.1*sum(q**4 for q in p),True),("quartic 1",lambda p: sum(q**4 for q in p),True),("quartic 10",lambda p: 10*sum(q**4 for q in p),True),
 ("cosh",lambda p: sum(np.cosh(q)-1 for q in p),True),("(phi1-phi2)^4",lambda p: (p[0]-p[1])**4,True),("(phi1+phi2)^4",lambda p: (p[0]+p[1])**4,True),
 ("|phi1|+|phi2|",lambda p: abs(p[0])+abs(p[1]),True),
 ("double well 0.5, 1.5",lambda p: 0.5*sum((q*q-1.5**2)**2 for q in p),False),("double well 1, 2",lambda p: sum((q*q-4)**2 for q in p),False)]
out=[]; V1=V2=V3=V4=True; X1=True
for which in 'AB':
    Ss=[system(which,n,L) for n,L in grids[which]]
    out.append("system %s: lambda_N = %.6f, 1/lambda_N = %.6f, free one-particle constant %.6f; grids n = %s, half-width %.1f"%(which,Ss[0]['lamN'],1/Ss[0]['lamN'],Ss[0]['free'],"/".join(str(g[0]) for g in grids[which]),grids[which][0][1])); print(out[-1],flush=True)
    for name,Vf,convex in cases:
        if which=='B' and not convex: continue
        ks=[kappa(S,Vf(S['phis'])) for S in Ss]; kap=ks[1][0]; rel=abs(ks[0][0]/kap-1); bound=1/Ss[0]['lamN']
        line="  %-22s kappa_exact %.6f (coarser grid %.6f, rel %.1e)  E0 %.6f  kappa*lambda_N %.4f"%(name,kap,ks[0][0],rel,ks[1][1],kap/bound)
        if convex:
            ok4=rel<2e-3; V4&=ok4; ok3=kap<=(1+2e-3)*bound; V3&=ok3; line+=("" if ok3 else " V3-FAILED")+("" if ok4 else " V4-FAILED")
            if name=="free":
                okc=abs(kap/Ss[0]['free']-1)<2e-3; line+=" control %s"%("MET" if okc else "FAILED")
                if which=='A': V1=okc
                else: V2=okc
        else:
            X1&=kap>bound; line+=" (not convex; rel between grids %.1e)"%rel
        out.append(line); print(line,flush=True)
for nm,v in (("V1",V1),("V2",V2),("V3",V3),("V4",V4)): out.append("%s %s"%(nm,"MET" if v else "FAILED"))
out.append("X1 %s"%("as expected" if X1 else "NOT as expected"))
open(sys.argv[1],'x').write("\n".join(out)+"\n"); print("\n".join(out[-5:]))
