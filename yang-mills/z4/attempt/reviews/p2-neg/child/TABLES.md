# Tables to be checked (every number must be found in a file of src/)

Each row lists numbers and the source file the writer took them from. "derived" means computed by the writer from source numbers (check the arithmetic).

## T1. Horizontal curvature kappa_H at equilibrium, periodic boxes (curvature route)
| program | L | beta | samples | kappa_H range | source |
|---|---|---|---|---|---|
| builder | 3 | 4, 6 | 8 each | -2.2 to -1.5 | a3-Acurv.PROOF.md S6 |
| builder | 3 | 12, 24, 48 | 4 each | -2.30 to -1.17 | a3-Acurv.PROOF.md S6 |
| builder | 4 | 4 | 2 | -1.60, -1.88 | a3-Acurv.PROOF.md S6 |
| builder | 4 | 6 | 2 | -1.53, -1.58 | a3-Acurv.PROOF.md S6 |
| challenger | 3 | 4 | (from 20 total at L=3) | -1.46 to -1.79 | a4-chalcurv.report.md A2 |
| challenger | 3 | 6 | | -1.39 to -1.96 | a4-chalcurv A2 |
| challenger | 3 | 12 | | -1.12 to -1.52 | a4-chalcurv A2 |
| challenger | 3 | 24 | | -1.12 to -1.93 | a4-chalcurv A2 |
| challenger | 3 | 48 | | -1.55 to -2.04 | a4-chalcurv A2 |
| challenger | 4 | 6 | 2 | -1.77, -1.26 | a4-chalcurv A2 |
| challenger | 4 | 24 | 2 | -1.15, -1.67 | a4-chalcurv A2 |
Claims: union of all ranges is [-2.30, -1.12] (derived). Samples with kappa_H >= 1/2: builder 0 of 32 (derived: 16+12+4), challenger 0 of 24. Ledger (A1_LEDGER.md) gives "-1.1 to -2.3"; builder report.md row S6 gives [-2.3, -1.2].
Open L=4 box (challenger): beta=4: -1.67 to -2.40; beta=6: +0.16, -0.32, -0.04; beta=12, 24, 48: +3, +9.6, +23.
Mechanism: k = 2.62, 2.51 (SU(2), ensemble G), c0 = 0.38-0.40, kappa_H(c=1) -> -1.62, -1.51; SU(3): k = 3.42, c0 = 0.44, relative deficit -2.28 vs -2.51 to -2.62; beta from 16 to 1024.
Pointwise: one plaquette at Q=-1 has eigenvalues 1-2beta (x3) and 1 (x9); 4D L=3 one link -1: 1 - 4.31 beta for beta = 1..6; SZZ criterion beta_W < 1/12; ||Hess V|| <= 12 beta_W on 76/76 samples, max about 6.6 beta_W; at L=3: lambda_min(B) = -6.4, -9.0, -12.2 vs kappa_H = -1.6, -2.0, -1.5 at beta = 12, 24, 48.

## T2. Vortex free energy F_L (vortex route), L = 2, 3, 4
| group | beta | F_2 | F_3 | F_4 | source |
|---|---|---|---|---|---|
| SU(2) | 1.8 | 0.69 +- 0.24 | -0.26 +- 0.28 | 0.49 +- 0.40 | a3-Avort.PROOF.md (iii) |
| SU(2) | 2.4 | 3.06 +- 0.42 | 1.55 +- 0.45 | 2.81 +- 0.95 | a3-Avort.PROOF.md (iii) |
| Z2 | 0.3 | 0.0774 | 0.0041 | 0.0061 (errors 0.002-0.005) | a3-Avort.report.md |
| Z2 | 0.6 | 3.205 | 8.244 | 15.84 (+-0.25) | a3-Avort.report.md |
Claim: at beta = 2.4, F(4) - F(3) = +1.26 +- 1.05 (1.2 standard errors). Exact 3D Z2 L=2: F(0.3) = 0.0325242683, F(0.6) = 0.6912790067.

