"""Exact incidence/energy budgets, isolated SU(2) rotor, SU(3) phase and Wilson seam controls."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product, combinations
from math import ceil
import numpy as np
from scipy.linalg import eigh_tridiagonal


def census(side):
    masks = defaultdict(set)
    for x in product(range(side), repeat=3):
        def step(i):
            return tuple((z+(j==i)) % side for j,z in enumerate(x))
        for i, j in combinations(range(3), 2):
            for e in ((x,i), (step(i),j), (step(j),i), (x,j)):
                masks[e].add((x,i,j))
    assert all(len(s)==4 for s in masks.values())
    assert len({frozenset(s) for s in masks.values()})==3*side**3
    zero=(0,0,0)
    star={(zero,i) for i in range(3)}
    star.update((tuple((side-1 if k==i else 0) for k in range(3)),i) for i in range(3))
    total=set()
    for e in star:
        total.symmetric_difference_update(masks[e])
    assert not total
    return len(masks)


def rank_control(k):
    eps2 = 2*(F(17*1024,8)+F(3,16))/2**20
    keep = 1-16*eps2
    rank = k*keep**2/(1+(k-1)*eps2)
    return float(keep), ceil(rank)


def rotor(g, cutoff):
    n=np.arange(cutoff)
    eig, basis=eigh_tridiagonal(n*(n+2.)+g,np.full(cutoff-1,-g/2))
    omega=basis[:,0]
    shifted=(-1.)**n*omega
    overlaps=basis.T @ shifted
    e=(eig-eig[0])/(2*g)
    weights=overlaps**2
    xomega=np.zeros(cutoff)
    xomega[1:]+=omega[:-1]/2
    xomega[:-1]+=omega[1:]/2
    u=1-omega @ xomega
    measured=np.sum(weights*(e-1)**2)
    assert abs(e @ weights-(1-u)) < 2e-10
    assert abs(measured-np.linalg.norm(omega-xomega)**2) < 2e-10
    assert measured <= 2*u+1e-12
    assert abs(weights.sum()-1)<1e-12
    return u, measured, weights[abs(e-1)<.25].sum(), np.exp(-e)@weights


def low_space():
    g=65536.
    n=np.arange(160)
    eig, basis=eigh_tridiagonal(n*(n+2.)+g,np.full(len(n)-1,-g/2))
    en=eig-eig[0]
    E=g/20
    sub=basis[:,en <= E]
    coefficients=basis.T @ (((-1.)**n)[:,None]*sub)
    residual=np.linalg.norm(((en/(2*g)-1)[:,None])*coefficients, 2)
    bound=E/(2*g)+np.sqrt(2*(eig[0]+E)/g)
    assert residual <= bound
    inside=abs(en/(2*g)-1)<.5
    least=np.linalg.svd(coefficients[inside,:],compute_uv=False)[-1]**2
    assert least >= 1-4*bound**2-1e-12
    return len(sub.T), residual, bound, least


def su3():
    rng=np.random.default_rng(20261123)
    z=np.exp(2j*np.pi/3)
    max_error=0.
    for _ in range(120):
        links=[]
        for _ in range(4):
            u,r=np.linalg.qr(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
            u=u @ np.diag(np.diag(r)/abs(np.diag(r)))
            u[:,0]/=np.linalg.det(u)
            links.append(u)
        shifts=rng.integers(0,3,4)
        phase=z**int(shifts[0]+shifts[1]-shifts[2]-shifts[3])
        def tr(a):
            return np.trace(a[0]@a[1]@a[2].conj().T@a[3].conj().T)/3
        before=tr(links)
        after=tr([u*z**int(s) for u,s in zip(links,shifts)])
        max_error=max(max_error,abs(after-phase*before))
        defect=before.real-after.real
        assert abs(defect-(1-phase.real)) <= abs(1-phase)*abs(before-1)+1e-13
        assert abs(before-1)**2 <= 2*(1-before.real)+1e-13
    assert max_error<1e-13
    return max_error


def seam():
    # Integrate four temporal gauge links independently on each transition.
    states=list(product((-1,1), repeat=4))
    index={x:i for i,x in enumerate(states)}
    flux=np.prod(states,axis=1)
    half=np.exp(.47*(flux-1)/2)
    T=np.zeros((16,16))
    observed=np.zeros_like(T)
    bad=np.zeros_like(T)
    shift=np.eye(16)[[index[(-x[0],*x[1:])] for x in states]]
    for i,x in enumerate(states):
        for j,y in enumerate(states):
            for h in states:
                plaquettes=np.array([x[e]*h[(e+1)%4]*y[e]*h[e] for e in range(4)])
                weight=half[i]*half[j]*np.exp(.71*plaquettes.sum())/16
                temporal=np.exp(-2*.71*plaquettes[0])
                T[i,j]+=weight
                bad[i,j]+=weight*temporal
                observed[i,j]+=weight*temporal*np.exp(-.47*flux[i])
    mismatch=np.max(abs(bad-shift@T))
    assert np.max(abs(observed-shift@T))<1e-12 and mismatch>.1
    leading, basis=np.linalg.eigh(T)
    norm=leading[-1]
    T/=norm
    observed/=norm
    omega=basis[:,-1]
    v=shift@omega
    for n in (1,2,5):
        read=omega @ observed @ np.linalg.matrix_power(T,n-1) @ observed @ omega
        assert abs(read-v @ np.linalg.matrix_power(T,n) @ v)<1e-12
    return mismatch


if __name__ == "__main__":
    for side in (3,4,5):
        count=census(side)
        print("side, distinct curvatures, band fraction and rank floor", side,count,*rank_control(count))
    for g in (1.,16.,256.,4096.,65536.):
        base=rotor(g,128)
        refined=rotor(g,192)
        assert np.max(np.abs(np.array(base)-refined))<1e-8
        print("isolated square g, deficit, relative residual², band mass, unit-time reading",g,*refined)
    print("square low-space dimension, residual, ceiling, least projected weight",*low_space())
    print("SU(3) largest phase discrepancy",su3())
    print("binary Wilson seam wrong-half maximum kernel error",seam())
