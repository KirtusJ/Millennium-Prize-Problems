"""T221 analysis. Predicates fixed before first run:
P1 control eigenvalue == 0.929632 (tol 5e-7, 6-decimal rounding).
P2 data shape: each stream X has M rows x n cols, Dc has 24 lines of n*n numbers; all finite.
P3 C(TRAIN) symmetric positive definite (Cholesky succeeds; cond < 1e12, i.e. 1/eps^(3/4)-ish where double
   precision generalized eig is trustworthy). Expectation (mine): holds.
P4 D(TRAIN) symmetric to 1e-10 relative; residual |D w - lam C w|/(|D w|) < 1e-8.
P5 smallest eigenvalue unique-ish: gap to 2nd > 1e-6*|lam|.
P6 jackknife: 16 leave-one-out values, all denominators >0.
"""
import numpy as np, sys
n_s=32
def load(i):
    with open(f'data/s{i}.X.csv') as f:
        names=f.readline().strip().split(',')
    X=np.loadtxt(f'data/s{i}.X.csv',delimiter=',',skiprows=1)
    Dc=np.loadtxt(f'data/s{i}.Dc.txt',comments='#')
    n=len(names)
    assert X.shape[1]==n and Dc.shape==(24,n*n),(X.shape,Dc.shape)
    return names,X,Dc.reshape(24,n,n).mean(0)
S=[load(i) for i in range(n_s)]
names=S[0][0]; n=len(names)
assert all(s[0]==names for s in S)
print('P2 finite',all(np.isfinite(s[1]).all() and np.isfinite(s[2]).all() for s in S),'rows',[s[1].shape[0] for s in S][:3])
def CD(idx):
    X=np.vstack([S[i][1] for i in idx]); Xc=X-X.mean(0)
    return Xc.T@Xc/len(X), np.mean([S[i][2] for i in idx],axis=0)
CT,DT=CD(range(16)); CH,DH=CD(range(16,32))
print('D sym err',np.abs(DT-DT.T).max()/np.abs(DT).max())
sv=np.linalg.svd(CT,compute_uv=False); print('cond(C_train) 2-norm',sv[0]/sv[-1],'sv min',sv[-1],'sv max',sv[0])
print('eig C train',np.sort(np.linalg.eigvalsh(CT))[:5])
try:
    L=np.linalg.cholesky(CT); print('P3 cholesky ok')
except Exception as e: print('P3 cholesky FAIL',e); L=None
Li=np.linalg.inv(L)
M=Li@DT@Li.T; M=(M+M.T)/2
lam,V=np.linalg.eigh(M); w=Li.T@V[:,0]
w=w/w[np.argmax(abs(w))]
print('lam sorted[:4]',lam[:4])
res=np.linalg.norm(DT@w-lam[0]*CT@w)/np.linalg.norm(DT@w); print('P4 residual',res)
print('lambda_min %.8g'%lam[0]); 
for k,v in zip(names,w): print('  w[%s]=%.6f'%(k,v))
q=lambda idx:(lambda c,d:(w@d@w)/(w@c@w))(*CD(idx))
qh=q(range(16,32)); qi=np.array([q([j for j in range(16,32) if j!=i]) for i in range(16,32)])
err=np.sqrt(15/16*((qi-qi.mean())**2).sum())
print('q = %.6f +- %.6f'%(qh,err),'loo mean',qi.mean())
sm=np.diag(DH)/np.diag(CH)
for k,v in zip(names,sm): print('  single %s %.6f'%(k,v))
print('smallest single',names[int(np.argmin(sm))],sm.min())
