"""zscore.py  (T232)  Test of the IBP / Stein identity claims for the two-link SU(2) pair measure.

rho(u,v) ~ exp(beta[Re(u h_u)+Re(v h_v)+Re(C u M v N)]),  Y=Re(C u M v N),  A_ab=Re(C u e_a M v e_b N)
Z = sum_ab [ D_aE_b A_ab + s_a E_bA_ab + t_b D_aA_ab + (E_b s_a) A_ab + s_a t_b A_ab ].
Sampling: exact conditional heat-bath Gibbs (u|v has staple h_u + M v N C ; v|u has staple h_v + N C u M),
 1000 independent chains from Haar starts, 400 burn-in sweeps, 100 recorded sweeps each -> 1e5 samples.
 SE = std of chain means / sqrt(chains) (accounts for autocorrelation).
Exteriors: h = sum of 5 random unit quaternions, C,M,N random unit; exterior e uses seed 100+e (same for every beta).
PREDICATES (fixed before first run):
 P1 pointwise identity sum A^2 == 2+Y^2, max abs err < 1e-9 (float roundoff).
 P2 |E Z| <= 4 SE   (4 sigma; MC noise)
 P3 |E[(Y-EY)Z] - E[2+Y^2]| <= 4 SE of the difference (per-sample paired difference, chain-mean SE)
 P4 ||Z||_L2 /beta <= 72 (claim iii; beta>=1, all cases)
 P5 Var(Y)*(...) ratio = Var(Y/4)*20736*beta^2 >= 1  (claim iv)
 P6 Cauchy-Schwarz  Var(Y) >= E[2+Y^2]^2 / E[Z^2]  (exact inequality, holds up to MC noise; tolerance 1%)
 P7 burn-in check: |mean Y first half of recorded - second half| <= 4 SE.
Results files are opened with mode "x" (never overwritten).
"""
import numpy as np, json, sys
E = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],float)
def qm(a,b):
    a0,a1,a2,a3=[a[...,i] for i in range(4)]; b0,b1,b2,b3=[b[...,i] for i in range(4)]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0],-1)
def qc(a): return a*np.array([1,-1,-1,-1.])
def rand_unit(rng,shape):
    x=rng.normal(size=shape+(4,)); return x/np.linalg.norm(x,axis=-1,keepdims=True)
def heatbath(rng,H,beta):
    """sample u ~ Haar * exp(beta Re(u H)); H (n,4)."""
    n=H.shape[0]; k=np.linalg.norm(H,axis=-1); lam=np.maximum(beta*k,1e-9)
    a0=np.zeros(n); todo=np.ones(n,bool)
    while todo.any():
        idx=np.where(todo)[0]; l=lam[idx]
        U=rng.random(len(idx)); x=1+np.log1p((1-U)*np.expm1(-2*l))/l
        x=np.clip(x,-1,1); acc=rng.random(len(idx))<np.sqrt(1-x*x)
        a0[idx[acc]]=x[acc]; todo[idx[acc]]=False
    d=rng.normal(size=(n,3)); d/=np.linalg.norm(d,axis=-1,keepdims=True)
    w=np.concatenate([a0[:,None],np.sqrt(1-a0**2)[:,None]*d],1)
    Hs=qc(H)/np.maximum(k,1e-300)[:,None]
    return qm(w,Hs)
def gibbs(rng,beta,hu,hv,C,M,N,nch=1000,burn=400,rec=100):
    u=rand_unit(rng,(nch,)); v=rand_unit(rng,(nch,))
    out_u=[];out_v=[]
    for s in range(burn+rec):
        u=heatbath(rng,hu+qm(qm(qm(M,v),N),C),beta)
        v=heatbath(rng,hv+qm(qm(qm(N,C),u),M),beta)
        if s>=burn: out_u.append(u.copy()); out_v.append(v.copy())
    return np.array(out_u),np.array(out_v)   # (rec,nch,4)
