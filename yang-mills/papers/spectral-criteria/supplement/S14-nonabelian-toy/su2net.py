import numpy as np, itertools, functools, scipy.sparse as sps
from su2core import *
dim=lambda j: tw(j)+1
def gen_on(j,dual):
    Jz,Jp,Jm=gens(j)
    return [(-G.T if dual else G) for G in (Jz,Jp,Jm)]
@functools.lru_cache(maxsize=None)
def inv_basis(j1,j2,j3):
    """orthonormal basis of the invariants in V*_{j1} (x) V_{j2} (x) V*_{j3} (x) V_{j3}; columns; index order (m1,n2,m3,n3)"""
    if abs(tw(j1)-tw(j2))%2: return np.zeros((dim(j1)*dim(j2)*dim(j3)**2,0))
    cols=[]
    for i in range(int(abs(j1-j2)), int(min(j1+j2,2*j3))+1):
        t=np.zeros((dim(j1),dim(j2),dim(j3),dim(j3)))
        for a,m1 in enumerate(ms(j1)):
            for b,n2 in enumerate(ms(j2)):
                mu=n2-m1
                if abs(mu)>i: continue
                c1=cg(j1,m1,i,mu,j2,n2)
                if c1==0: continue
                for c,m3 in enumerate(ms(j3)):
                    n3=m3-mu
                    if abs(n3)>j3: continue
                    d=ms(j3).index(n3); t[a,b,c,d]+=(-1)**int(round(abs(mu)))*c1*cg(j3,m3,i,-mu,j3,n3)
        if np.abs(t).max()>1e-12: cols.append(t.ravel())
    if not cols: return np.zeros((dim(j1)*dim(j2)*dim(j3)**2,0))
    Q,R=np.linalg.qr(np.array(cols).T); return Q
def check_inv(j1,j2,j3):
    E=inv_basis(j1,j2,j3)
    if E.shape[1]==0: return 0.0
    T=E.reshape(dim(j1),dim(j2),dim(j3),dim(j3),-1); worst=0
    g1=gen_on(j1,True); g2=gen_on(j2,False); g3=gen_on(j3,True); g4=gen_on(j3,False)
    for k in range(3):
        r=np.einsum('xa,abcde->xbcde',g1[k],T)+np.einsum('xb,abcde->axcde',g2[k],T)+np.einsum('xc,abcde->abxde',g3[k],T)+np.einsum('xd,abcde->abcxe',g4[k],T)
        worst=max(worst,np.abs(r).max())
    return worst
half=(0.5,-0.5)
def Lm(j,jp,mu): return Lmat(j,jp,mu) if abs(jp-j)==0.5 and jp>=0 else None
def two(j,j1,jp,mu1,mu2):
    A=Lm(j,j1,mu1); B=Lm(j1,jp,mu2) if A is not None else None
    return None if (A is None or B is None) else B@A
def reduce(Esrc,shape_src,Edst,ops):
    """ops: list of (coefficient, [matrix or None for each of the four indices]); returns Edst^H (sum) Esrc"""
    T=Esrc.reshape(*shape_src,-1); acc=0
    for coef,mats in ops:
        X=T
        for ax,Mx in enumerate(mats):
            if Mx is not None: X=np.moveaxis(np.tensordot(Mx,X,axes=(1,ax)),0,ax)
        acc=acc+coef*X
    if isinstance(acc,int): return None
    return Edst.conj().T@acc.reshape(-1,T.shape[-1])
# vertex 0: indices (m_a dual, n_b, m_c dual, n_c); vertex 1: (n_a , m_b dual, m_d dual, n_d)  -- both stored as inv_basis(j_dual, j_fund, j_loop)
@functools.lru_cache(maxsize=None)
def X0(kind,ja,jb,jc,jap,jbp,jcp,j1):
    E=inv_basis(ja,jb,jc); Ed=inv_basis(jap,jbp,jcp)
    if E.shape[1]==0 or Ed.shape[1]==0: return None
    ops=[]
    if kind=='W0':
        for al in half:
            for de in half:
                A=two(ja,j1,jap,al,-de); C1=Lm(jc,jcp,-al); C2=Lm(jc,jcp,-de)
                if A is None or C1 is None or C2 is None or jbp!=jb: return None
                ops.append(((1j)**int(round(2*al)),[A,None,C1,C2]))
    elif kind=='W1':
        for be in half:
            for ga in half:
                Bm=two(jb,j1,jbp,be,-ga); C1=Lm(jc,jcp,be); C2=Lm(jc,jcp,ga)
                if Bm is None or C1 is None or C2 is None or jap!=ja: return None
                ops.append(((1j)**int(round(-2*ga)),[None,Bm,C1,C2]))
    elif kind=='C':
        for al in half:
            C1=Lm(jc,jcp,al)
            if C1 is None or jap!=ja or jbp!=jb: return None
            ops.append((1.0,[None,None,C1,C1]))
    elif kind=='AB':
        for al in half:
            A=Lm(ja,jap,al); Bm=Lm(jb,jbp,al)
            if A is None or Bm is None or jcp!=jc: return None
            ops.append((1.0,[A,Bm,None,None]))
    elif kind=='ABC':
        for al in half:
            for ga in half:
                A=Lm(ja,jap,al); Bm=Lm(jb,jbp,ga); C1=Lm(jc,jcp,ga); C2=Lm(jc,jcp,al)
                if A is None or Bm is None or C1 is None or C2 is None: return None
                ops.append((1.0,[A,Bm,C1,C2]))
    return reduce(E,(dim(ja),dim(jb),dim(jc),dim(jc)),Ed,ops)
