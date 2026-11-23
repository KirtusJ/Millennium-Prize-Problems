"""Recompute periodic group integrals, quaternion scores and an uncapped physical rotor."""
from itertools import product
from pathlib import Path
import json
import math

import numpy as np
from scipy.linalg import eigh
from scipy.special import ive


def boundary_check():
    # The four-link spatial cycle has one gauge-invariant flux. At time period
    # two there are two distinct, independent crossing sets on the same slices.
    configs = np.array(list(product((-1, 1), repeat=4)))
    gauges = configs*np.roll(configs, -1, axis=1)
    beta = 0.8
    r = math.tanh(beta)
    norm = math.cosh(beta)**4
    k = np.exp(beta*(configs @ configs.T))/norm
    projected = sum(np.exp(beta*((configs*h) @ configs.T))/norm for h in gauges)/len(gauges)
    # Explicit original integrals for both temporal sets, at fixed spatial pair.
    z = 0.
    loop = 0.
    for x in configs:
        for y in configs:
            seam = np.exp(beta*(gauges @ (x*y)))/norm
            z += seam.mean()**2
            # Insert the product of both temporal links at vertex zero.
            loop += np.mean(configs[:,0]*seam)**2
    z /= len(configs)**2
    loop /= len(configs)**2
    expected = 1+r**8
    naive = np.trace((k/16) @ (k/16))
    gram_min = np.linalg.eigvalsh(projected*projected)[0]
    if abs(z-expected) > 1e-12 or abs(loop) > 1e-14 or gram_min < -1e-12:
        raise AssertionError("periodic projection or reflection")
    if abs(naive-(1+r*r)**4) > 1e-12 or naive < z+0.1:
        raise AssertionError("missing holonomy control")
    # G4's separate open-chain example, with nongauge-invariant end weights.
    lam = 0.6
    open_z = np.mean([math.exp(beta*u*v*h*k+lam*(u+v))
                      for u,v,h,k in product((-1, 1), repeat=4)])
    fixed = np.mean([math.exp(beta*u*v+lam*(u+v)) for u,v in product((-1, 1), repeat=2)])
    if abs(fixed-open_z-math.sinh(beta)*math.sinh(lam)**2) > 1e-12:
        raise AssertionError("end-weight adverse control")
    return {"period_two_partition": z, "unprojected_partition": naive,
            "polyakov_expectation": loop/z, "min_two_seam_gram_eigenvalue": gram_min,
            "open_nongauge_end_partition": open_z, "open_temporal_links_set_to_one": fixed}


def qmul(a, b):
    return np.concatenate([(a[0]*b[0]-np.dot(a[1:], b[1:])).reshape(1),
                           a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:], b[1:])])


def inv(a):
    return a*np.array([1, -1, -1, -1])


def move(x, d, step, sides):
    return tuple((v+(step if i==d else 0)) % sides[i] for i,v in enumerate(x))


def face(U, x, i, j):
    y = move(x, i, 1, U.shape[:4])
    z = move(x, j, 1, U.shape[:4])
    return qmul(qmul(U[x+(i,)], U[y+(j,)]), inv(qmul(U[x+(j,)], U[z+(i,)])))[0]


def active_exponent(U, x, i, g, b):
    # b = a*lambda. Differentiate the outgoing transition's left half action.
    value = g*face(U, x, i, 0)
    for j in (1, 2, 3):
        if j == i:
            continue
        value += (b/2)*(face(U, x, i, j)+face(U, move(x,j,-1,U.shape[:4]), i, j))
    return value


def electric_score(U, x, i, g, b, gamma):
    saved = U[x+(i,)].copy()
    try:
        # The active exponent is linear in this unit quaternion. Evaluations
        # on four basis elements recover its staple, including orientation.
        values = []
        for v in np.eye(4):
            U[x+(i,)] = v
            values.append(active_exponent(U,x,i,g,b))
        staple = np.asarray(values)
        phi = np.dot(staple,saved)
        return gamma*(3*phi-np.dot(staple,staple)+phi**2)
    finally:
        U[x+(i,)] = saved


