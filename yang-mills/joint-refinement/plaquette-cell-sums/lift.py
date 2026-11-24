"""Two lifts of a positive reversible kernel on nonuniform reference cells."""
import numpy as np


def deficit(joint):
    root=np.sqrt(joint.sum(axis=1))
    return 1-np.linalg.eigvalsh(joint/np.outer(root,root))[-2]


def ensemble(rng):
    f=rng.lognormal(0,.8,(12,5))
    J=f@f.T
    return J/J.sum()


def run(rng):
    cells=np.repeat(np.arange(4),3)
    membership=np.eye(4)[cells]
    h=rng.dirichlet(np.ones(12)*2)
    laws=[ensemble(rng),ensemble(rng)]
    records=[]
    for joint in laws:
        v=joint.sum(axis=1)
        J=membership.T@joint@membership
        cell_v=J.sum(axis=1)
        cell_h=h@membership
        density=joint/np.outer(h,h)
        L=max(np.max(np.abs(np.log(density[x]/density[y])))
              for x in range(12) for y in np.flatnonzero(cells==cells[x]))
        ref_cond=h/cell_h[cells]
        lifted=J[np.ix_(cells,cells)]*np.outer(ref_cond,ref_cond)
        np.testing.assert_allclose(deficit(lifted),deficit(J),atol=1e-12)
        assert np.all(joint+1e-14>=np.exp(-2*L)*lifted)
        assert np.all(v<=np.exp(L)*lifted.sum(axis=1)+1e-14)
        assert deficit(joint)+1e-12>=np.exp(-3*L)*deficit(J)
        normalized=joint/np.outer(v,v)
        U=max(np.max(np.abs(np.log(normalized[x]/normalized[y])))
              for x in range(12) for y in np.flatnonzero(cells==cells[x]))
        assert deficit(joint)+1e-12>=np.exp(-2*U)*deficit(J)
        records.append((J,cell_v,L))
    (jf,vf,L),(jc,vc,_)=records
    off=~np.eye(4,dtype=bool)
    alpha=min(1,np.exp(-3*L)*np.min(jf[off]/jc[off])/np.max(vf/vc))
    assert deficit(laws[0])+1e-12>=alpha*deficit(laws[1])
    # Recurrence identity including the clipping case.
    d0=d=rng.uniform(.1,.9)
    weight=1.
    cost=0.
    for _ in range(8):
        alpha,K,kappa=rng.uniform(.6,1.),rng.uniform(1.,1.2),rng.uniform(0,.05)
        d=max(0,alpha*d-kappa)/K
        cost+=weight*kappa/alpha
        weight*=K/alpha
        np.testing.assert_allclose(d,max(0,d0-cost)/weight,atol=1e-14)


if __name__=="__main__":
    rng=np.random.default_rng(865721)
    for _ in range(300):run(rng)
    print("300 nonuniform reference, cross-lattice, and recurrence checks passed")
