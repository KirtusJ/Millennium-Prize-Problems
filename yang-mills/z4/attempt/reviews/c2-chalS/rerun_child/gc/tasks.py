import numpy as np, itertools
from collections import deque
# A
rows=[]
for i in range(4):
    for j in range(i+1,4):
        M=np.zeros((4,4));M[i,j]=1;M[j,i]=-1;rows.append(M.flatten())
rA=np.linalg.matrix_rank(np.array(rows))
# B
gens=[]
for p in itertools.permutations(range(4)):
    for s in itertools.product([1,-1],repeat=4):
        M=[[0]*4 for _ in range(4)]
        for i in range(4): M[i][p[i]]=s[i]
        gens.append(tuple(map(tuple,M)))
R=((0,-1,0,0),(1,0,0,0),(0,0,1,0),(0,0,0,1))
gens.append(R)
def mul(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)) for i in range(4))
I=tuple(tuple(int(i==j) for j in range(4)) for i in range(4))
seen={I};q=deque([I])
while q:
    x=q.popleft()
    for g in gens:
        y=mul(x,g)
        if y not in seen: seen.add(y);q.append(y)
sB=len(seen)
# contrast
c,s=np.cos(1),np.sin(1)
Rf=np.eye(4);Rf[:2,:2]=[[c,-s],[s,c]]
G=[np.array(g,float) for g in gens[:-1]]+[Rf]
key=lambda m:tuple(np.round(m,9).flatten()+0.0)
seen2={key(np.eye(4))};q=deque([np.eye(4)]);cap=20000
while q and len(seen2)<=cap:
    x=q.popleft()
    for g in G:
        y=x@g;k=key(y)
        if k not in seen2: seen2.add(k);q.append(y)
sC=len(seen2)
out=f"A rank={rA} {'met' if rA==6 else 'failed'}\nB size={sB} {'met' if sB==384 else 'failed'}\nC size>{cap}: reached {sC} {'met' if sC>cap else 'failed'}\n"
print(out)
with open("results.txt","x") as f: f.write(out)
with open("notes.md","a") as f: f.write("\n## run\n"+out+"Rerun: cd grandchild && python3 control.py && python3 tasks.py (delete results.txt/control.txt first)\nCaveat: rounding at 1e-9 via np.round(9) keys, not true tolerance clustering.\n")
