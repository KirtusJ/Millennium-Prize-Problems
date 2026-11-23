import numpy as np
L=8; tau=4.0; N=2000
rng=np.random.default_rng(12345)
n=np.arange(L); k=2*np.pi*n/L
D1=np.exp(1j*k)-1
g=np.meshgrid(n,n,n,n,indexing='ij')
D=np.stack([D1[x].ravel() for x in g],axis=1)   # (V,4)
q2=np.abs(D)**2; A=q2.sum(1); p2=q2[:,:3].sum(1)
m=A>1e-12; D=D[m]; q2=q2[m]; A=A[m]; p2=p2[m]; V=len(A)  # k!=0
Ds=D[:,:3]
# M = exp(-tau p2) P_T + P_L
PL=np.zeros((V,3,3),complex); nz=p2>1e-12
PL[nz]=Ds[nz,:,None]*np.conj(Ds[nz,None,:])/p2[nz,None,None]
I3=np.eye(3)[None]
M=np.exp(-tau*p2)[:,None,None]*(I3-PL)+PL
# MC
sc=1/np.sqrt(2*A)
a=(rng.standard_normal((N,V,4))+1j*rng.standard_normal((N,V,4)))*sc[None,:,None]
af=np.einsum('vij,nvj->nvi',M,a[:,:,:3])
th=Ds[None]*a[:,:,3:4]-D[None,:,3:4]*af
S=(np.abs(th)**2).sum((1,2))/L**4
mc=S.mean(); se=S.std(ddof=1)/np.sqrt(N)
# exact: T is V x 3 x 4
T=np.zeros((V,3,4),complex)
T[:,:,:3]=-D[:,3,None,None]*M
T[:,:,3]=Ds
Sig=np.eye(4)[None]/A[:,None,None]
ex=np.real(np.einsum('vij,vjk,vik->',T,Sig,np.conj(T)))/L**4
z=(mc-ex)/se
out="V=%d N=%d tau=%g seed=12345\nMC=%.8f\nSE=%.8f\nexact=%.8f\nz=%.3f sigmas\npredicate |MC-exact|<4SE: %s\n"%(V,N,tau,mc,se,ex,z,abs(mc-ex)<4*se)
open("results.txt","x").write(out); print(out)
