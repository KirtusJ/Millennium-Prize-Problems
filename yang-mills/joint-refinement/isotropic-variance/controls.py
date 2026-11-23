"""Independent finite checks of the Haar formulas, checkerboard and infrared control."""
import math
import numpy as np


def bessel_ratio_over_k(k):
    den=260.
    for j in reversed(range(2,130)):
        den=2*j+k*k/den
    return 1/den


def haar():
    # Second-kind Chebyshev nodes integrate the S^3 axial Haar law.
    theta=np.pi*np.arange(1,1025)/1025
    t=np.cos(theta)
    for k in (0.,1e-8,0.1,1.,3.4,20.,63.99):
        w=np.sin(theta)**2*np.exp(k*(t-1))
        w/=w.sum()
        mean=w@t
        axial=w@((t-mean)**2)
        transverse=w@(1-t*t)/3
        q=bessel_ratio_over_k(k)
        np.testing.assert_allclose([k*q,1-3*q-(k*q)**2,q],
                                   [mean,axial,transverse],atol=3e-14,rtol=0)
        if k in (1.,3.4):
            tv=w@np.sign(t)
            assert tv>=mean>6/25
            print("beta, TV, six-neighbor lower bound", k,tv,6*mean)
    roots=np.exp(2j*np.pi*np.arange(5)/5)
    assert abs(roots.sum())<2e-15


def geometry():
    for n in range(6,66,2):
        space=np.indices((n,n,n))
        for normal in range(3):
            mu=(normal+1)%3
            nu=(normal+2)%3
            selected=(space[normal]+space[nu])%2
            assert selected.sum()==n**3//2
            for axis in (normal,nu):
                assert np.all(selected+np.roll(selected,-1,axis)==1)
            assert np.all(selected==np.roll(selected,1,mu))
    print("checkerboard incidences across all even sides 6 to 64")


def close_to_flat(beta,order):
    theta=2/math.sqrt(beta)
    cutoff=2/(12*math.sqrt(beta))
    nodes,weights=np.polynomial.legendre.leggauss(order)
    def probability(a,b):
        def integral(lo,hi):
            x=(lo+hi)/2+(hi-lo)*nodes/2
            radius=np.sqrt(1-x*x)
            density=np.exp(a*(radius-1)+b*x)*(-np.expm1(-2*a*radius))
            return (hi-lo)*(weights@density)/2
        right=integral(cutoff,1)
        return right/(right+integral(-1,cutoff))
    return 6*(probability(beta*(5+math.cos(theta)),beta*math.sin(theta))-probability(6*beta,0))


def massive_scalar(n):
    length=np.minimum(np.arange(n),n-np.arange(n))
    idx=np.stack(np.meshgrid(length,length,length,indexing="ij"))
    s=1/n**2+4*np.sum(np.sin(np.pi*idx/n)**2,axis=0)
    fourier=1/np.sqrt(s*(s+4))
    g=np.fft.ifftn(fourier).real
    assert np.min(g)>-1e-13
    c=np.exp(-g[0,0,0])*np.sinh(g)
    radius=idx.max(axis=0)
    axial=np.stack([c[:,0,0],c[0,:,0],c[0,0,:]])
    bound=(axial[:,radius]*(idx==radius)).sum(axis=0)/(idx==radius).sum(axis=0)
    assert np.all(c<=bound+1e-14)
    floor=np.exp(-g[0,0,0])*fourier[0,0,0]
    assert c.sum()>=floor-1e-12
    print("Gaussian slice: side, susceptibility, floor, contact",n,c.sum(),floor,c[0,0,0])


if __name__=="__main__":
    haar()
    geometry()
    for beta in (3.4,16,64,256,1024):
        value=close_to_flat(beta,192)
        assert abs(value-close_to_flat(beta,384))<3e-8
        print("six near-flat event differences",beta,value)
    print("Gaussian limit",6*math.erf(1/math.sqrt(12)))
    for side in (8,16,32,64):
        massive_scalar(side)
