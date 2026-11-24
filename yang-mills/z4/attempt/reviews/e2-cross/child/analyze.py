"""Predicates (fixed before first run):
P1 each file ends with END; P2 8 held-out chains (i%4 in {2,3}) per ensemble;
P3 NS>0 and Var(f)>0 for every test; P4 R finite; P5 jackknife n=8;
P6 control: pooled R of x=1,2,3,4 periodic formula equals 1.2 within 1e-12 (float rounding).
Tolerance 1e-12 = double precision rounding on O(1) numbers.
Usage: analyze.py ENS [ENS...]; output file opened with mode x, named results-<ENS>.txt"""
import sys, numpy as np
D="/home/user/z4-workers/e2-cross/results/"
tests={"t1":{0:1/3,1:1/3,2:1/3},"t2":{3:1/3,4:1/3,5:1/3},"t3":{10:1},"t4":{3:1,4:-1}}
def load(ens,i):
    L=open(f"{D}{ens}/chain-{i}.txt").read().split("\n")
    assert L[-1]=="END" or (L[-1]=="" and L[-2]=="END"),"no END"
    S00=np.zeros((16,16));SL=np.zeros((16,16))
    for l in L:
        p=l.split(",")
        if p[0]=="NS":ns=float(p[1])
        elif p[0]=="S1":s1=np.array(p[1:],float)
        elif p[0]=="S00":S00[int(p[1])]=np.array(p[2:],float)
        elif p[0]=="SL":SL[int(p[1])]=np.array(p[2:],float)
    return ns,s1,S00,SL
def R(ch,a):
    ns=sum(c[0] for c in ch);mu=sum(c[1] for c in ch)/ns
    C0=sum(c[2] for c in ch)/ns-np.outer(mu,mu);CL=sum(c[3] for c in ch)/ns-np.outer(mu,mu)
    CLs=(CL+CL.T)/2;v=a@C0@a
    assert ns>0 and v>0
    r=1-a@CLs@a/v;assert np.isfinite(r);return r,v
x=np.array([1,2,3,4.]);d=x-x.mean();c0=(d*d).mean();c1=(d*np.roll(d,-1)).mean()
assert abs(1-c1/c0-1.2)<1e-12
res={}
for ens in sys.argv[1:]:
    held=[i for i in range(16) if i%4 in(2,3)];assert len(held)==8
    ch=[load(ens,i) for i in held];out=[]
    for t,c in tests.items():
        a=np.zeros(16)
        for k,v in c.items():a[k]=v
        r,v=R(ch,a);rs=np.array([R(ch[:k]+ch[k+1:],a)[0] for k in range(8)])
        se=np.sqrt(7/8*((rs-rs.mean())**2).sum());res[(ens,t)]=r
        out.append(f"{ens} {t} R={r:.6f} SE={se:.6f} Var={v:.6g}")
    with open(f"results-{ens}.txt","x") as f:f.write("\n".join(out)+"\n")
    print("\n".join(out))
