"""Compare the near-central SO(3) prediction with pinned Wilson integration."""
import importlib.util
from pathlib import Path

import numpy as np
from scipy.special import i0, i1, logsumexp, ndtri
from scipy.stats import qmc

spec = importlib.util.spec_from_file_location("axial", Path(__file__).resolve().parents[1]/"check.py")
axial = importlib.util.module_from_spec(spec)
spec.loader.exec_module(axial)
nodes, weights = np.polynomial.legendre.leggauss(32)


def fisher_logs(matrices):
    singular = np.linalg.svd(matrices, compute_uv=False)
    a, b, c = singular.T
    c = c*np.sign(np.linalg.det(matrices))
    factors = (i0((a+b)[:, None]*(1+nodes)/2)*
               i0((a-b)[:, None]*(1-nodes)/2))*weights/2
    return tuple(np.log(np.sum(factors*np.exp(sign*c[:, None]*nodes),axis=1))
                 for sign in (1,-1))


def boltzmann_ratio(beta,t,amplitudes,data,normals):
    starts, ends, axes, chol = data
    n = len(chol)+1
    angle = t*np.array(amplitudes)/np.sqrt(beta*n)
    xi = np.linalg.solve(chol.T,normals.reshape(-1,n-1,3).transpose(1,0,2)
                         .reshape(n-1,-1)).reshape(n-1,-1,3).transpose(1,0,2)/np.sqrt(beta)
    radius = np.linalg.norm(xi,axis=-1)
    q = np.empty((len(normals),n,4))
    q[:,0] = [1,0,0,0]
    q[:,1:,0], q[:,1:,1:] = np.cos(radius), xi*np.sinc(radius[:,:,None]/np.pi)
    weight = (normals**2).sum(1)/2+2*np.log(np.abs(np.sinc(radius/np.pi))).sum(1)
    weight[np.any(radius>=np.pi,axis=1)] = -np.inf
    left = np.zeros((len(axes),4))
    left[:,0] = np.cos(angle[axes])
    left[np.arange(len(axes)),1+axes] = -np.sin(angle[axes])
    terms = axial.multiply(q[:,ends]*[1,-1,-1,-1],axial.multiply(left,q[:,starts]))
    weight += beta*(terms[:,:,0]*np.cos(angle[axes])-1).sum(axis=1)
    matrix = -beta*np.stack([terms[:,axes==i,1:].sum(axis=1)*np.sin(angle[i])
                             for i in range(3)],axis=2)
    same, mirror = fisher_logs(matrix)
    return logsumexp(weight+same)-logsumexp(weight+mirror)


def run():
    t = 1.2
    k = t*t
    explicit = 2*k+np.log((i0(2*k)-i1(2*k))/(i0(2*k)+i1(2*k)))
    same, mirror = fisher_logs(k*np.eye(3)[None,:,:])
    assert abs((same-mirror).item()-explicit)<1e-14
    data = axial.design(2)
    betas = (16,64,256,1024)
    rows = []
    for seed in range(8):
        normals = ndtri(qmc.Sobol(21,scramble=True,seed=331+seed).random_base2(12))
        if seed==0:
            assert abs(boltzmann_ratio(64,t,[1,2,0],data,normals)) < 1e-13
        rows.append([boltzmann_ratio(b,t,[1,1,1],data,normals) for b in betas])
    print("diffusive limiting log ratio",explicit)
    for b,row in zip(betas,np.array(rows).T):
        print(b,row.mean(),row.std(ddof=1)/np.sqrt(len(row)))
    assert abs(np.mean(rows,axis=0)[-1]-explicit)<.003


if __name__=='__main__':
    run()
