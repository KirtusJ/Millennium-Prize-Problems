"""Infinite-lattice Green kernel quadrature and the harmonic defect on an ordinary torus."""
from functools import lru_cache
from itertools import combinations, product
from math import pi,prod,sqrt
import numpy as np
from scipy.special import ive,roots_legendre

PLANES=list(combinations(range(4),2))


def marks(origin,star=False):
    points=[]
    for a,b in PLANES:
        c,d=[i for i in range(4) if i not in (a,b)]
        for u,v in product(range(2),repeat=2):
            x=list(origin);x[c]+=u;x[d]+=v
            if star:x[a]+=1;x[b]+=1
            points.append((tuple(x),(c,d) if star else (a,b)))
    return points


def green_kernel(order):
    nodes,weights=roots_legendre(order)
    u=(nodes+1)/2
    @lru_cache(maxsize=None)
    def green(x):
        scale=1+sum(t*t for t in x)
        time=scale*u/(1-u)
        n=np.array(x)[:,None]
        z=2*time
        use=z>1e7
        factors=np.empty((4,len(z)))
        factors[:,~use]=ive(n,z[None,~use])
        u2=n*n/z[None,use]
        factors[:,use]=np.exp(-u2/2)/np.sqrt(2*pi*z[use])*(1+(u2*u2-6*u2+3)/(24*z[use]))
        return np.dot(weights,scale/2/(1-u)**2*np.prod(factors,axis=0))
    def second(x,i,j):
        def term(k,l):
            a=list(x);a[i]+=k;a[j]+=l
            return green(tuple(sorted(map(abs,a))))
        return term(1,-1)-term(1,0)-term(0,-1)+term(0,0)
    def kernel(p,q):
        x=tuple(i-j for i,j in zip(p[0],q[0]))
        a,b=p[1];c,d=q[1]
        return ((second(x,a,c) if b==d else 0)-(second(x,a,d) if b==c else 0)
              -(second(x,b,c) if a==d else 0)+(second(x,b,d) if a==c else 0))
    return kernel


def block(kernel,f,g):
    return np.array([[kernel(p,q) for q in g] for p in f])


def continuum(origins):
    r=[np.linalg.norm(np.subtract(origins[z],origins[(z+1)%3])) for z in range(3)]
    return sum(r[(z+1)%3]**4/(r[z]*r[(z+2)%3])**4 for z in range(3))/(6*pi*pi)


def bulk(kernel,origins):
    cubes=[marks(pt) for pt in origins]
    stars=[marks(pt,True) for pt in origins]
    xx=[block(kernel,cubes[z],cubes[(z+1)%3]) for z in range(3)]
    yy=[block(kernel,stars[z],stars[(z+1)%3]) for z in range(3)]
    sign=np.array([(-1)**(a+b-1) for _,(a,b) in cubes[0]])
    for x,y in zip(xx,yy):
        assert np.max(np.abs(y+sign[:,None]*x*sign))<1e-11*np.max(abs(x))+5e-16
    pair=[1.5*np.sum(x*x) for x in xx]
    t=.75*sum(np.dot((x*x).sum(axis=1),(xx[z-1]**2).sum(axis=0)) for z,x in enumerate(xx))
    return t/sqrt(prod(pair))


def periodic():
    shape=(6,4,4,4)
    V=prod(shape)
    k=np.meshgrid(*(2*pi*np.arange(n)/n for n in shape),indexing='ij')
    q=np.exp(1j*np.array(k))-1
    den=np.sum(abs(q)**2,axis=0)
    den.flat[0]=1
    table={}
    for a,b in PLANES:
        for c,d in PLANES:
            p=((b==d)*q[a]*q[c].conj()-(b==c)*q[a]*q[d].conj()
              -(a==d)*q[b]*q[c].conj()+(a==c)*q[b]*q[d].conj())/den
            table[(a,b),(c,d)]=np.fft.ifftn(p).real
    def kernel(p,q):
        return table[p[1],q[1]][tuple((a-b)%n for a,b,n in zip(p[0],q[0],shape))]
    cubes=[marks((t,0,0,0)) for t in (0,2,4)]
    stars=[marks((t,0,0,0),True) for t in (0,2,4)]
    sign=np.array([(-1)**(a+b-1) for _,(a,b) in cubes[0]])
    H=np.array([[float(a[1]==b[1])/V for b in cubes[0]] for a in cubes[0]])
    base=[];duals=[]
    for z in range(3):
        x=block(kernel,cubes[z],cubes[(z+1)%3])
        y=block(kernel,stars[z],stars[(z+1)%3])
        assert np.max(abs(x+H+sign[:,None]*y*sign))<2e-16
        base.append(x);duals.append(y)
    def tri(v):return 3*np.trace(v[0]@v[1]@v[2])
    defect=(tri(base)+tri(duals))/2
    expected=(tri(base)-tri([x+H for x in base]))/2
    assert abs(expected-defect)<1e-16 and abs(defect)>1e-8
    print('ordinary finite torus paired free triangle and harmonic prediction',defect,expected)


def main():
    periodic()
    lo,hi=green_kernel(90),green_kernel(150)
    for label,pattern in [('collinear',[(0,0,0,0),(1,0,0,0),(2,0,0,0)]),
                          ('skew',[(0,0,0,0),(1,0,0,0),(0,1,1,0)]),
                          ('squeezed',[(0,0,0,0),(1,0,0,0),(6,0,0,0)])]:
        for r in (2,4,8,16,32):
            pts=[tuple(r*x for x in p) for p in pattern]
            measured=bulk(hi,pts)
            pred=continuum(pts)
            assert abs(bulk(lo,pts)/measured-1)<5e-6
            print(label,r,'r^4 R1',r**4*measured,'ratio to asymptotic',measured/pred,flush=True)
        assert abs(measured/pred-1)<.02


if __name__=='__main__':main()
