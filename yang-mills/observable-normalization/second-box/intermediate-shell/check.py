"""Independent finite controls for the shell penalty and nonlocal localization."""
import numpy as np
from scipy.special import roots_hermitenorm


def oscillator():
    nodes, weights = roots_hermitenorm(96)
    weights /= np.sqrt(2*np.pi)
    for radius in (.01,.1,.4,1.):
        # Freeze one per-link slow color vector at |c_i|=radius; use S>=|c_i x c_j|².
        mass = radius**2/4
        omega = 2*np.arcsinh(np.sqrt(mass)/2)
        width = np.sinh(omega)
        for y in (0.,.4,1.7):
            at = y+nodes
            got = np.exp(-mass*y*y/4)*np.dot(weights,np.exp(-(mass/4+width/2)*at**2))
            expected = np.exp(-omega/2-width*y*y/2)
            np.testing.assert_allclose(got,expected,rtol=2e-13)
        assert (1-np.exp(-omega))/radius > .35
    # Removing both transverse components would spuriously remove the penalty.
    assert abs(np.dot(weights,np.ones_like(nodes))-1)<1e-14


def localization():
    rng = np.random.default_rng(491)
    x = np.linspace(-1,1,151)
    sigma = .058
    k = np.exp(-.5*((x[:,None]-x[None,:])/sigma)**2)
    k /= k.sum(axis=1).max()
    # Two cutoffs varying across the center and a nonconstant magnetic half-weight.
    theta = 1.2*x+.1
    chi = np.array([np.cos(theta),np.sin(theta)])
    m = np.exp(-x**4)
    t = m[:,None]*k*m[None,:]
    localized = sum(c[:,None]*t*c[None,:] for c in chi)
    defect = t-localized
    exact = .5*t*np.sum((chi[:,:,None]-chi[:,None,:])**2,axis=0)
    np.testing.assert_allclose(exact,defect,atol=1e-16)
    moment = np.sum(k*(x[:,None]-x[None,:])**2,axis=1).max()
    assert np.linalg.norm(defect,2) <= .5*1.2**2*moment+1e-14
    f = rng.normal(size=len(x))
    assert abs(f@(defect-exact)@f)<1e-13


if __name__ == "__main__":
    oscillator()
    localization()
    print("Twelve Gaussian oscillator evaluations and the signed cutoff identity passed.")
