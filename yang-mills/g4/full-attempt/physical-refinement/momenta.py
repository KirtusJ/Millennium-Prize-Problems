"""Spatial trial readings. Compute zero, first, and second axial Fourier shells."""
import csv
import math
from pathlib import Path
import sys
from zipfile import ZipFile

import numpy as np
from analysis import estimates
from calibration import tune,TABLE

def grouped(path):
    z=None if path.is_dir() else ZipFile(path)
    by={}
    try:
        names=sorted(p.name for p in path.glob("modes_*.bin")) if z is None else sorted(n for n in z.namelist() if n.startswith("modes_"))
        for name in names:
            _,n,t,beta,seed,hot,burn,count,stride=Path(name).stem.split("_")
            n,t,count=int(n),int(t),int(count)
            raw=(path/name).read_bytes() if z is None else z.read(name)
            assert abs(float(beta)-tune(TABLE[n]))<1e-9 and t==6*n
            a=np.frombuffer(raw,dtype="<f4").reshape(count,t+1,26).astype(float)
            by.setdefault(n,[]).append(a[:,n:t+1-n])
    finally:
        if z:z.close()
    return by

def terms(x,k,zero):
    width=x.shape[1]
    # Sum cosine/sine contributions, then average over the 3 axial directions.
    v=(x[:,:width-k]*x[:,k:]).sum(axis=2).mean(axis=1)
    if zero:return np.column_stack((v,x[:,:,0]))
    return v[:,None]/3

def statistic(data,real_lag,zero):
    """One estimate with its profile subtraction inside all jackknife replicates."""
    width=data[0].shape[1]
    lo=int(real_lag)
    frac=real_lag-lo
    hi=lo+int(frac>0)
    block=1+width if zero else 1
    samples=[np.hstack([terms(x,k,zero) for k in (lo,hi,0)]) for x in data]
    def cov(v,k):
        if not zero:return v[...,0]
        m=v[...,1:]
        return v[...,0]-(m[...,:width-k]*m[...,k:]).mean(axis=-1)
    def value(v):
        return (1-frac)*cov(v[...,:block],lo)+frac*cov(v[...,block:2*block],hi)
    return (estimates(samples,value),
            estimates(samples,lambda v:value(v)/cov(v[...,2*block:],0)))

def write(path,out):
    w=csv.writer(out,lineterminator="\n")
    w.writerow(("N","probe","pL_over_2pi","lag","covariance","cov_se","ratio","ratio_se"))
    for n,streams in sorted(grouped(path).items()):
        for i,label in enumerate(("cell","quarter_box")):
            start=13*i
            for shell in range(3):
                sl=slice(start,start+1) if shell==0 else slice(start+1+(shell-1)*6,start+1+shell*6)
                data=[a[:,:,sl] for a in streams]
                for lag,k in (("zero",0),("one_step",1),("quarter_L",n/4),("half_L",n/2),("one_L",n)):
                    (c,e),(r,se)=statistic(data,k,shell==0)
                    w.writerow([n,label,shell,lag,*(f"{v:.10g}" for v in (c,e,r,se))])

if __name__=="__main__":
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name("samples.zip")
    write(path,sys.stdout)
