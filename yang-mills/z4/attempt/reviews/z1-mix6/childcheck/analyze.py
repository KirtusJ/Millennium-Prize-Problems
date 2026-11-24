"""Delete-one-stream jackknife. Usage: analyze.py DIR"""
import json,sys,numpy as np
d=sys.argv[1]; S=[json.load(open(f"{d}/stream{s}.json")) for s in range(4)]
R=[np.array(s['rec']) for s in S]  # cols f1,f4,spread,J1,J4
def stats(idx):
    A=np.concatenate([R[i] for i in idx]); v1=A[:,0].var(); v4=A[:,1].var()
    return np.array([A[:,2].mean(),v4,v1,A[:,3].mean()/v1,A[:,4].mean()/v4,A[:,3].mean(),A[:,4].mean()])
full=stats(range(4)); jk=np.array([stats([i for i in range(4) if i!=k]) for k in range(4)])
se=np.sqrt(3/4*((jk-jk.mean(0))**2).sum(0))
ref={'spread':(.3442,.0084),'Var4':(.06182,.00732),'JV1':(.0639,.0023),'JV4':(.0464,.0055)}
names=['spread','Var(f4)','Var(f1)','J/Var f1','J/Var f4','J f1','J f4']
for n,a,b in zip(names,full,se): print(f"{n:9s} {a:.5f} +- {b:.5f}")
for key,i in [('spread',0),('Var4',1),('JV1',3),('JV4',4)]:
    r,rs=ref[key]; z=(full[i]-r)/np.hypot(se[i],rs); print(key,'ref',r,rs,'z=%.2f'%z,'AGREE' if abs(z)<=2 else 'FAIL')
for s,r in zip(S,R): print('stream',s['stream'],'hot' if s['hot'] else 'cold','means f1,f4,spread,J1,J4',np.round(r.mean(0),5))
print('structure_ok',S[0]['structure_ok'])
