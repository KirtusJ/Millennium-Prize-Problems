"""Geometric, character-integral and transfer controls for the lowest Wilson shell."""
import itertools
import json
from pathlib import Path

import numpy as np
from scipy.special import iv, ive

from cube_bounds import certified_intervals


def shift(point, direction, size=None):
    value = list(point)
    value[direction] += 1
    if size:
        value[direction] %= size
    return tuple(value)


def square(x, i, j):
    y, z = shift(x, i), shift(x, j)
    return (x, y, shift(y, j), z)


def sides(face):
    return {tuple(sorted((a, b))) for a, b in zip(face, face[1:] + face[:1])}


def corner_masks():
    zero = (0, 0, 0)
    corner = [sides(square(zero, i, j)) for i, j in itertools.combinations(range(3), 2)]
    outer = sorted(set.union(*corner) - {tuple(sorted((zero, shift(zero, i)))) for i in range(3)},
                   key=lambda edge: (min(edge, key=sum), max(edge, key=sum)))
    masks = {0}
    for x in itertools.product(range(-1, 2), repeat=3):
        for i, j in itertools.combinations(range(3), 2):
            edges = sides(square(x, i, j))
            if edges not in corner:
                masks.add(sum(1 << k for k, edge in enumerate(outer) if edge in edges))
    assert sorted(masks) == [0, 1, 2, 3, 4, 8, 12, 16, 32, 48]
    return sorted(masks)


def cycles(size):
    graph = {}
    for x in itertools.product(range(size), repeat=3):
        for axis in range(3):
            y = shift(x, axis, size)
            edge = (x, axis)
            graph.setdefault(x, []).append((y, edge))
            graph.setdefault(y, []).append((x, edge))
    found = set()
    for root in graph:
        def visit(x, seen, path):
            for y, edge in graph[x]:
                if edge in path:
                    continue
                if y == root:
                    found.add(frozenset(path + [edge]))
                elif y not in seen and len(path) + 1 < min(size, 4):
                    visit(y, seen | {y}, path + [edge])
        visit(root, {root}, [])
    return len(found)


def cube_faces():
    data = []
    for axis in range(3):
        j, k = 1 << ((axis+1) % 3), 1 << ((axis+2) % 3)
        for high in (False, True):
            x = (1 << axis) if high else 0
            a, b = (j, k) if high else (k, j)
            data.extend((x, x|a, x|a|b, x|b))
    return bytes(data)


def periodic_symbol(size):
    sites = list(itertools.product(range(size), repeat=3))
    ix = {x: k for k, x in enumerate(sites)}
    n = len(sites)
    incidence = np.zeros((n, 3*n))
    adjacency = np.zeros((n, n))
    for x, k in ix.items():
        for j in range(3):
            y = ix[shift(x, j, size)]
            incidence[k, 3*k+j] = incidence[k, 3*y+j] = 1
            adjacency[k,y] = adjacency[y,k] = 1
    face_graph = incidence.T @ incidence - 2*np.eye(3*n)
    assert np.all(face_graph.sum(axis=1) == 10)
    assert np.array_equal(incidence @ face_graph - 10*incidence,
                          (adjacency-6*np.eye(n)) @ incidence)
    shell = [4+2*np.sum(np.cos(2*np.pi*np.array(p)/size)) for p in sites] + [-2.]*(2*n)
    assert np.max(np.abs(np.linalg.eigvalsh(face_graph)-np.sort(shell))) < 1e-11
    return int(np.sum(np.abs(np.array(shell)+2) < 1e-10))


def ring_transfer(beta_s):
    # An open four-link square: all irreducible characters are physical and orthonormal.
    theta = np.pi*np.arange(1, 129)/129
    w = (2/129) * np.square(np.sin(theta)) * np.exp(beta_s*np.cos(theta))
    chi = np.sin(np.arange(1, 10)[:, None]*theta)/np.sin(theta)
    gram = (chi*w) @ chi.T
    variance = gram[1,1]/gram[0,0]-(gram[0,1]/gram[0,0])**2
    errors = []
    for beta_t in (0.4, 0.2, 0.1):
        root = (iv(np.arange(1, 10),beta_t)/iv(1,beta_t))**2
        eigen = np.linalg.eigvalsh(root[:,None]*gram*root)
        value = eigen[-2]/(eigen[-1]*root[1]**2)
        errors.append(abs(value-variance))
    assert errors[0] > errors[1] > errors[2] and errors[-1] < 1e-6
    return {"variance": float(variance), "absolute_errors": errors}


