"""Predicates fixed before first run (data: FHK hep-lat/9208012 Tables 3, 8; LTW hep-lat/0404008 Table 14).
P1: a*sqrt(sigma) strictly decreases with beta over 2.2..2.85 (Table 3).
P2: plaquette <Up>=1-(1-<Up>) strictly increases with beta over Table 8.
P3: asymptotic-scaling ratio a(2.3)/a(2.4) vs 2-loop expectation exp(-(b)(2.4-2.3)*...) : 
    only report ratio; tolerance: ratio within 20% of 2-loop prediction (my own expectation, no source).
P4: m0++/sqrt(sigma)=3.78(7) lies within 3 sigma of 3.55(7)(SU(3)) is NOT required; just report.
P5 (for-all, tested per case): for each consecutive pair of Table 3 rows, count qualifying decreases.
Result file opened with mode x."""
import math
t3=[(2.2,.4690),(2.3,.3690),(2.4,.2660),(2.5,.1905),(2.6,.1360),(2.7,.1015),(2.85,.0630)]
t8=[(1.88,.52637),(2.1768,.43158),(2.2986,.39746),(2.3726,.37661),(2.4265,.36352),(2.5115,.34564),(2.7395,.30869)]
out=[]
q=[t3[i][1]>t3[i+1][1] for i in range(len(t3)-1)]
out.append(f"P1 pairs qualifying {sum(q)}/{len(q)} -> {'PASS' if all(q) else 'FAIL'}")
q=[t8[i][1]>t8[i+1][1] for i in range(len(t8)-1)]
out.append(f"P2 (1-<Up> decreasing) pairs qualifying {sum(q)}/{len(q)} -> {'PASS' if all(q) else 'FAIL'}")
# 2-loop SU(2): b0=11*2/(3*16pi^2)... a Lambda = (b0 g^2)^(-b1/(2b0^2)) exp(-1/(2 b0 g^2)), g^2=4/beta
b0=11*2/(3*16*math.pi**2); b1=34/3*(2/(16*math.pi**2))**2
def aL(b):
    g2=4/b; return (b0*g2)**(-b1/(2*b0**2))*math.exp(-1/(2*b0*g2))
for lo,hi in [(2.3,2.4),(2.4,2.5)]:
    r=dict(t3)[lo]/dict(t3)[hi]; p=aL(lo)/aL(hi)
    out.append(f"P3 a({lo})/a({hi}) measured {r:.3f} 2-loop {p:.3f} dev {abs(r/p-1)*100:.1f}% -> {'PASS' if abs(r/p-1)<.2 else 'FAIL(own expectation: 20% tol, beta~2.3 is pre-asymptotic)'}")
for b in (2.3,2.4,2.5): out.append(f"P6 plaquette at exactly beta={b} in Table 8: {'yes' if any(abs(x-b)<1e-9 for x,_ in t8) else 'NO (not tabulated)'}")
s="\n".join(out); print(s)
with open("prog/result_check.txt","x") as f: f.write(s+"\n")
