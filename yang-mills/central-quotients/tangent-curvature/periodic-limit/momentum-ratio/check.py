"""Derive the exact CDF, then check it against independent two-leg samples."""
import numpy as np
import sympy as sp


def derive():
    x, u, v = sp.symbols("x u v")
    marginal = sp.Rational(63, 4)*x**6*(1-x**2)
    moments = [sp.integrate(marginal*sp.legendre(l, x), (x, -1, 1)) for l in range(9)]
    density_z = sp.Poly(sum((2*l+1)*a**2*sp.legendre(l, 1-2*u)
                            for l, a in enumerate(moments)), u)
    beta = sp.Rational(2**20, 10*sp.binomial(20, 10))
    q = sum(density_z.nth(i)*u**i * 2/beta *
            sum(sp.binomial(8-i, j)*(-1)**j*(1-u)**j/(2*j+1) for j in range(9-i))
            for i in range(9))
    cdf = sp.Poly(sp.integrate((2*v**2*q.subs(u, 1-v**2)).expand(), v), v)
    assert cdf.eval(0) == 0 and cdf.eval(1) == 1 and cdf.degree() == 19
    assert cdf.nth(3) == sp.Rational(92169, 16384)
    assert cdf.diff().eval(1) == sp.Rational(5586, 1105)
    assert sp.integrate((1-v**2)*cdf.diff().as_expr(), (v, 0, 1)) == sp.Rational(10, 21)
    assert sp.integrate((1-v**2)**2*cdf.diff().as_expr(), (v,0,1)) == sp.Rational(1780,5313)
    print("polar moments", moments)
    print("CDF", sp.factor(cdf.as_expr()))
    print("P(V<=1/2)", cdf.eval(sp.Rational(1, 2)))
    return sp.lambdify(v, cdf.as_expr(), "numpy")


def draw_leg(rng, size, isotropic=False):
    if isotropic:
        x = rng.uniform(-1., 1., size)
    else:
        x = np.sqrt(rng.beta(3.5, 2, size))*rng.choice([-1, 1], size)
    phi = rng.uniform(0., 2*np.pi, size)
    radius = np.sqrt(1-x*x)
    direction = np.column_stack((radius*np.cos(phi), radius*np.sin(phi), x))
    return rng.gamma(10, size=size), direction


def simulate(cdf):
    rng = np.random.default_rng(113847)
    a, alpha = draw_leg(rng, 250_000)
    b, beta = draw_leg(rng, len(a))
    total = a+b
    v = np.linalg.norm(a[:, None]*alpha+b[:, None]*beta, axis=1)/total
    bounds = np.arange(1, 20)/20
    for name, sample in (("all", v), ("energy 12..18", v[(total>=12)&(total<=18)]),
                         ("energy 22..30", v[(total>=22)&(total<=30)])):
        errors = np.abs(np.searchsorted(np.sort(sample), bounds)/len(sample)-cdf(bounds))
        print(name, "samples", len(sample), "maximum grid CDF error", round(max(errors), 6))
        assert max(errors) < .009
    # An isotropic surrogate has the same gamma energy but a different angular law.
    _, iso_a = draw_leg(rng, len(a), True)
    _, iso_b = draw_leg(rng, len(a), True)
    iso_v = np.linalg.norm(a[:, None]*iso_a+b[:, None]*iso_b, axis=1)/total
    measured = np.mean(iso_v <= .5)
    print("isotropic replacement at 1/2", round(measured, 6))
    assert abs(measured-cdf(.5)) > .04
    # Tying the directions makes V=1 regardless of either energy.
    assert np.max(abs(np.linalg.norm(a[:,None]*alpha+b[:,None]*alpha,axis=1)/total-1)) < 1e-12


if __name__ == "__main__":
    simulate(derive())
