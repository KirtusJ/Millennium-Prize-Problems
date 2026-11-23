"""Predicates fixed before first run.
P1: q_k in (0,1) for all k (physical: R1<R0). Tolerance: exact inequality. [for-all: count qualifying cases]
P2: xi strictly increasing as s decreases (xi=1/(3.74 s)); exact.
P3: xi_1 to 3 decimals == 0.725 (matches control); tol 5e-4 from 3-decimal rounding.
P4: pairwise exponents and LSQ exponent all positive (P grows with xi); expectation only, measured.
P5: LSQ exponent lies within [min,max] of pairwise exponents (expectation; tol none) -- measured, may fail.
Seed: none needed (deterministic); seed fixed 0.
"""
import math,sys
R0=[3.751e-2,3.615e-2,3.233e-2];R1=[1.012e-2,1.166e-2,1.245e-2];s=[0.3690,0.2660,0.1905]
q=[b/a for a,b in zip(R0,R1)];xi=[1/(3.74*x) for x in s];P=[x*(1-y) for x,y in zip(xi,q)]
out=open("result.txt","x")
def w(t):print(t);out.write(t+"\n")
for k in range(3):w(f"k={k+1} q={q[k]:.3f} xi={xi[k]:.3f} P={P[k]:.3f}")
pw={}
for i,j in[(0,1),(1,2),(0,2)]:
    pw[(i+1,j+1)]=math.log(P[j]/P[i])/math.log(xi[j]/xi[i]);w(f"pair{i+1}{j+1} p={pw[(i+1,j+1)]:.2f}")
lx=[math.log(x) for x in xi];lp=[math.log(x) for x in P];mx=sum(lx)/3;mp=sum(lp)/3
p=sum((a-mx)*(b-mp) for a,b in zip(lx,lp))/sum((a-mx)**2 for a in lx)
w(f"LSQ p={p:.2f} C={math.exp(mp-p*mx):.3f}")
def pred(n,ok,msg):w(f"{n} {'MET' if ok else 'FAILED'} {msg}")
pred("P1",all(0<x<1 for x in q),f"{sum(0<x<1 for x in q)}/3 cases qualify")
pred("P2",xi[0]<xi[1]<xi[2],"")
pred("P3",abs(xi[0]-0.725)<5e-4,"")
pred("P4",p>0 and all(v>0 for v in pw.values()),"measured")
pred("P5",min(pw.values())<=p<=max(pw.values()),"measured")
