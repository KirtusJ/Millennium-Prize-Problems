"""Test the relative spectral bracket with nonconstant endpoint factors."""
import numpy as np


def norm(a):
    return np.linalg.norm(a, ord=2)


def check(U, labels, endpoint):
    U = U/np.linalg.norm(U)
    size = max(labels)+1
    basis = np.column_stack([endpoint*(labels==i) for i in range(size)])
    basis /= np.linalg.norm(basis, axis=0)
    comp = basis.T @ U @ basis
    table = np.zeros_like(comp)
    h = np.zeros_like(comp)
    F = U / np.outer(endpoint, endpoint)
    for i in range(size):
        for j in range(size):
            indices = np.ix_(labels==i, labels==j)
            table[i,j] = np.linalg.norm(U[indices])
            lo, hi = np.min(F[indices]), np.max(F[indices])
            h[i,j] = 2*np.sqrt(lo*hi)/(lo+hi)
    scale = norm(table)
    tol = 1e-12
    eta = norm(np.sqrt(np.maximum(0,1-h*h))*table)/scale
    delta = norm((1-h)*table)/scale
    assert norm(U-basis@comp@basis.T) <= eta*scale+tol
    xi = np.linalg.svd(table, compute_uv=False)/scale
    excited = np.linalg.eigvalsh(U)[::-1][:size]/scale
    c = xi+delta
    upper = (c+eta+np.sqrt((c-eta)**2+4*eta**2))/2
    assert np.all(excited+tol >= xi-delta)
    assert np.all(excited <= np.minimum(upper, c+eta)+tol)
    v = norm(h*table)/scale
    assert v-tol <= excited[0] <= 1+tol
    return max(0,xi[1]-delta), min(1,upper[1]/v), excited[0]**2*scale**2


def main():
    rng = np.random.default_rng(2341)
    labels = np.repeat(np.arange(3), [2,4,3])
    for step in range(60):
        base = rng.uniform(.1,2,(3,4))
        features = base[labels] + rng.uniform(0,.01+.003*step,(len(labels),4))
        endpoint = rng.uniform(.3,2,len(labels))
        U = (features@features.T+1e-5*np.eye(len(labels)))*np.outer(endpoint,endpoint)
        check(U, labels, endpoint)

    def block(a,e):
        return np.array([[a+e,a-e],[a-e,a+e]])/2
    eps = 1/32
    U = np.block([[block(2,eps),block(1,0)],[block(1,0),block(2,eps)]])
    base = check(U,np.array([0,0,1,1]),np.ones(4))
    for m in [1,4,16]:
        # All spectator states have separate visible labels.
        extra = np.eye(m)/8+np.ones((m,m))*7/(8*m)
        val = check(np.kron(extra,U),np.repeat(np.arange(2*m),2),np.ones(4*m))
        assert np.allclose(val[:2],base[:2])
        assert np.isclose(val[2],base[2]/(1+(m-1)/64))
        assert .333 <= val[0] <= 1/3 <= val[1] <= .335
        print(m,val)


if __name__ == "__main__":
    main()
