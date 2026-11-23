"""Zero-mode-deleted, Abelian Gaussian control in exactly the sampled 4^4 geometry."""
from itertools import product
import numpy as np


def kernels(L):
    eye=np.eye(3)
    Ms=np.zeros((2,6,6),dtype=complex)
    for idx in product(range(L),repeat=4):
        if not any(idx):
            continue
        k=2*np.pi*np.array(idx)/L
        p=np.exp(1j*k)-1
        P=(abs(p[3])**2*eye+np.outer(p[:3],p[:3].conj()))/np.sum(abs(p)**2)
        D=np.zeros((6,3),dtype=complex)
        D[::2]=-eye
        D[1::2]=np.diag(np.exp(-1j*k[:3]))
        term=D@P@D.conj().T
        Ms[0]+=term
        Ms[1]+=term*np.exp(1j*k[3])
    assert np.max(abs(Ms.imag))<1e-9
    return Ms.real/L**4


def main():
    d=.70662423756
    a,b=d/2,(2-d)/3
    poles=np.array([.5,1.,2.,4.])
    coeff=[]
    for i,r in enumerate(poles):
        w=(-r-1)*(-r-a)*(-r-b)/np.prod(np.delete(poles-r,i))
        coeff.append(w*(1+1/r)**1.5*(1+a/r)**3*(1+b/r)**4.5)
    for L in (4,8):
        K=kernels(L)
        assert np.allclose(K[0]@np.ones(6),1) and np.allclose(K[1]@np.ones(6),0)
        assert abs(K[0][0,0]-(1-L**-4)/2)<1e-13
        for n,M in enumerate(K):
            covariance=0.
            for c,r in zip(coeff,poles):
                mean=np.linalg.det(np.eye(6)+K[0]/r)**-1.5
                cov=np.trace(M.T@np.linalg.solve(r*np.eye(6)+K[0],M))
                covariance-=1.5*c*mean*cov
            print("zero-mode-deleted Gaussian, L, lag, mixed covariance",L,n,covariance)


if __name__=="__main__":
    main()
