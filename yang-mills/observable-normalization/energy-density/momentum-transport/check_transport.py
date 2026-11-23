"""Positive-time transport, finite reading intervals, and stress-scalar recovery."""
import math

import numpy as np
from scipy.integrate import quad
from scipy.special import i1e


def move_continuous(read, t, a):
    if a == 0:
        return read(t)
    def integrand(x):
        z = np.sqrt(a*(x*x-t*t))
        scaled = i1e(z)/z if z else .5
        return read(x)*a*x*np.exp(z)*scaled
    # Finite endpoint avoids overflow of the individual exponential factors.
    return read(t)+quad(integrand, t, 220., epsabs=2e-13, epsrel=2e-12)[0]


def finite_readings(read, t, u, a, cells, order, end, rel_error):
    times = np.linspace(t, end, cells+1)
    samples = np.array([read(x) for x in times])
    lower, upper = samples*(1-rel_error), samples*(1+rel_error)
    if a == 0:
        return lower[0], upper[0]
    d = (times*times-t*t)/4
    term = np.ones_like(times)
    weights = np.zeros(cells)
    for n in range(1, order+1):
        term *= a*d/n**2
        weights += np.diff(term)
    r = (u+a)/2
    p, m = np.sqrt(u), np.sqrt(u-r)
    series_tail = (a/r)**(order+1)*p/m*np.exp(t*(p-m))*upper[0]
    gap = p-np.sqrt(a)
    time_tail = a*upper[0]/2*np.exp(t*p-end*gap)*(end/gap+1/gap**2)
    return (lower[0]+weights @ lower[1:],
            upper[0]+weights @ upper[:-1]+series_tail+time_tail)


def recover(values, u, h):
    y0, y1, y2 = values
    A = (y2-2*y1+y0)/(2*h*h)
    X = (y1-y0-(2*u*h+h*h)*A)/(2*h)
    B = y0-u*u*A-2*u*X
    return np.array([A, X, B])


def shell(s, u, t):
    energy = np.sqrt(s+u)
    return np.exp(-t*energy)/(2*energy)


