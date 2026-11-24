"""S1,S2,S3 recomputation. Usage: python3 s1_s2_s3.py [tag]   (results file results_s123_<tag>.txt, mode 'x')
Predicates fixed BEFORE first run:
 S1a: for every grid point (k,theta): p_k(theta) <= min(1, C(1+k)^1.5 theta^3), C=pi^2 sqrt(e)/4, slack 1e-12 (float64 quadrature error
      budget: Gauss-Legendre 400 panels x 10 nodes on smooth integrand, expected <1e-13).
 S1b: the ratio of the two derivation bounds (theta^3/3)/((4/pi^2)e^-.5 (1/3)(1+k)^-1.5) equals C(1+k)^1.5 theta^3 to rel 1e-13.
 S1c: derivation side conditions: (1+k)^-1/2 <= pi/2 and k(1-cos r)<=1/2 on [0,(1+k)^-1/2] checked on grid, and sin r>=2r/pi there.
 S2: p_k(0.05),p_k(0.2),p_k(0.6) at k=6*3.399810242 round to the stated 3 s.f. (0.00307,0.156,0.935). Tolerance = half unit of the 3rd s.f.
 S3: M*C*(1+6b)^1.5*theta^3 == 3 pi^2 sqrt(e)/32 c^3/N, rel 1e-12 (float64 rounding), several N,c,b; plus algebra by hand in notes.
 Hypothesis count for 'for all' claims: number of grid cases tested and number qualifying are reported."""
import sys, numpy as np
tag=sys.argv[1] if len(sys.argv)>1 else "run1"
x,w=np.polynomial.legendre.leggauss(10)
def integ(k,a,b,panels=400):
    e=np.linspace(a,b,panels+1); lo=e[:-1,None]; hi=e[1:,None]
    r=(hi-lo)/2*x[None,:]+(hi+lo)/2
    return np.sum((hi-lo)/2*w[None,:]*np.sin(r)**2*np.exp(k*(np.cos(r)-1)))
def p(k,th):
    return integ(k,0,th)/integ(k,0,np.pi)
C=np.pi**2*np.sqrt(np.e)/4
out=[]; P=out.append
P(f"C=pi^2 sqrt(e)/4 = {C:.12f}")
ks=sorted(set([0,1e-3,0.01,0.1,0.5,1,2,3,5,6,10,20.398861452,30,50,75,100,150,200]+list(np.linspace(0,200,21))))
ths=sorted(set(list(np.linspace(0,np.pi,81))+[1e-3,1e-2,0.05,0.1,0.2,0.3,0.6,np.pi]+[ (1+k)**-.5 for k in ks if (1+k)**-.5<=np.pi]))
n=0;viol=0;maxr=0;arg=None;maxrel_ratio=0;side=0
for k in ks:
    for th in ths:
        if th==0: continue
        n+=1
        pv=p(k,th); B=C*(1+k)**1.5*th**3
        rt=pv/B
        if rt>maxr: maxr,arg=rt,(k,th)
        if pv>min(1,B)+1e-12: viol+=1; P(f"VIOL k={k} th={th} p={pv} B={B}")
        # S1b
        r1=(th**3/3)/((4/np.pi**2)*np.exp(-.5)*(1/3)*(1+k)**-1.5)
        maxrel_ratio=max(maxrel_ratio,abs(r1-B)/B)
    a=(1+k)**-.5
    rr=np.linspace(0,a,2001)
    ok=(a<=np.pi/2) and np.all(k*(1-np.cos(rr))<=.5+1e-15) and np.all(np.sin(rr)>=2*rr/np.pi-1e-15)
    side+=bool(ok)
P(f"S1a: cases={n}, qualifying (p<=min(1,B)+1e-12)={n-viol}, violations={viol}")
P(f"S1a: max p/B = {maxr:.9f} at (k,theta)={arg}")
P(f"S1b: max rel diff of bound-ratio vs C(1+k)^1.5 th^3 = {maxrel_ratio:.2e} (PASS if <1e-13)")
P(f"S1c: side conditions hold for {side}/{len(ks)} values of k")
b=3.399810242; k=6*b
P(f"S2: k=6beta={k:.9f}")
S2={0.05:0.00307,0.2:0.156,0.6:0.935}
s2ok=True
for th,st in S2.items():
    v=p(k,th); import math
    dec=len(str(st).split('.')[1]); tol=0.5*10**-dec
    ok=abs(v-st)<=tol; s2ok&=ok
    P(f"S2: p_k({th}) = {v:.9f}  stated {st}  |diff|={abs(v-st):.2e} tol={tol:.1e} {'PASS' if ok else 'FAIL'}")
P("S2 overall "+("PASS" if s2ok else "FAIL"))
mx=0;cnt=0
for N in [1,2,3,10,100,1000]:
    for c in [0.1,1,2.5]:
        for bb in [0,1,3.399810242,10]:
            M=3*(N/2)**3; th=c*(1+6*bb)**-.5*N**(-4/3)
            lhs=M*C*(1+6*bb)**1.5*th**3; rhs=3*np.pi**2*np.sqrt(np.e)/32*c**3/N
            mx=max(mx,abs(lhs-rhs)/rhs);cnt+=1
P(f"S3: {cnt} cases, max rel diff {mx:.2e} (PASS if <1e-12). Algebra: 3N^3/8 * C * c^3 N^-4 = 3 pi^2 sqrt(e) c^3/(32 N) since (1+6b)^1.5*(1+6b)^-1.5=1, (N^-4/3)^3=N^-4.")
P("S3 "+("PASS" if mx<1e-12 else "FAIL"))
P("S1 verdict: "+("PASS" if viol==0 and maxrel_ratio<1e-13 else "FAIL"))
f=open(f"results_s123_{tag}.txt","x"); f.write("\n".join(out)+"\n"); f.close(); print("\n".join(out))
