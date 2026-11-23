"""Check cycle ranks, SU(2) loop coordinates, and the normalized-filter estimate."""
from collections import deque
from pathlib import Path
import importlib.util
import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.special import ndtr

spec = importlib.util.spec_from_file_location(
    "box", Path(__file__).resolve().parents[3] / "second-box/transverse-plaquettes/check.py")
box = importlib.util.module_from_spec(spec)
spec.loader.exec_module(box)


def graph(shape, add_seam=False):
    sites = list(np.ndindex(shape))
    ids = {v:i for i,v in enumerate(sites)}
    edges, keep = [], []
    for v in sites:
        for i in range(3):
            w = list(v)
            w[i] = (w[i]+1)%shape[i]
            keep.append(w[i] != 0 or (add_seam and i == 0 and v[1:] == (0,0)))
            edges.append((ids[v], ids[tuple(w)], i))
    return edges, keep


def cycle_basis(edges,keep):
    n = max(max(a,b) for a,b,_ in edges)+1
    adjacent = [[] for _ in range(n)]
    for e,(a,b,_) in enumerate(edges):
        if keep[e]:
            adjacent[a].append((b,e,1))
            adjacent[b].append((a,e,-1))
    tree, paths = set(), {}
    for root in range(n):
        if root in paths:
            continue
        paths[root] = []
        q = deque([root])
        while q:
            a = q.popleft()
            for b,e,s in adjacent[a]:
                if b not in paths:
                    paths[b] = paths[a]+[(e,s)]
                    tree.add(e)
                    q.append(b)
    chords = [e for e in range(len(edges)) if keep[e] and e not in tree]
    loops = []
    for e in chords:
        a,b,_ = edges[e]
        loops.append(paths[a]+[(e,1)]+[(j,-s) for j,s in reversed(paths[b])])
    cycles = np.zeros((len(loops),len(edges)))
    for row,loop in zip(cycles,loops):
        for e,s in loop:
            row[e] += s
    np.testing.assert_array_equal(cycles[:,chords],np.eye(len(chords)))
    return cycles, loops


def hard_projector(edges):
    n = len(edges)//3
    gradient = np.zeros((len(edges),n))
    constants = np.zeros((len(edges),3))
    for e,(a,b,i) in enumerate(edges):
        gradient[e,a] = -1
        gradient[e,b] = 1
        constants[e,i] = 1
    excluded = np.column_stack([gradient[:,1:],constants])
    q = np.linalg.qr(excluded)[0]
    return np.eye(len(edges))-q@q.T,constants


def angle(q):
    v = q[1:]
    r = np.linalg.norm(v)
    return v if r == 0 else np.arctan2(r,q[0])*v/r


def log_loop(u, loop):
    q = np.array([1.,0.,0.,0.])
    for e,s in loop:
        factor = u[e] if s == 1 else u[e]*np.array([1,-1,-1,-1])
        q = box.multiply(q,factor)
    return angle(q)


def rank_and_loop(shape):
    edges,keep = graph(shape)
    cycles,loops = cycle_basis(edges,keep)
    hard,constants = hard_projector(edges)
    np.testing.assert_allclose(cycles@hard,cycles,atol=1e-13)
    minimum = np.linalg.eigvalsh(cycles@hard@cycles.T)[0]
    assert minimum>1-1e-12
    edges,seam = graph(shape,True)
    extra,_ = cycle_basis(edges,seam)
    u, widths, _ = np.linalg.svd(extra@constants,full_matrices=True)
    assert np.count_nonzero(widths>1e-8)==1
    residual = u[:,1:].T@extra
    np.testing.assert_allclose(residual@hard,residual,atol=1e-12)
    assert np.linalg.eigvalsh(residual@hard@residual.T)[0]>1-1e-12
    print(shape,"cycles",len(loops),"minimum Gram eigenvalue",round(minimum,8))
    if shape!=(2,2,2):
        return
    rng = np.random.default_rng(6292)
    x = rng.normal(size=(3,3))*.2
    z = hard@rng.normal(size=(len(edges),3))*.4
    dz = hard@rng.normal(size=z.shape)
    direction = np.array([i for _,_,i in edges])
    prev = None
    for h in (0.04,0.01,0.0025,0.000625):
        s = h**1.5
        def measure(zfield):
            u = box.qexp(h*x[direction]+s*zfield)
            return np.array([log_loop(u,loop)/s for loop in loops])
        err = np.max(np.abs(measure(z)-cycles@z))
        eps=1e-4
        derivative=(measure(z+eps*dz)-measure(z-eps*dz))/(2*eps)
        graderr=np.max(np.abs(derivative-cycles@dz))
        print(f"h={h:g} loop error={err:.7f}, hard derivative error={graderr:.7f}")
        if prev is not None:
            assert err < .65*prev[0] and graderr < .4*prev[1]
        prev=err,graderr


def rare_filter():
    # X is a symmetric sign, Y=Z+eps*X; conditional mean = tanh(eps*Y).
    nodes,weights=hermgauss(64)
    for eps in (.2,.1,.05):
        optimum=np.sqrt(weights@np.tanh(eps*(eps+np.sqrt(2)*nodes))**2/np.sqrt(np.pi))
        pplus,pminus=ndtr(eps-4),ndtr(-eps-4)
        prob=(pplus+pminus)/2
        rare=(pplus-pminus)/(2*np.sqrt(prob*(1-prob)))
        assert 0<rare<optimum<=1.01*eps
        print(f"eps={eps} rare normalized overlap={rare:.7f} optimum={optimum:.7f}")


if __name__=='__main__':
    for shape in [(2,2,2),(3,3,3),(3,2,4)]:
        rank_and_loop(shape)
    rare_filter()
