"""PREDICATES (fixed before first run). usage: python3 grid.py RESULTFILE
Tolerance TOL=1e-12: float64 roundoff of sums of O(1) terms (eps 2.2e-16 * ~1e3 safety); a predicate fails if
slack < -TOL. Hypothesis-per-case: a 'case' is one (eta,S) pair; it is MET if the inequality holds for every
sampled (x,y,a,b) in it (rule 4). Point counts are also reported.
 N1: F <= 1-m for eta,S in [s_lo,s_hi], x in[0,1], y in[0,1], a in[0,exp(-3eta/4)], b in[0,exp(-1/16)].
 N2: F <= 1-m/2 for x in[0,1], a in[0,exp(-3eta/4)], b in[0,1], y in[0,m/2].
 N3: MA2(eta) <= Mc2(eta), slack Mc2-MA2 >= -TOL (also reported: values at eta=.4,.2,.1,.05,.01).
 G : my recomputation equals grandchild's numbers (MA2,Mc2 at .4,.01; P(s_lo)+exp(-1/16) at .01) to rel 1e-9
     (1e-9 = grandchild printed 12 digits, allow libm differences).
Sampling: F is bilinear in (a,y) and linear in b,y, so extremes over a,b,y are at corners -> corners x fine x grid
(2001 pts, F concave in x since gamma in(0,1)); additionally a 5^3 interior lattice of (a,b,y) with 101 x-pts to
check the corner argument (expectation: no interior point beats corners). Eta grid: 80 log-spaced in [1e-4,0.4]
plus the named values. S grid: 120 points uniform in [s_lo,s_hi] plus both ends. Fixed seed unused (deterministic grid)."""
import sys, json, math
import numpy as np
TOL=1e-12
def e(S): return 2*np.arcsinh(S)
def k(S): return np.sqrt(1+S*S)/S
def gam(S): return 1-1/k(S)
def coth(t): return 1/np.tanh(t)
m1=(1-math.exp(-1/16))/2
def m0f(eta): return (1-math.exp(-0.75*eta))/2
def MA2(eta):
    r02=eta*math.sinh(eta)/4; m0=m0f(eta)
    return 2*math.sqrt(2+r02)+max(coth(eta)*math.log(1/m1), 0.75*eta*coth(eta)+math.log(1/m0))
def Mc2(eta):
    C=e(math.sqrt(2))+eta+1/8+1
    return (math.sqrt(2)/math.sinh(eta))*(e(math.sqrt(2))+1)+math.log(4)-math.log(math.expm1(eta/2))+C
def P(S,eta): return np.exp(e(S)-MA2(eta)/k(S))
named=[0.4,0.2,0.1,0.05,0.01,0.001]
etas=sorted(set([float(t) for t in np.geomspace(1e-4,0.4,80)]+named))
xf=np.linspace(0,1,2001); xc=np.linspace(0,1,101)
res={"N1":{},"N2":{},"N3":{},"G":{}}
def run(name,eta):
    m=min(m0f(eta),m1); amax=math.exp(-0.75*eta)
    if name=="N1": bmax=math.exp(-1/16); ymax=1.0; bound=1-m
    else: bmax=1.0; ymax=m/2; bound=1-m/2
    slo=math.sinh(eta); shi=math.sqrt(1+eta*math.sinh(eta)/4)
    S=np.concatenate([np.linspace(slo,shi,120)]); g=gam(S)[:,None]; Pc=P(S,eta)[:,None]
    best=np.full(len(S),np.inf); worst=(np.inf,None)
    def upd(a,b,y,x,tag):
        F=a*(1-x)*(1-y)+Pc*x[None,:]**g+b*y
        sl=bound-F; mn=sl.min(axis=1); nonlocal best,worst
        best=np.minimum(best,mn)
        i,j=np.unravel_index(sl.argmin(),sl.shape)
        if sl[i,j]<worst[0]: worst=(float(sl[i,j]),dict(S=float(S[i]),x=float(x[j]),a=a,b=b,y=y,tag=tag))
        return sl.size
    npts=0
    for a in (0,amax):
        for b in (0,bmax):
            for y in (0,ymax): npts+=upd(a,b,y,xf,"corner")
    for fa in np.linspace(0,1,5):
        for fb in np.linspace(0,1,5):
            for fy in np.linspace(0,1,5): npts+=upd(fa*amax,fb*bmax,fy*ymax,xc,"interior")
    return dict(eta=eta,min_slack=worst[0],worst=worst[1],cases=len(S),cases_met=int((best>=-TOL).sum()),
                cases_failed=int((best<-TOL).sum()),points=npts,points_failed_note="per-case counts above")
for nm in ("N1","N2"):
    for eta in etas: res[nm][repr(eta)]=run(nm,eta)
# N3
fine=sorted(set([float(t) for t in np.geomspace(1e-6,0.4,4000)]+named))
sl=[(Mc2(t)-MA2(t),t) for t in fine]
mn=min(sl)
res["N3"]=dict(points=len(fine),met=sum(1 for s,_ in sl if s>=-TOL),failed=sum(1 for s,_ in sl if s<-TOL),
    min_slack=mn[0],at_eta=mn[1],
    table={repr(t):dict(Mc2=Mc2(t),etaMc2=t*Mc2(t),MA2=MA2(t),etaMA2=t*MA2(t)) for t in [0.4,0.2,0.1,0.05,0.01]})
# G
gc={"MA2_0.4":12.060726371361,"Mc2_0.4":18.047286402488,"MA2_0.01":352.522415570200,"Mc2_0.01":475.721934138243,
    "Psum_0.01":0.969456631752}
mine={"MA2_0.4":MA2(0.4),"Mc2_0.4":Mc2(0.4),"MA2_0.01":MA2(0.01),"Mc2_0.01":Mc2(0.01),
      "Psum_0.01":float(P(math.sinh(0.01),0.01))+math.exp(-1/16)}
res["G"]={q:dict(mine=mine[q],gc=gc[q],ok=bool(abs(mine[q]-gc[q])<=1e-9*abs(gc[q]))) for q in gc}
# summary
summ={}
for nm in ("N1","N2"):
    r=res[nm].values()
    summ[nm]=dict(etas=len(res[nm]),cases_total=sum(v["cases"] for v in r),cases_met=sum(v["cases_met"] for v in r),
      cases_failed=sum(v["cases_failed"] for v in r),min_slack=min(v["min_slack"] for v in r),
      worst=min(r,key=lambda v:v["min_slack"]))
res["summary"]=summ
with open(sys.argv[1],"x") as f: json.dump(res,f,indent=1)
print(json.dumps(summ,indent=1))
print("N1 slack at named eta:",{t:res["N1"][repr(t)]["min_slack"] for t in [0.4,0.1,0.01,0.001]})
print("N3",{k_:v for k_,v in res["N3"].items() if k_!="table"})
for t,v in res["N3"]["table"].items(): print(t,v)
print("G",res["G"])
bad=summ["N1"]["cases_failed"]+summ["N2"]["cases_failed"]+res["N3"]["failed"]+sum(not v["ok"] for v in res["G"].values())
sys.exit(0 if bad==0 else 1)
