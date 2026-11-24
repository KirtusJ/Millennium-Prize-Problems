"""Exact-size Fourier matrices for the quadratic 24-colour test in the time vacuum."""
from itertools import combinations, product
import numpy as np
from retraction import step

PARITY = list(product(range(2), repeat=3))


def transverse(q):
    gradient = np.expm1(1j*q)
    if np.linalg.norm(gradient) < 1e-12:
        return np.empty((3, 0), dtype=complex)
    return np.linalg.qr(gradient[:, None], mode="complete")[0][:, 1:]


def colour_matrix():
    jmat = np.zeros((24,24))
    for p in PARITY:
        for i,j in combinations(range(3),2):
            x = p if p[j] else step(p,j)
            y = p if p[i] else step(p,i)
            slots = [3*PARITY.index(x)+i,3*PARITY.index(y)+j]
            sign = (1 if p[j] else -1)*(-1 if p[i] else 1)
            jmat[np.ix_(slots,slots)] += np.linalg.inv([[6,sign],[sign,6]])/24
    return jmat


def fibre(k,jmat,period=None):
    harmonics = []
    variances = []
    for ell in PARITY:
        q = k/2+np.pi*np.array(ell)
        frame = transverse(q)
        if not frame.shape[1]:
            continue
        phases = np.exp(1j*np.array(PARITY)@q)/np.sqrt(8)
        harmonics.append(np.vstack([phase*frame for phase in phases]))
        s = sum(abs(np.expm1(1j*q))**2)
        covariance=1/np.sqrt(s*(s+4))
        if period is not None:
            omega=2*np.arcsinh(np.sqrt(s)/2)
            cov_sum=np.mean(1/(s+4*np.sin(np.pi*np.arange(period)/period)**2))
            np.testing.assert_allclose(cov_sum,covariance/np.tanh(period*omega/2),rtol=1e-12)
            covariance=cov_sum
        variances.extend([covariance]*frame.shape[1])
    basis = np.hstack(harmonics)
    g = np.diag(variances)
    coarse_frame = transverse(k)
    edges = np.zeros((24,3))
    for i in range(3):
        edges[i,i]=1
        edges[3*PARITY.index(step((0,0,0),i))+i,i]=1
    coarse_edges=edges@coarse_frame
    coarse=basis.conj().T@coarse_edges
    np.testing.assert_allclose(basis@coarse,coarse_edges,atol=2e-12)
    np.testing.assert_allclose(jmat@coarse_edges,0,atol=2e-12)
    if coarse.shape[1]:
        gc=g@coarse
        residual=g-gc@np.linalg.solve(coarse.conj().T@gc,gc.conj().T)
        fine=np.linalg.qr(coarse, mode="complete")[0][:, coarse.shape[1]:]
    else:
        residual=g
        fine=np.eye(len(g))
    packed=basis@fine
    loss=packed.conj().T@jmat@packed
    var=fine.conj().T@residual@fine
    lower=np.linalg.cholesky(var)
    left=np.linalg.solve(lower,loss)
    normalized=np.linalg.solve(lower,left.conj().T).conj().T
    if period is not None:
        return np.linalg.eigvalsh(normalized)[0]
    omega=np.arcsinh(1/(2*np.array(variances)))
    inv_loss=1/(-np.expm1(-2*omega))
    physical_fine=np.linalg.qr(np.sqrt(variances)[:,None]*coarse,mode="complete")[0][:,coarse.shape[1]:]
    inverse=physical_fine.conj().T@(inv_loss[:,None]*physical_fine)
    return np.array([np.linalg.eigvalsh(normalized)[0],1/np.linalg.eigvalsh(inverse)[-1]])


if __name__=="__main__":
    jmat=colour_matrix()
    for side in (6,8,10,16,24,32,64):
        m=side//2
        # Cubic symmetries and reflection through even grid vertices preserve the
        # parity colouring as a collection and the Gaussian vacuum.
        freq = 2*np.pi*np.arange(m//2+1)/m
        vals=[]
        for a,b,c in product(freq,repeat=3):
            if a<=b<=c:
                vals.append(fibre(np.array([a,b,c]),jmat))
        if side in (6,8):
            full=[fibre(2*np.pi*np.array(indices)/m,jmat) for indices in product(range(m),repeat=3)]
            np.testing.assert_allclose(np.min(full,axis=0),np.min(vals,axis=0),atol=1e-13)
        local,time=np.min(vals,axis=0)
        assert local>=1/2688-1e-12 and time>=1/6-1e-12
        print(f"N={side:2}, minimum local quotient={local:.9f}, physical two-step={time:.9f}")
        if side==8:
            for period in (6,12,48):
                finite=min(fibre(np.array([a,b,c]),jmat,period)
                           for a,b,c in product(freq,repeat=3) if a<=b<=c)
                assert finite >= 1/2688
                print(f"  finite period {period}, local quotient={finite:.9f}")
            np.testing.assert_allclose(finite,local,rtol=1e-9)
