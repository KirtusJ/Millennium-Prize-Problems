"""One-step SU(2) Wilson integrals on an actual cube with Gaussian control variates."""
from itertools import combinations, product

import numpy as np


def mul(a,b):
    w,v = a[:,:1],a[:,1:]
    t,u = b[:,:1],b[:,1:]
    return np.concatenate((w*t-np.sum(v*u,axis=1,keepdims=True),w*u+t*v+np.cross(v,u)),axis=1)


def inv(a):
    return a*np.array([1,-1,-1,-1])


def expq(x):
    length=np.linalg.norm(x,axis=1,keepdims=True)
    return np.concatenate((np.cos(length),x*np.sinc(length/np.pi)),axis=1)


def deficit(a):
    return np.sum(np.square(a[:,1:]),axis=1)/(1+a[:,0])


def geometry():
    # Vertices use one bit per coordinate; the anchored tree clears the highest bit.
    edges=[(x,x|(1<<j)) for x in range(8) for j in range(3) if not x&(1<<j)]
    ix={p:i for i,p in enumerate(edges)}
    paths=np.zeros((8,12))
    tree=[]
    for y in range(1,8):
        x=y^(1<<(y.bit_length()-1))
        e=ix[x,y]
        tree.append(e)
        paths[y]=paths[x]
        paths[y,e]+=1
    chords=[i for i in range(12) if i not in tree]
    c=np.array([paths[edges[e][0]]-paths[edges[e][1]]+np.eye(12)[e] for e in chords])
    faces=[]
    for i,j in combinations(range(3),2):
        for x in range(8):
            if x&((1<<i)|(1<<j)):
                continue
            y,z=x|(1<<i),x|(1<<j)
            w=y|z
            faces.append([(ix[x,y],1),(ix[y,w],1),(ix[z,w],-1),(ix[x,z],-1)])
    d=np.zeros((6,12))
    for k,face in enumerate(faces):
        for e,sign in face:
            d[k,e]=sign
    return edges,tree,chords,faces,c,d[:,chords]


def evaluate(seed,count=8192):
    edges,tree,chords,faces,c,d=geometry()
    b=c@c.T
    ev,vec=np.linalg.eigh(b)
    root=(vec*np.sqrt(ev))@vec.T
    w2,rot=np.linalg.eigh(root@d.T@d@root)
    assert np.allclose(w2,[4,4,4,6,6])
    theta=2*np.arcsinh(np.sqrt(w2)/2)
    step=np.exp(-theta)[:,None]
    rng=np.random.default_rng(seed)
    v=rng.normal(size=(count,5,3))
    vp=step*v+np.sqrt(1-step**2)*rng.normal(size=v.shape)
    width=np.sqrt(2*np.sqrt(w2*(1+w2/4)))[:,None]
    x=np.einsum('ij,njc->nic',root@rot,v/width)
    y=np.einsum('ij,njc->nic',root@rot,vp/width)
    raw=rng.normal(size=(count,12,3))
    mismatch=y-x-np.einsum('ij,njc->nic',c,raw)
    z=raw+np.einsum('ij,njc->nic',np.linalg.solve(b,c).T,mismatch)
    assert np.allclose(np.einsum('ij,njc->nic',c,z),y-x)
    ident=np.tile([1.,0.,0.,0.],(count,1))
    def basis(v):
        vectors=[np.ones(count)]
        for i,j in combinations(range(3),2):
            vectors.append(np.sum(v[:,i]*v[:,j],axis=1)/np.sqrt(3))
        for i in range(3):
            vectors.append((np.sum(v[:,i]**2,axis=1)-3)/np.sqrt(6))
        return np.stack(vectors,axis=1)
    phi,psi=basis(v),basis(vp)
    energy_xy=sum(np.sum(np.einsum('ij,njc->nic',d,coord)**2,axis=(1,2)) for coord in (x,y))/4
    energy_z=np.sum(z**2,axis=(1,2))/2
    def integrand(g):
        end_links=[]
        space=np.zeros(count)
        logj=np.zeros(count)
        valid=np.ones(count,dtype=bool)
        for coord in (x,y):
            links=[ident]*12
            angle=abs(g)*np.linalg.norm(coord,axis=2)
            valid &= np.all(angle<np.pi,axis=1)
            logj+=np.log(abs(np.sinc(angle/np.pi))).sum(axis=1)
            for i,e in enumerate(chords):
                links[e]=expq(g*coord[:,i])
            end_links.append(links)
            for face in faces:
                U=ident
                for e,sign in face:
                    U=mul(U,links[e] if sign==1 else inv(links[e]))
                space+=deficit(U)/(2*g*g)
        h=[ident]*8
        kinetic=np.zeros(count)
        for e in tree:
            a,bb=edges[e]
            angle=abs(g)*np.linalg.norm(z[:,e],axis=1)
            valid &= angle<np.pi
            V=expq(g*z[:,e])
            h[bb]=mul(h[a],V)
            kinetic+=deficit(V)/(g*g)
            logj+=2*np.log(abs(np.sinc(angle/np.pi)))
        for e in chords:
            a,bb=edges[e]
            U=mul(mul(inv(end_links[0][e]),inv(h[a])),mul(end_links[1][e],h[bb]))
            kinetic+=deficit(U)/(g*g)
        return np.where(valid,np.exp(logj+energy_xy+energy_z-space-kinetic),0)
    limit=np.diag([1.]+[np.exp(-2*theta[0])]*6)
    result=[]
    for g in (.18,.09,.045,.0225):
        delta=(integrand(g)+integrand(-g))/2-1
        matrix=limit+(phi.T*delta)@psi/count
        matrix=(matrix+matrix.T)/2
        # Common one-link normalization cancels; divide by the vacuum trial entry.
        matrix/=matrix[0,0]
        result.append(float(np.linalg.norm(matrix-limit,2)))
    assert all(a>b for a,b in zip(result,result[1:]))
    assert .2 < result[-1]/result[-2] < .3
    return result
