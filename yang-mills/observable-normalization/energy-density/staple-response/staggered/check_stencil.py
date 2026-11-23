"""Position-space alternating tests built from a scalar lattice propagator."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import numpy as np
from scipy.special import gammaln


def slice_green(L, t):
    x=np.arange(L)*2*np.pi/L
    a=4*np.sin(x/2)**2
    total=a[:,None,None]+a[None,:,None]+a[None,None,:]
    omega=2*np.arcsinh(np.sqrt(total)/2)
    gh=np.zeros_like(omega)
    gh[total>0]=np.exp(-t*omega[total>0])/(2*np.sinh(omega[total>0]))
    return np.fft.ifftn(gh).real


def evaluate(L, n=1):
    G=slice_green(L,n)
    time=2*G-slice_green(L,n-1)-slice_green(L,n+1)
    idx=np.rint(np.fft.fftfreq(L)*L).astype(int)
    alt=1-2*(idx%2)
    chi=alt[:,None,None]*alt[None,:,None]*alt[None,None,:]
    C=np.zeros_like(G)
    for j in range(3):
        for k in range(3):
            spatial=np.roll(G,1,axis=k)-G
            H=np.roll(spatial,-1,axis=j)-spatial
            if j==k: H+=time
            sq=H*H/1536
            if j==k==0:
                signed=np.sum(chi*sq)
            faces=sq+np.roll(sq,1,axis=j)
            C+=faces+np.roll(faces,-1,axis=k)
    assert abs(np.sum(chi*C))<1e-18
    # The polynomial uses centered coordinates. The finite torus has seam
    # corrections to the infinite-lattice summation-by-parts identity.
    curvature=-.5*np.sum(chi*idx[:,None,None]**2*C)
    packets=[]
    for m in (16,64,256,1024):
        corr=np.zeros(L)
        keep=abs(idx)<=2*m
        corr[keep]=alt[keep]*np.exp(2*gammaln(2*m+1)-gammaln(2*m+idx[keep]+1)-gammaln(2*m-idx[keep]+1))
        read=np.sum(C*corr[:,None,None]*corr[None,:,None]*corr[None,None,:])
        packets.append(float(m*read/(3*signed)))
    return signed,curvature,packets


def incidence_control():
    rng=np.random.default_rng(923)
    n=8
    chi=(-1.)**np.indices((n,n,n)).sum(axis=0)
    F=rng.uniform(0,2,(3,n,n,n))
    psi=rng.normal(size=chi.shape)
    star=sum(f+np.roll(f,1,axis=j) for j,f in enumerate(F))
    direct=np.sum(chi*psi*star)
    face=sum(np.sum(chi*(psi-np.roll(psi,-1,axis=j))*f) for j,f in enumerate(F))
    assert abs(direct-face)<1e-12 and abs(np.sum(chi*star))<1e-12
    assert abs(np.sum(chi*F[0]))>1
    print("arbitrary face array: translated-weight residual and constant-weight sum",direct-face,np.sum(chi*star))


def compensated_control():
    file=Path(__file__).resolve().parents[2]/"star-reconstruction/check_reconstruction.py"
    spec=spec_from_file_location("wilson_abel",file)
    inverse=module_from_spec(spec)
    spec.loader.exec_module(inverse)
    S=3.
    target=-S*S/288
    relative=[]
    for beta in (10.,40.,100.):
        read=beta**3*(inverse.inverse(6*beta-S)-inverse.inverse(6*beta)+S/(48*beta**2))
        relative.append(abs(read/target-1))
        print("beta, fixed S, compensated inverse / target",beta,S,read/target)
    assert relative[-1]<.008 and relative[0]>relative[-1]
    k=np.full(3,np.pi/4)
    p=np.exp(1j*k)-1
    pol=np.array([1.,-1.,0.])/np.sqrt(2.)
    assert abs(np.vdot(p,pol))<1e-14
    pair=lambda a,b: np.sum(pol**2*(1+np.exp(-1j*(a+b))))
    zero=pair(2*k,2*k)
    vertex=3*pair(k,k)**2
    assert abs(zero)<1e-14 and abs(abs(vertex)-6)<1e-13
    print("two-leg corner vertex and four-leg absolute pairing sum",abs(zero),abs(vertex))


if __name__=="__main__":
    incidence_control()
    compensated_control()
    for L in (32,64,96):
        signed,curvature,packets=evaluate(L)
        print("spatial side, sign-summed H11^2/1536, second coordinate moment, binomial ratios",L,signed,curvature,packets)
    assert abs(curvature/signed-1)<1e-6
    assert abs(packets[-1]-1)<.002
    assert abs(signed/2.656897531777926e-6-1)<.0001
