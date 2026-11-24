"""T233 reduction. Predicates fixed before first run:
 P1: |z| <= 2 for r1 and r4 in each directory (z = (r_hot-r_cold)/(2*err(r_pooled))).
 P2: |d| <= 2 for r1 and r4 in each directory (first vs last 576 rows).
 P3: meta hot flag (args token 4) == stream ID parity for all 64 streams.
Tolerances: 2 = conventional 2-sigma, taken from the task statement. Nothing else is a tolerance.
Hypothesis checks for 'for all': P3 is counted per stream (n matching of 64).
Output file opened mode 'x' (never overwritten). Pure numpy, no randomness (no seed needed).
"""
import numpy as np, sys, json, math
R="/home/user/z4-workers/e2-repair/results/"
def load(d):
    S=[];hot=[]
    for i in range(32):
        a=np.loadtxt(f"{R}{d}/s{i}.csv",delimiter=",",skiprows=1)
        S.append(a)
        for l in open(f"{R}{d}/s{i}.meta.txt"):
            if l.startswith("args"): hot.append(int(l.split()[4])); break
    return S,hot
def stat(blocks,ci,cj):  # blocks: list of arrays; returns J,Var,r
    x=np.concatenate([b[:,ci] for b in blocks]); j=np.concatenate([b[:,cj] for b in blocks])
    v=x.var(); J=j.mean(); return J,v,J/v
def jack(blocks,ci,cj,k):
    n=len(blocks); xs=[stat(blocks[:m]+blocks[m+1:],ci,cj)[k] for m in range(n)]
    xs=np.array(xs); return math.sqrt((n-1)/n*((xs-xs.mean())**2).sum())
# jackknife for r on subset-of-streams: n = len(blocks) (32 pooled; 16 for strata not needed)
def r_err(blocks,ci,cj):
    return stat(blocks,ci,cj)[2], jack(blocks,ci,cj,2)
out=open("results_run3.json","x"); res={}
cols={"1":(0,3),"4":(1,4)}
for d in ["N-d2","N-d0"]:
    S,hot=load(d); o={}
    par=[i%2 for i in range(32)]
    o["meta_match"]=sum(h==p for h,p in zip(hot,par)); o["rows"]=sorted(set(len(s) for s in S))
    for t,(ci,cj) in cols.items():
        J,V,r=stat(S,ci,cj)
        o["J"+t]=[J,jack(S,ci,cj,0)]; o["Var"+t]=[V,jack(S,ci,cj,1)]; o["r"+t]=[r,jack(S,ci,cj,2)]
        H=[S[i] for i in range(1,32,2)]; C=[S[i] for i in range(0,32,2)]
        rh=stat(H,ci,cj)[2]; rc=stat(C,ci,cj)[2]
        o["z"+t]=(rh-rc)/(2*o["r"+t][1]); o["rhot"+t]=rh; o["rcold"+t]=rc
        F=[s[:576] for s in S]; L=[s[576:] for s in S]
        rf,ef=r_err(F,ci,cj); rl,el=r_err(L,ci,cj)
        o["d"+t]=(rl-rf)/math.sqrt(ef**2+el**2); o["rfirst"+t]=[rf,ef]; o["rlast"+t]=[rl,el]
    res[d]=o
for t in "14":
    a=res["N-d2"]["r"+t]; b=res["N-d0"]["r"+t]; Q=a[0]/b[0]
    res["Q"+t]=[Q,Q*math.sqrt((a[1]/a[0])**2+(b[1]/b[0])**2)]
# predicate summary
res["pred"]={"P1":{d+t:bool(abs(res[d]["z"+t])<=2) for d in ["N-d2","N-d0"] for t in "14"},
 "P2":{d+t:bool(abs(res[d]["d"+t])<=2) for d in ["N-d2","N-d0"] for t in "14"},
 "P3_matches_of_64":res["N-d2"]["meta_match"]+res["N-d0"]["meta_match"]}
json.dump(res,out,indent=1); out.close(); print(json.dumps(res,indent=1))
