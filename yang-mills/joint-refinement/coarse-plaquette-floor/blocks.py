"""Connected variance of cubic blocks from the deposited momentum data."""
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parent
DATA = ROOT.parent / "plaquette-covariance"
sys.path.insert(0, str(DATA))
sys.path.insert(0, str(ROOT.parent / "isotropic-variance"))
from spectra import orbit_masks, seeds, sides
from stars import jackknife


def lengths(n):
    values = [1]
    while values[-1] < n:
        values.append(min(n, 2 * values[-1]))
    return values


def block_estimates(rows, n):
    for power, zero in rows:
        np.testing.assert_allclose(power[:, 0], (zero[..., 0]**2).mean(axis=(1, 2)))
    powers = np.mean([power.mean(axis=0) for power, zero in rows], axis=0)
    mean = np.mean([zero[..., 0].mean() for power, zero in rows])
    powers[0] -= mean**2
    mask = orbit_masks(n)[0]
    spectrum = powers[np.searchsorted(np.unique(mask), mask)]
    values = []
    correlation = np.fft.ifftn(spectrum).real
    offsets = np.arange(n)
    for length in lengths(n):
        indicator = (offsets < length).astype(float)
        weight = abs(np.fft.fft(indicator))**2 / length
        weights = np.einsum("i,j,k->ijk", weight, weight, weight)
        value = np.mean(weights * spectrum)
        # Periodic overlap counts are a direct real-space cross-check.
        overlap = np.maximum(0, length - offsets) + np.maximum(0, length - (n - offsets))
        real_weights = np.einsum("i,j,k->ijk", overlap, overlap, overlap) / length**3
        np.testing.assert_allclose(value, np.sum(correlation * real_weights), atol=1e-10)
        values.append(value)
    np.testing.assert_allclose(values[-1], powers[0], atol=1e-10)
    return np.r_[values[0], np.diff(values), values[-1]]


if __name__ == "__main__":
    for extent in (6, 10):
        with np.load(DATA / f"spectra{extent}.npz", allow_pickle=False) as data:
            for n in sides(extent):
                rows = [(data[f"{n}_{seed}_power"], data[f"{n}_{seed}_zero"]) for seed in seeds(n, extent)]
                vals, errors = jackknife(rows, lambda subset: block_estimates(subset, n))
                print(extent, n, lengths(n), " ".join(f"{v:.6f}({e:.6f})" for v, e in zip(vals, errors)))
                stream_means = np.array([zero[..., 0].mean() for _, zero in rows])
                cross = np.outer(stream_means, stream_means)[~np.eye(len(rows), dtype=bool)].mean()
                correction = stream_means.mean()**2 - cross
                np.testing.assert_allclose(correction, stream_means.var(ddof=1)/len(rows), atol=5e-12)
                print(f"  cross-stream centering changes full susceptibility by {correction:+.8f}")
