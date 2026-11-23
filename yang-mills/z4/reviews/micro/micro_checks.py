"""Micro-review checks C2, C3(independent), C4, C6 for the Z4 two-dim control. Own program.
PREDICATES (fixed before first run):
 Q2a  U(1): M(N) > 1/2 for N=1,2,3.           Q2b SU(2): M(N) > 3/8 for N=1,2,3.
 Q2c  H (closed Bessel coefficient vs Haar quadrature, rel 1e-25, dps 40, as in input program) qualifies for N=1,2,3,
      per group, 2 labels each; report count qualifying (of 3 N per group).  Tolerance source: input program's own.
 Q4a  Z_n (n=2,3,5) M(N) strictly decreasing for N=1..16 (all integers); Q4b ratios M/A at N=2,4,8,16 reported (measured only).
      also Q4c: ratio at N=1..16 integers reported; Q4d: |M/A-1|<1e-6 at N=16 (input's own) re-evaluated.
 Q3   Z_4, Z_6 (indep. of delegate): |M/A -1| at N=2,4,8,16 with k=2 reported; predicate |M/A-1|<1e-6 at N=16, and
      relative error decays like exp(-N^2*e) (e = gap between first and second excited cosine levels..) -> reported only.
 Q6   x*(-log tanh x) vs 1/(1+x) at x=0.01,1,10; predicate: LHS<=RHS (holds) ; 'tight' = LHS/RHS>0.9 (my expectation: fails everywhere);
      also sup over x of LHS*(1+x) on a grid, measured only.
Output micro_result.json, refused if exists. No random numbers."""
import json, os, sys
sys.path.append(sys.argv[1])
import mpmath as mp
OUT = "micro_result.json"
if os.path.exists(OUT): sys.exit("exists")
mp.mp.dps = 40
r = {}
def s(x, n=15): return mp.nstr(x, n)
def u1c(n,b): return mp.besseli(n,b)*mp.exp(-b)
def u1q(n,b):
    f=lambda t: mp.exp(b*(mp.cos(t)-1))*mp.cos(n*t); w=6/mp.sqrt(b)
    pts=[-mp.pi,-w,0,w,mp.pi] if w<mp.pi else [-mp.pi,0,mp.pi]
    return mp.quad(f,pts)/(2*mp.pi)
def sc(t,b): return 2*mp.besseli(t+1,b)/b*mp.exp(-b)
def sq(t,b):
    d=t+1; f=lambda p: mp.exp(b*(mp.cos(p)-1))*mp.sin(d*p)*mp.sin(p); w=6/mp.sqrt(b)
    pts=[0,w,mp.pi] if w<mp.pi else [0,mp.pi]
    return (2/mp.pi)*mp.quad(f,pts)/d
tol=mp.mpf(10)**-25
r["Q2"]={}
for N in (1,2,3):
    b=mp.mpf(N)**2; b2=4*b
    h1=[abs(u1c(n,b)-u1q(n,b))/abs(u1c(n,b)) for n in (0,1)]
    h2=[abs(sc(t,b2)-sq(t,b2))/abs(sc(t,b2)) for t in (0,1)]
    M1=-b*mp.log(mp.besseli(1,b)/mp.besseli(0,b)); M2=-b*mp.log(mp.besseli(2,b2)/mp.besseli(1,b2))
    r["Q2"][N]={"M_U1":s(M1),"M_SU2":s(M2),"U1_gt_half":bool(M1>0.5),"SU2_gt_3_8":bool(M2>mp.mpf(3)/8),
      "H_U1_rel":[s(x,5) for x in h1],"H_SU2_rel":[s(x,5) for x in h2],"H_U1":all(x<tol for x in h1),"H_SU2":all(x<tol for x in h2)}
mp.mp.dps=400
def Mn(n,N):
    b=mp.mpf(N)**2
    lam=lambda k: mp.fsum(mp.exp(b*(mp.cos(2*mp.pi*j/n)-1))*mp.cos(2*mp.pi*j*k/n) for j in range(n))
    return -b*mp.log(lam(1)/lam(0)), b
def A(n,N):
    b=mp.mpf(N)**2; d=1-mp.cos(2*mp.pi/n); k=1 if n==2 else 2
    return b*k*d*mp.exp(-b*d)
r["Q4"]={}
for n in (2,3,5):
    Ms=[Mn(n,N)[0] for N in range(1,17)]
    rat=[Ms[N-1]/A(n,N) for N in range(1,17)]
    r["Q4"]["Z%d"%n]={"decreasing_1_to_16":all(Ms[i]>Ms[i+1] for i in range(15)),
      "M_N1":s(Ms[0],10),"ratio_N1_to_16":[s(x,12) for x in rat],"ratio_2_4_8_16":[s(rat[i-1],15) for i in (2,4,8,16)],
      "within_1e-6_N16":bool(abs(rat[15]-1)<mp.mpf(10)**-6)}
r["Q3"]={}
for n in (4,6):
    rat=[Mn(n,N)[0]/A(n,N) for N in (2,4,8,16)]
    r["Q3"]["Z%d"%n]={"ratio":[s(x,15) for x in rat],"err":[mp.nstr(x-1,5) for x in rat],"within_1e-6_N16":bool(abs(rat[-1]-1)<mp.mpf(10)**-6)}
mp.mp.dps=40
r["Q6"]={}
for x in (0.01,1,10):
    x=mp.mpf(x); L=x*(-mp.log(mp.tanh(x))); R=1/(1+x)
    r["Q6"][str(x)]={"lhs":s(L,8),"rhs":s(R,8),"ratio":s(L/R,6),"le":bool(L<=R)}
g=[mp.mpf(i)/1000 for i in range(1,20001)]
best=max(g,key=lambda x:x*(-mp.log(mp.tanh(x)))*(1+x))
r["Q6"]["sup_ratio_grid"]={"x":s(best,5),"ratio":s(best*(-mp.log(mp.tanh(best)))*(1+best),6)}
with open(OUT,"x") as f: json.dump(r,f,indent=1,sort_keys=True)
print(json.dumps(r,indent=1,sort_keys=True))
