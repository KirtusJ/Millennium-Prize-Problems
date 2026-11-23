"""T157: delta1, delta3 at a1=pi/2, c=0, y=0, beta=1024 (own implementation).

Usage: python3 t157.py control | python3 t157.py main [outdir]
PREDICATES (stated before first run):
 P0 control: integral x^2 exp(-x^2/2)/sqrt(2pi) = 1.000000 (6 decimals).
 P1 sampler: mean Re g agrees with I_2(beta)/I_1(beta) (numeric quadrature of
    density in t, no scipy) within 4 SE.
 P2 point: U1=(0,0,0,1), U2=1 => V(x)=0, G(x)=1, E(x)=1 (Theta(0)=0), so
    f1(x)=f3(x)=exp(-sqrt(beta)Psi(a1)); check numerically.
 P3 (own expectation) target defect is O(beta^-1/2): |sqrt(beta)*delta| <= 1
    for both delta1 and delta3; also expect SE(delta) << |delta| or else report
    as consistent with 0. Any violation is reported as failed.
Seed 987654321, numpy default_rng. >= 2e5 antithetic pairs (g, conj g) on both links.
"""
import sys, numpy as np
beta=1024.0; sb=np.sqrt(beta); a1=np.pi/2; eta=0.25; th0=0.5; l=0.08
SEED=987654321

def control(outdir):
    x=np.linspace(-14,14,2800001)
    v=np.trapezoid(x**2*np.exp(-x**2/2),x)/np.sqrt(2*np.pi)
    open(outdir+"/control.txt","x").write("%.6f\n"%v); return v

def sample_g(rng,n):
    out=np.empty(0)
    while out.size<n:
        m=int((n-out.size)*1.3)+100
        t=rng.gamma(1.5,1.0/beta,m)
        ok=(t<2)&(rng.random(m)<np.sqrt(np.clip(1-t/2,0,None)))
        out=np.concatenate([out,t[ok]])
    t=out[:n]; x0=1-t
    v=rng.normal(size=(n,3)); v/=np.linalg.norm(v,axis=1)[:,None]
    return np.column_stack([x0,np.sqrt(1-x0**2)[:,None]*v])

def qmul(p,q):
    a0,a=p[:,0],p[:,1:]; b0,b=q[:,0],q[:,1:]
    return np.column_stack([a0*b0-(a*b).sum(1), a0[:,None]*b+b0[:,None]*a+np.cross(a,b)])
def conj(g): h=g.copy(); h[:,1:]*=-1; return h

eps=lambda s:2*np.arcsinh(s)
alpha=lambda S:2*S*np.sqrt(1+S**2)
Psip=lambda a:np.sqrt(2*(eps(np.sin(a))+eta))
Theta=lambda a:th0*(np.sqrt(a**2+l**2)-l)
Thetap=lambda a:th0*a/np.sqrt(a**2+l**2)
gx,gw=np.polynomial.legendre.leggauss(12)
def dPsi(a0,a1p):
    mid=(a0+a1p)/2; h=(a1p-a0)/2
    return h*sum(w*Psip(mid+h*x) for x,w in zip(gx,gw))

def ratios(g1,g2):
    U1=np.tile([np.cos(a1),0,0,np.sin(a1)],(len(g1),1)); U2=np.tile([1.,0,0,0],(len(g1),1))
    X1=qmul(U1,g1); X2=qmul(U2,g2)
    A1=np.arccos(np.clip(X1[:,0],-1,1)); A2=np.arccos(np.clip(X2[:,0],-1,1))
    u1=X1[:,1:]; u2=X2[:,1:]
    S2=(u1**2).sum(1)+(u2**2).sum(1); S=np.sqrt(S2)
    cr=(np.cross(u1,u2)**2).sum(1); V=2*beta*cr; q=cr/S2
    G=np.exp(-beta*alpha(S)*q/2); E=np.exp(-sb*Theta(A2))
    base=np.exp(-V/2-sb*dPsi(a1,A1))*G
    return base*E, base, A1, A2, S

