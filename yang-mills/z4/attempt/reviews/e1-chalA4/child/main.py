"""Predicates fixed before first run.
P1: X(d)=2c(2d)+c(2d-1)+c(2d+1) <= 0 for all d=1..15. Hypothesis test: count of d with X<0 (qualifying) out of 15;
    X values with |X| < tol are "indeterminate", tol = max |X_N1 - X_N2| between meshes N=96 and N=144 (x10).
P2: L*N(L) bounded for L=2,4,8,16: met if L*N(L) <= 2*max over smaller L... fixed: met if L*N(L)(16) <= 1.5*L*N(L)(2) and
    no monotone growth by more than factor 1.5 over the range; otherwise failed.
ID: N(L) <= (1/(2L))*Var(D_0), Var(D_0)=2c(0)+2c(1); holds only if all X(d)<=0 (test numerically as well, per L).
Mesh tolerance: agreement of N=96 and N=144 midpoint quadratures.
Output files opened with mode x."""
import numpy as np, json
from quad import cvals
c1=cvals(96); c2=cvals(144)
tol=np.max(np.abs(c1-c2)); print("mesh diff max",tol)
c=c2
X=lambda d,c:2*c[2*d]+c[2*d-1]+c[2*d+1]
Xs=[X(d,c) for d in range(1,16)]; Xd=[abs(X(d,c1)-X(d,c2)) for d in range(1,16)]
def NL(L,c): return sum(c[abs(u-v)] for u in range(L) for v in range(L))/L**2
res={"c":list(c[:9]),"X":Xs,"Xmeshdiff":Xd,"tol":tol,
 "N":{L:NL(L,c) for L in (2,4,8,16)},"LN":{L:L*NL(L,c) for L in (2,4,8,16)},
 "bound":{L:(1/(2*L))*(2*c[0]+2*c[1]) for L in (2,4,8,16)}}
for k,v in res.items(): print(k,v)
nneg=sum(1 for x,dx in zip(Xs,Xd) if x<-dx)
print("X<0 beyond mesh error:",nneg,"/15; X>0 count:",sum(1 for x in Xs if x>0))
ln=list(res["LN"].values())
print("P1","met" if all(x<=0 for x in Xs) else "failed")
print("P2","met" if ln[-1]<=1.5*ln[0] and all(ln[i+1]<=1.5*ln[i] for i in range(3)) else "failed")
print("ID",{L:res["N"][L]<=res["bound"][L] for L in res["N"]})
json.dump(res,open("results/main.json","x"),indent=1)