@functools.lru_cache(maxsize=None)
def X1(kind,ja,jb,jd,jap,jbp,jdp,j1):
    # stored as inv_basis(jb (dual, m_b), ja (fund, n_a), jd): index order (m_b, n_a, m_d, n_d)
    E=inv_basis(jb,ja,jd); Ed=inv_basis(jbp,jap,jdp)
    if E.shape[1]==0 or Ed.shape[1]==0: return None
    ops=[]
    if kind=='W0':
        for be in half:
            for ga in half:
                A=two(ja,j1,jap,be,-ga); D1=Lm(jd,jdp,be); D2=Lm(jd,jdp,ga)
                if A is None or D1 is None or D2 is None or jbp!=jb: return None
                ops.append(((1j)**int(round(-2*ga)),[None,A,D1,D2]))
    elif kind=='W1':
        for al in half:
            for de in half:
                Bm=two(jb,j1,jbp,al,-de); D1=Lm(jd,jdp,-al); D2=Lm(jd,jdp,-de)
                if Bm is None or D1 is None or D2 is None or jap!=ja: return None
                ops.append(((1j)**int(round(2*al)),[Bm,None,D1,D2]))
    elif kind in ('AB','ABC'):
        for be in half:
            A=Lm(ja,jap,be); Bm=Lm(jb,jbp,be)
            if A is None or Bm is None or jdp!=jd: return None
            ops.append((1.0,[Bm,A,None,None]))
    return reduce(E,(dim(jb),dim(ja),dim(jd),dim(jd)),Ed,ops)
class Net:
    def __init__(s,J):
        s.J=J; sp=[k/2 for k in range(int(2*J)+1)]; s.sp=sp; s.blocks={}; off=0
        for ja in sp:
            for jb in sp:
                if (tw(ja)+tw(jb))%2: continue
                for jc in sp:
                    r0=inv_basis(ja,jb,jc).shape[1]
                    if r0==0: continue
                    for jd in sp:
                        r1=inv_basis(jb,ja,jd).shape[1]
                        if r1==0: continue
                        s.blocks[(ja,jb,jc,jd)]=(off,r0,r1); off+=r0*r1
        s.n=off
    def nf(s,j,jp): return np.sqrt(dim(j)/dim(jp))
    def assemble(s,kind):
        rows=[];cols=[];vals=[]
        for (ja,jb,jc,jd),(off,r0,r1) in s.blocks.items():
            if kind=='W0': tg=[(ja+da,jb,jc+dc,jd+dd) for da in (-1,0,1) for dc in (-.5,.5) for dd in (-.5,.5)]
            elif kind=='W1': tg=[(ja,jb+db,jc+dc,jd+dd) for db in (-1,0,1) for dc in (-.5,.5) for dd in (-.5,.5)]
            elif kind=='C': tg=[(ja,jb,jc+dc,jd) for dc in (-.5,.5)]
            elif kind=='AB': tg=[(ja+da,jb+db,jc,jd) for da in (-.5,.5) for db in (-.5,.5)]
            elif kind=='ABC': tg=[(ja+da,jb+db,jc+dc,jd) for da in (-.5,.5) for db in (-.5,.5) for dc in (-.5,.5)]
            for t in tg:
                if t not in s.blocks: continue
                jap,jbp,jcp,jdp=t; offp,r0p,r1p=s.blocks[t]; Mb=0
                j1s=[None]
                if kind=='W0': j1s=[j for j in (ja-.5,ja+.5) if j>=0 and abs(jap-j)==0.5]
                if kind=='W1': j1s=[j for j in (jb-.5,jb+.5) if j>=0 and abs(jbp-j)==0.5]
                for j1 in j1s:
                    A=X0(kind,ja,jb,jc,jap,jbp,jcp,j1)
                    Bq=X1(kind,ja,jb,jd,jap,jbp,jdp,j1) if kind!='C' else (np.eye(r1) if (jap,jbp,jdp)==(ja,jb,jd) else None)
                    if A is None or Bq is None: continue
                    Mb=Mb+np.kron(A,Bq)
                if isinstance(Mb,int): continue
                f=s.nf(ja,jap)*s.nf(jb,jbp)*s.nf(jc,jcp)*s.nf(jd,jdp)*(0.5 if kind in ('W0','W1') else 1.0)
                Mb=f*Mb; nz=np.nonzero(np.abs(Mb)>1e-14)
                rows+=list(offp+nz[0]); cols+=list(off+nz[1]); vals+=list(Mb[nz])
        return sps.csr_matrix((vals,(rows,cols)),shape=(s.n,s.n))
    def evaluate(s,key,a,b,c,d):
        """values of the basis functions of one block at group elements (for validation)"""
        ja,jb,jc,jd=key; off,r0,r1=s.blocks[key]
        E0=inv_basis(ja,jb,jc).reshape(dim(ja),dim(jb),dim(jc),dim(jc),r0); E1=inv_basis(jb,ja,jd).reshape(dim(jb),dim(ja),dim(jd),dim(jd),r1)
        Da,Db,Dc,Dd=[np.sqrt(dim(j))*Dmat(j,g) for j,g in ((ja,a),(jb,b),(jc,c),(jd,d))]
        # Psi = sum t0[m_a,n_b,m_c,n_c] t1[m_b,n_a,m_d,n_d] Da[m_a,n_a] Db[m_b,n_b] Dc[m_c,n_c] Dd[m_d,n_d]
        return np.einsum('abcde,fghif,ag,fb,cd,hi->e',E0,np.moveaxis(E1,4,4),Da,Db,Dc,Dd) if False else np.einsum('pqrsx,uvwzy,pv,uq,rs,wz->xy',E0,E1,Da,Db,Dc,Dd).ravel()
