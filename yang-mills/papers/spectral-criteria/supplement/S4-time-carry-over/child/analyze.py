"""T227 analysis. Predicates fixed BEFORE first run:
 P1 parse: each stream has sm(3), smm(9), per block sy(308), smy(924), syy(47586); N_s=1152 from header.
 P2 pooled C_YY symmetric (by construction exact) and PSD: min eig >= -1e-10*max eig (same relative
    cutoff as the task's pseudo-inverse threshold; roundoff scale for float64 moments is ~1e-12).
 P3 |rho| <= 1 + 1e-12 (Cauchy-Schwarz; 1e-12 ~ float64 roundoff).
 P4 R2_train in [-1e-9, 1+1e-9] (OLS with intercept, in-sample; slack = roundoff of moment cancellation);
    with truncated pinv it is still a projection-like fit so >=0 expected.
 P5 R2_held <= 1 (+1e-9); may be negative (not a failure).
 P6 jackknife se finite and >0.
 P7 jackknife leave-one-out values all finite.
Conventions: ddof 0; jackknife se = sqrt((n-1)/n * sum (t_i - mean t)^2).
Output files opened mode 'x'. No randomness used (seed n/a).
"""
import numpy as np, json, sys, re
D='data'; NS=32; M=308
w=np.array(open(f'{D}/w.txt').read().split(),float)
assert w.size==M
iu=np.triu_indices(M)
def load(s):
    out={'blocks':{}}
    for line in open(f'{D}/s{s}.mom.txt'):
        if line.startswith('#'):
            if s==0 and 'samples' not in globals(): pass
            mm=re.search(r'samples (\d+)',line)
            if mm: out['N']=int(mm.group(1))
            continue
        t=line.split(); tag=t[0]
        if tag=='sm': out['sm']=np.array(t[1:4],float)[0]; assert len(t)==4
        elif tag=='smm': assert len(t)==10; out['smm']=float(t[1])
        else:
            b=int(t[1]); v=np.array(t[2:],float); d=out['blocks'].setdefault(b,{})
            if tag=='sy': assert v.size==M; d['sy']=v
            elif tag=='smy': assert v.size==3*M; d['smy']=v[:M]
            elif tag=='syy':
                assert v.size==M*(M+1)//2; A=np.zeros((M,M)); A[iu]=v; A=A+A.T-np.diag(np.diag(A)); d['syy']=A
    return out
S=[load(s) for s in range(NS)]
assert all(x['N']==1152 for x in S), 'N header'
fails=[]
def pred(name,ok,info=''):
    print(('PASS ' if ok else 'FAIL ')+name,info)
    if not ok: fails.append((name,info))
def pool(idx,b):
    N=sum(S[s]['N'] for s in idx)
    return dict(N=N,sm=sum(S[s]['sm'] for s in idx),smm=sum(S[s]['smm'] for s in idx),
      sy=sum(S[s]['blocks'][b]['sy'] for s in idx),smy=sum(S[s]['blocks'][b]['smy'] for s in idx),
      syy=sum(S[s]['blocks'][b]['syy'] for s in idx))
def rho_of(p):
    N=p['N']; mm=p['sm']/N; my=p['sy']/N
    cov=w@p['smy']/N-mm*(w@my)
    C=p['syy']/N-np.outer(my,my)
    return cov/np.sqrt((p['smm']/N-mm**2)*(w@C@w))
def fit(p):
    N=p['N']; mm=p['sm']/N; my=p['sy']/N
    C=p['syy']/N-np.outer(my,my); C=(C+C.T)/2
    cym=p['smy']/N-mm*my
    ev,U=np.linalg.eigh(C); keep=ev>1e-10*ev.max()
    beta=U[:,keep]@((U[:,keep].T@cym)/ev[keep])
    a=mm-beta@my
    return a,beta,int((~keep).sum()),ev
def r2(p,a,beta):
    N=p['N']; Em=p['sm']/N; Emm=p['smm']/N; Ey=p['sy']/N; Emy=p['smy']/N; Eyy=p['syy']/N
    E=Emm+a*a+beta@Eyy@beta-2*a*Em-2*beta@Emy+2*a*(beta@Ey)
    return 1-E/(Emm-Em**2)
res={}
for b in (0,1):
    allp=pool(range(NS),b); N=allp['N']
    pred(f'b{b} N=36864',N==32*1152,N)
    my=allp['sy']/N; C=allp['syy']/N-np.outer(my,my)
    ev=np.linalg.eigvalsh((C+C.T)/2)
    pred(f'b{b} C_YY PSD (full pool)',ev.min()>=-1e-10*ev.max(),f'min/max={ev.min()/ev.max():.3e}')
    rho=rho_of(allp)
    pred(f'b{b} |rho|<=1',abs(rho)<=1+1e-12,rho)
    loo=np.array([rho_of(pool([s for s in range(NS) if s!=k],b)) for k in range(NS)])
    se=np.sqrt((NS-1)/NS*((loo-loo.mean())**2).sum())
    pred(f'b{b} rho jackknife finite>0',np.isfinite(loo).all() and se>0,se)
    tr=pool(range(16),b); he=pool(range(16,32),b)
    a,beta,ndisc,evt=fit(tr)
    pred(f'b{b} C_YY(train) PSD',evt.min()>=-1e-10*evt.max(),f'min/max={evt.min()/evt.max():.3e}')
    r2tr=r2(tr,a,beta); r2h=r2(he,a,beta)
    pred(f'b{b} R2_train in [0,1]',-1e-9<=r2tr<=1+1e-9,r2tr)
    pred(f'b{b} R2_held<=1',r2h<=1+1e-9,r2h)
    lo=np.array([r2(pool([s for s in range(16,32) if s!=k],b),a,beta) for k in range(16,32)])
    se2=np.sqrt(15/16*((lo-lo.mean())**2).sum())
    pred(f'b{b} R2_held jackknife finite>0',np.isfinite(lo).all() and se2>0,se2)
    res[f'b{b}']=dict(rho=rho,rho_se=se,R2_held=r2h,R2_held_se=se2,R2_train=r2tr,discarded=ndisc,
        eig_max_train=float(evt.max()),eig_min_train=float(evt.min()),n_streams_rho=NS,n_held=16)
res['failed_predicates']=[list(map(str,f)) for f in fails]
with open('results.json','x') as f: json.dump(res,f,indent=1,default=float)
print(json.dumps(res,indent=1,default=float))
sys.exit(0)
