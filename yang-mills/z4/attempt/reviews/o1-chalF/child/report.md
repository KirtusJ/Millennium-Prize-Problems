# T142 report — Barta ratio B(rho)

**Control (I_0(1))**: `control.txt` = 1.266066 (scipy is NOT installed; I wrote my own ive via the periodic midpoint rule on the integral representation, exp(-x)I_n(x)=(1/pi)∫exp(x(cos t-1))cos(nt)dt).

## Table (sup over the 9-point rho grid; full values in res1.csv, summary.csv)
| beta | s | A | sup B | rho at sup | -log sup B | -log sup B - log A |
|---|---|---|---|---|---|---|
| 64 | 0.1 | 1.2210 | 0.837219 | 0.3 | 0.177670 | -0.021998 |
| 64 | 0.3 | 1.8064 | 0.562314 | 0.3 | 0.575695 | -0.015652 |
| 64 | 1 | 5.8284 | 0.173543 | 0.1 | 1.751331 | -0.011416 |
| 256 | 0.1 | 1.2210 | 0.821763 | 0.1 | 0.196303 | -0.003365 |
| 256 | 0.3 | 1.8064 | 0.556164 | 0.1 | 0.586693 | -0.004653 |
| 256 | 1 | 5.8284 | 0.172010 | 0.1 | 1.760200 | -0.002547 |
| 1024 | 0.1 | 1.2210 | 0.820336 | 0.1 | 0.198041 | -0.001627 |
| 1024 | 0.3 | 1.8064 | 0.553836 | 0 | 0.590887 | -0.000460 |
| 1024 | 1 | 5.8284 | 0.171666 | 0 | 1.762204 | -0.000544 |
| 4096 | 0.1 | 1.2210 | 0.819050 | 0 | 0.199610 | -0.000058 |
| 4096 | 0.3 | 1.8064 | 0.553645 | 0 | 0.591231 | -0.000115 |
| 4096 | 1 | 5.8284 | 0.171596 | 0 | 1.762611 | -0.000136 |

Grid-sup only; for small beta the true sup over rho may lie between grid points (sup at rho=0.1 or 0.3 for beta<=256).

## Method
rho'=sin(phi) (removes the sqrt endpoint singularity at rho'=1); composite Gauss-Legendre in phi, 256 panels x 24 nodes, breakpoints incl. peak phi*=asin(rho/A); exponent combined as beta(RR'+rho rho'-c rho'^2+(a/2-s^2)rho^2-1) with ive. Refinement: 512 panels x 32 nodes. res1.csv holds the fine values. Since B underflows for 5 cases (beta=4096, listed below), res_log.csv gives log B.

## Convergence check and predicates (programs: barta.py, barta2.py; predicates in docstrings)
- P1 Bessel I0(1), I1(1) vs tables within 1e-9: PASS. P2 Bessel node-doubling < 1e-13: PASS (2.6e-14). P3 B(0) at s=1e-9 equals 1 within 1e-8: PASS (0.99999999805, deviation 2e-9 = O(s) expected).
- **P4 FAILED (kept)**: relative change < 1e-9 for all 108 cases: 103/108 qualify. The 5 failures (beta=4096: s=0.3 rho=0.999,1; s=1 rho=0.99,0.999,1) have B < 1e-300 (underflow/denormal/0), so relative change is NaN or 9e-5 on denormals. Cause: my own predicate (relative change on underflowed numbers), not a defect of the target or quadrature. B values in res1.csv for those rows are 0/denormal and should be read as "< 1e-300".
- Fix in barta2.py (log form): Q1 log B changes < 1e-9 for 108/108; Q2 exp(logB) matches res1.csv within 1e-9 for all cases with B>1e-250: PASS; Q3 below: PASS. Max change in sup values is far below 1e-9.
- P5 (not asserted): B<=1 held in 108/108 cases. B(0) = 1 check at s->0 passed.
- Tolerance sources: 1e-9 chosen as in the task ("refinement changes B < 1e-9 relative"); 1e-8 for s=1e-9 allows O(s) deviation; Bessel 1e-9 vs 10-digit tables. barta.py itself exited 1 (P4) -> recorded as pcp check K1 (expected 0, got 1); its output files were already written, so my manual re-run hit FileExistsError (mode 'x' working as intended).
- Honesty note: barta2.py's Q printouts weren't in my captured output (pcp check hides stdout); I re-evaluated Q3 directly (below). Q1/Q2 are exit-0 attested only.

## Sub-agent (T143, admitted --parent T142, released after return)
Independent method: u by Gauss-Legendre, theta midpoint, using I_0, I_1 integral representations (no radial Bessel routine); control integral x^2 = 0.333333 (grandchild/control.txt). Returned B(0; beta=64, s=0.3) = 0.5576952560 (grids up to 800x3200 agree to 1e-14). I reread its files, reran its gc.py in a copy (/tmp/claude-0/rerun, rm of old outputs needed because of mode 'x'; PCP check K3, exit 0), same output. My value: 0.5576952560002162; relative difference 3.9e-13 -> agrees. Caveat: the grandchild was handed the reduction of B(0) to a 1-D formula by me, so it checks quadrature/Bessel implementation, not my transcription of the definition.

## Task ids
T142 (me), T143 (grandchild, admitted event 285, released event 286).

## PCP records
checks K1 barta (exit 1, expected 0 - recorded failure), K2 barta2 (0), K3 grandchild-rerun (0).
- `pcp_os.py verify --ws pcp` last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right." (result: PASS)
- `pcpos verify pcp/register.jsonl` last line: same sentence (exit 0).

## Rerun (in a fresh copy of the directory, outputs use mode 'x')
```
cd child; python3 barta.py; python3 barta2.py
cd grandchild; python3 gc.py
```
