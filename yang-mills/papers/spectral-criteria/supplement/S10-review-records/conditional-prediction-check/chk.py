"""Check of two claims by an auditor session (pass 2), finite state. Seed 5. Output results.txt (not overwritten).
PREDICATES (fixed before first run):
 R1 reversible positive kernel K on n states, stationary pi, partition C (coarse), good set of cells.
    A = K on centred L2(pi). rho(c) = maximal correlation of (X,Y) given C(X)=c. gamma = 1 - max_{good c} rho(c)^2.
    G f = 1_good(C) (f - E[f|C]). Then lambda_min(I - A^2 - gamma G) >= -1e-10 (all vectors, incl. constants).
    Qualify only if gamma > 1e-6.
 R2 intermediate lag: PSD contraction A, projections P,B,G orthogonal summing to I, integers k>=1, m>=2k, 1<=j<=m.
    gamma = largest with I - A^{2k} >= gamma G (computed), kappa=||B A^j B||, b = 1-||P A^m P||.
    Then 1-||A^m|| >= (b-kappa)_+ / (1 + 2k/(m gamma)) - 1e-10. Qualify if gamma>1e-6.
 R2c control expected to FAIL sometimes: same with denominator 1 + 2/(m gamma) when k>1.
"""
import numpy as np, sys, os
rng=np.random.default_rng(5); out=[]
def r1():
    n=rng.integers(4,10); W=rng.random((n,n))+0.05; W=W+W.T; W=W@W  # PSD-ish symmetric positive
    pi=W.sum(1); pi/=pi.sum()*1.0; K=W/W.sum(1)[:,None]; pi=W.sum(1)/W.sum()
    D=np.diag(np.sqrt(pi)); Di=np.diag(1/np.sqrt(pi)); S=D@K@Di  # symmetric
    ev=np.linalg.eigvalsh((S+S.T)/2)
    if ev.min()<-1e-12: return None
    nc=rng.integers(2,max(3,n//2)+1); lab=rng.integers(0,nc,n)
    good=rng.random(nc)<0.7; J=np.outer(pi,np.ones(n))*K  # joint P(X=x,Y=y)
    rho2=0; Gm=np.zeros((n,n))
    for c in range(nc):
        idx=np.where(lab==c)[0]
        if len(idx)==0: continue
        pc=pi[idx]/pi[idx].sum()
        Pc=np.zeros((n,n))
        for a in idx: Pc[a,idx]=pc
        if good[c]:
            Ic=np.zeros((n,n)); Ic[idx,idx]=1; Gm+=Ic-Pc
            if len(idx)>1:
                Jc=J[idx,:]/pi[idx].sum(); px=Jc.sum(1); py=Jc.sum(0); keep=py>0
                M=Jc[:,keep]/np.sqrt(np.outer(px,py[keep])); s=np.linalg.svd(M,compute_uv=False)
                rho2=max(rho2,s[1]**2 if len(s)>1 else 0)
    g=1-rho2
    if g<1e-6 or not np.any(Gm): return None
    Gs=D@Gm@Di; Gs=(Gs+Gs.T)/2
    one=np.sqrt(pi); Pr=np.eye(n)-np.outer(one,one)
    Op=np.eye(n)-S@S-g*Gs
    return np.linalg.eigvalsh((Op+Op.T)/2).min()
def nrm(M): return np.linalg.norm(M,2)
def r2():
    n=rng.integers(3,9); Q,_=np.linalg.qr(rng.normal(size=(n,n))); ev=rng.random(n)**rng.choice([0.3,1,3]); A=Q@np.diag(ev)@Q.T
    lab=rng.integers(0,3,n); lab[0]=0; lab[1]=2
    P=np.diag((lab==0)*1.);B=np.diag((lab==1)*1.);G=np.diag((lab==2)*1.)
    k=rng.integers(1,4); m=rng.integers(2*k,2*k+12); j=rng.integers(1,m+1)
    mp=np.linalg.matrix_power
    Dm=np.eye(n)-mp(A,2*k); gi=np.where(lab==2)[0]
    Dinv=np.linalg.inv(Dm+1e-300*np.eye(n)); g=1/nrm(Dinv[np.ix_(gi,gi)])
    if g<1e-6: return None
    b=1-nrm(P@mp(A,m)@P); ka=nrm(B@mp(A,j)@B); d=1-nrm(mp(A,m))
    return d-max(b-ka,0)/(1+2*k/(m*g)), d-max(b-ka,0)/(1+2/(m*g)), k
q1=[x for x in (r1() for _ in range(6000)) if x is not None]
q2=[x for x in (r2() for _ in range(20000)) if x is not None]
L=["R1 qualify %d of 6000; min eig %.3e; %s"%(len(q1),min(q1),"MET" if min(q1)>=-1e-10 else "FAILED"),
   "R2 qualify %d of 20000; min slack %.3e; %s"%(len(q2),min(x[0] for x in q2),"MET" if min(x[0] for x in q2)>=-1e-10 else "FAILED"),
   "R2c (k>1, old denominator) min slack %.3e; violations %d"%(min(x[1] for x in q2 if x[2]>1),sum(1 for x in q2 if x[2]>1 and x[1]<-1e-10))]
open('results.txt','x').write('\n'.join(L)+'\n'); print('\n'.join(L))
