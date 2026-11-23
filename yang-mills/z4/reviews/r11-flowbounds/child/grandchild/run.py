import numpy as np
N=16;l=1.;b=l/N;s=0.005
n=np.arange(-7,9);k=2*np.pi*n/l
kh1=(2/b)*np.sin(k*b/2)
K1,K2,K3=np.meshgrid(kh1,kh1,kh1,indexing='ij')
kh2=K1**2+K2**2+K3**2; kh=np.sqrt(kh2)
nz=kh2>0
ratio=np.zeros_like(kh); ratio[nz]=(K1**2+K2**2)[nz]/kh2[nz]
base=ratio*kh/2*np.exp(-2*s*kh2)
base[~nz]=0
# exp(i k.r) per axis: E[x,m]=exp(i k_m b x)
x=np.arange(N)
E=np.exp(1j*np.outer(x,k)*b)  # direct sum over modes, separable
# D on difference grid d=x-y in 0..15 (periodic): Dd[d1,d2,d3]
def Dgrid(t):
    G=base*np.exp(-t*kh)/l**3
    return np.einsum('ia,jb,kc,abc->ijk',E,E,E,G,optimize=True).real
X1,X2,X3=np.meshgrid(x,x,x,indexing='ij')
X=np.stack([X1.ravel(),X2.ravel(),X3.ravel()],1)
y=X*b
f=np.exp(0.8*np.cos(2*np.pi*y[:,0])+0.3*np.sin(4*np.pi*y[:,0])+0.6*np.cos(2*np.pi*y[:,1]-0.4)+0.5*np.sin(2*np.pi*y[:,2])+0.3*np.cos(2*np.pi*(y[:,0]-y[:,2])))
idx=((X[:,None,:]-X[None,:,:])%N)
flat=(idx[...,0]*N+idx[...,1])*N+idx[...,2]
def C(t):
    D=Dgrid(t)
    return 2*b**6*f@(D.ravel()[flat]**2)@f
C0=C(0.)
print("C(0)=%.12e"%C0)
res={}
for h in (1e-2,1e-3,1e-4):
    cp,cm=C(h),C(-h);c2=C(2*h)
    cen=-(cp-cm)/(2*h)
    fw1=-(cp-C0)/h
    fw2=-(-3*C0+4*cp-c2)/(2*h)          # 2nd-order one-sided
    rich=-(( 4*(cp-C0)/h -(c2-C0)/(2*h)))/3  # Richardson of fw1
    c3=C(3*h)
    fw3=-(-11*C0+18*cp-9*c2+2*c3)/(6*h)
    for nm,v in (("central",cen),("fwd1",fw1),("fwd2",fw2),("richardson(fwd1 h,2h)",rich),("fwd3",fw3)):
        print("h=%g %-22s M1=%.12e M1/M0=%.10f"%(h,nm,v,v/C0))
