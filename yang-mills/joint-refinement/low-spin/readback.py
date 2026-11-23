"""Reduce the paired Wilson trajectories and compare them with their original records."""
from pathlib import Path
from zipfile import ZipFile
import numpy as np

ROOT = Path(__file__).resolve().parent


def estimates(rows):
    v, d, innovation, second, lag_delta = np.moveaxis(rows, -1, 0)
    upper = v*d/(v+d)
    return np.stack([innovation/v, upper/v, 1-innovation/upper, (second-v)/v, lag_delta/v], axis=-1)


def readback():
    groups = {}
    with (ZipFile(ROOT/"samples.zip") as current,
          ZipFile(ROOT.parent/"fine-states/anchors.zip") as prior,
          ZipFile(ROOT.parents[1]/"g4/full-attempt/physical-refinement/samples.zip") as orig):
        for name in sorted(current.namelist()):
            n, seed = map(int, Path(name).stem.split("_"))
            key, = [k for k in orig.namelist() if k.startswith(f"open_{n}_{6*n}_")
                    and k.split("_")[4] == str(seed) and k.split("_")[6:8] == ["384","320"]]
            record = np.frombuffer(orig.read(key), "<f4").reshape(320,6*n+1,14)
            obs = np.frombuffer(current.read(name), "<f8").reshape(320,2,4,3)
            full, coarse, mean, var = np.moveaxis(obs, 2, 0)
            anchors = np.frombuffer(prior.read(name), "<f8").reshape(320,2,8,3)
            np.testing.assert_allclose(coarse, anchors[:,:,0], rtol=0, atol=2e-14)
            np.testing.assert_array_equal(full.astype("<f4"), record[:,[5*n//2,7*n//2],2:5])
            np.testing.assert_allclose(full, anchors.mean(axis=2), rtol=0, atol=2e-14)
            assert np.isfinite(obs).all() and np.min(var) >= 0
            error = anchors-full[:,:,None,:]
            groups.setdefault(n, []).append([
                np.mean(full**2), np.mean(error**2), var.mean(), np.mean(mean**2+var),
                np.mean(mean[:,0]*mean[:,1] - full[:,0]*full[:,1])
            ])
    assert {n:len(g) for n,g in groups.items()} == {6:4,8:4,10:4}
    for n, streams in sorted(groups.items()):
        rows = np.array(streams)
        value = estimates(rows.mean(axis=0))
        omit = estimates((rows.sum(axis=0)-rows)/3)
        se = np.sqrt(3*np.mean((omit-omit.mean(axis=0))**2, axis=0))
        print(n, " ".join(f"{v:.6f}({e:.6f})" for v,e in zip(value,se)))


def replication():
    groups = {}
    with ZipFile(ROOT/"replication.zip") as z:
        for name in sorted(z.namelist()):
            n, seed = map(int, Path(name).stem.split("_"))
            idx, rem = divmod(seed-1357001-1123*n,15101)
            assert 0 <= idx < 6 and rem == 0
            obs = np.frombuffer(z.read(name),"<f8").reshape(320,2,4,3)
            full, _, mean, var = np.moveaxis(obs,2,0)
            assert np.isfinite(obs).all() and np.min(var) >= 0
            groups.setdefault(n, []).append([np.mean(full**2), var.mean(),
                np.mean(mean**2+var-full**2), np.mean(mean[:,0]*mean[:,1]-full[:,0]*full[:,1])])
    assert {n:len(g) for n,g in groups.items()} == {6:6,10:6}
    for n, streams in sorted(groups.items()):
        rows = np.array(streams)
        combined = rows.sum(axis=0)
        value = combined[1:]/combined[0]
        leave = combined-rows
        jack = leave[:,1:]/leave[:,:1]
        se = np.sqrt(5*np.mean((jack-jack.mean(axis=0))**2,axis=0))
        print("replication",n," ".join(f"{v:.6f}({e:.6f})" for v,e in zip(value,se)))


if __name__ == "__main__":
    readback()
    replication()
