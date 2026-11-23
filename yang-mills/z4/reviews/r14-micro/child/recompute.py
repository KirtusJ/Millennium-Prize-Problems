"""Recompute claimed values A1-A15. Fixed predicates (set BEFORE first run):
 P1 Each row: MATCH iff |claimed - computed| <= tol, tol = half a unit of the last quoted digit
    of the claim (written explicitly per row); qualitative claims judged on the stated inequality.
 P2 Quoted errors x(e): value tol and error tol are separate rows, each half unit of last digit.
 P3 A6 'standard errors': claim MATCHes only if BOTH (1-ratio)/err(ratio) and
    |diff|/sqrt(e1^2+e2^2) are within tol of claim. Percent claims use unrounded ratio.
 P4 A14 counted with exact integer/Fraction arithmetic (floating arange not trusted).
 P5 'for all' groups (A3, A4, A5, A6, A8): report n_match/n_cases per group; no 'all' claim made unless n_match==n.
 P6 A10/A11/A12: no sigma claim in task; report the number. A12 and A10 value tol half unit of last digit.
 P7 A9 MATCH iff |x|/err < 2.
 P8 A13 solved by closed form AND bisection, must agree 1e-9; m/0.3690 tol 0.005.
 Tolerance origin: task statement (half unit of last quoted digit). Seeds: none needed (deterministic).
"""
import math, json
from fractions import Fraction
rows=[]  # item, claimed, computed, tol, group
def add(item,cl,co,tol,grp): rows.append((item,cl,co,tol,grp))
q=lambda a,b:math.sqrt(a*a+b*b)
# A1
add("A1 6*0.3690",2.214,6*0.3690,5e-4,"A1"); add("A1 12*0.1905",2.286,12*0.1905,5e-4,"A1")
# A2
r=12*0.1905/(6*0.3690); e=r*q(0.0030/0.3690,0.0008/0.1905)
add("A2 mismatch %",3.25,(r-1)*100,5e-3,"A2"); add("A2 error %",0.94,e*100,5e-3,"A2")
# A3
for s in (0.5,2.0):
    add(f"A3 a^2/(8s), s/a^2={s}",{0.5:0.25,2.0:0.0625}[s],1/(8*s),5e-5 if s==2.0 else 5e-3,"A3")
    add(f"A3 sqrt(8s)/a, s/a^2={s}",{0.5:2,2.0:4}[s],math.sqrt(8*s),0.5,"A3")
# A4 (a=1)
add("A4 sqrt(6s)/l",0.29,math.sqrt(6/72),5e-3,"A4")
add("A4 s/a^2 l=6a",0.5,36/72,0.05,"A4"); add("A4 s/a^2 l=12a",2.0,144/72,0.05,"A4")
# A5
def ratio(n,en,d,ed):
    R=n/d; return R,R*q(en/n,ed/d)
A5={"R(0)":((3.42,0.12,3.751,0.042),(0.913,0.033)),
    "R(l/6)":((5.00,0.66,10.12,0.32),(0.494,0.067)),
    "Q0":((8.93,0.11,9.335,0.026),(0.956,0.012))}
RR={}
for k,(inp,(cv,ce)) in A5.items():
    R,E=ratio(*inp); RR[k]=(R,E,inp)
    add(f"A5 {k} value",cv,R,5e-4,"A5"); add(f"A5 {k} error",ce,E,5e-4,"A5")
# A6
for k,pc,nse in (("Q0",4.4,3.6),("R(0)",9,2.7),("R(l/6)",None,7.6)):
    R,E,(a,ea,b,eb)=RR[k]
    s1=(1-R)/E; s2=abs(b-a)/q(ea,eb)
    if pc is not None: add(f"A6 {k} percent diff",pc,(1-R)*100,0.05 if k=="Q0" else 0.5,"A6")
    else: add(f"A6 {k} factor",2,1/R,0.5,"A6")
    add(f"A6 {k} nse via ratio",nse,s1,0.05,"A6")
    add(f"A6 {k} nse via direct diff",nse,s2,0.05,"A6")
