# T153 report
Control answer (control.txt): **1.648721** (= exp(1/2)).

## Results (kappa = 0.25, Decimal 50 digits for sector eigenpairs)
| beta | N | Nx | L | M | R | Delta (identity) | Delta (E(h)) | Delta (eig. subtraction, float64 diff of Decimal-refined eigs) | M/L | R/M | log(R/L)/log(beta) | rho_CB |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 16 | 13 | 104 | 4.000031 | 25.3828 | 968.74 | 6.003928381e-07 | 6.003928381e-07 | 6.003928381e-07 | 6.346 | 38.17 | 1.980 | 6.206e+07 |
| 36 | 19 | 152 | 4.000000 | 38.9012 | 1531.37 | 1.198046609e-10 | 1.198046609e-10 | 1.198046609e-10 | 9.725 | 39.37 | 1.660 | 3.364e+11 |
| 64 | 26 | 208 | 4.000000 | 53.0952 | 3269.14 | 2.047078373e-14 | 2.047078373e-14 | 2.047078373e-14 | 13.274 | 61.57 | 1.612 | 3.071e+15 |
| 100 | 32 | 256 | 4.000000 | 66.4126 | 4175.77 | 3.197035698e-18 | 3.197035698e-18 | 3.197035698e-18 | 16.603 | 62.88 | 1.509 | 2.041e+19 |
| 144 | 38 | 304 | 4.000000 | 79.7165 | 5090.46 | 4.712854182e-22 | 4.712854182e-22 | 4.712854182e-22 | 19.929 | 63.86 | 1.438 | 1.421e+23 |
| 196 | 44 | 352 | 4.000000 | 93.0159 | 6011.32 | 6.665738406e-26 | 6.665738406e-26 | 6.665738406e-26 | 23.254 | 64.63 | 1.386 | 1.025e+27 |
| 256 | 51 | 408 | 4.000000 | 108.4283 | 4762.75 | 9.141581715e-30 | 9.141581715e-30 | 9.141581715e-30 | 27.107 | 43.93 | 1.277 | 5.108e+30 |

L = (m_0-m_N)^2 = 4 to 5e-6 (m_0 = 1.000004 ; m_N = -m_0 exactly). Chain inequality L <= M <= R holds at all 7 betas, with large slack (R/M 38..64, 44 at beta=256). log(R/L)/log(beta) falls 1.98 -> 1.28, i.e. R/L is not a clean power of beta in this range.
Delta(identity) and Delta(E(h)) agree to relative 1e-49 (exact discrete identity). Float64 eigenvalue subtraction (`eig_double_diff` in results json): agrees at beta=16, 36; off by 2.4% at 64 (1.998e-14 vs 2.047e-14); garbage at 100 (2.2e-16) and negative at 144 (-1e-15) -- as the task warned. The Delta_dir column in the table is from the 50-digit eigenvalues, so it is fine.

## What I did about h near pi/2
g(pi/2) = 1.2e-3 (16), 2e-5 (36), 3e-7 (64), 4e-9 (100), 5e-11 (144). Double eigenvectors would carry abs error ~1e-16, i.e. relative error ~1e-5 at beta=144 and worse with cancellation in T_-. Instead: float64 eigh only for a start vector, then 4 steps of inverse iteration in 50-digit Decimal (own LU); eigen-residual ~5e-50. h = f/g formed in Decimal. rho_CB used float Nystrom values of g (positive sums: relative accuracy ok).

## Predicates
Met (counts per case): 
- P1 T symmetry/sigma-commutation: NOT separately run as a program; it is by construction of the Toeplitz construction (measured only: eig residual checks). Counted as **measured only**.
- P2 g>0, int_A fg>0, norm: 7/7 met (norm_full = 1 to 1e-49).
- P3 Delta_id == Delta_E rel < 1e-25: 7/7 met (max 4.4e-49).
- P4 L<=M: 7/7. P5 M<=R: 7/7 (at kappa=0.125, beta 16,36: also met).
- P6 Delta>0, decreasing: 7/7.
Failed:
- P7 (statement says h odd): **fails — defect of the target statement**: h is even under x->-x (h(0)=+1, h(pi)=-1; even defect 1e-48, odd defect 2.0); it is sigma-odd. Chain argument unaffected (m_N=-m_0 holds).
- P8 Delta/lam_e < 1e-16 for beta>=36: 4/6 cases met over beta in {36,64,100,144,196,256} (36: 1.75e-10 and 64: 2.8e-14 not met; 100: 4.2e-18 and larger met). My expectation "beta>=36" from the task text was too early: it is true only from beta~100.
- P10 (my own expectation) Delta converges in kappa to <1e-3: **fails**: Delta(kappa=0.125)/Delta(0.25)-1 = 1.5e-2 at beta=16 and 1.4e-2 at 36. Cause: midpoint/uniform-grid quadrature error of an exponentially small tunnelling splitting; M and R shift by ~1%, ordering unaffected (M 25.19 vs 25.38, R 967 vs 969).
Own failed runs, kept: pcp K2 (Decimal+float TypeError, own bug), dbg2 file (g sign not fixed -> rho nonsense, own bug; fixed).
Measured only: rho_CB grid-max (coarse = refined half-grid, equal) is enormous (6e7 .. 1.4e23), so R is dominated by rho_CB; it is the max over grid pairs, a lower bound of the continuum max, not rigorous; M/L grows ~ linearly in sqrt(beta)(6.3 -> 27).

## Grandchild T155
Admitted by `pcpos task-admit ... --label q1-paths-grandchild --parent T153` -> T155; released after return. Control (beta=9, rho=2): 7.389056 (=exp 2, correct). Returned: Delta_direct = 6.003928380016177e-07, Delta_identity = 6.003928380884987e-07 at beta=16, rel diff 1.4e-10 (float64 rounding), beta=16 resolvable. My value (Decimal) 6.00392838088503e-07 agrees with identity to 1e-14 rel. Rerun by me (copy in scratchpad): identical numbers, control 7.389056.

## Rerun
cd /home/user/z4-workers/q1-paths/child; (new dir or remove results_* , control.txt first; files open mode x)
python3 control.py; python3 chain.py k025_all 0.25 16 36 64 100 144; python3 chain.py k0125 0.125 16 36; python3 chain.py k025_big 0.25 196 256
Grandchild: cd grandchild && rm -f control.txt result.md && python3 run.py
PCP: Python verify last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"; Rust verify last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
