"""Check the quartic symbol against independent real-space incidence and exact jets."""
from itertools import combinations, product

import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix


def exact():
    z, theta = sp.symbols("z theta")
    u = z/4*(1-z**2/24+z**4/384)
    ratio = (1-z**2/24+z**4/384)**4
    series = sp.series(ratio*(1-2*u**2+(2+theta)*u**4),z,0,6).removeO()
    expected = 1-7*z**2/24+z**4*(sp.Rational(23,384)+theta/256)
    assert sp.expand(series-expected)==0
    # Repeated upper root and a lower eigenvalue saturate the two zero orders.
    roots = [expected.subs(theta,k) for k in (-3,-3,6)]
    for x,order in ((2*z**2,14),(roots[2]+z**6,14),(roots[0]-z**6,16)):
        factors = [x]*7+[x-b for b in roots]
        actual = sum(min(m[0] for m,c in sp.Poly(p,z).terms() if c) for p in factors)
        assert actual == order
    # Cubic sign and normalization test for the matched moments.
    a,h = sp.symbols("a h")
    def moment(m,w,j):
        return 1-m+m*((1+w)**j+(1-w)**j)/2
    for j in range(4):
        assert sp.expand(moment(a,h/2,j)-moment(a/16,2*h,j))==0


def projector_controls():
    from fractions import Fraction as F
    from math import comb
    a,b = F(1,100),F(1,1000)
    for r in range(1,8):
        D=3*r-1
        for x in [F(0),a/2,a,1-b,1-b/2,F(1),1+b/2,1+b]:
            reading=sum(comb(D,j)*x**j*(1-x)**(D-j) for j in range(2*r,D+1))
            exact=int(x>F(1,2))
            bound=(8*max(a*a,(1+b)**2*b))**r
            assert abs(reading-exact)<=bound
    # Two laws indistinguishable through lag three, including total mass.
    w,alpha=F(1,8),F(3,5)
    def law(m,d):
        return {F(1):1-m,1-d:m/2,1+d:m/2}
    low,wide=law(alpha,w/2),law(alpha/16,2*w)
    for j in range(4):
        assert sum(m*x**j for x,m in low.items())==sum(m*x**j for x,m in wide.items())
    assert sum(m for x,m in low.items() if abs(x-1)<=w)-sum(
        m for x,m in wide.items() if abs(x-1)<=w)==alpha/16


def graph(L):
    pts = list(product(range(L),repeat=3))
    idx = {p:n for n,p in enumerate(pts)}
    def shift(p,i):
        return tuple((c+int(j==i))%L for j,c in enumerate(p))
    faces, cubes = [], []
    for p in pts:
        for i,j in combinations(range(3),2):
            k = 3-i-j
            f = 3*idx[p]+k
            for q,g in ((p,i),(p,j),(shift(p,i),j),(shift(p,j),i)):
                faces.append((3*idx[q]+g,f))
            # A face of normal k bounds the cube starting at p and its predecessor.
            prev = tuple((v-int(jj==k))%L for jj,v in enumerate(p))
            cubes.extend([(idx[p],f),(idx[prev],f)])
    def mat(entries,n):
        row,col=zip(*entries)
        return coo_matrix((np.ones(len(row)),(row,col)),shape=(n,3*L**3)).tocsr()
    e,c=mat(faces,3*L**3),mat(cubes,L**3)
    # B = A_edge + A_cube + (12-4/3)I; incidence diagonals sum to six.
    def apply(x):
        return e.T@(e@x)+c.T@(c@x)+(14/3)*x
    assert np.allclose(apply(np.ones(3*L**3)),98/3)
    for mode in ((0,0,0),(1,0,0),(1,2,3),(L//2,L//2,0)):
        k = np.array(mode)*(2*np.pi/L)
        M = np.empty((3,3),dtype=complex)
        phases = np.array([np.exp(1j*(np.array(pts)@k+(sum(k)-k[i])/2)) for i in range(3)]).T
        for i in range(3):
            p = np.zeros((L**3,3),dtype=complex)
            p[:,i] = phases[:,i]
            out = apply(p.ravel()).reshape(-1,3)/phases
            M[:,i] = out[0]
            assert np.max(np.abs(out-out[0])) < 1e-12
        t = 2*np.cos(k/2)
        b = (50/3-4*sum(np.sin(k/2)**2))*np.eye(3)+2*(np.outer(t,t)-np.diag(t*t))
        assert np.max(abs(b-M))<1e-12
        print("side",L,"mode",mode,"quartic eigenvalues",np.linalg.eigvalsh(b))


def binary_transfer():
    # Exact physical basis on two adjacent Z2 squares, evaluated at high precision.
    import mpmath as mp
    mp.mp.dps=90
    states=list(product((1,-1),repeat=2))
    for inv in (16,32,64,128):
        beta=mp.mpf(1)/inv
        u=mp.tanh(beta)
        rows=[]
        for a,b in states:
            row=[]
            for c,d in states:
                kinetic=1+(a*c+b*d)*u**4+a*b*c*d*u**6
                row.append(mp.exp(beta*(a+b+c+d)/2)*kinetic/4)
            rows.append(row)
        eig=mp.eigsy(mp.matrix(rows),eigvals_only=True)
        x=[eig[i]/(eig[3]*beta**4) for i in range(3)]
        center=1-7*beta**2/3
        assert abs(x[0]/beta**2-1)<8*beta**2
        assert max(abs(v-center) for v in x[1:])<8*beta**4
        filtered=max(abs(v*v*(v-center)) for v in x)
        print("binary inverse beta",inv,"lower/beta^2",float(x[0]/beta**2),
              "max polynomial/beta^4",float(filtered/beta**4))


if __name__ == "__main__":
    exact()
    projector_controls()
    graph(8)
    graph(10)
    binary_transfer()
