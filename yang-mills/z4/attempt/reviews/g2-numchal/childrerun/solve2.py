"""PCP T80 solver v2 (sine-DVR radial, T from grandchild/e0.py idea; P1 re-posed: HO self-test 3.0 tol 1e-6 as sine-DVR is spectral; P4 tol 1e-5 on E0,E1 between refinements).
Original predicates P2,P3 as in solve.py (FD version). h=-(1/2)Lap+2 r1^2 r2^2 sin^2 g on SO(3)-invariant functions.
Discretization: u_i=r_i f, uniform grid r_k=k*dr (k=1..N, Dirichlet at 0 and R), 3-pt FD;
orthonormal Legendre basis in L (parity p, step 2, nL functions, cos^2 = (X^2) exact);
own Lanczos with full reorthogonalisation; exchange sector s=+-1 enforced by projection.
PREDICATES (fixed before first run):
 P1 self-test (flag --ho: potential replaced by (r1^2+r2^2)/2, i.e. 6-D HO): lowest (p=0,s=+) = 3.0 within 2e-3
    (FD error ~ dr^2 * O(1) with dr=0.1 => ~1e-3; also truncation of box negligible at R=8).
 P2 ground state of the real problem is in sector p=0,s=+ (expectation: nodeless, even).
 P3 Ritz values converged: |change over last 20 Lanczos steps| < 1e-9.
 P4 convergence: E0 changes < 1e-4 between successive refinements in (R,dr,Lmax) and Richardson (dr^2) shifts < 1e-4;
    target 5 significant digits (|E| ~ O(few) => ~1e-4 abs).
Results files are opened with mode 'x' (never overwritten)."""
import numpy as np, json, sys, argparse, time
ap=argparse.ArgumentParser()
ap.add_argument("--R",type=float);ap.add_argument("--N",type=int);ap.add_argument("--nL",type=int)
ap.add_argument("--ho",action="store_true");ap.add_argument("--nev",type=int,default=3)
ap.add_argument("--sectors",default="0+,0-,1+,1-");ap.add_argument("--tag")
a=ap.parse_args()
np.random.seed(12345)
N=a.N;dr=a.R/(N+1);r=dr*np.arange(1,N+1)
k=np.arange(1,N+1);S_=np.sqrt(2/(N+1))*np.sin(np.pi*np.outer(k,k)/(N+1));T=(S_*((np.pi*k/a.R)**2/2))@S_
def Xmat(n):
    X=np.zeros((n,n))
    for L in range(n-1):
        c=(L+1)/np.sqrt(4*(L+1)**2-1);X[L,L+1]=X[L+1,L]=c
    return X
def run(p,s):
    Ls=p+2*np.arange(a.nL);nL=len(Ls)
    Xf=Xmat(Ls[-1]+4);X2=(Xf@Xf)[np.ix_(Ls,Ls)];S=np.eye(nL)-X2
    cent=0.5*Ls*(Ls+1)
    R1=r[:,None];R2=r[None,:]
    D=cent[:,None,None]*(1/R1**2+1/R2**2)[None]
    W=2*(R1**2*R2**2)
    def sym(F):return 0.5*(F+s*F.transpose(0,2,1))
    def mv(F):
        out=np.matmul(T,F)+np.matmul(F,T)+D*F
        if a.ho: out+=0.5*(R1**2+R2**2)[None]*F
        else: out+=W[None]*np.einsum("ab,bij->aij",S,F)
        return out
    v=sym(np.random.randn(nL,N,N));v/=np.linalg.norm(v)
    V=[v];al=[];be=[];prev=None;m=0
    for m in range(1,700):
        w=mv(V[-1]);al.append(np.vdot(V[-1],w))
        for _ in range(2):
            for q in V:w-=np.vdot(q,w)*q
        w=sym(w);b=np.linalg.norm(w);be.append(b);V.append(w/b)
        if m%20==0:
            Tm=np.diag(al)+np.diag(be[:-1],1)+np.diag(be[:-1],-1)
            ev=np.linalg.eigvalsh(Tm)[:a.nev]
            if prev is not None and np.max(abs(ev-prev))<1e-9:break
            prev=ev
    return ev.tolist(),m
res={"R":a.R,"N":N,"dr":dr,"nL":a.nL,"Lmax":2*(a.nL-1)+1,"ho":a.ho,"sect":{}}
for sec in a.sectors.split(","):
    t=time.time();ev,m=run(int(sec[0]),1 if sec[1]=="+" else -1)
    res["sect"][sec]={"ev":ev,"iters":m,"sec":round(time.time()-t,1)};print(sec,ev,m,flush=True)
json.dump(res,open("results/%s.json"%a.tag,"x"))
