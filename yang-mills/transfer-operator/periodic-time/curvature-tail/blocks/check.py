"""Predictable fractions for two incident, differently oriented central faces."""
import numpy as np
from scipy.fft import dct, dst
from scipy.integrate import quad
from scipy.special import ive


def relative_covariance(radius):
    n = 2*radius
    # On the common edge orientation 0, the two boundary currents differ
    # only in which transverse axis carries the opposing edge.
    source = np.zeros((n,n-1,n-1,n-1))
    source[radius,radius-1,radius-1,radius-1] = 1
    if radius > 1:
        source[radius,radius,radius-1,radius-1] = -1
    modes = dct(source, type=2, axis=0, norm="ortho")
    for axis in (1,2,3):
        modes = dst(modes, type=1, axis=axis, norm="ortho")
    w = 4*np.sin(np.pi*np.arange(n)/(2*n))**2
    eig = w[:,None,None,None]+w[None,1:,None,None]+w[None,None,1:,None]+w[None,None,None,1:]
    diagonal = 2*np.sum(modes*modes/eig)
    cross = np.sum(modes*modes.swapaxes(1,2)/eig)
    return diagonal, cross


def main():
    # Integral of the scalar four-dimensional heat kernel with one difference
    # in each of two perpendicular directions, for the common edge component.
    def integrand(t):
        p, q = ive(0,2*t), ive(1,2*t)
        return (p-q)**2*p**2
    cross, error = quad(integrand, 0, np.inf, epsabs=1e-14, epsrel=1e-13)
    assert error < 2e-14
    print(f"Free cross covariance {cross:.10f}")
    signs = np.array([1.,-1.])
    previous = np.ones(2)
    for radius in (1,2,4,8,12):
        diagonal, off_diagonal = relative_covariance(radius)
        t = 1-(diagonal+signs*off_diagonal)/(.5+signs*cross)
        if radius == 1:
            np.testing.assert_allclose([diagonal,off_diagonal],[7/24,7/48],rtol=1e-14)
        assert (t>0).all() and (t<previous).all()
        previous = t
        print(f"R={radius:2}, t_plus={t[0]:.9g}, t_minus={t[1]:.9g}, "
              f"R^4 t_max={radius**4*max(t):.7f}")


if __name__ == "__main__":
    main()
