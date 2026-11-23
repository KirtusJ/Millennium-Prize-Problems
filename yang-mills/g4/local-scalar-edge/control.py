"""Independent controls for curvature, Fourier normalization, and finite-size scaling."""
import cmath
from fractions import Fraction
from itertools import product
import json
import math

D = Fraction(7, 768)


def top_orientation(k):
    """Power iteration on a shifted real symmetric orientation matrix near zero."""
    cosines = [math.cos(x/2) for x in k]
    diagonal = 50/3 - sum(4*math.sin(x/2)**2 for x in k)
    matrix = [[diagonal+64 if i == h else 8*cosines[i]*cosines[h]
               for h in range(3)] for i in range(3)]
    v = [1/math.sqrt(3)]*3
    for _ in range(100):
        image = [sum(a*b for a, b in zip(row, v)) for row in matrix]
        norm = math.sqrt(sum(a*a for a in image))
        v = [a/norm for a in image]
    return sum(v[i]*matrix[i][h]*v[h] for i in range(3) for h in range(3))-64


def curvature():
    ratios = []
    for direction in [(1, 0, 0), (1, 1, 0), (1, -1, 2)]:
        k = [n/256 for n in direction]
        ratio = (98/3-top_orientation(k))/(256*sum(x*x for x in k))
        assert abs(ratio-float(D)) < 2e-7
        ratios.append(round(ratio, 9))
    return ratios


def fourier_inversion():
    # Synthetic positive covariances on an eight-site ring, including conjugation.
    length = 8
    v = [1+2j, 0, 0.5j, -0.25, 0, -1j, 0, 0]
    coeff = [sum(z*cmath.exp(2j*math.pi*k*y/length) for y,z in enumerate(v))
             /math.sqrt(length) for k in range(length)]
    spectral = [abs(z)**2 for z in coeff]
    assert abs(sum(spectral)-sum(abs(z)**2 for z in v)) < 1e-12
    for h in range(length):
        direct = sum(v[y].conjugate()*v[(y+h) % length] for y in range(length))/length
        inverse = sum(w*cmath.exp(-2j*math.pi*k*h/length)
                      for k,w in enumerate(spectral))/length
        assert abs(direct-inverse) < 1e-12
    # Omitting the local measure's volume divisor gives a false zero-lag result.
    assert abs(sum(spectral)-sum(abs(z)**2 for z in v)/length) > 1
    return length


def ball_counts():
    cases = 0
    for side in (8, 16, 28):
        norms = [sum(i*i for i in n) for n in product(range(-side//2, side//2), repeat=3)]
        for radius in (0.01, 0.1, 0.3, 0.7, 1.2):
            s = side*radius/(2*math.pi)
            count = sum(n <= s*s for n in norms)
            assert (1+2*math.floor(s/math.sqrt(3)))**3 <= count <= (1+2*math.floor(s))**3
            cases += 1
    return cases


def heat_sum(side, a):
    # Model with the same quadratic curvature and periodic lattice momenta.
    terms = [math.exp(-float(D)*a*4*math.sin(math.pi*n/side)**2)
             for n in range(-side//2, side//2)]
    return math.fsum(terms)**3


def crossover():
    bulk = (4*math.pi*float(D))**(-1.5)
    ell = 0.25
    theta = math.fsum(math.exp(-4*math.pi**2*float(D)*n*n/ell**2)
                      for n in range(-50, 51))**3
    errors = []
    for a in (4096, 16384, 65536):
        length = math.isqrt(a)
        bulk_reading = heat_sum(8*length, a)*a**1.5/(8*length)**3
        finite_reading = heat_sum(length//4, a)
        errors.append([abs(bulk_reading/bulk-1), abs(finite_reading/theta-1)])
    assert all(errors[i+1][k] < 0.27*errors[i][k] for i in range(2) for k in (0, 1))
    assert max(errors[-1]) < 0.0004
    assert abs(heat_sum(8, 65536)-1) < 1e-12
    # Two lags have the expected extra 3 log(2)/2 even before division by j.
    a = 65536
    lag_bias = math.log(heat_sum(2048, a)/heat_sum(2048, 2*a))
    assert abs(lag_bias-1.5*math.log(2)) < 0.001
    return {"bulk_constant": round(bulk, 8), "theta_at_quarter": round(theta, 8),
            "relative_errors": [[round(x, 8) for x in row] for row in errors],
            "doubled_lag_log_ratio": round(lag_bias, 8)}


if __name__ == "__main__":
    print(json.dumps({"directional_curvatures": curvature(), "fourier_sites": fourier_inversion(),
                      "ball_counts": ball_counts(), "synthetic_heat_kernel": crossover()},
                     indent=2))
