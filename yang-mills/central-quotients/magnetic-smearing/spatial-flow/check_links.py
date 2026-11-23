"""Nonlinear SU(2) Wilson-flow check on a periodic history of original links."""
import numpy as np


def mul(a,b):
    scalar=a[...,0]*b[...,0]-np.sum(a[...,1:]*b[...,1:],axis=-1)
    vec=a[...,:1]*b[...,1:]+b[...,:1]*a[...,1:]+np.cross(a[...,1:],b[...,1:])
    return np.concatenate((scalar[...,None],vec),axis=-1)


def inv(a):
    return a*np.array([1.,-1.,-1.,-1.])


def expq(v):
    r=np.linalg.norm(v,axis=-1)
    return np.concatenate((np.cos(r)[...,None],np.sinc(r/np.pi)[...,None]*v),axis=-1)


def at(a,axis,displacement=1):
    return np.roll(a,-displacement,axis=axis)


def velocity(U,axes):
    z=np.zeros(U.shape[:-1]+(3,))
    for i in axes:
        for j in axes:
            if i==j:
                continue
            u,v=U[...,i,:],U[...,j,:]
            plus=mul(mul(v,at(u,j)),inv(at(v,i)))
            back=at(v,j,-1)
            minus=mul(mul(inv(back),at(u,j,-1)),at(back,i))
            z[...,i,:]-=mul(u,inv(plus+minus))[...,1:]
    return z


def evolve(U,axes,tau,steps):
    h=tau/steps
    for _ in range(steps):
        k=velocity(U,axes)
        mid=mul(expq(h*k/2),U)
        U=mul(expq(h*velocity(mid,axes)),U)
    return U


def face(U,i,j):
    a,b=U[...,i,:],U[...,j,:]
    return mul(mul(a,at(b,i)),inv(mul(b,at(a,j))))


def main():
    shape=(3,3,3,6)
    coords=np.indices(shape)
    A=np.zeros(shape+(4,3))
    # Only past spatial links differ from identity. At the two positive slices
    # all four original links agree in this pair of histories.
    defect=coords[3]==5
    A[...,1,0]=defect*np.sin(2*np.pi*coords[0]/3)
    A[...,0,1]=0.4*defect*np.cos(2*np.pi*coords[1]/3)
    linear=at(A[...,1,:],0)-A[...,1,:]-at(A[...,0,:],1)+A[...,0,:]
    lam=sum(4*np.sin(np.pi*coords[j]/shape[j])**2 for j in range(4))
    tau=0.33
    free=np.fft.ifftn(np.fft.fftn(linear,axes=(0,1,2,3))*np.exp(-tau*lam)[...,None],
                       axes=(0,1,2,3)).real
    err=[]
    for amp in (0.2,0.1,0.05):
        U=expq(amp*A)
        flowed=evolve(U,range(4),tau,28)
        F=face(flowed,0,1)
        err.append(np.max(abs(F[...,1:]/amp-free)))
        full_change=np.max(1-F[:,:,:,1,0])
        assert full_change>1.e-10
        spatial=evolve(U,range(3),tau,14)
        np.testing.assert_allclose(face(spatial,0,1)[:,:,:,1,:],np.broadcast_to([1.,0,0,0],shape[:3]+(4,)),atol=1e-14)
        print(f"amplitude {amp:g}, full-flow change in positive-slice trace deficit {full_change:.9g}, tangent error {err[-1]:.8g}")
    assert err[2]<0.6*err[1] and err[1]<0.6*err[0]
    rng=np.random.default_rng(7291)
    U=expq(0.15*rng.standard_normal(shape+(4,3)))
    h=expq(rng.standard_normal(shape+(3,)))
    gauge=np.stack([mul(mul(h,U[...,i,:]),inv(at(h,i))) for i in range(4)],axis=-2)
    for axes in [range(3),range(4)]:
        f=face(evolve(U,axes,0.1,6),0,1)
        fg=face(evolve(gauge,axes,0.1,6),0,1)
        np.testing.assert_allclose(mul(mul(h,f),inv(h)),fg,atol=1.e-12)
    print("Both flows gauge covariant; spatial flow keeps the original slice support.")


if __name__ == "__main__":
    main()
