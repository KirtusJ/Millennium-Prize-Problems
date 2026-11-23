"""run_a1.py -- A1: validate my own Hess V and horizontal projection.

Predicates (fixed before first run):
 P1 FD: on 4D L=3 periodic SU(2), random config (seed 1), beta=3: for 6 random pairs of unit directions
    v,w the polarised central FD second derivative (V(v+w)-V(v-w) along geodesics, step h=1e-3) agrees with
    v^T H w to abs err <= 1e-5 * max(1,|H|_2).  Tolerance: FD truncation O(h^2 * |V'''|) ~ 1e-6*beta*nP-ish
    per direction on unit vectors plus rounding eps*|V|/h^2 ~ 1e-16*1e3/1e-6 = 1e-7; 1e-5 relative gives margin.
 P2 One plaquette (open 2D L=2 box = one plaquette), Q=-1 (U1=-1): spectrum of B at beta in {1,3}
    = {1-2beta x3, 1 x9} to 1e-10 (double precision rounding).
 P3 U=1 on 4D L=3 periodic: rank G = 3*81-3 = 240 (non-generic kernel: constant omega), kappa_H = 1 to 1e-9.
    Also rank G = 3*81 = 243 on the random config (generic).
 P4 One plaquette Q=-1: kappa_H (horizontal) = 1-2beta, i.e. the three negative modes are horizontal (file S5).
 P5 SU(3) one plaquette at Q = exp(i*2pi/3)*1 (center element): measured only; FD check of SU(3) H on
    4D L=3 random config same as P1 (predicate, same tolerance).
"""
import sys, numpy as np
from lat import *

out = open('result_a1.txt', 'x')
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s + '\n'); out.flush()

fails = []
def fd_check(lat, U, beta, N, rng, npair=6, h=1e-3):
    E = basis(N); D = len(E)
    H = hessV(lat, U, beta, N)
    nrm = np.linalg.norm(H, 2)
    errs = []
    for _ in range(npair):
        v = rng.normal(size=lat.nE * D); v /= np.linalg.norm(v)
        w = rng.normal(size=lat.nE * D); w /= np.linalg.norm(w)
        def f(z):
            T = np.einsum('ea,aij->eij', z.reshape(lat.nE, D), E)
            return action(lat, expm_su(T) @ U, beta, N)
        def d2(z):
            return (f(h * z) - 2 * f(0 * z) + f(-h * z)) / h ** 2
        fd = (d2(v + w) - d2(v - w)) / 4
        errs.append(abs(fd - v @ H @ w))
    return max(errs), nrm

rng = np.random.default_rng(1)
lat = Lattice(3)
say('lattice L=3 4D periodic: nE', lat.nE, 'nS', lat.nS, 'nP', lat.nP, 'batches', len(lat.batches))
U = expm_su(np.einsum('ea,aij->eij', rng.normal(size=(lat.nE, 3)), basis(2)))
e, nrm = fd_check(lat, U, 3.0, 2, rng)
ok = e <= 1e-5 * max(1, nrm); say('P1 SU2 FD maxerr', e, '|H|2', nrm, 'PASS' if ok else 'FAIL'); ok or fails.append('P1')

one = Lattice(2, d=2, periodic=False)
say('one-plaquette box: nE', one.nE, 'nP', one.nP)
for beta in (1.0, 3.0):
    U1 = np.array([np.eye(2, dtype=complex)] * 4); U1[0] = -np.eye(2)
    H = hessV(one, U1, beta, 2)
    w = np.sort(np.linalg.eigvalsh(np.eye(12) + H))
    exp_ = np.sort([1 - 2 * beta] * 3 + [1] * 9)
    ok = np.abs(w - exp_).max() < 1e-10
    r = kappa_H(one, U1, beta, 2)
    say(f'P2 beta={beta} eig B', np.round(w, 12), 'PASS' if ok else 'FAIL'); ok or fails.append('P2')
    ok4 = abs(r['kH'] - (1 - 2 * beta)) < 1e-10
    say(f'P4 beta={beta} kappa_H', r['kH'], 'rankG', r['rankG'], 'dimH', r['dimH'], 'PASS' if ok4 else 'FAIL'); ok4 or fails.append('P4')

Uone = np.array([np.eye(2, dtype=complex)] * lat.nE)
r = kappa_H(lat, Uone, 3.0, 2)
ok = r['rankG'] == 240 and abs(r['kH'] - 1) < 1e-9
say('P3 U=1 L=3 beta=3: rankG', r['rankG'], 'kH', r['kH'], 'kfull', r['kfull'], 'PASS' if ok else 'FAIL'); ok or fails.append('P3a')
nz = int((np.abs(r['wH'] - 1) < 1e-9).sum())
say('   number of horizontal eigenvalues equal to Ric=1 at U=1 (zero modes of curl form, horizontal):', nz)
r = kappa_H(lat, U, 3.0, 2)
ok = r['rankG'] == 243
say('P3 random config: rankG', r['rankG'], 'PASS' if ok else 'FAIL'); ok or fails.append('P3b')

U3 = expm_su(np.einsum('ea,aij->eij', 0.7 * rng.normal(size=(lat.nE, 8)), basis(3)))
e, nrm = fd_check(lat, U3, 3.0, 3, rng)
ok = e <= 1e-5 * max(1, nrm); say('P5 SU3 FD maxerr', e, '|H|2', nrm, 'PASS' if ok else 'FAIL'); ok or fails.append('P5')
r = kappa_H(lat, np.array([np.eye(3, dtype=complex)] * lat.nE), 3.0, 3)
say('   SU3 U=1: kH', r['kH'], '(Ric=1.5) rankG', r['rankG'], '(expect 8*81-8=640)')
say('FAILED:', fails)
sys.exit(1 if fails else 0)
