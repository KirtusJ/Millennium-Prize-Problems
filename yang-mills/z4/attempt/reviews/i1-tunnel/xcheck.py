"""xcheck.py -- control (iii) and tie-in with the child's numbers.
PREDICATES (fixed before run):
 X1 lattice quadrature (lat.build_su2, beta=4, N=4, Nx=40, Nt=40): <Phi_000|e^{-V}|Phi_000> = B_child = 0.198249519694 to 1e-10
    (child error estimate 2e-15, my rule exact up to e^{-V} resolution; 1e-10 allows quadrature error).
 X2 <Phi_220| c |Phi_000> * sign = A_child = -1/12 to 1e-12 (polynomial integrand, exact quadrature, rounding).
 X3 beta=2: Tr T and Tr T^2 over the gauge-invariant space, from the full dense spectrum (N=12, Nx=Nt=48),
    agree with a direct Haar Monte Carlo over (U1,U2,g[,W,g']) with 4e6 samples (seed 2026) within 4 standard errors
    (4 sigma: two-sided, false alarm ~6e-5).
 X4 -ln lambda0 (free energy per time step) at beta=2 is bracketed: -ln TrT <= -ln lambda0 and
    -(1/2) ln TrT^2 <= -ln lambda0 , and lambda0 >= TrT^2 / TrT  (since sum l^2 <= l0 sum l) -- using the MC values.
"""
import numpy as np, json, lat
rep={}; fails=[]
m,hc,(a,t)=lat.build_su2(4.0,4,40,40)
e0=np.zeros((5,5,5)); e0[0,0,0]=1
f0=m.fwd(e0)
w3=(m.w[:,None,None]*m.w[None,:,None]*m.wt[None,None,:])
B=(w3*np.exp(-4.0*(1-hc))*f0*f0).sum()
e2=np.zeros((5,5,5)); e2[0,2,2]=1; f2=m.fwd(e2)
A=(w3*hc*f0*f2).sum()
sign=np.sign(m.F[0,2,0])  # F_{2,0} = +-chi_1
rep['X1_B']=B; rep['X2_A']=A; rep['X2_A_sign_of_F20_at_a_small']=float(sign)
if not abs(B-0.198249519694)<1e-10: fails.append('X1')
if not abs(abs(A)-1/12)<1e-12: fails.append('X2')
# X3
beta=2.0; N=12
md,_,_=lat.build_su2(beta,N,48,48)
ev,asym=lat.dense_from_matvec(md,lambda c:c*md.mask,(N+1,)*3)
tr1=ev.sum(); tr2=(ev**2).sum(); lam0=ev[0]
rng=np.random.default_rng(2026)
def haar(n):
    q=rng.standard_normal((n,4)); q/=np.linalg.norm(q,axis=1)[:,None]
    U=np.empty((n,2,2),complex); U[:,0,0]=q[:,0]+1j*q[:,3]; U[:,1,1]=q[:,0]-1j*q[:,3]
    U[:,0,1]=q[:,2]+1j*q[:,1]; U[:,1,0]=-q[:,2]+1j*q[:,1]; return U
dag=lambda U: np.conj(np.swapaxes(U,-1,-2))
htr=lambda U: 0.5*np.real(U[:,0,0]+U[:,1,1])
k=lambda U: np.exp(-beta*(1-htr(U)))
s1=[];s2=[]
for chunk in range(8):
    n=500000
    U1,U2,W1,W2,g,h=(haar(n) for _ in range(6))
    VU=beta*(1-htr(U1@U2@dag(U1)@dag(U2))); VW=beta*(1-htr(W1@W2@dag(W1)@dag(W2)))
    s1.append(np.exp(-VU)*k(U1@g@dag(U1)@dag(g))*k(U2@g@dag(U2)@dag(g)))
    s2.append(np.exp(-VU-VW)*k(U1@g@dag(W1)@dag(g))*k(U2@g@dag(W2)@dag(g))*k(U1@h@dag(W1)@dag(h))*k(U2@h@dag(W2)@dag(h)))
s1=np.concatenate(s1); s2=np.concatenate(s2)
m1,e1=s1.mean(),s1.std()/np.sqrt(len(s1)); m2,e2_=s2.mean(),s2.std()/np.sqrt(len(s2))
rep['X3']=dict(dim=len(ev),asym=asym,TrT_spec=tr1,TrT_MC=m1,err1=e1,z1=(m1-tr1)/e1,TrT2_spec=tr2,TrT2_MC=m2,err2=e2_,z2=(m2-tr2)/e2_,lam0=lam0,
               minus_ln_lam0=-np.log(lam0),top5=ev[:5].tolist())
if not (abs(m1-tr1)<4*e1 and abs(m2-tr2)<4*e2_): fails.append('X3')
ok4 = (-np.log(m1) <= -np.log(lam0)) and (-0.5*np.log(m2) <= -np.log(lam0)) and (lam0 >= m2/m1)
rep['X4']=dict(lower1=-np.log(m1),lower2=-0.5*np.log(m2),upper=-np.log(m2/m1),value=-np.log(lam0),ok=bool(ok4))
if not ok4: fails.append('X4')
rep['FAILED']=fails
open('results/xcheck.json','x').write(json.dumps(rep,indent=1,default=float))
print(json.dumps(rep,indent=1,default=float)); raise SystemExit(1 if fails else 0)
