"""Numerical and exact controls for conditional mixing and the two spectator checks."""
from collections import Counter, defaultdict
from itertools import combinations, product
import numpy as np
from retraction import geometry, step


def score():
    nodes, weights = np.polynomial.legendre.leggauss(160)
    reference = [5.13356662,2.64938753,2.39642319,2.42504436,2.44258593,2.44904230]
    for beta, ref in zip((1,4,16,64,256,4096), reference):
        end = min(18, np.pi*np.sqrt(beta))
        theta = (nodes+1)*end/(2*np.sqrt(beta))
        s = 2*beta*np.sin(theta/2)**2
        y = 1-s/beta
        weights_y = weights*np.sin(theta)**2*np.exp(-s)
        weights_y /= weights_y.sum()
        z = 9*y/beta+7*y*y-4-y*(2*s-s*s/beta)
        ratio = np.sqrt(weights_y @ (z*z))
        np.testing.assert_allclose(ratio,ref,atol=6e-8,rtol=0)
        assert abs(weights_y@z)<3e-12
        np.testing.assert_allclose(weights_y@(-s*z),2+weights_y@(y*y),atol=3e-12)
        print(f"score beta={beta}, norm/beta={ratio:.8f}")


def spectral():
    for alpha,gamma,eta in ((.1,.5,.9),(.0001,.01,.99),(.025,.15,.75)):
        h = alpha*(eta-gamma)/(gamma*(eta-alpha))
        q = np.sqrt([h,1-h])
        p = np.array([q[1],-q[0]])
        d = np.diag([alpha,eta])
        assert np.linalg.eigvalsh(d-gamma*np.outer(q,q)).min() >= -1e-13
        np.testing.assert_allclose(p@d@p,alpha*eta/gamma)
    d = np.full((2,2),.25)
    assert d[1,1] == .25 and np.linalg.eigvalsh(d)[0] == 0
    # Colour mixtures at tensor order two: the same colour is used in both slots.
    a = np.diag([1.,.8,.1])
    rot = np.eye(3)
    rot[1:,1:] = [[.6,-.8],[.8,.6]]
    b = rot@a@rot.T
    mixed = (np.kron(a,a)+np.kron(b,b))/2
    assert not np.allclose(mixed,np.kron((a+b)/2,(a+b)/2))
    assert np.linalg.eigvalsh(mixed[1:,1:])[-1] <= np.linalg.eigvalsh(((a+b)/2)[1:,1:])[-1]+1e-12


def colours(n):
    def move(p,i):
        return tuple(v%n for v in step(p,i))
    faces={}
    assigned=defaultdict(list)
    uses=Counter()
    for p in product(range(n), repeat=3):
        for i,j in combinations(range(3),2):
            edges=((p,i),(move(p,j),i),(p,j),(move(p,i),j))
            faces[p,i,j]=edges
            key=i,j,tuple(v%2 for v in p)
            pair=edges[int(not p[j]%2)],edges[2+int(not p[i]%2)]
            assigned[key].append(pair)
            uses.update(pair)
    assert len(assigned)==24
    for p in product(range(n),repeat=3):
        for i in range(3):
            assert uses[p,i]==2*sum(v%2 for j,v in enumerate(p) if j!=i)
    for pairs in assigned.values():
        owners={e:k for k,pair in enumerate(pairs) for e in pair}
        assert len(owners)==2*len(pairs)
        for edges in faces.values():
            assert len({owners[e] for e in edges if e in owners})<=1
    return len(faces)


def mul(a,b):
    return np.r_[a[0]*b[0]-a[1:]@b[1:],
                 a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:],b[1:])]


def noncommuting_paths():
    n=6
    rng=np.random.default_rng(65285)
    field=rng.normal(size=(n,n,n,3,4))
    field/=np.linalg.norm(field,axis=-1,keepdims=True)
    def transport(p,word):
        u=np.array([1.,0.,0.,0.])
        for i in word:
            u=mul(u,field[tuple(v%n for v in p)+(i,)])
            p=step(p,i)
        return u
    for x in product(range(2),repeat=3):
        for i in range(3):
            for origin in ((0,0,0),(4,4,4)):
                p=tuple(a+b for a,b in zip(origin,x))
                a=[d for d in range(3) if p[d]%2]+[i]
                y=step(p,i)
                target=([i,i] if p[i]%2 else [])+[d for d in range(3) if y[d]%2]
                start=transport(origin,a)
                slots=0
                distances=0
                for pos,d in enumerate(target):
                    at=a.index(d,pos)
                    while at>pos:
                        middle=origin
                        for direction in a[:at-1]:
                            middle=step(middle,direction)
                        distance=np.linalg.norm(transport(middle,a[at-1:at+1])-transport(middle,a[at-1:at+1][::-1]))
                        before=transport(origin,a)
                        a[at-1],a[at]=a[at],a[at-1]
                        np.testing.assert_allclose(distance,np.linalg.norm(before-transport(origin,a)),atol=2e-14)
                        slots+=1
                        distances+=distance
                        at-=1
                assert slots<=4 and a==target
                assert np.linalg.norm(start-transport(origin,target))<=distances+1e-12


if __name__=="__main__":
    spectral()
    score()
    noncommuting_paths()
    counts=[colours(n) for n in (6,8,10,12,16)]
    print("spatial faces",counts,"total",sum(counts))
    assert all(geometry(n)[:2]==(4,4) for n in (2,6,8,10))
    print("All controls passed.")
