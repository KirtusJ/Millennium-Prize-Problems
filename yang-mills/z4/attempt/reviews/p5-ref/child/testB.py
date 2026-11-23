"""Test B. Predicates fixed before first run.
C^N = D[p0,:] pinv(D^T D) D[p0,:]^T (diag of projector onto range D). pinv by eigh of D^T D; eigenvalue cut: lam > 1e-9
(source: spectrum is reported; gap between largest 'zero' and smallest kept eigenvalue must exceed 1e3 ratio, else flagged).
B1: |C^1-7/24|<1e-9 [float roundoff]. B2: |C^2-0.49267|<5e-6 [5 decimals]. B3: |C^3-0.49916|<5e-6.
B4: C^1<=C^2<=C^3<0.5 (only N=1..3 computed; N=4 not).
B5: Q=D''^T D'' ; min eig>0 and |min eig - 0.837722|<5e-7 (N=1), |.-0.147122|<5e-7 (N=2). N=3 reported only.
Orientation: link (x,mu) = x->x+e_mu. p0 = (0;1,2).
"""
import numpy as np, itertools, json, sys
tag=sys.argv[1]
def build(N):
    inter=lambda x: max(abs(c) for c in x)<N
    inbox=lambda x: max(abs(c) for c in x)<=N
    e=np.eye(4,dtype=int)
    links=[]
    for x in itertools.product(range(-N,N+1),repeat=4):
        for mu in range(4):
            y=tuple(np.array(x)+e[mu])
            if inbox(y) and (inter(x) or inter(y)): links.append((x,mu))
    lid={l:i for i,l in enumerate(links)}
    rows=[];plaq=[]
    for x in itertools.product(range(-N-1,N+2),repeat=4):
        xa=np.array(x)
        for mu in range(4):
            for nu in range(mu+1,4):
                terms=[((tuple(xa+e[mu]),nu),1),((x,nu),-1),((tuple(xa+e[nu]),mu),-1),((x,mu),1)]
                tt=[(lid[l],s) for l,s in terms if l in lid]
                if tt: rows.append(tt); plaq.append((x,mu,nu))
    D=np.zeros((len(rows),len(links)))
    for r,tt in enumerate(rows):
        for c,s in tt: D[r,c]=s
    return links,plaq,D
out={};claims=[]
def rec(n,ok,info): claims.append((n,bool(ok),info)); print(n,'PASS' if ok else 'FAIL',info,flush=True)
C={}
for N in (1,2,3):
    links,plaq,D=build(N)
    p0=plaq.index(((0,0,0,0),1,2))
    Q=D.T@D
    w,V=np.linalg.eigh(Q)
    keep=w>1e-9
    zero_max=w[~keep].max(); keepmin=w[keep].min()
    d=D[p0]@V[:,keep]
    C[N]=float(np.sum((d/np.sqrt(w[keep]))**2))
    print(f'N={N}: links {len(links)} plaq {len(plaq)} kernel dim {int((~keep).sum())} max|zero eig|={zero_max:.2e} min kept={keepmin:.4e} C={C[N]:.10f}',flush=True)
    out[N]=dict(links=len(links),plaq=len(plaq),kernel=int((~keep).sum()),zero_max=float(zero_max),keepmin=float(keepmin),C=C[N])
    # B5
    tint=set(i for i,(x,mu) in enumerate(links) if mu==0 and max(abs(c) for c in x)<N)
    cols=[i for i in range(len(links)) if i not in tint]
    Q2=D[:,cols].T@D[:,cols]; mn=np.linalg.eigvalsh(Q2).min()
    out[N]['B5_min_eig']=float(mn); out[N]['B5_links']=len(cols)
    print(f'   B5 N={N}: |Lambda\'\'|={len(cols)} min eig Q={mn:.6f}',flush=True)
rec('B1',abs(C[1]-7/24)<1e-9,f'C1={C[1]:.12f} 7/24={7/24:.12f}')
rec('B2',abs(C[2]-0.49267)<5e-6,f'C2={C[2]:.7f}')
rec('B3',abs(C[3]-0.49916)<5e-6,f'C3={C[3]:.7f}')
rec('B4',C[1]<=C[2]<=C[3]<0.5,f'{C[1]:.6f}<={C[2]:.6f}<={C[3]:.6f}<0.5')
rec('B5a',out[1]['B5_min_eig']>0 and abs(out[1]['B5_min_eig']-0.837722)<5e-7,f"N=1 min eig {out[1]['B5_min_eig']:.7f}")
rec('B5b',out[2]['B5_min_eig']>0 and abs(out[2]['B5_min_eig']-0.147122)<5e-7,f"N=2 min eig {out[2]['B5_min_eig']:.7f}; N=3 {out[3]['B5_min_eig']:.6f} (unclaimed)")
json.dump(dict(out=out,claims=claims),open(f'results/B_{tag}.json','x'),indent=1)
sys.exit(0 if all(c[1] for c in claims) else 1)
