"""Check periodic Wilson geometry, two admissible exteriors and the binary channel."""
import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.special import ive, ndtr, roots_chebyu


def move(x, direction, side):
    return tuple((v+1) % side[i] if i == direction else v for i, v in enumerate(x))


def face(x, i, j, side):
    return [(x, i), (move(x, i, side), j), (move(x, j, side), i), (x, j)]


def graph_control(pitch):
    side = (3, 2*pitch, 2*pitch, 2*pitch)
    grid = list(itertools.product(*(range(s) for s in side)))
    marks = set()
    counts = []
    for x in grid:
        if x[0] or any(v % pitch for v in x[1:]):
            continue
        for axis in (1, 2, 3):
            v = x
            before = len(marks)
            for j in range(pitch):
                if 0 < j < pitch-1:
                    marks.add((v, axis))
                v = move(v, axis, side)
            counts.append(len(marks)-before)
    hits = [sum(e in marks for e in face(x, i, j, side))
            for x in grid for i, j in itertools.combinations(range(4), 2)]
    if min(counts) != pitch-2 or max(counts) != pitch-2 or max(hits) != 1 or sum(hits) != 6*len(marks):
        raise AssertionError("coarse-edge incidence")
    return {"pitch": pitch, "coarse_edges":len(counts), "marks":len(marks), "max_per_face":max(hits)}


def rectangle_exteriors():
    # Change a link on the distant return side, in each of two disjoint rectangles.
    # Recompute complete SU(2) Wilson exponents on the four-dimensional torus.
    side = (3, 7, 5, 4)
    axes = list(itertools.combinations(range(4), 2))
    grid = list(itertools.product(*(range(s) for s in side)))
    faces = [face(x, i, j, side) for x in grid for i,j in axes]
    active = [((0,x,0,z),1) for z in (0,2) for x in range(1,5)]
    insertions = {((0,2,2,z),1) for z in (0,2)}
    if any(sum(e in active for e in f)>1 or
           (set(f)&insertions and set(f)&set(active)) for f in faces):
        raise AssertionError("overlapping active staples")
    rng = np.random.default_rng(42023)
    def su2():
        w,x,y,z = rng.normal(size=4)
        return np.array([[w+1j*z, y+1j*x],[-y+1j*x,w-1j*z]])/math.sqrt(w*w+x*x+y*y+z*z)
    eye = np.eye(2)
    varied = {e:su2() for e in active}
    def exponent(links):
        value = 0.
        for f in faces:
            a,b,c,d = (links.get(e,eye) for e in f)
            value += .5*np.trace(a @ b @ c.conj().T @ d.conj().T).real
        return value
    prediction = 6*sum(np.trace(u).real/2-1 for u in varied.values())
    errors, traces = [], []
    for sign in (1,-1):
        ext = {e: sign*eye for e in insertions}
        errors.append(abs(exponent(varied|ext)-exponent(ext)-prediction))
        vals = []
        for z in (0,2):
            u = eye
            for x in range(1,5):
                u = u @ varied[((0,x,0,z),1)]
            vals.append(float(np.trace(u @ ext[((0,2,2,z),1)].conj().T).real))
        traces.append(vals)
    if max(errors)>1e-10 or not np.allclose(traces[0], -np.array(traces[1])):
        raise AssertionError("conditional Wilson exponents or trace signs")
    # Opposite failure mode: two active edges on one action face have a mixed change.
    u = -eye
    first, second = faces[0][:2]
    mixed = exponent({first:u,second:u}) + exponent({}) - exponent({first:u})-exponent({second:u})
    if abs(mixed-4)>1e-10:
        raise AssertionError("shared-plaquette adverse control")
    return {"four_dimensional_faces": len(faces), "active_links":len(active),
            "max_action_residual":max(errors), "trace_pair":traces,
            "shared_face_mixed_change":mixed}


