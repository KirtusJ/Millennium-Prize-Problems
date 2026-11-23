"""Independent separated-time Maxwell controls, in units with one photon species."""
from itertools import product

import numpy as np
from scipy.integrate import quad
from scipy.special import roots_legendre


def exact(q, t):
    return np.exp(-t*q)*np.array([q**4/(120*np.pi**2*t),
        (24/t**5+24*q/t**4+8*q*q/t**3)/(64*np.pi**2)])


def interval(n, a, b):
    x, w = roots_legendre(n)
    return (a+b+(b-a)*x)/2, (b-a)*w/2


def pair_integral(q, t, n):
    # Integrate physical radius and polar angle in the original photon modes.
    # Compute both matrix elements on oriented transverse polarization bases.
    mu, wm = interval(n, -1, 1)
    sin = np.sqrt(1-mu**2)
    radii = [interval(n, 0, q), interval(n, q, 42/t+q)]
    total = np.zeros(3)
    for rr, wr in radii:
        for r, weight in zip(rr, wr):
            k = np.stack([sin, 0*mu, mu], axis=-1)
            ell = np.array([0., 0., q])-r*k
            s = np.linalg.norm(ell, axis=-1)
            ell /= s[:, None]
            normal = np.broadcast_to([0., 1., 0.], k.shape)
            # B implements the transverse quarter turn n × epsilon.
            basis_k = [normal, np.cross(k, normal)]
            basis_l = [normal, np.cross(ell, normal)]
            weights = r*r*weight*wm*np.exp(-t*(r+s))*r*s/(32*np.pi**2)
            for e, f in product(basis_k, basis_l):
                electric = (e*f).sum(axis=1)
                magnetic = (np.cross(k, e)*np.cross(ell, f)).sum(axis=1)
                T, U = electric+magnetic, electric-magnetic
                total += np.array([weights @ (T*T), weights @ (U*U), weights @ (T*U)])
    return total


def spatial_transform(q, t):
    # Separated-point C_T = 4/pi^4 for a single Maxwell field in four dimensions.
    def radial(r):
        R2 = r*r+t*t
        return r*((1-2*t*t/R2)**2-1/4)/R2**4
    value = quad(radial, 0, np.inf, weight='sin', wvar=q, epsabs=1e-12)[0]
    return 16*value/(q*np.pi**3)


def lattice_integrals(b, p, t, n):
    # t=0: full Brillouin zone in theta=b*k; output includes powers b and b^5.
    # t>0: quadrature in physical k. The discarded tails are exponentially small.
    limit = np.pi if t == 0 else min(np.pi/b, 42/t)
    abscissa, half_weights = interval(n, 0, limit)
    v = np.r_[-abscissa[::-1], abscissa]
    weights = np.r_[half_weights[::-1], half_weights]
    coords = np.meshgrid(v, v, v, indexing='ij', sparse=True)
    theta = coords if t == 0 else [b*x for x in coords]
    k = [2*np.sin(x/2) for x in theta]
    ell = [2*np.sin((b*pi-x)/2) for pi, x in zip(p, theta)]
    r, s = (np.sqrt(sum(x*x for x in vec)) for vec in (k, ell))
    plus = sum((u/r+v/s)**2 for u, v in zip(k, ell))/2
    minus = sum((u/r-v/s)**2 for u, v in zip(k, ell))/2
    factor = r*s/4
    def integrate(arr):
        return np.einsum('i,j,k,ijk', weights, weights, weights, arr, optimize=True)/(2*np.pi)**3
    if t:
        factor = factor*np.exp(-t*(r+s)/b)/b**2
        return np.array([integrate(factor*plus**2), integrate(factor*minus**2)])
    derivative = [pi*np.cos(x/2) for pi, x in zip(p, theta)]
    proj2 = sum(v*v for v in derivative)-sum(u*v for u, v in zip(k, derivative))**2/r**2
    limit_total = integrate(proj2**2/(16*r**2))
    return np.array([integrate(factor*plus**2)/b**4, integrate(factor*minus**2), limit_total])


def main():
    for q, t in [(1., 1.), (2., .7), (.8, 1.4)]:
        direct = pair_integral(q, t, 120)
        target = exact(q, t)
        position = spatial_transform(q, t)
        assert np.max(abs(direct[:2]/target-1)) < 2e-5 and abs(direct[2]) < 1e-12
        assert abs(position/target[0]-1) < 2e-8
        print("photons", q, t, *direct, "position-space", position)
    p = np.array([.4, -.6, 1.2])
    q, t = np.linalg.norm(p), 1.
    for b in [.4, .2, .1, .05]:
        reading = lattice_integrals(b, p, t, 40)
        relative = reading/exact(q, t)-1
        print("positive time", b, *reading, "relative errors", *relative)
    assert np.max(abs(relative)) < .006
    for b in [.2, .1, .05, .025]:
        scaled_T, scaled_U, predicted = lattice_integrals(b, p, 0., 56)
        print("sharp time", b, scaled_T, scaled_U, "predicted", predicted, 6.)
    assert abs(scaled_T/predicted-1) < .02 and abs(scaled_U/6-1) < .001
    # Detect a scalar admixture from two clocks at nonzero spatial momentum.
    A, B = 1.7**2, .3**2
    def clock(t):
        T, U = exact(q, t)*t*np.exp(q*t)
        return A*T+B*U, U
    (v, g), (w, h) = clock(.7), clock(1.3)
    recovered = np.array([(g*w-h*v)/(g-h)*120*np.pi**2/q**4, (v-w)/(g-h)])
    assert np.allclose(recovered, [A, B], atol=1e-13, rtol=1e-13)
    print("recovered squared amplitudes", *recovered)


if __name__ == '__main__':
    main()