def main():
    u0, h, t = .9, .55, .8
    us = [u0+i*h for i in range(3)]
    s = np.array([0., .2, 1., 4., 11.])
    a = np.array([.3, 2., -.7, 0., .9])
    b = np.array([-.9, -.7, .2, 1.3, -.6])
    scalar_noise = np.array([.02, .4, 0., .5, .1])
    gram = np.array([a*a, a*b, b*b+scalar_noise])
    expected = gram @ shell(s, u0, t)
    values, raw = [], []
    for u in us:
        coeffs = (u*a+b)**2+scalar_noise
        def read(x):
            return coeffs @ shell(s, u, x)
        truth = coeffs @ shell(s, u0, t)
        moved = move_continuous(read, t, u-u0)
        assert abs(moved-truth) < 2e-12
        raw.append(read(t))
        values.append(moved)
        for cells in [300, 1200, 4800]:
            lo, hi = finite_readings(read, t, u, u-u0, cells, 80, 80., 1e-6)
            assert lo <= truth <= hi
            if cells == 4800:
                assert hi-lo < .013*truth
                print("squared momentum, shifted reading, finite interval", u, truth, lo, hi)
    recovered = recover(values, u0, h)
    assert np.max(abs(recovered-expected)) < 1e-11
    assert recovered[1] < 0 and recovered[1]**2 <= recovered[0]*recovered[2]
    assert np.max(abs(recover(raw, u0, h)-expected)) > .01
    print("tensor, cross, scalar", *recovered)
    print("uncorrected at the three momenta", *recover(raw, u0, h))
    # Continuum free Maxwell has a continuous invariant mass spectrum.
    def maxwell(u, x):
        q = np.sqrt(u)
        return np.exp(-x*q)*np.array([u*u/(120*np.pi**2*x),
            (24/x**5+24*q/x**4+8*u/x**3)/(64*np.pi**2)])
    amps = np.array([2., .09])
    moved = [move_continuous(lambda x: amps @ maxwell(u, x), t, u-u0) for u in us]
    value = recover(moved, u0, h)
    expected = maxwell(u0, t)*amps*np.array([1/u0**2, 1.])
    assert np.max(abs(value-[expected[0], 0., expected[1]])) < 3e-12
    print("Maxwell reconstruction", *value)
    # Shift entire smooth, finite-width packets before fitting their three coefficients.
    nodes, weights = np.polynomial.legendre.leggauss(64)
    v = 1.4+.5*nodes
    weights *= .5*np.exp(-2/(1-nodes**2))
    Y = np.zeros((3, 3))
    for m in range(3):
        for i in range(3):
            shift = i*h
            U = v[:, None]+shift
            coeffs = (U*a+b)**2+scalar_noise
            def packet(x):
                return (weights*v**m) @ np.sum(coeffs*shell(s, U, x), axis=1)
            Y[m, i] = move_continuous(packet, t, shift)
    Am = (Y[:, 2]-2*Y[:, 1]+Y[:, 0])/(2*h*h)
    Hm = (Y[:, 1]-Y[:, 0]-h*h*Am)/(2*h)
    packet_result = [Am[0], Hm[0]-Am[1], Y[0, 0]-2*Hm[1]+Am[2]]
    target = gram @ (weights @ shell(s, v[:, None], t))
    assert np.max(abs(packet_result-target)) < 2e-12
    print("finite-width packet", *packet_result)
    # Periodizing the packet gives zero spatial mean on staggered centers.
    # Here momenta step by 1/4 and the reciprocal cutoff exceeds every annulus.
    side = 24
    modes = np.fft.fftfreq(side)*side/4
    P = np.meshgrid(modes, modes, modes, indexing='ij', sparse=True)
    U = sum(p*p for p in P)
    residual = 0.
    for shift in (0., h, 2*h):
        nodes = (U-shift-1.4)/.5
        pick = abs(nodes)<1
        amplitude = np.zeros_like(U)
        amplitude[pick] = np.exp(-1/(1-nodes[pick]**2))/U[pick]**.25
        for offset in ([.5, 0, 0], [0, .5, .5]):
            phase = np.exp(1j*2*np.pi*4/side*sum(c*p for c, p in zip(offset, P)))
            values = np.fft.ifftn(phase*amplitude)
            residual = max(residual, abs(values.sum()), np.max(abs(values.imag)))
            assert np.max(abs(values)) > 1e-4
    assert residual < 1e-13
    print("staggered zero-mode residual", residual)
    # Neither individual field detects this massless shell at these times.
    # Their sum cancels a large heavy component and saturates the lower bound.
    masses = np.array([0., 9.])
    amplitudes = np.array([[1., 1.], [10., -10.]])
    def G(t):
        return amplitudes.T @ (shell(masses, u0, t)[:, None]*amplitudes)
    tau, threshold = .75, .8
    d = np.exp(-tau*np.sqrt(u0+threshold))
    z = np.exp(-tau*np.sqrt(u0))
    lower = (G(.5+tau)-d*G(.5))/(z-d)
    direction = np.array([1., 1.])/np.sqrt(2.)
    assert max(np.diag(lower)) < 0
    got = direction @ lower @ direction
    assert np.isclose(got, 2*shell(0., u0, .5))
    print("subthreshold weight detected by the cross term", got)
    # A polynomial perturbation vanishes at two momenta while both Grams stay positive.
    d = .1
    changed = np.array([[1+d, -d*(us[0]+us[1])/2],
                        [-d*(us[0]+us[1])/2, 1+d*us[0]*us[1]]])
    assert np.linalg.eigvalsh(changed)[0] > 0
    diffs = [np.array([u, 1.]) @ (changed-np.eye(2)) @ np.array([u, 1.]) for u in us]
    assert max(abs(x) for x in diffs[:2]) < 1e-14
    assert math.isclose(diffs[2], 2*d*h*h)
    print("two-momentum ambiguity at the third", diffs[2])


if __name__ == '__main__':
    main()
