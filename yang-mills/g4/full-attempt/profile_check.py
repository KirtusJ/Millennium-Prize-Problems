"""Exact finite gauge projection and a binomial check on the limiting TV formula."""
from fractions import Fraction
from itertools import product
from math import erf, fsum, prod, sqrt
import json


def perimeter_test(lag):
    # The first two squares share link 0. The third square is disjoint.
    faces = ((0,1,2,3), (0,4,5,6), (7,8,9,10))
    u = Fraction(1, 2)**lag
    relative = {s: Fraction(0) for s in product((-1,1), repeat=3)}
    for links in product((-1,1), repeat=11):
        signs = tuple(prod(links[i] for i in face) for face in faces)
        relative[signs] += prod((1+u*x)/2 for x in links)
    assert sum(relative.values()) == 1
    t = u**4
    residual = Fraction(0)
    for (x,y,z), probability in relative.items():
        likelihood = 8*probability  # product-Haar orbit differences are uniform on three signs
        projected = (1+t*x+t*y)*(1+t*z)
        omitted = u**6*x*y*(1+t*z)
        assert likelihood-projected == omitted
        residual += omitted**2/8
    assert residual == u**12*(1+t*t)
    return str(residual)


def binomial(count, probability):
    # Start at a mode to avoid underflow in the tails of the recurrence.
    mode = int((count+1)*probability)
    weights = [0.0]*(count+1)
    weights[mode] = 1.0
    for k in range(mode, count):
        weights[k+1] = weights[k]*(count-k)/(k+1)*probability/(1-probability)
    for k in range(mode, 0, -1):
        weights[k-1] = weights[k]*k/(count-k+1)*(1-probability)/probability
    total = fsum(weights)
    return [p/total for p in weights]


def binomial_profile(theta):
    target = erf(sqrt(3*theta)/(2*sqrt(2)))
    samples = []
    for volume in (64, 256, 1024, 4096):
        t = sqrt(theta/volume)
        joint = binomial(3*volume, (1+t)/2)
        independent = binomial(3*volume, 0.5)
        tv = fsum(abs(x-y) for x,y in zip(joint, independent))/2
        samples.append(round(tv, 8))
    assert abs(samples[-1]-target) < 0.0002
    return {"theta":theta, "product_controls":samples, "limit":round(target,8)}


if __name__ == "__main__":
    print(json.dumps({"perimeter_squared_norms":[perimeter_test(n) for n in (1,2,4)],
                      "profile_controls":[binomial_profile(x) for x in (0.25,1,3)]}, indent=2))
