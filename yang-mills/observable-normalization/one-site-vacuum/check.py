"""Independent numerical controls for the Wilson walk used in the M0 proof."""
from math import ceil, log, sqrt

import numpy as np
from scipy.special import ive


def increments(rng, size, beta):
    # Haar deficit s has density proportional to sqrt(s(2-s)).
    s = np.empty(size)
    missing = np.arange(size)
    while len(missing):
        candidate = rng.gamma(1.5, 1/beta, len(missing))
        accepted = rng.random(len(missing))**2 < 1-candidate/2
        s[missing[accepted]] = candidate[accepted]
        missing = missing[~accepted]
    axis = rng.normal(size=(size,3))
    axis /= np.linalg.norm(axis, axis=1)[:,None]
    return np.column_stack((1-s, np.sqrt(s*(2-s))[:,None]*axis))


def multiply(x, y):
    return np.column_stack((x[:,0]*y[:,0]-(x[:,1:]*y[:,1:]).sum(axis=1),
                            x[:,:1]*y[:,1:]+y[:,:1]*x[:,1:]+np.cross(x[:,1:],y[:,1:])))


def occupation(beta, start, rng):
    size = 4096
    m = ceil(np.cbrt(beta))
    x,y = [np.tile(v,(size,1)) for v in start]
    log_survival = np.zeros(size)
    late = []
    for j in range(m):
        cross = np.cross(x[:,1:],y[:,1:])
        V = 2*beta*np.einsum('ij,ij->i',cross,cross)
        log_survival -= np.log1p(V)
        if j>=(m+1)//2:
            late.append((m*V >= 0.02).mean())
        x=multiply(x,increments(rng,size,beta))
        y=multiply(y,increments(rng,size,beta))
    survival=np.exp(log_survival)
    print(f"beta={beta:g}, m={m}, min sampled late fraction={min(late):.4f}, "
          f"mean survival={survival.mean():.6f}, SE={survival.std(ddof=1)/sqrt(size):.6f}")
    assert min(late)>0.5 and survival.mean()<0.95


def spectral(beta):
    m = ceil(np.cbrt(beta))
    j = (m+1)//2
    # A numerical partial sum at identity; the infinite tail is bounded in the proof.
    k = np.arange(1, 1+ceil(14*sqrt(beta/j)))
    coeff = ive(k,beta)/ive(1,beta)
    scaled = (j/beta)**1.5 * np.sum(k*k*coeff**j)
    assert 0.5 < scaled < 4
    for n,v in zip(k[7:],coeff[7:]):
        assert log(v) <= -n*np.log1p(n/beta)/8+1e-12
    print(f"scaled identity density partial sum={scaled:.7f}")


if __name__ == "__main__":
    rng=np.random.default_rng(293)
    I=(1,0,0,0)
    U=(0.6,0.8,0,0)
    for beta in (64, 1000, 32768):
        spectral(beta)
        for start in ((I,I),(U,U),(U,(0.6,0,0.8,0))):
            occupation(beta,start,rng)
