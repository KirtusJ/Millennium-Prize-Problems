"""Read back conditional link integration in the matched open preparations."""
import argparse
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
import numpy as np

ROOT = Path(__file__).resolve().parent
def names(n,extent):
    base,offset,stride=(194223,1435,12007) if extent==6 else (2432111,2143,13883)
    return [f"{n}_{base+offset*n+stride*i}" for i in range(4)]


def design(extent):
    return ((6,8,10),160) if extent==6 else ((10,),320)


def pack(folder, dest,extent):
    sides,count=design(extent)
    with ZipFile(dest,"w") as z:
        for n in sides:
            for name in names(n,extent):
                data=(folder/(name+".bin")).read_bytes()
                assert len(data)==count*2*3*3*8
                entry=ZipInfo(name+".bin",(2026,11,23,0,0,0))
                entry.compress_type=ZIP_DEFLATED
                z.writestr(entry,data)


def stats(streams):
    raw,mean,j=np.moveaxis(np.concatenate(streams),-1,0)
    f=raw-raw.mean()
    m=mean-mean.mean()
    v=np.mean(f*f)
    vm=np.mean(m*m)
    h=np.mean(f[:,0]*f[:,1])
    hm=np.mean(m[:,0]*m[:,1])
    return np.array([v,vm,j.mean(),v-vm-j.mean(),h-hm])


def jackknife(rows,fn):
    full=fn(rows)
    dropped=np.stack([fn(rows[:i]+rows[i+1:]) for i in range(len(rows))])
    se=np.sqrt((len(rows)-1)*np.mean((dropped-dropped.mean(axis=0))**2,axis=0))
    return full,se


def lag_diagnostics(rows):
    # Long contiguous batches provide a separate sensitivity check on the stream errors.
    f,m,_=np.moveaxis(np.stack(rows),-1,0)
    f=f-f.mean()
    m=m-m.mean()
    diff=(f[:,:,0]*f[:,:,1]-m[:,:,0]*m[:,:,1]).mean(axis=-1)
    for width in (20,40):
        blocks=diff.reshape(len(rows),-1,width).mean(axis=-1)
        se=np.sqrt(blocks.var(axis=1,ddof=1).sum()/blocks.shape[1])/len(rows)
        print("  lag difference: batch size, SE",width,f"{se:.6f}")
    print("  lag difference: stream values",np.round(diff.mean(axis=1),6))


def read(archive,extent):
    sides,count=design(extent)
    prior_path=ROOT.parent/f"plaquette-covariance/spectra{extent}.npz"
    with ZipFile(archive) as z,np.load(prior_path,allow_pickle=False) as prior:
        expected=[key+".bin" for n in sides for key in names(n,extent)]
        assert sorted(z.namelist())==sorted(expected)
        for n in sides:
            rows=[]
            for name in names(n,extent):
                a=np.frombuffer(z.read(name+".bin"),"<f8").reshape(count,2,3,3)
                assert np.isfinite(a).all() and (a[...,2]>=0).all()
                np.testing.assert_allclose(a[...,0],prior[name+"_zero"][:count,...,0],
                                           rtol=0,atol=3e-12)
                rows.append(a)
            val,err=jackknife(rows,stats)
            print(n, " ".join(f"{v:.6f}({e:.6f})" for v,e in zip(val,err)))
            lag_diagnostics(rows)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--pack",type=Path)
    ap.add_argument("--archive",type=Path)
    ap.add_argument("--extent",type=int,choices=(6,10),default=6)
    args=ap.parse_args()
    dest=args.archive or ROOT/f"streams{args.extent}.zip"
    if args.pack:
        pack(args.pack,dest,args.extent)
    read(dest,args.extent)