def cube_character(beta):
    # Common exponential factor cancels. Recurrences give derivatives before scaling.
    d = np.arange(1, int(14*np.sqrt(beta+1))+14)
    vals = ive(d,beta)
    dlog = ive(d+1,beta)/vals+(d-1)/beta
    # I_d satisfies the modified Bessel equation.
    ddlog = 1+(d*d-1)/beta**2 - 3*dlog/beta - dlog**2
    weights = d*d*(vals/vals.max())**6
    weights /= weights.sum()
    off = 4*np.dot(weights,(dlog-np.dot(weights,dlog))**2)
    transverse = 4*np.dot(weights,ddlog)
    return float(off), float(transverse), float(transverse+6*off)


def open_projector(length):
    cells = list(itertools.product(range(length), repeat=3))
    faces = sorted({(y, j) for x in cells for j in range(3) for y in (x, shift(x, j))})
    ix = {f: k for k, f in enumerate(faces)}
    incidence = np.zeros((len(cells), len(faces)))
    for k, x in enumerate(cells):
        for j in range(3):
            incidence[k, ix[x,j]] = -1
            incidence[k, ix[shift(x,j),j]] = 1
    green = np.linalg.inv(incidence@incidence.T)
    projection = np.eye(len(faces))-incidence.T@green@incidence
    weak = 6*np.square(projection)
    assert np.max(np.abs(weak.sum(axis=1)-6*np.diag(projection))) < 1e-12
    exterior = [ix[((0,0,0),j)] for j in range(3)]
    trial = weak[np.ix_(exterior,exterior)].sum()/3
    top = np.linalg.eigvalsh(weak)[-1]
    assert trial >= 108/25-1e-12 and trial <= top+1e-12 and top <= 5+1e-12
    return [float(green[0,0]), float(trial), float(top)]


def joint_mobility():
    q = np.array([1., -.5, .3])
    results = {}
    for ratio in (0., .5, 1., 3.):
        predicted = 1+4*ratio**2/3
        errors = []
        for n in (10,20,40):
            t = 2*np.cos(q/(2*n))
            x,y,z = t
            edge = np.array([[0,z,y],[z,0,x],[y,x,0]])
            cube = np.outer(t,t)
            total = cube+edge@edge
            target = 2*cube
            np.fill_diagonal(target,t@t)
            assert np.max(np.abs(total-target)) < 1e-12
            generator = cube-12*np.eye(3)+ratio**2*(edge@edge-16*np.eye(3))
            eigen = np.linalg.eigvalsh(generator)[-1]
            errors.append(abs(-eigen*n**2/(q@q)-predicted))
        assert errors[2] < errors[1] < errors[0] and errors[2] < .002
        results[str(ratio)] = [predicted, errors[-1]]
    return results


PROOF = '''/-- The edge masks of every additional square meeting the exposed corner hexagon. -/
def faceMask : Fin 10 → Nat := ![{masks}]

set_option maxRecDepth 8000 in
set_option maxHeartbeats 2000000 in
theorem coreCompletion : ∀ a b c : Fin 10,
    faceMask a ||| faceMask b ||| faceMask c = 63 →
    (faceMask a = 3 ∨ faceMask b = 3 ∨ faceMask c = 3) ∧
    (faceMask a = 12 ∨ faceMask b = 12 ∨ faceMask c = 12) ∧
    (faceMask a = 48 ∨ faceMask b = 48 ∨ faceMask c = 48) := by decide
'''


def run(out):
    masks = corner_masks()
    counts = [cycles(n) for n in range(2, 7)]
    assert counts == [12, 27, 240, 375, 648]
    flat = [periodic_symbol(n) for n in (4, 5)]
    assert flat == [129, 250]
    small = [cube_character(b)[0]/(b/4)**4 for b in (0.4, 0.2, 0.1)]
    assert abs(small[2]-1) < abs(small[1]-1) < abs(small[0]-1) < .1
    large = {str(b): [b*b*x for x in cube_character(b)] for b in (20, 100, 500)}
    assert np.max(np.abs(np.array(large["500"])-[1/6,4,5])) < .02
    result = {"mobility_prediction_and_n40_error": joint_mobility(), "certified_cube_transfer": certified_intervals(), "corner_masks": masks, "open_G_trial_top": {str(n):open_projector(n) for n in range(1,5)}, "girth_counts_L2_to_L6": counts,
              "flat_multiplicity_L4_L5": flat, "one_square": ring_transfer(1.3),
              "cube_off_over_z4": small, "cube_scaled_off_transverse_scalar": large}
    (out/"geometry").write_text(PROOF.format(masks=",".join(map(str,masks))))
    (out/"counts.bin").write_bytes(cube_faces())
    (out/"checks.json").write_text(json.dumps(result,indent=2)+"\n")
