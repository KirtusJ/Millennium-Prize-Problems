"""Independent finite-box tests of the shell norm and the winding sum."""
from itertools import product
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
from scipy.special import ive


def oscillator_check():
    for r in (0.25, 0.125, 0.0625):
        m = (r/8)**2/4
        omega = 2*np.arcsinh(np.sqrt(m)/2)
        step = 0.35
        extent = int(np.ceil(8 / (step*np.sqrt(np.sinh(omega)))))
        y = np.arange(-extent,extent+1)*step
        offsets = np.arange(-28,29)
        weights = np.exp(-(offsets*step)**2/2)*step/np.sqrt(2*np.pi)
        gaussian = diags(weights, offsets, shape=(len(y),len(y)))
        ends = diags(np.exp(-m*y*y/4))
        top = eigsh(ends @ gaussian @ ends, k=1, which='LA',tol=1e-12,
                    v0=np.exp(-y*y/20), return_eigenvectors=False)[0]
        np.testing.assert_allclose(top**2,np.exp(-omega),atol=2e-12,rtol=0)
        print(f"r={r:.4f} two-coordinate norm={top**2:.10f} deficit/r={(1-top**2)/r:.7f}")


def winding_check(shape, theta):
    p = np.array(list(product(*[2*np.pi*np.arange(n)/n for n in shape])))
    mass = lambda k: np.sum(4*np.sin(k/2)**2, axis=-1)
    w = lambda k: 2*np.arcsinh(np.sqrt(mass(k))/2)
    excess = np.sum(w(p+theta)+w(p-theta)-2*w(p))
    assert excess > 0.01
    for t in (0.5, 2.0, 5.0):
        direct = np.mean(np.exp(-t*mass(p+theta)))
        factors = []
        for n, angle in zip(shape, theta):
            j = np.arange(1,36)
            factors.append(ive(0,2*t)+2*np.sum(ive(j*n,2*t)*np.cos(j*n*angle)))
        np.testing.assert_allclose(direct,np.prod(factors),atol=1e-14,rtol=0)
        assert np.mean(np.exp(-t*mass(p))) > direct
    np.testing.assert_allclose(np.sum(w(p+2*np.pi/np.array(shape))-w(p)),0,atol=1e-12)
    print(shape, "one charged-pair contribution per polarization pair, excess", round(excess,8))


if __name__ == '__main__':
    oscillator_check()
    for shape in [(2,2,2),(3,3,3),(4,3,2),(5,2,2)]:
        winding_check(shape,np.array([0.17,-0.31,0.23]))
