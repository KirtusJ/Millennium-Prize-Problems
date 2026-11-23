"""Direct quaternion plaquettes on the periodic 2^3 box, with NumPy."""
from itertools import combinations, product
import numpy as np

sites = np.array(list(product(range(2), repeat=3)))
pairs = tuple(combinations(range(3), 2))


def qexp(v):
    r = np.linalg.norm(v, axis=-1, keepdims=True)
    return np.concatenate((np.cos(r), np.sinc(r / np.pi) * v), axis=-1)


def multiply(a, b):
    ar, av = a[..., :1], a[..., 1:]
    br, bv = b[..., :1], b[..., 1:]
    return np.concatenate((ar * br - (av * bv).sum(axis=-1, keepdims=True),
                           ar * bv + br * av + np.cross(av, bv)), axis=-1)


def action(field, background):
    links = multiply(qexp(field), qexp(background))
    total = 0.0
    for i, j in pairs:
        ui, uj = links[..., :, i, :], links[..., :, j, :]
        first = multiply(ui, uj[..., np.arange(8) ^ (1 << (2-i)), :])
        second = multiply(uj, ui[..., np.arange(8) ^ (1 << (2-j)), :])
        # 1-Re(P) is half the squared chord between the two paths.
        total = total + 0.5 * ((first - second)**2).sum(axis=(-1, -2))
    return total


def basis():
    fields = []
    for mode in sites[1:]:
        phase = (-1.0)**(sites @ mode) / np.sqrt(8)
        frame = np.linalg.svd(mode[None, :], full_matrices=True)[2][1:]
        for v in frame:
            for color in np.eye(3):
                fields.append(np.einsum('x,i,a->xia', phase, v, color))
    fields = np.array(fields)
    flat = fields.reshape(42, -1)
    np.testing.assert_allclose(flat @ flat.T, np.eye(42), atol=1e-14)
    return fields


def horizontal_basis(a):
    field_basis = []
    h = qexp(a)
    for mode in sites[1:]:
        phase = (-1.0)**(sites @ mode) / np.sqrt(8)
        rotations = []
        for link, bit in zip(h, mode):
            scalar, axis = link[0], link[1:]
            rotated = np.array([(scalar**2 - axis@axis)*e + 2*(axis@e)*axis
                                + 2*scalar*np.cross(axis, e) for e in np.eye(3)]).T
            rotations.append(np.eye(3) - (-1.0)**bit * rotated)
        tangent = np.concatenate(rotations)
        u, singular, _ = np.linalg.svd(tangent, full_matrices=True)
        assert min(singular) > 1
        for direction in u[:, 3:].T:
            field_basis.append(phase[:, None, None] * direction.reshape(3, 3))
    return np.array(field_basis)


def spectrum(fields, a, eps=0.0001):
    # Mixed symmetric differences, batching one matrix row at a time.
    hessian = []
    for f in fields:
        plus, minus = eps * (f + fields), eps * (f - fields)
        row = (action(plus, a) + action(-plus, a)
               - action(minus, a) - action(-minus, a)) / (4*eps**2)
        hessian.append(row)
    return np.linalg.eigvalsh(hessian)


def vacuum(eigs):
    return 0.5 * np.arccosh(1 + eigs / 2).sum()


def main():
    fields = basis()
    base = spectrum(fields, np.zeros((3, 3)))
    np.testing.assert_allclose(base, np.repeat([4, 8, 12], [18, 18, 6]), atol=2e-7)
    print(f"center Gaussian energy {vacuum(base):.9f}")
    coefficients = []
    for r in (0.06, 0.03, 0.015):
        eigs = spectrum(fields, r * np.eye(3))
        ratio = (vacuum(eigs) - vacuum(base)) / r**2
        coefficients.append(ratio)
        print(f"noncommuting r={r:.3f}  min Hessian={eigs[0]:.7f}  energy shift/r²={ratio:.7f}")
    assert abs(coefficients[2]-coefficients[1]) < abs(coefficients[1]-coefficients[0]) < 0.2
    angles = np.array([0.13, -0.17, 0.08])
    commuting = np.outer(angles, [0, 0, 1])
    moving_lambdas, fixed_lambdas = [], []
    for mode in sites[1:]:
        n = -mode / np.sqrt(mode.sum())
        d = (-1.0)**mode * np.exp(2j*angles)-1
        full = np.vdot(d, d).real
        projected = abs(n @ d)**2
        neutral = 4*mode.sum()
        moving_lambdas.extend([neutral]*2 + [full]*4)
        fixed_lambdas.extend([neutral]*2 + [full]*2 + [projected]*2)
    for frame, analytic in [(fields, fixed_lambdas), (horizontal_basis(commuting), moving_lambdas)]:
        np.testing.assert_allclose(spectrum(frame, commuting), sorted(analytic), rtol=0, atol=3e-7)
    q = 4/np.sqrt(96) + 8/(3*np.sqrt(192))
    kappa = 8*(1/np.sqrt(32) - 1/np.sqrt(96) - 1/np.sqrt(192))
    r = 0.005
    for name, v in [("parallel", np.array([[1,0,0],[1,0,0],[0,0,0]])),
                    ("antiparallel", np.array([[1,0,0],[-1,0,0],[0,0,0]])),
                    ("orthogonal", np.eye(3))]:
        norms = np.sum(v*v)
        fixed = (vacuum(spectrum(fields,r*v))-vacuum(base))/r**2
        covariant = (vacuum(spectrum(horizontal_basis(r*v), r*v))-vacuum(base))/r**2
        fixed_limit = q*(-4*norms + sum(v[i] @ v[j] for i,j in pairs))
        print(f"{name:12} fixed={fixed:.6f} ({fixed_limit:.6f})"
              f"  horizontal={covariant:.6f} ({kappa*norms:.6f})")
        assert abs(fixed-fixed_limit) < 0.002 and abs(covariant-kappa*norms) < 0.002
    a = 0.06 * np.eye(3)
    direction = np.tensordot(np.random.default_rng(3462).normal(size=42), fields, axes=1)
    direction /= np.linalg.norm(direction)
    s0 = 0.1
    previous = None
    for j in range(4):
        s = s0 / 2**j
        plus, minus = action(s*direction, a), action(-s*direction, a)
        odd = (plus-minus)/(2*s**3)
        even = (plus+minus-2*action(0*direction, a))/(2*s**2)
        # The exact translation-invariant background kills the linear term.
        print(f"s={s:.4f}  odd/s³={odd:.9f}  even/s²={even:.9f}")
        if previous is not None:
            assert abs(odd-previous) < 0.001
        previous = odd
    assert abs(previous) > 0.001  # cubic is present before parity averaging


if __name__ == '__main__':
    main()
