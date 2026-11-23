"""Independent free-lattice checks of a level shift and two coupling normalizations."""
from math import asinh, exp, factorial, log, pi, sin, sinh, sqrt
from itertools import product
from scipy.integrate import quad
from scipy.special import i0e, i1e


def integral(mu, order, cosine=False):
    # Integrate inverse powers of the massive lattice symbol in log proper time.
    # The optional cosine replaces one of the four zero-order Bessel factors.
    def kernel(u):
        t = exp(u)
        a = i0e(2*t)
        b = i1e(2*t) if cosine else a
        return exp(order*u-mu*mu*t)*a**3*b/factorial(order-1)
    return quad(kernel, -45, log(70/mu**2), epsabs=1e-13, epsrel=2e-11)[0]


def shell(z, side):
    m = z/side
    mu = 2*sinh(m/2)
    zero = None
    levels = []
    for p in product(range(-2,3), repeat=3):
        h2 = [(2*sin(pi*q/side))**2 for q in p]
        energy = 2*asinh(sqrt(mu**2+sum(h2))/2)
        if p==(0,0,0):
            zero = energy
            assert h2[0]-h2[1] == 0 and sum(h2) == 0
        if abs(h2[0]-h2[1])>1e-15:
            levels.append(2*energy)
    assert abs(zero-m)<1e-14
    return min(levels)/m-2


if __name__=="__main__":
    z=8
    target=2*(sqrt(1+(2*pi/z)**2)-1)
    shifts=[shell(z,n) for n in (16,32,64,128,256,512,1024)]
    assert all(0<x<y for x,y in zip(shifts,shifts[1:]))
    assert abs(target-shifts[-1]) < 3e-5
    print("E+ levels minus 2m, in mass units:",shifts,"limit",target)
    for power in (3,6,9,12):
        mu=2.**(-power)
        m=2*asinh(mu/2)
        i2,i3,i4=(integral(mu,j) for j in (2,3,4))
        j1=((8+mu**2)*i3-i2)/3
        j2=(8/3)*integral(mu,3,cosine=True)
        assert abs(j1/j2-1)<2e-10
        xi2=j1/(8*i2)
        k_g2=-12*i4/(i2**2*xi2**2)
        k_ggap=-12*i4*(2*m)**4/i2**2
        print("mu",mu,"k*g_second/pi²",k_g2/pi**2,
              "k*g_gap/pi²",k_ggap/pi**2,
              "mu²*xi_second²*log(1/mu)",mu**2*xi2*log(1/mu))
    assert abs(k_g2/pi**2+1152)<.02
