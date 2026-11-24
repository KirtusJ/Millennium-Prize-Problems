"""Stress the row-likelihood and Ritz bounds on positive reversible kernels."""
import numpy as np


def check(rng):
    size=12
    # Two endpoints independent conditional on one latent label: positive operator.
    centers=np.arange(4)
    memberships=np.repeat(centers,3)
    logits=rng.normal(0,1.4,(4,5))[memberships]+rng.normal(0,.08,(size,5))
    conditional=np.exp(logits)
    conditional/=conditional.sum(axis=0)
    joint=(conditional*rng.dirichlet(np.ones(5))) @ conditional.T
    marginal=joint.sum(axis=1)
    root=np.sqrt(marginal)
    operator=joint/np.outer(root,root)
    centered=operator-np.outer(root,root)
    V=np.eye(4)[memberships]
    V*=root[:,None]/np.sqrt(marginal@V)
    E=V@V.T
    projected=np.linalg.eigvalsh(V.T@centered@V)[-1]
    actual=np.linalg.eigvalsh(centered)[-1]
    oscillation=0
    for i in range(size):
        for j in np.flatnonzero(memberships==memberships[i]):
            oscillation=max(oscillation,np.ptp(np.log(joint[j]/joint[i])))
    delta=np.sinh(oscillation/2)/np.sqrt(2)
    assert np.linalg.norm((np.eye(size)-E)@operator,2)<=delta+1e-12
    upper=(projected+np.hypot(projected,2*delta))/2
    assert projected<=actual+1e-12 and actual<=upper+1e-12
    return upper<1


if __name__=="__main__":
    rng=np.random.default_rng(571824)
    informative=sum(check(rng) for _ in range(200))
    assert informative>0
    print(f"200 partition enclosures passed, {informative} upper bounds below one")
