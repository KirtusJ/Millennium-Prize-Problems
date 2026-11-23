"""Finite compact-link controls for the spatial heat trace."""
from itertools import product
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh, eigvalsh, expm
from scipy.special import ive


IDENTITY = np.eye(2)
GENERATORS = 1j * np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])


def random_link(rng):
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    return q[0]*IDENTITY + np.einsum("i,ijk->jk", q[1:], GENERATORS)


def cube(side, rng):
    vertices = list(product(range(side), repeat=3))
    numbers = {vertex: i for i, vertex in enumerate(vertices)}
    edges = {}
    for i, vertex in enumerate(vertices):
        for axis in range(3):
            neighbor = list(vertex)
            neighbor[axis] += 1
            if tuple(neighbor) in numbers:
                edges[i, numbers[tuple(neighbor)]] = random_link(rng)
    return vertices, edges


def block(i):
    return slice(2*i, 2*i+2)


def laplacian(count, links, *, dirichlet):
    matrix = np.zeros((2*count, 2*count), dtype=complex)
    for (i, j), u in links.items():
        matrix[block(i), block(j)] = -u
        matrix[block(j), block(i)] = -u.conj().T
        for k in (i, j):
            matrix[block(k), block(k)] += IDENTITY
    if dirichlet:
        np.fill_diagonal(matrix, 6)
    return matrix


def cycle(links, sites):
    result = IDENTITY
    for i, j in zip(sites, sites[1:]+sites[:1]):
        result = result @ (links[i,j] if (i,j) in links else links[j,i].conj().T)
    return result


def gradient_controls():
    rng = np.random.default_rng(20261123)
    vertices, links = cube(2, rng)
    count = len(vertices)
    b, s = 0.56, 0.13
    matrix = laplacian(count, links, dirichlet=True) / b**2
    K = expm(-s*matrix)
    rotations = [random_link(rng) for _ in vertices]
    transformed = {(i,j): rotations[i] @ u @ rotations[j].conj().T
                   for (i,j), u in links.items()}
    gauge_error = abs(np.trace(K) -
                      np.exp(-s*eigvalsh(laplacian(count, transformed, dirichlet=True)/b**2)).sum())
    gradient2, difference, worst_edge, summed_energy = 0., 0., 0., 0.
    for (i,j), u in links.items():
        diff = np.zeros((2, 2*count), dtype=complex)
        diff[:, block(i)], diff[:, block(j)] = IDENTITY, -u
        energy = np.trace(diff @ K @ diff.conj().T).real
        summed_energy += energy
        mass = np.trace(K[block(j), block(j)]).real
        for X in GENERATORS:
            deriv = np.zeros_like(diff)
            deriv[:, block(j)] = -X @ u
            val = -2*s/b**2*np.trace(deriv @ K @ diff.conj().T).real
            dt = 1e-4
            vals = []
            for sign in (-1, 1):
                varied = links.copy()
                varied[i,j] = (math.cos(dt)*IDENTITY + sign*math.sin(dt)*X) @ u
                vals.append(np.exp(-s*eigvalsh(laplacian(count, varied, dirichlet=True)/b**2)).sum())
            difference = max(difference, abs((vals[1]-vals[0])/(2*dt)-val))
            worst_edge = max(worst_edge, val**2/(4*s*s/b**4*mass*energy))
            gradient2 += val**2
    full_energy = np.trace(matrix @ K).real * b**2
    if (difference > 2e-9 or gauge_error > 2e-12 or not 1e-10 < worst_edge <= 1+1e-12
            or not 0 < summed_energy < full_energy or not 0 < gradient2 < 96*4*count*b**4/s**2):
        raise AssertionError(("covariant derivative", difference, worst_edge))
    root_loop = cycle(links, [0, 2, 6, 4])
    defect = 2 - np.trace(root_loop).real
    minimum = eigvalsh(laplacian(count, links, dirichlet=False))[0]
    if minimum < defect/256 or minimum <= 0:
        raise AssertionError("small cube anchor")
    return {"generators_tested": 3*len(links), "max_derivative_error": difference,
            "gauge_error": float(gauge_error), "largest_edge_CS_ratio": worst_edge,
            "gradient_squared": gradient2, "dirichlet_boundary_energy": full_energy-summed_energy,
            "cube_gap": minimum, "one_plaquette_floor": defect/256}


