"""Independent contact, two-particle phase space, and displaced lattice-square controls."""
from itertools import combinations, product
from math import pi, factorial, exp
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.special import ive


def contact():
    def deriv_squared(t):
        q=ive(0,2*t)
        qp=2*(ive(1,2*t)-q)
        return 3*qp*qp*q*q
    d=2-quad(deriv_squared,0,np.inf,epsabs=1e-12)[0]
    bonds=list(combinations(range(4),2))
    matrix=np.zeros((6,6))
    for i in range(4):
        g=np.array([[float(v in e and i in e and v!=i) for e in bonds] for v in range(4) if v!=i])
        h=g.sum(axis=0)
        matrix+=np.outer(h,h)/48+d/16*(g-h/3).T@(g-h/3)
    eigen=np.linalg.eigvalsh(matrix)
    np.testing.assert_allclose(eigen, sorted([1/8]+[(1+2*d)/24]*3+[d/8]*2),atol=1e-14)
    assert abs(d-.70662424)<1e-8
    print("Schwinger-parameter d",d,"six contact eigenvalues",eigen)


def density(e,k):
    return ((e*e-k*k)**2+8*k**4/15)/(49152*pi**2) if e>=k else 0.


def shell(e,k):
    # Independent shell reduction in the original angle about the total momentum.
    # Solve a + sqrt(a^2+k^2-2ak mu) = E for a and include its radial Jacobian.
    if e<=k:
        return 0.
    def integrand(mu):
        a=(e*e-k*k)/(2*(e-k*mu))
        b=e-a
        angle=(k*mu-a)/b
        jac=1+(a-k*mu)/b
        return 2*pi*a*a*a*b*(1+angle**2)/jac
    return quad(integrand,-1,1,epsabs=2e-12,epsrel=2e-11)[0]/(1536*(2*pi)**3)


def predictions():
    for e,k in [(2,0),(2,.3),(2,1.5),(2,1.98),(2,3)]:
        assert abs(shell(e,k)-density(e,k))<=2e-10*max(1e-10,density(e,k))
    for e in (.5,2,7):
        mass=quad(lambda k: k*k*density(e,k)/(2*pi*pi),0,e,epsabs=1e-14)[0]
        assert abs(mass/(e**7/(128*pi**4*factorial(7)))-1)<2e-13
    for t in (1.2,2.4):
        for x in (.4,1.2):
            def radial(k):
                # Integrate the shell in the excess energy variable to handle the threshold.
                remaining=quad(lambda u: exp(-t*u)*density(k+u,k),0,np.inf,epsabs=1e-13)[0]
                return k*k*np.sinc(k*x/pi)*exp(-k*t)*remaining/(2*pi*pi)
            peak=quad(radial,0,48/t,epsabs=2e-14)[0]
            exact=((t*t+x*x)**2+2*(x*x-t*t)**2)/(384*pi**4*(t*t+x*x)**6)
            assert abs(peak/exact-1)<1e-8
    print("two-body angular shell, E^7 marginal, inverse transform at four displaced points passed")


def lattice(n, location, order):
    # n time steps with physical time 1. Rescaled momenta cover the octants separately.
    u,w=leggauss(order)
    end=min(n*pi,45.)
    u=(u+1)*end/2
    w=w*end/(2*n*2*pi)
    axes=np.meshgrid(u/n,u/n,u/n,indexing="ij",sparse=True)
    a=sum(4*np.sin(k/2)**2 for k in axes)
    om=2*np.arcsinh(np.sqrt(a)/2)
    measure=w[:,None,None]*w[None,:,None]*w[None,None,:]*np.exp(-n*om)/(2*np.sinh(om))
    # Average each entry over all spatial reflections by separable one-axis transforms.
    def factor(axis,i,ri,j,rj,term):
        k=axes[axis]
        def direction(z):
            scalar=np.exp(1j*z*location[axis])
            if axis==i:
                scalar=scalar*(np.exp(-1j*z) if ri else -1)
                if term:
                    scalar=scalar*np.expm1(1j*z)
            if axis==j:
                scalar=scalar*(np.exp(1j*z) if rj else -1)
                if term:
                    scalar=scalar*np.expm1(-1j*z)
            return scalar
        return (direction(k)+direction(-k)).real
    result=np.zeros((6,6))
    for i,ri,j,rj in product(range(3),range(2),range(3),range(2)):
        entry=1.
        for axis in range(3):
            entry=entry*factor(axis,i,ri,j,rj,True)
        if i==j:
            diagonal=a
            for axis in range(3):
                diagonal=diagonal*factor(axis,i,ri,j,rj,False)
            entry=entry-diagonal
        result[2*i+ri,2*j+rj]=np.sum(measure*entry)*n**4
    assert abs(result.sum(axis=0)).max()<5e-13
    return np.sum(result**2)/1536


def orientations():
    rng=np.random.default_rng(3796)
    faces=list(combinations(range(4),2))
    for x in [np.array([1.,1.,0.,0.])]+list(rng.normal(size=(63,4))):
        rr=x@x
        eye=np.eye(4)
        inv=eye-2*np.outer(x,x)/rr
        # Mixed second derivatives in the two coordinates of the photon Green function.
        deriv=eye/(2*pi**2*rr**2)-2*np.outer(x,x)/(pi**2*rr**3)
        face=np.array([[eye[b,d]*deriv[a,c]-eye[b,c]*deriv[a,d]
                        -eye[a,d]*deriv[b,c]+eye[a,c]*deriv[b,d]
                        for c,d in faces] for a,b in faces])
        select=np.array([[float(i in pair) for pair in faces] for i in range(4)])
        gram=select@(face**2)@select.T/384
        np.testing.assert_allclose(gram,(1+2*inv**2)/(384*pi**4*rr**4),rtol=2e-13)
        scalar=np.full(4,.25)
        T=eye[0]-scalar
        assert abs(scalar@gram@T)<1e-12*(scalar@gram@scalar)
        h=x[0]**2
        r2=x[1:]@x[1:]
        pred=(3*h*h-10*h*r2+3*r2*r2)/(768*pi**4*rr**6)
        assert abs(T@gram@T-pred)<1e-12*(scalar@gram@scalar)
        if x[0]==1:
            assert pred<0
    assert 3/(4*16*48**2)==1/49152 and 6/(15*16*48**2)==1/92160
    print("64 spacetime displacements: 16 orientation pairs, mixed cancellation, signed tensor node and both Meyer coefficients passed")


def compare():
    for y in [(0,0,0),(.5,.25,0),(1,0,0)]:
        s=sum(t*t for t in y)
        target=((1+s)**2+2*(s-1)**2)/(384*pi**4*(1+s)**6)
        errors=[]
        for n in (8,16,32,64):
            val=lattice(n,[int(n*p) for p in y],80)
            errors.append(float(abs(val/target-1)))
        refined=lattice(64,[int(64*p) for p in y],102)
        assert abs(refined/val-1)<3e-8, (y, refined/val-1,errors)
        assert all(a>b for a,b in zip(errors,errors[1:])) and errors[-1]<.005
        print("lag/spacing n=8,16,32,64; x=",y,"relative errors",errors,"quadrature change",float(abs(refined/val-1)))


if __name__=="__main__":
    contact()
    predictions()
    orientations()
    compare()
