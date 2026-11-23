# Report: lam(U,b)=min eig(I+Hess V), SU(2)^4 plaquette
Control (control.txt): -1.000000 (Tr exp(tX)=2cos(t/sqrt2)); FD gives -0.99999996.

## Verdict table (met = predicate passed, failed, measured only)
| item | verdict | evidence |
|---|---|---|
| P0 control = -1 | met | FD h=1e-3: -0.99999996 |
| P1 analytic Hess = FD Hess | met | max abs diff 1.4e-7 (20 Haar configs, b=1.7), 1.7e-7 at Q=-1; tol 1e-5 (FD h=1e-3 truncation ~1e-7) |
| Q1 / P2: lam(Q=-1)=1-2b | met | b=0.5: 1.5e-16, b=1: -1, b=2: -3, b=4: -7 (err <1.1e-14, tol 1e-8 = float64 roundoff). Hess V = -(b/2)|s1+s2-s3-s4|^2 per colour: eigenvalues -2b (x3), 0 (x9) |
| Q2 / P3: global min = Q1 value | measured only | 5000 Haar samples per b + 13 hill-climb starts per b: min found 0 / -1 / -3 / -7, never below 1-2b (|diff| <= 1.1e-14, i.e. equal at float roundoff). Not a proof; found min is an upper bound on the true min |
| Q3 / P4: horizontal min | measured only | gauge span rank 9 (singular values 2 x3, 1.414 x6, 0 x3; tol 1e-9), horizontal dim 3; horizontal eigs of I+Hess V = 1-2b (x3): ~1e-16, -1, -3, -7. Gauge-block min = 1.0 for all b. Soft modes are horizontal, so horizontal min = lam |
| sub-agent FD-only check (b=1) | met | -0.99999973 (h=1e-3); I+H eigs -1 x3, +1 x9; agrees with -1 within 2.7e-7 |

## Failed predicates
- Run K1 (first hess.py run): exit 1, ModuleNotFoundError scipy. Environment defect, not a predicate failure; script fixed (own expm, own hill-climb), rerun as K2 (exit 0). K1 stays in the register.
- No numerical predicate failed. My hand derivation (P2) held. P4 expectation was left open and measured.
- Random search alone (5000 samples) did not reach the Q1 value (0.0011 vs 0 for b=0.5; -0.99617 vs -1; -2.9978 vs -3; -6.98200 vs -7); only local optimisation did. This is a sample-size effect, not a failed predicate.

## Not checked
- Analytic proof of the global minimum (searched only; 12 dims, crude hill-climb, one seed set: 12345 and 777+10b).
- Other b values. Other plaquette orientation conventions; I used link corners U1(0,1), U2(1,2), U3(3,2), U4(0,3).
- Symmetrisation of the mixed second derivative is by construction (polarised quadratic form), verified only through FD agreement.

## Delegated question
Sub-agent (grandchild/): FD-only lam at Q=-1, b=1; control first (-1.000000, correct). Result -0.99999973 (h=1e-3), distinct eigenvalues -1 x3, +1 x9. I reread its hess.py (central differences, no analytic formula, 'x' file modes) and reran it in clean copies grandchild_rerun/ and grandchild_rerun2/ (K3, PCP-checked): results.txt byte-identical to its own. scipy was unavailable to it; it used its own expm via eigh.

## Rerun
cd /home/user/z4-workers/a3-Acurv/child; export OMP_NUM_THREADS=1
# results_hess.json is opened mode 'x': run in a fresh directory
mkdir r1 && cp hess.py r1/ && (cd r1 && python3 hess.py)      # ~21 s
mkdir r2 && cp grandchild/hess.py r2/ && (cd r2 && python3 hess.py)   # sub-agent FD check
