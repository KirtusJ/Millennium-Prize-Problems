"""Predicates (fixed before first run). Exact Fraction arithmetic, so tolerance = 0.
Cases: seeds 0..N-1 (random.Random(seed)), n in 1..8, K_i>=1, kappa,eps>=0, d0>=0 (rationals, denominators 1000).
Modes per case: 'eq' (every hypothesis with equality), 'slack' (b_i = d_{i-1}-eps_i+random>=0, d_i = ref + random>=0).
P1: for every case hypotheses hold (qualify count reported, hypothesis checked per case).
P2[v]: for v in C (M_{i-1}), C' (M_i), C'' (M_{i-2}): d_n >= RHS_v in every case.
 Expected: C met, C' met, C'' fails (my expectation: C'' subtracts less so is stronger than C; it is not a defect of target).
P3: in 'eq' mode, d_n == RHS_C exactly whenever RHS_C>0 (equality expectation) -- measured.
Min slack of C = min(d_n - RHS_C) over all cases (measured only).
"""
import random, sys
from fractions import Fraction as F
N=2000
def pos(x): return x if x>0 else F(0)
def rhs(d0,K,eps,kap,shift):
    n=len(K); M=[F(1)]
    for k in K: M.append(M[-1]*k)
    Mi=lambda j: M[j] if j>=0 else F(1)
    s=sum(Mi(i-shift)*(eps[i-1]+kap[i-1]) for i in range(1,n+1))
    return pos(d0-s)/M[n]
def run():
    out={'cases':0,'qual':0,'C':0,"C'":0,"C''":0,'eqC':0,'eqpos':0}
    minslack={'C':None,"C'":None,"C''":None}; cex=None
    for seed in range(N):
        r=random.Random(seed); R=lambda hi: F(r.randint(0,1000),1000)*hi
        n=r.randint(1,8)
        K=[1+R(3) if r.random()<.8 else F(1) for _ in range(n)]
        eps=[R(F(1,10)) for _ in range(n)]; kap=[R(F(1,10)) for _ in range(n)]
        d0=R(1)
        for mode in ('eq','slack'):
            d=d0; ok=True
            for i in range(n):
                b=d-eps[i]+(0 if mode=='eq' else R(F(1,20)))
                if not b>=d-eps[i]: ok=False
                d=pos(b-kap[i])/K[i]+(0 if mode=='eq' else R(F(1,50)))
                if not d>=pos(b-kap[i])/K[i]: ok=False
            out['cases']+=1; out['qual']+=ok
            if not ok: continue
            for name,sh in (('C',1),("C'",0),("C''",2)):
                v=rhs(d0,K,eps,kap,sh); sl=d-v
                if sl>=0: out[name]+=1
                elif name=="C''" and cex is None: cex=(seed,mode,n,[float(x) for x in K],float(d),float(v))
                if minslack[name] is None or sl<minslack[name]: minslack[name]=sl
            if mode=='eq':
                v=rhs(d0,K,eps,kap,1)
                if v>0:
                    out['eqpos']+=1; out['eqC']+= (d==v)
    return out,minslack,cex
out,ms,cex=run()
print(out); print({k:(float(v),str(v)) for k,v in ms.items()}); print("C'' first counterexample:",cex)
ok = out['C']==out['qual'] and out["C'"]==out['qual'] and out['eqC']==out['eqpos'] and out["C''"]<out['qual']
print("PREDICATES_AS_EXPECTED" if ok else "UNEXPECTED"); 
with open("results_test_c.txt","x") as f: f.write(repr((out,{k:str(v) for k,v in ms.items()},cex))+"\n")
sys.exit(0 if ok else 1)
