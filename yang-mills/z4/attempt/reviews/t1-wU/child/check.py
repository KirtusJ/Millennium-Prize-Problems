"""check.py -- numeric fidelity checks for src/tun_upper.tex (task T170). numpy only, no randomness (grids), 1 core.
Predicates fixed BEFORE the first run (tolerance sources in brackets):
 C1  c* = int_0^pi sqrt(2*2asinh(sin a)) da  within 5e-7 of 4.6054132   [quoted 7 digits => 5e-8; quadrature slack x10]
 C2  L = sqrt(4 asinh 1) within 5e-5 of 1.8776                          [quoted 4 digits => 5e-5]
 C3  D(1)=1-1/2-sqrt(2pi)e^{-1}/2 > 0.039 (the tex claim "D(1)>0.039"). My prior: FALSE (0.0389). Also D>0 and increasing on beta in [1,60] grid.
 C4  I1 lower bound I1(z) >= e^z(1-1/(2z))/sqrt(2 pi z) - 1/2 for z in logspace(-2,3,400)  [exact float compare, margin>=-1e-12 relative]
 C5  Bessel envelope e^{-z}I0(z) <= min(1,H_delta(z)), z in logspace(-2,3,300) x delta in {.05,.1,.25,.5,.75,1}  [slack 1e-12]
 C6  Outer exponent Phi_out(r) <= -(r^2/64)(1-A^-2)^2 ; r in [0,1] (101 pts), c in {0,.01,.05,.2,1,2.9,5} ; max over q on 40001-angle grid
     [grid under-estimates the max by <= (pi/40000)^2*|p|/2 ~ 3e-9, so slack 1e-8]
 C7  Taylor step gamma_r(1-gamma/8) <= -gamma^2/16, same (r,c) grid; hypothesis gamma in [0,1/2) counted
 C8  weight lemma (3) scalars: for eps>=3eta: sqrt(2eps)-sqrt(2(eps-2eta)) <= 2 sqrt(eta); for eps<3eta: sqrt(2eps) <= sqrt(6 eta); eta in {.01..0.5}
 C9  Lemma K first bound, exact LHS (radial reduction, angular average of cosh = sinh(x)/x) <= RHS; beta in {16,64,256,1024,4096}, |p| in {.25,.5,1,2,3},
     H in {0,1}, eta in {beta^-1/8, .5, 1}; only cases with beta'>0 qualify (count reported). Quadrature: trapezoid 400001 pts in log domain.
 C10 master-bound deficit log max(M_in, A M_out), tau=delta=beta^-1/3: (a) beta in {256,1024,4096}, s in 0.01-grid [0.1,1]: all within [8.5,14.3]
     (tex: "8.6 to 14"; CHAL 8.58-14.23); (b) first beta on grid 10^(k/20) with max_{s in[.1,1]} deficit<0.2 lies in [1e13,1e14] (tex: 2.2e13).
     only beta>125 qualify (tau<1/5).
 C11 C(eta)=1+(e^{eta/2}-e^{-eta/4})/(e^{-eta/4}-e^{-eta/2}) finite >=1 on eta in (0,1/2]; e^{eta/4}<=2.
Results to result_check.json (mode 'x').
"""
import numpy as np, json, math, sys
tag=sys.argv[1]
res={}; fails=[]
def rec(name,ok,**kw):
    res[name]=dict(ok=bool(ok),**kw)
    if not ok: fails.append(name)
# Bessel scaled: e^{-z} I_n(z) = (1/pi) int_0^pi e^{-z(1-cos t)} cos(nt) dt (trapezoid on periodic-even integrand => spectral accuracy)
def sI(n,z,N=200001):
    t=np.linspace(0,np.pi,N); w=np.ones(N); w[0]=w[-1]=.5
    return np.array([ (np.exp(-zz*(1-np.cos(t)))*np.cos(n*t)*w).sum()*(np.pi/(N-1))/np.pi for zz in np.atleast_1d(z)])
# C1,C2
u,wt=np.polynomial.legendre.leggauss(400); sq=np.pi**0.5  # a=pi*v^2, v in [0,1]: da=2 pi v dv
v=(u+1)/2; wv=wt/2; a=np.pi*v**2
cstar=float((np.sqrt(2*2*np.arcsinh(np.sin(a)))*2*np.pi*v*wv).sum())
rec('C1',abs(cstar-4.6054132)<5e-7,cstar=cstar)
Lv=math.sqrt(4*math.asinh(1)); rec('C2',abs(Lv-1.8776)<5e-5,L=Lv)
# C3
D=lambda b:1-1/(2*b)-math.sqrt(2*math.pi*b)*math.exp(-b)/2
bs=np.linspace(1,60,2000); Ds=np.array([D(b) for b in bs])
rec('C3_D1_gt_0.039',D(1)>0.039,D1=D(1))
rec('C3b_D_pos_incr',bool((Ds>0).all() and (np.diff(Ds)>0).all()),n=len(bs))
# C4
zs=np.logspace(-2,3,400); i1=sI(1,zs)  # scaled e^{-z}I1
lb=(1-1/(2*zs))/np.sqrt(2*np.pi*zs)-0.5*np.exp(-zs)
rec('C4',bool((i1>=lb-1e-12).all()),n=len(zs),min_margin=float((i1-lb).min()))
# C5
zs=np.logspace(-2,3,300); i0=sI(0,zs); bad=0;n=0;mm=1e9
for d in [.05,.1,.25,.5,.75,1.0]:
    H=1/np.sqrt(2*np.pi*zs*(1-5*d*d/48))+np.exp(-zs*(1-np.cos(d)))
    env=np.minimum(1,H); m=(env-i0).min(); mm=min(mm,m); bad+=int((i0>env+1e-12).sum()); n+=len(zs)
