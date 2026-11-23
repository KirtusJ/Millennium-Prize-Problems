"""Flat axial SU(2): projected plane metric and unsquared Gaussian fidelity."""
import numpy as np
from scipy.integrate import quad
from scipy.linalg import null_space


def check_planes():
    rng = np.random.default_rng(331)
    largest = 0.
    for p in rng.uniform(-np.pi, np.pi, size=(100, 3)):
        for delta in (-0.23, 0.11):
            shift = np.array([delta, 0, 0])
            # Right-trivialized infinitesimal gauge orbit and exponential derivative.
            d0 = 1-np.exp(1j*p)
            d1 = 1-np.exp(1j*(p+shift))
            plane = null_space(d0.conj()[None, :])
            off_orbit = np.eye(3)-np.outer(d1, d1.conj())/np.vdot(d1, d1)
            f = np.sinc(delta/(2*np.pi))
            observed = np.linalg.svd(off_orbit@np.diag([f*np.exp(0.5j*delta), 1, 1])@plane,
                                     compute_uv=False)
            x, s2, s3 = 2*np.sin(p/2)
            y = 2*np.sin((p[0]+delta)/2)
            transverse = s2*s2+s3*s3
            cosine = (f*transverse+x*y)/np.sqrt((transverse+x*x)*(transverse+y*y))
            largest = max(largest, np.max(np.abs(observed-[1, abs(cosine)])))
    assert largest < 2e-13
    print("direct plane SVD maximum error", largest)


def lattice(size, theta):
    p = 2*np.pi*np.fft.fftfreq(size)
    components = (2*np.sin(p/2))**2
    transverse = components[:, None]+components[None, :]
    delta = theta/size
    f = np.sinc(delta/(2*np.pi))
    correction = []
    for px in p:
        x = 2*np.sin(px/2)
        dy = 4*np.cos(px/2+delta/4)*np.sin(delta/4)
        y = x+dy
        m = x*x+transverse
        active = m > 0
        t = transverse[active]
        m = m[active]
        shifted = y*y+t
        dm = dy*(x+y)
        u = (np.log1p(dm/m)+np.log1p(dm/(4+m)))/4
        loss = (1-f)*(1+f)*t/m + t*((f-1)*y+dy)**2/(m*shifted)
        dv = np.log1p(-loss)/2
        change = np.log1p(2*np.sinh(u+dv/2)*np.sinh(dv/2)/np.cosh(u))
        correction.append(change.sum())
    return sum(correction)


def quartic_constant(terms):
    n = np.arange(1, terms+1, dtype=float)
    def sums(t):
        weights = np.exp(-t*n*n)
        return 1+2*sum(weights), 2*sum(n*n*weights)
    def small(s):
        t = s*s
        theta, moment = sums(np.pi**2/t)
        return 2*np.pi**1.5*(theta/2-np.pi**2*moment/t)**2*theta
    def large(t):
        theta, moment = sums(t)
        return t**3*moment**2*theta
    return 5/(24*(2*np.pi)**4)*(quad(small, 0, 1, epsabs=1e-13)[0]+
                                  quad(large, 1, np.inf, epsabs=1e-13)[0])


if __name__ == '__main__':
    check_planes()
    coefficient = quartic_constant(16)
    assert abs(coefficient-quartic_constant(24)) < 1e-15
    print("continuum quartic coefficient", format(coefficient,'.13g'))
    for size in (16,32,64,128):
        values = [lattice(size,t)/t**4 for t in (.5,.25)]
        print(size, *[format(v, '.11g') for v in values])
    assert abs(values[1]/coefficient-1) < .06
