"""Direct Wilson quadrature of the rescaled transfer at two representative points."""
from itertools import combinations
from math import pi

import numpy as np
from scipy.integrate import cumulative_trapezoid, trapezoid
from scipy.stats import qmc


def exponential(y):
    norm = np.linalg.norm(y, axis=-1, keepdims=True)
    return np.concatenate([np.cos(norm), np.sinc(norm/pi)*y], axis=-1)


def multiply(a, b):
    return np.concatenate([a[...,:1]*b[...,:1]-(a[...,1:]*b[...,1:]).sum(-1,keepdims=True),
                           a[...,:1]*b[...,1:]+b[...,:1]*a[...,1:]
                           +np.cross(a[...,1:], b[...,1:])], axis=-1)


def potential(vectors):
    return 2*sum((np.cross(vectors[...,i,:], vectors[...,j,:])**2).sum(-1)
                 for i,j in combinations(range(vectors.shape[-2]),2))


def evaluate(beta, x, points):
    h = beta**(-1/3)
    u = exponential(h*x)
    t = np.linspace(0, 14, 16385)
    theta = t/np.sqrt(beta)
    radial = np.exp(-2*beta*np.sin(theta/2)**2)*(np.sqrt(beta)*np.sin(theta))**2
    cdf = cumulative_trapezoid(radial, t, initial=0)
    cdf /= cdf[-1]
    second = trapezoid(t*t*radial,t)/(3*trapezoid(radial,t))
    assert abs(second-1) < 1/beta
    polar = 2*points[...,1]-1
    angle = 2*pi*points[...,2]
    axis = np.stack([np.sqrt(1-polar**2)*np.cos(angle),
                     np.sqrt(1-polar**2)*np.sin(angle), polar],axis=-1)
    xi = (np.interp(points[...,0],cdf,t)/np.sqrt(beta))[...,None]*axis
    def reading(g):
        return np.exp(-(g[...,1:]**2).sum(axis=(-1,-2))/(2*h*h))
    def half(g):
        return np.exp(-beta*potential(g[...,1:])/2)
    evolved = 0
    for sign in (-1,1):
        y = multiply(u, exponential(sign*xi))
        evolved += (half(y)*reading(y)).mean()/2
    return (reading(u)-half(u)*evolved)/h


if __name__ == "__main__":
    for k in (2,3):
        points=qmc.Sobol(3*k,scramble=True,seed=293+k).random_base2(16).reshape(-1,k,3)
        x=np.array([[0.7,-0.1,0.2],[0.1,0.8,0.3],[-0.6,0.2,0.4]])[:k]
        expected=((3*k-(x*x).sum())/2+potential(x))*np.exp(-(x*x).sum()/2)
        for beta in (1e3,1e6,1e9):
            approx=evaluate(beta,x,points)
            print(k, int(beta), f"{approx:.7f}", f"limit {expected:.7f}")
        assert abs(approx-expected)<0.008
