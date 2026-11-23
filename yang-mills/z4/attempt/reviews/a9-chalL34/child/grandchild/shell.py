"""Predicates (stated before first run):
P1: V = 3^4 - 1 = 80 (sites with max|x_i|=1 in Z^4) -- checked by enumeration vs formula.
P2: control Z^3 count 26 (done, control.txt).
P3: every plaquette's 4 boundary links are in E (all corners in shell => edges in shell).
P4: b1 = (E-V+c) - r, r = GF(2) rank of boundary map; b1 >= 0 and r <= F.
Rerun: python3 shell.py   (writes result_raw.txt with mode 'x'; remove nothing, use new name if exists)
"""
import itertools, sys
R=range(-2,3)
S={x for x in itertools.product(R,repeat=4) if max(map(abs,x))==1}
def add(x,m,d=1): y=list(x); y[m]+=d; return tuple(y)
E=set()
for x in S:
    for m in range(4):
        y=add(x,m)
        if y in S: E.add((x,y))
idx={e:i for i,e in enumerate(sorted(E))}
rows=[]
for x in S:
    for m in range(4):
        for n in range(m+1,4):
            c=[x,add(x,m),add(add(x,m),n),add(x,n)]
            if all(p in S for p in c):
                es=[(x,add(x,m)),(add(x,n),add(add(x,n),m)),(x,add(x,n)),(add(x,m),add(add(x,m),n))]
                assert all(e in idx for e in es)  # P3
                rows.append(sum(1<<idx[e] for e in es))
F=len(rows)
par={x:x for x in S}
def f(a):
    while par[a]!=a: par[a]=par[par[a]]; a=par[a]
    return a
for a,b in E: par[f(a)]=f(b)
c=len({f(x) for x in S})
basis={}
r=0
for v in rows:
    while v:
        h=v.bit_length()-1
        if h in basis: v^=basis[h]
        else: basis[h]=v; r+=1; break
b1=len(E)-len(S)+c-r
out=f"V={len(S)} E={len(E)} F={F} c={c} r={r} b1={b1}\nP1 {'ok' if len(S)==80 else 'FAIL'}\nP4 {'ok' if b1>=0 and r<=F else 'FAIL'}\n"
print(out)
open('result_raw.txt','x').write(out)
