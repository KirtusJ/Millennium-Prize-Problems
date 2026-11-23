"""Metropolis MC, lattice (Z/1)^3 x (Z/T), temporal gauge U_0=1 except U_0(T-1)=W.
PREDICATES (fixed before first run):
 P1 (U(1), beta=4, T=64): m_fit from cosh fit of connected <cos th1(0) cos th1(t)>, window
    t=1..tmax (tmax = last t with C(t)>3*jackknife sigma, capped at 12), jackknife over R=32 independent
    replicas. PASS iff |m_fit - 0.146735| < 3*sigma_jack AND sigma_jack < 0.01 (else INCONCLUSIVE).
    Tolerance source: our own jackknife statistical error.
 P2 (SU(2), beta=16 and 64, T=64): signal exists iff C_E(1)>3 sigma at both betas (else INCONCLUSIVE).
 P3 ratio r=m_e(16)/m_e(64) (jackknife error sigma_r): PASS-A "closer to 4^{1/3}" iff |r-1.5874|<|r-4|
    i.e. r<2.794; additionally require |r-1.5874| < 3 sigma_r for 'consistent with 4^{1/3}'.
    PASS-B 'closer to 4' iff r>2.794. Either result is reported; failing of the 3-sigma consistency is
    reported as a failed predicate. Tuning of proposal width eps: during thermalisation only (target
    acceptance 0.3-0.7), frozen before measurement.
 Seeds fixed: U(1) 1234, SU(2) 5678+beta.
Result files opened mode 'x'.
usage: mc.py u1 | mc.py su2 BETA
"""
import sys, json, time
import numpy as np
T=64; R=32
def qmul(a,b):
    a0,a1,a2,a3=a[...,0],a[...,1],a[...,2],a[...,3]
    b0,b1,b2,b3=b[...,0],b[...,1],b[...,2],b[...,3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0],-1)
def qd(a): return a*np.array([1,-1,-1,-1.])
def rnd_delta(rng,shape,eps):
    g=rng.standard_normal(shape+(4,)); g[...,0]=1.0; g[...,1:]*=eps
    return g/np.linalg.norm(g,axis=-1,keepdims=True)

def fit_m(C,sig,Tn=T,cap=12):
    """cosh fit of C(t)=A cosh(m(t-T/2)) over t=1..tmax; grid+refine in m, A linear weighted LSQ."""
    ok=[t for t in range(1,cap+1) if C[t]>3*sig[t]]
    tm=0
    for t in range(1,cap+1):
        if C[t]>3*sig[t]: tm=t
        else: break
    if tm<2: return np.nan,tm
    ts=np.arange(1,tm+1); y=C[ts]; w=1/sig[ts]**2
    def chi(m):
        f=np.cosh(m*(ts-Tn/2)); A=(w*f*y).sum()/(w*f*f).sum(); return (w*(y-A*f)**2).sum()
    ms=np.linspace(0.005,3,600); c=[chi(m) for m in ms]; m0=ms[int(np.argmin(c))]
    ms=np.linspace(max(1e-4,m0-0.01),m0+0.01,401); c=[chi(m) for m in ms]
    return ms[int(np.argmin(c))],tm

def analyse(S,M,N,cap=12):
    """S[r,tau]=sum over meas of mean_t O(t)O(t+tau); M[r]=sum of mean_t O; N=#meas. jackknife over replicas."""
    Rr=S.shape[0]
    def conn(idx):
        return S[idx].sum(0)/(N*len(idx)) - (M[idx].sum()/(N*len(idx)))**2
    full=conn(np.arange(Rr))
    jk=np.array([conn(np.delete(np.arange(Rr),r)) for r in range(Rr)])
    sig=np.sqrt((Rr-1)/Rr*((jk-jk.mean(0))**2).sum(0))
    m,tm=fit_m(full,sig,cap=cap)
    ms=[fit_m(j,sig,cap=cap)[0] for j in jk]   # window frozen by full-sample sig
    ms=np.array(ms)
    err=np.sqrt((Rr-1)/Rr*((ms-ms.mean())**2).sum())
    return full,sig,m,err,tm,ms

def corr_acc(O):   # O shape (R,T) -> per-replica mean_t O(t)O(t+tau), and mean
    F=np.fft.rfft(O,axis=1); c=np.fft.irfft(F.conj()*F,n=T,axis=1)/T
    return c,O.mean(1)

def run_u1(seed=1234,beta=4.0,therm=500,nmeas=6000):
    rng=np.random.default_rng(seed)
    th=rng.uniform(-np.pi,np.pi,(R,3,T))
    # NOTE: abelian => W cancels from temporal plaquettes (U_i U_0 U_i^-1 U_0^-1 = e^{i(th_t-th_t+1)})
    def sweep(th,eps=1.5):
        acc=0;n=0
        for par in (0,1):
            idx=np.arange(par,T,2)
            old=th[:,:,idx]; new=old+eps*rng.standard_normal(old.shape)
            nb=th[:,:,(idx+1)%T]; pb=th[:,:,(idx-1)%T]
            dS=-beta*(np.cos(new-nb)+np.cos(new-pb)-np.cos(old-nb)-np.cos(old-pb))
            a=rng.random(old.shape)<np.exp(-dS)
            th[:,:,idx]=np.where(a,new,old); acc+=a.sum(); n+=a.size
        return acc/n
    for _ in range(therm): acc=sweep(th)
    S=np.zeros((R,T)); M=np.zeros(R); 
    for k in range(nmeas):
        acc=sweep(th)
        c,m=corr_acc(np.cos(th[:,0,:])); S+=c; M+=m
        c,m=corr_acc(np.cos(th[:,1,:])); S+=c; M+=m
        c,m=corr_acc(np.cos(th[:,2,:])); S+=c; M+=m
    return S,M,3*nmeas,acc

