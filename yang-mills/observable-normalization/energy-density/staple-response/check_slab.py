"""Deterministic Haar integration of a temporal link with noncommuting boundaries."""

import numpy as np
from scipy.special import ive, roots_chebyu, roots_legendre


def adj(q):
    return q * np.array([1.,-1.,-1.,-1.])


def mul(a,b):
    return np.r_[a[0]*b[0]-a[1:]@b[1:],
                 a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:],b[1:])]


def cube(seed=21664):
    rng=np.random.default_rng(seed)
    q=rng.normal(size=(27,7,4))
    q/=np.linalg.norm(q,axis=-1,keepdims=True)
    return q[:,:3],q[:,3:6],q[:,6]


def paths(x,y,h):
    result=[]
    for j in range(3):
        fwd=3**j
        prev=2*fwd
        result.extend([mul(mul(x[0,j],h[fwd]),adj(y[0,j])),
                       mul(mul(adj(x[prev,j]),h[prev]),y[prev,j])])
    return np.array(result)


def sphere():
    # Haar on S^3, fixed polar axis unrelated to the random link staple.
    z,wz=roots_chebyu(34)
    c,wc=roots_legendre(32)
    phi=2*np.pi*np.arange(64)/64
    z,c,phi=np.broadcast_arrays(z[:,None,None],c[None,:,None],phi[None,None,:])
    r=np.sqrt(1-z*z)
    q=np.stack([z,r*c,r*np.sqrt(1-c*c)*np.cos(phi),r*np.sqrt(1-c*c)*np.sin(phi)],axis=-1)
    w=np.broadcast_to(wz[:,None,None]*wc[None,:,None]/(np.pi*64),z.shape)
    return q.reshape(-1,4),w.ravel()


def main():
    x,y,h=cube()
    p=paths(x,y,h)
    rev=paths(y,x,adj(h))
    assert np.max(abs(rev-adj(p)))<5e-15
    wrong=paths(y,x,h)
    assert np.max(abs(wrong-adj(p)))>.2
    q,w=sphere()
    assert abs(w.sum()-1)<1e-13
    traces=q@p.T
    for beta in (.35,2.,5.):
        force=beta*p.sum(axis=0)
        R=np.linalg.norm(force)
        m=ive(2,R)/ive(1,R)
        # Integrate the unmodified product of the six plaquette Boltzmann factors.
        raw=w*np.prod(np.exp(beta*traces),axis=1)
        raw/=raw.sum()
        action=beta*(6-traces.sum(axis=1))
        W=action-(6*beta-R*m)
        v=R*R*(1-m*m-3*m/R)
        err=max(abs(raw@W),abs(raw@(W*W)-v))
        assert err<8e-12
        reversed_W=R*m-adj(q)@(beta*rev.sum(axis=0))
        assert np.max(abs(W-reversed_W))<2e-14
        print("beta, actual staple norm, boundary kernel residual", beta, R, err)


if __name__=="__main__":
    main()
