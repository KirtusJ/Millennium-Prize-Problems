"""Ground-state E_0 of h=-(1/2)(Lap1+Lap2)+2|Y1xY2|^2 on rotation-invariant functions.
Discretization: r_i: sine (Dirichlet box [0,L]) basis for u=r f, evaluated as DVR on
 r_k=kL/(N+1) (exact sine kinetic matrix, diagonal potentials). gamma: Legendre basis P_l(cos g),
 even l only (Y2->-Y2 parity), l=0,2,..,2(nl-1); x^2 matrix exact. Own Lanczos, full reorth, matrix-free.
PREDICATES (recorded before first run):
 P1 control (3D HO l=0, same sine-DVR, L=8,N=60): E=1.5, tol 1e-8 (source: sine-DVR exponential
    convergence, box tail e^-64, grid spacing 0.13 << oscillator length).
 P2 main: Lanczos residual norm < 1e-6.
 P3 main: E0 between 1 and 10 (sanity; guess from gaussian trial/zero-point estimates).
 P4 main: E0 change between the two finest successive refinements < 2e-3 (box, N, nl each).
 P5 E0 non-increasing as nl increases (variational in angular space, same radial grid), tol 1e-9.
Usage: python e0.py control | python e0.py L N nl
"""
import sys, numpy as np, time
def sine_T(N,L):
    h=L/(N+1); k=np.arange(1,N+1)
    S=np.sqrt(2/(N+1))*np.sin(np.pi*np.outer(k,k)/(N+1))   # orthogonal, symmetric
    w=(np.pi*k/L)**2/2
    return (S*w)@S, h*k
def control():
    T,r=sine_T(60,8.0); H=T+np.diag(0.5*r**2)
    return np.linalg.eigvalsh(H)[0]
def lanczos(mv,n,kmax=600,tol=1e-9,seed=0):
    rng=np.random.default_rng(seed); v=rng.standard_normal(n); v/=np.linalg.norm(v)
    V=[v]; a=[]; b=[]; old=1e9
    for j in range(kmax):
        w=mv(V[-1]); a.append(w@V[-1]); w-=a[-1]*V[-1]
        if j: w-=b[-1]*V[-2]
        for u in V: w-=(w@u)*u
        for u in V: w-=(w@u)*u
        bj=np.linalg.norm(w)
        if (j+1)%20==0 or bj<1e-12:
            Tm=np.diag(a)+np.diag(b,1)+np.diag(b,-1)
            ev,evec=np.linalg.eigh(Tm); res=abs(bj*evec[-1,0])
            if res<tol or bj<1e-12: break
            old=ev[0]
        b.append(bj); V.append(w/bj)
    x=sum(c*u for c,u in zip(evec[:,0],V)); return ev[0],res,j+1,x
def main(L,N,nl):
    T,r=sine_T(N,L); l=2*np.arange(nl)
    # x^2 in orthonormal Legendre basis via Gauss quadrature
    xg,wg=np.polynomial.legendre.leggauss(2*nl*2+4)
    P=np.array([np.polynomial.legendre.legval(xg,[0]*m+[1])*np.sqrt((2*m+1)/2) for m in l])
    X2=(P*wg*xg**2)@P.T
    r2=r**2; ll=l*(l+1)/2.0
    D=0.5*(1/r2[:,None]+1/r2[None,:])[:,:,None]*(l*(l+1))[None,None,:]
    W=2*(r2[:,None]*r2[None,:])[:,:,None]
    def mv(v):
        p=v.reshape(N,N,nl)
        o=np.einsum('ik,kjl->ijl',T,p)+np.einsum('jk,ikl->ijl',T,p)+D*p
        o+=W*(p-np.einsum('lm,ijm->ijl',X2,p)); return o.ravel()
    return lanczos(mv,N*N*nl)
if __name__=="__main__":
    if sys.argv[1]=="control":
        E=control(); print("control",E,abs(E-1.5))
        with open("control.txt","x") as f: f.write(f"E0={E!r} err={abs(E-1.5):.3e} tol=1e-8 pass={abs(E-1.5)<1e-8}\n")
    else:
        L,N,nl=float(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]); t=time.time()
        E,res,it,_=main(L,N,nl)
        line=f"L={L} N={N} nl={nl} E0={E:.8f} res={res:.1e} it={it} t={time.time()-t:.0f}s"
        print(line); open("results_%g_%d_%d.txt"%(L,N,nl),"x").write(line+"\n")
