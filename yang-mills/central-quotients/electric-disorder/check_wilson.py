"""SU(2) Wilson transfer on the physical Hilbert space of one isolated square."""
from math import exp, pi
import numpy as np
from scipy.linalg import eigh
from scipy.special import ive


def evaluate(beta, beta_s, dimension):
    beta_t=beta*beta/beta_s
    labels=np.arange(1,dimension+1)
    theta=pi*labels/(dimension+1)
    sine=np.sqrt(2/(dimension+1))*np.sin(np.outer(labels,theta))
    x=np.cos(theta)
    # Product of four temporal link multipliers on a loop character.
    free=(ive(labels,beta_t)/ive(1,beta_t))**4
    half=np.exp(-.5*beta_s*(1-x))
    factor=np.sqrt(free)[:,None]*sine*half
    transfer=factor.T @ factor
    values,eigen=eigh(transfer)
    leading=values[-1]
    values/=leading
    omega=eigen[:,-1]
    defect=omega[::-1]
    j=np.exp(-beta_s*x)
    conjugate=(j[:,None]*transfer)*j
    assert np.max(abs(transfer[::-1,::-1]-conjugate))/leading < 3e-10
    u=1-(omega*x)@omega
    time=2*beta_s
    one_step=np.linalg.norm(factor @ defect)**2/leading
    threshold=np.exp(-time/2)
    assert min(abs(values-threshold))>1e-13
    low=np.linalg.norm(eigen[:,values>=threshold].T @ defect)**2
    bound=(np.sqrt(4*u)+np.exp(-time/8))**2
    assert low <= bound+1e-12
    residual=np.linalg.norm(transfer @ defect/leading-np.exp(-time)*defect)
    assert residual <= time*(np.exp(time)+1)*np.sqrt(2*u)/2+1e-12
    return np.array([u,one_step,low])


if __name__=="__main__":
    for beta in (2.,4.,8.,16.,24.):
        for beta_s in (.5,beta):
            fine=evaluate(beta,beta_s,157)
            coarse=evaluate(beta,beta_s,91)
            assert np.max(abs(coarse-fine)) < 1e-8
            print("beta, spatial coupling, deficit, one-step reading, raw mass below half scale",
                  beta,beta_s,*fine)
