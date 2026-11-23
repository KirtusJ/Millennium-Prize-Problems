# T162 — numerical check of "limsup (-log m)/sqrt(beta) <= c*"

**Control:** c* = ∫₀^π sqrt(2·eps(a)) da = **4.6054** (control.txt; Gauss–Legendre with a=t² substitution, 400 vs 800 nodes agree to 3e-14; eps=2·asinh|sin a|, so the integrand is sqrt(4·asinh|sin a|)).

## Method
`hp.py`: fold by σ into even/odd blocks on [0,π) (cyclic, N points, h=π/N), conjugate by W=exp(-√β·Φ), refine the top eigenpair of each block by Newton in 300-digit `Decimal` (residual in Decimal, correction from a double-precision Jacobian inverse). Kernel truncated at exp(-600). So λ_e, λ_o are obtained to ~250 digits and m=log(λ_e/λ_o) is read directly (diff ~1e-124 at β=4096). I did not need the g,f identity. The discrete model uses the double-precision value of eps_j (exact Decimal of it); this is a ~1e-14 relative perturbation of the model.
Method check β=16: HP −log m = 13.838350475234 (N=51) vs plain double eigenvalue difference 13.83835047577 (N=51): agree to 5e-10 → **P0 met** (tol 1e-6).

## Table (-log m; every row has h·√β ≤ 1/4; 4096 only at the coarsest grid)
| beta | N | h | -log m | (-log m)/√β | diff to next finer N |
|---|---|---|---|---|---|
| 64 | 102 | 0.03080 | 31.205527 | 3.900691 | -1.410e-2 |
| 64 | 204 | 0.01540 | 31.191426 | 3.898928 | -3.516e-3 |
| 64 | 408 | 0.00770 | 31.187910 | 3.898489 | — |
| 64 | Richardson (h²) | | 31.186738 | 3.898342 | |
| 256 | 202 | 0.01555 | 66.664544 | 4.166534 | -1.159e-2 |
| 256 | 404 | 0.00778 | 66.652958 | 4.165810 | -2.891e-3 |
| 256 | 808 | 0.00389 | 66.650068 | 4.165629 | — |
| 256 | Richardson | | 66.649104 | 4.165569 | |
| 1024 | 404 | 0.00778 | 138.522929 | 4.328842 | -9.342e-3 |
| 1024 | 808 | 0.00389 | 138.513587 | 4.328550 | -2.332e-3 |
| 1024 | 1616 | 0.00194 | 138.511255 | 4.328477 | — |
| 1024 | Richardson | | 138.510478 | 4.328452 | |
| 4096 | 806 | 0.00390 | 283.493857 | 4.429592 | not run (N=1612 killed at the 5-min limit) |

Grid differences shrink by 4.0 per halving: error is O(h²) (kink of eps at 0, π — a property of the target's eps, not a bug). Richardson rows assume exactly this order (observed ratios 4.01, 4.01, 4.00). A stray test run res_64_101.txt (N=101, 31.205902) is also in the directory; it is not in the series. For β=4096 the discretisation error at this h√β≈1/4 was 0.019/0.015/0.0125 for β=64/256/1024, so I expect ≈0.01 (estimate, not measured) → 4096 value ≈ 283.483.
Convergence of refinement (P2): last Newton step / diff ≤ 4e-138 in all runs (met).

## Predicates
- P0 met (above). 
- P1 (grid |Δ|<1e-3 between N and 2N): **failed** at every β at the fixed h√β≤1/4 (smallest finest-pair Δ: 2.3e-3 at β=1024, 3.5e-3 at β=64/ 2.9e-3 at 256). Cause: my own tolerance was too tight for an O(h²) scheme with a kink; not a target defect. The grandchild's analogous predicate (1e-6 at β=16) failed for the same reason (see below).
- Q1 (−log m ≤ c*√β+3 log β): **met** at 64 (31.19 ≤ 49.32), 256 (66.65 ≤ 90.32), 1024 (138.51 ≤ 168.17), and 4096 (283.49 ≤ 319.7); margins 18, 24, 30, 36.
- Q2 (ratio increasing and < c*): **met (measured)**: 3.8983, 4.1656, 4.3285, 4.4296(coarse grid) — increasing, all < 4.6054. The gap to c* is 0.71, 0.44, 0.28, 0.18.
- Q3 (fit a√β+b logβ+c, |a−c*|≤0.2): with 3 Richardson points the fit is exact (3 params): a=4.5499, b=−0.676, c=−2.402, |a−c*|=0.056 **met but not informative** (no residual). With 4 points incl. 4096 (raw / minus guessed 0.0105): a=4.5640 / 4.5635, b=−0.79, c=−2.02 / −2.03, |a−c*|≈0.04. The 4096 point is single-grid, so this is measured-with-caveat. A 2-parameter fit a√β+c over the 3 points gives a=4.47 (poor, since log term matters). The data are consistent with a→c* from below with a negative log correction; nothing here refutes the claim, but limsup cannot be established by 4 values.

## Sub-agent
Question: independent plain-double, unfolded (full 2N circle, eigh, parity-classified) recomputation of −log m at β=16, N=200/400, with known-answer control ∫₀^π sin = 2. Task id **T163** (admitted, released after return). Outcome: control 2 (trapezoid 1.99999959, GL 1.99999999999999); −log m = 13.816575 (N=200), 13.815443 (N=400); its own predicate (agree to 1e-6) FAILED with Δ=1.13e-3 = my own expectation error (O(h²) kink), not a target defect. I reread and reran (`python3 run.py out2`): identical numbers. It agrees with my folded double result (13.816517 at N=204, 13.815428 at N=408) and the HP value.

## Rerun (in a fresh copy of the directory; result files open with "x")
```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P init pcp --principal principal --principal-name "Kirtus Justus"
python3 hp.py 16 51 --double ; python3 hp.py 16 51
./runall.sh        # hp.py for the 11 (beta,N) pairs, via pcp check; the last (4096 1612) exceeds 5 min
python3 table.py
cd grandchild && python3 run.py out2
```

## PCP OS
Python `verify --ws pcp`, last line: `A pass is a fact about these bytes...` preceded by `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`.
Rust `pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.` (preceded by `result: PASS ...`). The killed 4096/1612 run has no check record.
T163 released via task-release.
