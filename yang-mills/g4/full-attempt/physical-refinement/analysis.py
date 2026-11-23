"""Reduce matched.rs little-endian time slices or SF derivatives. Requires NumPy."""
import argparse
import csv
import io
import math
from pathlib import Path
import sys
from zipfile import ZipFile

import numpy as np
from calibration import TABLE, tune

ROOT = Path(__file__).resolve().parent
PROBES = ("E_wind","E_local","T2_wind","T2_local")
PAIRS = tuple((v,v) for v in PROBES)+(("E_wind","E_local"),("T2_wind","T2_local"))
SLICES = {p:slice(2+3*i,5+3*i) for i,p in enumerate(PROBES)}
TIMES = (0.,0.25,0.5,0.75,1.,1.25,1.5,2.)

def read_streams(path, incomplete=False):
    zipfile = None if path.is_dir() else ZipFile(path)
    names = sorted(p.name for p in path.glob("*.bin")) if zipfile is None else sorted(zipfile.namelist())
    by = {}
    try:
        for name in names:
            mode,ns,ts,bs,seed,hot,burn,count,stride = Path(name).stem.split("_")
            if mode=="modes":continue
            n,t,hot,burn,count,stride=map(int,(ns,ts,hot,burn,count,stride))
            assert abs(float(bs)-tune(TABLE[n])) < 1e-9
            raw=(path/name).read_bytes() if zipfile is None else zipfile.read(name)
            shape=(count,) if mode=="sf" else (count,t+1,14)
            dtype="<f8" if mode=="sf" else "<f4"
            if incomplete and len(raw)!=math.prod(shape)*np.dtype(dtype).itemsize:continue
            a=np.frombuffer(raw,dtype=dtype).reshape(shape).astype(float)
            assert np.isfinite(a).all()
            if mode=="sf":
                phase="scale" if count==1024 else "scale_pilot"
            elif mode=="smooth":
                phase="smoothed"
            else:
                phase="boundary" if t==8*n else ("pilot" if burn==112 else "production")
            by.setdefault((n,phase),(t,[]))[1].append((hot,int(seed),a))
    finally:
        if zipfile: zipfile.close()
    return by

def corr(a,b,k):
    size=a.shape[1]-k
    forward=(a[:,:size]*b[:,k:]).mean(axis=(1,2))
    backward=(b[:,:size]*a[:,k:]).mean(axis=(1,2))
    return (forward+backward)/2

def sample_values(a,n,t,margin):
    middle=a[:,margin*n:t+1-margin*n]
    out={"plaq":middle[:,:,0].mean(axis=1),"adj":middle[:,:,1].mean(axis=1)}
    for p,q in PAIRS:
        x,y=middle[:,:,SLICES[p]],middle[:,:,SLICES[q]]
        pair=p if p==q else p+"*"+q
        for tau in TIMES:
            s=n*tau
            lo=int(s)
            v=corr(x,y,lo)
            if s>lo:v=(1-(s-lo))*v+(s-lo)*corr(x,y,lo+1)
            out[pair,tau]=v
    return out