def binary_law():
    x, weights = roots_chebyu(384)
    weights *= 2/np.pi
    theta = np.arccos(x)
    n = np.arange(1,41)
    chars = np.sin(np.outer(n+1,theta))/np.sin(theta)
    strength = 6.0
    ratios = ive(n+1,strength)/ive(1,strength)
    coeffs = n+1
    if np.max(ratios-ratios[0]**n)>1e-13:
        raise AssertionError("order ratios")
    result = []
    for m in (6,10,14,18):
        s = ratios[0]**m
        p = 1 + (coeffs*ratios**m)@chars
        q = p[::-1]
        if min(p)<0 or abs(weights@p-1)>1e-12:
            raise AssertionError("radial density")
        chi = 2*x
        np.testing.assert_allclose(weights@(p*chi), 2*s, atol=2e-13)
        np.testing.assert_allclose(weights@(p*chi**2), 1+3*ratios[1]**m, atol=2e-13)
        reverse = weights@((p-1)**2/p)
        np.testing.assert_allclose(reverse, weights@(1/p)-1, atol=5e-14)
        eps = max(abs(p-1))
        if eps<1 and reverse>eps**2/(1-eps):
            raise AssertionError("reverse chi-square")
        ll = np.log(p/q)
        mean = weights@(p*ll)
        variance = weights@(p*(ll-mean)**2)
        M = round(.25/s**2)
        # Fourier inversion for the sign test under the plus hypothesis.
        # Double the integration grid and extend the frequency range as a control.
        def bayes_error(cut, steps):
            t = np.linspace(0,cut,steps+1)
            cf = (np.exp(1j*np.outer(t,ll)) @ (weights*p))**M
            val = np.empty_like(t)
            val[0] = M*mean
            val[1:] = cf.imag[1:]/t[1:]
            return .5-np.trapz(val,t)/np.pi
        err = bayes_error(12,1200)
        refined = bayes_error(20,2400)
        if abs(err-refined)>2e-6 or not 0<refined<.5:
            raise AssertionError(("likelihood inversion",m,err,refined))
        # Integrate each character on Tr(g)>0 against exact radial Haar.
        cap_chars = (np.sin(n*np.pi/2)/n-np.sin((n+2)*np.pi/2)/(n+2))/np.pi
        cap_plus = .5+(coeffs*ratios**m)@cap_chars
        cap_minus = .5+(((-1.)**n)*coeffs*ratios**m)@cap_chars
        cap_slope = math.log(cap_plus/cap_minus)/s
        rare_M = round(1/s)
        result.append({"m":m, "M":M, "s":s, "M_s_squared":M*s*s,
                       "KL_over_s_squared":mean/s**2, "variance_over_s_squared":variance/s**2,
                       "equal_prior_error":refined, "normal_limit_at_Ms2":float(ndtr(-2*math.sqrt(M)*s)),
                       "inversion_change":abs(err-refined), "cap_log_ratio_over_s":cap_slope,
                       "rare_M":rare_M, "all_positive_ratio":math.exp(rare_M*s*cap_slope)})
    if abs(result[-1]["KL_over_s_squared"]-8)>.01 or abs(result[-1]["variance_over_s_squared"]-16)>.01:
        raise AssertionError("likelihood constants")
    if abs(result[-1]["cap_log_ratio_over_s"]-32/(3*np.pi))>.001:
        raise AssertionError("positive-cap relative likelihood rate")
    return result


def translation_control():
    # A multimodal, non-even circle potential tests the general Hessian argument.
    N = 8192
    x = 2*np.pi*np.arange(N)/N
    logp = 1.6*np.cos(3*x+.3)+.7*np.sin(5*x)+.15*np.cos(x)
    score = -4.8*np.sin(3*x+.3)+3.5*np.cos(5*x)-.15*np.sin(x)
    hessian = -14.4*np.cos(3*x+.3)-17.5*np.sin(5*x)-.15*np.cos(x)
    L = 14.4+17.5+.15
    p = np.exp(logp); p /= p.mean()
    fisher = np.mean(p*score**2)
    if abs(fisher+np.mean(p*hessian))>3e-12 or fisher>L:
        raise AssertionError("Fisher integration by parts")
    j = int(N/(2*np.pi*math.sqrt(L)))
    h = 2*np.pi*j/N
    overlap = np.minimum(p,np.roll(p,-j)).mean()
    if overlap<1-.5*math.sqrt(L)*h:
        raise AssertionError("translation overlap")
    coeff = np.fft.rfft(p)/N
    freq = np.arange(1,257)
    ratio = np.max(overlap*abs(np.exp(1j*freq*h)-1)**2/(4*(1-abs(coeff[freq])**2)))
    if ratio>1:
        raise AssertionError("unitary variance comparison")
    return {"fisher":fisher,"hessian_cap":L,"small_shift_overlap":overlap,
            "tested_modes":len(freq),"max_displacement_ratio":ratio}


def dressed_channel():
    # Visible exterior sign R multiplies a Haar-centered nonlinear graph test.
    # Evaluate the conditional bias and its energy under each product law.
    M, eps = 10,.085
    words = np.array(list(itertools.product((-1.,1.), repeat=M)))
    phi = np.exp(.4*words.sum(axis=1))
    phi -= phi.mean()
    ratio = []
    for sign in (-1,1):
        p = (1+sign*eps*words).prod(axis=1)
        rev = ((1-p)**2/p).mean()
        exact = (1/(1-eps**2))**M-1
        np.testing.assert_allclose(exact, rev)
        score = (sign*p*phi).mean()**2/(p*phi**2).mean()
        if score>rev:
            raise AssertionError("dressed conditional L2 bound")
        ratio.append(score)
    return {"edges":M,"reverse_chi_squared":rev,"conditional_squared_bias_over_energy":ratio}


def run(out: Path):
    graphs = [graph_control(n) for n in (3,4,6)]
    controls = {"graphs":graphs, "rectangles":rectangle_exteriors(),
                "binary_channel":binary_law(), "dressing":dressed_channel(),
                "circle_translation":translation_control()}
    (out/"checks.json").write_text(json.dumps(controls, indent=2)+'\n')
    lost = {g["pitch"]-g["marks"]//g["coarse_edges"] for g in graphs}
    if lost!={2}:
        raise AssertionError("endpoint count")
    trim, = lost
    (out/"geometry").write_text(f"theorem interiorLinks (m : ℕ) (h : {trim} ≤ m) : (m-{trim})+{trim} = m := by omega\n")
    # For the native search: overlap denominator, number of squared triangle
    # terms, Haar average squared displacement of a unit vector.
    (out/"counts.bin").write_bytes(bytes([2,2,2]))
