"""Quadrature in two coordinate systems and independent Laguerre coefficient controls."""
from math import ceil, factorial, pi, sqrt
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq
from scipy.special import eval_genlaguerre, roots_genlaguerre


def nodes(lo, hi, pieces, order):
    """Map composite Gauss nodes to one interval per row."""
    x, w = leggauss(order)
    x = ((np.arange(pieces)[:, None]+(x+1)/2)/pieces).ravel()
    w = np.tile(w/(2*pieces), pieces)
    length = np.maximum(0., np.asarray(hi)-lo)[..., None]
    return np.asarray(lo)[..., None]+length*x, length*w


def outer_nodes(cuts, m, order):
    parts = [nodes(a,b,max(1,ceil((b-a)*sqrt(m)/2)),order)
             for a,b in zip(cuts[:-1],cuts[1:]) if b>a]
    return tuple(np.concatenate(v) for v in zip(*parts))


def field(p, m, center=1., a=1., b=4.):
    step = (b-a)/(2*(m-1))
    def half_angle(momentum):
        return np.arcsin(np.sqrt(-np.expm1(-step*momentum**2)))
    angle, center_angle = half_angle(p), half_angle(center)
    def kernel(t):
        return (np.sinc(m*t/pi)/np.sinc(t/pi))**2
    return np.exp(-a*p*p)*(kernel(angle-center_angle)+kernel(angle+center_angle))**2


def leg_integrals(m, half_width=1., order=12, lag=None):
    # p,q >= 0, |p-q| <= k <= p+q. The diagnostic uses k=1, E0=2.
    k, target, cap = 1., 2., 7.
    d = half_width/sqrt(m)
    switches = [0., k, cap-k, cap]
    for boundary in (target-d, target+d):
        switches += [boundary-k, (boundary+k)/2, (boundary-k)/2, boundary-cap]
    cuts = sorted(set(v for v in switches if 0<=v<=cap))
    p, dp = outer_nodes(cuts,m,order)
    low, high = abs(k-p), np.minimum(cap,k+p)
    p = p[:, None]
    def integrate(lower, upper):
        q, dq = nodes(lower,upper,max(1,ceil(k*sqrt(m))),order)
        E, z = p+q, p-q
        W = (E*E-k*k)**2+(k*k-z*z)**2
        measure = 2*dp[:,None]*dq*W*(field(p,m)*field(q,m))**2
        if lag is not None:
            tilted = measure*np.exp(-lag*(E-k))
            return tilted.sum(), np.sum(tilted*np.exp(-(E-k)))
        return np.sum(measure), np.sum(measure*m*(E-target)**2)
    norm, variance = integrate(low, high)
    if lag is not None:
        return k-np.log(variance/norm)
    inside, _ = integrate(np.maximum(low,target-d-p[:,0]),np.minimum(high,target+d-p[:,0]))
    return np.array([norm, variance, inside])


def energy_distribution(m, half_width=1., order=16):
    # Independent E,z integration over the same truncated physical triangle.
    k, target, cap = 1., 2., 7.
    d = half_width/sqrt(m)
    cuts = sorted({k, target-d, target+d, 2*cap-k, 2*cap})
    E, dE = outer_nodes(cuts,m,order)
    top = np.minimum(k,2*cap-E)
    z, dz = nodes(np.zeros_like(E),top,max(1,ceil(k*sqrt(m)/2)),order)
    E = E[:,None]
    p, q = (E+z)/2, (E-z)/2
    W = (E*E-k*k)**2+(k*k-z*z)**2
    measure = 2*dE[:,None]*dz*W*(field(p,m)*field(q,m))**2
    return E[:,0], measure.sum(axis=1)


def check_laguerre():
    y, w = roots_genlaguerre(100,2)
    A, B, k, radius = 1.3, .44, 1., .3
    omega = np.exp(2j*pi*np.arange(128)/128)
    t = A+radius*omega
    max_error = 0.
    for n in range(21):
        x = y/(A+.5)
        gamma_norm = sqrt((n+1)*(n+2))
        actual = w @ (np.cosh(B*np.sqrt(x+k*k))*eval_genlaguerre(n,2,x))
        actual /= (A+.5)**3*gamma_norm
        tilted = gamma_norm/(t+.5)**3*((t-.5)/(t+.5))**n*np.exp((A-t)*k*k)
        predicted = sum((-B*B/radius)**j*factorial(j)/factorial(2*j)
                        *np.mean(tilted*omega**(-j)) for j in range(17))
        max_error = max(max_error, abs(actual-predicted))
    assert max_error < 2e-12
    print(f"21 symmetric Laguerre coefficients, maximum absolute discrepancy {max_error:.3g}")


if __name__ == "__main__":
    check_laguerre()
    for m in (8,16,32,64,128,256,512):
        direct = leg_integrals(m)
        E, mass = energy_distribution(m)
        spectral = np.array([mass.sum(), mass @ (m*(E-2)**2),
                             mass[abs(E-2)<1/sqrt(m)].sum()])
        np.testing.assert_allclose(direct,spectral,rtol=3e-8,atol=2e-12)
        norm, error, inside = direct
        def effective(t):
            weights = mass*np.exp(-t*(E-1))
            return 1-np.log((weights @ np.exp(-(E-1)))/weights.sum())
        crossing = brentq(lambda t: effective(t)-1.5, 0., 200.)
        np.testing.assert_allclose(leg_integrals(m,lag=crossing),1.5,rtol=0,atol=2e-8)
        print(f"m={m:3} scaled second moment={error/norm:.8f} fraction={inside/norm:.8f} "
              f"time to effective energy 1.5={crossing:.5f}")
    # Compare exact integrals to finite quadrature with an analytic tail allowance.
    v, dv = nodes(0.,64*pi,256,14)
    for power, expected in ((6,pi/12),(8,151*pi/630)):
        partial = dv @ (np.sin(v)**8 / v**power)
        tail = (64*pi)**(1-power)/(power-1)
        assert partial-1e-13 <= expected <= partial+tail+1e-13
    print(f"limiting scaled second moment at [1,4]: {70/151:.8f}")
