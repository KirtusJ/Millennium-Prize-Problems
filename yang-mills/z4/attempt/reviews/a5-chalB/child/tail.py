"""Claim S3a(2D): P_beta(O>t) <= C exp(-t/8), beta>=2. O = beta(1-cos a), a-density ∝ sin^2 a exp(beta cos a).
P(O>t) = int_{a0}^pi w / int_0^pi w, a0=arccos(1-t/beta), w=exp(beta(cos a-1)) sin^2 a, Gauss-Legendre.
PREDICATES (fixed before first run):
 P1 quadrature convergence: |P_2000 - P_4000| <= 1e-9*P  (rel; analytic integrand, GL error is far below; 1e-9 is
    chosen as 3 orders under the 6-digit reporting level) for every (beta,t) with P>0.
 P2 mean: |<O>_quad - beta(1-I2/I1)| <= 1e-9*mean, I_n by power series recurrence (independent of quadrature).
 P3 per-case hypothesis H(beta,t): P*exp(t/8) <= 2 (C=2 is my chosen test constant; the claim gives none, and
    P(O>0)=1 forces C>=1). Report met/failed over all (beta,t) cases, and per beta.
 P4 rate: r(beta)=-log P/t at t=min(20,1.9beta) must be >= 1/8 for every beta.
 P5 Gamma(3/2) limit: sup_t|P_beta-Q| strictly decreasing in beta (my expectation; measured, not a claim of the target).
 P6 monotone: P nonincreasing in t (sanity of the code).
Outputs: results_tail.csv (mode x), prints summary.
"""
import numpy as np, math
def GL(n,lo,hi):
    x,w=np.polynomial.legendre.leggauss(n); return (x+1)*(hi-lo)/2+lo, w*(hi-lo)/2
def wt(b,a): return np.exp(b*(np.cos(a)-1))*np.sin(a)**2
def P(b,t,n):
    if t>=2*b: return 0.0
    a0=math.acos(1-t/b); x,w=GL(n,a0,math.pi); xd,wd=GL(n,0,math.pi)
    return (w*wt(b,x)).sum()/(wd*wt(b,xd)).sum()
def In(nu,z):
    T=(z/2)**nu/math.factorial(nu); s=0.0
    for k in range(4000):
        s+=T; T*=(z/2)**2/((k+1)*(k+1+nu))
    return s
def Q(t): return math.erfc(math.sqrt(t))+2*math.sqrt(t/math.pi)*math.exp(-t)  # Gamma(3/2,t)/Gamma(3/2)
betas=[2,4,8,16,32,64,128,256]; ts=[0.25*i for i in range(0,161)]
res={}; f=open("results_tail.csv","x"); f.write("beta,t,P,Pexp\n")
met=fail=0; p1f=0; p6f=0; per={}
for b in betas:
    prev=1.0; per[b]=[0,0]
    for t in ts:
        if t>2*b: continue
        p=P(b,t,2000); p2=P(b,t,4000)
        if p>0 and abs(p-p2)>1e-9*p: p1f+=1
        if p>prev*(1+1e-12): p6f+=1
        prev=p; res[(b,t)]=p
        v=p*math.exp(t/8); f.write(f"{b},{t},{p!r},{v!r}\n")
        if v<=2: met+=1; per[b][0]+=1
        else: fail+=1; per[b][1]+=1
f.close()
print("P1 failures",p1f,"P6 failures",p6f)
print("P3 cases met/failed/measured-only: %d/%d/0"%(met,fail)); print("per beta (met,fail):",per)
cmax=max((p*math.exp(t/8),b,t) for (b,t),p in res.items()); print("C_emp",cmax)
for b in betas:
    cb=max((p*math.exp(t/8),t) for (bb,t),p in res.items() if bb==b)
    tr=min(20,1.9*b); p=P(b,tr,2000); r=-math.log(p)/tr
    # sup |P-Q| over t in [0,20] on 0.05 grid
    tt=np.arange(0,20.0001,0.05); d=max(abs(P(b,t,2000)-Q(t)) for t in tt)
    xq,wq=GL(4000,0,math.pi); dens=wt(b,xq); mean=b*(1-((wq*dens*np.cos(xq)).sum()/(wq*dens).sum()))
    ex=b*(1-In(2,b)/In(1,b))
    print(f"beta={b} sup_t Pe^(t/8)={cb[0]:.6f}@t={cb[1]} t_ref={tr} r={r:.6f} sup|P-Q|={d:.6e} mean_quad={mean:.9f} mean_exact={ex:.9f} rel={abs(mean-ex)/ex:.2e} P2ok={abs(mean-ex)<=1e-9*ex} P4ok={r>=0.125}")
