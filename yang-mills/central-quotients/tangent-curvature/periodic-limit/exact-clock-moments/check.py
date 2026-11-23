"""Test exact interpolation and positive measures on a known spectral reference."""
from fractions import Fraction
from math import prod
import mpmath as mp


def rational_check():
    # Degree three on [0, 3/4]. Both positive parts and the external atom
    # share moments to degree three. The next moment separates them.
    c, b = Fraction(3, 4), Fraction(7, 8)
    nodes = [0, c/4, 3*c/4, c]
    weights = [prod((b-y)/(x-y) for y in nodes if y != x) for x in nodes]
    assert all(sum(w*x**j for x, w in zip(nodes, weights)) == b**j for j in range(4))
    assert sum(w*x**4 for x, w in zip(nodes, weights)) != b**4
    z = 2*b/c - 1
    assert sum(map(abs, weights)) == 4*z**3 - 3*z
    print("Exact degree-three variation:", sum(map(abs, weights)))


def clock_trial(J):
    m = 1/(2*(mp.mpf(J)+mp.mpf("1.25")))
    a = m**(mp.mpf(7)/64)
    c, b = mp.exp(-a), mp.exp(-2*m)
    h = (J-1)//2
    degree = int(J*mp.sqrt(a)/16)
    assert degree >= 1 and int(1/(2*m))-1 == J
    nodes = [c*(1+mp.cos(mp.pi*i/degree))/2 for i in range(degree+1)]
    # Barycentric cardinal coefficients evaluated at the external point b.
    raw = [(-1)**i/((2 if i in (0, degree) else 1)*(b-x)) for i,x in enumerate(nodes)]
    weights = [v/mp.fsum(raw) for v in raw]
    variation = mp.fsum(abs(w) for w in weights)
    assert mp.almosteq(variation, mp.chebyt(degree, 2*b/c-1), rel_eps=mp.mpf("1e-80"))
    for j in range(degree+1):
        assert abs(mp.fsum(w*x**j for w,x in zip(weights,nodes))-b**j) < mp.mpf("1e-80")

    A = a**8
    lo = A*mp.exp(-2*a*J)
    hi = A*mp.exp(-a*J/3)
    def moment(j, positive):
        # Reference energy has Gamma(8,1) law. Integrate its tail above a.
        t = a*(1+j)
        retained = mp.exp(-t)*mp.fsum(t**n/mp.factorial(n) for n in range(8))/(1+j)**8
        compensator = mp.fsum(max(0,-w if positive else w)*x**j for w,x in zip(weights,nodes))
        return retained + A*c**j + (hi if positive else lo)*b**j + (hi-lo)*compensator

    assert max(abs(moment(j,True)-moment(j,False)) for j in range(degree+1)) < mp.mpf("1e-80")
    plus = moment(h,True)/moment(J,True)
    minus = moment(h,False)/moment(J,False)
    assert minus >= mp.exp(a*(J-h))/(1+mp.exp(-a*J))*(1-mp.eps*10000)
    print(f"J={J} h={h} degree={degree} plus={float(plus):.9g} log(minus)={float(mp.log(minus)):.9g}")
    return plus, minus


if __name__ == "__main__":
    mp.mp.dps = 135
    rational_check()
    results = [clock_trial(J) for J in (63, 128, 511, 1024)]
    assert abs(results[-1][0]-mp.sqrt(mp.e)) < mp.mpf("0.01")
    assert results[-1][1] > mp.exp(200)