# A7
add("A7 (2.214/2.286)^3",0.91,(2.214/2.286)**3,5e-3,"A7")
# A8
for a,b,c in ((3.751,0.042,88),(1.012,0.032,31),(3.65,0.34,11)):
    add(f"A8 {a}/{b}",c,a/b,0.5,"A8")
# A9
add("A9 |x|/err <2 (claimed inside 2se -> 1 true)",1,1.0 if 2.0/1.1<2 else 0,0,"A9"); a9=2.0/1.1
# A10 series Bessel
def I(nu,x):
    return sum((x/2)**(2*k+nu)/(math.factorial(k)*math.factorial(k+nu)) for k in range(40))
v10=1-I(2,0.5)/I(1,0.5)
add("A10 1-I2/I1 (0.5)",0.876282,v10,5e-7,"A10")
nse10=(0.875486-0.876282)/0.000760
# A11
n11a=(0.602953-0.602934)/q(159e-6,37e-6); n11b=(0.652029-0.651941)/q(160e-6,198e-6)
# A12
v12=math.sqrt(math.pi)/(640*math.pi**2); add("A12",0.00028060,v12,5e-9,"A12")
# A13
r13=1.012e-2/3.65e-3
x=(r13+math.sqrt(r13*r13+8))/4; mc=math.acosh(x)
f=lambda m:math.cosh(-2*m)/math.cosh(-m)-r13
lo,hi=1e-6,5.0
for _ in range(200):
    mid=(lo+hi)/2
    if f(lo)*f(mid)<=0: hi=mid
    else: lo=mid
mb=(lo+hi)/2; assert abs(mb-mc)<1e-9
add("A13 m/0.3690",3.01,mc/0.3690,5e-3,"A13")
# A14
n_all=int(Fraction(50)/Fraction(5,100))+1; n_sub=int((Fraction(50)-Fraction(350,100))/Fraction(5,100))+1
add("A14 points 0..50",1001,n_all,0,"A14")
# A15
add("A15 configs/block",None,160/8,0,"A15")
out=[]; groups={}
for it,cl,co,tol,g in rows:
    ok=None if cl is None else abs(cl-co)<=tol+1e-12
    out.append((it,cl,co,ok)); 
    if ok is not None: groups.setdefault(g,[]).append(ok)
# A6 combined verdict (P3): pair ratio/direct rows
comb={}
for it,cl,co,ok in out:
    if "nse via" in it: comb.setdefault(it.split(" nse")[0],[]).append(ok)
with open("results.json","x") as fj: json.dump(out,fj,indent=1)
with open("report.md","x") as f:
    f.write("# Report\n\nControl: control.txt = 3.25\n\n| item | claimed | computed | verdict |\n|---|---|---|---|\n")
    for it,cl,co,ok in out:
        v="(no claim; value reported)" if ok is None else ("MATCH" if ok else "MISMATCH")
        f.write(f"| {it} | {cl} | {co:.8g} | {v} |\n")
    for k,l in comb.items(): f.write(f"| {k} nse combined (P3) | | | {'MATCH' if all(l) else 'MISMATCH'} |\n")
    f.write(f"| A9 2.0/1.1 | inside 2 se | {a9:.4f} se | {'MATCH' if a9<2 else 'MISMATCH'} |\n")
    f.write(f"| A10 (0.875486-0.876282)/0.000760 | - | {nse10:.3f} se | (no claim) |\n")
    f.write(f"| A11 0.602953(159) vs 0.602934(37) | - | {n11a:.3f} se | (no claim) |\n")
    f.write(f"| A11 0.652029(160) vs 0.651941(198) | - | {n11b:.3f} se | (no claim) |\n")
    f.write(f"| A13 m (lattice units), closed form / bisection | - | {mc:.10f} / {mb:.10f} | agree 1e-9 |\n")
    f.write(f"| A14 points 3.50..50 | - | {n_sub} | (no claim) |\n")
    f.write("\n## Group counts (P5)\n\n")
    for g,l in groups.items(): f.write(f"- {g}: {sum(l)}/{len(l)} rows MATCH\n")
print(open("report.md").read())
