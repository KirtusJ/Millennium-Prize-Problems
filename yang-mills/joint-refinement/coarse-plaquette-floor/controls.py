"""Exhaustive periodic incidence checks and independent quaternion/Fourier controls."""
from itertools import combinations, product

import numpy as np


def geometry(n):
    directions = tuple(combinations(range(3), 2))
    vertices = tuple(product(range(n), repeat=3))

    def step(p, axis):
        return tuple((v + (i == axis)) % n for i, v in enumerate(p))

    faces = {}
    groups = {}
    for p in vertices:
        for i, j in directions:
            face = ((p, i), (step(p, j), i), (p, j), (step(p, i), j))
            faces[p, i, j] = face
            pair = (face[int(p[j] % 2 == 0)], face[2 + int(p[i] % 2 == 0)])
            assert all(any(v % 2 for a, v in enumerate(x) if a != k) for x, k in pair)
            colour = i, j, tuple(v % 2 for v in p)
            groups.setdefault(colour, {})[p, i, j] = pair
    assert len(groups) == 24
    incidences = dict.fromkeys(faces, 0)
    for pairs in groups.values():
        owners = {link: owner for owner, pair in pairs.items() for link in pair}
        assert len(owners) == 2 * len(pairs)
        touched = {owner: [] for owner in pairs}
        for owner, face in faces.items():
            hits = [owners[link] for link in face if link in owners]
            assert len(set(hits)) <= 1
            assert (len(hits) == 2) == (owner in pairs)
            if len(hits) == 2:
                assert hits[0] == owner
            if hits:
                touched[hits[0]].append(owner)
                if owner[1:] == hits[0][1:]:
                    incidences[owner] += 1
        for face, neighbours in touched.items():
            assert len(neighbours) == 7
            assert sum(other[1:] == face[1:] for other in neighbours) == 3
            for (x, _, _), (y, _, _) in combinations(neighbours, 2):
                assert all(min((a-b)%n, (b-a)%n) <= 1 for a,b in zip(x,y))
    assert set(incidences.values()) == {3}
    return len(faces)


def mul(a, b):
    return np.r_[a[0]*b[0] - a[1:]@b[1:],
                 a[0]*b[1:] + b[0]*a[1:] + np.cross(a[1:], b[1:])]


def spacetime_control(n, period, lag):
    """Enumerate four-dimensional faces and the actual length-two coarse paths."""
    extents=(n,n,n,period)
    def step(p,k):
        return tuple((a+(j==k))%extents[j] for j,a in enumerate(p))
    owners={}
    for p in product(*(range(size) for size in extents)):
        if p[3] not in (0,lag):
            continue
        for i,j in combinations(range(3),2):
            base=(p,i,j)
            colour=i,j,tuple(v%2 for v in p[:3])
            for edge in ((p if p[j]%2 else step(p,j),i),(p if p[i]%2 else step(p,i),j)):
                assert colour not in owners.setdefault(edge,{})
                owners[edge][colour]=base
    contacts=0
    for p in product(*(range(size) for size in extents)):
        if all(v%2==0 for v in p[:3]):
            for i in range(3):
                assert (p,i) not in owners and (step(p,i),i) not in owners
        for i,j in combinations(range(4),2):
            hits={}
            for edge in ((p,i),(step(p,j),i),(p,j),(step(p,i),j)):
                for colour,face in owners.get(edge,{}).items():
                    hits.setdefault(colour,set()).add(face)
            contacts+=sum(len(faces)>1 for faces in hits.values())
    return contacts


def unit(rng):
    q = rng.normal(size=4)
    return q / np.linalg.norm(q)


def mixed(rng, count=32):
    for _ in range(count):
        u, v, w, outside_u, outside_v = [unit(rng) for _ in range(5)]
        c, cu, cv = rng.normal(size=(2, 3)).T @ np.array([1, 1j])
        beta = rng.uniform(1, 45)
        h = 1 / (4*np.sqrt(beta))
        z = mul(mul(v, w), u)
        basis_sum = 0
        for a, b in product(np.eye(4)[1:], repeat=2):
            diff = 0j
            for s, t in product((-1, 1), repeat=2):
                us = mul(u, np.cos(h)*np.eye(4)[0] + s*np.sin(h)*a)
                tv = mul(np.cos(h)*np.eye(4)[0] + t*np.sin(h)*b, v)
                energy = beta*(c*(1-mul(mul(us,tv),w)[0]) + cu*(1-us@outside_u) + cv*(1-tv@outside_v))
                diff += s*t*energy
            scalar = mul(mul(u, mul(a,b)), mul(v,w))[0]
            np.testing.assert_allclose(diff, -4*c*beta*np.sin(h)**2*scalar, atol=2e-12)
            basis_sum += scalar**2
        np.testing.assert_allclose(basis_sum, 2+z[0]**2, atol=1e-12)
        hface = mul(mul(u,v),w)
        # Reversing the same closed loop duplicates its real trace.
        np.testing.assert_equal(hface[0] - (hface*np.array([1,-1,-1,-1]))[0], 0)


def half_band(rng):
    for n in (6, 8, 10, 12):
        freq = np.fft.fftfreq(n)
        coords = np.indices((n,n,n))
        odd = (coords[1] + coords[2]) % 2 == 1
        modes = rng.normal(size=odd.shape) + 1j*rng.normal(size=odd.shape)
        modes[:, (freq < -.25) | (freq >= .25), :] = 0
        c = np.fft.ifftn(modes, norm="ortho")
        actual = 2*np.vdot(c[odd], np.roll(c, 1, axis=1)[odd]).real
        np.testing.assert_allclose(actual, np.sum(abs(modes)**2 * np.cos(2*np.pi*freq)[None,:,None]), atol=2e-11)
    # Deliberately include both boundary planes on a multiple of four.
    n=8
    modes=np.zeros((n,n,n),complex)
    modes[0,2,0], modes[0,6,4] = 1, 1j
    c=np.fft.ifftn(modes,norm="ortho")
    x,y,z=np.indices(c.shape)
    odd=(y+z)%2==1
    assert abs(2*np.vdot(c[odd],np.roll(c,1,axis=1)[odd]).real) > 1


def gaussian():
    for n in (8, 16, 32):
        size=n*n
        volume=n**3
        target=(volume/size)**.5
        amp=n**-4
        mass=amp/(2*target)
        axis=4*np.sin(np.pi*np.fft.fftfreq(n))**2
        s=mass**2 + axis[:,None,None]+axis[None,:,None]+axis[None,None,:]
        eigen=amp/np.sqrt(s*(s+4))
        g=np.fft.ifftn(eigen).real
        assert g.min() > -1e-12
        c=np.exp(-g[0,0,0])*np.sinh(g)
        assert c.sum() >= np.exp(-g[0,0,0])*eigen[0,0,0]-1e-12
        assert np.fft.fftn(c).real.min() >= -1e-12
        print("bounded scalar",n,"contact",float(c[0,0,0]),"susceptibility",float(c.sum()))


if __name__ == "__main__":
    print("coloured spatial faces", [(n,geometry(n)) for n in (6,8,10)])
    assert spacetime_control(6,6,2)==spacetime_control(6,6,4)==0
    assert spacetime_control(6,6,1)>0 and spacetime_control(6,6,5)>0
    rng=np.random.default_rng(7135)
    mixed(rng)
    half_band(rng)
    gaussian()
    print("All controls passed.")
