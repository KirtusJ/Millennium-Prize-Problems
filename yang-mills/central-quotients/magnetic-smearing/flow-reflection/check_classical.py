"""Reduced nonlinear SU(2) Wilson flow, compared with a periodic continuum heat solution."""
import math
import numpy as np


def bump(t):
    z = -np.sin(t)-0.125
    f = np.zeros_like(t)
    f[z > 0] = np.exp(-1/z[z > 0])
    return f


def continuum(s):
    n = 8192
    t = np.arange(n)*2*math.pi/n
    k = np.fft.fftfreq(n, 1/n)
    coefficients = np.fft.fft(bump(t))/n
    value = np.sum(coefficients*np.exp(-s*k*k + 1j*k*math.pi/4))
    assert abs(value.imag) < 1e-12
    return 0.5*(math.exp(-s)*value.real)**2


def lattice(n, s, step_factor):
    a = 2*math.pi/n
    x = a*np.arange(n)
    F = bump(x)[:, None]*np.sin(x)[None, :]
    assert np.max(np.abs(F[:n//2+1])) == 0

    def velocity(f):
        forward_t = np.sin(a*(np.roll(f,-1,axis=0)-f))
        forward_x = np.sin(a*(np.roll(f,-1,axis=1)-f))
        return (forward_t-np.roll(forward_t,1,axis=0)
                + forward_x-np.roll(forward_x,1,axis=1))/a**3

    steps = math.ceil(s/(step_factor*a*a))
    dt = s/steps
    for _ in range(steps):
        k1 = velocity(F)
        k2 = velocity(F+dt*k1/2)
        k3 = velocity(F+dt*k2/2)
        k4 = velocity(F+dt*k3)
        F += dt*(k1+2*k2+2*k3+k4)/6
    phase = a*(F[n//8,0]-F[n//8,1])
    return 2*(math.sin(phase/2)/a**2)**2


if __name__ == "__main__":
    s = 0.5
    target = continuum(s)
    assert target > 0
    print(f"Continuum positive-side magnetic deficit/a^4: {target:.12g}")
    errors = []
    for n in (16,32,64,96):
        value = lattice(n, s, 0.22)
        fine = lattice(n, s, 0.11)
        error = abs(fine-target)
        errors.append(error)
        print(f"N={n}, fine={fine:.12g}, abs error={error:.4g}, step-halving difference={abs(fine-value):.3g}")
        assert fine > 0 and abs(fine-value) < 0.002*error
    assert all(a>b for a,b in zip(errors,errors[1:]))
    assert errors[-1] < 0.02*target
