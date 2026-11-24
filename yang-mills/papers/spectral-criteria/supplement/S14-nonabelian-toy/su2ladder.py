import numpy as np, sys, time, scipy.sparse as sps, scipy.special as spc
from scipy.sparse.linalg import LinearOperator, eigsh, cg as cgsolve, expm_multiply
from su2net import *
class Model:
    def __init__(s,J,beta,magnetic=True,Dg=6,net=None,mats=None):
        s.N=net or Net(J); N=s.N; s.n=N.n; s.beta=beta
        s.W=mats or {k:N.assemble(k) for k in ('W0','W1','C','AB','ABC')}
        s.real=all(abs(M.imag).max()<1e-13 for M in s.W.values())
        if s.real: s.W={k:M.real.tocsr() for k,M in s.W.items()}
        lam=lambda j: spc.ive(tw(j)+1,beta)/spc.ive(1,beta)
        s.K=np.zeros(N.n)
        for (ja,jb,jc,jd),(off,r0,r1) in N.blocks.items(): s.K[off:off+r0*r1]=lam(ja)*lam(jb)*lam(jc)*lam(jd)
        s.A=(0.5*beta)*(s.W['W0']+s.W['W1']-2*sps.identity(N.n)) if magnetic else None
        s.Dg=Dg
    def Mv(s,v): return v if s.A is None else expm_multiply(s.A,v)
    def T(s,v): return s.Mv(s.K*s.Mv(v))
    def vacuum(s):
        v=np.zeros(s.n); v[s.N.blocks[(0,0,0,0)][0]]=1.0; v=s.T(v); v/=np.linalg.norm(v); lam=0
        for it in range(100000):
            w=s.T(v); new=np.linalg.norm(w); w/=new
            if abs(new-lam)<1e-14*new and np.linalg.norm(w-v)<1e-12: break
            lam=new; v=w
        s.Om=w; s.L0=float(np.real(np.vdot(w,s.T(w))))
        s.coarse(s.Dg)
    def coarse(s,Dg,tol=1e-7):
        """orthonormal basis of span{ C^p AB^q ABC^r Omega : p+q+r <= Dg }, one new vector per monomial (Arnoldi by degree)"""
        ops=(s.W['C'],s.W['AB'],s.W['ABC']); idx={(0,0,0):0}; Q=[s.Om]; s.dropped=0
        for deg in range(1,Dg+1):
            for p in range(deg,-1,-1):
                for q in range(deg-p,-1,-1):
                    r=deg-p-q; x=None
                    for k,(dp,dq,dr) in enumerate(((1,0,0),(0,1,0),(0,0,1))):
                        prev=(p-dp,q-dq,r-dr)
                        if min(prev)>=0 and prev in idx: x=ops[k]@Q[idx[prev]]; break
                    if x is None: continue
                    n0=np.linalg.norm(x); Qm=np.array(Q).T
                    for _ in range(2): x=x-Qm@(Qm.conj().T@x)
                    if np.linalg.norm(x)>tol*n0: idx[(p,q,r)]=len(Q); Q.append(x/np.linalg.norm(x))
                    else: s.dropped+=1
        s.Q=np.array(Q).T
    def That(s,v): return s.T(v)/s.L0
    def P(s,v): return s.Q@(s.Q.conj().T@v)
    def G(s,v): return v-s.P(v)
    def low(s,k=6):
        ev,V=eigsh(LinearOperator((s.n,s.n),matvec=s.That,dtype=float if s.real else complex),k=k,which='LA',tol=1e-11,v0=s.Om+0.01*np.random.default_rng(3).normal(size=s.n))
        o=np.argsort(-ev); return ev[o],V[:,o]
    def gamma(s,ev,V):
        """1/||G (I - That^2)^-1 G|| with G = I - (projection on the coarse space built so far); the low eigenvectors
        (ev, V), excited states only, are treated exactly and the rest by conjugate gradients on their complement."""
        dt=float if s.real else complex; B=np.column_stack([s.Om,V])
        def comp(v): return v-B@(B.conj().T@v)
        def A(v):
            u=comp(v); return comp(u-s.That(s.That(u)))+(v-u)
        Aop=LinearOperator((s.n,s.n),matvec=A,dtype=dt)
        def Sop(v):
            g=s.G(v); c=V.conj().T@g; r=comp(g)
            x,info=cgsolve(Aop,r,rtol=1e-11,atol=0,maxiter=20000); assert info==0
            return s.G(comp(x)+V@(c/(1-ev**2)))
        mu=eigsh(LinearOperator((s.n,s.n),matvec=Sop,dtype=dt),k=1,which='LA',tol=1e-8,v0=s.G(V[:,0]+0.1*np.random.default_rng(1).normal(size=s.n)))[0][0]
        return 1/mu
if __name__=='__main__':
    J=float(sys.argv[1]); betas=[float(x) for x in sys.argv[2].split(',')]; Dg=int(sys.argv[3]); dog=len(sys.argv)>4
    t=time.time(); N=Net(J); mats={k:N.assemble(k) for k in ('W0','W1','C','AB','ABC')}; print('J',J,'basis',N.n,'assembled in %.0fs'%(time.time()-t),flush=True)
    for beta in betas:
        t=time.time(); m=Model(J,beta,Dg=Dg,net=N,mats=mats); m.vacuum(); ev,V=m.low()
        line="SU(2) J=%.1f beta %.2f: gap %.8f ; coarse space dim %d"%(J,beta,-np.log(ev[1]),m.Q.shape[1])
        for i in (1,2,3):
            E=-np.log(ev[i]); w=np.linalg.norm(m.G(V[:,i]))**2; line+=" | state %d E=%.6f w=%.4e w/E=%.4f"%(i,E,w,w/E)
        if dog: line+=" | gamma_opt %.6f"%m.gamma()
        print(line,'(%.0fs)'%(time.time()-t),flush=True)
