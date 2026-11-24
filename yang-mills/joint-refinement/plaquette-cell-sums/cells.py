"""Fourier covariance of translated clear-cell marks and conditional two-copy losses."""
from pathlib import Path
from zipfile import ZipFile
import numpy as np

ROOT=Path(__file__).resolve().parent


def read(z,label):
    side=4 if label=="n8" else 3
    cells=side**3
    streams=[]
    for i in range(4):
        rows=np.loadtxt(z.open(f"{label}-{i}.csv"),skiprows=1,delimiter=",")
        assert rows.shape==(160*cells,7)
        np.testing.assert_array_equal(rows[:,0],np.repeat(np.arange(160),cells))
        np.testing.assert_array_equal(rows[:,1],np.tile(np.arange(cells),160))
        assert np.max(abs(rows[:,2]))<=1 and np.max(abs(rows[:,3:]))<=2
        streams.append(rows[:,2:].reshape(160,side,side,side,5))
    return np.array(streams)


def moments(streams):
    data=np.concatenate(streams)
    marks=data[...,0]-data[...,0].mean()
    deltas=data[...,1:]
    fft=lambda x: np.fft.fftn(x,axes=(1,2,3),norm="ortho")
    var=np.mean(abs(fft(marks))**2,axis=0)
    j_diagonal=np.mean(np.sum(deltas**2,axis=-1))/48
    j_mode=np.sum(np.mean(abs(fft(deltas))**2,axis=0),axis=-1)/48
    return var,j_diagonal,j_mode


def report(streams):
    zero=(0,0,0)
    def summary(group):
        v,j,jmode=moments(group)
        return np.array([v.mean(),v[zero],v[zero]/v.mean(),j,j/v[zero],
                         jmode[zero]/j,j/v.max()])
    full=summary(streams)
    omit=np.stack([summary(np.delete(streams,i,axis=0)) for i in range(4)])
    err=np.sqrt(.75*np.sum((omit-omit.mean(axis=0))**2,axis=0))
    print("estimate"," ".join(f"{v:.7f}" for v in full))
    print("stream SE"," ".join(f"{s:.7f}" for s in err))
    print("cold/hot J/V at zero", summary(streams[::2])[4],summary(streams[1::2])[4])
    var,j,_=moments(streams)
    print("mode maximizing covariance (z,y,x)",np.unravel_index(var.argmax(),var.shape))
    for train,test in (([0,1],[2,3]),([2,3],[0,1])):
        v,_,_=moments(streams[train])
        index=np.unravel_index(v.argmax(),v.shape)
        w,k,_=moments(streams[test])
        print("held-out J/V at selected mode",index,k/w[index])
    return full


if __name__=="__main__":
    with ZipFile(ROOT/"cells.zip") as z:
        for label in ("haar","n6","n8"):
            print(label)
            estimate=report(read(z,label))
            if label=="haar":
                # Loose checks on finite random data. The Haar values are analytic.
                np.testing.assert_allclose(estimate[[0,1,3,4]],[1/16,1/16,1/128,1/8],rtol=.18)
