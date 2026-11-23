"""Analysis. Usage: python3 analyze.py <resultjson> <outjson>. Predicates P1,P2 (beta=0) or P4-P8 (beta=2) as in mc3.py docstring."""
import sys, json, numpy as np
d=json.load(open(sys.argv[1])); sO=np.array(d['sO']); sOO=np.array(d['sOO']); R=d['R']; beta=d['beta']
def jk(f):
    full=f(np.arange(R)); vals=np.array([f(np.delete(np.arange(R),r)) for r in range(R)])
    return full, np.sqrt((R-1)/R*((vals-vals.mean(0))**2).sum(0))
def C(idx,a,b):
    m=sO[idx].mean(0); c=sOO[idx].mean(0)
    return np.array([c[a,b,t]-m[a]*m[b] for t in range(sOO.shape[-1])])
res={'beta':beta,'acc':d['acc']}; pred={}
if beta==0:
    v,s=jk(lambda i: sO[i,2].mean()/3); pred['P1']=(abs(v-0.25)<5*s, v, s)
    v,s=jk(lambda i: C(i,2,2)[1]); pred['P2']=(abs(v)<5*s, v, s)
else:
    CAA=lambda i:C(i,0,0); CBB=lambda i:C(i,1,1)
    c2=lambda i:(C(i,0,0)+C(i,1,1))/2
    v,s=jk(c2); res['C2']=v.tolist(); res['C2err']=s.tolist()
    v,s=jk(lambda i:C(i,2,2)); res['CS']=v.tolist(); res['CSerr']=s.tolist()
    v,s=jk(lambda i:C(i,0,0)[1:4]); pred['P4']=(bool((v>0).all()),v.tolist(),s.tolist())
    mm=lambda c,t:np.log(c[t]/c[t+1])
    for nm,f in (('A',CAA),('B',CBB),('2f',c2),('S',lambda i:C(i,2,2))):
        v,s=jk(lambda i:np.array([mm(f(i),t) for t in range(1,6)])); res['m_'+nm]=v.tolist(); res['m_'+nm+'_err']=s.tolist()
    ok=True;det=[]
    for t in (1,2):
        v,s=jk(lambda i:mm(CAA(i),t)-mm(CBB(i),t)); ok&=abs(v)<3*s; det.append((float(v),float(s)))
    pred['P5']=(bool(ok),det)
    v,s=jk(lambda i:C(i,0,1)[1]); pred['P6']=(bool(abs(v)<3*s),float(v),float(s))
    pl=None
    for t in (1,2,3):
        v,s=jk(lambda i:mm(c2(i),t)-mm(c2(i),t+1))
        if abs(v)<2*s: pl=t;break
    pred['P7']=(pl is not None,pl)
    if pl: 
        v,s=jk(lambda i:mm(c2(i),pl)); res['m_e']=float(v); res['m_e_err']=float(s); res['m_e_tau']=pl
    v,s=jk(lambda i:mm(C(i,2,2),2)-mm(c2(i),2)); pred['P8']=(bool(v>2*s),float(v),float(s))
res['pred']={k:[x if not isinstance(x,np.generic) else x.item() for x in (v if isinstance(v,(list,tuple)) else [v])] for k,v in pred.items()}
res['P3_acc_in_0.2_0.8']=bool(0.2<=d['acc']<=0.8)
json.dump(res,open(sys.argv[2],"x"),indent=1); print(json.dumps(res,indent=1))
