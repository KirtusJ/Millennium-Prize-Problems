"""Finite geometry, original-link score, Haar normalization and free time-kernel checks."""
from collections import Counter
from itertools import combinations, product
from math import asinh, cos, exp, expm1, pi, sin, sinh, sqrt

import numpy as np
from scipy.integrate import quad
from scipy.special import ive


def reflected_geometry():
    for side in (4, 6, 8, 10, 12, 14, 16, 18, 30):
        width = 2**((side//2).bit_length()-1)
        for plane in combinations(range(4), 2):
            faces = Counter({(0,0,0,0): 1})
            for axis in range(4):
                old = 1
                while old < width:
                    reflected = Counter()
                    for base, copies in faces.items():
                        image = list(base)
                        image[axis] = 2*old-base[axis]-int(axis in plane)
                        reflected[tuple(image)] += copies
                    faces.update(reflected)
                    old *= 2
            assert sum(faces.values()) == width**4
            assert max(faces.values()) <= 4
            assert len(faces) == width**2*(width//2+1)**2
            assert 256*width**4 > side**4
        spatial = sum(1 for t in range(side) for _ in range(3))
        live, retained = (spatial+1)*side**3, (spatial-3)*side**3
        assert 3*(live-retained) == 12*side**3
    print("54 reflected blocks across nine even sides, all face multiplicities at most four")


def haar_check():
    for beta in (2, 8, 128, 4096, 10**6):
        # y=sqrt(beta)*theta keeps the integral localized in fixed-width units.
        top = min(16.,pi*sqrt(beta))
        def density(y):
            theta = y/sqrt(beta)
            return 2/pi*(sqrt(beta)*sin(theta))**2*exp(-2*beta*sin(theta/2)**2)
        scaled = quad(density,0,top,epsabs=1e-13)[0]
        exact = 2*sqrt(beta)*ive(1,beta)
        np.testing.assert_allclose(scaled,exact,rtol=4e-13)
        cap = quad(lambda y: 2/pi*(sqrt(beta)*sin(y/sqrt(beta)))**2,0,1)[0]
        assert cap >= 8/(3*pi**3) and cap <= 2/(3*pi)
    print("Five SU(2) Haar integrals reproduce the Bessel normalization and cap inequalities")


def multiply(p, q):
    return np.r_[p[0]*q[0]-p[1:]@q[1:],p[0]*q[1:]+q[0]*p[1:]+np.cross(p[1:],q[1:])]


def inverse(p):
    return p*np.array([1,-1,-1,-1])


def word(*factors):
    out = np.array([1.,0.,0.,0.])
    for factor in factors:
        out = multiply(out,factor)
    return out


def score_check():
    rng = np.random.default_rng(20261123)
    errors = []
    delta = 1e-5
    for _ in range(32):
        A,U,B = (v/np.linalg.norm(v) for v in rng.normal(size=(3,4)))
        x = rng.normal(size=3)
        x /= np.linalg.norm(x)
        for sign in (-1,1):
            def observable(step):
                shifted = word(np.r_[cos(step),x*sin(step)],U)
                return 1-word(A,shifted if sign==1 else inverse(shifted),B)[0]
            P = word(A,U if sign==1 else inverse(U),B)
            V = A if sign==1 else word(A,inverse(U))
            predicted = sign*(x @ word(inverse(V),P,V)[1:])
            fd = (observable(delta)-observable(-delta))/(2*delta)
            errors.append(abs(fd-predicted))
    assert max(errors)<1e-9
    print(f"64 raw quaternion score variations, maximum discrepancy {max(errors):.3g}")


def fourier_check():
    max_error = 0.
    for v,T in product(((.12,.14,.1),(.3,.52,.41),(1.2,2.2,.6)),(24,50,128)):
        hats = np.square(2*np.sin(np.array(v)/2))
        S = sum(hats)
        omega = 2*asinh(sqrt(S)/2)
        numerator = hats[2]*(hats[0]+hats[1])
        angles = (2*pi/T)*np.arange(T)
        for n in (0,1,4,8):
            direct = numerator*np.mean(np.cos(n*angles)/(S+4*np.sin(angles/2)**2))
            periodized = numerator*(exp(-n*omega)+exp(-(T-n)*omega))/(
                -expm1(-T*omega)*2*sinh(omega))
            max_error = max(max_error, abs(direct-periodized))
            assert 0 < periodized
    assert max_error<1e-13
    print(f"36 exact-box time Fourier coefficients against positive image sums, error {max_error:.3g}")


if __name__ == "__main__":
    reflected_geometry()
    haar_check()
    score_check()
    fourier_check()
