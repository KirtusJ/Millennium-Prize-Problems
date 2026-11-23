"""PCP T125 child. Predicates fixed before first run:
P1 (Q1): matrix first visible energy == closed form 2acosh(1+2sin^2(pi/max(N1,N2))), tol 1e-8 (printed precision of auditor / eigh error ~1e-12).
P2 (Q1): matrix E == auditor E to 1e-8 (auditor gives 8 decimals).
P3 (Q1): matrix weight == auditor weight to 1e-7 relative 1e-5 (auditor 7-8 digits). Weight convention: ORDERED pairs (v,v'), mu=3/2*sum a a'; unordered also reported.
P4 (Q2): matrix E_atom,mu_atom == closed form, tol 1e-9 rel.
Mode degeneracy: eigenvalues grouped within 1e-9; a summed per group (basis independent).
Convergence rates: measured only (log-ratio of successive N).
"""
import numpy as np, math
def build(N):
    N1,N2,N3=N; n=N1*N2*N3
    idx=lambda x:(x[0]%N1)*N2*N3+(x[1]%N2)*N3+(x[2]%N3)
    link=lambda x,d:3*idx(x)+d
    C=np.zeros((3*n,3*n)); r=0; P=None
    for a in range(N1):
      for b in range(N2):
        for c in range(N3):
          x=(a,b,c)
          for (i,j) in ((0,1),(0,2),(1,2)):
            def sh(y,d): y=list(y); y[d]+=1; return tuple(y)
            C[r,link(sh(x,i),j)]+=1; C[r,link(x,j)]-=1
            C[r,link(sh(x,j),i)]-=1; C[r,link(x,i)]+=1
            if x==(0,0,0) and (i,j)==(0,1): P=r
            r+=1
    return C,P
def modes(N):
    C,P=build(N); M=C.T@C
    ev,V=np.linalg.eigh(M)
    keep=ev>1e-9
    ev=ev[keep]; V=V[:,keep]
    w=np.arccosh(1+ev/2)
    a=(C[P]@V)**2/(2*np.sinh(w))
    # group
    G=[]
    for e,ww,aa in zip(ev,w,a):
        if G and abs(G[-1][0]-e)<1e-9: G[-1][2]+=aa
        else: G.append([e,ww,aa])
    return G,a.sum()
def first(G):
    vis=[(g[1],g[2]) for g in G if g[2]>1e-12]
    E=2*vis[0][0]
    # ordered pairs at energy E: all (g,g') with w+w'=E within 1e-9
    tot=0;tot_u=0
    for g in vis:
        for h in vis:
            if abs(g[0]+h[0]-E)<1e-9: tot+=1.5*g[1]*h[1]
    return E,tot,vis
def cf(N):
    m=4*math.sin(math.pi/N)**2; w=math.acosh(1+m/2)
    return 2*w,1.5*(2*m/(N**3*math.sinh(w)))**2
if __name__=="__main__":
    aud={(2,2,2):(3.52549435,0.046875),(3,3,3):(3.13359847,0.01410935),(3,2,5):(3.13359847,0.00285714)}
    print("Q1")
    for N,(aE,aw) in aud.items():
        G,s=modes(N); E,mu,vis=first(G)
        Ecl=2*math.acosh(1+2*math.sin(math.pi/max(N[0],N[1]))**2)
        print(N,"E=%.8f mu=%.8f mu_unordered=%.8f sum_a=%.8f Ecf=%.8f"%(E,mu,mu/2 if len(vis)>0 else 0,s,Ecl),
          "P1",abs(E-Ecl)<1e-8,"P2",abs(E-aE)<1e-8,"P3",abs(mu-aw)<1e-7,"n_visible_groups",len(vis))
    print("Q2")
    for n in (4,8):
        G,s=modes((n,n,n)); E,mu,_=first(G); Ec,mc=cf(n)
        print(n,"matrix",E,mu,"closed",Ec,mc,"P4",abs(E-Ec)<1e-9*Ec and abs(mu-mc)<1e-9*mc)
    prev=None
    for n in (4,8,16,32):
        Ec,mc=cf(n); d1=n*Ec-4*math.pi; d2=n**8*mc-24*math.pi**2
        r=("" if prev is None else " rate1=%.3f rate2=%.3f"%(math.log2(prev[0]/d1),math.log2(prev[1]/d2)))
        print(n,"N*E-4pi=%.10e N^8mu-24pi^2=%.10e"%(d1,d2)+r); prev=(d1,d2)
