"""qcheck.py - known-answer checks for Q1 (2D YM gaps, convention conversion) and Q3 (plaquette PT).

Conventions (Z4, input/Z4_README_sections.md sec. 2): L = g = 1, circle of N links, a = 1/N,
U(1) beta = N^2, SU(2) beta = 4 N^2; physical gap M = -N^2 ln(lambda_1/lambda_0), with
U(1) ratio I_1(beta)/I_0(beta), SU(2) (spin 1/2 over spin 0) ratio I_2(beta)/I_1(beta).

Predicates (fixed before first run):
 A1: U(1) M(64) equals Z4's printed 0.500061048820 within 1e-11 (tolerance: Z4 printed 12 decimals).
 A2: SU(2) M(64) equals Z4's printed 0.375011444266 within 1e-11 (same source of tolerance).
 A3: the Casimir-times-coupling product e^2 C2(fund SU(2)) is the same in the two conventions found in
     the sources: (i) T_a = sigma_a/2 orthonormal for 2 tr, e^2 = g^2 (standard lattice convention,
     beta = 2N/g^2); (ii) T_a = i sigma_a/sqrt2 orthonormal for -tr (Witten 1992 p.60, C2 = (n^2-1)/2),
     where keeping (1/4e^2)<F,F> fixed forces e^2 = g^2/2. Equality to 1e-14 (float64 roundoff), and
     e^2 L C2 / 2 = 3/8 within 1e-14.  Also U(1) charge 1: g^2 L * 1 / 2 = 1/2.
 A4: the continuum limit: beta*(-ln(I_{nu+1}/I_nu)) at beta = 1e6 equals (2 nu + 1)/2 within 1e-5
     (tolerance: next asymptotic term is O(1/beta) = 1e-6 times a coefficient of order one).
     nu = 0 gives U(1) gap 1/2 on beta = N^2; nu = 1 gives 3/2, i.e. 3/8 on beta = 4N^2.
 M1 (measured only): lattice PT for SU(2), d = 4 (Karsch et al. hep-lat/9605031 eq. 3.1 p.6):
     c1 = 3 I, I = (1/4)(1 - 1/V); c2 = (5*3/6) I^2 + 48 alpha_4, alpha_4 = -0.000103 (infinite lattice);
     c3 = 0.143055 (quoted there from its ref. [14]). Prediction for beta^2 (1 - 3/(4 beta) - P) at
     beta = 8 on V = 8^4 through O(beta^-3), compared with Z4's measured 0.172(1).
Exit code 0 if A1-A4 all met, else 1. Result file never overwritten.
Usage: python -I qcheck.py <site-packages dir> <out file>
"""
import sys, os, json
sys.path.append(sys.argv[1])
import mpmath as mp
import numpy as np
out = sys.argv[2]
if os.path.exists(out):
    sys.exit("refuse to overwrite " + out)
mp.mp.dps = 50
res, fails = {}, []
def gap(nu, beta, N):
    return -N**2 * mp.log(mp.besseli(nu + 1, beta) / mp.besseli(nu, beta))
u = gap(0, mp.mpf(64)**2, 64); s = gap(1, 4 * mp.mpf(64)**2, 64)
res['A1'] = (mp.nstr(u, 15), abs(u - mp.mpf('0.500061048820')) < 1e-11)
res['A2'] = (mp.nstr(s, 15), abs(s - mp.mpf('0.375011444266')) < 1e-11)
# A3
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
Ts = [x / 2 for x in sig]; Tw = [1j * x / np.sqrt(2) for x in sig]
ons = max(abs(2 * np.trace(a @ b) - (i == j)) for i, a in enumerate(Ts) for j, b in enumerate(Ts))
onw = max(abs(-np.trace(a @ b) - (i == j)) for i, a in enumerate(Tw) for j, b in enumerate(Tw))
C2s = sum(a @ a for a in Ts)[0, 0].real; C2w = -sum(a @ a for a in Tw)[0, 0].real
g2 = 1.0; L = 1.0
e2s, e2w = g2, g2 / 2
gs, gw = e2s * L * C2s / 2, e2w * L * C2w / 2
a3 = ons < 1e-14 and onw < 1e-14 and abs(gs - gw) < 1e-14 and abs(gs - 0.375) < 1e-14 and abs(g2 * L / 2 - 0.5) < 1e-14
res['A3'] = (dict(C2_std=C2s, C2_witten=C2w, gap_std=gs, gap_witten=gw, naive_mix_e2std_C2witten=e2s * L * C2w / 2), a3)
# A4
b = mp.mpf(10)**6
r0 = b * -mp.log(mp.besseli(1, b) / mp.besseli(0, b)); r1 = b * -mp.log(mp.besseli(2, b) / mp.besseli(1, b))
res['A4'] = ((mp.nstr(r0, 12), mp.nstr(r1, 12)), abs(r0 - 0.5) < 1e-5 and abs(r1 - 1.5) < 1e-5)
# M1
V = 8**4; I = 0.25 * (1 - 1 / V); beta = 8.0
c1 = 3 * I; c2 = 2.5 * I**2 + 48 * (-0.000103); c3 = 0.143055
pred = beta**2 * (c1 / beta - 0.75 / beta) + c2 + c3 / beta
res['M1'] = dict(c1=c1, c2=c2, c2_inf=2.5 / 16 + 48 * (-0.000103), finite_V_shift=beta**2 * (c1 - 0.75) / beta,
                 pred_through_beta3=pred, z4_measured=0.172, diff=0.172 - pred, implied_c4_if_all_from_beta4=(0.172 - pred) * beta**2)
for k in ('A1', 'A2', 'A3', 'A4'):
    print(k, res[k]);  fails += [] if res[k][1] else [k]
print('M1', res['M1'])
print('met', 4 - len(fails), 'failed', len(fails), fails, 'measured only 1')
with open(out, 'w') as f:
    json.dump({k: str(v) for k, v in res.items()}, f, indent=1)
sys.exit(1 if fails else 0)
