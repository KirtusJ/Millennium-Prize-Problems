"""Midpoint-reflected winding and clover readings on the archived SU(2) ensembles."""
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[3] / "g4" / "full-attempt" / "physical-refinement"
sys.path.insert(0, str(SOURCE))
from analysis import read_streams, SLICES


def per_configuration(samples, n, window):
    end = samples.shape[1] - 1
    assert end == 6*n
    if window == "point":
        # Odd N uses adjacent insertions on EACH half, including all four products.
        times = sorted({5*n//2, (5*n+1)//2})
    elif window == "window":
        times = range((3*n+1)//2, 5*n//2+1)
    else:
        raise ValueError(window)
    idx = np.array(times)
    probes = np.stack([samples[:, :, SLICES[p]] for p in ("E_wind", "E_local")], axis=-1)
    left, right = probes[:, idx].mean(axis=1), probes[:, end-idx].mean(axis=1)
    def products(x, y):
        return np.stack([(x[...,0]*y[...,0]).mean(axis=1),
                         ((x[...,0]*y[...,1]+x[...,1]*y[...,0])/2).mean(axis=1),
                         (x[...,1]*y[...,1]).mean(axis=1)], axis=-1)
    return np.column_stack((products(left,right), (products(left,left)+products(right,right))/2))


def metrics(means):
    a, b = means
    ww, wc, cc, aw, ac, al = (a+b)/2
    norm = aw*al
    assert norm > ac**2
    # Independent-stream product estimates the population determinant in raw units.
    det_cross = (a[0]*b[2]+a[2]*b[0])/2 - a[1]*b[1]
    plugin = ww*cc - wc*wc
    return np.array([ww/aw, wc/np.sqrt(norm), cc/al,
                     det_cross/norm, plugin/norm, ac/np.sqrt(norm)])


def reduce(streams):
    assert len(streams) == 2 and streams[0].shape == streams[1].shape
    means = np.array([s.mean(axis=0) for s in streams])
    central = metrics(means)
    errors = []
    for block in (8,16,32):
        variance = np.zeros_like(central)
        for i, observations in enumerate(streams):
            blocks = observations.reshape(-1, block, 6).mean(axis=1)
            count = len(blocks)
            reps = []
            for deleted in blocks:
                reduced = means.copy()
                reduced[i] = (count*means[i]-deleted)/(count-1)
                reps.append(metrics(reduced))
            variance += (count-1) * np.var(reps, axis=0)
        errors.append(np.sqrt(variance))
    # Sensitivity to the two starting conditions for the three linear entries.
    # A single stream cannot supply the independent-product determinant.
    split = (metrics(np.array([means[0],means[0]]))-metrics(np.array([means[1],means[1]])))/2
    conservative = np.max(errors, axis=0)
    conservative[:3] = np.maximum(conservative[:3], np.abs(split[:3]))
    return central, conservative


def main():
    ensembles = read_streams(SOURCE/"samples.zip")
    print("filter N   Gww/Aww       Gwc/sqrt(Aww Acc)  Gcc/Acc       cross-det/(Aww Acc)   plug-in det    same-side corr")
    for window in ("point","window"):
        values, errors = [], []
        for n in (5,6,7,8,10):
            t, group = ensembles[n,"smoothed"]
            assert t == 6*n and {s[0] for s in group} == {0,1} and len({s[1] for s in group}) == 2
            data = [per_configuration(s[2],n,window) for s in sorted(group)]
            central, se = reduce(data)
            values.append(central)
            errors.append(se)
            # The population Gram is positive; preserve every negative sample estimate.
            print(f"{window:6} {n:2} " + " ".join(f"{x: .5f}({y:.5f})" for x,y in zip(central,se)))

        mu = np.mean(values,axis=0)
        pooled_error = np.linalg.norm(errors,axis=0)/len(values)
        lower_cross = max(0., abs(mu[1])-3*pooled_error[1])
        upper_winding = mu[0]+3*pooled_error[0]
        lower_local = lower_cross**2/upper_winding if upper_winding > 0 else float("nan")
        print(f"{window}: mean mixed={mu[1]:.8f} +/- {pooled_error[1]:.8f}, "
              f"mean winding={mu[0]:.8f} +/- {pooled_error[0]:.8f}, "
              f"mean clover={mu[2]:.8f} +/- {pooled_error[2]:.8f}")
        print(f"three-error rectangle: |mixed| >= {lower_cross:.8f}, "
              f"winding <= {upper_winding:.8f}, implied clover >= {lower_local:.8f}")
        if window == "point":
            assert lower_cross >= .02287 and upper_winding <= .29865
            assert 2287**2 > 29865*175


if __name__ == "__main__":
    main()
