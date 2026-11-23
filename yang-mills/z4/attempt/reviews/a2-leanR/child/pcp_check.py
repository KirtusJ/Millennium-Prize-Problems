"""Numerical check of L1-L7 + mutation. Usage: python3 pcp_check.py RESULT.json
Predicates fixed before first run (viol = lhs > rhs*(1+TOL)+1e-300, TOL=1e-12:
 ~1e-16 double eps * <=8-term sums and exp of args <=400, with 4 orders margin):
 Hypothesis counts are reported per statement (cases where premise holds).
 L1: D=C(.5)/C(1); for K in grid(-2..30 step .25) U {E_i} U {E_i-1e-9}: T(K)<=D e^{-K/2} C(1).
 L2: c~U(0,1), D=C(c)/C(1): T(K)<=D e^{-(1-c)K} C(1) same K set.
 L3: E_i>=1 (premise), t~U[1,10]: C(t)<=e^{-(t-1)}C(1).
 L4: premise C(1)>0: C(t)>=C(1)e^{-(t-1)Ebar}, t~U[1,10] (L4a) and t~U[-1,1) (L4b).
 L5: premise C(1)>0: Ebar<=2 log D.
 L6: E~U[1,2]: C(.5)<=e*C(1); report max ratio vs e, e^.5.
 L7: D=max_i e^{E_i/2} sum_{E_j>=E_i} w_j e^{-E_j}/C(1); c~U(.5,1): C(c)/C(1)<=f(D,c); report max ratio.
 MUT: L1 with e^{-K} in place of e^{-K/2}, D=C(.5)/C(1); n=1 search + random rate.
Seed 12345, 10^4 sets per statement."""
import math, json, sys, random
SEED=12345; N=10000; TOL=1e-12
def C(a,t): return sum(w*math.exp(-t*E) for w,E in a)
def T(a,K): return sum(w*math.exp(-E) for w,E in a if E>K)
def Eb(a): return sum(w*E*math.exp(-E) for w,E in a)/C(a,1)
def gen(rng,u=False):
    n=rng.randint(1,8)
    return [(rng.random(), (rng.uniform(1,2) if u else 1+rng.expovariate(1/2))) for _ in range(n)]
def Ks(a):
    g=[-2+0.25*i for i in range(129)]
    return g+[E for _,E in a]+[E-1e-9 for _,E in a]
def viol(l,r): return l>r*(1+TOL)+1e-300
res={}
def run(name,f,u=False,seed_off=0):
    rng=random.Random(SEED+seed_off); q=v=0; worst=None; ex=None
    for _ in range(N):
        a=gen(rng,u)
        r=f(a,rng)
        if r is None: continue
        q+=1
        bad,m=r
        if bad:
            v+=1
            if ex is None: ex=a
        if m is not None and (worst is None or m>worst): worst=m
    res[name]={"qualifying":q,"violations":v,"extreme":worst,"first_violating_set":ex}
def L1(a,rng):
    c1=C(a,1)
    if c1<=0: return None
    D=C(a,.5)/c1
    return any(viol(T(a,K),D*math.exp(-K/2)*c1) for K in Ks(a)),None
def L2(a,rng):
    c=rng.uniform(0,1); c1=C(a,1)
    if c1<=0: return None
    D=C(a,c)/c1
    return any(viol(T(a,K),D*math.exp(-(1-c)*K)*c1) for K in Ks(a)),None
def L3(a,rng):
    if min(E for _,E in a)<1: return None
    t=rng.uniform(1,10); return viol(C(a,t),math.exp(-(t-1))*C(a,1)),None
def L4a(a,rng):
    if C(a,1)<=0: return None
    t=rng.uniform(1,10); return viol(C(a,1)*math.exp(-(t-1)*Eb(a)),C(a,t)) ,None
def L4b(a,rng):
    if C(a,1)<=0: return None
    t=rng.uniform(-1,1); return viol(C(a,1)*math.exp(-(t-1)*Eb(a)),C(a,t)),None
def L5(a,rng):
    c1=C(a,1)
    if c1<=0: return None
    D=C(a,.5)/c1
    return viol(Eb(a),2*math.log(D)) if D>1 else (Eb(a)>1e-12+2*math.log(D)),None
def L6(a,rng):
    c1=C(a,1)
    if c1<=0: return None
    r=C(a,.5)/c1; return viol(r,math.e),r
def L7(a,rng):
    c1=C(a,1)
    if c1<=0: return None
    D=max(math.exp(E/2)*sum(w*math.exp(-F) for w,F in a if F>=E) for _,E in a)/c1
    c=rng.uniform(.5,1); f=1+2*(1-c)*D/(2*c-1)
    r=C(a,c)/c1/f; return viol(r,1),r
def MUT(a,rng):
    c1=C(a,1)
    if c1<=0: return None
    D=C(a,.5)/c1
    return any(viol(T(a,K),D*math.exp(-K)*c1) for K in Ks(a)),None
for i,(n,f,u) in enumerate([("L1",L1,0),("L2",L2,0),("L3",L3,0),("L4a_t>=1",L4a,0),("L4b_t in[-1,1)",L4b,0),("L5",L5,0),("L6",L6,1),("L7",L7,0),("MUT_L1_exp(-K)",MUT,0)]):
    run(n,f,u,i)
# mutation n=1 search: atom w=1,E in grid, K grid
best=None
for E in [1+0.25*i for i in range(0,80)]:
    a=[(1.0,E)]; D=C(a,.5)/C(a,1)
    for K in Ks(a):
        if viol(T(a,K),D*math.exp(-K)*C(a,1)):
            if best is None or E==2.0: best={"atoms":a,"K":K,"T":T(a,K),"rhs":D*math.exp(-K)*C(a,1)}
            break
res["MUT_n1_counterexample"]=best
with open(sys.argv[1],"x") as fh: json.dump(res,fh,indent=1)
for k,v in res.items(): print(k,{x:v[x] for x in v if x!="first_violating_set"} if "qualifying" in v else v)
