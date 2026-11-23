"""Predicates fixed before first run:
P1: control bisection matches closed form m=acosh((1+sqrt3)/2) to <1e-9.
P2: task bisection matches closed form m=acosh((r+sqrt(r^2+8))/4) to <1e-9.
"""
from math import cosh, acosh, sqrt
def bis(r):
    f=lambda m: cosh(m*(1-3))/cosh(m*(2-3))-r
    lo,hi=0.01,5.0
    assert f(lo)<0<f(hi)
    for _ in range(200):
        mid=(lo+hi)/2
        if f(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2
def closed(r): return acosh((r+sqrt(r*r+8))/4)
out=[]
mc=bis(2.0); cc=acosh((1+sqrt(3))/2)
p1=abs(mc-cc)<1e-9
out.append(f"control bisect={mc!r} closed={cc!r} diff={abs(mc-cc):.3e} P1={'PASS' if p1 else 'FAIL'}")
r=1.012e-2/3.65e-3
mb=bis(r); mf=closed(r)
p2=abs(mb-mf)<1e-9
out.append(f"r={r!r} bisect={mb!r} closed={mf!r} diff={abs(mb-mf):.3e} P2={'PASS' if p2 else 'FAIL'}")
out.append(f"m/0.3690={mf/0.3690!r} (claimed 3.01)")
for name,lines in (("control.txt",out[:1]),("result.txt",out[1:])):
    with open(name,"x") as fh: fh.write("\n".join(lines)+"\n")
print("\n".join(out))
