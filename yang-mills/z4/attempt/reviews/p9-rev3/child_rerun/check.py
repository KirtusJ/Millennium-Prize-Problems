"""Predicates (fixed before first run), N=6, seed 64:
P1 C1: for every nonempty subset S of slices (63), supp(tau F)=S+1 mod N, F=random poly in U_s,s in S
   (support measured numerically by perturbation, independent of the formula). Qualifying cases: all 63.
P2 C2: for S subset {0,1,2} nonempty (7): supp(tau F) subset {0..3}. For S subset {0..3}:
   tau F leaves A_+ iff 3 in S (15 cases).
P3 C3: 200 random polys F (random monomials in all 6 vars, deg<=3), 20 random U each:
   |theta tau F - tau^-1 theta F| <= 1e-9 (tolerance: float64 roundoff, values O(1e2) * eps*~1e2).
P4 C4: tau' on F=U_0 gives function of U_5 only, 5 not in {0..3}; supp measured numerically.
Result file opened with mode 'x'.
"""
import random, itertools, sys
N=int(sys.argv[1]) if len(sys.argv)>1 else 6
out=sys.argv[2]
rng=random.Random(64)
def tau(F): return lambda U: F([U[(s+1)%N] for s in range(N)])
def taup(F): return lambda U: F([U[(s-1)%N] for s in range(N)])
def tauinv(F): return taup(F)
def th(F): return lambda U: F([U[(-s)%N] for s in range(N)])
def randpoly(S,deg=3,nm=6):
    mons=[(rng.uniform(-2,2),[rng.choice(S) for _ in range(rng.randint(1,deg))]) for _ in range(nm)]
    # ensure each var in S appears
    for s in S: mons.append((rng.uniform(1,2),[s]))
    def F(U):
        t=0
        for c,m in mons:
            p=c
            for i in m:p*=U[i]
            t+=p
        return t
    return F
def supp(F):
    sp=set()
    for s in range(N):
        for _ in range(5):
            U=[rng.uniform(-1,1) for _ in range(N)];V=list(U);V[s]+=rng.uniform(.5,1.5)
            if abs(F(U)-F(V))>1e-9: sp.add(s);break
    return sp
res=[];fails=[]
def rec(name,ok,ev):
    res.append((name,ok,ev))
    if not ok: fails.append(name)
subs=[list(c) for k in range(1,N+1) for c in itertools.combinations(range(N),k)]
bad=0
for S in subs:
    if supp(tau(randpoly(S)))!={(s+1)%N for s in S}: bad+=1
rec("P1 C1 supp shift",bad==0,f"{len(subs)} cases qualify, {bad} violations")
h=[S for S in subs if set(S)<=set(range(min(3,N)))]
b2=sum(1 for S in h if not supp(tau(randpoly(S)))<=set(range(N//2+1)))
rec("P2a tau{0,1,2}->A+",b2==0,f"{len(h)} cases, {b2} violations")
h=[S for S in subs if set(S)<=set(range(N//2+1))]
b2=0;leave=0
for S in h:
    L=not supp(tau(randpoly(S)))<=set(range(N//2+1)); leave+=L
    if L!=((N//2) in S): b2+=1
rec("P2b leaves A+ iff slice N/2 in S",b2==0,f"{len(h)} cases, {leave} leave, {b2} violations")
mx=0
for _ in range(200):
    F=randpoly(list(range(N)))
    for _ in range(20):
        U=[rng.uniform(-1,1) for _ in range(N)]
        mx=max(mx,abs(th(tau(F))(U)-tauinv(th(F))(U)))
rec("P3 C3 theta tau = tau^-1 theta",mx<=1e-9,f"4000 evals, max diff {mx:.3g}")
sp=supp(taup(lambda U:U[0]))
rec("P4 C4 tau' U0 -> U_{N-1} outside A+",sp=={N-1} and (N-1) not in range(N//2+1),f"supp={sorted(sp)}")
with open(out,"x") as f:
    for r in res: f.write(f"{'MET' if r[1] else 'FAIL'}\t{r[0]}\t{r[2]}\n")
    f.write(f"met={sum(r[1] for r in res)} failed={len(fails)}\n")
print(open(out).read())
sys.exit(1 if fails else 0)
