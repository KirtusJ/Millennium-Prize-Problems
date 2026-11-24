"""Mean-zero free scalar. Check the one-particle regression and energy inequalities."""
from itertools import product

import numpy as np


def omega(indices, n):
    return 2*n*np.sqrt(np.sum(np.sin(np.pi*np.asarray(indices)/n)**2, axis=-1))


def position_space_control():
    n = 6
    sites = np.arange(n**3).reshape(n,n,n)
    identity = np.eye(n**3)
    laplacian = 6*identity
    for axis in range(3):
        for sign in [-1,1]:
            laplacian -= identity[np.roll(sites,sign,axis).ravel()]
    freq2, basis = np.linalg.eigh(n*n*laplacian)
    freq = np.sqrt(freq2[1:])
    modes = basis[:,1:]
    covariance = (modes/(2*freq))@modes.T
    sample = identity[sites[::2,::2,::2].ravel()]
    sample -= sample.mean(axis=0)
    observed = sample@covariance@sample.T
    residual = covariance-covariance@sample.T@np.linalg.pinv(observed,hermitian=True)@sample@covariance
    wave = np.cos(2*np.pi*np.indices(sites.shape)[0].ravel()/n)
    measured = (wave@residual@wave)/(wave@covariance@wave)
    aliases = np.array([1,0,0])+(n//2)*np.array(list(product([0,1],repeat=3)))
    inverse = 1/omega(aliases,n)
    np.testing.assert_allclose(measured,1-inverse[0]/inverse.sum(),atol=1e-12)
    print(f"Direct position-space Gaussian regression, side six: loss={measured:.8f}")


def check(n):
    m = n//2
    reps = np.arange(-(m//2), (m+1)//2)
    offsets = m*np.array(list(product([0,1], repeat=3)))
    momenta = np.array(list(product(reps, repeat=3)))
    momenta = momenta[np.any(momenta,axis=1)]
    freq = omega(momenta[:,None,:]+offsets[None,:,:],n)
    coarse = omega(momenta,m)
    assert np.all(freq[:,1:] >= np.sqrt(2)*n-1e-10)
    assert np.all(freq >= coarse[:,None]-1e-10)
    inverse = 1/freq
    weights = inverse / inverse.sum(axis=1)[:,None]
    lag = 1/64
    inherited = np.sum(weights*np.exp(-lag*freq),axis=1)
    assert np.all(inherited <= np.exp(-lag*coarse)+1e-14)
    cutoff = -np.log(.75)/lag
    assert cutoff < np.sqrt(2)*n
    low = freq[:,0]<=cutoff
    losses = 1-weights[:,0]
    assert np.all(losses[low] <= 7/np.sqrt(2)*freq[low,0]/n)
    k = np.flatnonzero(np.all(momenta==[1,0,0],axis=1))[0]
    exact_ratio = losses[k]*n/freq[k,0]
    p = np.outer(np.sqrt(weights[k]),np.sqrt(weights[k]))
    # Direct conditional projection on a normalized, two-particle low-mode tensor.
    tensor = np.kron(p,p)
    assert 1-tensor[0,0] <= 7/np.sqrt(2)*2*freq[k,0]/n
    print(f"N={n}, low linear modes={low.sum()}, fixed-mode loss/(a*omega)={exact_ratio:.8f}")
    return exact_ratio


if __name__=="__main__":
    position_space_control()
    values = [check(n) for n in (16,24,32,48,64,96)]
    limit = (3+3/np.sqrt(2)+1/np.sqrt(3))/2
    assert np.all(np.diff(values)>0) and abs(values[-1]-limit)<abs(values[0]-limit)
    print(f"Analytic limit {limit:.8f}; all checks passed.")
