"""Seed-separated readings from the frozen Wilson files and declared-count replay."""
import argparse
from pathlib import Path

import numpy as np

DATA = Path(__file__).resolve().parents[2] / "z4/reviews/ext-match/predeclared"
SAMPLES = ("frozen-unique", "declared-ids", "historical-rows")


def arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sample", choices=SAMPLES, default=SAMPLES[0])
    return parser.parse_args()


def unique_records(data):
    """Check repeated IDs agree on every measured field (last column is timing)."""
    ids = data[:, 0].astype(int)
    if not np.array_equal(ids, data[:, 0]):
        raise ValueError("Nonintegral configuration ID")
    seen = {}
    for i, cfg in enumerate(ids):
        if cfg in seen:
            if not np.array_equal(data[i, 1:-1], data[seen[cfg], 1:-1]):
                raise ValueError(f"Conflicting physical readings for ID {cfg}")
        else:
            seen[cfg] = i
    if list(seen) != list(range(len(seen))):
        raise ValueError("Distinct configuration IDs have gaps or arrive out of order")
    return data[list(seen.values())]


def seed_rows(side, sample):
    files = sorted(DATA.glob(f"meas_L{side}_*.txt"))
    if len(files) != {6:1, 8:1, 12:3}[side]:
        raise ValueError(f"Unexpected seed list for side {side}")
    for path in files:
        frozen = np.loadtxt(path)
        rows = unique_records(frozen)
        if sample == "declared-ids" and len(rows) < len(frozen):
            snapshot = np.loadtxt(DATA.parent/path.name)
            if not np.array_equal(snapshot[:len(frozen)], frozen):
                raise ValueError(f"Snapshot prefix changed for {path.name}")
            rows = unique_records(snapshot)[:len(frozen)]
            if len(rows) != len(frozen):
                raise ValueError(f"Incomplete declared IDs in {path.name}")
        elif sample == "historical-rows":
            rows = frozen
        yield rows[10:, 2+2*side:2+3*side]


def circular_means(chains, block, repetitions=4000):
    """Bootstrap entire seeds separately, drawing circular blocks within each seed."""
    rng = np.random.default_rng(20261123)
    total = sum(len(chain) for chain in chains)
    replicates = np.zeros((repetitions, chains[0].shape[1]))
    for chain in chains:
        n = len(chain)
        extended = np.concatenate((chain, chain[:block]))
        cumulative = np.vstack((np.zeros(chain.shape[1]), extended.cumsum(axis=0)))
        count, tail = divmod(n, block)
        starts = rng.integers(n, size=(repetitions,count))
        replicates += (cumulative[starts+block]-cumulative[starts]).sum(axis=1)
        if tail:
            starts = rng.integers(n, size=repetitions)
            replicates += cumulative[starts+tail]-cumulative[starts]
    return sum(c.sum(axis=0) for c in chains)/total, replicates/total
