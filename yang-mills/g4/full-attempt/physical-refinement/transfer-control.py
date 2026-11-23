"""Exact orbit enumeration on a two-dimensional spatial Z2 Wilson grid, floating eigensolver."""
from itertools import product
import numpy as np

def check(beta):
    n=2
    edges=[(x,((x%2+1)%2+2*(x//2)) if d==0 else (x+2)%4) for x in range(4) for d in range(2)]
    frames=np.array([[h[i]*h[j] for i,j in edges] for h in product((-1,1),repeat=4)])
    all_links=list(product((-1,1),repeat=len(edges)))
    reps=sorted({min(tuple(row) for row in frames*x) for x in all_links})
    links=np.asarray(reps)
    orbit={tuple(row):i for i,x in enumerate(links) for row in frames*x}
    k=np.exp(beta*((links[:,None,:]*frames[None,:,:])@links.T)).mean(axis=1)
    upper=np.cosh(4*beta)**(len(edges)/4)
    assert k.min()>=1-1e-13 and k.max()<upper
    faces=[[2*x,2*edges[2*x][1]+1,2*edges[2*x+1][1],2*x+1] for x in range(4)]
    w=np.exp(.5*beta*sum(np.prod(links[:,p],axis=1) for p in faces))
    transfer=w[:,None]*k*w
    flips=[np.array([(-1 if d==mu and (x//(2**mu))%2==0 else 1)
                     for x in range(4) for d in range(2)]) for mu in range(2)]
    classes=sorted({tuple(sorted({orbit[tuple(x*h)] for h in (np.ones(8),*flips,flips[0]*flips[1])})) for x in links})
    basis=np.zeros((len(links),len(classes)))
    for j,c in enumerate(classes):basis[list(c),j]=len(c)**-.5
    ev=np.linalg.eigvalsh(basis.T@transfer@basis)
    assert np.all(ev>0) and abs(ev[-1]-np.linalg.eigvalsh(transfer)[-1])<1e-9*ev[-1]
    ratio=ev[-2]/ev[-1]
    assert 0<ratio<1-1/upper
    return ratio,1-1/upper

if __name__=="__main__":
    for beta in (.25,.6,1.5):
        print(beta,*(f"{x:.10f}" for x in check(beta)))
