"""K(n) via periodic-chain Green function, tau=6, 16^4 lattice.
Closed form (derived: G solves -G(n+1)+(2+m2)G(n)-G(n-1)=delta_n, periodic N=16):
  G(n)=cosh(w(8-|n|))/(2 sinh w sinh 8w), cosh w = 1+m2/2.
Predicates (fixed before first run):
 P1 closed form == direct 16-term sum for every distinct nonzero spatial m2, n=0..4; tol 1e-35 abs
    (50-digit Decimal arithmetic; roundoff ~1e-48, so 1e-35 is generous but still meaningful).
 P2 (independent) plain-float direct 4-fold sum of K(n) agrees with Decimal K(n), rel tol 1e-11
    (65536 terms double precision, roundoff ~1e-15 per term, sums of positives -> 1e-11 safe).
 P3 K(n) all > 0 for n=0, and |K(n)|<=K(0).
 P4 qualifying-case count reported for P1 (all-cases claim: count cases tested).
"""
from decimal import Decimal as D, getcontext
import math, itertools, json
getcontext().prec = 50
L=16; TAU=6
def pi_():
    def atan_inv(x):
        x=D(x); t=1/x; s=t; k=1; x2=x*x
        while abs(t)>D(10)**-55:
            t=-t/x2; k+=2; s+=t/k
        return s
    return 4*(4*atan_inv(5)-atan_inv(239))
PI=pi_()
def cosd(x):
    x=x%(2*PI); s=D(1); t=D(1); k=0
    while abs(t)>D(10)**-55:
        k+=2; t=-t*x*x/(k*(k-1)); s+=t
    return s
c=[cosd(2*PI*l/L) for l in range(L)]
q2=[2-2*ci for ci in c]
def cosh(x): e=x.exp(); return (e+1/e)/2
def sinh(x): e=x.exp(); return (e-1/e)/2
def G_closed(n,m2):
    w=(1+m2/2); w=(w+(w*w-1).sqrt()).ln()
    return cosh(w*(8-abs(n)))/(2*sinh(w)*sinh(8*w))
def G_direct(n,m2):
    return sum(c[(l*n)%L]/(m2+q2[l]) for l in range(L))/L
if __name__=="__main__":
    # P1
    seen={}; maxd=D(0); cases=0
    for l1,l2,l3 in itertools.product(range(L),repeat=3):
        if (l1,l2,l3)==(0,0,0): continue
        m2=q2[l1]+q2[l2]+q2[l3]
        key=str(m2.quantize(D(10)**-40))
        if key in seen: continue
        seen[key]=1
        for n in range(5):
            cases+=1
            maxd=max(maxd,abs(G_closed(n,m2)-G_direct(n,m2)))
    print("P1 distinct m2:",len(seen),"cases:",cases,"max|diff|:",maxd,"PASS" if maxd<D(10)**-35 else "FAIL")
    # K via Green
    K=[D(0)]*5
    for l1,l2,l3 in itertools.product(range(L),repeat=3):
        if (l1,l2,l3)==(0,0,0): continue
        m2=q2[l1]+q2[l2]+q2[l3]; pref=(q2[l1]+q2[l2])*(-2*TAU*m2).exp()
        if pref==0: continue
        for n in range(5): K[n]+=pref*G_closed(n,m2)
    K=[k/L**3 for k in K]
    R=(K[2]**2-2*K[3]**2+K[4]**2)/K[0]**2
    # P2 float direct
    cf=[math.cos(2*math.pi*l/L) for l in range(L)]; qf=[2-2*x for x in cf]
    Kf=[0.0]*5
    for l1,l2,l3,l4 in itertools.product(range(L),repeat=4):
        if not(l1 or l2 or l3 or l4): continue
        S=qf[l1]+qf[l2]+qf[l3]; A=S+qf[l4]
        p=(qf[l1]+qf[l2])/A*math.exp(-2*TAU*S)
        for n in range(5): Kf[n]+=p*cf[(l4*n)%L]
    Kf=[k/L**4 for k in Kf]
    rel=max(abs(Kf[n]-float(K[n]))/abs(float(K[n])) for n in range(5))
    print("P2 max rel diff float-direct vs Green:",rel,"PASS" if rel<1e-11 else "FAIL")
    print("P3",K[0]>0 and all(abs(k)<=K[0] for k in K),"PASS" if K[0]>0 and all(abs(k)<=K[0] for k in K) else "FAIL")
    for n in range(5): print(f"K({n}) = {K[n]:.30e}   float-direct {Kf[n]!r}")
    print(f"R = {R:.30e}")
    with open("K_result.json","x") as f: json.dump({"K":[str(k) for k in K],"R":str(R),"Kfloat":Kf,"P1_maxdiff":str(maxd)},f)
    import sys
    sys.exit(0 if maxd<D(10)**-35 and rel<1e-11 and K[0]>0 else 1)
