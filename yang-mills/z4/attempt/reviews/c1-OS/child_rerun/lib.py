import numpy as np
def fI(n, z):
    """e^{-z} I_n(z) via periodic trapezoid of (1/pi)int_0^pi e^{z(cos th-1)}cos(n th)."""
    N = int(14*np.sqrt(z)+6*abs(n)+60)
    th = (np.arange(N)+0.5)*np.pi/N  # midpoint on half-period (even integrand)
    return np.mean(np.exp(z*(np.cos(th)-1))*np.cos(n*th))
def GA(n, m, ns=1800, smax=None):
    """Method A: Schwinger t-integral, t=e^s trapezoid."""
    smax = np.log(60/m**2) 
    s = np.linspace(-30, smax, ns); ds = s[1]-s[0]
    tot = 0.0
    for si in s:
        t = np.exp(si); p = 1.0
        for k in n: p *= fI(k, 2*t)
        tot += np.exp(-m*m*t)*p*t
    return tot*ds
def GB(n, m, N=256):
    """Method B: k4 analytic (lambda^|n4|/sqrt(a^2-4)), 3D midpoint grid in k1..k3 (slice loop over k1)."""
    k = (np.arange(N)+0.5)*2*np.pi/N - np.pi
    K2, K3 = np.meshgrid(k,k,indexing='ij'); tot=0.0
    for k1 in k:
        A = m*m + (2-2*np.cos(k1))+(2-2*np.cos(K2))+(2-2*np.cos(K3))
        a = A+2; r = np.sqrt(a*a-4); lam=(a-r)/2
        tot += np.sum(np.cos(n[0]*k1+n[1]*K2+n[2]*K3)*lam**abs(n[3])/r)
    return tot/N**3
def S(x):
    r = float(np.sqrt(sum(v*v for v in x)))
    u = np.linspace(0, 12, 6001)
    K1 = np.trapezoid(np.exp(-r*np.cosh(u))*np.cosh(u), u)
    return K1/(4*np.pi**2*r)
