"""Q2: A=int chi1(U1)chi1(U2) c, B=int exp(-4(1-c)), SU(2)^2 Haar (mass 1), explicit 2x2 matrices.
U = cos a + i sin a n.sigma ; Haar: (2/pi) sin^2 a da dOmega/4pi.
Rules: a: Gauss-Chebyshev 2nd kind a_k=k pi/(N+1), w_k=2/(N+1) sin^2 a_k (exact for Haar-weighted polys);
 sphere: Gauss-Legendre in cos(theta) (weights/2) x uniform phi.
 MODE red: uses invariance of the integrand under simultaneous conjugation (chi1 class fn, c invariant):
   U1 axis fixed to z, U2 phi=0; 3-dim rule N^3. MODE full: no reduction, 6-dim, small N, chunked. MODE mc: 2e6 Haar samples, seed 12345.
Predicates (fixed before first run):
 Q1 normalization: sum of weights =1 (|d|<1e-13); int chi1 =0 (<1e-13); int chi1^2 =1 (<1e-12). Source: float64 eps x ~1e4 terms.
 Q2 |Im c| max <1e-14 and c in [-1,1] (+1e-14): trace of commutator real by construction.
 Q3 red convergence: |A(N=40)-A(N=32)|<1e-10 and same for B. (analytic integrands -> geometric convergence; 1e-10 well above eps.)
 Q4 full (N_a=10,Nt=8,Np=16) agrees with red N=40 within 1e-8 for A,B  (full rule is lower order, tolerance from the red N=10 change).
 Q5 MC within 4 sigma (sigma = sample std/sqrt(n)) of red value for A and B.
 Q6 'for all' hypothesis: not applicable (no universal claim).
Result file: q2_result.txt (mode x)."""
import numpy as np
s0=np.eye(2,dtype=complex)
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1,-1]).astype(complex)
def U_of(a,n):  # a (M,), n (M,3) -> (M,2,2)
    return (np.cos(a)[:,None,None]*s0 + 1j*np.sin(a)[:,None,None]*(n[:,0,None,None]*sx+n[:,1,None,None]*sy+n[:,2,None,None]*sz))
def dag(M): return np.conj(np.swapaxes(M,-1,-2))
def chi1(U): return np.trace(U,axis1=-2,axis2=-1)**2-1
def cfun(U1,U2):
    C=U1@U2@dag(U1)@dag(U2)
    return 0.5*np.trace(C,axis1=-2,axis2=-1)
def cheb(N):
    k=np.arange(1,N+1); a=k*np.pi/(N+1); return a,2/(N+1)*np.sin(a)**2
def sphere(Nt,Np):
    x,w=np.polynomial.legendre.leggauss(Nt); th=np.arccos(x); ph=2*np.pi*np.arange(Np)/Np
    T,P=np.meshgrid(th,ph,indexing='ij'); W=np.repeat(w[:,None]/2/Np,Np,1)
    n=np.stack([np.sin(T)*np.cos(P),np.sin(T)*np.sin(P),np.cos(T)],-1).reshape(-1,3)
    return n,W.ravel()
def red(N):
    a,wa=cheb(N); x,w=np.polynomial.legendre.leggauss(N); th=np.arccos(x); wt=w/2
    a1,a2,t=np.meshgrid(a,a,th,indexing='ij'); W=wa[:,None,None]*wa[None,:,None]*wt[None,None,:]
    a1=a1.ravel();a2=a2.ravel();t=t.ravel();W=W.ravel()
    nz=np.tile([0,0,1.0],(a1.size,1)); n2=np.stack([np.sin(t),0*t,np.cos(t)],-1)
    U1=U_of(a1,nz);U2=U_of(a2,n2); c=cfun(U1,U2)
    return W,chi1(U1),chi1(U2),c
