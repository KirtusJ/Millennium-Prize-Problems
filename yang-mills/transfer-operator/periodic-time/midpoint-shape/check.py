"""Invert midpoint-subtracted thermal shapes on the measured even-period lattices."""
from fractions import Fraction
from pathlib import Path
import sys

import numpy as np
from sympy import Poly, Rational, symbols

YM = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(YM / "observable-normalization/thermal-transitions"))
from matched_rows import circular_means, seed_rows


def kernel(n, t, z):
    """Normalized single-frequency shape, including both continuous endpoints."""
    upper = sum(z**j for j in range(n-t))
    lower = sum(z**j for j in range(n))
    return z**t * (upper/lower)**2


def inverse(n, t, value):
    if value <= 0:
        return 0.0
    if value >= kernel(n, t, 1.0):
        return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(56):
        mid = (lo+hi)/2
        if kernel(n, t, mid) < value:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def one_factor(n, bounds):
    low, high = 0.0, 1.0
    for t, (a, b) in enumerate(bounds, 1):
        if a > kernel(n, t, 1.0) or b < 0:
            return None
        low = max(low, inverse(n, t, a))
        high = min(high, inverse(n, t, b))
    return (low, high) if low <= high else None


def slow_fraction(n, bounds, cutoff):
    low, high = 0.0, 1.0
    for t, (a, b) in enumerate(bounds, 1):
        at_cutoff = kernel(n, t, cutoff)
        at_one = kernel(n, t, 1.0)
        low = max(low, (a-at_cutoff)/(at_one-at_cutoff))
        high = min(high, b/at_cutoff)
    return low, high


def region_radius(center, draws, precision):
    delta = draws-center
    squared = np.einsum("bi,ij,bj->b", delta, precision, delta)
    return np.quantile(squared, 1-.05/3, method="higher")


def ellipsoid(n, center, draws):
    # Hold the covariance fixed while calibrating the radius on resampled shape vectors.
    covariance = np.cov(draws, rowvar=False)
    if np.linalg.eigvalsh(covariance)[0] <= 0:
        raise ValueError("Shape covariance is singular")
    precision = np.linalg.inv(covariance)
    precision = (precision + precision.T)/2
    cutoff = region_radius(center, draws, precision)

    # Clearing the positive common denominator converts containment into P(z) <= 0.
    # Isolate all real roots on [0,1] over the rationals for the computed float inputs.
    variable = symbols("z")
    z = Poly(variable, variable)

    def geometric(k):
        return sum(z**j for j in range(k))

    denominator = geometric(n)**2
    offsets = [z**t*geometric(n-t)**2 - denominator*Rational(float(q))
               for t, q in enumerate(center, 1)]
    polynomial = -Rational(float(cutoff))*denominator**2
    for i, left in enumerate(offsets):
        for j, right in enumerate(offsets):
            polynomial += left*right*Rational(float(precision[i,j]))
    roots = polynomial.intervals(inf=0, sup=1, eps=Rational(1, 10**9))
    crossings = [float((a+b)/2) for (a,b), _ in roots]
    # The same rational polynomial locates the extrema of the squared distance.
    derivative = polynomial.diff()*denominator - 2*polynomial*denominator.diff()
    critical = derivative.intervals(inf=0, sup=1, eps=Rational(1, 10**9))
    points = [0., 1.] + [float((a+b)/2) for (a,b), _ in critical]

    def distance(value):
        profile = np.array([kernel(n,t,value) for t in range(1,n)])
        delta = profile-center
        return delta @ precision @ delta

    minimum = min((distance(p), p) for p in points)
    print("  joint ellipsoid: cov condition", round(np.linalg.cond(covariance), 2),
          "squared radius", round(cutoff, 3), "contains z=0", bool(polynomial.eval(0) <= 0),
          "boundary factors", np.round(crossings, 7))
    print("  one-factor minimum (squared distance, z)", np.round(minimum, 5))
    if n == 6:
        for name, v in [("q3", [0,0,1,0,0]), ("q1-q2", [1,-1,0,0,0])]:
            v = np.array(v)
            radius = np.sqrt(cutoff*(v @ covariance @ v))
            print("  ellipsoid projection", name, np.round(v @ center + np.array([-radius,radius]), 6))



def row_contrasts(x):
    n = x.shape[1]//2
    # For an exactly periodic row, C(0)-C(t) is half its mean squared t-step difference.
    def loss(t):
        return ((x-np.roll(x, t, axis=1))**2).mean(axis=1)/2
    midpoint_loss = loss(n)
    return np.column_stack([midpoint_loss] + [midpoint_loss-loss(t) for t in range(1, n)])


