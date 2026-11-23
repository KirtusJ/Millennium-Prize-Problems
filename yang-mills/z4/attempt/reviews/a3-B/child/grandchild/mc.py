"""Haar SU(2) Monte Carlo. Plain sampling, no importance weights (proposal = Haar itself).
Predicates (stated before first run):
 CONTROL: est of E[exp(2*x0)] over 20 batches (batch means); PASS iff |est-1.590637| <= 3*SE
          (SE = std of batch means / sqrt(20)). If FAIL, main run is skipped.
 MAIN: P = sum(w*1{1-x0>0.2})/sum(w), w=exp(16*x0); SE by delta method on ratio
          (SE^2 = var(a - P*w)/ (N * mean(w)^2)). Report with SE only; no agreement claims.
Seed 12345. Result file opened with mode "x" (never overwritten).
Rerun: python3 mc.py <outfile>   (outfile must not exist)
"""
import sys, numpy as np
SEED=12345; NB=20; PER=1_000_000   # N = NB*PER per run
def draw(rng,n):
    g=rng.standard_normal((n,4)); g/=np.linalg.norm(g,axis=1,keepdims=True)
    return g[:,0]   # cos(alpha)=x0 for U=[[x0+i x3, x2+i x1],[-x2+i x1, x0-i x3]]
rng=np.random.default_rng(SEED)
out=open(sys.argv[1],"x")
def log(s): print(s); out.write(s+"\n"); out.flush()
# control
bm=np.array([np.exp(2*draw(rng,PER)).mean() for _ in range(NB)])
est=bm.mean(); se=bm.std(ddof=1)/np.sqrt(NB)
ok=abs(est-1.590637)<=3*se
log(f"CONTROL N={NB*PER} est={est:.6f} SE={se:.6f} diff={est-1.590637:+.6f} PASS={ok}")
if not ok: log("control failed; stopping"); sys.exit(1)
# main: use 5x more samples
N_B=40; S=0; sw=0; swa=0; sums=[]
num=[];den=[]
A=[];W=[]
for _ in range(N_B):
    x=draw(rng,PER); w=np.exp(16*x); a=w*(1-x>0.2)
    num.append(a.sum()); den.append(w.sum())
    A.append(a);W.append(w)
A=np.concatenate(A);W=np.concatenate(W);N=len(W)
P=A.sum()/W.sum()
se=np.sqrt(np.var(A-P*W,ddof=1)/N)/W.mean()
ess=W.sum()**2/(W**2).sum()
bmP=np.array(num)/np.array(den)
log(f"MAIN seed={SEED} N={N} P={P:.6e} SE(delta)={se:.3e} SE(batch means of ratio, {N_B} batches)={bmP.std(ddof=1)/np.sqrt(N_B):.3e} ESS={ess:.0f}")
