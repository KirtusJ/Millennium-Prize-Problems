"""T242 analysis. Predicates fixed BEFORE first run (tolerances in brackets, with source):
 P1 every (class,vector) Var>0 for pooled and all 8 leave-one-out sets  [exact, Var is a variance of counts]
 P2 jackknife SE finite and >0 for every R and for lambda2               [exact]
 P3 J_sym symmetric, row sums>0; top eigenvalue of M == 1 within 1e-9    [M has eigvec sqrt(v) with eigenvalue 1; 1e-9 ~ float64 eigh error]
 P4 V4 has exactly one |eig|<1e-9*max, its eigvec ~ (1,1,1,1)/2 within 1e-9  [stated in task; float64]
 P5 Csym symmetric to 1e-12, pooled NS sums to the expected totals          [float64]
 P6 (measured only, no a-priori expectation) |lambda2 - (1-minR)| reported; threshold 1e-6 as asked.
 P7 control: R for x=1..5 lag 2 == 1.5 (control.txt)
Result file results.json opened mode 'x' (never overwritten). No randomness.
"""
import numpy as np, json, glob, re, sys
ids=[2,3,6,7,10,11,14,15]
def load(i):
    d={}
    for ln in open(f'data/chain-{i}.txt'):
        p=ln.strip().split(',')
        k=p[0]
        if k in('LNS','ZNS'): d[k]=float(p[1])
        elif k in('LS1','ZS1'): d[k]=np.array(p[1:],float)
        elif k in('LS00','ZS00','LSL','ZSL'):
            d.setdefault(k,np.zeros((54,54)))[int(p[1])]=np.array(p[2:],float)
        elif k=='J': d.setdefault('J',np.zeros((4,4)))[int(p[1])]=np.array(p[2:],float)
    return d
D={i:load(i) for i in ids}
preds={}
def pool(S,c):
    N=sum(D[i][c+'NS'] for i in S); s1=sum(D[i][c+'S1'] for i in S)
    s0=sum(D[i][c+'S00'] for i in S); sl=sum(D[i][c+'SL'] for i in S)
    mu=s1/N; C0=s0/N-np.outer(mu,mu); CL=sl/N-np.outer(mu,mu)
    return N,C0,CL,(CL+CL.T)/2
aW=np.zeros(54);aW[0:3]=1; aP=np.zeros(54);aP[3:6]=1
def R(S,c,a):
    N,C0,CL,Cs=pool(S,c); V=a@C0@a; E=a@(C0-Cs)@a; return E/V,V
def jk(vals):
    v=np.array(vals);return float(np.sqrt(7/8*((v-v.mean())**2).sum()))
res={'control':float(open('control.txt').read())}
P1=True;out={}
for c in 'LZ':
    for nm,a in(('W',aW),('P',aP)):
        r,V=R(ids,c,a); P1&=V>0
        loo=[]
        for j in ids:
            rr,VV=R([i for i in ids if i!=j],c,a);P1&=VV>0;loo.append(rr)
        out[f'{c}_{nm}']=(r,jk(loo),loo)
res['R']=out
preds['P1']=bool(P1)
def lam2(S):
    J=sum(D[i]['J'] for i in S);Js=(J+J.T)/2;v=Js.sum(1)
    M=Js/np.sqrt(np.outer(v,v));w=np.linalg.eigvalsh(M);return w,Js,v,M
w,Js,v,M=lam2(ids); l2=w[-2]
loo=[lam2([i for i in ids if i!=j])[0][-2] for j in ids]
res['lambda2']=(float(l2),jk(loo),[float(x) for x in loo]); res['eigs']=[float(x) for x in w]
preds['P3']=bool((v>0).all() and abs(w[-1]-1)<1e-9 and np.allclose(Js,Js.T))
allse=[o[1] for o in out.values()]+[jk(loo)]
preds['P2']=bool(all(np.isfinite(allse)) and all(s>0 for s in allse))
N,C0,CL,Cs=pool(ids,'L')
preds['P5']=bool(np.abs(Cs-Cs.T).max()<1e-12 and N==sum(D[i]['LNS'] for i in ids))
Dm=C0-Cs
idx=lambda mu,b:42+4*mu+b
E4=np.zeros((4,4));V4=np.zeros((4,4))
for m1 in range(3):
  for m2 in range(3):
    for b in range(4):
      for b2 in range(4):
        E4[b,b2]+=Dm[idx(m1,b),idx(m2,b2)];V4[b,b2]+=C0[idx(m1,b),idx(m2,b2)]
E4=(E4+E4.T)/2;V4=(V4+V4.T)/2
ev,U=np.linalg.eigh(V4); res['V4eig']=[float(x) for x in ev]
null=U[:,0]; preds['P4']=bool(abs(ev[0])<1e-9*ev[-1] and ev[1]>1e-9*ev[-1] and np.allclose(abs(null),0.5,atol=1e-9))
Q=U[:,1:]  # orthonormal basis of complement of null
g=np.linalg.eigvals(np.linalg.solve(Q.T@V4@Q,Q.T@E4@Q)).real
minR=float(g.min()); res['minR4']=minR; res['gen_eigs']=sorted(float(x) for x in g)
res['one_minus_lambda2']=float(1-l2); res['diff']=float(abs((1-l2)-minR))
preds['P6_measured_only_diff_le_1e-6']=bool(res['diff']<=1e-6)
preds['P7']=abs(res['control']-1.5)<1e-9
res['preds']=preds
json.dump(res,open('results.json','x'),indent=1)
print(json.dumps(res,indent=1))
