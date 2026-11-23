"""Independent quadrature and counterexamples for three-time energy readings."""
from math import cos, e, exp, expm1, log, log1p, pi, sin

from scipy.integrate import quad
from scipy.special import gamma

K = 3*log(3)-4*log(2)


def detector(u):
    return exp(-u)*expm1(-u)**2


def log_time_integral(reading, freq=0., lo=-40., hi=40.):
    def integrate(trig):
        def f(y):
            t = exp(y)
            return reading(t)*trig(freq*y)/t
        return quad(f, lo, hi, epsabs=2e-13, epsrel=2e-13, limit=500)[0]
    return integrate(cos)-1j*integrate(sin)


def multiplier(xi):
    if xi == 0:
        return K
    z = 1j*xi
    return gamma(1-z)*(3**(1+z)-2*2**(1+z)+1)/(z*(1+z))


def compare_transform(reading, characteristic):
    errors = []
    for xi in (0., 0.25, 1., 3., 6.):
        observed = log_time_integral(reading, xi)
        factor = multiplier(xi)
        recovered = observed/factor
        errors.append(abs(recovered-characteristic(xi)))
        assert abs(observed-factor*characteristic(xi)) < 5e-11
    assert max(errors) < 1e-8
    return max(errors)


def quadrature_grid(reading, lo, hi, steps):
    h = (hi-lo)/steps
    return h*sum(reading(exp(lo+j*h))/exp(lo+j*h) for j in range(steps))


def main():
    # Entries are energy and FIRST-moment weight, not raw spectral mass.
    atoms = [(0.125, .2), (2., .55), (40., .25)]
    mixed = lambda t: sum(w*detector(t*energy)/energy for energy, w in atoms)
    mixed_char = lambda xi: sum(w*energy**(1j*xi) for energy, w in atoms)
    err_atomic = compare_transform(mixed, mixed_char)

    # The raw measure exp(-E) dE/E has infinite total mass. Pairing the
    # three exponentials makes its detector finite, with this closed form.
    infrared = lambda t: log1p(t*t/((1+t)*(1+3*t)))
    err_infinite = compare_transform(infrared, lambda xi: gamma(1+1j*xi))
    print(f"constant {K:.12f}, maximum characteristic errors {err_atomic:.2g}, {err_infinite:.2g}")

    lo, hi = -5., 3.
    window = log_time_integral(mixed, lo=lo, hi=hi).real/K
    for count in (32, 128, 512):
        estimate = quadrature_grid(mixed, lo, hi, count)/K
        bound = 2*(hi-lo)/(e*count)
        assert abs(estimate-window) <= bound
        print(f"grid {count}: retained {window:.9f}, estimate {estimate:.9f}, margin {bound:.9f}")

    for n in (32, 1024, 32768):
        def escaping(t):
            return .3*detector(t/n)*n + .5*detector(t) + .2*detector(t*n)/n
        # Use a moving intermediate threshold to separate scales.
        edge = log(n)/2
        early = log_time_integral(escaping, lo=-45., hi=-edge).real/K
        late = log_time_integral(escaping, lo=edge, hi=45.).real/K
        middle = log_time_integral(escaping, lo=-edge, hi=edge).real/K
        assert abs(early+middle+late-1) < 1e-11
        print(f"escape {n}: early {early:.6f}, middle {middle:.6f}, late {late:.6f}")
    assert abs(early-.2) < .006 and abs(late-.3) < .006

    # Two norm-one log-energy densities at TV distance 1/pi. Their
    # normalized readings approach each other even on their common band.
    for n in (4, 16, 64):
        def difference(t):
            return quad(lambda x: detector(t*exp(x))/(t*exp(x)),
                        0, 2*pi, weight='cos', wvar=n, epsabs=1e-12)[0]/(2*pi)
        largest = max(abs(difference(exp(j/8))) for j in range(-96, 65))
        assert largest <= K/(pi*e*n)
        print(f"frequency {n}: sampled max {largest:.7g}, bound {K/(pi*e*n):.7g}")


if __name__ == '__main__':
    main()
