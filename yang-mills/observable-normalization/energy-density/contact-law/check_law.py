"""Independent checks for radial coupling, local Maxwell covariance, and contact modes."""
from itertools import combinations, product

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.stats import gamma


def radial_check():
    # For small R retain the physical upper endpoint. For very large R the omitted
    # gamma tail above 45 is negligible at the precision shown.
    ps = (np.arange(32768)+.5)/32768
    gamma_source = gamma.ppf(ps, 1.5)
    for R in [.25, 1., 6., 30., 120.]:
        ymax = min(2*R, 45.)
        theta = np.linspace(0, np.pi/2, 36001)
        y = ymax*np.sin(theta)**2
        density = np.sqrt(y*np.maximum(0., 1-y/(2*R)))*np.exp(-y)
        cdf = cumulative_trapezoid(density, y, initial=0)
        cdf /= cdf[-1]
        sample = np.interp(ps, cdf, y)
        assert np.max(sample-gamma_source) < 1e-7
        error = np.var(sample-gamma_source)
        assert error < min(15/4,105/(16*R))
        print("radial R, centered quantile squared error", R, error)


def fourier_coefficient(n):
    angles = 2*np.pi*np.arange(n)/n
    a = 2-2*np.cos(angles)
    den3 = a[:,None,None]+a[None,:,None]+a[None,None,:]
    # The zero Fourier mode is omitted in this known-answer lattice control.
    return sum((x*x/(den3+x)).mean() for x in a if x)/n


def simulate_exact_curl(n=14, repeats=12):
    rng = np.random.default_rng(12327)
    keys = [(0,j) for j in (1,2,3)]
    symbols = np.meshgrid(*[np.exp(2j*np.pi*np.arange(n)/n)-1]*4, indexing="ij", sparse=True)
    energy = sum(abs(a)**2 for a in symbols)
    inv = np.zeros_like(energy)
    inv[energy>0] = 1/np.sqrt(energy[energy>0])
    # Construct the exact two-form from a potential with four independent modes.
    # Apply signed differences in position space to make the three local sums.
    gram = np.zeros((3,3))
    for _ in range(repeats):
        modes=[np.fft.fftn(rng.normal(size=energy.shape))*inv for _ in range(4)]
        rows=[]
        for i,j in keys:
            face=np.fft.ifftn(symbols[i]*modes[j]-symbols[j]*modes[i]).real
            rows.append((np.roll(face,1,axis=j)-face).ravel())
        rows=np.array(rows)
        rows-=rows.mean(axis=0)
        gram+=rows@rows.T/(n**4*repeats)
    P=np.eye(3)-np.ones((3,3))/3
    assert np.max(abs(gram-fourier_coefficient(n)*P)) < .011
    return gram


def mask_check():
    # Stripes of four cells and one omitted column at each end. Mixed orientations
    # touch neither side of a seam. Include the periodic last-to-first seam.
    dims=(16,4,4,4)
    def shifted(x,j):
        y=list(x)
        y[j]=(y[j]+1)%dims[j]
        return tuple(y)
    chosen=set()
    for x in product(*(range(n) for n in dims)):
        i=(x[0]//4)%4
        if 1<=x[0]%4<3 and sum(x[j] for j in range(4) if j!=i)%2==0:
            chosen.add((x,i))
    for x in product(*(range(n) for n in dims)):
        for i,j in combinations(range(4),2):
            face={(x,i),(shifted(x,j),i),(x,j),(shifted(x,i),j)}
            assert len(chosen & face)<=1
    print("mixed mask, selected links by orientation",*[sum(j==i for _,j in chosen) for i in range(4)])


def main():
    radial_check()
    d=fourier_coefficient(64)
    assert abs(d-fourier_coefficient(48)) < 2e-7 and .5 < d < 2
    gram=simulate_exact_curl()
    pairs=list(combinations(range(4),2))
    incidence=np.array([[float(i in p) for p in pairs] for i in range(4)])
    G=d*np.eye(6)/8+(1-d)*incidence.T@incidence/48
    targets=[1/8]+[(1+2*d)/24]*3+[d/8]*2
    assert np.max(abs(np.linalg.eigvalsh(G)-np.sort(targets)))<1e-12
    assert np.linalg.eigvalsh(G)[0] > 1/16
    assert np.max(abs(G@np.ones(6)-np.ones(6)/8))<1e-12
    print("Fourier d and contrast Gram error",d,np.max(abs(gram-fourier_coefficient(14)*(np.eye(3)-np.ones((3,3))/3))))
    print("scalar, three orientation differences, two zero-row-sum eigenvalues",targets[0],targets[1],targets[-1])
    mask_check()


if __name__ == "__main__":
    main()