def quantities(u,v,hu,hv,C,M,N,beta):
    sh=u.shape[:-1]; u=u.reshape(-1,4); v=v.reshape(-1,4)
    Re=lambda x:x[...,0]
    ue=[u]+[qm(u,E[a]) for a in (1,2,3)]; ve=[v]+[qm(v,E[b]) for b in (1,2,3)]
    f=lambda ua,vb: Re(qm(qm(qm(qm(C,ua),M),vb),N))
    Y=f(ue[0],ve[0])
    A=np.array([[f(ue[a],ve[b]) for b in (1,2,3)] for a in (1,2,3)])  # (3,3,n)
    DA=np.array([f(ue[a],ve[0]) for a in (1,2,3)])   # Re(C u e_a M v N)
    EB=np.array([f(ue[0],ve[b]) for b in (1,2,3)])   # Re(C u M v e_b N)
    s=beta*(np.array([Re(qm(ue[a],hu)) for a in (1,2,3)])+DA)
    t=beta*(np.array([Re(qm(ve[b],hv)) for b in (1,2,3)])+EB)
    # D_aE_bA_ab = Y ; E_bA_ab=-Re(C u e_a M v N)=-DA[a] ; D_aA_ab=-EB[b] ; E_b s_a = beta A_ab
    Z=np.zeros_like(Y)
    for a in range(3):
        for b in range(3):
            Z+=Y + s[a]*(-DA[a]) + t[b]*(-EB[b]) + beta*A[a,b]**2 + s[a]*t[b]*A[a,b]
    S2=(A**2).sum((0,1))
    return Y.reshape(sh),Z.reshape(sh),S2.reshape(sh)
def se(x):  # x (rec,nch): SE from chain means
    m=x.mean(0); return m.std(ddof=1)/np.sqrt(len(m))
if __name__=="__main__":
    betas=[1,3.3,10,30]; rows=[]
    for bi,beta in enumerate(betas):
        for e in range(5):
            rng=np.random.default_rng(100+e)
            hu=rand_unit(rng,(5,)).sum(0); hv=rand_unit(rng,(5,)).sum(0)
            C,M,N=[rand_unit(rng,()) for _ in range(3)]
            rng=np.random.default_rng(10000*(bi+1)+e)   # sampling stream
            u,v=gibbs(rng,beta,hu,hv,C,M,N)
            Y,Z,S2=quantities(u,v,hu,hv,C,M,N,beta)
            EY=Y.mean(); varY=Y.var(); EZ=Z.mean(); L2=np.sqrt((Z**2).mean())
            T=(Y-EY)*Z; rhs=2+Y**2
            r=dict(beta=beta,ext=e,n=int(Y.size),L2Z_over_beta=L2/beta,EZ=EZ,EZ_se=se(Z),
              lhs=T.mean(),rhs=rhs.mean(),diff=(T-rhs).mean(),diff_se=se(T-rhs),
              EY=EY,varY=varY,ratio=varY/16*20736*beta**2,CS_bound=rhs.mean()**2/(Z**2).mean(),
              ident_err=float(np.abs(S2-rhs).max()),
              burn_diff=float(Y[:50].mean()-Y[50:].mean()),burn_se=float(np.sqrt(se(Y[:50])**2+se(Y[50:])**2)))
            r["P1"]=bool(r["ident_err"]<1e-9); r["P2"]=bool(abs(EZ)<=4*r["EZ_se"])
            r["P3"]=bool(abs(r["diff"])<=4*r["diff_se"]); r["P4"]=bool(r["L2Z_over_beta"]<=72)
            r["P5"]=bool(r["ratio"]>=1); r["P6"]=bool(varY>=0.99*r["CS_bound"])
            r["P7"]=bool(abs(r["burn_diff"])<=4*r["burn_se"])
            r={k:(float(x) if isinstance(x,(np.floating,float)) else x) for k,x in r.items()}; rows.append(r); print(json.dumps(r),flush=True)
            with open("zscore_rows.jsonl","a") as f: f.write(json.dumps(r)+"\n")
    with open("zscore_results.json","x") as f: json.dump(rows,f,indent=1)
