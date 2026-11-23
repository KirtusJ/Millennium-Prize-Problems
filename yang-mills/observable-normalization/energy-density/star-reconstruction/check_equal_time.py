"""Direct equal-time electric projection, with the temporal mode integrated exactly."""
from itertools import product

import numpy as np
from numpy.polynomial.legendre import leggauss


def equal_time(order):
    nodes,weights=leggauss(order)
    # All octants, complex face shifts and both signs. No symmetry projection.
    k=np.pi*nodes
    k1,k2=np.meshgrid(k,k,indexing="ij")
    W=weights[:,None]*weights[None,:]/4
    M=np.zeros((6,6),dtype=complex)
    d=0.
    for k0,w0 in zip(k,weights/2):
        ang=np.array([np.full_like(k1,k0),k1,k2])
        p=np.exp(1j*ang)-1
        a=abs(p)**2
        A=a.sum(axis=0)
        factor=1/np.sqrt(A*(A+4))
        # Integral over k_t of 1/(a_t + A). The zero mode has measure zero.
        d+=np.sum(w0*W*a[0]**2*factor)
        for j,l in product(range(3),repeat=2):
            C=(j==l)+(p[j]*p[l].conj()-(A if j==l else 0))*factor
            for r,s in product(range(2),repeat=2):
                left=np.exp(-1j*ang[j]) if r else -1
                right=np.exp(1j*ang[l]) if s else -1
                M[2*j+r,2*l+s]+=np.sum(w0*W*left*C*right)
    assert np.max(abs(M.imag))<1e-13
    return M.real,d


def main():
    M,d=equal_time(54)
    vals=sorted([1.,d/2,d/2]+[(2-d)/3]*3)
    # Quadrature breaks exact four-axis permutation symmetry at finite order.
    assert np.max(abs(np.linalg.eigvalsh(M)-vals))<2e-6
    assert np.max(abs(M@np.ones(6)-1))<1e-13
    norm=1+d*d/2+(2-d)**2/3
    assert abs(norm-np.sum(M*M))<4e-6
    print("d, eigenvalues, squared Frobenius norm",d,vals,norm)
    print("scaled raw variance, exterior variance, irreducible fraction",norm/1536,(norm-1)/1536,1/norm)


if __name__=="__main__":
    main()
