"""Check the momentum-window calculation for the quartic orientation matrix."""
from math import pi, sqrt
import numpy as np

D = 7 / 768

def window(side, radius):
    # The row-sum bound on theta gives |k| <= pi sqrt(256 D) r / 2.
    end = int(np.ceil(side * radius * sqrt(256 * D) / 4))
    n = np.arange(-end, end+1)
    y, z = np.meshgrid(n, n, indexing="ij")
    counts = np.zeros(4)
    for x in n:
        k = np.stack(np.broadcast_arrays(x,y,z), axis=-1) * (2*pi/side)
        t = 2*np.cos(k/2)
        matrix = 2*t[..., :, None]*t[..., None, :]
        diagonal = 50/3 - np.sum(4*np.sin(k/2)**2, axis=-1)
        for i in range(3):
            matrix[...,i,i] = diagonal
        val, vec = np.linalg.eigh(matrix)
        inside = (98/3-val[..., -1]) <= 256*D*radius**2
        # Convert face-centered Fourier coordinates to common site anchors.
        v = vec[..., :, -1]*np.exp(0.5j*(k.sum(axis=-1)[..., None]-k))
        unit = np.abs(v.sum(axis=-1))**2/3
        face = np.abs(v[..., 0])**2
        difference = np.abs(v[..., 0]-v[..., 1])**2/2
        counts += [inside.sum(),unit[inside].sum(),face[inside].sum(),difference[inside].sum()]
    count, scalar, single, tensor = counts
    assert abs(single - (scalar+2*tensor)/3) < 1e-8 * count
    assert 0 <= tensor / count < radius**2
    return count/(side*radius)**3, single/scalar, tensor/(scalar*radius**2)

if __name__ == "__main__":
    for L, r in [(256,0.5),(512,0.25),(1024,0.125)]:
        rows = window(L,r)
        assert abs(rows[0]*6*pi**2 - 1)<0.04
        assert abs(rows[1]-1/3)<0.01
        print(L,r,*rows)
