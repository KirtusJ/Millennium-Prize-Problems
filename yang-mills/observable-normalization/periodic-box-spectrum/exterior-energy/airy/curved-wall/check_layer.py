"""L2 residual about the Rayleigh quotient, including the exact Dirichlet wall layer."""
import numpy as np
from scipy.special import airy, ai_zeros, roots_genlaguerre, roots_legendre


def switch(value):
    """C2 increasing cutoff and its derivatives on the unit interval."""
    t = np.clip(value, 0, 1)
    return (t**3*(10-15*t+6*t*t), 30*t*t*(1-t)**2, 60*t*(1-t)*(1-2*t))


def moments(radius, order):
    zero = ai_zeros(1)[0][0]
    alpha = -2*zero
    delta = radius**(-.25)
    nodes, weights = roots_legendre(order)
    y, wy = roots_genlaguerre(order, 1)
    cosine, wa = roots_legendre(10)
    mass = mean = square = 0.
    for left, right in ((0, delta/2), (delta/2, delta), (delta, 16)):
        s = (left + (right-left)*(nodes+1)/2)[:, None]
        z = radius+s
        u = y/(2*z)
        a, ap, _, _ = airy(2*s+zero)
        ap *= 2
        app = (8*s-2*alpha)*a
        appp = 8*a+(8*s-2*alpha)*ap
        theta, first, second = switch(2*s/delta-1)
        first *= 2/delta
        second *= 4/delta**2
        b = 1/(4*z)+1/(2*radius)
        bp = -1/(4*z*z)
        bpp = 1/(2*z**3)
        c = -theta*b*ap
        cp = -(first*b+theta*bp)*ap-theta*b*app
        cpp = (-(second*b+2*first*bp+theta*bpp)*ap
               -2*(first*b+theta*bp)*app-theta*b*appp)
        p = u-1/z
        f = a+c*p
        fz = ap+cp*p+c/z**2
        fzz = app+cpp*p+2*cp/z**2-2*c/z**3
        chi, dchi, ddchi = switch((4-u)/3)
        dchi *= -1/3
        ddchi *= 1/9
        fu = dchi*f+chi*c
        fuu = ddchi*f+2*dchi*c
        fzu = dchi*fz+chi*cp
        f, fz, fzz = chi*f, chi*fz, chi*fzz
        dz = fz-p*f
        dzz = fzz-2*p*fz+(p*p-1/z**2)*f
        du = fu-z*f
        duu = fuu-2*z*fu+z*z*f
        dzu = fzu-p*fu-z*fz+(-1+z*p)*f
        wall = np.sqrt(radius**2-u)
        x = wall+s
        kinetic = -.5*((1+u/wall**2)*dzz+8*du+4*u*duu
                       +4*u/wall*dzu+(4/wall+u/wall**3)*dz)
        measure = weights[:, None]*(right-left)/2*wy
        mass += np.sum(measure*f*f)
        for v, weight in zip(cosine, wa):
            det_sq = (u*v/2)**2
            w = x**4-x*x*u+det_sq
            grad_sq = (4*x**3-2*x*u)**2+4*x**4*u-16*x*x*det_sq+4*det_sq*u
            potential = 2*x*x*u+2*det_sq+x*x/w-grad_sq/(8*w*w)
            h = kinetic+(potential-4*radius-alpha)*f
            mean += weight/2*np.sum(measure*f*h)
            square += weight/2*np.sum(measure*h*h)
    mu = mean/mass
    return radius**2*mu, radius**2*(square/mass-mu**2)


if __name__ == '__main__':
    for radius in (16,32,64,128,256):
        row = moments(radius, 80)
        other = moments(radius, 56)
        print(radius, *(f'{v:.8f}' for v in row))
        assert np.allclose(row, other, rtol=1e-6, atol=1e-6)