def estimates(data,calc):
    """Vectorized nonlinear estimates, with delete-one contiguous blocks or whole streams."""
    a=np.array(data)             # stream, sample, sufficient statistic
    assert a.ndim==3
    m,n,d=a.shape
    center=a.mean(axis=(0,1))
    value=float(calc(center))
    if not math.isfinite(value):return (math.nan,math.nan)
    errors=[]
    for block in (8,16,32):
        if n%block or n//block<3:continue
        grouped=a.reshape(m,n//block,block,d).mean(axis=2).reshape(-1,d)
        b=len(grouped)
        reps=calc((b*center-grouped)/(b-1))
        if not np.isfinite(reps).all():return value,math.nan
        errors.append(float(reps.std(ddof=0)*math.sqrt(b-1)))
    if m>1:
        reps=calc((m*center-a.mean(axis=1))/(m-1))
        if not np.isfinite(reps).all():return value,math.nan
        errors.append(float(reps.std(ddof=0)*math.sqrt(m-1)))
    return value,max(errors,default=math.nan)

def plaquette_stats(selected,n,t,margin):
    profiles=[a[:,margin*n:t+1-margin*n,0] for _,_,a in selected]
    length=profiles[0].shape[1]
    def make(k):
        return [np.column_stack(((x[:,:length-k]*x[:,k:]).mean(axis=1),x)) for x in profiles]
    def connected(vec,k):
        m=vec[...,1:]
        return vec[...,0]-(m[...,:length-k]*m[...,k:]).mean(axis=-1)
    contact=make(0)
    split=length+1
    for label,k in (("0",0),("one_step",1),("1.0",n)):
        arrays=make(k)
        yield "connected","plaq_cell",label,*estimates(arrays,lambda v:connected(v,k))
        if k:
            joint=[np.column_stack((x,y)) for x,y in zip(arrays,contact)]
            yield "ratio","plaq_cell",label,*estimates(joint,lambda v:connected(v[...,:split],k)/connected(v[...,split:],0))

def rows(path,incomplete=False):
    for (n,phase),(t,streams) in sorted(read_streams(path,incomplete).items()):
        groups=[("all",streams)]
        if len(streams)>1:
            groups += [(tag,[s for s in streams if s[0]==i]) for i,tag in enumerate(("cold","hot"))]
        for group,selected in groups:
            if not selected:continue
            prefix=(n,phase,t,group,len(selected),len(selected[0][2]))
            if phase.startswith("scale"):
                norm=-24*n*n*math.sin(math.pi/(2*n*n))
                x=[a[:,None] for _,_,a in selected]
                for key,f in [("derivative",lambda u:u[...,0]),("coupling",lambda u:norm/u[...,0])]:
                    yield (*prefix,0,key,"SF","",*estimates(x,f))
                continue
            for margin in (1,2):
                samples=[sample_values(a,n,t,margin) for _,_,a in selected]
                def metric(keys,calc):
                    return estimates([np.stack([s[k] for k in keys],axis=-1) for s in samples],calc)
                for key in ("plaq","adj"):
                    yield (*prefix,margin,"mean",key,"",*metric([key],lambda u:u[...,0]))
                for row in plaquette_stats(selected,n,t,margin):yield (*prefix,margin,*row)
                for p,q in PAIRS:
                    pair=p if p==q else p+"*"+q
                    for tau in TIMES:
                        val=metric([(pair,tau)],lambda u:u[...,0])
                        yield (*prefix,margin,"cov",pair,tau,*val)
                        if p==q and tau>0:
                            val=metric([(p,tau),(p,0.)],lambda u:u[...,0]/u[...,1])
                            yield (*prefix,margin,"ratio",p,tau,*val)
                    if p!=q:continue
                    for start,end in [(0.25,0.5),(0.5,1.),(1.,1.5),(1.,2.)]:
                        def logratio(u):
                            with np.errstate(divide="ignore",invalid="ignore"):
                                return (np.log(u[...,0])-np.log(u[...,1]))/(end-start)
                        val=metric([(p,start),(p,end)],logratio)
                        yield (*prefix,margin,"eff",p,f"{start}-{end}",*val)

HEADER=("N","phase","T","starts","streams","samples_per_stream","margin_L","stat","probe","tau_over_L","value","se")
def write(path,out,incomplete=False):
    w=csv.writer(out,lineterminator="\n")
    w.writerow(HEADER)
    for *keys,v,se in rows(path,incomplete):
        w.writerow([*keys,f"{v:.11g}",f"{se:.8g}"])

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("data",type=Path,nargs="?",default=ROOT/"samples.zip")
    parser.add_argument("--partial",action="store_true")
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    if args.output:
        with args.output.open("w",newline="",encoding="utf8") as f:write(args.data,f,args.partial)
    else:write(args.data,sys.stdout,args.partial)
