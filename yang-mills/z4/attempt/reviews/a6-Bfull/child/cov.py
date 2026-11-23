"""AMENDMENT after run 1 (cov_result.json kept): at N=4 p2 sits at time 4=N (shell), all its links are fixed to 0, so F_p2=0,
 rhs b=0 and CG gave nan -> C2, C5, C4(n=2) failed through MY expectation (I overlooked p2 on the shell), not a defect of the target.
 Rerun: CG returns 0 for b=0 (C(p2,.)=0 exactly, a degenerate case); predicates otherwise unchanged. Output cov2_result.json.
Finite-N covariance of F on plaquettes p0,p1,p2, N=4,6,8.  Predicates fixed BEFORE first run:
 C1 gauge: ||D g||_inf < 1e-12 (exact integer arithmetic, so any nonzero is a bug).
 C2 CG vs dense solve (N=4,6): |C_cg - C_dense| < 1e-8 (CG rel. residual tol 1e-11 -> expected error ~1e-10).
 C3 (a) C^N(p0,p0) strictly increasing N=4<6<8 and < G(0)=0.5.   [expectation from the task; measured]
 C4 (b) |C^N(p0,pn)-G(n)| decreasing in N for n=0,1,2 (expectation; measured).  G(n) from gquad_result.json (err 3e-11).
 C5 PSD sanity: 3x3 matrix C^N(p_i,p_j) symmetric to 1e-9 and Cauchy-Schwarz C01^2<=C00*C11.
 C6 (c) at N=6 choose m0=1,m1=-C01*sign: Cov(F0^2,F1^2|b)=2C01^2+4 m0 m1 C01 < 0.
"""
import numpy as np, itertools, json, sys
out=sys.argv[1]; Gq=json.load(open('gquad_result.json'))['res']['512']
def build(N):
    sites=list(itertools.product(range(N+1),repeat=4))
    interior=lambda x: all(0<c<N for c in x)
    isite={x:i for i,x in enumerate([s for s in sites if interior(s)])}
    link={}
    for x in sites:
        for mu in range(4):
            if x[mu]<N:
                y=list(x);y[mu]+=1;y=tuple(y)
                if interior(x) or interior(y): link[(x,mu)]=len(link)
    sh=lambda x,mu:tuple(c+(i==mu) for i,c in enumerate(x))
    pl={};r=[];c=[];v=[]
    for x in sites:
        for mu in range(4):
            for nu in range(mu+1,4):
                if x[mu]<N and x[nu]<N:
                    row=len(pl);pl[(x,mu,nu)]=row
                    for l,s in (((x,mu),1),((sh(x,mu),nu),1),((sh(x,nu),mu),-1),((x,nu),-1)):
                        if l in link: r.append(row);c.append(link[l]);v.append(s)
    gr=[];gc=[];gv=[]
    for (x,mu),i in link.items():
        if x in isite: gr.append(i);gc.append(isite[x]);gv.append(-1)
        y=sh(x,mu)
        if y in isite: gr.append(i);gc.append(isite[y]);gv.append(1)
    return dict(np_=len(pl),nl=len(link),ns=len(isite),pl=pl,D=(np.array(r),np.array(c),np.array(v,float)),g=(np.array(gr),np.array(gc),np.array(gv,float)))
def mv(T,x,nout):  # y = T x, T=(rows,cols,vals)
    return np.bincount(T[0],weights=T[2]*x[T[1]],minlength=nout)
def tr(T): return (T[1],T[0],T[2])
def cg(A,b,tol=1e-11,maxit=5000):
    x=np.zeros_like(b)
    if not b.any(): return x,0
    r=b.copy();p=r.copy();rs=r@r;b2=np.sqrt(b@b)
    for it in range(maxit):
        Ap=A(p);a=rs/(p@Ap);x+=a*p;r-=a*Ap;rn=r@r
        if np.sqrt(rn)<tol*b2: return x,it+1
        p=r+rn/rs*p;rs=rn
    return x,-1
def run(N,dense):
    S=build(N);D,g=S['D'],S['g'];nl=S['nl']
    # C1: D g
    rng=np.random.default_rng(12345);lam=rng.standard_normal(S['ns'])
    Dg=abs(mv(D,mv(g,lam,nl),S['np_'])).max()
    Mv=lambda x: mv(tr(D),mv(D,x,S['np_']),nl)+mv(g,mv(tr(g),x,S['ns']),nl)
    c=(N//2,)*4
    rows=[S['pl'][((c[0]+n,)+c[1:],1,2)] for n in range(3)]
    C=np.zeros((3,3));Cd=None;its=[]
    for j,q in enumerate(rows):
        e=np.zeros(S['np_']);e[q]=1;b=mv(tr(D),e,nl)
        y,it=cg(Mv,b);its.append(it);C[:,j]=mv(D,y,S['np_'])[rows]
    if dense:
        M=np.zeros((nl,nl))
        for i in range(nl):
            e=np.zeros(nl);e[i]=1;M[:,i]=Mv(e)
        Dd=np.zeros((S['np_'],nl));np.add.at(Dd,(D[0],D[1]),D[2])
        Cd=Dd[rows]@np.linalg.solve(M,Dd[rows].T)
    return dict(N=N,nl=nl,np=S['np_'],Dg=Dg,C=C.tolist(),Cdense=None if Cd is None else Cd.tolist(),cg_iters=its)
R={N:run(N,N<=6) for N in (4,6,8)}
for N,r in R.items(): print(N,r['nl'],r['np'],'Dg',r['Dg'],'iters',r['cg_iters']);print(np.array(r['C']))
P={}
P['C1']=all(r['Dg']<1e-12 for r in R.values())
P['C2']=all(np.abs(np.array(R[N]['C'])-np.array(R[N]['Cdense'])).max()<1e-8 for N in (4,6))
c00=[R[N]['C'][0][0] for N in (4,6,8)]
P['C3']=bool(c00[0]<c00[1]<c00[2]<0.5)
P['C4']={n:[abs(R[N]['C'][0][n]-Gq[n]) for N in (4,6,8)] for n in range(3)}
P['C4_met']={n:bool(v[0]>v[1]>v[2]) for n,v in P['C4'].items()}
P['C5']=all(np.abs(np.array(R[N]['C'])-np.array(R[N]['C']).T).max()<1e-9 and R[N]['C'][0][1]**2<=R[N]['C'][0][0]*R[N]['C'][1][1] for N in R)
C6=np.array(R[6]['C']);c01=C6[0,1];m0=1.0;m1=-np.sign(c01)*abs(c01)
P['C6_value']=2*c01**2+4*m0*m1*c01;P['C6']=bool(P['C6_value']<0);P['C6_means']=[m0,m1]
for k,v in P.items(): print(k,v)
with open(out,'x') as f: json.dump(dict(R=R,P={k:(v if not isinstance(v,(np.bool_,)) else bool(v)) for k,v in P.items()},G=Gq),f,default=lambda o:bool(o) if isinstance(o,np.bool_) else float(o))
