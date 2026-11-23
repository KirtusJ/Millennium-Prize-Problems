"""Measure the moving-vacuum coarse/fine pairing on a binary-tetrahedral two-loop graph."""
from itertools import product
from pathlib import Path
import json
import runpy

import numpy as np


multiply = runpy.run_path(str(Path(__file__).resolve().parents[1]/"transfer_check.py"))["tetra_product"]


def detour_supports(side, mesh):
    """Find every magnetic face with the required center parities on a periodic cube."""
    def shift(site, axis, step=1):
        return tuple((v+step)%side if j==axis else v for j,v in enumerate(site))

    def face(site, a, b):
        return frozenset(((site,a), (site,b), (shift(site,a),b), (shift(site,b),a)))

    catalog = {face(v,a,b) for v in product(range(side),repeat=3) for a,b in ((0,1),(0,2),(1,2))}
    assert len(catalog) == 3*side**3
    boundary = set()
    for j in range(mesh):
        boundary.update((((j,0,0),0), ((j,mesh,0),0), ((0,j,0),1), ((mesh,j,0),1)))
    detours = set()
    for v,axis in boundary:
        p = face(v, axis, 2)
        bent = frozenset(boundary ^ p)
        assert len(bent) == 4*mesh+2 and (bent ^ boundary) in catalog
        # There is a horizontal edge omitted by the entire coarse skeleton at z=1.
        assert any(coord[2] == 1 and orient != 2 for coord,orient in bent)
        # Reconstruct the detour as a single closed loop from its edge set.
        adjacent = {}
        for site, orient in bent:
            end = shift(site,orient)
            adjacent.setdefault(site,set()).add(end)
            adjacent.setdefault(end,set()).add(site)
        assert all(len(nbr) == 2 for nbr in adjacent.values())
        first = next(iter(adjacent))
        seen, queue = {first}, [first]
        while queue:
            new = adjacent[queue.pop()] - seen
            seen.update(new)
            queue.extend(new)
        assert len(seen) == len(bent)
        detours.add(bent)
    assert len(detours) == 4*mesh


