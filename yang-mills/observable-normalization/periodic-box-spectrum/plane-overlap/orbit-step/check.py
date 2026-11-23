"""Pinned Haar integral for the one-step ratio, integrating the global axis exactly."""
from itertools import product

import numpy as np
from scipy.special import logsumexp, ndtri
from scipy.stats import qmc


def multiply(a, b):
    s, v = a[..., :1], a[..., 1:]
    t, w = b[..., :1], b[..., 1:]
    return np.concatenate([s*t-np.sum(v*w, axis=-1, keepdims=True),
                           s*w+t*v+np.cross(v,w)], axis=-1)


def log_sinhc(x):
    return np.log1p(x*x/6+x**4/120) if np.max(x) < 1e-4 else np.log(
        np.sinh(x)/np.where(x==0, 1, x), where=x!=0, out=np.zeros_like(x))


def design(size):
    sites = list(product(range(size), repeat=3))
    starts, ends, axes = [], [], []
    for k, site in enumerate(sites):
        for i in range(3):
            nxt = list(site)
            nxt[i] = (nxt[i]+1)%size
            starts.append(k)
            ends.append(sites.index(tuple(nxt)))
            axes.append(i)
    incidence = np.eye(len(sites))[starts,1:] - np.eye(len(sites))[ends,1:]
    return starts, ends, np.array(axes), np.linalg.cholesky(incidence.T@incidence)


def run(beta, t, data, normals):
    starts, ends, axes, chol = data
    rows = len(chol)
    samples = len(normals)
    xi = np.linalg.solve(chol.T, normals.reshape(samples,rows,3).transpose(1,0,2)
                         .reshape(rows,-1)).reshape(rows,samples,3).transpose(1,0,2)/np.sqrt(beta)
    radii = np.linalg.norm(xi,axis=-1)
    q = np.empty((samples,rows+1,4))
    q[:,0,:] = [1,0,0,0]
    q[:,1:,0] = np.cos(radii)
    q[:,1:,1:] = xi*np.sinc(radii[:,:,None]/np.pi)
    weights = np.sum(normals**2,axis=1)/2 + 2*np.log(np.abs(np.sinc(radii/np.pi))).sum(axis=1)
    weights[np.any(radii>=np.pi,axis=1)] = -np.inf
    link_angle = t/np.sqrt(beta*(rows+1))
    def log_integral(a,b):
        left = np.zeros((len(axes),4))
        left[:,0],left[:,3] = np.cos(a*(axes==0)),-np.sin(a*(axes==0))
        term = multiply(q[:,ends]*[1,-1,-1,-1],multiply(left,q[:,starts]))
        constant = (term[:,:,0]*np.cos(b*(axes==0))-1).sum(axis=1)
        vector = term[:,:,1:][:,axes==0,:].sum(axis=1)*np.sin(b)
        return logsumexp(weights + beta*constant + log_sinhc(beta*np.linalg.norm(vector,axis=1)))
    return (log_integral(0.,0.)+log_integral(link_angle,link_angle))/2-log_integral(0.,link_angle)


if __name__ == '__main__':
    data = design(2)
    t = 1.5
    target = log_sinhc(np.array([t*t]))[0]/2
    print("predicted limiting log ratio", target)
    estimates = []
    for seed in range(8):
        draws = qmc.Sobol(21,scramble=True,seed=111+seed).random_base2(12)
        normals = ndtri(draws)
        estimates.append([run(beta,t,data,normals) for beta in (16,64,256,1024)])
    for beta,values in zip((16,64,256,1024),np.array(estimates).T):
        print(beta, "mean",values.mean(),"scramble SE",values.std(ddof=1)/np.sqrt(len(values)))
    assert abs(np.mean(estimates,axis=0)[-1]-target)<.002
