"""S4,S5. Usage: python3 s4_s5.py [tag]  -> results_s45_<tag>.txt (mode 'x'). No mpmath installed: 'mpmath 30 digits' replaced by decimal (60 digits) with
 DIRECT termwise derivative series (independent of the identity); this is a substitution, reported as such.
Predicates fixed before first run:
 S4a: exact rational series: p-q = -k^2/48 + O(k^4): coef k^2 == -1/48; p' coef k == -1/16; w' coef k == 1/2 (exact Fraction equality), and k^0 coef of p-q == 0.
 S4b: identity R'=1-3R/k-R^2 with R' from termwise series derivative, at k=0.5,2,6,20, abs diff < 1e-40 (60-digit decimal, 150-term series; truncation at k=20 ~ (100^150/ (150!)^2) <<1e-40).
 S5a: Fractions, I_1(6),I_2(6) series j=0..32 (33 terms) + tail bound t_33/(1-r), r=9/(34*35) (ratio bound for j>=33); R' interval from R'=1-R/2-R^2
      (monotone decreasing in R>0) must lie strictly inside (0.036885895,0.036885896).
 S5b: decimal 60 digits direct-derivative R'(6) inside the same interval, and |S5a mid - S5b| < 1e-20.
 Hypothesis count: not applicable (no 'for all')."""
import sys
from fractions import Fraction as F
from math import factorial as fa
from decimal import Decimal as D, getcontext
tag=sys.argv[1] if len(sys.argv)>1 else "run1"
out=[];P=out.append
# ---- S4a: power series in k, truncated at order K
K=12
def mul(a,b):
    c=[F(0)]*K
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<K: c[i+j]+=x*y
    return c
def inv(a):
    b=[F(0)]*K; b[0]=1/a[0]
    for n in range(1,K): b[n]=-sum(a[i]*b[n-i] for i in range(1,n+1))/a[0]
    return b
# I_1 = sum (k/2)^(2j+1)/(j!(j+1)!), I_2 = sum (k/2)^(2j+2)/(j!(j+2)!)  -> R = I2/I1
A=[F(0)]*K;B=[F(0)]*K
for j in range(K):
    if 2*j<K: B[2*j]=F(1,2**(2*j)*fa(j)*fa(j+1))     # I_1/(k/2)
    if 2*j<K: A[2*j]=F(1,2**(2*j)*fa(j)*fa(j+2))     # I_2/(k/2)^2
Rc=mul(A,inv(B))      # R = (k/2) * A/B
R=[F(0)]+[x/2 for x in Rc[:K-1]]
q=[R[i+1] for i in range(K-1)]+[F(0)]          # R/k
p=[ (i+1)*R[i+1] for i in range(K-1)]+[F(0)]   # R'
diff=[p[i]-q[i] for i in range(K)]
pp=[(i+1)*p[i+1] for i in range(K-1)]+[F(0)]
w=[F(0),F(0)]+p[:K-2]
wp=[(i+1)*w[i+1] for i in range(K-1)]+[F(0)]
P(f"R series coeffs (k^1,k^3,k^5): {R[1]},{R[3]},{R[5]}")
P(f"p-q: k^0={diff[0]}, k^2={diff[2]}, k^4={diff[4]}")
P(f"p': k^1={pp[1]}, k^3={pp[3]};  w': k^1={wp[1]}, k^3={wp[3]}")
s4a= diff[0]==0 and diff[2]==F(-1,48) and pp[1]==F(-1,16) and wp[1]==F(1,2)
P("S4a "+("PASS" if s4a else "FAIL"))
# ---- S4b
getcontext().prec=60
def series(k,nu,N=150):
    h=D(k)/2; s=D(0); ds=D(0)
    for j in range(N):
        e=2*j+nu
        t=h**e/(D(fa(j))*D(fa(j+nu)))
        s+=t; ds+=D(e)*h**(e-1)/2/(D(fa(j))*D(fa(j+nu)))
    return s,ds
def Rprime_direct(k):
    i1,d1=series(k,1); i2,d2=series(k,2)
    return (d2*i1-i2*d1)/i1**2, i2/i1
mx=D(0)
for k in ["0.5","2","6","20"]:
    rp,r=Rprime_direct(k); kk=D(k)
    idv=1-3*r/kk-r*r
    d=abs(rp-idv); mx=max(mx,d)
    P(f"S4b k={k}: R={str(r)[:22]} R'direct={str(rp)[:22]} identity={str(idv)[:22]} |diff|={d:.2e}")
P(f"S4b max diff {mx:.2e} "+("PASS" if mx<D("1e-40") else "FAIL"))
# ---- S5a
k=F(6); h=k/2
t1=lambda j: h**(2*j+1)/(fa(j)*fa(j+1))
t2=lambda j: h**(2*j+2)/(fa(j)*fa(j+2))
S1=sum(t1(j) for j in range(33)); S2=sum(t2(j) for j in range(33))
r=F(9,34*35)
T1=t1(33)/(1-r); T2=t2(33)/(1-r)   # ratios t_{j+1}/t_j = 9/((j+1)(j+2)) resp 9/((j+1)(j+3)) <= r for j>=33
# check first ratio indeed <= r, exactly
assert t1(34)/t1(33)<=r and t2(34)/t2(33)<=r
I1lo,I1hi=S1,S1+T1; I2lo,I2hi=S2,S2+T2
Rlo=I2lo/I1hi; Rhi=I2hi/I1lo
f=lambda R: 1-R/2-R*R
dlo,dhi=f(Rhi),f(Rlo)
P(f"S5a tail bounds: T1={float(T1):.3e} T2={float(T2):.3e}")
P(f"S5a R'(6) in [{float(dlo):.18f}, {float(dhi):.18f}] (exact rationals; width {float(dhi-dlo):.2e})")
s5a= F(36885895,10**9)<dlo and dhi<F(36885896,10**9)
P("S5a "+("PASS" if s5a else "FAIL"))
rp,_=Rprime_direct("6")
P(f"S5b decimal-60 direct R'(6) = {rp}")
mid=(dlo+dhi)/2
s5b=D("0.036885895")<rp<D("0.036885896") and abs(D(mid.numerator)/D(mid.denominator)-rp)<D("1e-20")
P("S5b "+("PASS" if s5b else "FAIL"))
fo=open(f"results_s45_{tag}.txt","x");fo.write("\n".join(out)+"\n");fo.close();print("\n".join(out))
