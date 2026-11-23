"""Applies predicates fixed in run_beta.py docstring (A,B,C,D) to results_beta*_v2.json. Writes analysis.json (mode x)."""
import json, numpy as np
Bs=[64,256,1024,4096]
R={b:json.load(open('results_beta%d_v2.json'%b)) for b in Bs}
c=R[64]['cstar']; out={}
def fit(vals,bs):
    bs=bs[-3:];v=vals[-3:]
    A=np.array([[1,np.log(b)/b**.5,1/b**.5] for b in bs]);return np.linalg.solve(A,np.array(v))
r=[R[b]['r'] for b in Bs]; q=[R[b]['q'] for b in Bs]
out['r']=r; out['q']=q
out['A_closer_to_c']=all(abs(x-c)<abs(x-2*c) for x in r)
dev=[abs(x-c) for x in r]; out['A_monotone']=all(dev[i+1]<=dev[i] for i in range(3)); out['A_dev']=dev
fa=fit(r,Bs); out['A_fit']=list(fa); out['A_fit_ok']=abs(fa[0]-c)/c<0.03
out['B_closer_to_half']=all(abs(x-c/2)<abs(x-c) for x in q)
fb=fit(q,Bs); out['B_fit']=list(fb); out['B_fit_ok']=abs(fb[0]-c/2)/(c/2)<0.03
out['B_dev']=[abs(x-c/2) for x in q]
out['C']={b:dict(minS=R[b]['c_minS'],minW=R[b]['c_minW'],kink=R[b]['c_kink']) for b in Bs}
out['C_nqualS']=sum(R[b]['c_minS']>=1-1e-9 for b in Bs); out['C_nqualW']=sum(R[b]['c_minW']>=1-1e-9 for b in Bs); out['C_nqualK']=sum(R[b]['c_kink']>=1-1e-9 for b in Bs)
out['D_rel']=[abs(2*qq-rr)/rr for qq,rr in zip(q,r)]; out['D_ok']=out['D_rel'][-1]<=0.10
out['D_2q_over_r']=[2*qq/rr for qq,rr in zip(q,r)]
import sys
out={k:(bool(v) if isinstance(v,np.bool_) else v) for k,v in out.items()}
s=json.dumps(out,indent=1,default=bool); open('analysis.json','x').write(s); print(s)