def coarse_controls():
    rng = np.random.default_rng(17)
    vertices, links = cube(4, rng)
    index = {v: i for i, v in enumerate(vertices)}
    loops, chosen = [], set()
    for x,y,z in product((0, 2), repeat=3):
        face = [index[row] for row in ((x,y,z),(x+1,y,z),(x+1,y+1,z),(x,y+1,z))]
        assert all(i not in chosen for i in face)
        chosen.update(face)
        loops.append(cycle(links, face))
    radii2 = [2-np.trace(u).real for u in loops]
    exact = eigvalsh(laplacian(len(vertices), links, dirichlet=False))[0]
    r2 = float(np.median(sorted(radii2)[3:5]))
    floor = 1/(5*4**2+4*256/r2)
    assert exact >= floor and sum(value >= r2 for value in radii2) >= 4
    # An adjoint rotation about a single axis fixes that axis. Two half
    # turns about orthogonal axes have no shared fixed vector.
    rx, ry = np.diag([1,-1,-1]), np.diag([-1,1,-1])
    def gram(rotation):
        defect = np.eye(3)-rotation
        return defect.T @ defect
    adjoint = [eigvalsh(gram(rx))[0], eigvalsh(gram(rx)+gram(ry))[0]]
    assert adjoint == [0, 4]
    return {"small_cubes": len(loops), "large_cube_gap": exact,
            "large_cube_floor": floor, "adjoint_one_two_loop_minima": adjoint}


def conditional_controls():
    rows = []
    for R in (0, 1, 6, 60, 6000):
        norm = 1 if R == 0 else 2*ive(1,R)/R
        cap = 1/(8*math.sqrt(1+R))
        angle = 2*math.asin(cap/2)
        prob = quad(lambda t: 2/math.pi * math.sin(t)**2 *
                    math.exp(-2*R*math.sin(t/2)**2) / norm, 0, angle)[0]
        if not 0 < prob < 1/16 or 1/norm > 20*(1+R)**1.5:
            raise AssertionError("one-link cap")
        rows.append([R, prob])
    return rows


def original_wilson_conditionals():
    # Rebuild the complete four-dimensional Wilson exponent and independently
    # recover the six incident staples by evaluating four quaternion directions.
    rng = np.random.default_rng(41123)
    side = 3
    sites = list(product(range(side), repeat=4))
    links = {(x, d): random_link(rng) for x in sites for d in range(4)}
    coefficients = {(i,j): (0.7 if i == 0 else 1.8) for i in range(4) for j in range(i+1, 4)}
    def move(x, i, sign=1):
        return tuple((z+sign) % side if j == i else z for j,z in enumerate(x))
    def face(x, i, j):
        forward = links[x,i] @ links[move(x,i),j]
        back = links[x,j] @ links[move(x,j),i]
        return np.trace(forward @ back.conj().T).real / 2
    def action():
        return sum(beta*face(x,i,j) for x in sites for (i,j),beta in coefficients.items())
    def incident(x, e):
        return sum(beta*(face(x,i,j)+face(move(x,j if i == e else i,-1),i,j))
                   for (i,j),beta in coefficients.items() if e in (i,j))
    errors, norms = [], []
    initial = action()
    directions = [IDENTITY, *GENERATORS]
    for vertex in [sites[0], sites[-1], sites[17]]:
        for axis in (1,2,3):
            key = (vertex, axis)
            original = links[key]
            original_value = incident(*key)
            coords = []
            for direction in directions:
                links[key] = direction
                coords.append(incident(*key))
            q = rng.normal(size=4)
            q /= np.linalg.norm(q)
            links[key] = sum(q[i]*directions[i] for i in range(4))
            errors.append(abs(action()-initial - (np.dot(coords,q)-original_value)))
            norms.append(np.linalg.norm(coords))
            links[key] = original
    if max(errors) > 3e-12 or max(norms) > 4*1.8+2*0.7:
        raise AssertionError(("original 4D conditional", errors, norms))
    return {"links": len(errors), "full_action_residual":max(errors), "largest_staple":max(norms)}


def exact_wilson_square():
    # Four spatial links around one isolated SU(2) Wilson face. Three Haar
    # integrals reduce to one class angle. The Neumann circuit has twisted
    # Fourier eigenvalues 4 sin^2((theta+2 pi j)/8) in each Cartan sector.
    rows = []
    for b in (0.25, 0.125, 0.0625, 0.03125):
        beta, s = math.log(1/b), 1.0
        norm = 2*ive(1, beta)/beta
        def integrand(theta, power):
            mass = 2/math.pi * math.sin(theta)**2 * math.exp(-2*beta*math.sin(theta/2)**2)/norm
            trace = 2*sum(math.exp(-4*s/b**2 * math.sin((theta+2*math.pi*j)/8)**2)
                          for j in range(4))
            return mass*trace**power
        mean, second = [quad(integrand, 0, math.pi, args=(p,), epsabs=2e-13)[0] for p in (1, 2)]
        rows.append([b, mean, second/mean**2])
    if not all(0 < b[1] < a[1] and b[2] > a[2] > 1 for a,b in zip(rows,rows[1:])):
        raise AssertionError("one-square group integral")
    return rows


