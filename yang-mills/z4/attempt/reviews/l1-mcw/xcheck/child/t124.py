"""T124: exact Gaussian SU(2) 2x2x2xT plaquette-energy correlators.
Model: per colour phi=sqrt(beta)*theta ~ N(0,P), P = orthogonal projector onto range(B).
 X=(1/2)sum_a phi^T M phi (M diagonal 0/1)  =>  <X>=(3/2)tr(MP), Cov(X,Y)=(3/2) sum_{p in M,q in N} P_pq^2.
P computed in time-Fourier blocks (48x32 per k), exact for each finite T; T->inf = large-T limit (checked by convergence).
PREDICATES (fixed before first run):
 P1 Fourier-block P equals dense SVD projector at T=16: max|diff|<1e-9 (SVD roundoff ~1e-12)
 P2 tr P (sum over k of ranks) == dense rank at T=16 ; P idempotent per block: |P^2-P|<1e-10
 P3 convergence: C_X(t)/C_X(0), t=0..6, T=256 vs T=512 agree to 1e-10 relative (exp. error e^{-gap T})
 P4 spectral fit C(t)=sum_n w_n exp(-E_n t), E_n=4 asinh(sqrt(m)/... ) i.e. 2*omega, sinh^2(omega/2)=m/4+? with m=1,2,3 (phat^2=4m), t=1..8 LS:
    max relative residual <1e-6 (noise in P(tau)^2 ~1e-16/P^2 grows with t; tolerance chosen from this)
 P5 E1 from fit == 4 asinh(1)=3.52549435.. to 1e-8
 P6 dense and Fourier C_X(t) agree at T=16, t=0..6 rel 1e-9
 P7 mean over spatial plaquettes all equal across 12,13,23 (symmetry) to 1e-12
"""
import numpy as np, itertools, json, sys
np.set_printoptions(precision=12)
pl=[(m,n) for m in range(4) for n in range(m+1,4)]   # 6 plaquette orientations
sites=list(itertools.product(range(2),repeat=3)); sidx={s:i for i,s in enumerate(sites)}
def spat_shift(s,mu):  # mu in 1..3
    s=list(s); s[mu-1]^=1; return tuple(s)
def Bk(k):
    B=np.zeros((48,32),complex)
    ph=np.exp(1j*k)
    for s in sites:
        i=sidx[s]
        for pi_,(m,n) in enumerate(pl):
            r=i*6+pi_
            def add(mu,shift,sg):
                # link (mu) at x+e_shift (shift in {None,m,n}) 
                ss=s; f=1.0
                if shift is not None:
                    if shift==0: f=ph
                    else: ss=spat_shift(s,shift)
                B[r,sidx[ss]*4+mu]+=sg*f
            add(m,None,1); add(n,m,1); add(m,n,-1); add(n,None,-1)
    return B
def Pblock(k,tol=1e-9):
    B=Bk(k); U,sv,_=np.linalg.svd(B); r=int((sv>tol).sum()); U=U[:,:r]
    return U@U.conj().T, r
def Ptau(T,tmax):
    ks=2*np.pi*np.arange(T)/T
    Ps=[];tot=0
    for k in ks:
        P,r=Pblock(k); tot+=r; Ps.append(P)
        assert np.abs(P@P-P).max()<1e-10
    Ps=np.array(Ps)
    out=[]
    for t in range(tmax+1):
        ph=np.exp(1j*ks*t)[:,None,None]
        out.append(((ph*Ps).sum(0)/T).real)
    return out,tot
sel=np.array([[ (s*6+pl.index(p)) for s in range(8)] for p in [(1,2),(1,3),(2,3)]])
def corr(Pt,mean_only=False):
    Cs=[]
    for t,P in enumerate(Pt):
        C=np.zeros((3,3))
        for a in range(3):
            for b in range(3):
                C[a,b]=1.5*(P[np.ix_(sel[a],sel[b])]**2).sum()
        Cs.append(C)
    return np.array(Cs)
e=np.array([0,-1,1])/np.sqrt(2); one=np.ones(3)
def ops(Cs):
    return {'S':Cs[:,0,0],'A1':np.einsum('a,tab,b->t',one,Cs,one),'E':np.einsum('a,tab,b->t',e,Cs,e)}
def dense(T,tmax):
    nl=4*8*T; npl=6*8*T
    Lid=lambda t,s,mu:((t%T)*8+sidx[s])*4+mu
    B=np.zeros((npl,nl))
    for t in range(T):
      for s in sites:
        for pi_,(m,n) in enumerate(pl):
            r=((t*8+sidx[s])*6+pi_)
            def sh(mu,shift):
                tt,ss=t,s
                if shift==0: tt=t+1
                elif shift is not None: ss=spat_shift(s,shift)
                return Lid(tt,ss,mu)
            B[r,sh(m,None)]+=1;B[r,sh(n,m)]+=1;B[r,sh(m,n)]-=1;B[r,sh(n,None)]-=1
    U,sv,_=np.linalg.svd(B,full_matrices=False); r=int((sv>1e-9).sum()); U=U[:,:r]
    return U@U.T,r
def main(tag):
    res={}
    # dense check T=16
    Pd,rd=dense(16,6)
    Pt,tot=Ptau(16,6)
    # dense P time-block (t,0)
    Pdt=[Pd[ (t*48):(t+1)*48, 0:48] for t in range(7)]
    res['P1_maxdiff']=max(np.abs(Pdt[t]-Pt[t]).max() for t in range(7))
    res['P2_rank_dense']=rd; res['P2_rank_fourier']=tot
    Cd=ops(corr(Pdt)); Cf=ops(corr(Pt))
    res['P6']=max(np.abs(Cd[x]-Cf[x]).max()/Cf[x][0] for x in Cd)
    out={}
    for T in (32,48,64,256,512):
        Pt,tot=Ptau(T,40 if T>=256 else 8)
        Cs=corr(Pt); o=ops(Cs)
        out[T]={x:o[x].tolist() for x in o}
        if T>=256:
            P0=Pt[0]; 
            # mean/variance of one plaquette: P_pp for orientation
            dia=np.diag(P0).reshape(8,6)
            out[T]['Ppp_by_orientation']=dia.mean(0).tolist()
            out[T]['Ppp_spread']=float(np.ptp(dia,axis=0).max())
            out[T]['Cs']=Cs[:12].tolist()
        out[T]['rank']=tot
    res['out']=out
    return res
if __name__=='__main__':
    tag=sys.argv[1]
    r=main(tag)
    with open(f'data_{tag}.json','x') as f: json.dump(r,f)
    print('done',tag)
