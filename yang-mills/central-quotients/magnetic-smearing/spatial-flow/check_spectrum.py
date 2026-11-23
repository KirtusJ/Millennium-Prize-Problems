"""Direct radial, heat-kernel, and Bessel checks for the two flow prescriptions."""
from math import exp, pi, sqrt
from scipy.integrate import quad
from scipy.special import ive
import numpy as np


def radial(fun):
    return quad(fun,0,np.inf,epsabs=1e-13,epsrel=2e-11)[0]


def full(t):
    return quad(lambda y: 2*y*exp(-y*t*t/8),0,1)[0]/(128*pi*pi)


def spatial(t):
    return radial(lambda p:p**3*exp(-2*p*p-p*t))/(6*pi*pi)


def lattice(R,t):
    n=int(R*t)
    # u=R^2/v maps the Schwinger integration range [2R^2,infinity) into (0,1/2].
    def f(v):
        u=R*R/v
        h0,h1,hn=ive([0,1,n],2*u)
        return 4*(h0-h1)*h0**2*hn*R**6/v**2
    return quad(f,0,0.5,epsabs=5e-14,epsrel=1e-9)[0]


def main():
    # Independent ellipsoidal angular average of the free four-momentum propagator.
    for t in [0,0.5,0.75,1,3]:
        from scipy.special import roots_jacobi
        x,w=roots_jacobi(96,0.5,0.5)
        integral=radial(lambda p:p**3*exp(-2*p*p)*
                        (w@((1-x*x)*np.cos(t*p*x)))/(6*pi**3))
        np.testing.assert_allclose(integral,full(t),rtol=1e-9)
    tau=[0.5,0.75,1.]
    shift=lambda f:(f(tau[0])/f(0))**2-2*(f(tau[1])/f(0))**2+(f(tau[2])/f(0))**2
    print(f"temporary four-dimensional flow form {shift(full):.12g}; spatial flow {shift(spatial):.12g}")
    assert shift(full)<-0.012 and shift(spatial)>0
    np.testing.assert_allclose(spatial(0)/full(0),8/3,rtol=1e-11)
    for R in (4,8,16):
        q=shift(lambda t:lattice(R,t))
        print(f"infinite lattice R={R} scaled K0={lattice(R,0):.11g} normalized form={q:.10g}")
        assert q<0 and abs(q-shift(full)) < 0.025/R**2
    # Two transverse modes, one real color; volume-integrated and point readings differ.
    for t in [0.,0.7,2.]:
        from_p=radial(lambda p:p**4*exp(-4*p*p-2*p*t))/(8*pi*pi)
        from_E=radial(lambda E:E**4*exp(-E*E-E*t))/(256*pi*pi)
        np.testing.assert_allclose(from_p,from_E,rtol=1e-11)
    for eps in [0.1,0.02,0.002]:
        mass=quad(lambda E:E**4*exp(-E*E)/(256*pi*pi),0,eps)[0]
        assert abs(mass*1280*pi*pi/eps**5-1)<eps**2
    print("magnetic mean ratio 8/3; integrated spectral coefficient 1/(256*pi^2); low-window power 5")
    # A positive Laplace transform is bounded by its real value on every vertical line.
    def complex_norm(z):
        u=z*z/8
        return (2*(1-(1+u)*np.exp(-u))/u**2)**2
    ratios=[abs(complex_norm(2+1j*y))/complex_norm(2).real for y in (4.,8.,12.)]
    assert ratios[0]>1 and ratios[-1]>1e8
    print("vertical ratios at 2+i*y", ratios)


if __name__=="__main__":
    main()
