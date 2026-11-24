"""T224 analysis v2 (after run 1 failed P1: C is exactly rank 304/308). Method: eigendecomposition C=U diag(e) U^T, keep e>1e-10*emax (the 4 dropped are ~1e-16),
 whiten W=U_r e_r^-1/2, symmetric eigenproblem of W^T D W, w=W v (minimum-norm, in range of C).
Predicates fixed BEFORE first run (tolerances: float64 eps-scale 1e-8 relative for residual/symmetry; statistical ones from the task):
 P1 (revised) C(TRAIN),C(HELD) have exactly 4 eigs below 1e-10*emax, the same null space N (|C_held N|<1e-12), and D(TRAIN),D(HELD) vanish on N (<1e-12). Original P1 'PD' FAILED in run 1.
 P2 D(TRAIN) symmetric (rel asym < 1e-10) and PSD (min eig >= -1e-10*max eig).
 P3 lambda_train <= min over single marks of D_kk/C_kk on TRAIN (rayleigh min) -- for all k; report how many marks qualify.
 P4 generalised residual ||D w - lam C w||/(||D w||) < 1e-8.
 P5 q >= lambda_train - 3*err (jackknife).
 P6 cond of C restricted to its range < 1e6 (the gap e[4]/emax is 2.8e-3 so ~360 expected). Full 308-dim cond is infinite; reported.
 P7 jackknife leave-one-out check: mean of q_k within 3 err of q.
Results written with mode 'x'.
"""
import numpy as np, json
R='data/'
names=[l.strip() for l in open(R+'names.txt') if l.strip()]
n=len(names)
m=[float(open(R+f's{i}.m.txt').read().split()[0]) for i in range(32)]
s1=[np.loadtxt(R+f's{i}.sum1.txt') for i in range(32)]
s2=[np.loadtxt(R+f's{i}.sum2.txt') for i in range(32)]
D=[np.loadtxt(R+f's{i}.D.txt') for i in range(32)]
def CD(S):
    M=sum(m[i] for i in S); mu=sum(s1[i] for i in S)/M
    C=sum(s2[i] for i in S)/M-np.outer(mu,mu)
    return (C+C.T)/2, sum(D[i] for i in S)/len(S)
out={}; fails=[]
def pred(name,ok,info=''):
    out[name]=bool(ok); print(name,ok,info)
    if not ok: fails.append(name)
TR=range(16); HE=range(16,32)
Ct,Dt=CD(TR); Ch,Dh=CD(HE)
et,U=np.linalg.eigh(Ct); r=et>1e-10*et[-1]; N=U[:,~r]
eh=np.linalg.eigvalsh(Ch)
pred('P1 rank/nullspace',(~r).sum()==4 and (eh<1e-10*eh[-1]).sum()==4 and np.abs(Ch@N).max()<1e-12 and np.abs(Dt@N).max()<1e-12 and np.abs(Dh@N).max()<1e-12)
ev=np.linalg.eigvalsh((Dt+Dt.T)/2)
pred('P2 D(TRAIN) sym+PSD',np.abs(Dt-Dt.T).max()<=1e-10*np.abs(Dt).max() and ev.min()>=-1e-10*ev.max(),f'mineig {ev.min():.3e}')
cond=et[-1]/et[r][0]; cond_full=np.linalg.cond(Ct)
W=U[:,r]/np.sqrt(et[r])
A=W.T@((Dt+Dt.T)/2)@W; A=(A+A.T)/2
lam,V=np.linalg.eigh(A)
lt=lam[0]; w=W@V[:,0]
sd=np.sqrt(np.diag(Ct))
w=w/np.abs(w).max()
pred('P4 residual',np.linalg.norm(Dt@w-lt*Ct@w)/np.linalg.norm(Dt@w)<1e-8,f'{np.linalg.norm(Dt@w-lt*Ct@w)/np.linalg.norm(Dt@w):.3e}')
pred('P6 range cond<1e6',cond<1e6,f'{cond:.10g}')
qt=np.diag(Dt)/np.diag(Ct)
nq=int((lt<=qt+1e-12).sum())
pred('P3 lambda<=every single-mark train quotient',nq==n,f'{nq}/{n} marks qualify')
q=(w@Dh@w)/(w@Ch@w)
qk=[]
for k in HE:
    S=[i for i in HE if i!=k]; c,d=CD(S); qk.append((w@d@w)/(w@c@w))
qk=np.array(qk); err=np.sqrt(15/16*((qk-qk.mean())**2).sum())
pred('P5 q>=lam-3err',q>=lt-3*err,f'q={q:.10g} err={err:.6g}')
pred('P7 jackknife mean within 3err of q',abs(qk.mean()-q)<=3*err,f'{qk.mean():.10g}')
sc=np.abs(w)*sd; top=np.argsort(-sc)[:3]
qh=np.diag(Dh)/np.diag(Ch); kmin=int(np.argmin(qh))
res=dict(lambda_train=lt,cond_Ctrain_range=cond,cond_Ctrain_full_numpy=cond_full,q=q,jackknife_err=err,top3=[(names[k],sc[k]) for k in top],
 min_single_held=(names[kmin],qh[kmin]),B_xy000_g00_held=qh[names.index('B.xy000.g00')],
 cond_first15=np.linalg.cond(Ct[:15,:15]),lambda_next=lam[1:4].tolist(),failed=fails,preds=out)
print(json.dumps(res,indent=1,default=float))
with open('results.json','x') as f: json.dump(res,f,indent=1,default=float)