def check_group(g, length=8):
    group = [tuple(2*s if j == i else 0 for j in range(4)) for i in range(4) for s in (1,-1)]
    group += list(product((-1,1), repeat=4))
    size = len(group)
    index = {x:i for i,x in enumerate(group)}
    mul = np.array([[index[multiply(x,y)] for y in group] for x in group])
    inv = np.array([index[(a,-x,-y,-z)] for a,x,y,z in group])
    center = np.array([v[0]/2 for v in group])
    weight = np.exp(g*center)
    weight /= weight.sum()
    q = float(weight @ center)
    # delta[new,old] is the left multiplier that takes old into new.
    delta = mul[:, inv]
    one = weight[delta]
    identity = index[(2,0,0,0)]
    long_arm = np.linalg.matrix_power(one, length-1)[:, identity]
    short_arm = np.linalg.matrix_power(one, 3)[:, identity]
    transfer = np.zeros((size**2, size**2))
    for v in range(size):
        left_increment = mul[inv[v], delta]
        transfer += weight[v]*np.kron(long_arm[left_increment], short_arm[left_increment])
    assert np.max(abs(transfer.sum(axis=0)-1)) < 2e-14
    assert np.max(abs(transfer-transfer.T)) < 2e-14
    coarse = np.repeat(2*center, size)
    detour = 2*center[delta].reshape(-1)  # Tr(a b^-1), after the common first link cancels
    magnetic = np.tile(center, size)
    r, u = q**length, q**(length+2)
    assert np.max(abs(transfer @ coarse - r*coarse)) < 2e-13
    assert np.max(abs(transfer @ detour - u*detour)) < 2e-13
    assert abs(np.mean(detour*magnetic*coarse)-0.25) < 1e-14
    marginal = np.linalg.matrix_power(one, 4)

    def pairings(b):
        # The spatial interaction is on the short face. Its actual vacuum lifts from that face.
        short_weight = np.exp(b*center/2)
        eigs, modes = np.linalg.eigh(short_weight[:,None]*marginal*short_weight[None,:])
        omega = np.tile(modes[:,-1], size)
        if omega[0] < 0:
            omega *= -1
        assert np.min(omega) > 0
        half_weight = np.exp(b*magnetic/2)
        sym = half_weight[:, None]*transfer*half_weight[None,:]
        assert np.max(abs(sym @ omega - eigs[-1]*omega)) < 2e-13
        vacuum = omega**2
        vacuum /= vacuum.sum()
        rows = vacuum.reshape(size,size)
        conditional = (rows*detour.reshape(size,size)).sum(axis=1)/rows.sum(axis=1)
        # The conditional mean is constant on the conjugacy class of each coarse holonomy.
        for a in range(size):
            assert np.max(abs(conditional[mul[mul[:,a],inv]]-conditional[a])) < 1e-12
        detail = detour - np.repeat(conditional, size)
        assert np.max(abs((rows*detail.reshape(size,size)).sum(axis=1))) < 1e-14
        obs = omega*(coarse - vacuum @ coarse)
        result = {}
        for n in range(1,4):
            obs = (sym @ obs)/eigs[-1]
            if n in (1,3):
                result[n] = float((vacuum*detail) @ (obs/omega))
        return result

    step = 0.002
    def differences(h):
        plus, minus = pairings(h), pairings(-h)
        return {n:(plus[n]-minus[n])/(2*h) for n in plus}
    large, small = differences(step), differences(step/2)
    values = []
    for n in (1,3):
        measured = (4*small[n]-large[n])/3
        predicted = r**n*q**2*(1-q**(2*n))/(4*(1-q**4))
        assert abs(measured-predicted) < 2e-10 and predicted > 0
        values.append({"n":n,"measured":round(measured,12),"formula":round(predicted,12)})
    return {"g":g,"link_ratio":round(q,10),"states":size**2,"length":length,"pairings":values}


def time_limit():
    # Integrate the actual SU(2) class density; subtract its peak exponent for stability.
    nodes, weights = np.polynomial.legendre.leggauss(160)
    angle = (nodes+1)*np.pi/2
    cosine = np.cos(angle)
    kappa, s, k = 2, 0.25, 8
    ef, eh, ep = 3*k/(2*kappa), 3*(k+2)/(2*kappa), 6/kappa
    target = kappa/24*np.exp(-s*ef)*(1-np.exp(-3*s/kappa))
    times = (nodes+1)*s/2
    duhamel = s/2*(weights @ np.exp(-(s-times)*eh-times*ef))
    from_hamiltonian = (duhamel-(np.exp(-s*ef)-np.exp(-s*eh))/ep)/4
    assert abs(target-from_hamiltonian) < 1e-13
    unnormalized = duhamel/4
    assert abs(unnormalized-2*from_hamiltonian) < 1e-13
    slopes = []
    for g in (16,64,256,1024):
        dt, n = kappa/g, g//8
        assert n*dt == s
        density = weights*np.sin(angle)**2*np.exp(g*(cosine-1))
        q = (density @ cosine)/np.sum(density)
        slopes.append(dt*q**(k*n+2)*(1-q**(2*n))/(4*(1-q**4)))
    errors = [abs(x-target) for x in slopes]
    assert all(y < x for x,y in zip(errors, errors[1:])) and errors[-1] < 0.001*target
    return {"electric_slopes":[round(float(x),10) for x in slopes],
            "hamiltonian_slope":round(float(from_hamiltonian),10),
            "slope_without_vacuum_term":round(float(unnormalized),10)}


if __name__ == "__main__":
    for side, mesh in ((8,2), (12,2), (16,4)):
        detour_supports(side, mesh)
    print(json.dumps({"pairings":[check_group(g) for g in (2.2,4.0,6.0)],
                      "physical_time":time_limit()}, indent=2))