## T3. Flux coupling z = L * m_eff(1), 4D lattices L^3 x 12, beta = 2.3 (finite-size route)
| L | z SU(2) | z U(1) | rotor model (post hoc) |
|---|---|---|---|
| 2 | 0.562 +- 0.016 | 0.335 +- 0.024 | 0.324 |
| 4 | 2.12 +- 0.06 | 0.553 +- 0.078 | 0.422 |
| 6 | 8.02 +- 0.40 | 0.684 +- 0.068 | 0.500 |
Source a3-Afs.PROOF.md TEST table. 1/(2 beta) = 0.217. Residuals 1.5 to 2.6 standard errors (a3-Afs.report.md). z_SU2(6)/z_U1(6) = 11.7.

## T4. Dual amplitudes (dual positivity route), d=3 periodic 2x1x1
4 negative, 141 positive, 584 zero, of 729 configurations; min A = -0.003086419753; Monte Carlo -0.002892 +- 0.000237 (seed 7, N = 4e7). One-site 3-torus: 27/27 positive. Source a7-wild.report.md.
c_j(beta) = 2(2j+1) I_{2j+1}(beta)/beta.

## T5. Hypothesis (C) free-field numbers (a3-C)
Lattice-local phi(0)^2: xi(1 - C(1)/C(0)) = 0.963 xi, C(1)/C(0) -> 0.0373 (xi = 4..256).
Flowed, s = 0.1: xi(1 - C(1)/C(0)) = 3.56, 4.13, 4.46, 4.64, 4.73, 4.78 at xi = 8, 16, 32, 64, 128, 256.
R(xi) for phi(0): 6.584, 5.921, 5.580, 5.522, 5.508, 5.505, 5.504 at xi = 4..256; continuum 5.503975; phi^2: 30.2937.

## T6. Three-spacing measurement (MATCHED_MEASUREMENT.md and A1_LEDGER.md)
| N | beta | a sqrt(sigma) | R(0) | R(1 step) | q = R(1)/R(0) (derived) | xi = 1/(3.74 a sqrt(sigma)) (derived) | xi(1-q) (derived) |
|---|---|---|---|---|---|---|---|
| 6 | 2.3 | 0.3690(30) | 3.751(42)e-2 | 1.012(32)e-2 | 0.270 | 0.72 | 0.53 |
| 8 | 2.4 | 0.2660(20) | 3.615(60)e-2 | 1.166(51)e-2 | 0.323 | 1.01 | 0.68 |
| 12 | 2.5 | 0.1905(8) | 3.233(61)e-2 | 1.245(51)e-2 | 0.385 | 1.40 | 0.86 |
Configurations: 1500 at N = 8; 840 rows / 834 distinct at N = 12 (3 seeds; each added seed repeats IDs 40-42). Glueball 3.74(12) sqrt(sigma). Growth exponent about 0.75 (derived).

## T7. Calibration of (E) on Ising models (c1-E.report.md, HYPOTHESIS_E.md)
Free field d=4, L=8, m=0.25, 4000 samples: U4 = 0.007 +- 0.025, g_R = 0.34 +- 1.20, xi2 = 4.023 +- 0.046, block kappa4/kappa2^2 = -0.19 +- 0.07.
4D Ising, xi2/L = 0.25: g_R = 67 +- 9, 46 +- 8, 32 +- 7 at L = 6, 8, 12. xi/L about 0.33: 36 +- 2, about 29, 22 +- 2, 20 +- 3 at L = 6, 8, 12, 16. Seeds 2001..2017.
2D Ising at K_c: U4 = 0.6115, 0.6107 (child, L = 16, 32); 0.6111 +- 0.0005, 0.6098 +- 0.0007 (worker, L = 16, 32); literature 0.61069 (from memory). g_R about 2.2.
chi^2_3: kappa4/kappa2^2 = 12/k = 4.

## T8. 5D SU(2) (c1-excl.report.md)
beta_c about 1.64; hysteresis on 4^5: 0.090 +- 0.003 at beta = 1.6; 0.018 at 1.7; below 0.002 at 1.3, 1.5, 1.9, 2.2; 200 Metropolis sweeps, one seed per start. Plaquette beta = 2.2: 0.6925 vs 0.7273; beta = 1.9: 0.630 vs 0.684.