def outside_test():
    # Extreme test supported entirely on the rare inside state. The supremum
    # over exterior unit L2 tests is the norm of its conditional expectation.
    q = 1/64
    outside = np.array([0.4, 0.6])
    event = np.array([q/4, q])
    amps = np.array([2., 1.])
    amps /= math.sqrt(np.dot(outside, event*amps**2))
    optimal = math.sqrt(np.dot(outside, (event*amps)**2))
    # Same marginal rarity, now revealed by the outside coordinate itself.
    # The two unit test vectors coincide and their correlation is exactly one.
    marginal_only = q*(1/math.sqrt(q))**2
    assert 0 < optimal <= math.sqrt(q) and marginal_only == 1
    return {"conditional_norm": optimal, "conditional_ceiling": math.sqrt(q),
            "unconditional_only_correlation": marginal_only}


def rare_cube_trial():
    rng = np.random.default_rng(441)
    rows = []
    for m in (2, 3, 4):
        vertices, links = cube(m, rng)
        eps = 1/m
        for edge in links:
            axis = rng.normal(size=3)
            axis /= np.linalg.norm(axis)
            angle = eps*rng.uniform(0, 1)
            links[edge] = math.cos(angle)*IDENTITY + math.sin(angle)*np.einsum("i,ijk->jk", axis, GENERATORS)
        trial = np.zeros(2*len(vertices), dtype=complex)
        for i, v in enumerate(vertices):
            trial[2*i] = math.prod(math.sin(math.pi*(coord+1)/(m+1)) for coord in v)
        trial /= np.linalg.norm(trial)
        matrix = laplacian(len(vertices), links, dirichlet=True)
        rayleigh = np.vdot(trial, matrix @ trial).real
        minimum = eigvalsh(matrix)[0]
        upper = 2*(6-6*math.cos(math.pi/(m+1)))+6*eps**2
        if not minimum <= rayleigh+1e-12 or not rayleigh <= upper:
            raise AssertionError(("rare cube trial", minimum, rayleigh, upper))
        rows.append([m, minimum, rayleigh, upper])
    return rows


def smooth_fields():
    # Dirichlet lattice cube with a fixed smooth Abelian magnetic field in SU(2).
    # The two Cartan charges have equal heat traces and the third axis separates.
    rows = []
    for n in (6, 12, 24):
        b, s, field = 1/(n+1), 0.04, 18.
        two = np.eye(n*n, dtype=complex)*4
        for x,y in product(range(n), repeat=2):
            i = n*x+y
            if x+1 < n:
                two[i,i+n] = two[i+n,i] = -1.
            if y+1 < n:
                two[i,i+1] = -np.exp(1j*field*(x+1)*b*b)
                two[i+1,i] = two[i,i+1].conjugate()
        one = (2-2*np.cos(math.pi*np.arange(1,n+1)/(n+1)))/b**2
        one_trace = np.exp(-s*one).sum()
        flat = 2*one_trace**3
        charged = 2*one_trace*np.exp(-s*eigvalsh(two)/b**2).sum()
        if not 0 < charged < 0.999*flat:
            raise AssertionError("flat/curved separation")
        rows.append([n, flat, charged, charged/flat])
    return rows


def run(out: Path):
    results = {"SU2_links": gradient_controls(), "Neumann_blocks": coarse_controls(),
               "conditional_small_ball": conditional_controls(), "smooth_fields": smooth_fields(),
               "original_Wilson": original_wilson_conditionals(), "Wilson_square": exact_wilson_square(),
               "rare_cube": rare_cube_trial(), "outside": outside_test()}
    (out/"checks.json").write_text(json.dumps(results, indent=2)+"\n")

    # Read the geometry of the full unit cube and its lower face. The host
    # fragment and the native certificate are derived independently from it.
    vertices = list(product((0, 1), repeat=3))
    distance = max(sum(v) for v in vertices)
    face = [v for v in vertices if v[2] == 0]
    order = bytes([len(vertices), distance, len(face)])
    (out/"counts.bin").write_bytes(order)
    a = 2*len(vertices)*len(face)
    c = 2*len(vertices)*distance
    (out/"geometry").write_text(
        "theorem cellAnchor {r mass E : ℝ} (unit : r ≤ 4)\n"
        f"    (hE : 0 ≤ E) (v : r*mass ≤ {a}*E+{c}*r*E) : r*mass ≤ {a+4*c}*E := by\n"
        "  have h := mul_le_mul_of_nonneg_right unit hE\n"
        "  linarith\n")
