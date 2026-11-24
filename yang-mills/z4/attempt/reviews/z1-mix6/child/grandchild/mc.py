import numpy as np
N=400000
rng=np.random.default_rng(12345)
def haar(): 
    q=rng.standard_normal((N,4)); return q/np.linalg.norm(q,axis=1,keepdims=True)
def mul(p,q):
    a1,b1,c1,d1=p.T;a2,b2,c2,d2=q.T
    return np.stack([a1*a2-b1*b2-c1*c2-d1*d2,a1*b2+b1*a2+c1*d2-d1*c2,a1*c2-b1*d2+c1*a2+d1*b2,a1*d2+b1*c2-c1*b2+d1*a2],1)
def inv(q): return q*np.array([1,-1,-1,-1])
L={}
def X(x,y):
    if ('X',x,y) not in L: L[('X',x,y)]=haar()
    return L[('X',x,y)]
def Y(x,y):
    if ('Y',x,y) not in L: L[('Y',x,y)]=haar()
    return L[('Y',x,y)]
gs=[]
for cx,cy in [(0,0),(1,0),(0,1),(1,1)]:
    P=mul(mul(mul(X(cx,cy),Y(cx+1,cy)),inv(X(cx,cy+1))),inv(Y(cx,cy)))
    path=np.tile([1.,0,0,0],(N,1))
    for x in range(cx): path=mul(path,X(x,0))
    for y in range(cy): path=mul(path,Y(cx,y))
    gs.append(mul(mul(path,P),inv(path)))
g1=gs[0]; gbar=sum(gs)/4
f1=g1[:,1]*-1   # Re(i*g) = -b
B=np.array([0,1.,0,0]); f1=mul(np.tile(B,(N,1)),g1)[:,0]; f4=mul(np.tile(B,(N,1)),gbar)[:,0]
sp=1-(gbar**2).sum(1)
rows=[]
for name,v,ex in [("E[f1^2]",f1**2,0.25),("E[f4^2]",f4**2,1/16),("E[spread]",sp,0.75)]:
    m=v.mean(); se=v.std(ddof=1)/np.sqrt(N); rows.append((name,m,se,ex,(m-ex)/se))
# control MC
a=haar()[:,0]; ctl=(a**4).mean()
cc=np.corrcoef(np.array([g[:,1] for g in gs]))
with open('control.txt','x') as f: f.write("0.125000\n")
with open('results.md','x') as f:
    f.write("# Results\n\n## Control\nE[a^4] for Haar SU(2)=S^3: 3/(n(n+2)), n=4 -> 0.125000 (control.txt). MC check: %.6f\n\n"%ctl)
    f.write("## MC estimates (N=400000, seed 12345)\n\n|quantity|MC|SE|exact (indep Haar)|z|\n|-|-|-|-|-|\n")
    for n,m,se,ex,z in rows: f.write("|%s|%.6f|%.6f|%.6f|%.2f|\n"%(n,m,se,ex,z))
    f.write("\n## Exact derivations (g_k independent Haar)\n- f1=Re(i g1)=-b1; E[b^2]=1/4 -> E[f1^2]=1/4.\n- f4=-mean of 4 indep b's: Var=(1/16)*4*(1/4)=1/16.\n- E|gbar|^2=(1/16)(4*1+cross terms 0)=1/4 -> E[spread]=3/4.\n\n")
    ok=all(abs(r[4])<3 for r in rows)
    f.write("## Agreement\nMC agrees with the independent-Haar values within 3 sigma: %s\n"%("YES" if ok else "NO"))
    f.write("\nCorrelation of b-components of g1..g4 (diagnostic):\n```\n%s\n```\n"%np.round(cc,4))
print(open('results.md').read())
