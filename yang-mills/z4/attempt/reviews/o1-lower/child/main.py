"""T144 main. Predicates fixed BEFORE first run:
P1 (Q1) literal flux sum over i in A, j not in A with extended f,g equals Delta*<f 1_A,g>; at beta=16 the
   flux Delta agrees with plain eigenvalue subtraction to rel 1e-4 (tolerance: eigensolver error ~1e-16*lambda/Delta ~1e-8 at beta=16;
   1e-4 is loose margin). For each beta the sector-form flux (2 f^T C g) equals the literal full-circle sum to rel 1e-10 (bookkeeping check).
P2 (Q2) lower: Delta >= 2*sum_{ordered (i,j), f_i f_j<0} T_ij|f_i||f_j|/||f||^2 (ordered; derived from Perron on |f|).
   upper as stated: Delta <= 2<g1_A,T g1_Ac>/||g||^2 -- hypothesis tested per beta, count reported. Variant factor 4 also reported.
P3 (Q3) -log(Delta)/sqrt(beta) monotone toward c*=4.605413 : |value-c*| decreasing in beta (my expectation, not a theorem).
P4 h-convergence: Delta at N and 2N agree to rel 1e-3 (O(h^2)-type quadrature error, h<=0.25/sqrt(beta)).
P5 sector eigenvector residual in weighted norm < 1e-10. Weighted eigvec positive in A (sign-structure assumption for Q2).
Results written to results_*.json (mode 'x')."""
import numpy as np, json, sys
def eps(a): return 2*np.arcsinh(np.abs(np.sin(a)))
def logT(xi,xj,beta,h,psi_i=None,psi_j=None):
    d=xi[:,None]-xj[None,:]
    s=0
    for k in (-1,0,1): s=s+np.exp(-beta*(d+2*np.pi*k)**2/2)  # unweighted
    return s
def Tmat(xi,xj,beta,h,pi_=None,pj_=None,sb=0.0):
    # entries with optional weight exp(sb*(Psi_i-Psi_j)), computed in log domain per k
    d=xi[:,None]-xj[None,:]; pre=np.log(h*np.sqrt(beta/(2*np.pi)))-(eps(xi)[:,None]+eps(xj)[None,:])/2
    if pi_ is not None: pre=pre+sb*(pi_[:,None]-pj_[None,:])
    return sum(np.exp(pre-beta*(d+2*np.pi*k)**2/2) for k in (-1,0,1))
def Psi(x,sb_unused=None):
    # Psi(x)=int_0^{|x|} sqrt(2eps), |x|<=pi/2, fine cumulative Simpson-free trapezoid on 400 sub-points/cell
    ax=np.abs(x); out=np.empty_like(ax)
    for n,a in enumerate(ax):
        t=np.linspace(0,np.sqrt(a),401) if a>0 else np.zeros(2)
        y=np.sqrt(4*np.arcsinh(np.abs(np.sin(t**2))))*2*t
        out[n]=np.trapezoid(y,t) if a>0 else 0
    return out
