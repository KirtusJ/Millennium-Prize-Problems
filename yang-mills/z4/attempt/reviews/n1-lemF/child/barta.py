"""T138 Barta ratio quadrature. No scipy available: own i0e/i1e (power series x<=30, asymptotic series x>30).
PREDICATES (fixed before first run):
 P0 own i0e,i1e agree with periodic-trapezoid integral representation to rel 1e-11 at x in {0.5,5,30,31,200,4096}.
    (tolerance: series truncation ~1e-16 + roundoff; 1e-11 is generous.)
 P1 quadrature convergence: doubling all grids (chi nodes, rho grid) changes -log Bsup by < 1e-6 (given in task).
 P2 MEASURED ONLY: sign of (-log Bsup - 2 asinh s).
 P3 Z(beta) by trapezoid quadrature == 2 I1(beta)/beta to rel 1e-10 (given in task).
 P4 sanity expectation (own): B(rho)>0 finite, Bsup>=B(0). 
Method: B(rho)=e^{b(a/2-s^2)rho^2}*(2/Z)*int_0^1 r I0(b sqrt(1-rho^2)sqrt(1-r^2)) I0(b rho r) e^{-b c r^2} dr, r=sin chi,
composite Gauss-Legendre (16 nodes/panel) in chi. Deterministic (no randomness; seed n/a).
Usage: python3 barta.py out.csv   (out.csv opened mode 'x')
"""
import numpy as np, math, sys
def _series(x):
    y=x*x/4; s=np.ones_like(x)
    for k in range(90,0,-1): s=1+s*y/(k*k)
    return np.exp(-x)*s
def _series1(x):
    y=x*x/4; s=np.ones_like(x)
    for k in range(90,0,-1): s=1+s*y/(k*(k+1))
    return np.exp(-x)*s*(x/2)
def _asym(x,nu):
    m=4.0*nu*nu; term=np.ones_like(x); s=np.ones_like(x)
    for k in range(1,40):
        term=term*(-(m-(2*k-1)**2))/(k*8.0*x)
        s=s+term
    return s/np.sqrt(2*np.pi*x)
def _chunk(f,x):
    return np.concatenate([f(x[i:i+4000]) for i in range(0,len(x),4000)])
def i0e(x):
    x=np.asarray(x,float); out=np.empty_like(x); m=x<=30
    out[m]=_chunk(_series,x[m]) if m.any() else 0
    if (~m).any(): out[~m]=_asym(x[~m],0)
    return out
def i1e(x):
    x=np.asarray(x,float); out=np.empty_like(x); m=x<=30
    out[m]=_chunk(_series1,x[m]) if m.any() else 0
    if (~m).any(): out[~m]=_asym(x[~m],1)
    return out
def trap(x,nu,N=1<<15):
    t=2*np.pi*np.arange(N)/N
    return np.mean(np.exp(x*(np.cos(t)-1))*np.cos(nu*t))
def Zq(beta,N=1<<15):  # Z=(2/pi)int_0^pi e^{b cos}sin^2, scaled by e^{-b}; returns log Z
    t=2*np.pi*np.arange(N)/N
    return beta*0+np.log(np.mean(np.exp(beta*(np.cos(t)-1))*np.sin(t)**2)*2)+beta  # (2/pi)*(1/2)*2pi*mean = 2*mean
def logB(beta,s,rho,M):
    al=2*s*math.sqrt(1+s*s); c=s*s+al/2
    xg,wg=np.polynomial.legendre.leggauss(16)
    e=np.linspace(0,math.pi/2,M+1); h=e[1]-e[0]
    chi=((e[:-1,None]+e[1:,None])/2+h/2*xg[None,:]).ravel(); w=(h/2*wg[None,:]).ravel().repeat(1) if False else np.tile(h/2*wg,M)
    r=np.sin(chi); jac=np.sin(chi)*np.cos(chi)   # r dr
    rho=np.atleast_1d(rho)[:,None]
    a=beta*np.sqrt(1-rho**2)*np.cos(chi)[None,:]; b=beta*rho*r[None,:]
    L=a+b-beta*c*r[None,:]**2+np.log(i0e(a.ravel()).reshape(a.shape))+np.log(i0e(b.ravel()).reshape(b.shape))
    mx=L.max(axis=1,keepdims=True)
    I=np.sum(np.exp(L-mx)*(w*jac)[None,:],axis=1)
    return (beta*(al/2-s*s)*rho[:,0]**2+math.log(beta)-np.log(i1e(np.array([beta]))[0])-beta+mx[:,0]+np.log(I))
def sup(beta,s,M,nr):
    g=np.linspace(0,1,nr+1); lb=logB(beta,s,g,M); k=int(lb.argmax())
    lo,hi=g[max(k-1,0)],g[min(k+1,nr)]
    for _ in range(7):
        gg=np.linspace(lo,hi,201); l2=logB(beta,s,gg,M); j=int(l2.argmax())
        lo,hi=gg[max(j-1,0)],gg[min(j+1,200)]
    return gg[j],l2[j],lb[0]
if __name__=="__main__":
    out=sys.argv[1]; f=open(out,"x"); log=lambda m:(print(m),open("notes.md","a").write("- "+m+"\n"))
    ok0=True
    for x in [0.5,5,30,31,200,4096]:
        for nu,fn in [(0,i0e),(1,i1e)]:
            r=fn(np.array([x]))[0]; t=trap(x,nu); e=abs(r-t)/t
            if e>1e-11: ok0=False; log(f"P0 FAIL x={x} nu={nu} rel={e:.2e}")
    log(f"P0 own Bessel vs trapezoid: {'PASS' if ok0 else 'FAIL'}")
    ok3=True
    for beta in [64,256,1024,4096]:
        lz=Zq(beta); lz2=math.log(2)-math.log(beta)+math.log(i1e(np.array([float(beta)]))[0])+beta
        e=abs(math.expm1(lz-lz2)); 
        if e>1e-10: ok3=False
        log(f"P3 beta={beta} rel err Z={e:.2e}")
    log(f"P3 {'PASS' if ok3 else 'FAIL'}")
    f.write("beta,s,Bsup,neglogBsup,2asinh_s,diff,argmax_rho,B0,neglogBsup_fine,P1_change\n")
    npass=0;tot=0;pos=0
    for beta in [64,256,1024,4096]:
        for s in [0.01,0.03,0.1,0.3,0.6,1.0]:
            rho,lb,l0=sup(beta,s,64,400); rho2,lb2,_=sup(beta,s,128,800)
            d=abs(lb-lb2); tot+=1; npass+=d<1e-6
            nl=-lb2; t=2*math.asinh(s); pos+= (nl-t)>0
            f.write(f"{beta},{s},{math.exp(lb2):.10g},{nl:.10f},{t:.10f},{nl-t:.4e},{rho2:.6f},{math.exp(l0):.10g},{nl:.10f},{d:.2e}\n"); f.flush()
            log(f"beta={beta} s={s} Bsup={math.exp(lb2):.8g} -logB={nl:.8f} 2asinh={t:.8f} diff={nl-t:.3e} rho*={rho2:.5f} B0={math.exp(l0):.6g} P1chg={d:.1e}")
    log(f"P1: {npass}/{tot} cases change<1e-6; P2 measured: diff>0 in {pos}/{tot} cases")
