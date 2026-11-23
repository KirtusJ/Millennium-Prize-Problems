"""Stable quadrature of the actual lattice symbol at both mass clocks."""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import kve


def kernel(d, m, s, order, *, scalar=False):
    """Remove exp(-sd) and m^4 d^(3/2), or m^2 sqrt(d) for the site scalar."""
    mass = m*d
    scale = m*np.sqrt(d)
    cutoff = min(180./min(1.,np.sqrt(d)), np.pi/scale)
    nodes, weights = leggauss(order)
    # Geometrically expanding panels resolve the central peak and remote tail.
    edges = np.r_[0., 2.**np.arange(max(0,int(np.ceil(np.log2(cutoff))))), cutoff]
    half = np.diff(edges)[:,None]/2
    u = (edges[:-1,None]+(1+nodes)*half).ravel()
    w = (half*weights).ravel()/np.pi
    h2 = (u*np.sinc(scale*u/(2*np.pi)))**2
    yz = h2[:,None]+h2[None,:]
    ww = np.outer(w,w)
    total = 0.
    for hx, wx in zip(h2,w):
        spatial = scale**2*(hx+yz)
        energy = 2*np.arcsinh(.5*np.sqrt((2*np.sinh(mass/2))**2+spatial))
        delta = 2*np.arcsinh(spatial/(4*np.sinh((energy+mass)/2)))
        numerator = 1. if scalar else hx+h2[:,None]
        total += wx*np.sum(ww*numerator * (mass/(2*np.sinh(energy)))
                           * np.exp(-s*delta/m))
    return total


if __name__ == "__main__":
    for d in (16,64,256):
        m = d**-2
        logs = {}
        for s in (.25,.5,1.):
            pair = []
            for mass_ratio in (1,d):
                k = kernel(mass_ratio,m,s,10)
                coarse = kernel(mass_ratio,m,s,8)
                assert abs(coarse/k-1) < 1.e-7
                continuum = np.sqrt(mass_ratio)*kve(2,s*mass_ratio)/(2*np.pi**2*s**2)
                assert abs(k/continuum-1) < .007
                pair.append(np.log(k)+1.5*np.log(mass_ratio)-s*mass_ratio)
            logs[s]=pair
        for label, logw in [('slow',-np.sqrt(d)),('middle',-d/3),('fast',-2*d)]:
            def log_signal(s):
                light, heavy = logs[s]
                return np.logaddexp(logw+light, np.log1p(-np.exp(logw))+heavy)
            # Log ratios of the squared covariance; the bounded reading has
            # the same limits since its determinant expansion starts quadratically.
            slopes = [2*(log_signal(s)-log_signal(1))/d for s in (.5,.25)]
            print(d,label,*[round(x,6) for x in slopes])
            if d==256 and label=='fast':
                assert abs(slopes[0]-1) < .03
            if d==256 and label=='middle':
                assert slopes[0] < .04 and slopes[1] > .15

    # At t=1/M use M as the base mass. The light/heavy mass ratios are 1/D,1.
    for d in (64,256,1024):
        m = d**-2
        logw = -np.sqrt(d)
        def site_log(base, ratios):
            parts = [2*np.log(base)+.5*np.log(a)-a
                     +np.log(kernel(a,base,1,12,scalar=True)) for a in ratios]
            return np.logaddexp(logw+parts[0], np.log1p(-np.exp(logw))+parts[1])
        log_ratio = 2*(site_log(m*d,(1/d,1))-site_log(m,(1,d)))
        remainder = log_ratio-(4*np.log(d)+2*np.sqrt(d))
        print("site clock",d,"log ratio minus predicted leading terms",round(remainder,7))
        assert abs(remainder)<.01