def analyze(side, sample, block, repetitions, start=0, omit=None):
    rows = [row_contrasts(chain) for chain in seed_rows(side, sample)]
    rows = [chain[:, start:] for i, chain in enumerate(rows) if i != omit]
    center, replicates = circular_means(rows, block, repetitions)
    if center[0] <= 0 or replicates[:, 0].min() <= 0:
        raise ValueError("Undefined midpoint-subtracted normalization")
    q = center[1:]/center[0]
    draws = replicates[:, 1:]/replicates[:, :1]
    se = draws.std(axis=0, ddof=1)
    if np.any(se <= 0):
        raise ValueError("A shape coordinate has zero estimated variance")
    maxima = np.max(np.abs((draws-q)/se), axis=1)
    crit = np.quantile(maxima, 1-.05/3, method="higher")
    bounds = list(zip(q-crit*se, q+crit*se))
    n = side//2 - start
    print(f"{side=} {sample=} {block=} {start=} {omit=} critical={crit:.3f}")
    print("  point", np.round(q, 5), "SE", np.round(se, 5))
    print("  band", np.round(bounds, 5).tolist())
    interval = one_factor(n, bounds)
    print("  one-factor", np.round(interval, 6) if interval else "empty")
    ellipsoid(n, q, draws)
    if side == 12 and start == 0 and omit is None:
        local_residuals(q, draws)
        augmented_witness(sample, block)
    for cutoff in [1/3, 1/2]:
        band = slow_fraction(n, bounds, cutoff)
        print(f"  fraction at or above {cutoff:.4f}", np.round(band, 6))


def augmented_witness(sample, block):
    """Restore the measured connected midpoint for two fixed examples on the fine lattice."""
    n = 6
    rows = []
    for x in seed_rows(2*n, sample):
        y = x - 0.0057  # A constant shift cancels in the connected midpoint.
        rows.append(np.column_stack([row_contrasts(y), y.mean(1),
                                     (y*np.roll(y, n, axis=1)).mean(1)]))
    center, replicates = circular_means(rows, block, 16000)

    def normalized(v):
        midpoint = v[..., -1:] - v[..., -2:-1]**2
        return np.concatenate([v[..., 1:n], midpoint], axis=-1)/v[..., :1]

    q = normalized(center)
    draws = normalized(replicates)
    covariance = np.cov(draws, rowvar=False)
    precision = np.linalg.inv(covariance)
    radius = region_radius(q, draws, precision)
    print("  augmented squared radius", round(radius, 3))
    for fast, slow, weight in [(0.1, 0.5, 0.7), (0.0, 0.5, 0.78)]:
        def shape(z):
            return np.array([kernel(n,t,z) for t in range(1,n)] +
                            [2*z**n/(1-z**n)**2])
        residual = (1-weight)*shape(fast) + weight*shape(slow) - q
        distance = residual @ precision @ residual
        print("  fixed example (fast, slow, slow share, squared distance)",
              fast, slow, weight, round(distance, 3))


def local_residuals(center, draws):
    """One-factor adjacent-difference recurrence, evaluated without a covariance inverse."""
    def values(v, start):
        full = np.concatenate([np.ones_like(v[..., :1]), v, np.zeros_like(v[..., :1]),
                               v[..., ::-1]], axis=-1)
        u = full-np.roll(full,-1,axis=-1)
        a,b,c,d = (u[...,start+j] for j in range(4))
        return (a+c)*c - (b+d)*b
    for start in (0, 1):
        print("  local residual", start, round(values(center, start), 6),
              "SE", round(values(draws, start).std(ddof=1), 6))


def controls():
    for n in (3, 4, 6):
        for t in range(1, n):
            prev = Fraction(0)
            for j in range(1, 32):
                z = Fraction(j, 32)
                curve = kernel(n, t, z)
                direct = (z**t + z**(2*n-t) - 2*z**n)/(1-z**n)**2
                assert prev < curve == direct < kernel(n, t, Fraction(1))
                assert abs(inverse(n, t, float(curve))-float(z)) < 2e-12
                prev = curve
        z1, z2, weight = Fraction(1, 5), Fraction(3, 4), Fraction(2, 5)
        q = [float((1-weight)*kernel(n,t,z1) + weight*kernel(n,t,z2)) for t in range(1,n)]
        exact = [(x-1e-12, x+1e-12) for x in q]
        assert one_factor(n, exact) is None
        for cutoff in (1/3, 1/2):
            a,b = slow_fraction(n, exact, cutoff)
            assert a <= float(weight) <= b
    x = np.random.default_rng(58).normal(size=(7, 12))
    ref = (x*np.roll(x,6,axis=1)).mean(1)
    direct = np.column_stack([(x*np.roll(x,t,axis=1)).mean(1)-ref for t in range(6)])
    np.testing.assert_allclose(row_contrasts(x), direct, atol=1e-13)
    np.testing.assert_allclose(row_contrasts(x+np.arange(7)[:,None]), direct, atol=1e-13)


if __name__ == "__main__":
    controls()
    for side, base in [(6, 11), (8, 17), (12, 25)]:
        samples = ["frozen-unique", "declared-ids"] if side == 12 else ["frozen-unique"]
        for sample in samples:
            for block in (base, 2*base):
                analyze(side, sample, block, repetitions=16000)
                if side == 12:
                    analyze(side, sample, block, repetitions=16000, start=1)
    for omitted in range(3):
        analyze(12, "frozen-unique", 25, repetitions=16000, omit=omitted)
