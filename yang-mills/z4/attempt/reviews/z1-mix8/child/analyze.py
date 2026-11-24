"""analyze.py file: pooled plug-in Var, J, J/Var (f1,f4), spread; error by jackknife over blocks of 50 consecutive samples within stream."""
import sys, numpy as np
fn=sys.argv[1]; rows=[l.strip().split(',') for l in open(fn) if not l.startswith('#')]
a=np.array(rows,float); st=a[:,0]
f1,f4,sp,j1,j4=a[:,2],a[:,3],a[:,4],a[:,5],a[:,6]
B=50; blocks=np.concatenate([np.arange(len(a[st==s]))//B+1000*s for s in np.unique(st)]).astype(int)
ids=np.unique(blocks)
def stat(m):
    return [j1[m].mean()/f1[m].var(), j4[m].mean()/f4[m].var(), f1[m].var(), f4[m].var(), j1[m].mean(), j4[m].mean(), sp[m].mean()]
full=np.array(stat(np.ones(len(a),bool)))
jk=np.array([stat(blocks!=b) for b in ids]); n=len(ids)
se=np.sqrt((n-1)/n*((jk-jk.mean(0))**2).sum(0))
for nm,v,e in zip(['J1/Var1','J4/Var4','Var f1','Var f4','J1','J4','spread'],full,se): print(f"{nm}: {v:.5f} +- {e:.5f}")
print("N samples",len(a),"blocks",n, "mean f1,f4",f1.mean(),f4.mean())
