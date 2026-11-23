"""run_a4.py -- A4/A5: kappa_H for controlled small fluctuations around U=1 with beta*eps^2 = c fixed.
usage: python3 run_a4.py N L bc ens nseed betas(comma) cs(comma)  -> result_a4_SU{N}_L{L}{bc}_{ens}.txt (mode x)
 ens = W : white noise, U_e = exp(eps X_e), X_e = sum_a x_a e_a, x_a ~ N(0,1), eps = sqrt(c/beta).
 ens = G : 'perturbative equilibrium without torons': t = sqrt(c) * sum_k xi_k phi_k / sqrt(beta*lambda_k) over horizontal
           eigenvectors of the curl form C = HessV(U=1)/beta with lambda_k > 1e-8 (torons/zero modes set to 0);
           c=1 is the Gaussian (one-loop) equilibrium of the non-toron modes.  U_e = exp(t_e) U=1.
 Seeds: 7919*seed + 31*N + L (independent of beta and c so the same direction pattern is rescaled: X fixed, eps varies).
Predicates (fixed before first run):
 M1 (convergence) for each (c, seed): |kH(beta_max) - kH(beta_prev)| <= 0.1 * Ric  -- i.e. kH tends to a
    c-dependent constant (tolerance: the expected correction is O(sqrt(c/beta)) relative, ~3% at beta=1024/256).
 M2 (sign, the file's claim restated) for c=1 on periodic boxes: limit kH < 0.
 Measured only: k = (Ric - kH)/c at beta_max, c0 = Ric/k (c where deficit equals Ric), the action density
    beta*<1 - ReTr Q/N> of the ensemble (equilibrium one-loop value: (N^2-1)/(4)= 0.75 for SU2, 2.0 for SU3),
    zero-momentum weight of the lowest eigenvector (no gauge fixing: the configurations are already near U=1).
"""
import sys, numpy as np
from lat import *

N, L, bc, ens, nseed = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4], int(sys.argv[5])
betas = [float(x) for x in sys.argv[6].split(',')]; cs = [float(x) for x in sys.argv[7].split(',')]
lat = Lattice(L, periodic=(bc == 'p'))
E = basis(N); D = len(E); Ric = N / 2
out = open(f'result_a4_SU{N}_L{L}{bc}_{ens}.txt', 'x')
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s + '\n'); out.flush()
say(f'SU({N}) L={L} bc={bc} ens={ens} nE={lat.nE} Ric={Ric}')
I = np.array([np.eye(N, dtype=complex)] * lat.nE)
if ens == 'G':
    C = hessV(lat, I, 1.0, N)
    Nh, r, _ = horizontal_basis(gauge_matrix(lat, I, N))
    lam, phi = np.linalg.eigh(Nh.T @ C @ Nh)
    keep = lam > 1e-8
    say(f'curl form on horizontal: dim {len(lam)}, zero modes {int((~keep).sum())}, min nonzero {lam[keep].min():.4f}')
    modes = Nh @ phi[:, keep]; lamk = lam[keep]

def zmw(v):
    vv = v.reshape(lat.nE, D); w = 0.0
    for mu in range(lat.d):
        sel = lat.links[:, 2] == mu; m = vv[sel].mean(0); w += sel.sum() * (m @ m)
    return w / (v @ v)

fails = []; res = {}
for seed in range(nseed):
    rng = np.random.default_rng(7919 * seed + 31 * N + L)
    if ens == 'W':
        X = rng.normal(size=lat.nE * D)
    else:
        X = modes @ (rng.normal(size=len(lamk)) / np.sqrt(lamk))
    for c in cs:
        for beta in betas:
            t = np.sqrt(c / beta) * X
            U = expm_su(np.einsum('ea,aij->eij', t.reshape(lat.nE, D), E))
            r = kappa_H(lat, U, beta, N, want_vec=True)
            dev = beta * (1 - np.trace(plaquettes(lat, U), axis1=1, axis2=2).real / N).mean()
            res[(seed, c, beta)] = r['kH']
            say(f'seed={seed} c={c} beta={beta} kH={r["kH"]:.4f} (kH-Ric)/Ric={(r["kH"]-Ric)/Ric:.4f} '
                f'beta*dev={dev:.4f} zeroMomW={zmw(r["vec"]):.3f} nneg={int((r["wH"]<0).sum())} low4={np.round(r["wH"][:4],3).tolist()}')
        a, b = res[(seed, c, betas[-1])], res[(seed, c, betas[-2])]
        ok = abs(a - b) <= 0.1 * Ric
        k = (Ric - a) / c
        say(f'  M1 seed={seed} c={c}: kH {b:.4f} -> {a:.4f} ' + ('PASS' if ok else 'FAIL') + f' | k={(k):.4f} c0=Ric/k={Ric/k:.3f}')
        ok or fails.append(f'M1 s{seed} c{c}')
        if c == 1.0 and bc == 'p':
            ok2 = a < 0
            say(f'  M2 seed={seed}: limit kH(c=1)={a:.4f} <0 ' + ('PASS' if ok2 else 'FAIL'))
            ok2 or fails.append(f'M2 s{seed}')
say('FAILED predicates:', fails)
sys.exit(0)
