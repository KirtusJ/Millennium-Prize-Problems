"""Bound Bessel ratios by rational intervals and enumerate the smallest SU(2) torus."""
from fractions import Fraction as Q
from itertools import product
from math import factorial, sqrt
import json


def bessel(order, coupling):
    """Enclose the positive Taylor series of I_order using a geometric tail."""
    half = Q(coupling, 2)
    term = half**order / factorial(order)
    total = term
    for k in range(1, 65):
        ratio = half**2 / (k*(k+order))
        term *= ratio
        total += term
    next_ratio = half**2 / (65*(65+order))
    assert next_ratio < 1
    return total, total + term*next_ratio/(1-next_ratio)


def ratio(top, bottom, coupling):
    lo, hi = bessel(top, coupling)
    base_lo, base_hi = bessel(bottom, coupling)
    scale = 10**20
    return Q((scale*lo/base_hi).__floor__(), scale), Q((scale*hi/base_lo).__ceil__(), scale)


def thick_slab(mesh, n, q, rho):
    """Square both positive comparisons in (3). Use upper endpoints throughout."""
    k = 4*mesh
    factor = 2*(1 + 1/(n*(1-q**4)))
    return max(5*mesh*(factor*q**(mesh*n)/(1-q**(5*mesh*n)))**2,
               k*(factor*rho**((k-2)*n)/(1-(q**k*rho**(k-2))**n))**2)


def cutoffs(mesh, n, coupling):
    qlo, qhi = ratio(2,1,coupling)
    k0 = 4*mesh
    witness = n*qlo**(k0*n)/(2*(1-qlo**(k0*n)))
    def excluded(k, electric):
        return k*((n + 1/(1-qhi**4))*electric**n/(1-electric**n))**2 < witness**2
    k = k0
    while not excluded(k+1, qhi**(k+1)):
        k += 1
    j = 1
    while not excluded(k, ratio(j+2,1,coupling)[1]**(mesh-1)):
        j += 1
    return k,j


def four_cycles(side):
    steps = tuple(product(range(3), (-1,1)))
    cycles = set()
    for start in product(range(side), repeat=3):
        for walk in product(steps, repeat=4):
            path = [start]
            for axis, direction in walk:
                pos = list(path[-1])
                pos[axis] = (pos[axis]+direction)%side
                path.append(tuple(pos))
            if path[0] == path[-1] and len(set(path[:-1])) == 4:
                cycles.add(frozenset(tuple(sorted(edge)) for edge in zip(path[:-1],path[1:])))
    winding = 0
    for loop in cycles:
        dims = {i for a,b in loop for i in range(3) if a[i]!=b[i]}
        assert len(dims) in (1,2)
        winding += len(dims)==1
    return len(cycles)-winding, winding


def loop_norm(j, mesh, n, ratios, corners):
    # Two neighboring common edges carry the same channel along their shared path.
    k = 4*mesh
    q, qj = ratios[1], ratios[j]
    r = qj**k
    lam = q**4
    def face(d):
        value = 0.
        for label in (j-1,j+1):
            u = qj**(k-d) * q**(4-d) * ratios[label]**d
            mult = (u-lam*r)/(1-lam)*sum(u**i*r**(n-1-i) for i in range(n))
            value += (label+1)/(8*(j+1))*mult**2/(1-u**n)
        return value
    return sqrt(((4*k-2*corners)*face(1)+corners*face(2))/(1-r**n))


def plot_spec():
    mesh, coupling = 2, 2
    ratios = [1.,float(sum(ratio(2,1,coupling))/2),float(sum(ratio(3,1,coupling))/2)]
    series=[]
    for name,corners in (("Coarse square",4),("Straight winding",0)):
        points=[]
        for n in range(1,9):
            reference=n*ratios[1]**(8*n)/2
            value=loop_norm(1,mesh,n,ratios,corners)/reference
            y=str(Q(round(value*10**6),10**6))
            points.append([n,y,y])
        series.append({"name":name,"data":points})
    return {"title":"First magnetic response of two four-edge loops","provenance":"model",
            "source":"Electric SU(2) Wilson transfer, g=2, mesh=2, side=8. Six decimal places.",
            "x_label":"time lag n","y_label":"norm divided by n q^(8n) / 2",
            "x_domain":[1,8],"y_domain":[0,"6/5"],"series":series}


def run():
    certificates = []
    for coupling,mesh in product((1,2,4,8), (2,3)):
        qlo,qhi = ratio(2,1,coupling)
        rlo,rhi = ratio(3,2,coupling)
        n = 1
        while thick_slab(mesh,n,qhi,rhi) >= 1:
            n += 1
        if n > 1:
            assert thick_slab(mesh,n-1,qlo,rlo) >= 1
        certificates.append(dict(g=coupling,mesh=mesh,first_certified_lag=n))
    # The graph and connected supports are enumerated on the coarse torus of side four.
    # In this example the certified edge cutoff leaves only fundamental or higher-spin four-cycles.
    coupling, mesh, n = 2,2,4
    k, jmax = cutoffs(mesh,n,coupling)
    assert k == 8
    squares, winds = four_cycles(4)
    assert (squares,winds)==(192,48)
    ratios = [1.] + [float(sum(ratio(j+1,1,coupling))/2) for j in range(1,jmax+2)]
    sectors = [(loop_norm(j,mesh,n,ratios,c),j,c) for j,c in product(range(1,jmax+1),(0,4))]
    sectors.sort(reverse=True)
    assert sectors[0][1:] == (1,4) and sectors[1][1:]==(1,0)
    return {"sufficient_lags":certificates, "smallest_torus":{"g":coupling,"n":n,"mesh":mesh,
            "edge_cutoff":k, "spin_index_cutoff":jmax, "squares":squares,"windings":winds,
            "connected_label_blocks":(squares+winds)*jmax,"largest_norm":sectors[0][0],
            "winding_norm":sectors[1][0],"largest_higher_spin":max(v for v,j,c in sectors if j>1)}}


if __name__=="__main__":
    print(json.dumps(run(),indent=2))
