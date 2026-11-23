import numpy as np, itertools
T=np.diag([2.]*3)-np.diag([1.]*2,1)-np.diag([1.]*2,-1)
c=np.linalg.eigvalsh(T)[0]
open('control.txt','w').write("%.9f\n"%c)
links=[(m,s) for m in range(4) for s in (1,-1)]
unk=[l for l in links if l!=(0,1)]
idx={l:i for i,l in enumerate(unk)}
rows=[];keys=[]
for m in range(4):
  for n in range(m+1,4):
    for s in (1,-1):
      for t in (1,-1):
        r=np.zeros(7)
        if (m,s) in idx:r[idx[(m,s)]]+=1
        if (n,t) in idx:r[idx[(n,t)]]-=1
        rows.append(r);keys.append((m,n,s,t))
D=np.array(rows);Q=D.T@D
lam=np.linalg.eigvalsh(Q)[0]
H=D@np.linalg.inv(Q)@D.T
k=keys.index((1,2,1,1))
out="control %.9f\nlambda %.9f\nC_pp %.9f\ntrace %.9f\n"%(c,lam,H[k,k],np.trace(H))
open('result.txt','w').write(out);print(out)
open('notes.md','w').write("prog.py: numpy only. D is 24x7 (pinned link 0->+e0 dropped), Q=D^T D, C=D Q^-1 D^T. Results in result.txt.\n")
