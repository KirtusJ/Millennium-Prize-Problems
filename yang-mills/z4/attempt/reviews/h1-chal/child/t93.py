"""T93: trial-state Q, nu_trial at beta=64,256,1024.  numpy only, deterministic (no RNG; seed n/a).
Predicates fixed before first run:
 P1 Parseval: |sum_n c_n^2 - <g1,g1>| < 1e-10 (tolerance: GL double-precision rounding + n-truncation; checked at nmax and 2*nmax)
 P2 Doubling: beta^(1/3)*nu changes by < 1e-9 when (Na,Nu,M,nmax) all doubled. Source: quad converges geometrically for analytic integrands.
 P3 Sanity: 0 < <g,Kg> <= <g,g>; W>=0 so <g,Wg> >= 0; 0<Q<1.
 P4 (all three beta) d=beta^(1/3)nu - E_trial: reported; d*beta^(1/3) bounded-ness is MEASURED ONLY (3 points cannot prove O()).
 P5 beta^(1/3)nu vs E_0=3.3505330: measured only (E_0 is continuum, finite-beta nu_0 differs).
 P6 Bessel check: kappa_0==1 within 1e-12 and kappa_n decreasing in n.
Result file opened mode 'x'."""
import numpy as np, sys, json
E0=3.3505330; al=2**(-1/3); Et=3*al+3/(4*al**2)
def kappas(beta,nmax,M):
    t=(np.arange(M)+.5)*np.pi/M
    e=np.exp(beta*(np.cos(t)-1))
    n=np.arange(1,nmax+3)
    I=np.array([ (e*np.cos(k*t)).mean() for k in n])  # I_k e^-beta, k=1..nmax+2
    return I[1:nmax+2]/I[0]   # I_{n+1}/I_1, n=0..nmax
def run(beta,Na,Nu,M,nmax):
    f=lambda a:np.exp(-al*beta**(2/3)*a*a)
    g1=lambda a:f(a)+f(np.pi-a)
    x,w=np.polynomial.legendre.leggauss(Na)
    a=(x+1)*np.pi/4; wa=w*np.pi/4            # [0,pi/2]
    # full [0,pi] by symmetry about pi/2 (g1,sin^2 symmetric): factor 2
    mu=lambda a:(2/np.pi)*np.sin(a)**2
    gg1=2*np.sum(wa*mu(a)*g1(a)**2)
    # c_n on full [0,pi] with own grid
    x2,w2=np.polynomial.legendre.leggauss(2*Na); a2=(x2+1)*np.pi/2; w2=w2*np.pi/2
    n=np.arange(nmax+1)
    c=np.array([np.sum(w2*(2/np.pi)*g1(a2)*np.sin(a2)*np.sin((k+1)*a2)) for k in n])
    kap=kappas(beta,nmax,M)
    par=abs(np.sum(c**2)-np.sum(w2*mu(a2)*g1(a2)**2))
    k1=np.sum(kap*c**2)
    # W
    u,wu=np.polynomial.legendre.leggauss(Nu); wu=wu/2   # density 1/2 du
    A1,A2,U=np.meshgrid(a,a,u,indexing='ij')
    V=2*beta*np.sin(A1)**2*np.sin(A2)**2*(1-U**2)
    wt=(wa*mu(a)*g1(a)**2)
    wW=np.einsum('i,j,k,ijk->',wt,wt,wu,np.expm1(V))*4   # factor 2 per angle
    GG=gg1**2; GK=k1**2
    Q=(GG-GK+wW)/(GG+wW); nu=-np.log(GK/(GG+wW))
    return dict(beta=beta,GG=GG,GK=GK,GW=wW,Q=Q,nu=nu,b13nu=beta**(1/3)*nu,parseval=par,kap0=kap[0],kapmono=bool(np.all(np.diff(kap)<0)))
out={}
for beta in (64,256,1024):
    r1=run(beta,200,100,40000,300); r2=run(beta,400,200,80000,600)
    r2['doubling_change_b13nu']=abs(r1['b13nu']-r2['b13nu']); r2['doubling_change_Q']=abs(r1['Q']-r2['Q'])
    r2['parseval1']=r1['parseval']
    d=r2['b13nu']-Et; r2['d']=d; r2['d_times_b13']=d*beta**(1/3); r2['minus_E0']=r2['b13nu']-E0
    out[beta]=r2
    print(json.dumps(r2))
json.dump(dict(Et=Et,E0=E0,res=out),open('result_t93.json','x'),indent=1)
fails=[]
for b,r in out.items():
    if r['parseval']>=1e-10 or r['parseval1']>=1e-10: fails.append(('P1',b,r['parseval'],r['parseval1']))
    if r['doubling_change_b13nu']>=1e-9: fails.append(('P2',b,r['doubling_change_b13nu']))
    if not(0<r['GK']<=r['GG'] and r['GW']>=0 and 0<r['Q']<1): fails.append(('P3',b))
    if abs(r['kap0']-1)>1e-12 or not r['kapmono']: fails.append(('P6',b,r['kap0'],r['kapmono']))
print('Et',Et,'FAILS',fails)
sys.exit(1 if fails else 0)
