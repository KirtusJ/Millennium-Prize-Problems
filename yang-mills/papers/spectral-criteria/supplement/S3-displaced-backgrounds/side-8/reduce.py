"""Reduction for z1-mix8 runs.  Usage: python3 reduce.py <label> <csv files...>

Estimator (same as G4 fixed.py): pool all rows of all streams; Var = plug-in variance
(numpy var, ddof=0) of the test; J = mean of j column; ratio = J/Var. Errors: delete-one-stream
jackknife, err = sqrt((S-1)/S * sum (drop - mean drop)^2) (for S=4 this equals G4's sqrt(3*mean(...))).
Per-colour J_k = mean over rows of c<k>; J = mean_k J_k exactly (checked).
Predicates (fixed before the first run):
T1 thermalisation: four-face ratio of hot-start streams and of cold-start streams (each pooled
   within its stratum, jackknife over its streams) agree: |r_hot - r_cold| <= 2*sqrt(e_hot^2+e_cold^2).
   Tolerance source: 2 sigma of the stream-jackknife errors (crude with 4 streams per stratum).
T1b same for the variance of the four-face mark.
S1 number of streams >= 4 (here 8 are used: 4 hot, 4 cold).
Output: JSON summary printed to stdout (caller stores it with mode "x").
"""
import sys, json, numpy as np
def load(p):
    with open(p) as f: head=f.readline().strip().split(",")
    a=np.loadtxt(p,delimiter=",",skiprows=1,ndmin=2); return head,a
def est(rows,cols):
    d=np.concatenate(rows); h=cols
    s,av,sp,j1,j4=[d[:,h.index(c)] for c in ("single","average","spread","j_single","j_average")]
    v1,v4=s.var(),av.var(); J1,J4=j1.mean(),j4.mean()
    out=[sp.mean(),v1,v4,J1,J4,J1/v1,J4/v4]
    if "j_single_raw" in h:
        sr,ar,jr1,jr4=[d[:,h.index(c)] for c in ("single_raw","average_raw","j_single_raw","j_average_raw")]
        out+=[jr1.mean()/sr.var(),jr4.mean()/ar.var()]
    return np.array(out)
NAMES=["spread","var_single","var_average","J_single","J_average","ratio_single","ratio_average","ratio_single_rawB","ratio_average_rawB"]
def jack(rows,cols):
    full=est(rows,cols); S=len(rows)
    drops=np.stack([est(rows[:i]+rows[i+1:],cols) for i in range(S)])
    err=np.sqrt((S-1)/S*np.sum((drops-drops.mean(0))**2,axis=0))
    return full,err
def main():
    label=sys.argv[1]; files=sys.argv[2:]
    rows=[];cols=None
    for p in files:
        h,a=load(p); cols=h if cols is None else cols; assert h==cols; rows.append(a)
    full,err=jack(rows,cols)
    res={"label":label,"files":files,"n_streams":len(rows),"rows_per_stream":[len(r) for r in rows]}
    res["estimates"]={n:[float(v),float(e)] for n,v,e in zip(NAMES,full,err)}
    per=[]
    for p,r in zip(files,rows):
        e=est([r],cols); per.append({"file":p,**{n:float(v) for n,v in zip(NAMES,e)},"mean_single":float(r[:,0].mean()),"mean_average":float(r[:,1].mean())})
    res["per_stream"]=per
    hot=[r for p,r in zip(files,rows) if "-hot" in p]; cold=[r for p,r in zip(files,rows) if "-cold" in p]
    if len(hot)>=2 and len(cold)>=2:
        fh,eh=jack(hot,cols); fc,ec=jack(cold,cols)
        res["hot"]={n:[float(v),float(e)] for n,v,e in zip(NAMES,fh,eh)}
        res["cold"]={n:[float(v),float(e)] for n,v,e in zip(NAMES,fc,ec)}
        i=NAMES.index("ratio_average"); k=NAMES.index("var_average")
        res["T1_ratio_hot_cold"]="MET" if abs(fh[i]-fc[i])<=2*np.hypot(eh[i],ec[i]) else "FAILED"
        res["T1b_var_hot_cold"]="MET" if abs(fh[k]-fc[k])<=2*np.hypot(eh[k],ec[k]) else "FAILED"
    res["S1_streams_ge_4"]="MET" if len(rows)>=4 else "FAILED"
    if "c0_single" in cols:
        d=np.concatenate(rows); pc={}
        for t in ("single","average"):
            m=np.array([d[:,cols.index(f"c{k}_{t}")].mean() for k in range(24)])
            ser=np.array([[r[:,cols.index(f"c{k}_{t}")].mean() for k in range(24)] for r in rows])
            jj=d[:,cols.index(f"j_{t}")].mean()
            assert abs(m.mean()-jj)<=1e-9*max(1,abs(jj))+1e-11, (m.mean(),jj)
            pc[t]={"J_k":m.tolist(),"stream_sd_of_J_k":ser.std(0,ddof=1).tolist() if len(rows)>1 else None,
                   "fraction_of_sum":(m/m.sum()).tolist()}
        res["per_colour"]=pc
    print(json.dumps(res,indent=1))
if __name__=="__main__": main()
