"""Arithmetic/trace check of target/sec_smallbox.tex against inputs/. Predicates fixed before first run.
Tolerance sources: printed digits of the quoted number (half unit of last printed place).
 P1  log-ratio(crossreview l.164-169) * beta^(1/3) rounds to table values 1.636,1.760,1.837,1.887,1.919,1.939 (tol 5e-4).
 P2  5.3254970-3.3505330 = 1.974964 (tol 5e-7 per 7-digit inputs -> 1e-6).
 P3  numerics3 l.81-83 logs * beta^(1/3) = 2.88, 2.04, 1.54 (tol 5e-3).
 P4  beta=1024: (1-l0)/h vs e0 and (1-l1)/h vs e1 are 16-23% low (tol 0.5 pct pt); -log l_j/h within 1.3% (tol 0.05 pt).
 P5  (-log l1 + log l0)/h at 1024 = log ratio * beta^(1/3) (consistency, 2e-4).
 P6  Rescaling A=2(bL^3)^(-1/3)Y: kinetic coeff = 1/2 (bL^3)^(-1/3), potential coeff = 2 (bL^3)^(-1/3), several bL^3 (1e-12).
 P7  beta=4/g^2: beta^(-1/3) = 4^(-1/3) g^(2/3) (1e-12).
 P8  6.534885*4^(-1/3) vs 4.1167196 (table, tol 5e-8) and vs 4.116719735 diff 1.5e-7 (2 s.f.), within 5e-7*4^(-1/3).
 P9  gaps *4^(-1/3) = 1.89778, 2.26965 (tol 5e-6+3.2e-7).
 P10 trace lines: every 'file l.N' cited in the .tex exists (N <= line count of file).  Hypothesis for 'for all': report qualifying count.
Result file opened mode 'x'. No randomness."""
import math,re,sys
D='inputs/'
met=failed=meas=0; out=[]
def pr(name,ok,msg):
    global met,failed
    met+=ok; failed+=(not ok); s=f"{name}: {'MET' if ok else 'FAILED'} {msg}"; out.append(s); print(s)
def ms(msg):
    global meas; meas+=1; out.append("measured: "+msg); print("measured:",msg)
# P1
lr={32:0.5151641763,64:0.4399423291,128:0.3645007923,256:0.2971232997,512:0.2398232122,1024:0.1923831345}
tab={32:1.636,64:1.760,128:1.837,256:1.887,512:1.919,1024:1.939}
bad=[b for b in lr if abs(lr[b]*b**(1/3)-tab[b])>5e-4]
pr("P1",not bad,f"{len(lr)-len(bad)}/{len(lr)} cases; values {[round(lr[b]*b**(1/3),4) for b in lr]}")
pr("P2",abs((5.3254970-3.3505330)-1.974964)<1e-6,f"diff={5.3254970-3.3505330:.7f}")
l3={1:2.876117,2:1.621505,4:0.968930}; t3={1:2.88,2:2.04,4:1.54}
pr("P3",all(abs(l3[b]*b**(1/3)-t3[b])<5e-3 for b in l3),str({b:round(l3[b]*b**(1/3),4) for b in l3}))
h=1024**(-1/3)
a0,a1=2.82763,4.09675; b0,b1=3.31863,5.25773; e0,e1=3.3505330,5.3254970
p0,p1=100*(1-a0/e0),100*(1-a1/e1); q0,q1=100*(1-b0/e0),100*(1-b1/e1)
pr("P4",abs(p0-16)<0.5 and abs(p1-23)<0.5 and max(abs(q0),abs(q1))<=1.3+0.05,f"(1-l)/h low by {p0:.2f}%,{p1:.2f}%; -log l/h low by {q0:.2f}%,{q1:.2f}%")
pr("P5",abs((b1-b0)-lr[1024]*1024**(1/3))<2e-4,f"{b1-b0:.5f} vs {lr[1024]*1024**(1/3):.5f}")
ok=True
for X in (1.0,8.0,64.0,1000.0):
    ok&=abs(2/X*0.25-0.5*X**(-1/3))<1e-12 if False else True
# kinetic: -(2/X) d^2/dA^2, A=sY: d^2/dA^2 = 1/s^2 d^2/dY^2, s=2X^(-1/3): coeff=2/X/(4 X^(-2/3)) 
    kin=(2/X)/(2*X**(-1/3))**2; pot=(X/8)*(2*X**(-1/3))**4
    ok&=abs(kin-0.5*X**(-1/3))<1e-12 and abs(pot-2*X**(-1/3))<1e-12
pr("P6",ok,"rescaling coefficients at X=beta L^3 in {1,8,64,1000}")
pr("P7",all(abs((4/g**2)**(-1/3)-4**(-1/3)*g**(2/3))<1e-12 for g in (0.3,1,2.5)),"")
k=4**(-1/3); c0=6.534885*k; d=c0-4.116719735
pr("P8",abs(c0-4.1167196)<5e-8 and 1.45e-7<=abs(d)<1.55e-7 and abs(d)<=5e-7*k,f"conv={c0:.10f} diff={d:.3e} tol={5e-7*k:.3e}")
pr("P9",abs(3.012539*k-1.89778)<5.4e-6 and abs(3.602838*k-2.26965)<5.4e-6,f"{3.012539*k:.7f},{3.602838*k:.7f}")
ms(f"geometric 3-pt vs fit vs continuum: 1.97583,1.97496,1.974964 (not recomputable, no raw data)")
# P10 trace lines
tex=open('target/sec_smallbox.tex').read()
n={f:sum(1 for _ in open(D+f)) for f in ['A4_M1.md','A4_M0.md','A4_center.md','crossreview.md','numerics2.md','numerics3.md','grounding.md','A3_NOTES.md']}
cites=[]
for line in tex.splitlines():
    m0=re.search(r'(?<!\\)%',line)
    if m0:
        line=line[m0.start():]
        for m in re.finditer(r'(\w+\.md) l\.(\d+)(?:-(\d+))?(?:, l\.(\d+))?',line):
            f=m.group(1); nums=[int(x) for x in m.groups()[1:] if x]
            cites.append((f,max(nums)))
        for m in re.finditer(r'(\w+\.md) l\.(\d+)',line): pass
badc=sorted({(f,x) for f,x in cites if x>n[f]})
pr("P10",not badc,f"{len(cites)-len(badc)}/{len(cites)} trace refs within file length; out of range: {badc}")
s=f"met {met}, failed {failed}, measured only {meas}"; out.append(s); print(s)
open('results_check_sec_v2.txt','x').write("\n".join(out)+"\n")
sys.exit(1 if failed else 0)
