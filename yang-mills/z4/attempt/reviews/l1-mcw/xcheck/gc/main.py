import numpy as np, itertools
T=10;L=(T,2,2,2);N=80
def sid(c): return np.ravel_multi_index([c[i]%L[i] for i in range(4)],L)
def sh(c,m):
    c=list(c);c[m]+=1;return c
coords=list(itertools.product(*[range(l) for l in L]))
lid=lambda c,m: sid(c)*4+m
plaqs=[];idx={}
for c in coords:
    for m in range(4):
        for n in range(m+1,4): idx[(sid(c),m,n)]=len(plaqs);plaqs.append((c,m,n))
B=np.zeros((len(plaqs),4*N))
for k,(c,m,n) in enumerate(plaqs):
    B[k,lid(c,m)]+=1;B[k,lid(sh(c,m),n)]+=1;B[k,lid(sh(c,n),m)]-=1;B[k,lid(c,n)]-=1
U,s,Vt=np.linalg.svd(B,full_matrices=False)
r=int((s>1e-9).sum());U=U[:,:r];P=U@U.T
print("plaq",len(plaqs),"links",4*N,"rank",r,"trP",np.trace(P))
mean=1.5*np.diag(P); Cov=1.5*P**2
def sel(m,n,t): return [idx[(sid((t,a,b,c)),m,n)] for a in range(2) for b in range(2) for c in range(2)]
def O(m,n,t): return sel(m,n,t)
def C(S0,St): return Cov[np.ix_(St,S0)].sum()
p=idx[(sid((0,0,0,0)),1,2)]
out=[f"rank={r} nplaq={len(plaqs)} nlinks={4*N}",f"<e_p> spatial(1,2) = {mean[p]:.10g}",f"Var(e_p) = {Cov[p,p]:.10g}  (check 1.5*P_pp^2={1.5*P[p,p]**2:.10g}, P_pp={P[p,p]:.10g})"]
# Cov over all spatial plaquettes is translation-inv; use t-sums
c=[C(O(1,2,0),O(1,2,t)) for t in range(5)]
for t in range(5): out.append(f"C({t}) = {c[t]:.10g}  ratio = {c[t]/c[0]:.10g}")
A=[(1,2),(1,3),(2,3)]
CA=sum(C(O(*a,0),O(*b,0)) for a in A for b in A)
out.append(f"C_A1(0) = {CA:.10g}")
out.append("<O_12> = %.10g"%mean[O(1,2,0)].sum())
# toy check: 1 plaquette-like: P=[[1]] var(phi^2/2 *3 colours)
rng=np.random.default_rng(1)
Q=np.array([[0.7,0.3],[0.3,0.4]]) # test Cov formula by sampling 2-var Gaussian
Lc=np.linalg.cholesky(Q);X=rng.standard_normal((3,2000000,2))@Lc.T
e=0.5*(X**2).sum(0);emp=np.cov(e.T)[0,1];print("toy",emp,1.5*Q[0,1]**2)
out.append(f"toy MC check Cov(e1,e2) empirical {emp:.5f} vs formula {1.5*Q[0,1]**2:.5f}; 1-var: formula Var={1.5*Q[0,0]**2:.5f} emp {np.cov(e.T)[0,0]:.5f}")
open('answer.txt','x').write("\n".join(out)+"\n");print("\n".join(out))
