"""SU(2) three-matrix commutator-model Monte Carlo via Euler angles (no quaternions).

PASS PREDICATES (stated before running):
 P0: control I1(1)/I0(1) from series matches 0.565159 within 1e-6.
 P1: Z(1) in (0,1]  (V>=0 so exp(-V)<=1).
 P2: Z(0.01) and Z(0.001) within 4 standard errors of 1 (Z->1 as beta->0).
 P3: |X(0.001)| and |X(0.01)| within 4 standard errors of 0 (X->0).
 P4: Euler range check: a in [0,2pi), cos b uniform [-1,1], c in [0,4pi) gives
     Haar measure; checked numerically via <chi_1(U)>=0 ... and <|TrU|^2>=1 within 4 se.
Samples N=2,000,000 per matrix triple, seed 12345; same samples reused for all betas
(common random numbers, so the betas' estimates are correlated).
Result files opened mode 'x' (never overwritten).
"""
import numpy as np
from math import factorial

def I(n, x, M=40):
    return sum((x/2)**(2*m+n)/(factorial(m)*factorial(m+n)) for m in range(M))

ctrl = I(1, 1.0)/I(0, 1.0)
with open('control.txt', 'x') as f:
    f.write('%.6f\n' % ctrl)

rng = np.random.default_rng(12345)
N = 2_000_000

def haar(n):
    a = rng.uniform(0, 2*np.pi, n)
    cb = rng.uniform(-1, 1, n)
    c = rng.uniform(0, 4*np.pi, n)
    b = np.arccos(cb)
    def rz(t):
        U = np.zeros((n, 2, 2), complex)
        U[:, 0, 0] = np.exp(1j*t/2); U[:, 1, 1] = np.exp(-1j*t/2)
        return U
    Ry = np.zeros((n, 2, 2), complex)   # exp(i b sy/2) = cos(b/2) + i sin(b/2) sy
    Ry[:, 0, 0] = np.cos(b/2); Ry[:, 1, 1] = np.cos(b/2)
    Ry[:, 0, 1] = np.sin(b/2); Ry[:, 1, 0] = -np.sin(b/2)
    return rz(a) @ Ry @ rz(c)

def inv(U):
    return np.conj(np.swapaxes(U, 1, 2))

U = [haar(N) for _ in range(3)]
def comm(A, B):
    return A @ B @ inv(A) @ inv(B)
def reTr(M):
    return (M[:, 0, 0] + M[:, 1, 1]).real
S = sum(1 - 0.5*reTr(comm(U[i], U[j])) for i, j in ((0, 1), (0, 2), (1, 2)))
chi = lambda A: np.abs(A[:, 0, 0] + A[:, 1, 1])**2 - 1
c1c2 = chi(U[0])*chi(U[1])
det_err = max(np.abs(np.linalg.det(u[:1000]) - 1).max() for u in U)

def est(x):
    return x.mean(), x.std(ddof=1)/np.sqrt(len(x))

lines = ['# Results (N=%d, seed 12345, Euler angles)' % N, '',
         'control I1(1)/I0(1) = %.6f' % ctrl, 'max |det-1| (sample) = %.2e' % det_err, '']
fails = []
def check(name, ok, msg):
    if not ok:
        fails.append('FAILED %s: %s' % (name, msg))
if abs(ctrl - 0.565159) >= 1e-6: check('P0', False, 'control %.6f' % ctrl)
m, e = est(chi(U[0])**0*np.abs(U[0][:, 0, 0] + U[0][:, 1, 1])**2)
lines.append('Haar check <|TrU|^2> = %.5f +- %.5f (expect 1)' % (m, e))
check('P4', abs(m-1) < 4*e, '<|TrU|^2>=%.5f+-%.5f' % (m, e))
m2, e2 = est(chi(U[0]))
lines.append('Haar check <chi_1> = %.5f +- %.5f (expect 0)' % (m2, e2))
check('P4', abs(m2) < 4*e2, '<chi1>=%.5f+-%.5f' % (m2, e2))
lines.append('')
for beta in (1.0, 0.01, 0.001):
    w = np.exp(-beta*S)
    Z, eZ = est(w)
    X, eX = est(c1c2*w)
    lines.append('beta=%g: Z = %.6f +- %.6f ; X = %.6f +- %.6f' % (beta, Z, eZ, X, eX))
    if beta == 1.0:
        check('P1', 0 < Z <= 1, 'Z(1)=%.6f' % Z)
    else:
        check('P2', abs(Z-1) < 4*eZ, 'beta=%g Z=%.6f+-%.6f (%.1f se from 1)' % (beta, Z, eZ, abs(Z-1)/eZ))
        check('P3', abs(X) < 4*eX, 'beta=%g X=%.6f+-%.6f (%.1f se from 0)' % (beta, X, eX, abs(X)/eX))
lines += [''] + (fails if fails else ['All predicates passed.'])
with open('results.md', 'x') as f:
    f.write('\n'.join(lines) + '\n')
print('\n'.join(lines))
