"""Evaluate the unconditioned opposite-source ratio in the five open preparations."""
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parent
DATA = ROOT.parent / "plaquette-covariance"
sys.path.insert(0, str(DATA))
sys.path.insert(0, str(ROOT.parent / "isotropic-variance"))
from spectra import seeds, sides
from stars import jackknife


def paired_source(rows, h=0.5):
    sample = np.concatenate(rows).ravel()
    sample -= sample.mean()
    log_ratio = sum(np.logaddexp.reduce(sign*h*sample)-np.log(sample.size) for sign in (-1, 1))
    proxy = np.expm1(log_ratio)/h**2
    assert proxy >= sample.var() - 1e-11
    return np.array([proxy, sample.var()])


if __name__ == "__main__":
    for extent in (6, 10):
        with np.load(DATA/f"spectra{extent}.npz", allow_pickle=False) as data:
            for n in sides(extent):
                rows = [data[f"{n}_{seed}_zero"][..., 0] for seed in seeds(n, extent)]
                values, errors = jackknife(rows, paired_source)
                print(extent, n, " ".join(f"{v:.6f}({e:.6f})" for v, e in zip(values, errors)))
