"""Predicates fixed before first run (pure python float64; no mpmath/numpy available).
Grid: 241 log-spaced c in [1e-3,50]; j=0..4.  theta_j summed |m|<=M with M=ceil(sqrt(800/c))+50 (terms < e^-800 * poly, negligible).
P0 (hypothesis per case, rule 4): f(x)=x^(2j)e^{-cx^2} unimodal on x>0 with max at sqrt(j/c) (j>=1), decreasing (j=0): checked by sign of f' on 2000 sample pts; count qualifying cases.
P1 T1: theta0 <= 1+sqrt(pi/c) + tol.
P2 T2: theta_j <= Gamma(j+.5)c^(-j-.5)+2(j/(ec))^j + tol, j>=1.
P3 variant constant 1: theta_j <= Gamma(j+.5)c^(-j-.5)+(j/(ec))^j  (expectation: may fail -> informational; failures counted, not a defect of T2).
P4 T3 q=2: 3 th1 th0^2 == brute-force 3-D sum_{n!=0}|n|^2 e^{-c|n|^2} (rel 1e-9) on c>=0.05 subgrid; also bound-version (thetas replaced by bounds) >= true.
P5 q=4 identity: 3 th2 th0^2+6 th1^2 th0 == brute force (rel 1e-9) on same subgrid; bound-version >= true on full grid.
Tolerance: tol = 1e-12*max(1,rhs) = float64 roundoff of sums of ~1e3 terms (eps 2.2e-16 x ~1e3 x safety); brute 3-D rel 1e-9 since ~1e5 terms.
Exit 0 iff P0 all qualify and P1,P2,P4,P5 have zero violations; P3 only reported.
"""
import math,sys
E=math.e
cs=[10**(-3+(math.log10(50)+3)*i/240) for i in range(241)]
def th(j,c):
    M=int(math.sqrt(800/c))+50
    s=1.0 if j==0 else 0.0
    return s+2*sum(m**(2*j)*math.exp(-c*m*m) for m in range(1,M+1))
def B(j,c):
    if j==0: return 1+math.sqrt(math.pi/c)
    return math.gamma(j+.5)*c**(-j-.5)+2*(j/(E*c))**j
def B1(j,c):
    return math.gamma(j+.5)*c**(-j-.5)+(j/(E*c))**j if j else 1+math.sqrt(math.pi/c)
res={"P0":[0,0],"P1":[0,0],"P2":[0,0],"P3":[0,0],"P4":[0,0],"P4b":[0,0],"P5":[0,0],"P5b":[0,0]}
fails=[];minratio={}
def rec(k,ok,info=None):
    res[k][0]+=1
    if not ok: res[k][1]+=1; fails.append((k,info))
for c in cs:
    for j in range(5):
        # P0 unimodal
        xs=[(i+1)*(4*math.sqrt(max(j,1)/c)+5/math.sqrt(c))/2000 for i in range(2000)]
        d=[(2*j-2*c*x*x)/x for x in xs]  # sign of f'/f
        if j==0: uni=all(v<0 for v in d)
        else:
            xm=math.sqrt(j/c); uni=all((v>0)==(x<xm) for v,x in zip(d,xs) if abs(x-xm)>1e-9)
        rec("P0",uni,(j,c))
        t=th(j,c); b=B(j,c); tol=1e-12*max(1,b)
        rec("P1" if j==0 else "P2",t<=b+tol,(j,c,t,b))
        r=t/b; minratio[j]=max(minratio.get(j,0),r)
        if j>=1: rec("P3",t<=B1(j,c)+tol,(j,c,t,B1(j,c)))
# T3
def brute(c,q):
    N=int(math.sqrt(45/c))+2; e=[math.exp(-c*k*k) for k in range(N+1)]
    s=0.0
    for a in range(-N,N+1):
        for b in range(-N,N+1):
            eab=e[abs(a)]*e[abs(b)]; r2=a*a+b*b
            for g in range(-N,N+1):
                n2=r2+g*g
                s+=(n2**(q//2))*eab*e[abs(g)]
    return s
for c in cs:
    t0,t1,t2=th(0,c),th(1,c),th(2,c); b0,b1,b2=B(0,c),B(1,c),B(2,c)
    u2=3*t1*t0**2; u4=3*t2*t0**2+6*t1**2*t0
    rec("P4b",3*b1*b0**2>=u2*(1-1e-12),(c,)); rec("P5b",3*b2*b0**2+6*b1**2*b0>=u4*(1-1e-12),(c,))
    if c>=0.05 and cs.index(c)%12==0:
        for q,u,k in((2,u2,"P4"),(4,u4,"P5")):
            bf=brute(c,q); rec(k,abs(bf-u)<=1e-9*u,(c,q,bf,u))
print({k:v for k,v in res.items()}); print("max ratio theta/bound by j",minratio)
for f in fails[:12]: print("FAIL",f)
print("P3 min margin info above")
bad=res["P0"][1]+res["P1"][1]+res["P2"][1]+res["P4"][1]+res["P4b"][1]+res["P5"][1]+res["P5b"][1]
sys.exit(1 if bad else 0)
