"""cont3.py -- Rayleigh-Ritz spectrum of h3 = -1/2 Lap_{R^9} + 2 sum_{i<j} |Y_i x Y_j|^2 on color-SO(3)-invariant states.
Y_i in R^3 (su(2) via U_i = exp(i Y_i.sigma)); kappa=2 as in D4 of NUMERICS_2DIR (per pair; derivation repeated in report).
Basis: Psi = R_{n1l1}(r1)R_{n2l2}(r2)R_{n3l3}(r3) sum_m (l1 l2 l3;m1 m2 m3) Y_{l1m1}Y_{l2m2}Y_{l3m3}, 3D HO radial
functions of frequency w, truncation sum_i (2n_i+l_i) <= NMAX (O(9)-invariant, hence spatial-SO(3)-invariant truncation).
|Yi x Yj|^2 = ri^2 rj^2 (2/3)(1 - P2(ni.nj)); P2 matrix elements by Edmonds 7.1.6 (ang.py), with pair (i,j) coupled to l_k;
the 3j reordering phases (-1)^{l1+l2+l3} cancel between bra and ket because l_i+l_i' is even for k=2.
Kinetic: -1/2 Lap = H_ho - (w/2) s, s = w r^2. Radial integrals exact by generalized Gauss-Laguerre (alpha=1/2), NMAX+12 nodes.
Sectors: parities (-1)^{l_i} of Y_i -> -Y_i (exact symmetries), 8 sectors; dense eigh per sector; only representatives
(000),(001),(110),(111) are diagonalised, images under permutations counted with multiplicity 3 (set before recorded runs).
Usage: python3 cont3.py MODE NMAX W OUTFILE      MODE in {h3, ctrl}
PREDICATES (fixed before first run):
 C1 (ctrl) potential replaced by (w^2/2) sum r_i^2: eigenvalues = w(sum(2n+l) + 9/2) exactly, max abs err < 1e-10
    (tolerance: double rounding over <=NMAX-term sums ~1e-13, 1e-10 leaves margin for the Gauss-Laguerre weights).
 C2 (ctrl) two-direction reduction: basis n3=l3=0, link-3 kinetic and V13,V23 dropped -> E0 = 3.3505330, E1-E0 = 1.974964
    (cont.py values of NUMERICS_2DIR) to 2e-4 at NMAX=40 (tolerance: their convergence table, levels move ~1e-4 at this size).
 C3 (h3) matrix symmetric to 1e-12 relative.
 C4 (h3) spatial SO(3) multiplets: every level below E0+4 of the pooled spectrum belongs to a cluster (spread < 1e-8)
    of odd size 2J+1 summed over sectors (degeneracy test of the angular algebra; truncation is SO(3)-invariant).
    Reported: number of clusters and how many have odd size (rule 4).
 C5 (analyse) Rayleigh-Ritz: E0, E1 non-increasing in NMAX; converged digits reported (measured only).
"""
import sys, json, math, time
import numpy as np
from ang import pairA

def gl(n, alpha):
    k=np.arange(n); J=np.diag(2*k+alpha+1)+np.diag(np.sqrt(k[1:]*(k[1:]+alpha)),1)+np.diag(np.sqrt(k[1:]*(k[1:]+alpha)),-1)
    x=np.linalg.eigvalsh(J)
    Q=np.zeros((n,n)); Q[0]=1/math.sqrt(math.gamma(alpha+1)); Q[1]=(alpha+1-x)*Q[0]/math.sqrt(1+alpha)
    for j in range(1,n-1): Q[j+1]=((2*j+alpha+1-x)*Q[j]-math.sqrt(j*(j+alpha))*Q[j-1])/math.sqrt((j+1)*(j+1+alpha))
    return x, 1/(Q**2).sum(0)

def radq(nmax,l,s):
    a=l+0.5; Q=np.zeros((nmax+1,len(s))); Q[0]=1/math.sqrt(math.gamma(a+1))
    if nmax>=1: Q[1]=(a+1-s)*Q[0]/math.sqrt(1+a)
    for j in range(1,nmax): Q[j+1]=((2*j+a+1-s)*Q[j]-math.sqrt(j*(j+a))*Q[j-1])/math.sqrt((j+1)*(j+1+a))
    return Q*s**(l/2)

