"""Paired stream jackknife for stationary coarse-gate returns on finite tori."""
from pathlib import Path
from zipfile import ZipFile
import numpy as np


def analyse(archive, design):
    totals = []
    for stream in range(4):
        with archive.open(f"{design}-{stream}.csv") as source:
            rows = np.loadtxt(source, delimiter=",", skiprows=1).reshape(128,6,7)
        assert np.array_equal(rows[:,:,0], np.repeat(np.arange(128)[:,None],6,axis=1))
        np.testing.assert_allclose(rows[:,:,1], np.tile(np.arange(1,7)/5, (128,1)))
        assert np.all(rows[:,:,3] <= rows[:,:,2]) and np.all(rows[:,:,4:] <= rows[:,:,3,None])
        totals.append(rows[:,:,2:].sum(axis=0))
    return np.stack(totals)


def summarize(count):
    exposures, hits, *pairs = count.T
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.column_stack([hits/exposures, *(pair/hits for pair in pairs)])


if __name__ == "__main__":
    with ZipFile(Path(__file__).with_name("returns.zip")) as archive:
        for design in ("haar", "n6", "n8"):
            data = analyse(archive, design)
            total = data.sum(axis=0)
            ratios = summarize(total)
            loo = np.stack([summarize(total-stream) for stream in data])
            errors = np.sqrt(.75 * np.sum((loo-loo.mean(axis=0))**2,axis=0))
            errors[total[:,1:] == 0] = np.nan
            for i,(values, err) in enumerate(zip(ratios,errors)):
                print(design, f"radius={(i+1)/5:.1f}", "counts", total[i].astype(int).tolist(),
                      "ratios", np.round(values,7), "stream SE", np.round(err,7))
            for name, parity in [("cold",0),("hot",1)]:
                print(design, name, "r=1.2", summarize(data[parity::2].sum(axis=0))[-1])
