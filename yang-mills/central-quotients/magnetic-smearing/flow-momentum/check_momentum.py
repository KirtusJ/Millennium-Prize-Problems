"""Compare phase-space and Cartesian-momentum two-point integrals for one free color."""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.special import erfc, erfcx

DENOM = 512*math.pi**2
Y, W = leggauss(72)


def line(p,t,s,flow):
    if flow == "unflowed":
        return np.exp(-p*t)
    if flow == "spatial":
        return np.exp(-p*t-2*s*p*p)
    a, b = math.sqrt(2*s)*p, t/math.sqrt(8*s)
    return (np.exp(-p*t)*erfc(a-b) + np.exp(-a*a-b*b)*erfcx(a+b))/2


def angular(E,k,y):
    z = k*y
    return ((E*E-k*k)**2+(k*k-z*z)**2)/DENOM


def integral(k,t,s,flow):
    def shell(E):
        p, q = (E+k*Y)/2, (E-k*Y)/2
        return np.dot(W, angular(E,k,Y)*line(p,t,s,flow)*line(q,t,s,flow))
    return quad(shell,k,np.inf,epsabs=1e-14,epsrel=1e-11)[0]


def cartesian(k,t,s,flow):
    def radial(p):
        def polar(mu):
            q = math.sqrt((p-k)**2+2*p*k*(1-mu))
            if q == 0:
                return 0
            cosine = (k*mu-p)/q
            return p**3*q*(1+cosine*cosine)*line(p,t,s,flow)*line(q,t,s,flow)/(32*math.pi**2)
        return quad(polar,-1,1,epsabs=1e-14,epsrel=1e-10)[0]
    return sum(quad(radial,a,b,epsabs=1e-13,epsrel=2e-9)[0]
               for a,b in ([(0,k),(k,np.inf)] if k else [(0,np.inf)]))


def density(k,E,s):
    if E < k:
        return 0
    return np.dot(W,angular(E,k,Y)*np.exp(-s*(E*E+(k*Y)**2)))


def run():
    for k in (0,0.5,1,2):
        for flow in ("full","spatial","unflowed"):
            a = integral(k,1,1,flow)
            b = cartesian(k,1,1,flow)
            assert abs(a-b) <= 2e-8*a
        for E in (max(0.7,k), k+1,k+2):
            benchmark = ((E*E-k*k)**2/256 + k**4/480)/math.pi**2
            assert math.isclose(density(k,E,0),benchmark,rel_tol=3e-14)
        full = [integral(k,t,1,"full") for t in (0,0.125,0.1875,0.25)]
        spat = [integral(k,t,1,"spatial") for t in (0,0.125,0.1875,0.25)]
        qfull = (full[1]-2*full[2]+full[3])/full[0]
        qspat = (spat[1]-2*spat[2]+spat[3])/spat[0]
        assert qfull < 0 < qspat
        for t in (0.5,2,6):
            c0 = integral(k,t,1,"unflowed")
            cf = integral(k,t,1,"full")
            envelope = 2*math.exp(-t*t/16)*integral(k,t/math.sqrt(2),1,"unflowed")
            assert 0 < c0-cf < envelope
        print(f"k={k}: short-time forms/C(0) full={qfull:.10g}, spatial={qspat:.10g}, threshold density={density(k,k,1):.10g}")
    k = 0.75
    endpoint = density(k,k,1)
    for t in (40,160,640):
        # Scale E-k with t to test the leading large-time coefficient stably.
        ratio = quad(lambda y: math.exp(-y)*density(k,k+y/t,1),0,100,epsabs=1e-15)[0]/endpoint
        print(f"k={k}, t={t}: t exp(k t) C_spatial(t,k) / threshold density = {ratio:.10g}")
    assert abs(ratio-1) < 0.01


if __name__ == "__main__":
    run()
