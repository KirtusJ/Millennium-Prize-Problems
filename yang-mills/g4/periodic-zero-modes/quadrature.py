"""Deterministic importance quadrature of the finite-coupling compact one-site integral."""
import json
from math import exp, pi, prod, sqrt
from statistics import NormalDist


BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
NORMAL = NormalDist()


def radical_inverse(index, base):
    value = 0.0
    place = 1.0 / base
    while index:
        index, digit = divmod(index, base)
        value += digit * place
        place /= base
    return value


def integrate(samples=65536):
    # The pivot is direction 0. Symmetry includes all four choices analytically.
    betas = (1e8, 1e32)
    sums = [[0.0, 0.0, 0.0] for _ in betas]
    for index in range(1, samples + 1):
        point = [radical_inverse(index, base) for base in BASES]
        alpha = 0.25 + 0.5 * point[0]
        t = [2*u - 1 for u in point[1:4]]
        y = [(NORMAL.inv_cdf(point[4 + 2*j])/2, NORMAL.inv_cdf(point[5 + 2*j])/2)
             for j in range(3)]
        lengths = [x*x + z*z for x,z in y]
        pivot_energy = 2 * sum(lengths)
        quadratic = 0.0
        quartic = 0.0
        for i,j in ((0,1), (0,2), (1,2)):
            quadratic += sum((t[i]*y[j][k] - t[j]*y[i][k])**2 for k in (0,1))
            quartic += (y[i][0]*y[j][1] - y[i][1]*y[j][0])**2
        for beta, accum in zip(betas, sums):
            r2 = beta ** (-alpha/2)
            q = beta ** (1-alpha)
            squared = [t[j]**2 + lengths[j]/q for j in range(3)]
            if any(x > 1 for x in squared):
                continue
            haar = 1/sqrt((1-r2) * prod(1-r2*x for x in squared))
            extra = 2 * (quadratic + quartic/q)
            energy = pivot_energy + extra
            # Each proposed transverse coordinate is N(0,1/4).
            weight = haar * exp(-extra)
            accum[0] += weight
            accum[1] += weight * energy
            accum[2] += weight * exp(-energy)
    results = []
    for beta, (weight, energy, tilt) in zip(betas, sums):
        # Coefficient per unit alpha length in [1/4,3/4].
        coefficient = 4/pi**4 * weight / samples
        results.append({"beta": beta, "coefficient": round(coefficient, 6),
                        "mean_scaled_action": round(energy/weight, 4),
                        "unit_laplace_transform": round(tilt/weight, 5)})
    return {"samples": samples, "shell": [0.25, 0.75], "estimates": results}


if __name__ == "__main__":
    print(json.dumps(integrate(), indent=2))
