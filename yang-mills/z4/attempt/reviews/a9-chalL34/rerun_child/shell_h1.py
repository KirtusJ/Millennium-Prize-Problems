"""Homology of lattice shell S_N in Z^4.
Predicates (fixed before first run):
 P0 control: sites with sup-norm 1 in Z^4 = 80.
 P1 V(N)=(2N+1)^4-(2N-1)^4 : 80, 544.
 P2 graph connected (c=1).
 P3 d1*d2 = 0 over Z (boundary of boundary).
 P4 b1 = 0 over GF(2) and over Q (modular rank mod p=2^31-1 equals rank over Q unless p divides an elementary
    divisor; the Z elimination below is the authoritative check), N=1,2.
 P5 integer elimination with only +-1 pivots exhausts the matrix (all elementary divisors 1 => H_1 torsion-free, trivial).
 P6 GF(2) rank == Z-elimination rank == mod p rank.
Tolerance: none, exact integer arithmetic.  Ranks via sparse elimination.
Usage: python3 shell_h1.py N   (writes res_N.txt, mode 'x')
"""
import sys, itertools
N=int(sys.argv[1])
R=range(-N,N+1)
sites=[x for x in itertools.product(R,repeat=4) if max(map(abs,x))==N]
S=set(sites); V=len(sites)
def sh(x,m,s=1):
    y=list(x); y[m]+=s; return tuple(y)
links={}
for x in sites:
    for m in range(4):
        y=sh(x,m)
        if y in S: links[(x,m)]=len(links)
E=len(links)
plaq=[]
for x in sites:
    for m in range(4):
        for n in range(m+1,4):
            a,b,c=sh(x,m),sh(sh(x,m),n),sh(x,n)
            if a in S and b in S and c in S: plaq.append((x,m,n))
F=len(plaq)
# d2 columns: plaquette -> {link:coef}; boundary = (x,m)+(x+m,n)-(x+n,m)-(x,n)
cols=[]
for x,m,n in plaq:
    c={}
    for k,s in (((x,m),1),((sh(x,m),n),1),((sh(x,n),m),-1),((x,n),-1)):
        c[links[k]]=c.get(links[k],0)+s
    cols.append(c)
# components
par=list(range(V)); idx={x:i for i,x in enumerate(sites)}
def f(a):
    while par[a]!=a: par[a]=par[par[a]]; a=par[a]
    return a
d1={}  # link -> (tail,head)
for (x,m),i in links.items():
    d1[i]=(idx[x],idx[sh(x,m)]); par[f(idx[x])]=f(idx[sh(x,m)])
comp=len({f(i) for i in range(V)})
# P3
p3=True
for c in cols:
    div=[0]*V
    for l,s in c.items():
        t,h=d1[l]; div[h]+=s; div[t]-=s
    if any(div): p3=False
def rank_mod(cols,p):
    piv={}; r=0
    for c in cols:
        c={k:v%p for k,v in c.items() if v%p}
        while c:
            k=min(c)
            if k in piv:
                q=piv[k]; fct=c[k]
                for kk,vv in q.items():
                    nv=(c.get(kk,0)-fct*vv)%p
                    if nv: c[kk]=nv
                    else: c.pop(kk,None)
            else:
                inv=pow(c[k],-1,p); piv[k]={kk:vv*inv%p for kk,vv in c.items()}; r+=1; break
    return r
# integer elimination with unit pivots (row/col ops preserve elementary divisors when pivot is +-1)
def unit_elim(cols):
    M=[dict(c) for c in cols]  # columns
    rows={}                    # row -> set of col idx
    for j,c in enumerate(M):
        for i in c: rows.setdefault(i,set()).add(j)
    alive=set(range(len(M))); steps=0
    while True:
        best=None
        for j in alive:
            for i,v in M[j].items():
                if abs(v)==1:
                    w=(len(M[j])-1)*(len(rows[i])-1)
                    if best is None or w<best[0]: best=(w,j,i)
                    if w==0: break
            if best and best[0]==0: break
        if best is None: break
        _,j,i=best; pv=M[j][i]
        # eliminate row i from other columns: col_k -= (a/pv) col_j ; then col_j & row i removed (unimodular)
        for k in list(rows[i]):
            if k==j: continue
            fct=M[k][i]*pv  # pv=+-1 so a/pv=a*pv
            for ii,vv in M[j].items():
                nv=M[k].get(ii,0)-fct*vv
                if nv: 
                    if ii not in M[k]: rows[ii].add(k)
                    M[k][ii]=nv
                else:
                    if ii in M[k]: del M[k][ii]; rows[ii].discard(k)
        for ii in M[j]: rows[ii].discard(j)
        M[j]={}; alive.discard(j); steps+=1
    left=[j for j in alive if M[j]]
    return steps,[M[j] for j in left]
r2=rank_mod(cols,2); rp=rank_mod(cols,2**31-1)
steps,rest=unit_elim(cols)
cyc=E-V+comp
out=f"N={N} V={V} E={E} F={F} c={comp} E-V+1={E-V+1} cyclespace(E-V+c)={cyc}\nd1d2=0:{p3}\nrank GF2={r2} rank mod p={rp} unit-pivot Z rank={steps} leftover nonzero cols={len(rest)}\nb1 GF2={cyc-r2} b1 Q(modp)={cyc-rp} b1 Z-elim={cyc-steps}\nH1 torsion-free & zero over Z: {len(rest)==0 and steps==cyc}\n"
print(out)
with open(f"res_{N}.txt","x") as fh: fh.write(out)
