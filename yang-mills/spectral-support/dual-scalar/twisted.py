"""Fixed-volume SU(2) weak coupling on a torus twisted in the two spatial directions 1,2."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import lcm
from pathlib import Path
import sys
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scalar-response'))
import numpy as np
from response import inverse_jets, parity


def geometry(shape,reverse=False):
    dimension=len(shape)
    twist_axes=(1,2) if dimension==4 else (0,1)
    sites=list(product(*(range(n) for n in shape)))
    def next_site(x,a,step=1):
        return x[:a]+((x[a]+step)%shape[a],)+x[a+1:]
    tree=set()
    for x in sites[1:]:
        dirs=[i for i,v in enumerate(x) if v]
        a=dirs[-1] if reverse else dirs[0]
        tree.add((next_site(x,a,-1),a))
    edges=[(x,a) for x in sites for a in range(dimension) if (x,a) not in tree]
    idx={e:i for i,e in enumerate(edges)}
    distinguished=[idx[(tuple(shape[d]-1 if d==a else 0 for d in range(dimension)),a)] for a in twist_axes]
    first,second=distinguished[::-1] if reverse else distinguished
    axis=int(reverse)
    active=np.ones((3,len(edges)),dtype=bool)
    active[:,first]=False
    active[axis,first]=True
    active[axis,second]=False
    density=np.ones(len(edges),dtype=int)
    density[first],density[second]=3,2  # coefficients in units of 1/3
    faces,words=[],[]
    for x in sites:
        for a,b in combinations(range(dimension),2):
            path=[(x,a,1),(next_site(x,a),b,1),(next_site(x,b),a,-1),(x,b,-1)]
            prefix=np.ones(3,dtype=int)
            word=[]
            for y,d,sgn in path:
                adj=np.ones(3,dtype=int)
                if d in twist_axes and y[d]==shape[d]-1:
                    adj[:]=-1
                    adj[twist_axes.index(d)]=1
                if sgn<0: prefix*=adj
                if (y,d) in idx:
                    word.append((idx[y,d],tuple(map(int,sgn*prefix))))
                if sgn>0: prefix*=adj
            assert np.all(prefix==1)
            faces.append((x,a,b));words.append(word)
    B=np.zeros((3,len(faces),len(edges)),dtype=int)
    for p,word in enumerate(words):
        for e,s in word:
            B[:,p,e]+=s
    return faces,words,B,active,density


def sources(shape,faces,origins,dual):
    index={face:i for i,face in enumerate(faces)}
    out=np.zeros((len(origins),len(faces)),dtype=int)
    for o,origin in enumerate(origins):
        for a,b in combinations(range(4),2):
            c,d=[i for i in range(4) if i not in (a,b)]
            for u,v in product(range(2),repeat=2):
                y=list(origin);y[c]+=u;y[d]+=v
                if dual:
                    y[a]+=1;y[b]+=1
                y=tuple(z%n for z,n in zip(y,shape))
                out[o,index[(y,c,d) if dual else (y,a,b)]]+=1
    return out


def jets_mul(x,y,mod):
    rows=[]
    for mask in range(8):
        value=x[mask]*y[0]
        sub=mask
        while sub:
            sub=(sub-1)&mask
            value=value+x[sub]*y[mask^sub]
        rows.append(value%mod if mod else value)
    return np.stack(rows) if mod else np.array(rows,dtype=object)


def modular_inverse(a,p):
    n=len(a)
    m=np.concatenate((a%p,np.eye(n,dtype=int)),axis=1)
    for i in range(n):
        piv=np.flatnonzero(m[i:,i])
        if not len(piv): raise ValueError('bad prime for tangent Hessian')
        j=i+piv[0]
        m[[i,j]]=m[[j,i]]
        m[i]=m[i]*pow(int(m[i,i]),-1,p)%p
        col=m[:,i].copy();col[i]=0
        m=(m-col[:,None]*m[i])%p
    return m[:,n:]


def covariances(B,active,f,mod):
    count=B.shape[2]
    dtype=int if mod else object
    cores=[];den=1
    pairs=[0]*3;triangle=0
    for a in range(3):
        b=B[a][:,active[a]]
        if mod:
            di=1
            q=modular_inverse(b.T@b,mod)
            steps=[(q@(b.T@(w[:,None]*b)))%mod for w in f]
            local=[q]
            for mask in range(1,8):
                local.append(-sum(steps[i]@local[mask^(1<<i)] for i in range(3) if mask&(1<<i))%mod)
        else:
            di,local,steps=inverse_jets(b,f)
        for k,(i,j) in enumerate(combinations(range(3),2)):
            tr=int(np.sum(steps[i]*steps[j].T))
            pairs[k]+=(tr*pow(2,-1,mod))%mod if mod else F(tr,2*di**2)
        pair_matrix=steps[0]@steps[1]
        if mod: pair_matrix%=mod
        tr=int(np.sum(pair_matrix*steps[2].T))
        triangle+=tr%mod if mod else F(tr,di**3)
        cores.append((di,local))
        den=lcm(di,den)
    C=np.zeros((3,8,count,count),dtype=dtype)
    for a,(di,local) in enumerate(cores):
        indices=np.flatnonzero(active[a])
        for m,row in enumerate(local):
            C[a,m][np.ix_(indices,indices)]=row*(den//di)**(1+m.bit_count())
    return den,C,pairs,triangle


def expansion_terms(words):
    fourth=[]
    triples=defaultdict(lambda:defaultdict(int))
    for p,w in enumerate(words):
        def dot_pair(scale,i,j,k,l):
            fourth.append((p,scale,w[i],w[j],w[k],w[l]))
        for i in range(len(w)): dot_pair(1,i,i,i,i)
        for i,j in combinations(range(len(w)),2):
            dot_pair(6,i,i,j,j);dot_pair(4,i,j,i,i);dot_pair(4,i,j,j,j)
            for k in range(len(w)):
                if k not in (i,j):dot_pair(12,i,j,k,k)
        if len(w)==4:
            dot_pair(24,0,1,2,3);dot_pair(-24,0,2,1,3);dot_pair(24,0,3,1,2)
        for triple in combinations(w,3):
            for perm in permutations(range(3)):
                key=tuple(triple[j][0] for j in perm)
                sign=parity(perm)
                for color,j in enumerate(perm):sign*=triple[j][1][color]
                triples[key][p]+=sign
    return fourth,triples


def evaluate(shape,origins,dual,reverse=False,mod=None):
    faces,words,B,active,density=geometry(shape,reverse)
    f=sources(shape,faces,origins,dual)
    assert np.all(f.sum(axis=1)==24) and np.all((f>0).sum(axis=0)<=1)
    return evaluate_sources((faces,words,B,active,density),f,mod)


def evaluate_sources(geo,f,mod=None):
    faces,words,B,active,density=geo
    den,C,pairs,triangle=covariances(B,active,f,mod)
    dtype=int if mod else object
    W=np.zeros((8,len(faces)),dtype=dtype);W[0]=1
    for i,row in enumerate(f):W[1<<i]=den*row.astype(dtype)
    def mul(a,b):return jets_mul(a,b,mod)
    haar=-8*den**2*(np.diagonal(C,axis1=2,axis2=3)@density).sum(axis=0)
    fourth,triples=expansion_terms(words)
    p=np.array([v[0] for v in fourth]);coef=np.array([v[1] for v in fourth])
    e=np.array([[x[0] for x in v[2:]] for v in fourth]).T
    s=np.array([[x[1] for x in v[2:]] for v in fourth]).transpose(1,2,0)
    def link(i,j,a):
        return C[a][:,e[i],e[j]]*(s[i,a]*s[j,a])
    def direct(i,j):
        return sum(link(i,j,a) for a in range(3))
    wick=mul(direct(0,1),direct(2,3))
    for a in range(3):
        wick+=mul(link(0,2,a),link(1,3,a))+mul(link(0,3,a),link(1,2,a))
    quart=den*(mul(W[:,p],wick)@coef)
    keys=[];weights=[]
    for key,vals in triples.items():
        vec=sum(W[:,p]*v for p,v in vals.items())
        if all(active[a,key[a]] for a in range(3)) and np.any(vec):
            keys.append(key);weights.append(vec)
    keys=np.array(keys,dtype=int)
    triple_term=np.zeros(8,dtype=dtype)
    if len(keys):
        V=np.stack(weights,axis=1)
        for start in range(0,len(keys),12):
            sel=slice(start,start+12)
            factors=[C[a][:,keys[sel,a,None],keys[None,:,a]] for a in range(3)]
            triple_term+=mul(mul(V[:,sel,None],V[:,None,:]),mul(factors[0],mul(factors[1],factors[2]))).sum(axis=(1,2))
            if mod:triple_term%=mod
    abel=np.zeros(8,dtype=dtype)
    for a in range(3):
        vals=np.stack([np.sum((B[a]@row)*B[a],axis=1) for row in C[a]])
        abel+=3*den*mul(W,mul(vals,vals)).sum(axis=1)
    parts={'haar':haar,'quartic':quart,'cubic':12*triple_term,'abelian':abel}
    parts['wilson']=haar+quart+12*triple_term
    def normalize(raw,m):
        n=int(raw[m]);d=24*den**(3+m.bit_count())
        return (n*pow(d,-1,mod))%mod if mod else F(n,d)
    return dict(A0=normalize(parts['wilson'],0),V1=[normalize(parts['wilson'],m) for m in (3,5,6)],
                pairs=[v%mod if mod else v for v in pairs],
                T0=triangle%mod if mod else triangle,
                T1={k:-normalize(v,7)%mod if mod else -normalize(v,7) for k,v in parts.items()},
                count=len(keys))
