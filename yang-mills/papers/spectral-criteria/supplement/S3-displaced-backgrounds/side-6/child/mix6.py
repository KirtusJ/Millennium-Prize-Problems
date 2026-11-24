"""T208 independent SU(2) 4D heat-bath implementation (own code).
Usage: mix6.py STREAM OUTDIR [NDISCARD NMEAS GAP]   (STREAM 0..3; seeds fixed below)
PREDICATES (fixed before first run; tolerance: 2 combined sigma, combined=sqrt(se_mine^2+ref_sigma^2),
 2 sigma ~ 95% two-sided for independent approx-normal estimates; my se is a 4-stream jackknife (3 dof), so noisy):
 S1 structure: 24 colours x 27 pairs, no frozen link in any pair, links of different pairs of same colour share no plaquette.
 S2 frozen holonomies: W=-I (xy), B=i (xz).
 R1 mean spread agrees with .3442(.0084)
 R2 Var(f4) agrees with .06182(.00732)
 R3 J/Var f1 agrees with .0639(.0023)
 R4 J/Var f4 agrees with .0464(.0055)
 R5 (sanity) 0 < J/Var < 1 for both tests, Var(f1)>Var(f4).
"""
import sys, json, numpy as np
BETA=3.276133577; D=(6,6,6,12)
def qm(a,b):
    a0,a1,a2,a3=a[...,0],a[...,1],a[...,2],a[...,3]; b0,b1,b2,b3=b[...,0],b[...,1],b[...,2],b[...,3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0],-1)
def qc(a): return a*np.array([1,-1,-1,-1.])
ID=np.array([1.,0,0,0]); QI=np.array([0,1.,0,0])
def frozen_mask(mu,pos):  # pos (n,4)
    if mu==3: return np.zeros(len(pos),bool)
    o=[c for c in range(3) if c!=mu]
    return (pos[:,3]==0)&(pos[:,o[0]]%2==0)&(pos[:,o[1]]%2==0)
def shift(pos,nu,s):
    p=pos.copy(); p[:,nu]=(p[:,nu]+s)%D[nu]; return p
def get(U,mu,pos): return U[mu][pos[:,0],pos[:,1],pos[:,2],pos[:,3]]
def put(U,mu,pos,val): U[mu][pos[:,0],pos[:,1],pos[:,2],pos[:,3]]=val
def staple(U,mu,pos,excl=None):
    V=np.zeros((len(pos),4)); pm=shift(pos,mu,1)
    for nu in range(4):
        if nu==mu: continue
        if excl!=(nu,1):
            pn=shift(pos,nu,1)
            V+=qm(qm(get(U,nu,pm),qc(get(U,mu,pn))),qc(get(U,nu,pos)))
        if excl!=(nu,-1):
            pd=shift(pos,nu,-1); pmd=shift(pm,nu,-1)
            V+=qm(qm(qc(get(U,nu,pmd)),qc(get(U,mu,pd))),get(U,nu,pd))
    return V
def randdir(rng,n):
    v=rng.normal(size=(n,3)); return v/np.linalg.norm(v,axis=1)[:,None]
def sample_a0(rng,alpha):
    n=len(alpha); a0=np.empty(n); todo=np.arange(n)
    while len(todo):
        al=alpha[todo]; m=len(todo); ok=np.zeros(m,bool); val=np.zeros(m)
        small=al<2.0
        if small.any():
            s=np.where(small)[0]; w=rng.normal(size=(len(s),4)); x=w[:,0]/np.linalg.norm(w,axis=1)
            a=rng.random(len(s))<np.exp(al[s]*(x-1)); ok[s]=a; val[s]=x
        big=~small
        if big.any():
            s=np.where(big)[0]; A=al[s]; r=rng.random((4,len(s)))
            x=-(np.log(1-r[0])+np.cos(2*np.pi*r[1])**2*np.log(1-r[2]))/A
            a=r[3]**2<=1-x/2; ok[s]=a; val[s]=1-x
        a0[todo[ok]]=val[ok]; todo=todo[~ok]
    return a0
def heatbath(rng,V,beta=BETA):
    k=np.linalg.norm(V,axis=1); Vh=np.where(k[:,None]>1e-12,V/np.maximum(k,1e-300)[:,None],ID)
    a0=sample_a0(rng,beta*k); r=np.sqrt(np.maximum(1-a0**2,0))
    X=np.concatenate([a0[:,None],r[:,None]*randdir(rng,len(k))],1)
    return qm(X,qc(Vh))
def init(rng,hot):
    U=[]
    for mu in range(4):
        if hot:
            w=rng.normal(size=D+(4,)); w/=np.linalg.norm(w,axis=-1)[...,None]
        else: w=np.broadcast_to(ID,D+(4,)).copy()
        U.append(w)
    grid=np.array(np.meshgrid(*[np.arange(d) for d in D],indexing='ij')).reshape(4,-1).T
    for mu in range(3):
        f=grid[frozen_mask(mu,grid)]; put(U,mu,f,ID)
    U[1][2,0,0,0]=[-1,0,0,0]; U[2][2,0,0,0]=QI
    return U,grid
def sweep(U,rng,gp):
    for mu in range(4):
        p=gp[mu]; put(U,mu,p,heatbath(rng,staple(U,mu,p)))
