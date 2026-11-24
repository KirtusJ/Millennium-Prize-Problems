"""Brute-force check of (e:trace), Lemma l:trace, on tiny abelian lattices (own program; Z_n in place of SU(2)).
Models: (A) Z_2 and (B) Z_3, 1+1 dimensions, two spatial sites on a circle (two spatial links, no spatial
plaquette, so W=1), T=3 and T=2; (C) Z_2, 2+1 dimensions, one open spatial plaquette (4 sites, 4 links, W non-trivial), T=3.
Weight: exp(beta * sum_p Re U_p), beta=0.7 (A,B,C) -- all plaquettes of the lattice, time-like links enumerated explicitly.
PREDICATES (fixed before the first run), tolerance 1e-10 relative (sums of <=1.7e7 positive doubles):
 T1 E_T[prod_s f_s(x_s)] by enumeration of ALL link configurations equals Tr(M_f0 L M_f1 L ... )/Tr(L^T), L = W C W Pi,
    for 5 random triples of non-gauge-invariant real f_s.
 T2 controls that must FAIL to match: L replaced by T_0=WCW (no Pi); for model C, W omitted.
 T3 C Pi = Pi C; L symmetric; kernel of L (matrix entries) > 0; C eigenvalues > 0; rank L = rank Pi (injective on invariant functions);
    L f = 0 when Pi f = 0.
 T4 two-slice vacuum limit (Prop p:vac): Tr(L^{T-j} M_f L^j M_g)/Tr(L^T) at T=60 agrees with <Omega, M_f (L/Lam0)^j M_g Omega> to 1e-8 (j=1,2).
Seed 7. No arguments. Output results_trace.txt (refuses to overwrite)."""
import numpy as np, itertools, os, sys
OUT='results_trace.txt'
if os.path.exists(OUT): sys.exit('refuse to overwrite')
rng=np.random.default_rng(7); log=[]; ok=True
def run(name,n,sites,links,plaqs,beta,Ts):
    global ok
    w=np.exp(2j*np.pi/n); nl=len(links); ns=len(sites)
    S=list(itertools.product(range(n),repeat=nl)); Gs=list(itertools.product(range(n),repeat=ns)); nS=len(S); nG=len(Gs)
    # spatial weight of a slice from its spatial plaquettes (list of lists of (link,sign))
    Wsq=np.array([np.exp(beta*sum((np.prod([w**(sg*U[e]) for e,sg in p])).real for p in plaqs)) for U in S])
    # slab weight straight from the time-like plaquettes: U_e(s) g_y conj(U_e(s+1)) conj(g_x), e=(x,y)
    K=np.zeros((nS,nS,nG))
    for a,U in enumerate(S):
        for b,V in enumerate(S):
            for c,g in enumerate(Gs):
                K[a,b,c]=np.exp(beta*sum((w**(U[e]+g[y]-V[e]-g[x])).real for e,(x,y) in enumerate(links)))
    # operator side
    C=np.array([[np.exp(beta*sum((w**(U[e]-V[e])).real for e in range(nl))) for V in S] for U in S])
    idx={U:i for i,U in enumerate(S)}
    Pi=np.zeros((nS,nS))
    for a,V in enumerate(S):
        for g in Gs:
            Vg=tuple((g[x]+V[e]-g[y])%n for e,(x,y) in enumerate(links)); Pi[a,idx[Vg]]+=1/nG
    W=np.diag(np.sqrt(Wsq)); T0=W@C@W; L=T0@Pi
    c3=[np.allclose(C@Pi,Pi@C,atol=1e-12),np.allclose(L,L.T,atol=1e-12),np.allclose(L,Pi@T0,atol=1e-12),bool(L.min()>0),
        bool(np.linalg.eigvalsh(C)[0]>1e-12),np.linalg.matrix_rank(L,tol=1e-10)==np.linalg.matrix_rank(Pi,tol=1e-10),
        np.allclose(L@(np.eye(nS)-Pi),0,atol=1e-12)]
    log.append(f'{name}: slices {nS}, gauge transformations {nG}, rank Pi {np.linalg.matrix_rank(Pi,tol=1e-10)}, min eig C {np.linalg.eigvalsh(C)[0]:.4e}, min kernel L {L.min():.4e}; T3 [CPi=PiC, L sym, T0Pi=PiT0, L>0 entrywise, C>0, rank L=rank Pi, L(1-Pi)=0] = {c3}')
    ok&=all(c3)
    for T in Ts:
        errs=[];ctl=[];ctlW=[]
        for trial in range(5):
            f=[rng.normal(size=nS)+2.0 for _ in range(T)]
            # full enumeration over all slices and all time-like links
            if T==3:
                num=np.einsum('a,b,c,abx,bcy,caz,a,b,c->',Wsq,Wsq,Wsq,K,K,K,f[0],f[1],f[2],optimize=False) if nS**3*nG**3<=6e5 else None
                if num is None:
                    num=0.0;den=0.0
                    for a in range(nS):
                        blk=np.einsum('b,c,bx,bcy,cz->bcxyz',Wsq,Wsq,K[a],K,K[:,a],optimize=False)  # all (U1,U2,g0,g1,g2)
                        num+=Wsq[a]*f[0][a]*np.einsum('bcxyz,b,c->',blk,f[1],f[2]); den+=Wsq[a]*blk.sum()
                else:
                    den=np.einsum('a,b,c,abx,bcy,caz->',Wsq,Wsq,Wsq,K,K,K,optimize=False)
            else:
                num=np.einsum('a,b,abx,bay,a,b->',Wsq,Wsq,K,K,f[0],f[1]); den=np.einsum('a,b,abx,bay->',Wsq,Wsq,K,K)
            brute=num/den
            def tr(Lm):
                X=np.eye(nS)
                for s in range(T): X=X@np.diag(f[s])@Lm
                return np.trace(X)/np.trace(np.linalg.matrix_power(Lm,T))
            errs.append(abs(tr(L)/brute-1)); ctl.append(abs(tr(T0)/brute-1)); ctlW.append(abs(tr(C@Pi)/brute-1))
        t1=max(errs)<1e-10; t2=min(ctl)>1e-6 and (len(plaqs)==0 or min(ctlW)>1e-6)
        log.append(f'{name} T={T}: T1 max rel err {max(errs):.2e} {"PASS" if t1 else "FAIL"}; T2 control without Pi min rel err {min(ctl):.2e}, control without W min rel err {min(ctlW):.2e} ({"n/a W=1" if len(plaqs)==0 else ""}) {"PASS" if t2 else "FAIL"}')
        ok&=t1 and t2
    ev,evec=np.linalg.eigh(L); Om=evec[:,-1]*np.sign(evec[0,-1]); L0=ev[-1]
    f=rng.normal(size=nS); g=rng.normal(size=nS); e4=[]
    for j in (1,2):
        T=60; Ln=L/L0
        lhs=np.trace(np.linalg.matrix_power(Ln,T-j)@np.diag(f)@np.linalg.matrix_power(Ln,j)@np.diag(g))/np.trace(np.linalg.matrix_power(Ln,T))
        rhs=Om@(f*(np.linalg.matrix_power(Ln,j)@(g*Om))); e4.append(abs(lhs-rhs))
    t4=max(e4)<1e-8 and Om.min()>0 and np.allclose(Pi@Om,Om)
    log.append(f'{name}: T4 vacuum limit |diff| {max(e4):.2e}, Omega>0 {bool(Om.min()>0)}, Pi Omega=Omega {np.allclose(Pi@Om,Om)}, Lam1/Lam0 {ev[-2]/ev[-1]:.4f} {"PASS" if t4 else "FAIL"}')
    ok&=t4
ring=dict(sites=[0,1],links=[(0,1),(1,0)],plaqs=[])
run('A Z2 1+1 ring',2,beta=0.7,Ts=[3,2],**ring)
run('B Z3 1+1 ring',3,beta=0.7,Ts=[3,2],**ring)
run('C Z2 2+1 open plaquette',2,sites=[0,1,2,3],links=[(0,1),(1,2),(3,2),(0,3)],plaqs=[[(0,1),(1,1),(2,-1),(3,-1)]],beta=0.7,Ts=[3])
log.append('ALL '+('PASS' if ok else 'FAIL'))
open(OUT,'x').write('\n'.join(log)+'\n'); print('\n'.join(log))