def score_check():
    rng = np.random.default_rng(20261122)
    sides = (4, 2, 2, 2)
    U = rng.normal(size=sides+(4,4))
    U /= np.linalg.norm(U,axis=-1,keepdims=True)
    gauges = rng.normal(size=sides+(4,))
    gauges /= np.linalg.norm(gauges,axis=-1,keepdims=True)
    V = np.empty_like(U)
    for x in np.ndindex(sides):
        for d in range(4):
            V[x+(d,)] = qmul(qmul(gauges[x],U[x+(d,)]),inv(gauges[move(x,d,1,sides)]))
    g,b,gamma = 3.,0.7,0.25
    fd, gauge, count = 0.,0.,0
    dt = 0.00015
    for x in np.ndindex(sides):
        for i in range(1,4):
            val = electric_score(U,x,i,g,b,gamma)
            gauge = max(gauge, abs(val-electric_score(V,x,i,g,b,gamma)))
            orig = U[x+(i,)].copy()
            center = active_exponent(U,x,i,g,b)
            deriv = 0.
            for axis in range(1,4):
                delta = np.zeros(4)
                delta[0], delta[axis] = math.cos(dt), math.sin(dt)
                U[x+(i,)] = qmul(orig, delta)
                plus = active_exponent(U,x,i,g,b)
                U[x+(i,)] = qmul(orig, inv(delta))
                minus = active_exponent(U,x,i,g,b)
                deriv += (math.expm1(plus-center)+math.expm1(minus-center))/dt**2
            U[x+(i,)] = orig
            fd = max(fd, abs(val+gamma*deriv))
            count += 1
    if gauge > 1e-12 or fd > 1e-6:
        raise AssertionError((gauge,fd))
    return {"link_tests": count, "max_gauge_change": float(gauge), "max_casimir_difference": fd}


def rotor_check():
    # Full trace on the gauge-invariant four-link circuit. Verify physical
    # observables both in character basis and by ordinary radial history scores.
    size, nodes = 32, 40
    n = np.arange(size)
    gamma, lam, a = 0.25, 1.1, 0.5
    g = 1/(2*gamma*a)
    theta = np.arange(1,nodes+1)*math.pi/(nodes+1)
    x = np.cos(theta)
    weights = 2*np.sin(theta)**2/(nodes+1)
    conf = np.sin(np.outer(theta,n+1))/np.sin(theta)[:,None]
    # Gegenbauer derivative in x, including its sign.
    dchar = (x[:,None]*conf-np.cos(np.outer(theta,n+1))*(n+1))/(1-x*x)[:,None]
    coeff = (ive(n+1,g)/ive(1,g))**4
    q = a*lam/2
    M = np.exp(-q*(1-x))
    kinetic = (conf*coeff) @ conf.T
    Traw = M[:,None]*kinetic*M[None,:]
    deriv = (conf*(n*(n+2))+(3*q*x-q*q*(1-x*x))[:,None]*conf
             -2*q*(1-x*x)[:,None]*dchar)
    # O = gamma*A on one link minus 0.3 times the magnetic potential.
    OT = M[:,None]*((deriv*coeff) @ conf.T)*M[None,:]*gamma-0.3*lam*(1-x)[:,None]*Traw
    if Traw.min() <= 0:
        raise AssertionError("nonpositive radial kernel")
    score = OT/Traw
    T = Traw*np.sqrt(np.outer(weights,weights))
    N, period = 1, 6
    heat = [np.linalg.matrix_power(T,h) for h in range(period+1)]
    readings = [np.trace((score*T) @ heat[k-1] @ (score*T) @ heat[period-k-1])/np.trace(heat[period])
                for k in (N,2*N,3*N)]
    W = lam*(np.eye(size)-(np.eye(size,k=1)+np.eye(size,k=-1))/2)
    E,basis = eigh(W)
    half = (basis*np.exp(-a*E/2)) @ basis.T
    tra = (half*coeff) @ half.T
    O = gamma*np.diag(n*(n+2))-0.3*W
    def value(k):
        return np.trace(O @ np.linalg.matrix_power(tra,k) @ O @ np.linalg.matrix_power(tra,period-k))/np.trace(np.linalg.matrix_power(tra,period))
    err = max(abs(v-value(k)) for k,v in zip((1,2,3),readings))
    if err > 1e-10:
        raise AssertionError(("score and transfer disagreement",err))
    # Uncapped graph-norm limit at fine time steps against the true rotor.
    H = np.diag(4*gamma*n*(n+2))+W
    e,U = eigh(H)
    omega = U[:,0]
    target = np.dot(abs(U.T @ O @ omega)**2, np.exp(-0.25*(e-e[0]))*(-np.expm1(-0.25*(e-e[0])))**2)
    data = []
    for dt in (1/32,1/128,1/512,1/2048):
        g = 1/(2*gamma*dt)
        M = (basis*np.exp(-dt*E/2)) @ basis.T
        tau,V = eigh((M*((ive(n+1,g)/ive(1,g))**4)) @ M.T)
        oa = V[:,-1]*np.sign(np.dot(V[:,-1],omega))
        graph = np.linalg.norm(4*gamma*n*(n+2)*(oa-omega))
        X = np.clip(tau/tau[-1],0,1)**round(0.25/dt)
        D = np.dot(abs(V.T @ O @ oa)**2, X*(1-X)**2)
        data.append([dt,float(graph),float(abs(target-D))])
    if not all(q[1]<p[1] and q[2]<p[2] for p,q in zip(data,data[1:])):
        raise AssertionError("fine time rotor")
    return {"thermal_readings": list(map(float,readings)), "thermal_signal": float(np.dot([1,-2,1],readings)),
            "max_basis_score_error": float(err), "vacuum_target": float(target), "time_graph_signal_errors": data}


