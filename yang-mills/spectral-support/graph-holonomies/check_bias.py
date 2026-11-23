"""Independent checks of staple-pair dispersion and the two bias scales."""
from itertools import combinations
import numpy as np
from scipy.special import ive


def projection(L):
    """Compute the exact-cochain covariance by a Fourier matrix, keeping k=0 absent."""
    grid=np.indices((L,)*4).reshape(4,-1).T
    p=np.exp(2j*np.pi*grid/L)-1
    D=np.zeros((len(p),6,4),complex)
    for i,(a,b) in enumerate(combinations(range(4),2)):
        D[:,i,b]=p[:,a]
        D[:,i,a]=-p[:,b]
    denom=np.sum(np.abs(p)**2,axis=1)
    denom[0]=1
    proj=(D@D.conj().swapaxes(1,2))/denom[:,None,None]
    assert np.max(np.abs(proj@proj-proj))<1e-14
    edge=D[:,:,0]
    projected=np.einsum("nij,nj->ni",proj,edge)
    np.testing.assert_allclose(projected,edge,atol=2e-15)
    star=np.sum(np.abs(projected)**2,axis=1).mean()
    var=np.diagonal(proj,axis1=1,axis2=2).real.mean(axis=0)
    np.testing.assert_allclose(star,6,atol=5e-14)
    np.testing.assert_allclose(var,(1-L**-4)/2,atol=1e-13)
    # Two oriented copies per face direction and three independent colors.
    bias=(6*2*3*var[:3].sum()-3*star)/72
    np.testing.assert_allclose(bias, .5-.75*L**-4, atol=1e-13)
    print(f"Fourier torus {L}^4: variance of oriented six-face sum {star:.6f}; staple coefficient {bias:.8f}.")


def identities():
    rng=np.random.default_rng(1989)
    for _ in range(30):
        S=rng.normal(size=(6,4))
        S/=np.linalg.norm(S,axis=1)[:,None]
        x=np.linalg.norm(S.sum(axis=0))/6
        loops=sum(1-S[a]@S[b] for a,b in combinations(range(6),2))
        np.testing.assert_allclose(loops/36,(1-x*x)/2,atol=3e-15)
        np.testing.assert_allclose((1-x)-loops/36,(1-x)**2/2,atol=3e-15)
    print("Thirty independent six-quaternion traces reproduce the exact dispersion.")


def bessel_scales():
    # A prescribed heterogeneous exterior validates the expansions, not a Wilson sample.
    q=lambda r: ive(2,r)/ive(1,r)
    H=np.array([.125,.25,.625,1.])
    assert H.mean()==.5
    for beta in [32,128,512,2048,8192]:
        delta=np.log(q(6*beta*(1-H/beta)))-np.log(q(6*beta))
        m=int(beta**1.5)//4*4
        log_relative=m*delta.mean()
        reading=-4*beta**2/m*np.expm1(log_relative)
        bulk=(H-H**2/(2*beta)).mean()
        for kappa in (0.25,1,2.):
            second=np.exp(kappa*beta*beta*delta.mean())
            assert abs(second-np.exp(-kappa/8))<2/beta
        if beta==8192:
            assert abs(reading-bulk)<.001
        print(f"beta={beta:5d}  first correction={reading:.7f}  "
              f"critical relative mean={np.exp(beta**2*delta.mean()):.7f} (limit {np.exp(-1/8):.7f})")
    assert abs(second-np.exp(-2/4))>.1


def adverse_common_mode():
    # Across two slices the product noise is independent given the same hidden bit.
    # A mean 1/2 for the local deficit alone does not imply concentration of its run average.
    kappa=2
    limits=np.exp(-kappa*np.array([0.,1.])/4)
    relative=(limits@limits/2)/(limits.mean()**2)-1
    np.testing.assert_allclose(relative,np.tanh(kappa/8)**2,atol=1e-14)
    assert limits.mean()>np.exp(-kappa/8) and relative>0
    print(f"Shared exterior control: second-scale relative covariance {relative:.7f}; a local mean alone fails.")


if __name__=="__main__":
    identities()
    for side in [4,6,8]:
        projection(side)
    bessel_scales()
    adverse_common_mode()
