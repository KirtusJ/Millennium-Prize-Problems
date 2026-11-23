"""Tilted gamma moments and positive-time projected electric-star covariance."""
from itertools import product

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss


def variance(R):
    # Exponentially scaled polar integral after the change y=R(1-z).
    def moment(k):
        f = lambda y: y**(mp.mpf('.5')+k)*mp.exp(-y)*mp.sqrt(max(0, 1-y/(2*R)))
        points = sorted(set([0, min(1,2*R), min(10,2*R), min(80,2*R), 2*R]))
        return mp.quad(f, points)
    a, b, c = [moment(k) for k in range(3)]
    return c/a-(b/a)**2


def radial_controls():
    mp.mp.dps = 36
    for R in (mp.mpf(1),mp.mpf(12),mp.mpf(240)):
        m = mp.besseli(2,R)/mp.besseli(1,R)
        measured = variance(R)
        assert abs(measured-R*R*(1-m*m-3*m/R)) < mp.mpf('1e-26')
    for beta in (100, 1000, 10000):
        values = []
        for deficit in (0,3,7):
            R = mp.mpf(6*beta-deficit)
            scaled = beta**2*(variance(R)-mp.mpf(3)/2+mp.mpf(1)/(8*beta))
            prediction = -mp.mpf(deficit)/48-mp.mpf(1)/32
            assert abs(scaled-prediction) < mp.mpf(.4)/beta
            values.append(float(scaled))
        print("beta, scaled variance corrections at staple deficits 0,3,7",beta,*values)


def cross(n, order=44):
    # Rescale the integration window at large separation. Symmetry of the octants
    # gives explicit real entries after sign averaging over the three momenta.
    x,w=leggauss(order)
    end=min(np.pi,48/n)
    k=(1+x)*end/2
    w=w*end/(2*np.pi)
    a=[4*np.sin(z/2)**2 for z in np.meshgrid(k,k,k,indexing="ij",sparse=True)]
    total=sum(a)
    omega=2*np.arcsinh(np.sqrt(total)/2)
    weight=w[:,None,None]*w[None,:,None]*w[None,None,:]*np.exp(-n*omega)/(2*np.sinh(omega))
    matrix=np.empty((6,6))
    for j,k in product(range(3), repeat=2):
        rows=slice(2*j,2*j+2)
        cols=slice(2*k,2*k+2)
        if j==k:
            d=weight*(a[j]-total)
            opposite=-(d*(1-a[j]/2)).sum()
            matrix[rows,cols]=[[d.sum(),opposite],[opposite,d.sum()]]
        else:
            matrix[rows,cols]=(weight*a[j]*a[k]/4).sum()
    return matrix


def direct_grid(n, side):
    # Full complex electric-curl symbol and signed staggered face offsets.
    # Midpoint grid avoids its isolated zero at k=0.
    theta=-np.pi+(np.arange(side)+.5)*2*np.pi/side
    result=np.zeros((6,6),dtype=complex)
    k2,k3=np.meshgrid(theta,theta,indexing="ij")
    for k1 in theta:
        angles=np.stack([np.full_like(k2,k1),k2,k3],axis=-1).reshape(-1,3)
        p=np.exp(1j*angles)-1
        a=(abs(p)**2).sum(axis=1)
        omega=2*np.arcsinh(np.sqrt(a)/2)
        weight=np.exp(-n*omega)/(2*np.sinh(omega)*side**3)
        for j,k in product(range(3),repeat=2):
            cov=p[:,j]*p[:,k].conj()-(a if j==k else 0)
            for r,s in product(range(2),repeat=2):
                u=np.exp(-1j*angles[:,j]) if r else -1
                v=np.exp(1j*angles[:,k]) if s else -1
                result[2*j+r,2*k+s]+=np.sum(weight*cov*u*v)
    assert np.max(abs(result.imag))<1e-12
    return result.real


def main():
    radial_controls()
    c=cross(1)
    other=direct_grid(1,42)
    assert np.max(abs(c-other)) < 6e-7
    print("complex-grid vs octant largest entry difference",np.max(abs(c-other)))
    target=1/(128*np.pi**4)
    for n in (1,2,4,16,64,256):
        mat=cross(n)
        P=np.eye(6)-np.ones((6,6))/6
        assert np.max(abs(P@mat@P-mat)) < 1e-13/n**4
        contrast=(mat[0,0]+mat[1,1]-2*mat[0,1])/2
        assert contrast<0
        coeff=np.sum(mat*mat)/1536
        print("n, coefficient, n^8 coefficient / asymptote",n,coeff,n**8*coeff/target)
    assert abs(n**8*coeff/target-1)<.00025


if __name__=="__main__":
    main()