def fobs(U):
    X=lambda x,y: U[0][x%6,y%6,0,0]; Y=lambda x,y: U[1][x%6,y%6,0,0]
    g=[]
    for cx,cy in [(0,0),(1,0),(0,1),(1,1)]:
        P=qm(qm(X(cx,cy),Y(cx+1,cy)),qm(qc(X(cx,cy+1)),qc(Y(cx,cy))))
        path=ID.copy()
        for x in range(cx): path=qm(path,X(x,0))
        for y in range(cy): path=qm(path,Y(cx,y))
        g.append(qm(qm(path,P),qc(path)))
    gb=sum(g)/4; return qm(QI,g[0])[0], qm(QI,gb)[0], 1-gb@gb
def colour_pairs():
    pairs={}
    planes=[(0,1),(0,2),(1,2)]
    for o,(i,j) in enumerate(planes):
        for px in (0,1):
         for py in (0,1):
          for pz in (0,1):
            p=(px,py,pz); k=8*o+px+2*py+4*pz; L=[]
            for x in range(px,6,2):
             for y in range(py,6,2):
              for z in range(pz,6,2):
                s=np.array([x,y,z,0]); su=s.copy()
                if p[j]==0: su[j]=(su[j]+1)%6
                sv=s.copy()
                if p[i]==0: sv[i]=(sv[i]+1)%6
                L.append((s,su,sv))
            pairs[k]=dict(i=i,j=j,pi=p[i],pj=p[j],s=np.array([a[0] for a in L]),u=np.array([a[1] for a in L]),v=np.array([a[2] for a in L]))
    return pairs
def check_structure(pairs):
    ok=True; msgs=[]
    for k,c in pairs.items():
        if len(c['s'])!=27: ok=False
        if frozen_mask(c['i'],c['u']).any() or frozen_mask(c['j'],c['v']).any(): ok=False; msgs.append(f'frozen in colour {k}')
        owner={}
        for n in range(27):
            for key in [(c['i'],tuple(c['u'][n])),(c['j'],tuple(c['v'][n]))]:
                if key in owner: ok=False; msgs.append(f'dup link colour {k}')
                owner[key]=n
        # plaquettes of the whole lattice
        for site in np.ndindex(*D):
            for mu in range(4):
                for nu in range(mu+1,4):
                    s=np.array(site); sm=s.copy(); sm[mu]=(sm[mu]+1)%D[mu]; sn=s.copy(); sn[nu]=(sn[nu]+1)%D[nu]
                    ls=[(mu,tuple(s)),(nu,tuple(sm)),(mu,tuple(sn)),(nu,tuple(s))]
                    ids={owner[l] for l in ls if l in owner}
                    if len(ids)>1: ok=False; msgs.append(f'shared plaq colour {k} {site} {mu}{nu}'); 
        if len(msgs)>5: break
    return ok,msgs
def pairdraw(U,rng,c,Vu,Vv):
    n=27; i,j=c['i'],c['j']; s=c['s']; se_i=shift(s,i,1); se_j=shift(s,j,1)
    pend=np.ones(n,bool)
    while pend.any():
        cu=heatbath(rng,Vu); cv=heatbath(rng,Vv)
        put(U,i,c['u'][pend],cu[pend]); put(U,j,c['v'][pend],cv[pend])
        Up=qm(qm(get(U,i,s),get(U,j,se_i)),qm(qc(get(U,i,se_j)),qc(get(U,j,s))))
        acc=rng.random(n)<np.exp(BETA*(Up[:,0]-1))
        # rejected pending entries get overwritten next round; accepted stay
        pend&=~acc
def measure_J(U,rng,pairs):
    sq=np.zeros(2); 
    for k,c in pairs.items():
        i,j=c['i'],c['j']
        sv_u=get(U,i,c['u']).copy(); sv_v=get(U,j,c['v']).copy()
        exu=(j,1 if c['pj']==1 else -1); exv=(i,1 if c['pi']==1 else -1)
        Vu=staple(U,i,c['u'],exu); Vv=staple(U,j,c['v'],exv)
        fs=[]
        for r in range(2):
            pairdraw(U,rng,c,Vu,Vv); fs.append(fobs(U)[:2])
            put(U,i,c['u'],sv_u); put(U,j,c['v'],sv_v)
        sq+=(np.array(fs[0])-np.array(fs[1]))**2/2
    return sq/24
if __name__=="__main__":
    st=int(sys.argv[1]); out=sys.argv[2]
    nd,nm,gap=(int(a) for a in sys.argv[3:6]) if len(sys.argv)>5 else (200,80,6)
    seed=[7101,7102,7103,7104][st]; hot=st in (1,3)
    rng=np.random.default_rng(seed); U,grid=init(rng,hot)
    gp=[grid[~frozen_mask(mu,grid)] for mu in range(4)]
    pairs=colour_pairs(); ok,msgs=check_structure(pairs) if st==0 else (None,None)
    print('structure',ok,msgs,flush=True)
    for _ in range(nd): sweep(U,rng,gp)
    rec=[]
    for m in range(nm):
        for _ in range(gap): sweep(U,rng,gp)
        f1,f4,sp=fobs(U); J=measure_J(U,rng,pairs)
        rec.append([f1,f4,sp,J[0],J[1]])
    with open(f"{out}/stream{st}.json","x") as fh:
        json.dump(dict(stream=st,seed=seed,hot=hot,nd=nd,nm=nm,gap=gap,structure_ok=ok,structure_msgs=msgs,rec=rec),fh)
    print('done',st,np.mean(rec,0))
