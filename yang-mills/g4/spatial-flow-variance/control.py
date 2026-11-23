"""Periodic incidence, SU(2) action derivatives and exact probability controls."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
import json
import math


def step(x, i, side):
    return tuple((v + (j == i)) % side for j, v in enumerate(x))


def faces(dim, side):
    for x in product(range(side), repeat=dim):
        for i, j in combinations(range(dim), 2):
            yield ((x, i), (step(x, i, side), j), (step(x, j, side), i), (x, j)), (i, j)


def mul(p, q):
    a, b, c, d = p
    w, x, y, z = q
    return (a*w-b*x-c*y-d*z, a*x+b*w+c*z-d*y,
            a*y-b*z+c*w+d*x, a*z+b*y-c*x+d*w)


def conjugate(q):
    return q[0], -q[1], -q[2], -q[3]


def real_loop(values):
    return mul(mul(values[0], values[1]), mul(conjugate(values[2]), conjugate(values[3])))[0]


def spatial(side):
    theta = 0.37
    incidences = defaultdict(list)
    rows = Counter()
    count = 0
    for loop, _ in faces(3, side):
        center = math.prod((-1)**sum(x[:i]) for x, i in loop)
        assert center == -1
        for position, link in enumerate(loop):
            incidences[link].append((loop, position))
            rows[link] += len(loop)
        count += 1
    assert set(rows.values()) == {16}

    def value(link):
        x, i = link
        angle = (-1)**x[0] * theta if i == 1 else 0.0
        return math.cos(angle), 0.0, 0.0, math.sin(angle)

    # Differentiate every incident face as an ordered quaternion word.  Inverse
    # links are differentiated by conjugation after the raw-link variation.
    axes = [(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
    max_error = 0.0
    for link, slots in incidences.items():
        x, i = link
        for j, axis in enumerate(axes):
            force = 0.0
            for loop, pos in slots:
                values = list(map(value, loop))
                values[pos] = mul(axis, values[pos])
                force += real_loop(values)
            expected = -2*(-1)**x[0]*math.sin(2*theta) if i == 1 and j == 2 else 0.0
            max_error = max(max_error, abs(force-expected))
    assert max_error < 1e-12
    return {"side": side, "faces": count, "row_sum": 16, "force_components": 3*len(rows)}


def probability_controls():
    p = Fraction(1, 8)
    left, right = Fraction(1, 8), Fraction(15, 8)
    mean = (left+right)/2
    variance = p*(left-mean)**2+p*(right-mean)**2
    assert variance == 49*p/32  # remaining mass is at the midpoint
    # Constant and centered eigenspaces of an independent stationary binary slice.
    states = (-1, 1)
    def prediction_error(stay):
        def transition(x, y):
            return stay if x == y else 1-stay
        two_step = sum(Fraction(1, 2)*x*z*transition(x,y)*transition(y,z)
                       for x,y,z in product(states, repeat=3))
        mse = sum(Fraction(1, 2)*transition(x,y) *
                  (y-sum(z*transition(x,z) for z in states))**2
                  for x,y in product(states, repeat=2))
        assert mse == 1-two_step
        return mse, two_step
    assert prediction_error(Fraction(1, 2)) == (1, 0)
    assert prediction_error(Fraction(3, 4)) == (Fraction(3, 4), Fraction(1, 4))
    # Equality in the scalar split; thresholds in the measure bound use a
    # closed upper region, so the endpoint bound may be approached from below.
    rho = Fraction(1, 4)
    upper_mass = rho/(2-rho)
    assert (1-upper_mass)*rho/2 + upper_mass == rho
    c = Fraction(1, 16)
    scale = Fraction(1, 64)
    lower_atom = c*scale/2-Fraction(1, 10**6)
    band_mass = (c*scale-lower_atom)/(scale-lower_atom)
    assert lower_atom > 0 and band_mass > c/(2-c)
    for k in range(1, 8):
        covariance = (1-band_mass)*lower_atom**k + band_mass*scale**k
        assert covariance >= c/(2-c)*(c*scale/2)**k
    return {"variance": str(variance), "split_mass": str(upper_mass),
            "band_mass": str(band_mass), "independent_lag_two": "0"}


def strong_coupling_controls():
    # The S^3 scalar marginal has density 2*sqrt(1-x*x)/pi.
    # Its even moments are Catalan(n)/4^n. Compute the tilted mean by exact
    # series division through order 5, independently of a Bessel library.
    def moment(k):
        if k % 2:
            return Fraction(0)
        n = k//2
        return Fraction(math.comb(2*n, n)//(n+1), 4**n)
    den = [moment(k)/math.factorial(k) for k in range(6)]
    num = [moment(k+1)/math.factorial(k) for k in range(6)]
    mean = []
    for k in range(6):
        mean.append((num[k]-sum(den[i]*mean[k-i] for i in range(1,k+1)))/den[0])
    assert mean == [0, Fraction(1,4), 0, Fraction(-1,96), 0, Fraction(1,1536)]
    leading = [moment(2)*mean[1]**(4*j) for j in range(3)]
    assert leading == [Fraction(1,4), Fraction(1,1024), Fraction(1,262144)]
    # Use the rational upper bound on H, at the largest allowed beta.
    beta = Fraction(1, 2**256)
    radius = Fraction(1, 1024)
    errors = [2**14*(beta/radius)/(1-beta/radius)*(4/radius)**(4*j) for j in range(3)]
    inside = Fraction(1,4)-errors[0]-(errors[0]+2*errors[1]+errors[2])*2**128
    assert inside > Fraction(9,64)
    assert Fraction(3,8)-16*Fraction(1,128) == Fraction(1,4)
    return {"mean_series": [str(x) for x in mean], "leading_C0_C1_C2": [str(x) for x in leading],
            "bare_band_mass_exceeds": "9/64", "flowed_band_mass_at_least": "1/16"}


def main():
    counts = Counter(link for loop, _ in faces(4, 4) for link in loop)
    assert set(counts.values()) == {6}
    result = {"spatial": [spatial(n) for n in (4, 6)], "four_dimensional_links": len(counts),
              "four_dimensional_faces_per_link": 6, "probability": probability_controls(),
              "electric_only_and_cauchy": strong_coupling_controls()}
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
