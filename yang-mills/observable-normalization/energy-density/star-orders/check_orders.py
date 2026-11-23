"""Rational d enclosure, Hermite cancellations and an independent transfer computation."""
from fractions import Fraction as F
from importlib.util import spec_from_file_location, module_from_spec
from itertools import product
from math import comb
from pathlib import Path

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import roots_genlaguerre


def fourier_bound():
    def raw(t,k):
        values=[comb(2*(t+j),t+j) for j in range(k+1)]
        for _ in range(3):
            values=[sum(comb(j,i)*values[i]*comb(2*(j-i),j-i) for i in range(j+1)) for j in range(k+1)]
        return values[k]
    def tilted(t,k):
        return sum(F(comb(k,j)*(-1)**j,16**j)*raw(t,j) for j in range(k+1))
    lower=sum(tilted(2,k)/16 for k in range(4))
    upper=lower+tilted(1,4)
    assert (lower,upper)==(F(5285,8192),F(6439,8192)) and upper<F(4,5)
    return lower,upper


def temporal(n):
    # Compute each eigenmode directly from its angular integrand, without
    # subtracting nearly equal matrix entries at large separation.
    x,w=leggauss(55)
    end=min(np.pi,54/n)
    k=(1+x)*end/2
    w=w*end/(2*np.pi)
    a=[4*np.sin(z/2)**2 for z in np.meshgrid(k,k,k,indexing="ij",sparse=True)]
    A=sum(a)
    omega=2*np.arcsinh(np.sqrt(A)/2)
    mu=w[:,None,None]*w[None,:,None]*w[None,None,:]*np.exp(-n*omega)/(2*np.sinh(omega))
    # Pair sums with weights (1,-1,0)/sqrt(2), and first pair difference.
    u=-(mu*(A*(a[0]+a[1])-(a[0]-a[1])**2)/4).sum()
    v=-(mu*(2-a[0]/2)*(A-a[0])).sum()
    return mp.mpf(float(u)),mp.mpf(float(v))


def sources(roots,q):
    radii=[mp.mpf(2)**(k-1) for k in range(len(roots)*(q-1)+1)]
    w=[mp.fprod((-r-z)**(q-1) for z in roots)/
       mp.fprod(t-r for t in radii if t!=r) for r in radii]
    for z in roots:
        for j in range(1,q):
            assert abs(sum(x/(r+z)**j for x,r in zip(w,radii)))<mp.mpf('1e-120')
    return radii,w


def normalized_cov(r,w,a,b,u,v):
    J=mp.mpf(0)
    for i,j in product(range(len(r)),repeat=2):
        x=u*u/((r[i]+a)*(r[j]+a))
        y=v*v/((r[i]+b)*(r[j]+b))
        J+=w[i]*w[j]*mp.expm1(-3*mp.log1p(-x)-mp.mpf(9)/2*mp.log1p(-y))
    return J


def independent_radial_check(a,b):
    # Tensor integration in three independent chi-square blocks. Directly
    # integrate the bounded reading against low- and fourth-degree tests.
    poles,weights=sources([1,a,b],2)
    lam=np.array([1.,float(a),float(b)])
    shape=np.array([1.5,3.,4.5])
    nodes=[]
    probs=[]
    for i in range(3):
        x,w=roots_genlaguerre(58,shape[i]-1)
        dims=[1,1,1]
        dims[i]=-1
        nodes.append(x.reshape(dims))
        probs.append((w/w.sum()).reshape(dims))
    S=sum(l*x for l,x in zip(lam,nodes))
    prob=probs[0]*probs[1]*probs[2]
    f=np.zeros_like(S)
    for r,w in zip(map(float,poles),map(float,weights)):
        L=np.prod((1+lam/r)**(-shape))
        f+=w*(np.exp(-S/r)/L-1)
    error=max(abs((prob*f*(x-k)).sum()) for x,k in zip(nodes,shape))
    assert error<2e-13 and abs((prob*f).sum())<2e-13
    # A degree-four Laguerre reading on the last Gaussian block.
    x,k=nodes[-1],shape[-1]
    obs=x*x-2*(k+1)*x+k*(k+1)
    val=(prob*f*obs).sum()
    target=float(k*(k+1)*b*b*sum(w/(r+b)**2 for w,r in zip(weights,poles)))
    assert abs(val-target)<3e-13 and abs(val)>.001
    print("independent radial quadrature: largest quadratic residual, quartic overlap",error,val)


def main():
    print("rational interval for d",*fourier_bound())
    mp.mp.dps=160
    base=Path(__file__).resolve().parents[1]
    def prior(name,path):
        spec=spec_from_file_location(name,base/path)
        module=module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    d=mp.mpf(float(prior("law","contact-law/check_law.py").fourier_coefficient(80)))
    old=prior("staple","staple-response/check_response.py")
    a,b=d/2,(2-d)/3
    independent_radial_check(a,b)
    u,v=temporal(2)
    spectrum=np.linalg.eigvalsh(old.cross(2))
    assert np.max(abs(spectrum-np.sort([0]+[float(u)]*2+[float(v)]*3)))<1e-12
    print("d and distinct variances",*(float(z) for z in (d,a,b)))
    for q in (1,2,3):
        roots=[mp.mpf(1),a,b]
        r,w=sources(roots,q)
        M=sum(x/(y+b)**q for x,y in zip(w,r))
        predicted=mp.rf(mp.mpf(9)/2,q)/mp.factorial(q)*M*M*(4/mp.pi**4)**q
        for n in (1,8,64,256):
            u,v=temporal(n)
            cov=normalized_cov(r,w,a,b,u,v)
            assert cov>0
            ratio=cov*n**(8*q)/predicted
            if n==256: assert abs(ratio-1)<mp.mpf('.001')
            print("order, step, covariance, scaled/target",q,n,mp.nstr(cov,9),mp.nstr(ratio,9))
    r,w=sources([a,b],2)
    assert abs(sum(x/(y+1) for x,y in zip(w,r)))>mp.mpf('.001')
    # A shorter filter leaves a nonzero quadratic coefficient on the uniform direction.
    r,w=sources([1,a,b],2)
    n=24
    u,v=temporal(n)
    base_cov=normalized_cov(r,w,a,b,u,v)
    damaged=list(w)
    damaged[0]+=mp.mpf('1e-4')
    perturbed=normalized_cov(r,damaged,a,b,u,v)
    lower=mp.mpf(9)/2*v**2*sum(x/(y+b) for x,y in zip(damaged,r))**2
    assert lower>base_cov*1000 and perturbed>=lower
    print("damaged/undamaged covariance at n=24",mp.nstr(perturbed/base_cov,9))
    print("large-step u,v amplitudes relative to analytic limits",
          float(temporal(256)[0]*256**6/(-3/mp.pi**2)),float(temporal(256)[1]*256**4/(-2/mp.pi**2)))
    # A squared Gaussian field at a single face is a second-order polynomial.
    # Its covariance with the bounded reading is proportional to R(lambda).
    assert max(abs(sum(x/(t+z) for t,x in zip(r,w))) for z in (1,a,b))<mp.mpf('1e-125')


if __name__=="__main__":
    main()
