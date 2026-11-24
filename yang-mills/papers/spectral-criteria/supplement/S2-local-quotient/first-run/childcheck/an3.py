"""T221 final. Predicates (fixed before run; replace failed P3 of an.py):
P1 reduced C(TRAIN) (marks minus 3 exact duplicates) Cholesky ok and cond<1e8 (tol: eig min 1.5e-2 seen in an2 => expect ~45).
P2 D(TRAIN) and D(HELD) symmetric to 1e-12 rel.
P3 residual |D w - lam C w|/|D w| < 1e-10 on full 14-vector w (gauge zeros).
P4 lam gap to 2nd eigenvalue > 1e-6*|lam|.
P5 q invariant to null shifts: |q(w+N a)-q(w)|<1e-10 rel.
P6 all jackknife denominators > 0 and C_kk(HELD) > 0.
P7 lam <= every single-mark train quotient D_kk/C_kk (Rayleigh bound) on reduced marks.
Output file is opened with mode 'x'."""
import numpy as np
src=open('an.py').read().split("print('D sym err'")[0].split('"""',2)[2]
exec(src)
drop=[names.index(k) for k in ('B.L_no00','B.L_no10','B.L_no01')]
keep=[i for i in range(n) if i not in drop]
CT,DT=CD(range(16)); CH,DH=CD(range(16,32))
out=open('an3.result.txt','x')
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
P('P2 sym', np.abs(DT-DT.T).max()/np.abs(DT).max()<1e-12, np.abs(DH-DH.T).max()/np.abs(DH).max()<1e-12)
Cr=CT[np.ix_(keep,keep)]; Dr=DT[np.ix_(keep,keep)]
sv=np.linalg.svd(Cr,compute_uv=False); P('P1 cond reduced C(TRAIN)',sv[0]/sv[-1],'ok',sv[0]/sv[-1]<1e8)
sv14=np.linalg.svd(CT,compute_uv=False); P('cond full 14x14 C(TRAIN) numerical',sv14[0]/sv14[-1],'(true value infinite: rank 11)')
L=np.linalg.cholesky(Cr); Li=np.linalg.inv(L)
M=Li@Dr@Li.T; M=(M+M.T)/2; lam,V=np.linalg.eigh(M)
wr=Li.T@V[:,0]; w=np.zeros(n); w[keep]=wr; w/=w[np.argmax(abs(w))]
P('lambda_min %.10g'%lam[0],' next',lam[1:3],'P4',lam[1]-lam[0]>1e-6*abs(lam[0]))
P('P3 residual',np.linalg.norm(DT@w-lam[0]*CT@w)/np.linalg.norm(DT@w))
for k,v in zip(names,w): P('  w[%s] = %.6f'%(k,v))
qf=lambda idx,v=w:(lambda c,d:(v@d@v)/(v@c@v))(*CD(idx))
qh=qf(range(16,32)); qi=np.array([qf([j for j in range(16,32) if j!=i]) for i in range(16,32)])
err=np.sqrt(15/16*((qi-qi.mean())**2).sum())
P('q_HELD = %.8f +- %.8f (jackknife, n=16)'%(qh,err),' loo mean %.8f'%qi.mean(),'P6 denom>0',all(np.diag(CH)>0))
e,U=np.linalg.eigh(CT); N=U[:,e<1e-12]
P('P5 null-shift invariance',abs(qf(range(16,32),w+N@np.array([.3,-.7,1.1]))-qh)/abs(qh)<1e-10)
st=np.diag(DT)/np.diag(CT); P('P7 lam<=train single quotients (reduced)',all(lam[0]<=st[keep]+1e-12))
sm=np.diag(DH)/np.diag(CH)
for k,v in zip(names,sm): P('  single HELD %s %.8f'%(k,v))
P('smallest single HELD:',names[int(np.argmin(sm))],'%.8f'%sm.min())
P('first mark B.g00 single HELD %.12f  D_kk %.12e C_kk %.12e'%(sm[0],DH[0,0],CH[0,0]))
P('cond(C_TRAIN) full numerical %.6e ; reduced %.6f'%(sv14[0]/sv14[-1],sv[0]/sv[-1]))
