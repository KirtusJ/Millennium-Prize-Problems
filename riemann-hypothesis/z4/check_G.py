"""Known-answer check of the RH working draft (21 Nov 2026), section I.1 sanity values.
Definitions (paper, eq. I.2): S(x)=sum_{n<=x} Lambda(n)(x/n-1); G(x)=S(x)-x log x+(1+gamma)x.
Predicates fixed before the first run:
 P1 G(1e4) rounds to 1.749   P2 G(1e5) rounds to 3.671
 P3 G(1e6) rounds to 11.040  P4 G(2e6) rounds to -12.268   (paper's printed 3 decimals)
 P5 2+gamma-log(4 pi) rounds to 0.0461 (paper: 0.0461...)
Tolerance basis: the paper prints three decimals; a predicate is met iff round(value,3) equals the printed value.
Sums use math.fsum (exactly rounded), so floating error is far below 5e-4.
"""
import math,sys
N=2_000_000
gamma=0.57721566490153286060651209
sieve=bytearray([1])*(N+1); sieve[0]=sieve[1]=0
for i in range(2,int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i]=bytearray(len(range(i*i,N+1,i)))
pp=[]  # (n, log p)
for p in range(2,N+1):
    if sieve[p]:
        lp=math.log(p); q=p
        while q<=N: pp.append((q,lp)); q*=p
def G(x):
    S=math.fsum(lp*(x/n-1) for n,lp in pp if n<=x)
    return S-x*math.log(x)+(1+gamma)*x
exp={10**4:1.749,10**5:3.671,10**6:11.040,2*10**6:-12.268}
ok=True
for i,(x,e) in enumerate(exp.items(),1):
    g=G(x); m=round(g,3)==e; ok&=m
    print(f"P{i} G({x})={g:.6f} printed {e} {'MET' if m else 'FAILED'}")
c=2+gamma-math.log(4*math.pi); m=abs(c-0.0461)<1e-4 and c>=0.0461; ok&=m
print(f"P5 2+gamma-log(4pi)={c:.6f} {'MET' if m else 'FAILED'}")
sys.exit(0 if ok else 1)
