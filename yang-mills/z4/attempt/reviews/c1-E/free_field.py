"""free_field.py -- worker c1-E (T6). Known-answer test (i) for formulations (E-a), (E-b).

Lattice free massive scalar field on the periodic torus L^4, action (1/2) sum phi (-Lap + m^2) phi.
Exact sampler: phi = IFFT( sqrt(V/(m^2+p_hat^2)) * complex white noise ), real part construction
via FFT of real white noise (exact Gaussian with the right covariance).

Same observables as ising_wolff.c: M = sum phi, F = (1/4) sum_mu |phi~(2pi e_mu/L)|^2,
U4 = 1 - <M^4>/(3<M^2>^2), xi2 = sqrt(<M^2>/F - 1)/(2 sin(pi/L)), gR = 3 U4 (L/xi2)^4.

PREDICATES (fixed before first run):
 P1a (PROVED analytically, here checked): M is a linear functional of a Gaussian field, so its
     fourth cumulant vanishes; U4 = 0 and gR = 0 exactly. MC check: |U4| < 4 sigma_jackknife.
     (tolerance: 4 sigma, a statistical bound only.)
 P1b exact: <M^2>/F - 1 = p_hat^2/m^2, so xi2 = 1/m exactly; MC check |xi2*m - 1| < 4 sigma.
 P1c the block-observable version of (E-b): normalized fourth cumulant of the block average of phi
     over a block of side L/2 also |kappa4/kappa2^2| < 4 sigma.
Seed fixed: 20261123. Output: results/free_L{L}_m{m}.txt opened with mode "x".
"""
import sys, numpy as np

def main(L=8, m=0.25, nsamp=4000, seed=20261123):
    rng = np.random.default_rng(seed)
    k = 2*np.pi*np.arange(L)/L
    ph2 = sum(np.meshgrid(*([4*np.sin(k/2)**2]*4), indexing="ij"))
    amp = 1/np.sqrt(m*m + ph2)
    M = np.empty(nsamp); F = np.empty(nsamp); B = np.empty(nsamp)
    for n in range(nsamp):
        w = rng.standard_normal((L,)*4)
        phi = np.real(np.fft.ifftn(np.fft.fftn(w)*amp))
        M[n] = phi.sum()
        ft = np.fft.fftn(phi)
        F[n] = (abs(ft[1,0,0,0])**2+abs(ft[0,1,0,0])**2+abs(ft[0,0,1,0])**2+abs(ft[0,0,0,1])**2)/4
        h = L//2
        B[n] = phi[:h,:h,:h,:h].mean()
    nb = 20; bs = nsamp//nb
    def stats(f):
        full = f(np.arange(nsamp)); jk = np.array([f(np.r_[0:b*bs, (b+1)*bs:nsamp]) for b in range(nb)])
        return full, np.sqrt((nb-1)/nb*((jk-jk.mean())**2).sum())
    U = lambda idx: 1 - (M[idx]**4).mean()/(3*(M[idx]**2).mean()**2)
    xi = lambda idx: np.sqrt((M[idx]**2).mean()/F[idx].mean()-1)/(2*np.sin(np.pi/L))
    kb = lambda idx: (lambda x: ((x**4).mean()-3*(x**2).mean()**2)/(x**2).mean()**2)(B[idx]-B[idx].mean())
    u, ue = stats(U); x, xe = stats(xi); c, ce = stats(kb)
    g = 3*u*(L/x)**4; ge = 3*ue*(L/x)**4
    res = dict(L=L, m=m, nsamp=nsamp, U4=u, U4err=ue, xi2=x, xi2err=xe, xi2_exact=1/m, gR=g, gRerr=ge,
               block_k4=c, block_k4err=ce,
               P1a=abs(u) < 4*ue, P1b=abs(x*m-1) < 4*xe*m, P1c=abs(c) < 4*ce)
    with open(f"results/free_L{L}_m{m}.txt", "x") as fh:
        fh.write(repr(res)+"\n")
    print(res)
    return 0 if (res["P1a"] and res["P1b"] and res["P1c"]) else 1

if __name__ == "__main__":
    sys.exit(main())
