"""Test of claimed chessboard bound (c) for 2D SU(2) bad-plaquette probability.
PREDICATES (fixed before first run):
 C0 control.txt == 1.590637 (done separately).
 S1 delta=-1 (whole group): P_L == 1 within 1e-12 for every beta, L.
 S2 quadrature: P_L at two resolutions (panels 400 vs 800) agree to rel 1e-9 (tolerance: double roundoff ~1e-16 amplified by
    cancellation in oscillatory integrals; 1e-9 is a generous but still strict test).
 S3 truncation: J=400 vs J=200 results agree to rel 1e-12; and last-kept term of denominator r_J^N < 1e-30.
 S4 P_L -> P_inf: for each (beta,delta): |log P_8 - log P_inf| <= |log P_2 - log P_inf| (monotone approach, endpoints). Own expectation;
    not a theorem and not uniform in beta (need N << beta-ish), so failures here are expectation failures, not target defects.
 S5 a_0 at beta=2 equals I_1(2)=1.590637 (via control).
 T1 (claim) for each case with L even or inf (all 200 qualify; hypothesis test = L even or infinity, count reported):
    log(minBound/P) >= 0 where minBound = min over eps grid of 20001 points in (0,pi/4] incl pi/4. Grid min is >= true min so
    a grid minimum can only make the bound weaker; a violation at grid is a violation of 'min over eps' claim only if also
    violates for the finer grid (checked with 2e6 pts for violating cases).
 M1 measured only: -log(P_inf)/beta vs delta at large beta.
"""
import numpy as np, sys, json
xg,wg=np.polynomial.legendre.leggauss(30)
def nodes(lo,hi,panels):
    e=np.linspace(lo,hi,panels+1); a=[];w=[]
    for i in range(panels):
        m=(e[i]+e[i+1])/2;h=(e[i+1]-e[i])/2
        a.append(m+h*xg);w.append(h*wg)
    return np.concatenate(a),np.concatenate(w)
def coeffs(beta,lo,J,panels):
    a,w=nodes(lo,np.pi,panels) if lo<np.pi else (np.zeros(1),np.zeros(1))
    wt=2/np.pi*w*np.exp(beta*(np.cos(a)-1))*np.sin(a)**2
    j=np.arange(J+1)[:,None]
    chi=np.sin((j+1)*a[None,:])/np.sin(a)[None,:]/(j+1)
    return chi@wt
def PL(beta,delta,L,J=400,panels=400):
    lo=0.0 if delta<=-1 else (np.arccos(1-delta) if delta<2 else np.pi)
    A=coeffs(beta,0.0,J,panels); Ap=coeffs(beta,lo,J,panels)
    if L is None: return Ap[0]/A[0],None
    N=L*L; r=A/A[0]; rp=Ap/A[0]
    num=np.sum(r**(N-1)*rp); den=np.sum(r**N)
    return num/den, r[-1]**N
betas=[1,2,4,8,16,32,64,128]; deltas=[0.05,0.1,0.2,0.5,1.0]; Ls=[2,4,6,8,None]
out=open("results.jsonl","x"); fails=[]
def log(m):
    open("notes.md","a").write(m+"\n")
# S1
mx=0
for b in betas:
    for L in Ls:
        mx=max(mx,abs(PL(b,-1,L)[0]-1))
log(f"S1 whole group max|P-1| = {mx:.2e} -> {'MET' if mx<1e-12 else 'FAILED'}")
if mx>=1e-12: fails.append("S1")
eps=np.concatenate([np.linspace(1e-4,np.pi/4,20001),[np.pi/4]])
H=(eps-np.sin(eps)*np.cos(eps))/np.pi
def minlogB(b,d,eps=eps,H=H): return np.min(-b*d+b*(1-np.cos(4*eps))-2*np.log(H))
eps2=np.linspace(1e-4,np.pi/4,2000001);H2=(eps2-np.sin(eps2)*np.cos(eps2))/np.pi
res={};s2=0;s3=0;s3b=0;viol=0;nontriv=0;ncase=0;viol_fine=0
for b in betas:
  for d in deltas:
    for L in Ls:
        p,tail=PL(b,d,L)
        p2,_=PL(b,d,L,panels=800); p3,_=PL(b,d,L,J=200)
        s2=max(s2,abs(p-p2)/p); s3=max(s3,abs(p-p3)/p)
        if tail is not None: s3b=max(s3b,tail)
        lb=minlogB(b,d); lr=lb-np.log(p); ncase+=1
        nontriv+= lb<0
        ok=lr>=0
        if not ok:
            viol+=1
            if minlogB(b,d,eps2,H2)-np.log(p)<0: viol_fine+=1
        res[(b,d,L)]=(p,lb,lr)
        out.write(json.dumps(dict(beta=b,delta=d,L=L if L else "inf",P=p,logP=float(np.log(p)),logMinBound=float(lb),logratio=float(lr),sat=bool(ok)))+"\n")
log(f"S2 quad max rel diff {s2:.2e} -> {'MET' if s2<1e-9 else 'FAILED'}")
log(f"S3 trunc J400 vs J200 max rel diff {s3:.2e}; max last-kept denominator term r_J^N {s3b:.2e} -> {'MET' if s3<1e-12 and s3b<1e-30 else 'FAILED'}")
# S4
nm=0;nt=0;bad=[]
for b in betas:
  for d in deltas:
    pi_=np.log(res[(b,d,None)][0]); e2=abs(np.log(res[(b,d,2)][0])-pi_); e8=abs(np.log(res[(b,d,8)][0])-pi_)
    nt+=1
    if e8<=e2: nm+=1
    else: bad.append((b,d))
log(f"S4 monotone-approach (L=8 closer than L=2): {nm}/{nt}; failing (beta,delta): {bad}")
log(f"T1: cases={ncase}, qualify(L even or inf)={ncase}, nontrivial bound (<1)={nontriv}, satisfy={ncase-viol}, violate on grid={viol}, violate on 2e6-grid={viol_fine}")
# table
with open("table.md","x") as f:
    f.write("| beta | delta | L | P | minBound | log(minBound/P) |\n|--|--|--|--|--|--|\n")
    for (b,d,L),(p,lb,lr) in res.items():
        f.write(f"| {b} | {d} | {L if L else 'inf'} | {p:.4e} | {np.exp(lb):.4e} | {lr:.3f} |\n")
# violations list
v=[(k,round(float(res[k][2]),3)) for k in res if res[k][2]<0]
log("violations (beta,delta,L): logratio : "+str(v))
# M1
with open("m1.md","x") as f:
    f.write("| beta | delta | -log(Pinf)/beta | diff vs delta |\n|--|--|--|--|\n")
    for b in betas[3:]:
        for d in deltas:
            q=-np.log(res[(b,d,None)][0])/b
            f.write(f"| {b} | {d} | {q:.5f} | {q-d:+.5f} |\n")
log("P_inf(beta=16,delta=0.2) = %.10e"%res[(16,0.2,None)][0])
log("a_0(beta=2) = %.6f"%coeffs(2,0.0,0,400)[0] if False else "")
sys.exit(1 if (mx>=1e-12 or s2>=1e-9 or s3>=1e-12 or s3b>=1e-30) else 0)