def build(NMAX,w,mode):
    s,ws=gl(NMAX+12,0.5)
    q={l:radq((NMAX-l)//2,l,s) for l in range(NMAX+1)}
    S={}
    for l in range(NMAX+1):
        for lp in (l-2,l,l+2):
            if 0<=lp<=NMAX: S[(l,lp)]=(q[l]*ws*s)@q[lp].T
    states=[]
    for l1 in range(NMAX+1):
     for l2 in range(NMAX+1-l1):
      for l3 in range(abs(l1-l2),min(l1+l2,NMAX-l1-l2)+1):
        for n1 in range((NMAX-l1-l2-l3)//2+1):
         for n2 in range((NMAX-l1-l2-l3-2*n1)//2+1):
          for n3 in range((NMAX-l1-l2-l3-2*n1-2*n2)//2+1):
            states.append((n1,l1,n2,l2,n3,l3))
    return s,ws,q,S,states

def sector_matrix(states,S,w,mode,NMAX):
    D=len(states); idx={st:i for i,st in enumerate(states)}; H=np.zeros((D,D))
    for i,(n1,l1,n2,l2,n3,l3) in enumerate(states):
        nl=[(n1,l1),(n2,l2),(n3,l3)]
        # kinetic (per link): w(2n+l+3/2) delta - (w/2) S
        for a in range(3):
            if mode=='c2' and a==2: continue
            n,l=nl[a]
            for np_ in (n-1,n,n+1):
                if np_<0 or np_>=S[(l,l)].shape[1]: continue
                t=list(nl); t[a]=(np_,l); j=idx.get((t[0][0],t[0][1],t[1][0],t[1][1],t[2][0],t[2][1]))
                if j is None: continue
                H[i,j]+=-(w/2)*S[(l,l)][n,np_]+(w*(2*n+l+1.5) if np_==n else 0)
                if mode=='ctrl': H[i,j]+=(w/2)*S[(l,l)][n,np_]
        if mode=='ctrl': continue
        pairs=[(0,1,2)] if mode=='c2' else [(0,1,2),(0,2,1),(1,2,0)]
        for (a,b,c) in pairs:
            (na,la),(nb,lb),(nc,lc)=nl[a],nl[b],nl[c]
            for lap in (la-2,la,la+2):
                if lap<0 or (la,lap) not in S: continue
                for lbp in (lb-2,lb,lb+2):
                    if lbp<0 or (lb,lbp) not in S: continue
                    ang=(1.0 if (lap==la and lbp==lb) else 0.0)-pairA(la,lb,lap,lbp,lc,2)
                    if ang==0: continue
                    Sa=S[(la,lap)]; Sb=S[(lb,lbp)]
                    for nap in range(Sa.shape[1]):
                        if abs(nap-na)>2: continue
                        for nbp in range(Sb.shape[1]):
                            if abs(nbp-nb)>2: continue
                            t=list(nl); t[a]=(nap,lap); t[b]=(nbp,lbp)
                            j=idx.get((t[0][0],t[0][1],t[1][0],t[1][1],t[2][0],t[2][1]))
                            if j is None: continue
                            H[i,j]+=2*(2/3)*ang*Sa[na,nap]*Sb[nb,nbp]/w**2
    return H

def main():
    mode,NMAX,w,out=sys.argv[1],int(sys.argv[2]),float(sys.argv[3]),sys.argv[4]
    f=open(out,'x'); t0=time.time(); res={'mode':mode,'NMAX':NMAX,'w':w}; ok=True
    if mode=='ctrl':
        s,ws,q,S,states=build(NMAX,w,mode)
        H=sector_matrix(states,S,w,'ctrl',NMAX)
        ev=np.linalg.eigvalsh(H); ex=np.sort([w*(2*a+b+2*c+d+2*e+g+4.5) for (a,b,c,d,e,g) in states])
        res['C1_err']=float(np.abs(ev-ex).max()); res['C1']=bool(res['C1_err']<1e-10); ok&=res['C1']
        # C2: two-direction reduction
        N2=40; s,ws,q,S,st=build(N2,w,'c2'); st2=[x for x in st if x[4]==0 and x[5]==0]
        ev2=[]
        for p in (0,1):
            stp=[x for x in st2 if x[1]%2==p]
            ev2+=list(np.linalg.eigvalsh(sector_matrix(stp,S,w,'c2',N2))[:4])
        ev2=np.sort(ev2); res['C2_levels']=ev2[:4].tolist()
        res['C2_E0']=float(ev2[0]); res['C2_gap']=float(ev2[1]-ev2[0])
        res['C2']=bool(abs(ev2[0]-3.3505330)<2e-4 and abs(ev2[1]-ev2[0]-1.974964)<2e-4); ok&=res['C2']
    else:
        s,ws,q,S,states=build(NMAX,w,mode); res['dim']=len(states); allev=[]; res['sectors']={}
        # sector representatives; (0,0,1) and (1,1,0) each stand for 3 permutation images (exact S3 symmetry), counted 3x
        for p,mult in [((0,0,0),1),((0,0,1),3),((1,1,0),3),((1,1,1),1)]:
            stp=[x for x in states if (x[1]%2,x[3]%2,x[5]%2)==p]
            if not stp: continue
            H=sector_matrix(stp,S,w,mode,NMAX)
            asym=float(np.abs(H-H.T).max()/np.abs(H).max()); ev=np.linalg.eigvalsh((H+H.T)/2)
            res['sectors'][str(p)]={'dim':len(stp),'asym':asym,'low':ev[:8].tolist()}
            ok&= asym<1e-12; allev+=[(e,str(p)) for e in ev[:30] for _ in range(mult)]
            print(p,len(stp),ev[:5],time.time()-t0,flush=True)
        res['C3']=bool(all(v['asym']<1e-12 for v in res['sectors'].values()))
        allev.sort(); E0=allev[0][0]; cl=[]
        for e,p in allev:
            if e>E0+4: break
            if cl and e-cl[-1][-1][0]<1e-8: cl[-1].append((e,p))
            else: cl.append([(e,p)])
        res['clusters']=[{'E':c[0][0],'E-E0':c[0][0]-E0,'size':len(c),'sectors':[x[1] for x in c]} for c in cl]
        nodd=sum(1 for c in cl if len(c)%2==1); res['C4_counts']=[nodd,len(cl)]
        res['C4']=bool(nodd==len(cl)); ok&=res['C4']
        for c in res['clusters'][:10]: print(c)
    res['time']=time.time()-t0; json.dump(res,f,indent=1); f.close(); print({k:v for k,v in res.items() if k not in('sectors','clusters')})
    sys.exit(0 if ok else 1)
main()