def full(Na,Nt,Np):
    a,wa=cheb(Na); n,wn=sphere(Nt,Np)
    A_=np.repeat(a,n.shape[0]); N_=np.tile(n,(Na,1)); W_=np.outer(wa,wn).ravel()
    U=U_of(A_,N_); c1=chi1(U); res=dict(w=0,A=0,B=0,c1=0,c2=0,imc=0,cmin=9,cmax=-9)
    for i in range(U.shape[0]):
        c=cfun(U[i][None],U)
        W=W_[i]*W_
        res['w']+=W.sum(); res['A']+=(W_[i]*c1[i]*W_*c1*c.real).sum(); res['B']+=(W*np.exp(-4*(1-c.real))).sum()
        res['imc']=max(res['imc'],np.abs(c.imag).max()); res['cmin']=min(res['cmin'],c.real.min()); res['cmax']=max(res['cmax'],c.real.max())
    return res
out=[]; ok=lambda b:'PASS' if b else 'FAIL'
R={}
for N in (10,16,24,32,40):
    W,x1,x2,c=red(N)
    R[N]=(np.sum(W*x1*x2*c.real),np.sum(W*np.exp(-4*(1-c.real))),W.sum(),np.abs(c.imag).max(),c.real.min(),c.real.max())
    out.append(f"red N={N}: A={R[N][0]:.12f} B={R[N][1]:.12f} sumW={R[N][2]:.15f} max|Im c|={R[N][3]:.1e} c in [{R[N][4]:.6f},{R[N][5]:.6f}]")
a,wa=cheb(40); x,w=np.polynomial.legendre.leggauss(1)  # 1D checks of normalization/orthonormality
nz=np.tile([0,0,1.0],(a.size,1)); Uc=U_of(a,nz); I0=wa.sum(); I1=(wa*chi1(Uc)).sum().real; I2=(wa*chi1(Uc)**2).sum().real
out.append(f"Q1 int1={I0:.15f} int chi1={I1:.2e} int chi1^2={I2:.15f} -> {ok(abs(I0-1)<1e-13 and abs(I1)<1e-13 and abs(I2-1)<1e-12)}")
out.append(f"Q2 {ok(max(R[N][3] for N in R)<1e-14 and min(R[N][4] for N in R)>-1-1e-14 and max(R[N][5] for N in R)<1+1e-14)}")
dA=abs(R[40][0]-R[32][0]); dB=abs(R[40][1]-R[32][1])
out.append(f"Q3 |dA|={dA:.2e} |dB|={dB:.2e} -> {ok(dA<1e-10 and dB<1e-10)}")
f=full(10,8,16)
out.append(f"full(10,8,16): A={f['A']:.12f} B={f['B']:.12f} sumW={f['w']:.15f} max|Im c|={f['imc']:.1e}")
dfA=abs(f['A']-R[40][0]); dfB=abs(f['B']-R[40][1])
out.append(f"Q4 |A_full-A_red|={dfA:.2e} |B_full-B_red|={dfB:.2e} -> {ok(dfA<1e-8 and dfB<1e-8)}")
rng=np.random.default_rng(12345); n=2_000_000
def haar(n):
    q=rng.normal(size=(n,4)); q/=np.linalg.norm(q,axis=1)[:,None]
    U=np.empty((n,2,2),complex); U[:,0,0]=q[:,0]+1j*q[:,3]; U[:,0,1]=q[:,2]+1j*q[:,1]; U[:,1,0]=-q[:,2]+1j*q[:,1]; U[:,1,1]=q[:,0]-1j*q[:,3]; return U
U1=haar(n);U2=haar(n); c=cfun(U1,U2).real
sa=chi1(U1).real*chi1(U2).real*c; sb=np.exp(-4*(1-c))
mA,eA=sa.mean(),sa.std()/np.sqrt(n); mB,eB=sb.mean(),sb.std()/np.sqrt(n)
out.append(f"MC n={n}: A={mA:.6f}+-{eA:.1e} B={mB:.6f}+-{eB:.1e}")
out.append(f"Q5 z_A={(mA-R[40][0])/eA:.2f} z_B={(mB-R[40][1])/eB:.2f} -> {ok(abs(mA-R[40][0])<4*eA and abs(mB-R[40][1])<4*eB)}")
out.append(f"FINAL A={R[40][0]:.10f} B={R[40][1]:.10f} (err est |N40-N32|: {dA:.1e}, {dB:.1e})")
with open("q2_result.txt","x") as fh: fh.write("\n".join(out)+"\n")
print("\n".join(out))
