"""Evaluate predicates P0-P4 from res/*.txt (fixed in mc.py docstring). Writes analysis.txt (mode x)."""
import re, glob, math
def I(n,x): return sum((x/2)**(2*k+n)/(math.factorial(k)*math.factorial(k+n)) for k in range(40))
u = I(2,.5)/I(1,.5)
rows=[]
for f in sorted(glob.glob("res/L[46]_b*.txt")):
    if "cold" in f: continue
    t=open(f).read(); g=re.search(r"L=(\d+) beta=(\S+) .*W11=(\S+) \+- (\S+) W12=(\S+) \+- (\S+)",t)
    rows.append((int(g[1]),float(g[2]),*map(float,g.groups()[2:])))
out=[f"u(0.5)={u:.6f} u^2={u*u:.6f}"]
q=0
for L,b,w1,e1,w2,e2 in sorted(rows):
    s=w2/e2; q+= (L==4 and w2>3*e2)
    out.append(f"L={L} b={b} W11={w1:.5f}({e1:.5f}) W12={w2:.5f}({e2:.5f}) W12/err={s:.1f}  W12<W11:{w2<w1}")
    if b==0.5:
        out.append(f"  P0 |W11-u|={abs(w1-u):.5f} tol={3*e1+1e-3:.5f} {'PASS' if abs(w1-u)<3*e1+1e-3 else 'FAIL'}; P2 |W12-u^2|={abs(w2-u*u):.5f} tol={3*e2+1e-3:.5f} {'PASS' if abs(w2-u*u)<3*e2+1e-3 else 'FAIL'}; sigmas W11 {(w1-u)/e1:+.2f} W12 {(w2-u*u)/e2:+.2f}")
out.append(f"P1 qualifying L=4 cases (W12>3sigma): {q}/5")
l4=[r for r in sorted(rows) if r[0]==4]; out.append("P3 W11 monotone L=4: "+str(all(l4[i][2]<l4[i+1][2] for i in range(4))))
h=re.search(r"W11=(\S+) \+- (\S+)",open("res/L4_b0.5_cold.txt").read()); hot=[r for r in l4 if r[1]==.5][0]
z=(float(h[1])-hot[2])/math.hypot(float(h[2]),hot[3]); out.append(f"P4 cold-hot W11 diff = {z:+.2f} sigma {'PASS' if abs(z)<3 else 'FAIL'}")
open("analysis.txt","x").write("\n".join(out)+"\n"); print("\n".join(out))
