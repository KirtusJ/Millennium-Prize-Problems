"""eps_eff for the SU(2) fibre operator F_a via the Legendre-reduced matrix M.
Predicates fixed BEFORE first run (tolerances: 1e-12 ~ 1000x double eps for exact identities;
1e-9 for convergence = far below the 1e-4 level of the quantity eps_eff-eps; MC 4 sigma):
 H1 V_a = beta sin^2 a (1-t) with t=x0^2+x3^2-x1^2-x2^2, on 1000 random S^3 points, max err <1e-12.
 H2 t uniform on [-1,1] under Haar: MC mean t^2 within 4 sigma of 1/3, N=400000, seed 1 (measured, MC only).
 H3 Pt_j orthonormal wrt dt/2 : max |Gram - I| < 1e-12 (j<=60).
 H4 l_j = I_{2j+1}/I_1 by backward recurrence agrees with direct series sum for beta=64, j<=5, rel err<1e-12.
 H5 M symmetric (1e-14 rel) and eigenvalues in (0,1].
 C1 truncation: |eps(J) - eps(1.5J)|<1e-9 for all 21 cases.
 C2 quadrature: |eps(N) - eps(2N)|<1e-9 for all 21 cases.
 C3 'for all' hypothesis: (eps_eff-eps)>0 for all cases -> count qualifying (measured).
 M  differences and scaled differences are MEASURED only.
Positivity of kernel / invariance of top eigenfunction: taken from Perron-Frobenius argument, NOT numerically tested here.
Output file opened mode 'x'."""
import numpy as np, math, sys
def lratio(beta, jmax):
    n0=6000; r=0.0; rs=np.zeros(n0+2)
    for n in range(n0,0,-1):
        r=1.0/(2*(n+1)/beta+r) ; rs[n]=r   # r_n=I_{n+1}/I_n
    l=np.ones(jmax+1)
    for j in range(1,jmax+1): l[j]=l[j-1]*rs[2*j-1]*rs[2*j]
    return l
def leg(J,x):
    P=np.zeros((J+1,len(x))); P[0]=1
    if J>=1: P[1]=x
    for n in range(1,J): P[n+1]=((2*n+1)*x*P[n]-n*P[n-1])/(n+1)
    return P*np.sqrt(2*np.arange(J+1)+1)[:,None]
def eps_eff(a,beta,J,N):
    x,w=np.polynomial.legendre.leggauss(N); w=w/2
    Pt=leg(J,x); l=lratio(beta,J)
    ev=np.exp(-beta*math.sin(a)**2*(1-x))
    M=(Pt*(w*ev))@Pt.T; s=np.sqrt(l); M=s[:,None]*M*s[None,:]
    asym=np.abs(M-M.T).max()/np.abs(M).max()
    e=np.linalg.eigvalsh((M+M.T)/2)
    return -math.log(e[-1]), asym, e[0]
if __name__=="__main__":
    out=open("results_eps_eff_run2.txt","x"); fails=[]
    def P(*a):
        s=" ".join(str(x) for x in a); print(s); out.write(s+"\n"); out.flush()
    rng=np.random.default_rng(1)
    # H1,H2
    X=rng.normal(size=(400000,4)); X/=np.linalg.norm(X,axis=1)[:,None]
    t=X[:,0]**2+X[:,3]**2-X[:,1]**2-X[:,2]**2
    h1=max(abs(2*b*math.sin(a)**2*(X[i,1]**2+X[i,2]**2)-b*math.sin(a)**2*(1-t[i])) for i in range(1000) for a,b in [(0.7,64.0)])
    P("H1 max err",h1,"PASS" if h1<1e-12 else "FAIL")
    m=(t**2).mean(); sig=(t**2).std()/math.sqrt(len(t)); P("H2 mean t^2",m,"vs 1/3, sigma",sig,"PASS" if abs(m-1/3)<4*sig else "FAIL")
    x,w=np.polynomial.legendre.leggauss(200); Pt=leg(60,x); G=(Pt*(w/2))@Pt.T
    g=abs(G-np.eye(61)).max(); P("H3 gram err",g,"PASS" if g<1e-12 else "FAIL")
    # H4 direct series I_nu(beta)
    def I(nu,b):
        t0=math.exp(nu*math.log(b/2)-math.lgamma(nu+1)); tot=0.0
        for k in range(400):
            tot+=t0; t0*=(b/2)**2/((k+1)*(k+1+nu))
        return tot
    l=lratio(64.0,5); e4=max(abs(l[j]-I(2*j+1,64.0)/I(1,64.0))/l[j] for j in range(6))
    P("H4 l_j rel err",e4,"PASS" if e4<1e-12 else "FAIL")
    betas=[64,256,1024]; As=[0.1,0.3,0.6,1.0,math.pi/2,2.2,3.0]
    P("beta a eps eps_eff diff diff*sqrt(beta) diff*beta  J N trunc_chg quad_chg asym minev")
    res={}; cc1=cc2=cpos=h5=0
    for b in betas:
        J=int(10*math.sqrt(b))+40; N=3*J+400
        for a in As:
            e1,asym,mn=eps_eff(a,b,J,N)
            e2,_,_=eps_eff(a,b,int(1.5*J),N)
            e3,_,_=eps_eff(a,b,J,2*N)
            eps=2*math.asinh(math.sin(a)); d=e1-eps
            c1=abs(e1-e2)<1e-9; c2=abs(e1-e3)<1e-9; cc1+=c1; cc2+=c2; cpos+=d>0; h5+=(asym<1e-14 and mn>0)
            if not c1: fails.append(("C1",a,b,abs(e1-e2)))
            if not c2: fails.append(("C2",a,b,abs(e1-e3)))
            res[(b,a)]=d
            P(b,"%.4f"%a,"%.8f"%eps,"%.10f"%e1,"%.6e"%d,"%.6f"%(d*math.sqrt(b)),"%.6f"%(d*b),J,N,"%.1e"%abs(e1-e2),"%.1e"%abs(e1-e3),"%.1e"%asym,"%.2e"%mn)
    P("H5 cases ok",h5,"/21"); P("C1 qualify",cc1,"/21"); P("C2 qualify",cc2,"/21"); P("C3 diff>0 qualify",cpos,"/21")
    for f in fails: P("FAILED",f)
    P("ratio d(64)/d(1024) per a (sqrt-scaling expects 4, beta-scaling expects 16):",[round(res[(64,a)]/res[(1024,a)],3) for a in As])
    P("ratio d(256)/d(1024) (sqrt:2, beta:4):",[round(res[(256,a)]/res[(1024,a)],3) for a in As])
