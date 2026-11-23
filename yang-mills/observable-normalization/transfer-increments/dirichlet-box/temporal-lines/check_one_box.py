"""Finite-coupling importance check for the conditional line variance in the smallest box."""
from pathlib import Path
import runpy

import numpy as np

box = runpy.run_path(str(Path(__file__).resolve().parents[1] / "check_box.py"))


def multiply(a, b):
    s, x = a[..., :1], a[..., 1:]
    t, y = b[..., :1], b[..., 1:]
    return np.concatenate((s*t-np.sum(x*y, axis=-1, keepdims=True),
                           s*y+t*x+np.cross(x, y)), axis=-1)


def estimate(beta, shell, seed):
    D, n, faces = box["complex_data"](2)
    D = D.toarray()
    gram = D[:, :n].T @ D[:, :n]
    shift = -np.linalg.solve(gram, D[:, :n].T @ D[:, n:] @ shell)
    chol = np.linalg.cholesky(np.linalg.inv(gram))
    rng = np.random.default_rng(seed)
    sums = np.zeros(7)
    for _ in range(32):
        # Use the conditional Gaussian on the seven free links as proposal.
        phi = shift + chol @ rng.normal(size=(256, n, 3))
        field = np.concatenate((phi, np.broadcast_to(shell, (256, *shell.shape))), axis=1)
        angles = np.linalg.norm(field, axis=2)/np.sqrt(beta)
        coeff = np.sinc(angles/np.pi)
        links = np.concatenate((np.cos(angles)[..., None],
                                coeff[..., None]*field/np.sqrt(beta)), axis=2)
        identity = np.broadcast_to([1.,0.,0.,0.], (256, 1, 4))
        links = np.concatenate((links, identity), axis=1)
        inv = np.array([1,-1,-1,-1])
        ordered = multiply(multiply(links[:, faces[:,0]], links[:, faces[:,1]]),
                           multiply(links[:, faces[:,2]]*inv, links[:, faces[:,3]]*inv))
        act = beta/2*np.square(ordered-[1.,0.,0.,0.]).sum(axis=(1,2))
        quad = np.square(D @ field).sum(axis=(1,2))/2
        w = np.exp(quad-act + 2*np.log(np.abs(coeff[:, :n])).sum(axis=1))
        w[np.any(angles[:, :n] >= np.pi, axis=1)] = 0.
        line = links[:, 0]-[1.,0.,0.,0.]
        sums += np.r_[w.sum(), w@w, w@line, w@np.square(line).sum(axis=1)]
    return sums[2:6]/sums[0], sums[6]/sums[0], sums[0]**2/sums[1]


if __name__ == '__main__':
    D, n, _ = box["complex_data"](2)
    rng = np.random.default_rng(51261)
    random_boundary = rng.normal(scale=.35, size=(D.shape[1]-n, 3))
    for label, shell in [('identity', np.zeros_like(random_boundary)), ('scaled', random_boundary)]:
        for beta in (64., 256., 4096.):
            m, q, ess = estimate(beta, shell, 376)
            m2, q2, ess2 = estimate(beta, shell, 933)
            variance = beta/4*(q+q2-2*m@m2)
            print(f'{label} beta={beta:g} variance*beta/L={variance:.6f} '
                  f'minimum effective sample size {min(ess,ess2):.1f}/8192', flush=True)
            assert abs(variance-.5)<.04 and min(ess, ess2)>6000
