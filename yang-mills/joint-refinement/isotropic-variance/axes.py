"""Estimate spatial shells of the connected raw covariance from PR 23's archives."""
import sys
from pathlib import Path
import numpy as np
from stars import jackknife

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/"plaquette-covariance"))
from spectra import orbit_masks, seeds, sides


def metrics(rows,n):
    power=np.mean([p.mean(axis=0) for p,z in rows],axis=0)
    mean=np.mean([z[...,0].mean() for p,z in rows])
    power[0]-=mean**2
    masks=orbit_masks(n)[0]
    indices=np.searchsorted(np.unique(masks),masks)
    cov=np.fft.ifftn(power[indices]).real
    length=np.minimum(np.arange(n),n-np.arange(n))
    coordinates=np.stack(np.meshgrid(length,length,length,indexing="ij"))
    radius=coordinates.max(axis=0)
    tied=coordinates==radius
    axial=np.stack([cov[:,0,0],cov[0,:,0],cov[0,0,:]])
    envelope=(tied*axial[:,radius]).sum(axis=0)/tied.sum(axis=0)
    np.testing.assert_allclose(cov.sum(),power[0],atol=1e-10)
    return np.array([cov[0,0,0],cov[radius>=2].sum(),power[0],envelope.sum()])


def channels(rows):
    zero=np.concatenate([z[...,0] for _,z in rows])
    zero-=zero.mean()
    scalar=zero.sum(axis=-1)/np.sqrt(3)
    s=np.mean(scalar**2)
    d=(np.mean(np.sum(zero**2,axis=-1))-s)/2
    st=np.mean(scalar[:,0]*scalar[:,1])
    dt=(np.mean(np.sum(zero[:,0]*zero[:,1],axis=-1))-st)/2
    np.testing.assert_allclose((s+2*d)/3,np.mean(zero**2))
    return np.array([s,d,st,dt])


def origin_averaged_packing(rows,n,stride):
    p=np.mean([powers.mean(axis=0) for powers,_ in rows],axis=0)
    p[0]-=np.mean([z[...,0].mean() for _,z in rows])**2
    masks=orbit_masks(n)[0]
    indices=np.searchsorted(np.unique(masks),masks)
    step=n//stride
    return p[indices][::step,::step,::step].mean()


def main():
    for extent in (6,10):
        with np.load(ROOT.parent/f"plaquette-covariance/spectra{extent}.npz",allow_pickle=False) as data:
            for n in sides(extent):
                rows=[(data[f"{n}_{s}_power"],data[f"{n}_{s}_zero"]) for s in seeds(n,extent)]
                values,errors=jackknife(rows,lambda sample:metrics(sample,n))
                print(extent,n," ".join(f"{v:.6f}({e:.6f})" for v,e in zip(values,errors)))
                values,errors=jackknife(rows,channels)
                print("  scalar, difference, scalar lag, difference lag",
                      " ".join(f"{v:.6f}({e:.6f})" for v,e in zip(values,errors)))
                for stride in (2,4):
                    if n%stride==0:
                        value,error=jackknife(rows,lambda sample:origin_averaged_packing(sample,n,stride))
                        print("  origin-averaged packing",stride,f"{value:.6f}({error:.6f})")


if __name__=="__main__":
    main()
