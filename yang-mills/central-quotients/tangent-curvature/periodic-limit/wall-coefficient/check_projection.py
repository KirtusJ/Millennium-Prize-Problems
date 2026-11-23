"""Quadrature of the angular quadratic form before expanding its Jacobian."""
import numpy as np
from scipy.special import roots_genlaguerre, roots_legendre


def angular_check(r, order):
    t, wt = roots_genlaguerre(order, 1)
    z, wz = roots_legendre(order)
    # t=2 r^3 |b|^2; z=2 det(b)/|b|^2 on a uniform three-sphere.
    h = t[:, None]/(2*r**3)
    k = h*z[None, :]/2
    weights = wt[:, None]*wz[None, :]/2
    # Localized trial cutoff, identically one for |b| <= 1/8.
    angle = np.pi/2 * np.clip((h-1/64)/(3/64), 0, 1)
    cutoff = np.where(h<1/16, np.cos(angle), 0.)
    derivative = np.where((h>1/64)&(h<1/16), -32*np.pi/3*np.sin(angle), 0.)
    active = (h[:, 0]<1/16)
    h, k, weights = h[active], k[active], weights[active]
    cutoff, derivative, t = cutoff[active], derivative[active], t[active,None]
    w = 1-3*h+2*h*h+k*k
    # Physical angular gradient after removing the scalar density J.
    # It is the Gaussian times a*b + c*cofactor(b).
    a = (-2*r**3-(-3+4*h)/w-0.5/(1-h))*cutoff+2*derivative
    c = -k/w*cutoff
    gradient_square = (a*a+c*c)*h+4*a*c*k-(a*h+2*c*k)**2
    norm = np.sum(weights*cutoff**2)
    kinetic = np.sum(weights*gradient_square)/(norm*2*r*r)
    potential = np.sum(weights*cutoff**2*(2*(1-h)*h+2*k*k))*r**4/norm
    log_derivative = (3-1.5*t)/r
    avg = lambda field: np.sum(weights*cutoff**2*field)/norm
    metric = (avg(log_derivative**2)-avg(log_derivative)**2)/2
    return (kinetic+potential-4*r)*r**2, metric*r*r


if __name__ == "__main__":
    for r in (12, 16, 24, 32, 48):
        angular, radial = angular_check(r, 64)
        combined = angular+radial+6
        print(f"{r:2d} angular={angular:.8f} width={radial:.8f} combined={combined:.8f}")
        assert abs(angular_check(r, 48)[0]-angular)<1e-7
    assert abs(combined+2.5)<1e-3
