"""Four-stream reductions for the specified raw skeleton with a marked coarse plaquette."""
from pathlib import Path
from zipfile import ZipFile
import io
import numpy as np


def estimate(rows):
    data=np.concatenate(rows)
    var=data[:,:2].var(axis=0)
    j=data[:,3:5].mean(axis=0)
    return np.r_[data[:,2].mean(),var,j/var]


def main():
    root=Path(__file__).resolve().parent
    with ZipFile(root/"fixed.zip") as z:
        assert len(z.namelist())==24
        for label in ("plus6","minus6","minus8","cold16","plus8long","minus8long"):
            rows=[]
            for i in range(4):
                raw=z.read(f"{label}-s{i}.csv")
                assert raw.splitlines()[0]==b"single,average,spread,j_single,j_average"
                a=np.loadtxt(io.BytesIO(raw),skiprows=1,delimiter=",")
                assert a.shape==((256 if "long" in label else 144),5) and np.all(np.isfinite(a))
                assert (np.abs(a[:,:2])<=1+1e-11).all() and (a[:,2:]>=-1e-12).all()
                rows.append(a)
            full=estimate(rows)
            drops=np.stack([estimate(rows[:i]+rows[i+1:]) for i in range(4)])
            err=np.sqrt(3*np.mean((drops-drops.mean(axis=0))**2,axis=0))
            print(label," ".join(f"{v:.6f}({s:.6f})" for v,s in zip(full,err)))
            means=np.stack([data[:,:2].mean(axis=0) for data in rows])
            print("  stream means of mark",np.round(means[:,0],4).tolist(),
                  "and of four-face average",np.round(means[:,1],4).tolist())
            for subset in (rows[::2],rows[1::2]):
                strata=estimate(subset)
                print("  start-stratified variances",np.round(strata[1:3],5).tolist(),
                      "numerators",np.round(strata[1:3]*strata[3:],5).tolist(),
                      "ratios",np.round(strata[-2:],5).tolist())


if __name__=="__main__":
    main()
