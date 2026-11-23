import numpy as np, math
L=2
def lk(x,y,z,d): return (((x%L)*L+(y%L))*L+(z%L))*3+d
planes=[]; stack=[]
for x in range(L):
 for y in range(L):
  for z in range(L):
   for (d,e) in [(0,1),(0,2),(1,2)]:
    o=[0,0,0]; p=[0,0,0]; q=[0,0,0]
    p[d]=1; q[e]=1
    pl=[lk(x,y,z,d),lk(x+p[0],y+p[1],z+p[2],e),lk(x+q[0],y+q[1],z+q[2],d),lk(x,y,z,e)]
    planes.append(pl)
    if (d,e)==(0,1) and x==0 and y==0: stack.append(len(planes)-1)
assert len(planes)==24 and len(stack)==2
N=1<<24; CH=1<<20
hist={}
for st in range(0,N,CH):
    c=np.arange(st,st+CH,dtype=np.int32)
    bits=[(c>>i)&1 for i in range(24)]
    sg=[1-2*(a^b^cc^d) for a,b,cc,d in [(bits[i],bits[j],bits[k],bits[l]) for i,j,k,l in planes]]
    T=sum(sg[i] for i in stack); S=sum(sg)-T
    key=(S+24)*8+(T+2)
    for k,v in zip(*np.unique(key,return_counts=True)):
        hist[int(k)]=hist.get(int(k),0)+int(v)
assert sum(hist.values())==N
def lnZ(beta,s):
    w=beta*(1-2*s)
    return math.log(sum(n*math.exp(beta*(k//8-24)+w*(k%8-2)) for k,n in hist.items()))
def avgT(beta,s):
    w=beta*(1-2*s); z=0;t=0
    for k,n in hist.items():
        e=n*math.exp(beta*(k//8-24)+w*(k%8-2)); z+=e; t+=e*(k%8-2)
    return t/z
xs,ws=np.polynomial.legendre.leggauss(8); xs=(xs+1)/2; ws=ws/2
out=[]
for beta in (0.3,0.6):
    Fd=-(lnZ(beta,1)-lnZ(beta,0))
    Fq=2*beta*sum(w*avgT(beta,s) for s,w in zip(xs,ws))
    out.append(f"beta={beta}: F_direct={Fd:.10f} F_quadrature={Fq:.10f} diff={Fd-Fq:.3e}")
with open('results.md','x') as f:
    f.write("# 3D L=2 Z2 gauge, twist on stack x1=x2=0 (2 plaquettes in (1,2) plane)\n\n"+"\n\n".join(out)+"\n\nControl: see control.txt\n")
print("\n".join(out))
