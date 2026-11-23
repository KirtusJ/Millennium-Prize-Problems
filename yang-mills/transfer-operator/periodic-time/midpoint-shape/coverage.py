"""Finite-sample calibration control using independent synthetic Gaussian ensembles."""
import numpy as np
from scipy.signal import lfilter

from check import circular_means, kernel, region_radius, row_contrasts


def run(rho, trials=256, repetitions=3000):
    n = 6
    z = .40
    # A Gaussian AR(1) across configurations. Each periodic row has a known one-factor covariance.
    distance = np.abs(np.arange(2*n)[:,None]-np.arange(2*n))
    row_covariance = (z**distance+z**(2*n-distance))/(1+z**(2*n))
    cholesky = np.linalg.cholesky(row_covariance)
    grid = np.linspace(0, 1, 501)
    profiles = np.column_stack([kernel(n, t, grid) for t in range(1, n)])
    truth = np.array([kernel(n, t, z) for t in range(1,n)])
    rng = np.random.default_rng(46193)
    misses = {b: np.zeros(4, dtype=int) for b in (25, 50)}
    inflation = {b: [] for b in misses}
    for _ in range(trials):
        chains = []
        for length in (260, 287, 287):
            innovations = rng.normal(size=(length, 2*n)) @ cholesky.T
            innovations[1:] *= np.sqrt(1-rho*rho)
            x = lfilter([1.], [1., -rho], innovations, axis=0)
            chains.append(row_contrasts(x))
        for block in misses:
            center, samples = circular_means(chains, block, repetitions)
            q = center[1:]/center[0]
            draws = samples[:,1:]/samples[:,:1]
            precision = np.linalg.inv(np.cov(draws, rowvar=False))
            cutoff = region_radius(q, draws, precision)
            residual = profiles-q
            best = ((residual @ precision)*residual).sum(1).min()
            # Grid rejections upper-bound rejections on the entire continuous curve.
            observed_ratio = 37.39653/13.857 if block == 25 else 51.53994/13.682
            standardized = draws.std(axis=0, ddof=1)
            maximum = np.abs((draws-q)/standardized).max(axis=1)
            box_cutoff = np.quantile(maximum, 1-.05/3, method="higher")
            true_ratio = ((truth-q) @ precision @ (truth-q))/cutoff
            inflation[block].append(true_ratio)
            misses[block] += [(np.abs(truth-q)/standardized).max() > box_cutoff,
                              true_ratio > 1,
                              best > cutoff, best/cutoff >= observed_ratio]
    print("rho, trials, block, missed box truth, missed ellipsoid truth, missed grid,"
          " grid ratio >= Wilson ratio, 98.33% true squared-radius multiplier")
    for block, counts in misses.items():
        print(rho, trials, block, *counts, round(np.quantile(
            inflation[block], 1-.05/3, method="higher"), 3))


if __name__ == "__main__":
    for persistence in (.60, .90):
        run(persistence)
