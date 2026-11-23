import math, numpy as np
L=4; K=math.log(1+math.sqrt(2))/2
# implementation A: pure loops
Z=m2=m4=0.0
for c in range(1<<16):
    s=[[1 if (c>>(4*i+j))&1 else -1 for j in range(4)] for i in range(4)]
    e=sum(s[i][j]*(s[i][(j+1)%4]+s[(i+1)%4][j]) for i in range(4) for j in range(4))
    M=sum(map(sum,s)); w=math.exp(K*e)
    Z+=w; m2+=w*M*M; m4+=w*M**4
A=(Z,m2/Z,m4/Z)
# implementation B: numpy
c=np.arange(1<<16)
s=(((c[:,None]>>np.arange(16))&1)*2-1).reshape(-1,4,4).astype(float)
e=(s*np.roll(s,-1,2)).sum((1,2))+(s*np.roll(s,-1,1)).sum((1,2))
nb=np.sum(np.abs(s*np.roll(s,-1,2))>0)+np.sum(np.abs(s*np.roll(s,-1,1))>0)
M=s.sum((1,2)); w=np.exp(K*e)
Zb=w.sum(); B=(Zb,(w*M**2).sum()/Zb,(w*M**4).sum()/Zb)
assert nb==(1<<16)*32
for a,b in zip(A,B): assert abs(a-b)<=1e-10*max(1,abs(a)),(a,b)
Z,M2,M4=B
U4=1-M4/(3*M2**2)
out=f"K={K:.15g}\nbonds=32 configs={1<<16}\nZ={Z:.10g}\n<M^2>={M2:.10g}\n<M^4>={M4:.10g}\nU4={U4:.10g}\n<M^2>/16={M2/16:.10g}\nloops-vs-numpy max rel diff={max(abs(a-b)/abs(a) for a,b in zip(A,B)):.3g}\n"
open('result.txt','x').write(out); print(out)