def haar_cells():
    # The unused second Hopf angle integrates exactly for this one-link test.
    # The electric-score integral must vanish because the sphere has no boundary.
    g = 2.5
    target = ive(2, g) / ive(1, g)
    rows = []
    for mesh in (8, 16, 32, 64):
        mid = (np.arange(mesh) + 0.5) / mesh
        x = np.sqrt(1 - mid[:, None]) * np.cos(2 * math.pi * mid[None, :])
        weight = np.exp(g * (x - 1))
        electric = 3 * g * x - g**2 + (g * x)**2
        magnetic_error = abs(np.sum(weight * x) / weight.sum() - target)
        electric_error = abs(np.sum(weight * electric) / weight.sum())
        rows.append([mesh, float(magnetic_error), float(electric_error)])
    if rows[-1][1] > 1e-4 or rows[-1][2] > 1e-3:
        raise AssertionError(("Hopf Haar cells", rows))
    return rows


def unequal_weight_control():
    # Independent opposed pairs on a full cubic grid. The tensor tent test has
    # an elementary sum of squares, so the comparison has an analytic value.
    rows = []
    for mesh in (16, 32, 64):
        b = 1 / mesh
        dilation = 2
        intervals = mesh // dilation
        grid = np.arange(-intervals, intervals + 1)
        tent = np.maximum(0, 1 - np.abs(grid) / intervals)
        phi = np.einsum("i,j,k->ijk", tent, tent, tent)
        expected_sum = ((2 * intervals**2 + 1) / (3 * intervals))**3
        moments = []
        for theta in (b**3, b**2):
            contrast = 2 * theta * phi
            actual = np.sum(contrast**2) / b**3
            expected = 4 * theta**2 * expected_sum / b**3
            if not math.isclose(actual, expected, rel_tol=1e-12):
                raise AssertionError(("opposed coefficient test", actual, expected))
            moments.append(float(actual))
        rows.append([mesh, *moments])
    if rows[-1][2] <= 12 * rows[0][2] or rows[-1][1] > rows[0][1]:
        raise AssertionError("coefficient powers in the first moment")
    return rows


def recover(out: Path):
    # Three orthogonal tangent directions on the unit quaternions. Each great
    # circle contributes -u to the second derivative of a coordinate.
    rank = np.linalg.matrix_rank(np.eye(4)[1:])
    poly = np.polynomial.polynomial.polymul([0,1],np.polynomial.polynomial.polymul([1,-1],[1,-1]))
    (out/"counts.bin").write_bytes(bytes(int(abs(v)) for v in poly[1:]))
    proof = (f"theorem sphericalScore {{h u : ℝ}} (rad : |u| ≤ h) :\n"
             f"    |{rank}*u-h^2+u^2| ≤ {rank}*h+h^2 := by\n"
             "  have bounds := abs_le.mp rad\n  have square := mul_self_le_mul_self (abs_nonneg u) rad\n"
             "  rw [abs_mul_abs_self] at square\n  apply abs_le.mpr\n"
             "  constructor <;> nlinarith [sq_nonneg u, sq_nonneg h]\n")
    result = {"periodic_boundary": boundary_check(), "full_SU2_scores": score_check(),
              "character_rotor": rotor_check(), "haar_midpoint": haar_cells(),
              "unequal_weights": unequal_weight_control()}
    (out/"geometry").write_text(proof)
    (out/"checks.json").write_text(json.dumps(result, indent=2)+"\n")
