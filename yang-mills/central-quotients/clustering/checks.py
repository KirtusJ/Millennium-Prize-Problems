"""Independent controls for the compact-time filter and its gap tests."""
from fractions import Fraction as F
from math import cos, cosh, exp, factorial, log, pi, sin, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.special import k0, lambertw


def response(M, x, a):
    b = np.hypot(1, a)
    def integrand(theta):
        u = sin(theta)
        # sinc is normalized with pi; handle the removable zero at lag zero.
        shape = 1. if not a else b*u*u/(u*u+a*a)
        return exp(M*(cos(theta)-b))*shape*x*np.sinc(x*u/pi)
    return (2/pi)*quad(integrand, 0, pi/2, epsabs=1e-13)[0]


def boundary(M, x, a):
    """Independent right vertical side of the rectangular contour."""
    b = np.hypot(1, a)
    def weight(u):
        return 2*b*(1+u*u)/((1+u*u)**2 + 4*a*a*u*u)
    if x == M:
        integral = quad(lambda z: weight(z)*cos(M*z), 0, 1, epsabs=1e-13)[0]
    else:
        freq, k = (x-M)/2, (x+M)/2
        def fourier(trig, weight_name):
            return quad(lambda u: weight(u)*trig(k/u), 1, np.inf,
                        weight=weight_name, wvar=freq, epsabs=4e-12, limlst=200)[0]
        integral = fourier(cos, 'cos') - fourier(sin, 'sin')
    return (2/pi)*exp(-M*b)*integral


def filter_checks():
    discrepancy = 0.
    for M in (.2, 1., 3., 8., 16.):
        static = [response(M, x, 0) for x in np.linspace(0, M, 45)]
        assert static[0] == 0 and np.min(np.diff(static)) >= -1e-12
        assert max(abs(1-y) for y in static) <= 1+1e-12
        for a in (0., .125, 1., 3.):
            for x in (M, M+.05, M+2., 2*M+7, M+45):
                residual = exp(-a*x)-response(M,x,a)
                discrepancy = max(discrepancy, abs(residual-boundary(M,x,a)))
                assert abs(residual) <= exp(-M*np.hypot(1,a))+2e-12
    assert discrepancy < 3e-12
    return discrepancy


def dimer():
    z = np.diag([1.,-1.])
    x = np.array([[0.,1.],[1.,0.]])
    eye = np.eye(2)
    a, b = np.kron(z, eye), np.kron(eye, z)
    h = -3*(a@b)-2*(np.kron(x, eye)+np.kron(eye,x))
    en, states = np.linalg.eigh(h)
    en -= en[0]
    left, right = (states.T @ op @ states[:,0] for op in (a,b))
    assert np.allclose(en, [0,2,8,10])
    assert np.allclose(left*right, [0,.8,-.2,0])
    positive = en>1e-12
    cov = (left*right)[positive].sum()
    lower = (cov-8*(1/4)**3-exp(-7/4))/(1-exp(-7/4))
    assert lower > 11/32 and np.isclose((left[positive & (en<7)]**2).sum(), .8)
    return cov, lower


def reciprocal_exp_bounds(x):
    """Rational lower and upper bounds on exp(-x), x positive."""
    n = 160
    assert 0 <= x < n+2
    total = sum((x**j/factorial(j) for j in range(n+1)), F(0))
    remainder = (x**(n+1)/factorial(n+1))/(1-x/(n+2))
    return 1/(total+remainder), 1/total


def continuum_control():
    # Connected sine-field covariance at spacetime lag tau, center separation r=8.
    def free_cov(r, tau):
        def kernel(y):
            return (1-abs(y))*k0(np.hypot(r+y,tau))/(2*pi)
        return quad(kernel,-1,0,epsabs=1e-14)[0]+quad(kernel,0,1,epsabs=1e-14)[0]
    variance = free_cov(0,0)
    def sine_cov(tau):
        return exp(-variance)*np.sinh(free_cov(8,tau))
    triple = sine_cov(1)-2*sine_cov(21)+sine_cov(41)
    ell = F(1,10**8)
    signal = reciprocal_exp_bounds(F(1,2)+F(91,10)*F(18,17))[0]/24
    exp_upper = lambda x: reciprocal_exp_bounds(F(x))[1]
    high = exp_upper(14)+3*exp_upper(42)
    infrared = (20*ell)**2+28*ell
    rigorous = (signal-exp_upper(21)-(high+infrared)/2)/9
    assert rigorous > F(12,10**8)
    assert triple > float(signal-exp_upper(21))
    return variance, triple, float(rigorous)


def clocks():
    c0 = 4*log(3)/13
    for beta in (1/sqrt(384), .01, .001, 1e-6, 1e-10):
        w = lambertw(c0*c0/(24*exp(2)*beta*beta)).real
        mu = w+2
        actual = mu/(1+(beta/c0)**2*3*(4+8*exp(mu/sqrt(2))+4*exp(mu)))**.5
        guaranteed = sqrt(w*(w+2))
        assert actual >= guaranteed
        print("beta, optimized guaranteed rate, rate at selected tilt", beta, guaranteed, actual)


if __name__ == "__main__":
    print("100 contour checks, largest two-contour discrepancy", filter_checks())
    print("dimer connected covariance and certified filter floor", *dimer())
    print("field variance, three-time sine covariance, rational band floor", *continuum_control())
    clocks()
