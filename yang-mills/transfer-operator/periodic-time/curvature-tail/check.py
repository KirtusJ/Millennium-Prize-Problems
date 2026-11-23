"""Independent finite-box projection checks for the curvature tail estimate."""
from itertools import combinations, product

import numpy as np
from scipy.fft import dct, dst
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import lsmr


def explicit_projection(radius):
    """Project a central face directly onto the range of the unpinned curl."""
    sites = list(product(range(-radius, radius+1), repeat=4))
    unit = np.eye(4, dtype=int).tolist()

    def shift(x, axis):
        return tuple(a+b for a, b in zip(x, unit[axis]))

    def inside(x):
        return max(map(abs, x)) < radius

    links = {(x, axis): None for x in sites for axis in range(4)
             if x[axis] < radius and (inside(x) or inside(shift(x, axis)))}
    indices = {key: i for i, key in enumerate(links)}
    rows, cols, values = [], [], []
    face_index, central = 0, None
    for x in sites:
        for i, j in combinations(range(4), 2):
            if max(x[i], x[j]) == radius:
                continue
            boundary = [((x, i), 1), ((shift(x, i), j), 1),
                        ((shift(x, j), i), -1), ((x, j), -1)]
            included = [(indices[e], sign) for e, sign in boundary if e in indices]
            if not included:
                continue
            if x == (0,)*4 and (i, j) == (0, 1):
                central = face_index
            for column, sign in included:
                cols.append(column)
                rows.append(face_index)
                values.append(sign)
            face_index += 1
    curl = coo_matrix((values, (rows, cols)), shape=(face_index, len(indices))).tocsr()
    test = np.zeros(face_index)
    assert central is not None
    test[central] = 1
    potential = lsmr(curl, test, atol=1e-13, btol=1e-13)[0]
    residual = test-curl@potential
    assert np.linalg.norm(curl.T@residual) < 1e-9
    return 1-residual[central]


def separated_projection(radius):
    # One component of curl*delta, with Neumann endpoints along the edge axis
    # and zero tangential boundary values along each transverse axis.
    n = 2*radius
    source = np.zeros((n, n-1, n-1, n-1))
    source[radius, radius-1, radius-1, radius-1] = 1
    if radius < n-1:
        source[radius, radius, radius-1, radius-1] = -1
    modes = dct(source, type=2, axis=0, norm="ortho")
    for axis in range(1, 4):
        modes = dst(modes, type=1, axis=axis, norm="ortho")
    energy = 4*np.sin(np.arange(n)*np.pi/(2*n))**2
    laplacian = (energy[:, None, None, None] + energy[None, 1:, None, None]
                 + energy[None, None, 1:, None] + energy[None, None, None, 1:])
    # The other face-boundary component has the same energy by axis exchange.
    return 2*np.sum(modes**2/laplacian)


def main():
    previous = None
    for radius in [1, 2, 3, 4, 6, 8, 12, 16]:
        diagonal = separated_projection(radius)
        if radius <= 3:
            np.testing.assert_allclose(diagonal, explicit_projection(radius), atol=2e-12, rtol=0)
        if radius == 1:
            np.testing.assert_allclose(diagonal, 7/24, atol=2e-14)
        defect = .5-diagonal
        action = 1.5*defect**2
        assert defect > 0 and (previous is None or defect < previous)
        previous = defect
        print(f"{radius:2}  {diagonal:.10f}  {radius**4*defect:.7f}  {radius**8*action:.7f}")


if __name__ == "__main__":
    main()
