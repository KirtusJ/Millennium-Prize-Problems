# T132 report: eps_eff(a) for the SU(2) fibre operator

**Control:** arccosh(3) = 1.762747 (control.txt).

## Hint verification
- Verified numerically (see results_eps_eff_run2.txt):
  - V_a = beta sin^2 a (1-t), max error 1.4e-14.
  - t is uniform under Haar. This is a Monte Carlo check only: mean t^2 = 0.33444 against 1/3, sigma 0.00047, seed 1.
  - P~_j are orthonormal for dt/2, Gram error 3.4e-13.
  - l_j from backward recurrence matches the direct Bessel series, relative error 2e-15.
  - M is symmetric to 1e-16.
- Not tested numerically:
  - Kernel positivity, so that the top eigenfunction is invariant. I took this from the Perron-Frobenius argument.
  - Commutation with U -> e^{i phi} U e^{i psi}. I took this from the fact that k is a class function (K commutes with translations) and V depends only on t.
  - That invariant functions in degree 2j are P_j(t). I took this from the Peter-Weyl structure, D^j_00 = P_j.
  - I did not diagonalise the full operator on non-invariant sectors. The reduction rests on the argument, not on a numerical check.

## eps_eff vs eps = 2 asinh(sin a)
Columns: eps_eff, then d = eps_eff - eps.

| a | eps | beta | eps_eff | d | d*sqrt(beta) | d*beta |
|---|---|---|---|---|---|---|
| 0.1 | 0.19933664 | 64 | 0.1840241980 | -1.5312e-02 | -0.1225 | -0.9800 |
| | | 256 | 0.1955978905 | -3.7388e-03 | -0.0598 | -0.9571 |
| | | 1024 | 0.1984069589 | -9.2968e-04 | -0.0298 | -0.9520 |
| 0.3 | 0.58275910 | 64 | 0.5691517814 | -1.3607e-02 | -0.1089 | -0.8709 |
| | | 256 | 0.5793944107 | -3.3647e-03 | -0.0538 | -0.8614 |
| | | 1024 | 0.5819201725 | -8.3892e-04 | -0.0268 | -0.8591 |
| 0.6 | 1.07654130 | 64 | 1.0646337639 | -1.1908e-02 | -0.0953 | -0.7621 |
| | | 256 | 1.0735877386 | -2.9536e-03 | -0.0473 | -0.7561 |
| | | 1024 | 1.0758043373 | -7.3696e-04 | -0.0236 | -0.7546 |
| 1.0 | 1.52945031 | 64 | 1.5187608017 | -1.0690e-02 | -0.0855 | -0.6841 |
| | | 256 | 1.5267957419 | -2.6546e-03 | -0.0425 | -0.6796 |
| | | 1024 | 1.5287877625 | -6.6255e-04 | -0.0212 | -0.6784 |
| pi/2 | 1.76274717 | 64 | 1.7525609198 | -1.0186e-02 | -0.0815 | -0.6519 |
| | | 256 | 1.7602167091 | -2.5305e-03 | -0.0405 | -0.6478 |
| | | 1024 | 1.7621155494 | -6.3162e-04 | -0.0202 | -0.6468 |
| 2.2 | 1.47857818 | 64 | 1.4677680197 | -1.0810e-02 | -0.0865 | -0.6919 |
| | | 256 | 1.4758939085 | -2.6843e-03 | -0.0429 | -0.6872 |
| | | 1024 | 1.4779082395 | -6.6995e-04 | -0.0214 | -0.6860 |
| 3.0 | 0.28131152 | 64 | 0.2664342552 | -1.4877e-02 | -0.1190 | -0.9521 |
| | | 256 | 0.2776578936 | -3.6536e-03 | -0.0585 | -0.9353 |
| | | 1024 | 0.2804019341 | -9.0958e-04 | -0.0291 | -0.9314 |

**Result.** eps_eff - eps is negative everywhere, and its magnitude is of order 1/beta.
- (eps_eff - eps)*beta is roughly constant in beta at fixed a, and it drifts by about 2-3% between beta = 256 and 1024.
- (eps_eff - eps)*sqrt(beta) is not constant: it halves each time beta quadruples.
- The ratios d(256)/d(1024) are 4.01 to 4.02. A pure 1/beta law would give 4. The ratios d(64)/d(1024) are 16.1 to 16.5, against 16 for a pure 1/beta law.
- The 1/beta constant depends on a. It is about -0.65 at a = pi/2 and about -0.95 at a = 0.1 and a = 3.0, and the profile is symmetric under a -> pi - a to roughly 3% (a = 0.1 against 3.0).
- The limit a -> 0 was not tested separately. At a = 0.1 the constant is about -0.95.

## Predicates
Fixed in the docstring of eps_eff.py before the first run.

| Predicate | Outcome |
|---|---|
| H1 V identity | met |
| H2 t uniform | met (MC, measured) |
| H3 Gram | met |
| H4 l_j | met |
| H5 M symmetric, eigenvalues > 0 | **failed in 6 of 21 cases** |
| C1 truncation, 1e-9 | met in 21/21 (change exactly 0: l_j tail underflows) |
| C2 quadrature, 1e-9 | met in 21/21 (max 7.8e-11) |
| C3 d > 0 | **failed, 0 of 21 qualify** |
| scaling of d | measured only |

Tolerances: 1e-12 is about 1000 times double precision, for exact identities. 1e-9 is far below the size of d (at least 6e-4). The Monte Carlo check uses 4 sigma.

## Failed predicates (kept)
- **Run 1** (results_eps_eff_run1_crashed.txt): crashed with OverflowError in my own direct Bessel series. This was a defect in my code, not in the target. H1-H3 had passed. The file was kept and run 2 wrote to a new file.
- **H5**: the predicate "min eigenvalue > 0" was too strict. The smallest eigenvalues of M are roundoff noise of order -1e-17, because the true eigenvalues underflow. This was my expectation, not a defect of the target. The top eigenvalue is unaffected, and symmetry (below 4e-16) held in all cases.
- **C3**: my expectation that eps_eff > eps was wrong. The data show eps_eff < eps in all 21 cases.

## Grandchild T133
- Question: independent recomputation of eps_eff at beta = 64 for a = pi/2 and a = 0.1.
- Method: composite Simpson with 40001 points instead of Gauss-Legendre, J = 60, 120, 200.
- Control: arccosh(2) = 1.316958, correct.
- Outcome: 1.75256092 at a = pi/2 and 0.18402420 at a = 0.1. These agree with my values 1.7525609198 and 0.1840241980 to 8 digits, and are stable in J.
- I reread its files and reran run.py as a copy in rerun_gc/ (check K3, exit 0, identical output).
- T133 was admitted and released with pcpos.

## PCP OS
- Register: pcp/. Checks: K1 (failed run 1), K2 (run 2), K3 (grandchild rerun).
- `pcp_os.py verify --ws pcp`, last line: "A pass is a fact about these bytes... result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)".
- `pcpos verify pcp/register.jsonl`, last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

## Rerun
```
cd /home/user/z4-workers/m1-agmon/child
mv results_eps_eff_run2.txt results_eps_eff_run2.old.txt   # the script opens its output with mode 'x'
python3 eps_eff.py          # about 106 s on 1 core
cp grandchild/run.py rerun_gc2/ ; cd rerun_gc2 ; python3 run.py
```