rec('C5',bad==0,n=n,bad=bad,min_margin=float(mm))
# C6, C7
q=np.linspace(0,2*np.pi,40001); n6=0;bad6=0;n7=0;bad7=0;qual7=0;mm6=1e9
for c in [0,.01,.05,.2,1,2.9,5]:
    A=1+2*c
    for r in np.linspace(0,1,101):
        R=math.sqrt(1-r);rho=math.sqrt(r)
        mx=(R*np.cos(q)+rho*np.sin(q)-c*np.sin(q)**2).max()   # q=(cos,sin), q2=sin
        Phi=c/A*r-1+mx; bnd=-(r*r/64)*(1-1/A**2)**2
        n6+=1; mm6=min(mm6,bnd-Phi)
        if Phi>bnd+1e-8: bad6+=1
        g=r/2*(1-1/A**2)
        if 0<=g<.5:
            qual7+=1; mu=1-g/8
            gr=(1-r)/(2*mu)+r/(2*(mu+2*c))+mu/2-1+c/A*r
            n7+=1
            if gr>-g*g/16+1e-12: bad7+=1
rec('C6',bad6==0,n=n6,bad=bad6,min_margin=float(mm6))
rec('C7',bad7==0,n=n7,qualifying=qual7,bad=bad7)
# C8
bad=0;n=0
for eta in [.01,.05,.1,.25,.5]:
    for eps in np.linspace(1e-6,3,3000):
        n+=1
        if eps>=3*eta:
            if math.sqrt(2*eps)-math.sqrt(2*(eps-2*eta))>2*math.sqrt(eta)+1e-12: bad+=1
        else:
            if math.sqrt(2*eps)>math.sqrt(6*eta)+1e-12: bad+=1
rec('C8',bad==0,n=n,bad=bad)
# C9
th=np.linspace(0,np.pi,400001); dth=th[1]-th[0]; wq=np.ones_like(th); wq[0]=wq[-1]=.5
def lse(x): m=x.max(); return m+math.log(np.exp(x-m).sum())
n9=0;q9=0;bad9=0;worst=-1e9
for b in [16,64,256,1024,4096]:
    sb=math.sqrt(b)
    # log Z (including (2/pi)sin^2 density): log int e^{b cos t}(2/pi) sin^2 t
    ls=np.where(th>0,2*np.log(np.maximum(np.sin(th),1e-300)),-np.inf)
    base=b*np.cos(th)+ls+math.log(2/math.pi)+np.log(wq*dth)
    logZ=lse(base)
    for pn in [.25,.5,1,2,3]:
        for H in [0,1]:
            for eta in [b**-.125,.5,1.0]:
                n9+=1; bp=b*(1-5*eta**2/48)-sb*H
                if bp<=0: continue
                q9+=1
                x=sb*pn*th; lsh=np.where(x>1e-8,x+np.log1p(-np.exp(-2*np.maximum(x,1e-8)))-math.log(2)-np.log(np.maximum(x,1e-300)),0.0)
                lhs=lse(base+lsh+sb*H*th**2/2)-logZ
                rhs=-math.log(1-1/b)+math.log((b/bp)**1.5*math.exp(pn**2*b/(2*bp))+(b/(2*math.pi))**1.5*2*math.pi**2*math.exp(-b*(1-math.cos(eta))+sb*(pn*math.pi+H*math.pi**2/2)))
                worst=max(worst,lhs-rhs)
                if lhs>rhs+1e-9: bad9+=1
rec('C9',bad9==0,n_total=n9,qualifying=q9,bad=bad9,max_lhs_minus_rhs=worst)
# C10
def deficit(b,s):
    tau=delta=b**(-1/3); A=1+2*s*s+2*s*math.sqrt(1+s*s); Dd=D(b)
    lMin=math.log((1/Dd)*(((1-tau)*(1-4*tau)*(1-5*delta**2/48))**-.5+math.sqrt(2*math.pi*b)*math.exp(-b*(1-5*tau)*(1-math.cos(delta)))+math.sqrt(2*math.pi*b)*math.exp(-b*A*tau/2)))
    lMout=math.log(b*math.sqrt(2*math.pi*b)/(2*Dd))-b*tau**2/64*(1-1/A**2)**2
    return max(lMin,math.log(A)+lMout)
ss=np.round(np.arange(0.1,1.0001,0.01),2); rng=[]
for b in [256,1024,4096]:
    d=[deficit(b,s) for s in ss]; rng+=d
rec('C10a',min(rng)>=8.5 and max(rng)<=14.3,n=len(rng),min=min(rng),max=max(rng))
first=None
for k in range(200,320):
    b=10**(k/20)
    if max(deficit(b,s) for s in ss)<0.2: first=b;break
rec('C10b',first is not None and 1e13<=first<=1e14,first_beta=first)
# C11
bad=0
for eta in np.linspace(1e-3,.5,500):
    C=1+(math.exp(eta/2)-math.exp(-eta/4))/(math.exp(-eta/4)-math.exp(-eta/2))
    if not(np.isfinite(C) and C>=1 and math.exp(eta/4)<=2): bad+=1
rec('C11',bad==0,bad=bad)
with open(f'result_check_{tag}.json','x') as f: json.dump(res,f,indent=1)
for k,v in res.items(): print(k,v)
print('FAILED:',fails); sys.exit(1 if fails else 0)
