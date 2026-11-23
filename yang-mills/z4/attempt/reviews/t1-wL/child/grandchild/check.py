"""Predicates fixed BEFORE first run:
P1 control integral matches 0.333333
P2 |min (a) - 8.35| < 0.005
P3 |value (b)(i) - 9.09| < 0.005
P4 the minimum (a) is interior to the box d in [1,5], rho in (0,1/2] (not on boundary)
No randomness. No scipy: coarse grid + nested grid refinement.
"""
from math import *
def l(K,d,r): return K+(d+2*r)**2+log(pi/2)+2*log(24*pi/(11*r**3))
K0=lambda r:2*(2*r+r*r)**2
Kk=lambda r:2*(sqrt(.5)+2*r+r*r)**2
def f0(d,r): return l(K0(r),d,r)/d
def fk(d,r): return l(Kk(r),d,r)/d
def mn(f):
    a,b,c,e=1,5,1e-6,.5
    for it in range(12):
        best=None
        for i in range(81):
            for j in range(81):
                d=a+(b-a)*i/80; r=c+(e-c)*j/80
                v=f(d,r)
                if best is None or v<best[0]: best=(v,d,r)
        v,d,r=best; w=(b-a)/80; w2=(e-c)/80
        a,b=max(1,d-2*w),min(5,d+2*w); c,e=max(1e-6,r-2*w2),min(.5,r+2*w2)
    return best
ctrl=sum((((i+.5)/200000)**2) for i in range(200000))/200000
with open("control.txt","x") as fh: fh.write("%.6f\n"%ctrl)
va=mn(f0); vb=mn(fk)
out=[]
out.append("control %.6f -> P1 %s"%(ctrl,abs(ctrl-1/3)<5e-7))
out.append("(a) min %.6f at d=%.6f rho=%.6f"%va)
out.append("(b)(i) Kk at (a)-argmin: %.6f"%fk(va[1],va[2]))
out.append("(b)(ii) Kk own min: %.6f at d=%.6f rho=%.6f"%vb)
out.append("(c) d=3.65 rho=0.265: l(K0)/d=%.6f l(Kk)/d=%.6f"%(f0(3.65,.265),fk(3.65,.265)))
P2=abs(va[0]-8.35)<.005; P3=abs(fk(va[1],va[2])-9.09)<.005
P4=1<va[1]<5 and 0<va[2]<.5
out.append("P2 %s P3 %s P4 %s"%(P2,P3,P4))
s="\n".join(out); print(s)
with open("result.md","x") as fh: fh.write(s+"\n")
