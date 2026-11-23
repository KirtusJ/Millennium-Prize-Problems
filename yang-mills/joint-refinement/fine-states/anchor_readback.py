"""Check the archived open-slab replay and reduce each chain before estimating errors."""
from pathlib import Path
from zipfile import ZipFile
import numpy as np

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parents[1]/"g4/full-attempt/physical-refinement/samples.zip"


def reduce(archive):
    groups = {}
    with ZipFile(archive) as new, ZipFile(OLD) as old:
        for name in sorted(new.namelist()):
            n, seed = map(int,Path(name).stem.split("_"))
            prior = [k for k in old.namelist() if k.startswith(f"open_{n}_{6*n}_") and k.split("_")[4] == str(seed)]
            assert len(prior)==1
            fields = Path(prior[0]).stem.split("_")
            burn, count = map(int, fields[6:8])
            anchors = np.frombuffer(new.read(name),"<f8").reshape(count,2,8,3)
            full = anchors.mean(axis=2)
            reference = np.frombuffer(old.read(prior[0]),"<f4").reshape(count,6*n+1,14)
            np.testing.assert_array_equal(full.astype("<f4"),reference[:,[5*n//2,7*n//2],2:5])
            deviation = anchors-full[:,:,None,:]
            v, d = np.mean(full**2), np.mean(deviation**2)
            vt, dt = np.mean(full[:,0]*full[:,1]), np.mean(deviation[:,0]*deviation[:,1])
            # Origin averaging kills both mixed terms before averaging over configurations.
            np.testing.assert_allclose(np.mean(anchors[:,0]*anchors[:,1]),vt+dt,atol=2e-17)
            groups.setdefault((n,burn),[]).append([v,d,vt,dt])
    return groups


def ratios(x):
    v,d,vt,dt = np.moveaxis(x,-1,0)
    return np.stack([d/(v+d),vt/v,dt/d],axis=-1)


if __name__ == "__main__":
    groups = reduce(ROOT/"anchors.zip")
    assert set(groups)=={(n,burn) for n in (6,8,10) for burn in (112,384)}
    for (n,burn), rows in sorted(groups.items()):
        x = np.array(rows)
        k = len(x)
        assert k==(2 if burn==112 else 4)
        estimates = ratios(x.mean(axis=0))
        jack = ratios((x.sum(axis=0)-x)/(k-1))
        se = np.sqrt((k-1)*np.mean((jack-jack.mean(axis=0))**2,axis=0))
        print(n,burn,"mean linear loss, full lag, difference lag",
              " ".join(f"{m:.6f}({e:.6f})" for m,e in zip(estimates,se)))
