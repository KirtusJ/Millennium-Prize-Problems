"""T165 main program. Predicates fixed BEFORE first run:
P1 identity-vs-direct: at beta=16,36, Delta from identity 2<go,W ge>/<go,ge> equals direct lam_e-lam_o (eigh) with
   rel diff < max(1e-6, 1e3*2.2e-16*lam_e/Delta)  [tolerance = double rounding amplified by cancellation; direct is the noisy one].
P2 grid convergence: -log(Delta)/sqrt(beta) on grid n and 1.5n differ < 1e-3 for every beta in 64,256,1024,4096.
P3 -log(Delta)/sqrt(beta) at beta=4096 within 15% of c* and nearer c* than 2c*; relative error to c* non-increasing over 64..4096.
   (15% is MY expectation: finite-beta corrections ~ log(beta)/sqrt(beta)=0.13 at 4096; not derived.)
P4 (log g0 - log g(pi/2))/sqrt(beta) at 4096 within 15% of c*/2; error non-increasing over the 4 betas (same origin).
P5 identity -log m = -log Delta + log lam_e + O(Delta): |(-log m/sqrt b) - (-log Delta/sqrt b) - log(lam_e)/sqrt b| < 1e-9.
Results file results.json opened mode 'x'. No randomness (deterministic).
"""
import numpy as np, json, sys
cstar=None
def cstar_val():
    # substitute a=t^2 and pi-a=t^2 symmetric: int_0^pi = 2 int_0^{pi/2}; a=t^2, da=2t dt; Gauss-Legendre
    xs,ws=np.polynomial.legendre.leggauss(400)
    T=np.sqrt(np.pi/2); t=(xs+1)/2*T; w=ws*T/2
    a=t*t
    return 2*np.sum(w*2*t*np.sqrt(4*np.arcsinh(np.sin(a))))
def eps(a): return 2*np.arcsinh(np.abs(np.sin(a)))
def build(beta,n,J=2):
    h=np.pi/(2*n); i=np.arange(n)
    x=(i+.5)*h; s=(n-i-.5)*h
    c=np.sqrt(beta/(2*np.pi)); 
    g=lambda z:c*np.exp(-beta*z*z/2)
    X=x[:,None]; Y=x[None,:]; SX=s[:,None]; SY=s[None,:]
    V=0;Wc=0;Dm=0
    for j in range(-J,J+1):
        sh=2*np.pi*j
        V=V+g(X-Y+sh)+g(X+Y+sh)
        Wc=Wc+g(X+Y-np.pi+sh)+g(X-Y-np.pi+sh)
        # V-W accurately
        u=X-Y+sh; v=-(SX+SY)+sh
        delta=4*SY*(SX-2*np.pi*j)+0*u   # v^2-u^2
        Dm=Dm+diff(u,v,delta,beta,c)
        p=X+Y+sh; w=-np.pi+SY-SX+sh
        delta2=(2*SY-2*np.pi)*(4*np.pi*j-2*SX)
        Dm=Dm+diff(p,w,delta2,beta,c)
    D=np.exp(-eps(x)/2)
    M=lambda A:(D[:,None]*A*D[None,:])*h
    Ae=M(V+Wc); Ao=M(Dm); W=M(Wc)
    sym=lambda A:(A+A.T)/2
    return sym(Ae),sym(Ao),sym(W),x
def diff(a1,a2,delta,beta,c):
    # g(a1)-g(a2), delta=a2^2-a1^2 given accurately
    pos=delta>=0
    out=np.where(pos, c*np.exp(-beta*a1**2/2)*(-np.expm1(-beta*delta/2)),
                      -c*np.exp(-beta*a2**2/2)*(-np.expm1(beta*delta/2)))
    return out
def top(A,k=60):
    B=A/A.max()
    for _ in range(k):
        B=B@B; B/=B.max()
    col=np.argmax(B.diagonal()); v=B[:,col].copy(); v/=np.linalg.norm(v)
    lam=v@A@v
    return v,lam
def run(beta,n):
    Ae,Ao,W,x=build(beta,n)
    ge,le=top(Ae); go,lo=top(Ao)
    Delta=2*(go@W@ge)/(go@ge)
    m=-np.log1p(-Delta/le)
    return dict(beta=beta,n=n,hsb=np.pi/(2*n)*np.sqrt(beta),lam_e=le,lam_o_rayleigh=lo,Delta=Delta,
      A=-np.log(Delta)/np.sqrt(beta),B=-np.log(m)/np.sqrt(beta),
      C=(np.log(ge[0])-np.log(ge[-1]))/np.sqrt(beta),Cx=(np.log(ge[0])-np.log(ge[-1])),
      ge_pos=bool(ge.min()>0),go_pos=bool(go.min()>0),Ae_min=float(Ae.min()),Ao_min=float(Ao.min()))
if __name__=="__main__":
    cs=cstar_val(); res=dict(cstar=cs,direct=[],runs=[])
    for beta in (16,36):
        n=int(np.ceil(np.pi/2*8*np.sqrt(beta)))
        Ae,Ao,W,x=build(beta,n)
        we=np.linalg.eigvalsh(Ae)[-1]; wo=np.linalg.eigvalsh(Ao)[-1]
        r=run(beta,n); d=we-wo
        tol=max(1e-6,1e3*2.2e-16*we/r['Delta'])
        res['direct'].append(dict(beta=beta,n=n,Delta_direct=d,Delta_identity=r['Delta'],reldiff=abs(d-r['Delta'])/r['Delta'],tol=tol,
                                   A_direct=-np.log(d)/np.sqrt(beta),A_identity=r['A']))
    for beta in (64,256,1024,4096):
        n=int(np.ceil(np.pi/2*8*np.sqrt(beta)))
        r1=run(beta,n); r2=run(beta,int(1.5*n)); r1['alt']=dict(n=r2['n'],A=r2['A'],B=r2['B'],C=r2['C'],Delta=r2['Delta'])
        res['runs'].append(r1); print(beta,r1['A'],r1['B'],r1['C'],r2['A'],flush=True)
    json.dump(res,open('results.json','x'),indent=1,default=float)
    # predicates
    cs=res['cstar']; R=res['runs']; out=[]
    for d in res['direct']: out.append(('P1 beta=%d'%d['beta'],d['reldiff']<d['tol'],d['reldiff'],d['tol']))
    out.append(('P2',all(abs(r['A']-r['alt']['A'])<1e-3 for r in R),[abs(r['A']-r['alt']['A']) for r in R],1e-3))
    eA=[abs(r['A']-cs)/cs for r in R]; eC=[abs(r['C']-cs/2)/(cs/2) for r in R]
    mono=lambda e:all(e[i+1]<=e[i] for i in range(len(e)-1))
    out.append(('P3',eA[-1]<.15 and abs(R[-1]['A']-cs)<abs(R[-1]['A']-2*cs) and mono(eA),eA,.15))
    out.append(('P4',eC[-1]<.15 and mono(eC),eC,.15))
    out.append(('P5',all(abs(r['B']-r['A']-np.log(r['lam_e'])/np.sqrt(r['beta']))<1e-9 for r in R),[r['B']-r['A']-np.log(r['lam_e'])/np.sqrt(r['beta']) for r in R],1e-9))
    for o in out: print(o)
    print('cstar',cs)
