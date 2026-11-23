"""Predicates (fixed before first run):
P1 control: mean 4sin^2(k/2) over 64 momenta == 2 within 1e-12 (exact identity).
P2 per-mode longitudinal sum_i<|D_i a4 - D4 (P_L a)_i|^2> == 1 for single k n=(3,5,1,7), L=16, tau in {1,4,16}; tol 1e-12 (float rounding).
P3 same for ALL k with p!=0 on L=16 (count qualifying), tol 1e-12.
P4 e(tau) from explicit-matrix covariance == closed form 1-ish expression
   e = (1/L^4) sum_{k!=0}[ (p!=0)*(1 + 2 q4^2 exp(-2 tau p^2)/A) + (p==0)*3 ] within 1e-10.
P5 m(tau) matrix vs closed form (1/L^4) sum_{k!=0} 2 p^2... : m=(1/L^4)sum 2*(sum_{i<j}...) computed as
   sum_{i<j}|D_i aT_j - D_j aT_i|^2 -> p^2 exp(-2 tau p^2)/A (one transverse curl norm); tol 1e-10.
Tolerances: float64 rounding ~1e-16 * accumulation of 65536 terms -> 1e-10 sums, 1e-12 per mode."""
import numpy as np, sys
L=16
n=np.arange(L); k=2*np.pi*n/L
D1=np.exp(1j*k)-1
def modes(nv): return np.array([D1[x] for x in nv])
def build(Dv,tau):
    """return A, T matrices for one mode: Dv length4. a flowed = M a; theta = Th (M a)"""
    A=np.sum(abs(Dv)**2); D=Dv[:3]; p2=np.sum(abs(D)**2)
    PL=np.outer(D,D.conj())/p2 if p2>1e-14 else np.zeros((3,3))
    PT=np.eye(3)-PL
    M=np.eye(4,dtype=complex); M[:3,:3]=PT*np.exp(-tau*p2)+PL
    return A,p2,PL,M
def theta_rows(Dv):
    pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
    T=np.zeros((6,4),complex)
    for r,(i,j) in enumerate(pairs):
        T[r,j]+=Dv[i]; T[r,i]-=Dv[j]
    return pairs,T
def single(nv,tau):
    Dv=modes(nv); A,p2,PL,M=build(Dv,tau)
    # longitudinal electric: v = D_i a4 - D4 (PL a)_i  as linear map on a (4 comps)
    B=np.zeros((3,4),complex); B[:,3]=Dv[:3]; B[:,:3]=-Dv[3]*PL
    return np.trace(B@B.conj().T)/A   # covariance I/A
def allmodes(tau,mat=True):
    e=m=0.0; cnt=0; bad=0; maxdev=0.0; n_p=0
    import itertools
    for nv in itertools.product(range(L),repeat=4):
        if not any(nv): continue
        Dv=modes(nv); A,p2,PL,M=build(Dv,tau)
        pairs,T=theta_rows(Dv); G=T@M@M.conj().T@T.conj().T/A
        e+=sum(G[r,r].real for r,(i,j) in enumerate(pairs) if j==3)
        m+=sum(G[r,r].real for r,(i,j) in enumerate(pairs) if j<3)
        if p2>1e-12:
            n_p+=1
            d=abs(single(nv,tau)-1); maxdev=max(maxdev,d)
            if d<1e-12: cnt+=1
    return e/L**4,m/L**4,n_p,cnt,maxdev
def closed(tau):
    e=m=0.0
    import itertools
    q=4*np.sin(np.pi*n/L)**2
    for nv in itertools.product(range(L),repeat=4):
        if not any(nv): continue
        qq=q[list(nv)]; A=qq.sum(); p2=qq[:3].sum()
        if p2>1e-12:
            e+=1+2*qq[3]*np.exp(-2*tau*p2)/A; m+=p2*np.exp(-2*tau*p2)/A
        else: e+=3
    return e/L**4,m/L**4
if __name__=="__main__":
    out=open("results_flow.txt","x")
    def w(s): print(s); out.write(s+"\n")
    c=float(open("control.txt").read()); w(f"P1 control {c} {'MET' if abs(c-2)<1e-12 else 'FAIL'}")
    for tau in (1,4,16):
        s=single((3,5,1,7),tau); w(f"P2 tau={tau} single-mode long. = {s.real:.15f} dev={abs(s-1):.2e} {'MET' if abs(s-1)<1e-12 else 'FAIL'}")
    for tau in (1,4,16):
        e,m,n_p,cnt,md=allmodes(tau); ce,cm=closed(tau)
        w(f"tau={tau}: e={e:.10f} m={m:.10e} tau^2*m={tau**2*m:.10e}")
        w(f"  P3 modes with p!=0: {n_p}, qualifying(|dev|<1e-12): {cnt}, max dev {md:.2e} {'MET' if cnt==n_p else 'FAIL'}")
        w(f"  P4 closed e={ce:.10f} diff={abs(e-ce):.1e} {'MET' if abs(e-ce)<1e-10 else 'FAIL'}; P5 closed m={cm:.10e} diff={abs(m-cm):.1e} {'MET' if abs(m-cm)<1e-10 else 'FAIL'}")
