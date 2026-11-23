"""Exact switch-point bound and independent radial quadrature of sampling costs."""
from fractions import Fraction as F
from math import expm1, factorial, log1p

import numpy as np
from scipy.special import ive, roots_chebyu


def term(j,k):
    return F(3,2)**(2*k+j)/(factorial(k)*factorial(k+j))


def check():
    lower = sum(term(2,k) for k in range(3))
    upper = sum(term(1,k) for k in range(3)) + term(1,3)/(1-F(9,80))
    assert lower > 2 and upper < 4
    z,w = roots_chebyu(512)
    for gamma in (0.001,0.3,1.,2.999,3.,3.001,10.,100.,500.):
        prob = w*np.exp(gamma*(z-1))
        prob /= prob.sum()
        u = ive(2,gamma)/ive(1,gamma)
        reading = gamma*(1-z*z)/3 if gamma <= 3 else z*np.tanh(gamma*z)
        assert abs(prob@reading/u-1)<3e-12
        relative = (prob@(reading**2))/u**2-1
        assert 0 <= relative < 1
        # 8n factors with two observations per factor per unit of exponent.
        power = 80
        cv2 = expm1(power*log1p(relative/(2*power)))
        assert cv2 < np.exp(0.5)-1
        print(f"gamma={gamma:7g} relative variance per draw={relative:.8f} product={cv2:.8f}")


def sample(gamma, size, rng):
    chunks = []
    remaining = size
    while remaining:
        if gamma <= 3:
            z = 2*rng.beta(1.5,1.5,remaining)-1
            keep = rng.random(remaining) < np.exp(gamma*(z-1))
            readings = gamma*(1-z[keep]**2)/3
        else:
            y = rng.gamma(1.5,1.,remaining)
            keep = rng.random(remaining) < np.sqrt(np.maximum(0,1-y/(2*gamma)))
            z = 1-y[keep]/gamma
            readings = z*np.tanh(gamma*z)
        chunks.append(readings)
        remaining -= len(readings)
    return np.concatenate(chunks)


def sample_check():
    rng = np.random.default_rng(20261123)
    power,replications = 16,1000
    for gamma in (0.1,3.,30.):
        u = ive(2,gamma)/ive(1,gamma)
        draws = sample(gamma,replications*power*2*power,rng)
        blocks = draws.reshape(replications,power,2*power).mean(axis=2)
        normalized = (blocks/u).prod(axis=1)
        se = normalized.std(ddof=1)/np.sqrt(replications)
        assert abs(normalized.mean()-1)<6*se
        print(f"gamma={gamma:g} sampled power ratio={normalized.mean():.6f} SE={se:.6f}")


if __name__ == "__main__":
    check()
    sample_check()
