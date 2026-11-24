"""Symmetrized matched-lag, four-bin compression. Run with NumPy."""
from pathlib import Path
from zipfile import ZipFile
import numpy as np

ROOT=Path(__file__).resolve().parent


def read(label,archive,long=False):
    streams=[]
    n=10 if label=="n10" else 5
    for i in range(4):
        data=np.loadtxt(archive.open(f"{label}-{i}.csv"),delimiter=",",dtype=int)
        samples=192 if long else 128
        period=(4 if long else 2)*n
        assert data.shape==(samples,17)
        np.testing.assert_array_equal(data[:,0],np.arange(samples))
        raw=data[:,1:].reshape(-1,4,4)
        assert (raw>=0).all() and (raw.sum(axis=(1,2))==75*period).all()
        np.testing.assert_array_equal(raw.sum(axis=1),raw.sum(axis=2))
        streams.append(raw)
    return np.array(streams)


def spectrum(counts):
    joint=counts+counts.T
    joint=joint/joint.sum()
    root=np.sqrt(joint.sum(axis=0))
    operator=joint/np.outer(root,root)
    eigen=np.linalg.eigvalsh(operator)
    np.testing.assert_allclose(eigen[-1],1.0)
    return eigen[-2]


def report(raw):
    sums=raw.sum(axis=1)
    full=spectrum(sums.sum(axis=0))
    omit=np.array([spectrum(sums.sum(axis=0)-s) for s in sums])
    se=np.sqrt(.75*np.sum((omit-omit.mean())**2))
    cold=spectrum(sums[::2].sum(axis=0))
    hot=spectrum(sums[1::2].sum(axis=0))
    # Held-out Rayleigh score limits selection bias from fitting the largest eigenvalue.
    training=sums[[0,1]].sum(axis=0)
    testing=sums[[2,3]].sum(axis=0)
    def held(train,test):
        jt=(train+train.T)/(2*train.sum())
        rt=np.sqrt(jt.sum(axis=0))
        vector=np.linalg.eigh(jt/np.outer(rt,rt))[1][:,-2]/rt
        j=(test+test.T)/(2*test.sum())
        v=j.sum(axis=0)
        centered=vector-v@vector
        return (centered@j@centered)/(v@(centered**2))
    return full,se,cold,hot,held(training,testing),held(testing,training)


def summarize(long):
    with ZipFile(ROOT/("long-streams.zip" if long else "streams.zip")) as archive:
        values={}
        for label in (("n5","n10") if long else ("haar","n5","n10")):
            values[label]=report(read(label,archive,long))
            print(label," ".join(f"{v:.7f}" for v in values[label]))
        f,c=values["n10"],values["n5"]
        print(f"fine minus coarse: {f[0]-c[0]:+.7f} +/- {np.hypot(f[1],c[1]):.7f}")


if __name__=="__main__":
    for long in (False,True):
        print("time circumference",4 if long else 2,"spatial lengths")
        summarize(long)
