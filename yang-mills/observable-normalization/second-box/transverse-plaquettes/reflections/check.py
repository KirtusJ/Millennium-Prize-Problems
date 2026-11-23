"""Apply all spatial link reflections to a noncommuting frozen background."""
from pathlib import Path
import importlib.util
import numpy as np

parent = Path(__file__).resolve().parents[1] / "check.py"
spec = importlib.util.spec_from_file_location("plaquettes", parent)
box = importlib.util.module_from_spec(spec)
spec.loader.exec_module(box)


def rotate_inverse(h, vectors):
    scalar, axis = h[0], -h[1:]
    return ((scalar**2 - axis @ axis)*vectors + 2*(vectors @ axis)[..., None]*axis
            + 2*scalar*np.cross(axis, vectors))


def reflect(field, background, mask):
    result = field.copy()
    h = box.qexp(background)
    for i in range(3):
        if mask & (1 << i):
            sites = np.arange(8) ^ (1 << (2-i))
            result[..., :, i, :] = -rotate_inverse(h[i], field[..., sites, i, :])
    return result


def log_density(v, frame):
    r = np.linalg.norm(v, axis=-1)
    unit = v / np.where(r == 0, 1, r)[..., None]
    tangential = np.sinc(r / np.pi)**2
    radial = (frame * unit).sum(axis=-1, keepdims=True) * unit
    metric_frame = tangential[..., None]*frame + (1-tangential[..., None])*radial
    gram = frame.reshape(42, -1) @ metric_frame.reshape(42, -1).T
    sign, logdet = np.linalg.slogdet(gram)
    assert sign == 1
    return logdet/2


def main():
    a = np.array([[0.09,0.03,0.01], [-0.02,0.06,-0.07], [0.04,0.02,0.08]])
    rng = np.random.default_rng(23890)
    fields = box.horizontal_basis(a)
    z, y = np.tensordot(rng.normal(size=(2,42)), fields, axes=1)*0.1
    def temporal(x, v):
        return np.sum((box.qexp(x)-box.qexp(v))**2)/2
    base = np.array([box.action(z,a), box.action(y,a), temporal(z,y), log_density(z,fields)])
    errors = []
    for mask in range(8):
        b = a * np.array([(-1)**((mask >> i)&1) for i in range(3)])[:,None]
        f = box.horizontal_basis(b)
        transformed = reflect(fields,a,mask).reshape(42,-1)
        overlaps = transformed @ f.reshape(42,-1).T
        error = np.max(np.abs(overlaps @ overlaps.T - np.eye(42)))
        zz, yy = reflect(z,a,mask), reflect(y,a,mask)
        observed = [box.action(zz,b), box.action(yy,b), temporal(zz,yy), log_density(zz,f)]
        errors.append([error, *np.abs(observed-base)])
    worst = np.max(errors,axis=0)
    assert max(worst) < 3e-13, worst
    print("maximum absolute errors: plane, spatial(z), spatial(y), temporal, log density")
    print(worst)


if __name__ == '__main__':
    main()
