"""Independent checks of periodic geometry, group derivatives and scaled moments."""
from fractions import Fraction
from itertools import product
import json
import math
from pathlib import Path
from random import Random
import runpy

previous = runpy.run_path(str(Path(__file__).resolve().parents[1]/"spatial-flow-variance/control.py"))
faces, mul, real_loop = (previous[k] for k in ("faces","mul","real_loop"))
axes = [(0,1,0,0),(0,0,1,0),(0,0,0,1)]


def cycles(side):
    vertices = list(product(range(side),repeat=3))
    def neighbors(x):
        for i in range(3):
            for sign in (-1,1):
                yield tuple((v+(sign if j==i else 0))%side for j,v in enumerate(x))

    circuits = set()
    for a in vertices:
        for b in neighbors(a):
            for c in neighbors(b):
                if c == a:
                    continue
                for d in neighbors(c):
                    if d != b and a in neighbors(d):
                        circuits.add(tuple(sorted(tuple(sorted(pair)) for pair in
                                                  ((a,b),(b,c),(c,d),(d,a)))))
    elementary = 3*side**3
    winding = len(circuits)-elementary
    assert winding == (3*side**2 if side==4 else 0)
    return {"side":side,"elementary":elementary,"winding":winding}


def gauge_derivatives():
    # Random links and tangent vectors are generated once. Packet-free checks
    # differentiate ordered quaternion words including their inverse slots.
    rng = Random(2973)
    face_list = [links for links,_ in faces(3,4)]
    links = sorted({e for face in face_list for e in face})
    def draw(n):
        return [rng.gauss(0,1) for _ in range(n)]
    def unit(a):
        norm = math.sqrt(sum(t*t for t in a))
        return tuple(x/norm for x in a)
    field = {e:unit(draw(4)) for e in links}
    velocity = {e:tuple(draw(3)) for e in links}
    grad = {e:[0.0]*3 for e in links}
    def action(config):
        return sum(1-real_loop([config[e] for e in face]) for face in face_list)
    def displaced(v,t):
        ans = {}
        for e, vector in v.items():
            norm = math.sqrt(sum(x*x for x in vector))
            angle = norm*t
            q = (math.cos(angle),*(x*(math.sin(angle)/norm if norm else 0.0) for x in vector))
            ans[e] = mul(q,field[e])
        return action(ans)
    laplacian = 0.
    step = 0.19
    for face in face_list:
        values = [field[e] for e in face]
        trace = real_loop(values)
        for i,e in enumerate(face):
            for j,axis in enumerate(axes):
                term = values.copy()
                term[i] = mul(axis,values[i])
                grad[e][j] -= real_loop(term)
                # For a coordinate on S³, this symmetric great-circle difference
                # divided by 2(1-cos step) equals the exact second derivative.
                traces = []
                for sign in (-1,1):
                    rotation = (math.cos(step),*(sign*math.sin(step)*a for a in axis[1:]))
                    term[i] = mul(rotation,values[i])
                    traces.append(real_loop(term))
                laplacian += (2*trace-sum(traces))/(2*(1-math.cos(step)))
    total = action(field)
    assert abs(laplacian+12*(total-len(face_list))) < 1e-8
    t = 1e-4
    plus,minus = displaced(velocity,t),displaced(velocity,-t)
    directional = sum(sum(x*y for x,y in zip(grad[e],velocity[e])) for e in links)
    assert abs((plus-minus)/(2*t)-directional) < 1e-4
    squared_speed = sum(sum(x*x for x in v) for v in velocity.values())
    assert abs((plus+minus-2*total)/t**2) <= 16*squared_speed
    magnitude = sum(sum(x*x for x in v) for v in grad.values())
    assert abs((displaced(grad,t)-displaced(grad,-t))/(2*t)-magnitude) < 1e-3
    return {"varied_links":len(links),"face_axis_differences":len(face_list)*12}


def tilted_link():
    # Independent quadrature with the SU(2) Haar radial density sin²(theta).
    # For k=0 the tilted law is Haar, and transverse variance is exactly 1/4.
    grid = 8192
    for k in (0.,0.1,1.,6.,30.,100.):
        z = longitudinal = transverse = 0.
        for i in range(grid):
            theta = (i+0.5)*math.pi/grid
            x, s = math.cos(theta),math.sin(theta)
            weight = math.exp(k*(x-1))*s*s
            z += weight
            longitudinal += weight*x
            transverse += weight*s*s/3
        h, var = longitudinal/z,transverse/z
        assert abs(h-k*var) < 2e-12
        assert var+1e-13 >= 1/(4+k)
        # Weighted Laplacian of x²: Delta x² = 2-8x², drift = 2 k x (1-x²).
        residual = 0.
        for i in range(grid):
            theta = (i+0.5)*math.pi/grid
            x, s = math.cos(theta),math.sin(theta)
            residual += math.exp(k*(x-1))*s*s*(2-8*x*x+2*k*x*s*s)
        assert abs(residual/z)<1e-11
    return {"tilts":6,"radial_nodes":grid}


def spectral():
    # An invisible component at zero defeats an unweighted second-moment test.
    eta = Fraction(1,8)
    atoms = [(0,Fraction(3,8)),(1,Fraction(1,4)),(Fraction(7,4),Fraction(1,16))]
    moments = [sum(w*x**j for x,w in atoms) for j in range(4)]
    loss = sum(w*x*(x-1)**2 for x,w in atoms)
    assert loss == moments[3]-2*moments[2]+moments[1]
    weighted_out = sum(w*x for x,w in atoms if abs(x-1)>eta)
    assert eta**2*weighted_out <= loss
    assert sum(w*(x-1)**2 for x,w in atoms) >= Fraction(3,8)
    # Bounded prototype of a pure degree-eight electric channel: all its mass
    # escapes to x=0 in the transfer coordinate scaled by the first band.
    for n in (4,8,16):
        t = Fraction(1,n**4)
        readings = [(t,Fraction(1,4)),(t*t,Fraction(1,9))]
        assert sum(w for lam,w in readings if abs(lam/t-1)<=eta)==Fraction(1,4)
    return {"weighted_loss":str(loss),"unweighted_zero_atom":"3/8"}


def unit_flow_band():
    # u=1, beta=2^-1024, eta=2^-256.  Use e<3, exp(x)-1 <= 2x
    # for 0<=x<=1/2, and a geometric majorant for the factorial tail.
    R = 96
    n = 3*(2*R+5)**3
    m = 3*(2*R+7)**3
    beta = Fraction(1,2**1024)
    first = Fraction(16**(R+1),math.factorial(R+1))
    tail = first/(1-Fraction(16,R+2))
    x = 12*beta*m
    assert 0 < x < Fraction(1,2)
    h_lower = Fraction(1,3**32)
    bracket = h_lower/4-(Fraction(4,3)+16*n)*tail-4*n*x-Fraction(n,2**194)
    assert bracket >= h_lower/8
    floor = h_lower**2/(32*n)
    assert floor > Fraction(1,10**40)
    return {"flow_time":1,"radius":R,"beta_exponent":-1024,"band_width_exponent":-256,
            "uniform_absolute_weight_exceeds":"1e-40"}


if __name__=="__main__":
    print(json.dumps({"circuits":[cycles(n) for n in (4,6)],"derivatives":gauge_derivatives(),
                      "conditional_link":tilted_link(),"spectral":spectral(),
                      "finite_beta":unit_flow_band()},sort_keys=True))
