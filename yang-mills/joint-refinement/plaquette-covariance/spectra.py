"""Reduce the reproducible open-slab fields to per-configuration moments."""
import argparse
from pathlib import Path
from zipfile import ZipFile
import numpy as np

ROOT = Path(__file__).resolve().parent
BETA = {6:3.276133577,8:3.399810242,10:3.493705679}
PRIOR = ROOT.parents[1]/"g4/full-attempt/physical-refinement/samples.zip"


def orbit_masks(n):
    k = np.minimum(np.arange(n),n-np.arange(n))
    z,y,x = np.meshgrid(k,k,k,indexing="ij")
    coords = [x,y,z]
    masks = []
    for i in range(3):
        f,g = coords[(i+1)%3],coords[(i+2)%3]
        masks.append((coords[i]*(n+1)+np.minimum(f,g))*(n+1)+np.maximum(f,g))
    return masks


def seeds(n,extent):
    base,stride=(194223+1435*n,12007) if extent==6 else (2432111+2143*n,13883)
    return [base+stride*i for i in range(4)]


def sides(extent):
    return (6,8,10) if extent==6 else (6,10)


def pack(folder, target, extent):
    out = {}
    with ZipFile(PRIOR) as prior:
        for n in sides(extent):
            beta=BETA[n]
            masks = orbit_masks(n)
            keys = np.unique(masks[0])
            assert all(np.array_equal(keys,np.unique(m)) for m in masks)
            for seed in seeds(n,extent):
                name=f"{n}_{seed}"
                raw=np.fromfile(folder/(name+".bin"),"<f8").reshape(320,2,n**3+1,3)
                fine=raw[:,:,:-1].reshape(320,2,n,n,n,3)
                coarse_sum=raw[:,:,-1]
                plaq=1-fine.mean(axis=(2,3,4,5))/beta
                assert np.isfinite(raw).all() and np.all(np.abs(plaq)<=1)
                if extent==6:
                    old, = [k for k in prior.namelist() if k.startswith(f"open_{n}_{6*n}_")
                            and k.split("_")[4]==str(seed) and k.split("_")[6:8]==["384","320"]]
                    ref=np.frombuffer(prior.read(old),"<f4").reshape(320,6*n+1,14)
                    np.testing.assert_array_equal(plaq.astype("<f4"),ref[:,[5*n//2,7*n//2],0])
                modes=np.fft.fftn(fine,axes=(2,3,4),norm="ortho")
                powers=np.abs(modes)**2
                spectrum=np.empty((320,len(keys)))
                for j,key in enumerate(keys):
                    parts=[powers[...,a][:,:,m==key].mean(axis=(1,2)) for a,m in enumerate(masks)]
                    spectrum[:,j]=np.mean(parts,axis=0)
                zero=np.stack([modes[:,:,0,0,0,:].real,coarse_sum/n**1.5],axis=-1)
                np.testing.assert_allclose(spectrum[:,0],(zero[...,0]**2).mean(axis=(1,2)))
                out[name+"_power"]=spectrum
                out[name+"_zero"]=zero
    np.savez_compressed(target,**out)


def summaries(arrays):
    mean=np.mean([z.mean(axis=(0,1,2)) for _,z in arrays],axis=0)
    eq=np.mean([np.einsum("atxi,atxj->ij",z,z)/(320*2*3) for _,z in arrays],axis=0)-np.outer(mean,mean)
    lag=np.mean([np.einsum("axi,axj->ij",z[:,0],z[:,1])/(320*3) for _,z in arrays],axis=0)-np.outer(mean,mean)
    lag=(lag+lag.T)/2
    w=np.array([1.,-eq[0,1]/eq[1,1]])
    var=w@eq@w
    spectrum=np.mean([p.mean(axis=0) for p,_ in arrays],axis=0)
    best=1+np.argmax(spectrum[1:])
    return np.array([eq[0,0],spectrum[best],var/eq[0,0],
                     (w@lag@w)/var,(lag[1]@w)/np.sqrt(eq[1,1]*var)]),best,spectrum-eq[0,0]


def readback(archive,extent):
    with np.load(archive,allow_pickle=False) as data:
        assert len(data.files)==8*len(sides(extent))
        for n in sides(extent):
            rows=[]
            for seed in seeds(n,extent):
                key=f"{n}_{seed}"
                p,z=data[key+"_power"],data[key+"_zero"]
                assert p.shape==(320,len(np.unique(orbit_masks(n)[0]))) and z.shape==(320,2,3,2)
                assert np.isfinite(z).all() and np.isfinite(p).all() and np.min(p)>=0
                rows.append((p,z))
            value,best,gaps=summaries(rows)
            deletions=[summaries(rows[:i]+rows[i+1:]) for i in range(4)]
            leave=np.array([state[0] for state in deletions])
            se=np.sqrt(3*np.mean((leave-leave.mean(axis=0))**2,axis=0))
            code=int(np.unique(orbit_masks(n)[0])[best])
            normal,rem=divmod(code,(n+1)**2)
            print(n,(normal,*divmod(rem,n+1)), " ".join(f"{v:.6f}({e:.6f})" for v,e in zip(value,se)))
            keys=np.unique(orbit_masks(n)[0])
            for label,key in [("parallel",1),("normal",(n+1)**2)]:
                j,=np.flatnonzero(keys==key)
                values=np.array([state[2][j] for state in deletions])
                print("first",label,"minus zero",f"{gaps[j]:.6f}({np.sqrt(3*np.mean((values-values.mean())**2)):.6f})")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--pack",type=Path,help="directory containing the regenerated binary fields")
    p.add_argument("--extent",type=int,choices=(6,10),default=6)
    p.add_argument("--archive",type=Path)
    args=p.parse_args()
    if args.pack:
        pack(args.pack,args.archive or ROOT/f"spectra{args.extent}.npz",args.extent)
    readback(args.archive or ROOT/f"spectra{args.extent}.npz",args.extent)
