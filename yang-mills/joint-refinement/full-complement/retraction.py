"""Integral cubical chain homotopy from fine to straight spacing-two currents."""
from collections import Counter
from itertools import combinations, product
import numpy as np


def step(x, i):
    return tuple(v+(d==i) for d,v in enumerate(x))


def walk(x, word):
    for i in word:
        x=step(x,i)
    return x


def surface(x,i):
    root=tuple(v-v%2 for v in x)
    y=step(x,i)
    word=[d for d in range(3) if x[d]%2]+[i]
    target=([i,i] if x[i]%2 else [])+[d for d in range(3) if y[d]%2]
    faces=Counter()
    for pos,d in enumerate(target):
        at=word.index(d,pos)
        while at>pos:
            j=word[at-1]
            corner=walk(root,word[:at-1])
            faces[corner,min(d,j),max(d,j)]+=1 if j<d else -1
            word[at-1],word[at]=word[at],word[at-1]
            at-=1
    assert word==target
    return +faces, -faces


def edges(x,word):
    values=Counter()
    for i in word:
        values[x,i]+=1
        x=step(x,i)
    return values


def geometry(n):
    rows=Counter()
    col_max=0
    for x in product(range(n),repeat=3):
        root=tuple(v-v%2 for v in x)
        for i in range(3):
            pos,neg=surface(x,i)
            col=sum(pos.values())+sum(neg.values())
            col_max=max(col_max,col)
            skeleton=all(v%2==0 for j,v in enumerate(x) if j!=i)
            assert not(skeleton and col)
            actual=Counter()
            for sign,faces in ((1,pos),(-1,neg)):
                for (z,a,b),size in faces.items():
                    wrapped=tuple(v%n for v in z)
                    rows[wrapped,a,b]+=size
                    for start,d,t in [(z,a,1),(step(z,a),b,1),(step(z,b),a,-1),(z,b,-1)]:
                        actual[start,d]+=sign*t*size
            expected=edges(root,[d for d in range(3) if x[d]%2]+[i])
            y=step(x,i)
            expected.subtract(edges(root,([i,i] if x[i]%2 else [])+[d for d in range(3) if y[d]%2]))
            assert actual==expected
    return col_max,max(rows.values()),sorted(set(rows.values()))


if __name__=="__main__":
    for n in (2,6,8,10,16):
        print(n,geometry(n))
