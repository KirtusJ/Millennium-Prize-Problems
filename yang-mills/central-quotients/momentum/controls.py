"""Adverse checks for the spatial-momentum and double-commutator arguments."""
from math import cos, pi, sin, sqrt
from itertools import product
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "local-response"))
from check import ONE, geometry, holonomy, mul


def harmonic(side):
    zero = side**-3
    values = []
    for mode in product(range(side), repeat=3):
        energy = sqrt(zero**2 + 4*sum(sin(pi*k/side)**2 for k in mode))
        mass = 1/energy
        if abs(mass*energy-1) > 1e-12 or mass*energy**3 > 13 + 1e-12:
            raise ValueError("moment bounds changed")
        values.append((energy, mass))
    mean = sum(m for _, m in values) / len(values)
    if mean > 4 or abs(values[0][1] / side**3 - 1) > 1e-12:
        raise ValueError("static normalization changed")
    return mean, values[0][0]


def quaternion_step(q, vector, scale):
    norm = sqrt(sum(v*v for v in vector))
    if not norm:
        return q
    rotation = (cos(norm*scale), *(v*sin(norm*scale)/norm for v in vector))
    return mul(rotation, q)


def face_gradient(face, links):
    deriv = {}
    h = 1e-6
    for a, b in face:
        edge = tuple(sorted((a,b)))
        current = links.get(edge, ONE)
        gradient = []
        for i in range(3):
            basis = [int(i == j) for j in range(3)]
            vals = []
            for t in (h, -h):
                update = dict(links)
                update[edge] = quaternion_step(current, basis, t)
                x = holonomy(face, update)[0]
                vals.append(4*x*x/3 - 1/3)
            gradient.append((vals[0]-vals[1])/(2*h))
        deriv[edge] = gradient
    return deriv


def side_hessian():
    # Actual oriented cube and two independent horizontal-gradient perturbations.
    faces = geometry(1)
    terminal = (cos(pi/4), sin(pi/4), 0., 0.)
    links = {((x, 0, 0), (x, 1, 0)): terminal for x in (0,1)}
    gradients = [face_gradient(face, links) for face in faces[:2]]
    if set(gradients[0]) & set(gradients[1]):
        raise ValueError("the two terminal faces share a link")
    def potential(s, t):
        updated = dict(links)
        for grad, weight in zip(gradients, (s,t)):
            for edge, direction in grad.items():
                updated[edge] = quaternion_step(links.get(edge, ONE), direction, weight)
        return sum(1-holonomy(face,updated)[0] for face in faces)
    h = 1e-3
    mixed = (potential(h,h)-potential(h,-h)-potential(-h,h)+potential(-h,-h))/(4*h*h)
    if abs(mixed + 64/9) > 1e-5:
        raise ValueError("second-ring magnetic term missing")
    return mixed


def radial_check():
    h = 1e-5
    residual = 0.
    for x in (-1., -.81, -.5, 0., .5, .73, 1.):
        q = (x, sqrt(1-x*x), 0., 0.)
        total = 0.
        for i in range(3):
            basis = [int(i == j) for j in range(3)]
            plus, minus = (quaternion_step(q, basis, t) for t in (h,-h))
            for j in range(1,4):
                dy = (plus[0]*plus[j]-minus[0]*minus[j])/(2*h)
                total += dy*dy
        residual = max(residual, abs(total-(1-2*x*x+4*x**4)))
    if residual > 1e-8:
        raise ValueError("adjoint gradient-map differential mismatch")
    return residual


if __name__ == "__main__":
    for n in (3,5,9,15):
        static, energy = harmonic(n)
        print(f"side={n} mean static mass={static:.8f} zero-mode energy={energy:.8f}")
    print(f"mixed magnetic derivative={side_hessian():.8f}")
    print(f"adjoint derivative residual={radial_check():.3g}")
