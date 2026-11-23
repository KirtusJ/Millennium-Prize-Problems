"""Exact finite operator constructions for the Gibbs sweep and compressed returns."""
import itertools
import numpy as np


def projection(mass, labels):
    _, groups = np.unique(labels, return_inverse=True, axis=0)
    membership = np.eye(groups.max()+1)[groups]
    weights = mass @ membership
    return np.sqrt(mass[:, None]/weights) * membership


def sweep(seed):
    rng = np.random.default_rng(seed)
    coordinates = np.array(list(itertools.product(range(2), repeat=4)))
    mass = rng.dirichlet(np.ones(16)*0.7)
    # x has three binary coordinates, y is retained during all three updates.
    U = projection(mass, coordinates[:, :3])
    blocks = [(0,1),(1,2),(0,2)]
    total = np.zeros((8,8))
    product = np.eye(16)
    for block in blocks:
        exterior = np.delete(coordinates,block,axis=1)
        V = projection(mass,exterior)
        E = V @ V.T
        total += np.eye(8)-U.T @ E @ U
        product = E @ product
    W = U.T @ product @ U
    marginal = np.sqrt(mass.reshape(8,2).sum(axis=1))
    centered = np.eye(8)-np.outer(marginal,marginal)
    W0 = centered @ W @ centered
    q = np.linalg.norm(W0,2)
    gamma = np.linalg.eigvalsh(total/len(blocks))[1]
    assert (1-q)/(len(blocks)*(1+q)) <= gamma+1e-12
    assert gamma <= (len(blocks)+1)*(1-q*q)/2+1e-12
    H = W0.T @ W0
    moment = np.trace(np.linalg.matrix_power(H,3))
    assert q**6 <= moment+1e-12
    # Stationarity and positive raw endpoint density after the complete sweep.
    np.testing.assert_allclose(W @ marginal,marginal,atol=1e-12)
    np.testing.assert_allclose(W.T @ marginal,marginal,atol=1e-12)
    assert W.min()>0


def cycles():
    b, a = 0.52, 0.71
    prob = np.array([(1-b)/2,(1+b)/2])
    root = np.sqrt(prob)
    spin = a*np.eye(2)+(1-a)*np.outer(root,root)
    fine = np.kron(spin,spin)
    m = np.kron(prob,prob)
    U = projection(m,np.array([1,-1,-1,1])[:,None])
    A = U.T @ fine @ U
    remainder = (np.eye(4)-U@U.T) @ fine @ U
    w = 2*b*b/(1+b*b)
    leak = np.trace(U.T @ fine @ fine @ U - A @ A)
    np.testing.assert_allclose([leak,np.linalg.norm(remainder)**2],w*(1-w)*(a-a*a)**2)
    h, rho = .00001,.83
    v = np.array([1-h,h])
    joint = rho*np.diag(v)+(1-rho)*np.outer(v,v)
    np.testing.assert_allclose(np.abs(joint-np.outer(v,v)).sum()/2,2*rho*h*(1-h))
    for p in (2,3,6):
        M = np.trace(np.linalg.matrix_power(joint/v[:,None],p))-1
        np.testing.assert_allclose(M,rho**p)
        raw = np.trace(np.linalg.matrix_power(np.outer(v,v),p))
        np.testing.assert_allclose(raw,(v@v)**p)
    print("unbroken-lag leakage",leak,"rare-state centered norm",rho)


if __name__ == "__main__":
    for seed in range(100):
        sweep(seed)
    cycles()
    print("100 all-test sweep comparisons passed")
