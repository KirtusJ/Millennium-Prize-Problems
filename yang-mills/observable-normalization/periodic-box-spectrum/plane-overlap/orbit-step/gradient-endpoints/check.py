"""Exact quaternion links, linear slice projection, and pinned Haar integration."""
import importlib.util
from itertools import product
from pathlib import Path

import numpy as np
from scipy.special import logsumexp, ndtri
from scipy.stats import qmc

parent = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("triad",parent/"constant-triads/check.py")
triad = importlib.util.module_from_spec(spec)
spec.loader.exec_module(triad)
axial = triad.axial
mul = axial.multiply


def inv(q):
    return q*np.array([1,-1,-1,-1])


def expq(v):
    r = np.linalg.norm(v,axis=-1)
    return np.concatenate([np.cos(r)[...,None],v*np.sinc(r[...,None]/np.pi)],axis=-1)


def area(phi,data):
    starts,ends,_,_ = data
    field = np.cross(phi[starts],phi[ends])
    D = np.eye(len(phi))[ends,1:]-np.eye(len(phi))[starts,1:]
    return field-D@np.linalg.lstsq(D,field,rcond=None)[0]


def endpoints(phi,eps,data):
    starts,ends,_,_ = data
    h = expq(eps*phi)
    links = expq(eps*(phi[ends]-phi[starts]))
    return links, mul(h[starts],mul(links,inv(h[ends])))


def magnetic(links,n):
    grid = links.reshape(n,n,n,3,4)
    cost = 0.
    for i,j in ((0,1),(1,2),(0,2)):
        a,b = grid[...,i,:],grid[...,j,:]
        cost += np.sum((mul(a,np.roll(b,-1,axis=i))-mul(b,np.roll(a,-1,axis=j)))**2)/2
    return cost


def controls():
    for n in (2,3,4):
        sites = np.array(list(product(range(n),repeat=3)))
        data = axial.design(n)
        phi = (np.column_stack([(-1.)**sites[:,0],(-1.)**sites[:,1],np.zeros(n**3)])
               if n!=3 else np.column_stack([np.cos(2*np.pi*sites[:,0]/n),
                                             np.sin(2*np.pi*sites[:,0]/n),np.zeros(n**3)]))
        projected = area(phi,data)
        np.testing.assert_allclose(area(phi+[.7,-1.1,.3],data),projected,atol=2e-14)
        norm2 = np.sum(projected**2)
        expected = n**3*(8 if n!=3 else np.sin(2*np.pi/n)**2)
        np.testing.assert_allclose(norm2,expected)
        for eps in (.05,.005,.0005):
            links,reduced = endpoints(phi,eps,data)
            scaled = reduced[:,1:]/eps**2
            err = np.max(np.abs(scaled-np.cross(phi[data[0]],phi[data[1]])))
            assert err < 8*eps
            cost = magnetic(links,n)
            exact = 2*n**3*np.sin(2*eps)**4 if n!=3 else 0.
            np.testing.assert_allclose(cost,exact,atol=2e-14)
        # A finite exact-gradient link is pure gauge even for these same potentials.
        h = expq(.3*phi)
        pure = mul(inv(h[data[0]]),h[data[1]])
        np.testing.assert_allclose(mul(h[data[0]],mul(pure,inv(h[data[1]]))),
                                   np.tile([1,0,0,0],(len(pure),1)),atol=2e-15)
        print(n, "projected area norm squared",norm2, "scaled area max error",err)


def wilson(beta,phi,data,normals):
    starts,ends,_,chol = data
    n = len(phi)
    xi = np.linalg.solve(chol.T,normals.reshape(-1,n-1,3).transpose(1,0,2)
                         .reshape(n-1,-1)).reshape(n-1,-1,3).transpose(1,0,2)/np.sqrt(beta)
    r = np.linalg.norm(xi,axis=-1)
    q = np.zeros((len(normals),n,4))
    q[:,0,0] = 1
    q[:,1:] = expq(xi)
    proposal = (normals**2).sum(axis=1)/2+2*np.log(np.abs(np.sinc(r/np.pi))).sum(1)
    proposal[np.any(r>=np.pi,axis=1)] = -np.inf
    original,U = endpoints(phi,beta**(-.25),data)
    I = np.zeros_like(U)
    I[:,0] = 1
    def entry(left,right):
        terms = mul(inv(q[:,ends]),mul(inv(left),q[:,starts]))
        scalar = beta*(terms[:,:,0]*right[:,0]-1).sum(1)
        F = -beta*np.einsum('nec,ed->ncd',terms[:,:,1:],right[:,1:])
        collective, _ = triad.fisher_logs(F)
        return logsumexp(proposal+scalar+collective)
    center,mixed,diag = entry(I,I),entry(I,U),entry(U,U)
    return [(center+diag)/2-mixed, mixed-center-beta*magnetic(original,2)/2]


if __name__=='__main__':
    controls()
    data = axial.design(2)
    sites = np.array(list(product(range(2),repeat=3)))
    phi = .4*np.column_stack([(-1.)**sites[:,0],(-1.)**sites[:,1],np.zeros(8)])
    w = 8*8*.4**4
    target = np.array([np.log(np.sinh(w)/w)/2,-20*8*.4**4])
    print("limiting log ratios, geometric and full mixed/central", target)
    betas = (64,256,1024,4096)
    runs = []
    for seed in range(6):
        normals = ndtri(qmc.Sobol(21,scramble=True,seed=909+seed).random_base2(11))
        runs.append([wilson(beta,phi,data,normals) for beta in betas])
    for beta,row in zip(betas,np.swapaxes(runs,0,1)):
        print(beta,row.mean(0),"scramble SE",row.std(0,ddof=1)/np.sqrt(len(row)))
    assert np.all(np.abs(np.mean(runs,0)[-1]-target)<[.01,.05])
