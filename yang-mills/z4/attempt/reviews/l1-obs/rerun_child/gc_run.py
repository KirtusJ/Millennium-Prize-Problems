import numpy as np, itertools, sys
def calc(N):
    N=tuple(N); n=N[0]*N[1]*N[2]
    idx=lambda x,y,z:((x%N[0])*N[1]+(y%N[1]))*N[2]+(z%N[2])
    L=lambda d,s:d*n+idx(*s)
    pl=[(i,j) for i in range(3) for j in range(i+1,3)]
    C=np.zeros((3*n,3*n)); P0=None
    for k,(i,j) in enumerate(pl):
        for x in itertools.product(*[range(m) for m in N]):
            row=k*n+idx(*x)
            xi=list(x);xi[i]+=1; xj=list(x);xj[j]+=1
            C[row,L(j,xi)]+=1; C[row,L(j,x)]-=1
            C[row,L(i,xj)]-=1; C[row,L(i,x)]+=1
            if (i,j)==(0,1) and x==(0,0,0): P0=row
    M=C.T@C
    ev,V=np.linalg.eigh(M)
    groups=[];
    for e,k in zip(ev,range(len(ev))):
        if e<=1e-9: continue
        if groups and abs(e-groups[-1][0])<1e-9: groups[-1][1].append(k)
        else: groups.append([e,[k]])
    res=[]
    for e,ks in groups:
        w=np.arccosh(1+e/2)
        a=sum((C[P0]@V[:,k])**2 for k in ks)/(2*np.sinh(w))
        res.append((w,a))
    vis=[(w,a) for w,a in res if a>1e-12]
    wm=min(w for w,a in vis)
    s=sum(a for w,a in vis if abs(w-wm)<1e-9)
    return 2*wm,1.5*s*s
def cf(f): return 2*np.arccosh(1+2*np.sin(np.pi/f)**2)
out=[]
E,W=calc((2,2,2)); out.append(f"control (2,2,2): E={E:.8f} W={W:.8f}")
ok=abs(E-3.52549435)<1e-7 and abs(W-0.046875)<1e-9
out.append("control OK" if ok else "CONTROL FAILED")
if ok:
    for N in [(5,2,3),(2,5,3),(3,2,5)]:
        E,W=calc(N)
        out.append(f"{N}: E={E:.8f} W={W:.8f} | max12={cf(max(N[:2])):.8f} maxall={cf(max(N)):.8f} min12={cf(min(N[:2])):.8f}")
open('out.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