def run_su2(beta,seed,therm=1500,nmeas=3000,hits=2):
    rng=np.random.default_rng(seed)
    U=np.zeros((R,3,T,4)); U[...,0]=1.0
    W=np.zeros((R,4)); W[:,0]=1.0
    ident=np.array([1.,0,0,0])
    def Wt(idx):   # U_0 at times idx: identity except T-1
        w=np.broadcast_to(ident,(R,len(idx),4)).copy()
        m=(idx==T-1)
        if m.any(): w[:,m,:]=W[:,None,:]
        return w
    def loc(i,X,idx,Uc):
        """local action contribution (sum over plaquettes containing U_i(idx)) for candidate X (R,n,4)."""
        s=0.0
        for j in range(3):
            if j==i: continue
            Uj=Uc[:,j,idx]
            p=qmul(qmul(X,Uj),qmul(qd(X),qd(Uj)))
            s=s+(1-p[...,0])
        w=Wt(idx); wm=Wt((idx-1)%T)
        Yn=Uc[:,i,(idx+1)%T]; Zp=Uc[:,i,(idx-1)%T]
        p1=qmul(qmul(X,w),qmul(qd(Yn),qd(w)))
        p2=qmul(qmul(Zp,wm),qmul(qd(X),qd(wm)))
        return beta*(s+(1-p1[...,0])+(1-p2[...,0]))
    def sweep(eps):
        a_s=0;n=0
        for par in (0,1):
            idx=np.arange(par,T,2)
            for i in range(3):
                for _ in range(hits):
                    old=U[:,i,idx].copy()
                    new=qmul(rnd_delta(rng,old.shape[:-1],eps),old)
                    new/=np.linalg.norm(new,axis=-1,keepdims=True)
                    dS=loc(i,new,idx,U)-loc(i,old,idx,U)
                    a=rng.random(dS.shape)<np.exp(-dS)
                    U[:,i,idx]=np.where(a[...,None],new,old); a_s+=a.sum(); n+=a.size
        # W update: appears in temporal plaquettes at t=T-1, i=0..2
        for _ in range(hits):
            def wact(Wc):
                s=0.0
                for i in range(3):
                    p=qmul(qmul(U[:,i,T-1],Wc),qmul(qd(U[:,i,0]),qd(Wc)))
                    s=s+(1-p[...,0])
                return beta*s
            new=qmul(rnd_delta(rng,(R,),eps),W); new/=np.linalg.norm(new,axis=-1,keepdims=True)
            dS=wact(new)-wact(W); a=rng.random(R)<np.exp(-dS)
            W[:]=np.where(a[:,None],new,W)
        return a_s/n
    eps=0.5/np.sqrt(beta)*2
    # tuning during thermalisation only
    for k in range(therm):
        acc=sweep(eps)
        if k<therm//2 and k%50==49:
            eps*= 1.3 if acc>0.55 else (0.77 if acc<0.35 else 1.0)
    acc_f=[]
    S=np.zeros((R,T)); M=np.zeros(R); Es=[]
    for k in range(nmeas):
        acc_f.append(sweep(eps))
        E=np.zeros((R,T))
        for i in range(3):
            j=(i+1)%3
            p=qmul(qmul(U[:,i],U[:,j]),qmul(qd(U[:,i]),qd(U[:,j])))
            E+=p[...,0]
        c,m=corr_acc(E); S+=c; M+=m
    return S,M,nmeas,np.mean(acc_f),eps

if __name__=="__main__":
    t0=time.time(); mode=sys.argv[1]
    if mode=="u1":
        S,M,N,acc=run_u1(); extra={"acc":float(acc)}; tag="u1_b4"; ref=0.146735
    else:
        beta=float(sys.argv[2]); S,M,N,acc,eps=run_su2(beta,5678+int(beta)); extra={"acc":float(acc),"eps":float(eps)}; tag=f"su2_b{int(beta)}"; ref=None
    full,sig,m,err,tm,ms=analyse(S,M,N)
    out=dict(tag=tag,m=float(m),err=float(err),tmax=int(tm),N=N,R=R,T=T,C=full[:17].tolist(),sig=sig[:17].tolist(),secs=time.time()-t0,**extra)
    if ref is not None:
        out["ref"]=ref; out["P1_pass"]=bool(abs(m-ref)<3*err and err<0.01)
    with open(f"result_{tag}.json","x") as f: json.dump(out,f,indent=1)
    print(json.dumps({k:v for k,v in out.items() if k not in("C","sig")}))
    print("C[:8]",np.round(full[:8],5)); print("sig[:8]",np.round(sig[:8],5))
