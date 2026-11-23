# Report: ell-scaling test of C_b, V, v

Control: sum 1/n^4 = 1.082323 (= pi^4/90). Results file: results_run3.json (run1/run2 are truncated crash outputs from a JSON numpy-bool serialization bug; kept, not overwritten; fix was casts only).

## Predicates (from scaling.py docstring, fixed before run1)
- P1 (C_b scales as lambda^-2, tol 1e-10): **MET**, 0/36 comparisons fail, max rel err 0.0
- P2 (V, v scale as lambda^-2, b0 as lambda, tol 1e-12): **MET**, 0/54 fail, max rel err 0.0 (lambda = 0.5, 2 are exact powers of 2, so the scaling is bit-exact in floating point)
- P3: qualifying cases (b <= b0): **27/27**; v <= C_b(2tau) and C_b(tau) <= V hold in all 27: **MET**. Cases with b > b0 (measured only): 0.
- Totals: met 3, failed 0, measured-only 0 cases.
- Margins: V/C_b(tau) in [3.27e6, 1.27e9] (upper bound extremely loose); C_b(2tau)/v in [5.86, 563] (tightest at N=12, tau=0.3 ell).

## Accuracy
int f and ||f||_1 (f>0 so equal): unit-cube value 1.406728540904221, identical to all digits at 64^3/96^3/128^3 (trapezoid on analytic periodic function, spectral). D4 (unit cube, 96^3): 28399.37; 64^3: 28398.60, 128^3: 28399.70. |Lap^2 g| has kinks at zeros, so convergence ~h^2; Richardson estimate ~28400.1, i.e. 96^3 value accurate to ~3e-5 relative. b0 depends on D4^(-1/4) (~1e-5 rel), F on D4 linearly via a term small relative to ||f||_1; no conclusion is near that sensitivity. C_b is an exact finite sum (FFT for D, direct 1728x1728 position-space double sum), floating-point only.

## Table
| ell | N | tau | b | b0 | C_b(tau) | V(tau) | C_b(2tau) | v(tau) |
|---|---|---|---|---|---|---|---|---|
| 0.5 | 6 | 0.025 | 0.0833 | 0.1098 | 3.51459e+04 | 4.4461e+13 | 8.46773e+03 | 3.7799e+01 |
| 0.5 | 6 | 0.050 | 0.0833 | 0.1098 | 8.46773e+03 | 2.7311e+11 | 6.47888e+02 | 1.2656e+01 |
| 0.5 | 6 | 0.150 | 0.0833 | 0.1098 | 7.40980e+01 | 2.4243e+08 | 6.28887e-01 | 8.3044e-02 |
| 0.5 | 9 | 0.025 | 0.0556 | 0.1098 | 1.29976e+05 | 4.4461e+13 | 1.70499e+04 | 3.7799e+01 |
| 0.5 | 9 | 0.050 | 0.0556 | 0.1098 | 1.70499e+04 | 2.7311e+11 | 6.09902e+02 | 1.2656e+01 |
| 0.5 | 9 | 0.150 | 0.0556 | 0.1098 | 5.71038e+01 | 2.4243e+08 | 5.17828e-01 | 8.3044e-02 |
| 0.5 | 12 | 0.025 | 0.0417 | 0.1098 | 2.72679e+05 | 4.4461e+13 | 2.12798e+04 | 3.7799e+01 |
| 0.5 | 12 | 0.050 | 0.0417 | 0.1098 | 2.12798e+04 | 2.7311e+11 | 5.19263e+02 | 1.2656e+01 |
| 0.5 | 12 | 0.150 | 0.0417 | 0.1098 | 5.10208e+01 | 2.4243e+08 | 4.86846e-01 | 8.3044e-02 |
| 1.0 | 6 | 0.050 | 0.1667 | 0.2197 | 8.78647e+03 | 1.1115e+13 | 2.11693e+03 | 9.4498e+00 |
| 1.0 | 6 | 0.100 | 0.1667 | 0.2197 | 2.11693e+03 | 6.8278e+10 | 1.61972e+02 | 3.1641e+00 |
| 1.0 | 6 | 0.300 | 0.1667 | 0.2197 | 1.85245e+01 | 6.0608e+07 | 1.57222e-01 | 2.0761e-02 |
| 1.0 | 9 | 0.050 | 0.1111 | 0.2197 | 3.24940e+04 | 1.1115e+13 | 4.26246e+03 | 9.4498e+00 |
| 1.0 | 9 | 0.100 | 0.1111 | 0.2197 | 4.26246e+03 | 6.8278e+10 | 1.52476e+02 | 3.1641e+00 |
| 1.0 | 9 | 0.300 | 0.1111 | 0.2197 | 1.42760e+01 | 6.0608e+07 | 1.29457e-01 | 2.0761e-02 |
| 1.0 | 12 | 0.050 | 0.0833 | 0.2197 | 6.81697e+04 | 1.1115e+13 | 5.31994e+03 | 9.4498e+00 |
| 1.0 | 12 | 0.100 | 0.0833 | 0.2197 | 5.31994e+03 | 6.8278e+10 | 1.29816e+02 | 3.1641e+00 |
| 1.0 | 12 | 0.300 | 0.0833 | 0.2197 | 1.27552e+01 | 6.0608e+07 | 1.21712e-01 | 2.0761e-02 |
| 2.0 | 6 | 0.100 | 0.3333 | 0.4393 | 2.19662e+03 | 2.7788e+12 | 5.29233e+02 | 2.3624e+00 |
| 2.0 | 6 | 0.200 | 0.3333 | 0.4393 | 5.29233e+02 | 1.7070e+10 | 4.04930e+01 | 7.9102e-01 |
| 2.0 | 6 | 0.600 | 0.3333 | 0.4393 | 4.63113e+00 | 1.5152e+07 | 3.93054e-02 | 5.1902e-03 |
| 2.0 | 9 | 0.100 | 0.2222 | 0.4393 | 8.12350e+03 | 2.7788e+12 | 1.06562e+03 | 2.3624e+00 |
| 2.0 | 9 | 0.200 | 0.2222 | 0.4393 | 1.06562e+03 | 1.7070e+10 | 3.81189e+01 | 7.9102e-01 |
| 2.0 | 9 | 0.600 | 0.2222 | 0.4393 | 3.56899e+00 | 1.5152e+07 | 3.23642e-02 | 5.1902e-03 |
| 2.0 | 12 | 0.100 | 0.1667 | 0.4393 | 1.70424e+04 | 2.7788e+12 | 1.32999e+03 | 2.3624e+00 |
| 2.0 | 12 | 0.200 | 0.1667 | 0.4393 | 1.32999e+03 | 1.7070e+10 | 3.24540e+01 | 7.9102e-01 |
| 2.0 | 12 | 0.600 | 0.1667 | 0.4393 | 3.18880e+00 | 1.5152e+07 | 3.04279e-02 | 5.1902e-03 |

PCP: checks K1 (exit 1, expected 0: the crash) and K2 (exit 0, expected 0).
Verify last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