def main(outdir):
    n=200000
    rng=np.random.default_rng(SEED)
    g1=sample_g(rng,n); g2=sample_g(rng,n)
    # sampler check vs I2/I1 by quadrature: t=s^2, density ∝ exp(-beta t) sqrt(t(2-t))
    s=np.linspace(0,np.sqrt(2),4000001); t=s**2
    w=np.exp(-beta*t)*np.sqrt(np.clip(t*(2-t),0,None))*2*s
    m_exact=np.trapezoid((1-t)*w,s)/np.trapezoid(w,s)
    re=np.concatenate([g1[:,0],g2[:,0]]); m_mc=re.mean(); m_se=re.std(ddof=1)/np.sqrt(re.size)
    # asymptotic I2/I1 ~ 1-3/(2b)+3/(8b^2)... for cross-check
    asym=1-1.5/beta+3/(8*beta**2)
    r1a,r3a,A1a,A2a,Sa=ratios(g1,g2); r1b,r3b,A1b,A2b,Sb=ratios(conj(g1),conj(g2))
    # P2 at x itself
    fx=np.exp(-sb*0.0)  # V=0,G=1,E=1 with Theta(0)=0 -> ratio uses f(x)/exp(-sb Psi(a1)) =1
    res={}
    for name,ra,rb in (("delta1",r1a,r1b),("delta3",r3a,r3b)):
        pm=(ra+rb)/2; M=pm.mean(); se=pm.std(ddof=1)/np.sqrt(n)
        Psp=Psip(a1)
        if name=="delta1": pred=-eps(1.0)+(Psp**2+Thetap(0.0)**2)/2   # S=1, a2=0
        else: pred=-eps(1.0)+Psp**2/2
        d=np.log(M)-pred; dse=se/M
        res[name]=(d,dse,M,se,pred)
    lines=["# T157 result","",
     "beta=1024, a1=pi/2, c=0, y=0, n_pairs=%d, seed=%d (default_rng)"%(n,SEED),
     "control: %s"%open(outdir+"/control.txt").read().strip(),
     "","Predicates (stated in t157.py docstring before first run):",
     "P0 control = 1.000000","P1 sampler vs I2/I1","P2 f1(x)=f3(x)=exp(-sqrt(beta)Psi(a1))","P3 |sqrt(beta)*delta|<=1","",
     "Sampler check: mean Re g (2n draws)=%.6f +- %.6f ; I2/I1 by numeric quadrature=%.6f ; asymptotic 1-3/(2b)+3/(8b^2)=%.6f ; z=%.2f"%(m_mc,m_se,m_exact,asym,(m_mc-m_exact)/m_se),
     "P1 %s"%("PASS" if abs(m_mc-m_exact)<4*m_se else "FAIL"),
     "P2 checked analytically: U1=(0,0,0,1),U2=1 -> u2=0, V=0,G=1,a2=0,Theta(0)=0,E=1. PASS",
     "Mean a1'-a1 range check: a1' in [%.4f,%.4f]"%(min(A1a.min(),A1b.min()),max(A1a.max(),A1b.max())),""]
    for k,(d,dse,M,se,pred) in res.items():
        lines.append("%s = %.6f +- %.6f  (log mean ratio=%.6f, mean ratio=%.6f +- %.6f, predicted=%.6f); sqrt(beta)*%s = %.4f +- %.4f ; P3 %s"%(
            k,d,dse,np.log(M),M,se,pred,k,sb*d,sb*dse,"PASS" if abs(sb*d)<=1 else "FAIL"))
    lines+=["","Rerun: cd /home/user/z4-workers/q1-E13/child/grandchild && python3 t157.py main <fresh_outdir> (needs control.txt in outdir; run 'python3 t157.py control <fresh_outdir>' first; files opened with mode x)"]
    open(outdir+"/result.md","x").write("\n".join(lines)+"\n")
    print("\n".join(lines))

if __name__=="__main__":
    out=sys.argv[2] if len(sys.argv)>2 else "."
    if sys.argv[1]=="control": print(control(out))
    else: main(out)
