"""Compute fourth norms by Fourier inversion of the exact tilted clock transform."""
import numpy as np
from scipy.fft import rfft, irfft, rfftfreq
from scipy.integrate import quad
from scipy.special import ive, roots_legendre


def norm_ratio(n, step):
    # Fourier convention exp(-i omega r). Big periodic box, centered grid.
    count = 2**int(np.ceil(np.log2((4*n+360)/step)))
    r = (np.arange(count)-count//2)*step
    freq = 2*np.pi*rfftfreq(count, step)
    z = 3+4j*freq
    q = 2/(2+z+np.sqrt(z)*np.sqrt(4+z))
    q3 = 2/(5+np.sqrt(21))
    g = np.exp(np.log(2)-.75*r-np.logaddexp(r,-r))
    conv = irfft(rfft(g)*(q/q3)**n,n=count)
    weight = 8*np.exp(-3*np.logaddexp(0,-2*r))
    return n**1.5*step*np.dot(weight,conv**4)/(2*np.pi)


def direct_norm(n):
    # Integrate against the original Bessel hitting density and the exact Haar law.
    nodes, weights = roots_legendre(500)
    u = (nodes+1)*24
    du = weights*24
    r = nodes*32
    dr = weights*32
    def sech(x):
        return np.exp(np.log(2)-np.logaddexp(x,-x))
    response = sech(r[:,None]-4*u[None,:]) @ (du*n*ive(n,2*u)/u)
    norm = np.sum(dr*sech(r)**3*response**4)/(2*np.pi)
    q3 = 2/(5+np.sqrt(21))
    return n**1.5*norm/q3**(4*n)


if __name__ == "__main__":
    sigma2 = 80/21**1.5
    integral = quad(lambda r: np.exp(np.log(2)-.75*r-np.logaddexp(r,-r)),
                    -np.inf,np.inf)[0]
    assert abs(integral - np.pi/np.cos(3*np.pi/8))<1e-9
    limit = (4/np.pi)*integral**4*np.sqrt(np.pi*sigma2/2)/(2*np.pi*sigma2)**2
    for n in (1,2,4):
        direct = direct_norm(n)
        transformed = norm_ratio(n,.0625)
        assert abs(direct/transformed-1)<2e-8
        print(f"n={n}: direct Haar and Fourier norms agree to {abs(direct/transformed-1):.2g} relative")
    for n in (8,32,128,512,2048):
        coarse,fine = norm_ratio(n,.125),norm_ratio(n,.0625)
        assert abs(coarse/fine-1)<1e-8
        print(f"n={n}: scaled fourth norm {fine:.8f}, asymptotic ratio {fine/limit:.8f}")
    assert abs(fine/limit-1)<.05