def run(beta,N):
    sb=np.sqrt(beta); h=2*np.pi/N; x=-np.pi+h*np.arange(N)
    iA=np.arange(N//4,3*N//4); xA=x[iA]; M=N//2
    PA=Psi(xA)
    S0=Tmat(xA,xA,beta,h,PA,PA,sb); C=Tmat(xA,xA+np.pi,beta,h,PA,PA,sb)
    res={}
    vec={}
    for name,Mx in (("e",S0+C),("o",S0-C)):
        w,V=np.linalg.eig(Mx); k=np.argmax(w.real); lam=w[k].real; v=V[:,k].real
        # inverse iteration polish
        for _ in range(3):
            v=np.linalg.solve(Mx-(lam*(1+1e-9))*np.eye(M),v); v/=np.abs(v).max()
        lam=(v@Mx@v)/(v@v)  # not symmetric; use left-free Rayleigh-ish; check residual
        lam=np.linalg.norm(Mx@v)/np.linalg.norm(v)
        r=np.linalg.norm(Mx@v-lam*v)/np.linalg.norm(v)
        if v.sum()<0: v=-v
        res["resid_"+name]=r; res["lam_"+name]=lam; res["minv_"+name]=float(v.min()/v.max())
        vec[name]=v
    sbPA=sb*PA
    f=vec["o"]*np.exp(-sbPA); g=vec["e"]*np.exp(-sbPA)
    f/=np.sqrt(2*(f@f)); g/=np.sqrt(2*(g@g))
    # extended full-circle vectors
    F=np.zeros(N); G=np.zeros(N)
    F[iA]=f; G[iA]=g; jA=(iA+N//2)%N; F[jA]=-f; G[jA]=g
    # literal flux with unweighted T rows i in A, cols j not in A
    outA=np.setdiff1d(np.arange(N),iA)
    TT=Tmat(x[iA],x[outA],beta,h)  # unweighted
    Fi,Gi,Fj,Gj=F[iA],G[iA],F[outA],G[outA]
    flux=np.sum(TT*(Fi[:,None]*Gj[None,:]-Fj[None,:]*Gi[:,None]))
    den=np.sum(Fi*Gi); Delta=flux/den
    flux_sec=2*f@(Tmat(xA,xA+np.pi,beta,h)@g); res["flux_rel_diff_sector_vs_literal"]=abs(flux_sec-flux)/flux
    # Q2 lower: ordered pairs f_i f_j<0 ; i in A interior, j=sigma j' ; plus symmetric ordering
    Cu=Tmat(xA,xA+np.pi,beta,h)
    low_unord=np.sum(Cu*np.outer(np.abs(f),np.abs(f))*(np.outer(f,-f)<0)) # (i in A, j'=sigma^-1 j in A): f_i * F_j = -f_j'
    nf=1.0
    lower=2*(2*low_unord)/nf   # ordered pairs = 2*unordered; factor 2 in bound
    X=np.sum(Cu*np.outer(g,g))
    upper2=2*X; upper4=4*X
    res.update(beta=beta,N=N,h=h,Delta=Delta,den=den,flux=flux,lower=lower,lower_unordered_only=2*low_unord,upper_stated=upper2,upper_factor4=upper4,
      r_lower=lower/Delta,r_upper_stated=upper2/Delta,r_upper4=upper4/Delta,m=None if Delta<=0 else None,
      neglogD_over_sb=-np.log(Delta)/sb, f_pos_in_A_interior=bool(np.all(f[1:-1]>0)))
    res["N_asym"]=None
    if beta<=36:
        Tf=Tmat(x,x,beta,h); w,V=np.linalg.eigh(Tf); ev=[];od=[]
        for k in range(N-1,-1,-1):
            v=V[:,k]; (ev if np.linalg.norm(v-np.roll(v,N//2))<1e-6 else od if np.linalg.norm(v+np.roll(v,N//2))<1e-6 else []).append((w[k],v))
        le,ge=ev[0]; lo,fo=od[0]
        res["plain_Delta"]=le-lo; res["plain_rel_diff"]=abs((le-lo)-Delta)/Delta
        # plain eigvec flux
        ge=ge if ge[N//2*0+N//2]*0==0 else ge
        s=np.sum(fo[iA]*ge[iA]); fo=fo*np.sign(s); 
        fl=np.sum(Tf[np.ix_(iA,outA)]*(fo[iA][:,None]*ge[outA][None,:]-fo[outA][None,:]*ge[iA][:,None]))
        res["plain_flux_Delta"]=fl/abs(s); res["plain_identity_rel_err"]=abs(fl/abs(s)-(le-lo))/(le-lo)
    return res
if __name__=="__main__":
    out={}
    for beta in (16,64,256,1024,4096):
        N=4*int(np.ceil(2*np.pi/(0.25/np.sqrt(beta))/4))
        r=run(beta,N); r2=run(beta,2*N) if (beta<=1024 or True) else None
        r["Delta_2N"]=r2["Delta"]; r["conv_rel"]=abs(r2["Delta"]-r["Delta"])/r["Delta"]
        out[str(beta)]=r; print(beta,{k:(float(v) if isinstance(v,(float,np.floating)) else v) for k,v in r.items()},flush=True)
        with open("notes.md","a") as fh: fh.write("- beta=%d N=%d Delta=%.6e -logD/sb=%.5f lower/D=%.4f up2/D=%.4f up4/D=%.4f conv=%.1e\n"%(beta,N,r["Delta"],r["neglogD_over_sb"],r["r_lower"],r["r_upper_stated"],r["r_upper4"],r["conv_rel"]))
    for beta in (36,):
        N=4*int(np.ceil(2*np.pi/(0.25/np.sqrt(beta))/4)); r=run(beta,N); out["36"]=r; print(36,r)
    with open("results_main.json","x") as fh: json.dump(out,fh,indent=1,default=float)
