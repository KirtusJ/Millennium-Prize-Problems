"""Reproduce the scale tail for three Gaussian curvature colors in the time vacuum."""
import numpy as np


def check(n):
    freq = np.fft.fftfreq(n)
    axis = 4 * np.sin(np.pi * freq)**2
    sx, sy, sz = np.meshgrid(axis, axis, axis, indexing="ij", sparse=True)
    s = sx + sy + sz
    h = np.divide(sx + sy, np.sqrt(s * (s + 4)), where=s>0, out=np.zeros_like(s))
    g = np.fft.ifftn(h).real
    d = np.minimum(np.arange(n), n-np.arange(n))
    for j in range(3):
        delta = np.roll(h, -1, axis=j)-h
        assert abs(delta).max() <= 4*np.pi/n
        profile = np.moveaxis(g,j,0).reshape(n,-1)
        np.testing.assert_allclose((4*np.sin(np.pi*d/n)**2)@(profile**2).sum(axis=1),
                                   (delta**2).mean(),atol=1e-14)
        assert d**2 @ (profile**2).sum(axis=1) <= np.pi**2
    c = 1.5*g**2
    full = c.sum()
    last = 0
    largest = 0
    for length in range(1,n+1):
        overlap = (np.maximum(0,length-d)+np.maximum(0,length-(n-d)))/length
        block = np.einsum("i,j,k,ijk->",overlap,overlap,overlap,c,optimize=True)
        assert last <= block + 1e-13 and -1e-13 <= full-block <= 4.5*np.pi/length
        last = block
        largest = max(largest,length*(full-block))
    np.testing.assert_allclose(last, full, atol=1e-13)
    return float(full),float(largest)


if __name__ == "__main__":
    for side in (6,8,10,16,32,64):
        full, largest = check(side)
        print(f"N={side:2}  chi={full:.8f}  max L*(chi-B)={largest:.8f}")
