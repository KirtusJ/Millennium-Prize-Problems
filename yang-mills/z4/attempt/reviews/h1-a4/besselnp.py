"""Scaled modified Bessel functions with numpy only (scipy absent on this machine).
ive0(z) = I_0(z) e^{-z}: power series for z<=30, asymptotic series (DLMF 10.40.1) for z>30.
ratio(n, x) = I_n(x)/I_{n-1}(x) by the backward continued fraction from DLMF 10.29.1."""
import numpy as np
from math import lgamma, log, exp
def ive0(z):
    z = np.asarray(z, float); out = np.empty_like(z)
    sm = z <= 30; x = z[sm]
    t = np.ones_like(x); s = np.ones_like(x)
    for k in range(1, 120):
        t = t*(x/2)**2/k**2; s = s+t
    out[sm] = s*np.exp(-x)
    x = z[~sm]; t = np.ones_like(x); s = np.ones_like(x)
    for k in range(1, 25):
        t = t*(2*k-1)**2/(k*8*x); s = s+t
    out[~sm] = s/np.sqrt(2*np.pi*x)
    return out
def ratio(n, x, extra=400):
    r = 0.0
    for m in range(n+extra, n-1, -1):
        r = 1.0/(2*m/x + r)
    return r
def ive1(x):
    return float(ive0(np.array([x]))[0])*ratio(1, x)
def In_over_I1(nmax, x):
    """array a[n] = I_n(x)/I_1(x) for n=0..nmax"""
    a = np.zeros(nmax+1); a[1] = 1.0
    for n in range(2, nmax+1):
        a[n] = a[n-1]*ratio(n, x)
    a[0] = 1/ratio(1, x)
    return a
if __name__ == "__main__":
    # self-test against known values: I0(1)=1.2660658777520082, I1(1)=0.5651591039924851, I0(50)e^-50 = 0.05656163266...
    print(ive0(np.array([1.0]))*np.e, ive1(1.0)*np.e, ive0(np.array([30.0, 30.0001])), ive0(np.array([50.0])))
