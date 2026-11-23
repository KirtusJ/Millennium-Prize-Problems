"""Numeric cross-check of the constant proved in Lean (A1R.L7) and of the child's layer-cake constant.
Predicates (fixed before first run):
 P1: for every random atom set with C(1)>0 and c in (1/2,1), a=1-c, D := sup_K T(K) e^{K/2}/C(1)
     (attained as K -> E_j from below, so D = max_j e^{E_j/2} sum_{E_i>=E_j} w_i e^{-E_i} / C(1)):
     C(c) <= (1 + D (e^a-1)/(1-e^{a-1/2})) C(1)        [Lean L7 constant]
 P2: same with f = 1 + 2aD/(1-2a)                     [continuous layer-cake, child's constant]
 P3 (expectation, measured): Lean constant >= child's constant for all a in (0,1/2).
Tolerance: relative 1e-12 (double eps 1e-16 times <=8 terms, exp args <= ~60; 4 orders margin).
Seed 20261123, 10^4 sets. Usage: python3 l7_check.py OUT.json (opened with mode "x")."""
import math, random, json, sys
rng=random.Random(20261123); TOL=1e-12
q=v1=v2=v3=0; m1=m2=0.0
for _ in range(10000):
    n=rng.randint(1,8); A=[(rng.random(),1+rng.expovariate(0.5)) for _ in range(n)]
    C1=sum(w*math.exp(-E) for w,E in A)
    if C1<=0: continue
    q+=1
    D=max(math.exp(Ej/2)*sum(w*math.exp(-E) for w,E in A if E>=Ej) for _,Ej in A)/C1
    c=rng.uniform(0.5,1); a=1-c
    if a<=0 or a>=0.5: continue
    Cc=sum(w*math.exp(-c*E) for w,E in A)
    fL=1+D*(math.exp(a)-1)/(1-math.exp(a-0.5)); fC=1+2*a*D/(1-2*a)
    r1=Cc/(fL*C1); r2=Cc/(fC*C1); m1=max(m1,r1); m2=max(m2,r2)
    v1+= r1>1+TOL; v2+= r2>1+TOL; v3+= fL<fC*(1-TOL)
out={"qualifying":q,"P1_viol":v1,"P1_max_ratio":m1,"P2_viol":v2,"P2_max_ratio":m2,"P3_viol":v3}
print(out); json.dump(out,open(sys.argv[1],"x"))
