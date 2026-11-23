"""Recompute the director's (C) cross-check in A1_LEDGER.md, line 75 (file line).
Inputs (from the brief / ledger): R0 = 3.751e-2, 3.615e-2, 3.233e-2; R1 = 1.012e-2, 1.166e-2, 1.245e-2;
a*sqrt(sigma) = 0.3690, 0.2660, 0.1905; xi = 1/(3.74 * a sqrt(sigma)).
Ledger claims: q=R1/R0 = 0.270, 0.323, 0.385; xi = 0.72, 1.00, 1.40; xi*(1-q) = 0.53, 0.68, 0.86; growth ~ xi^0.75.
Predicates (fixed before first run):
 Q:  for all 3 cases |q - claimed| <= 0.0005 (tolerance: half a unit in the 3rd decimal, the precision quoted).
 X:  for all 3 cases |xi - claimed| <= 0.005 (half a unit in the 2nd decimal quoted).
 P:  for all 3 cases |xi*(1-q) - claimed| <= 0.005 (same reason), using unrounded q, xi.
 P':  same as P but with the rounded quoted q and xi (to see if rounding explains a difference); measured only.
 E:  the least-squares log-log exponent of xi*(1-q) vs xi lies in [0.70, 0.80] (ledger says "roughly ~ xi^0.75";
     'roughly' read as +-0.05). Pairwise exponents measured only.
 G:  xi*(1-q) strictly increasing (the ledger's "It grows").
No randomness; no seed needed. Output file opened with mode "x".
"""
import math, sys
R0=[3.751e-2,3.615e-2,3.233e-2]; R1=[1.012e-2,1.166e-2,1.245e-2]; s=[0.3690,0.2660,0.1905]
cq=[0.270,0.323,0.385]; cx=[0.72,1.00,1.40]; cp=[0.53,0.68,0.86]
q=[b/a for a,b in zip(R0,R1)]; xi=[1/(3.74*v) for v in s]; P=[x*(1-r) for x,r in zip(xi,q)]
Pr=[x*(1-r) for x,r in zip(cx,cq)]
out=[]; fails=0
def pred(name, cases):
    global fails
    n=sum(cases); out.append(f"{name}: {n}/{len(cases)} cases qualify -> {'MET' if n==len(cases) else 'FAILED'}")
    if n!=len(cases): fails+=1
out.append("q   = "+", ".join(f"{v:.5f}" for v in q))
out.append("xi  = "+", ".join(f"{v:.5f}" for v in xi))
out.append("P   = "+", ".join(f"{v:.5f}" for v in P))
out.append("P(rounded inputs) = "+", ".join(f"{v:.5f}" for v in Pr)+"  [measured only]")
pred("Q",[abs(a-b)<=0.0005 for a,b in zip(q,cq)])
pred("X",[abs(a-b)<=0.005 for a,b in zip(xi,cx)])
pred("P",[abs(a-b)<=0.005 for a,b in zip(P,cp)])
lx=[math.log(v) for v in xi]; lp=[math.log(v) for v in P]
mx=sum(lx)/3; mp=sum(lp)/3
e=sum((a-mx)*(b-mp) for a,b in zip(lx,lp))/sum((a-mx)**2 for a in lx)
pw={(i,j):(lp[j]-lp[i])/(lx[j]-lx[i]) for i,j in [(0,1),(1,2),(0,2)]}
out.append(f"LSQ exponent = {e:.4f}; pairwise (1,2)={pw[(0,1)]:.4f} (2,3)={pw[(1,2)]:.4f} (1,3)={pw[(0,2)]:.4f} [pairwise measured only]")
out.append(f"xi range factor = {xi[2]/xi[0]:.4f}")
pred("E",[0.70<=e<=0.80])
pred("G",[P[0]<P[1]<P[2]])
txt="\n".join(out)+f"\nfailed predicates: {fails}\n"
with open(sys.argv[1],"x") as f: f.write(txt)
print(txt); sys.exit(1 if fails else 0)
