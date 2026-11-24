"""Checks of four statements of a reviewing model about the free theory (Appendix E).
PREDICATES (fixed before the run):
 R1 for N in {8,16,32} and every coarse momentum: gamma from canonical correlations (maxwell.py formulas)
    equals 1/||Q (I-R^2)^{-1} Q|| computed in whitened transverse coordinates, to 1e-8.
 R2 for the same momenta with k != 0: every u in ker F satisfies ||u_0||^2 <= (14/sqrt3) sinh(w_k) ||u_H||^2
    (tested on an orthonormal basis of ker F and 20 random combinations each), tolerance 1e-9.
 R3 min over all momenta and N in {4,...,64 even powers of two} of gamma >= 0.195358.
 R4 1/lambda_max(diag(h(3),h(3),h(5)) + vv^T/4) = 0.674941363 to 1e-8, h(c)=1/(1-(c-sqrt(c^2-1))^2),
    v=(sqrt(2/sqrt8),sqrt(2/sqrt8),sqrt(2/sqrt24)); and gamma at q=(1,0,0), N=2^16 within 1e-4 of it.
Seed 3. Output resolvent_check_result.txt (not overwritten)."""
import numpy as np, itertools
src=open('maxwell.py').read(); exec(src[:src.index("def wmin")].replace('import sys, numpy as np, itertools',''))
exec(open('worstq.py').read().split("for N in [16")[0].split("def fib")[1].join(["def fib",""]) if False else "")
def fib(N,q):
    S0=np.zeros((24,24),complex); S1=np.zeros((24,24),complex); K=np.zeros((3,24),complex)
    for a,n in enumerate(itertools.product((0,1),repeat=3)):
        p=[2*np.pi*(q[i]+n[i]*N//2)/N for i in range(3)]
        if all(abs(np.sin(x/2))<1e-12 for x in p): continue
        w=omega(p); M=Mmat(p); c=1/(2*np.sinh(w)); sl=slice(3*a,3*a+3)
        S0[sl,sl]=M*c; S1[sl,sl]=M*c*np.exp(-w)
        for r,(i,j) in enumerate(PL): K[r,3*a+r]=(1+np.exp(1j*p[i]))*(1+np.exp(1j*p[j]))
    C0=K@S0@K.conj().T; G=pinv_h(C0); KS0=K@S0; KS1=K@S1
    return 1-topcc(S0-KS0.conj().T@G@KS0, S1-KS0.conj().T@G@KS1, S0-KS1.conj().T@G@KS1)
rng=np.random.default_rng(3)
def white(N,q):
    """returns gamma via compressed resolvent, and the worst ratio of R2"""
    blocks=[]; Rd=[]; Fcols=[]; lowdim=0; wk=None
    kc=[2*np.pi*q[i]/N for i in range(3)]           # low representative in [0,pi); map to [-pi/2,pi/2) alias choice below
    d2=np.exp(2j*np.array(kc))-1
    if np.linalg.norm(d2)>1e-12:
        PT=np.eye(3)-np.outer(d2,d2.conj())/np.vdot(d2,d2).real
    else: PT=None
    als=[]
    for n in itertools.product((0,1),repeat=3):
        p=np.array([2*np.pi*(q[i]+n[i]*N//2)/N for i in range(3)])
        if all(abs(np.sin(x/2))<1e-12 for x in p): continue
        als.append(p)
    # low alias: the one with all components in [-pi/2,pi/2) mod 2pi
    def islow(p): return all(((x+np.pi/2)%(2*np.pi))<np.pi for x in p)
    Fs=[]; Rs=[]; low=[]
    for p in als:
        d=np.exp(1j*p)-1; w=omega(p)
        # orthonormal basis of d^perp
        U,_,_=np.linalg.svd(np.eye(3)-np.outer(d,d.conj())/np.vdot(d,d).real); Bp=U[:,:2]
        D=np.diag(1+np.exp(1j*p))
        if PT is None: Fb=np.zeros((3,2),complex)
        else: Fb=PT@D@Bp/np.sqrt(2*np.sinh(w))
        Fs.append(Fb); Rs+= [np.exp(-w)]*2; low+=[islow(p)]*2
        if islow(p): wk=w
    F=np.hstack(Fs); Rs=np.array(Rs); low=np.array(low)
    _,s,Vh=np.linalg.svd(F); rank=(s>1e-10*max(s.max(),1e-300)).sum() if s.size else 0
    ker=Vh[rank:].conj().T
    T=ker.conj().T@np.diag(1/(1-Rs**2))@ker
    gam=1/np.linalg.eigvalsh((T+T.conj().T)/2).max()
    worst=-np.inf
    if wk is not None and low.any():
        for _ in range(20+ker.shape[1]):
            c=rng.normal(size=ker.shape[1])+1j*rng.normal(size=ker.shape[1]); u=ker@c
            worst=max(worst,np.linalg.norm(u[low])**2-(14/np.sqrt(3))*np.sinh(wk)*np.linalg.norm(u[~low])**2)
    return gam,worst
out=[]; m1=0; m2=-np.inf
for N in (8,16,32):
    for q in itertools.product(range(N//2),repeat=3):
        g1=fib(N,q); g2,w=white(N,q); m1=max(m1,abs(g1-g2)); m2=max(m2,w)
out.append("R1 max |gamma_cc - gamma_resolvent| = %.2e  %s"%(m1,"MET" if m1<1e-8 else "FAILED"))
out.append("R2 max(||u0||^2 - (14/sqrt3) sinh w ||uH||^2) = %.3e  %s"%(m2,"MET" if m2<=1e-9 else "FAILED"))
mn=min(fib(N,q) for N in (4,8,16,32,64) for q in itertools.product(range(N//2),repeat=3))
out.append("R3 min gamma over N<=64 = %.6f  %s"%(mn,"MET" if mn>=0.195358 else "FAILED"))
h=lambda c:1/(1-(c-np.sqrt(c*c-1))**2); v=np.array([np.sqrt(2/np.sqrt(8)),np.sqrt(2/np.sqrt(8)),np.sqrt(2/np.sqrt(24))])
lim=1/np.linalg.eigvalsh(np.diag([h(3),h(3),h(5)])+np.outer(v,v)/4).max(); gbig=fib(2**16,(1,0,0))
out.append("R4 axial limit %.9f (claimed 0.674941363); gamma(N=65536,q=(1,0,0)) = %.6f  %s"%(lim,gbig,"MET" if abs(lim-0.674941363)<1e-8 and abs(gbig-lim)<1e-4 else "FAILED"))
open('resolvent_check_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
