# T152 report: Q1 Harnack lower bound, 1-D grid model

**Control:** c* = 4.6054 (numpy Gauss-Legendre, n=200 vs 400 agree to 1e-8). The grandchild got 4.605413 independently.

## Results
| beta | N | a | x used | L(a) | J(a) | sqrt(b)(L-J) | Q1 met? | Q2 met? | 1-lambda | (1-lambda)b^(1/3) |
|---|---|---|---|---|---|---|---|---|---|---|
| 256 | 204 | 0.05 | 0.0616 | 0.01187 | 0.01490 | -0.0485 | yes | yes | 0.180654 | 1.1471 |
| 256 | 204 | 0.1 | 0.0924 | 0.02344 | 0.04213 | -0.2991 | yes | yes | 0.180654 | 1.1471 |
| 256 | 204 | 0.2 | 0.1848 | 0.07626 | 0.11892 | -0.6825 | yes | yes | 0.180654 | 1.1471 |
| 256 | 204 | 0.4 | 0.4004 | 0.27393 | 0.33361 | -0.9548 | yes | yes | 0.180654 | 1.1471 |
| 1024 | 404 | 0.05 | 0.0467 | 0.00769 | 0.01490 | -0.2308 | yes | yes | 0.118717 | 1.1966 |
| 1024 | 404 | 0.1 | 0.0933 | 0.02584 | 0.04213 | -0.5213 | yes | yes | 0.118717 | 1.1966 |
| 1024 | 404 | 0.2 | 0.2022 | 0.09588 | 0.11892 | -0.7371 | yes | yes | 0.118717 | 1.1966 |
| 1024 | 404 | 0.4 | 0.4044 | 0.29469 | 0.33361 | -1.2453 | yes | yes | 0.118717 | 1.1966 |
| 4096 | 804 | 0.05 | 0.0469 | 0.00862 | 0.01490 | -0.4021 | yes | yes | 0.076778 | 1.2285 |
| 4096 | 804 | 0.1 | 0.1016 | 0.03283 | 0.04213 | -0.5957 | yes | yes | 0.076778 | 1.2285 |
| 4096 | 804 | 0.2 | 0.2032 | 0.10329 | 0.11892 | -1.0006 | yes | yes | 0.076778 | 1.2285 |
| 4096 | 804 | 0.4 | 0.3986 | 0.30095 | 0.33361 | -2.0902 | yes | yes | 0.076778 | 1.2285 |

L is measured at the grid point nearest a, so L(a) is not exactly L at a, while J is taken at the exact a.

## Counts (12 cases each)
- Q1 (sqrt(b)L <= sqrt(b)J + log b): met 12, failed 0.
- Q2 (L <= 10a): met 12, failed 0.
- Measured only: 1-lambda, (1-lambda)b^(1/3), sqrt(b)(L-J) (36 values).
- Hypothesis per case (rule 4): all 12 of 12 cases qualify for each of Q1 and Q2.
- sqrt(b)(L-J) is negative in every case (-0.05 to -2.09). Q1 holds with a slack of at least log(b) = 5.5.
- sqrt(b)(L-J) gets more negative as beta grows at fixed a. At a = 0.4 it goes -0.95, -1.25, -2.09.
- The sampled cases do not show L approaching J from above.
- Q2 has large slack: L/a is at most about 0.7.
- (1-lambda)b^(1/3) goes 1.147, 1.197, 1.229. It is measured only, and I make no claim about its limit.

## Failed predicates (kept in the register)
- Check K2 (main.py): asserted strict g > 0 everywhere. It failed with min g = -6.1e-16. This was my own expectation. Double precision cannot hold positivity in the tail between the wells. It is not a defect of the target.
- The revised predicate asserts g > 0 strictly for |x| <= 0.5 and g.min() > -1e-12 globally. K3 passed with it.
- Tolerances: 1e-12 for symmetry and for the roundoff floor (double precision, about 1e3 times machine epsilon). 1e-10 for the eigen residual and the J quadrature (convergence between n = 200 and n = 400). 1e-9 for degeneracy grouping (the observed gap is about 1e-15).

## Note on the model (degeneracy)
eps vanishes at both x=0 and x=pi, so the top eigenvalue is exactly 2-fold degenerate up to roundoff (degen=2 in every case). "The top eigenvector (positive)" is the Perron vector. I took it as the projection of the all-ones vector onto the top eigenspace, which is the symmetric combination and is positive. g(a)/g(0) lies within the 0-well, so it does not depend on this choice up to tunnelling (which is zero to roundoff).

## Grandchild T154 (q1-harnack-grandchild)
- Question: independently recompute sqrt(b)L(0.1) at b=256 with a dense eigensolver and its own code. Also the boundary case L(0) = 0. It had a known-answer control first (c* = 4.6054).
- Returned:
  - control 4.605413 (matches the expected 4.6054).
  - N = 204, index 105 (x = 0.0924).
  - sqrt(b)L = 0.375048.
  - L(0) = -0.0, which equals 0.
  - lambda = 0.8193455397.
  - It also flagged the degeneracy (top two eigenvalues equal to 7.8e-16).
- My rerun of its script reproduced the same numbers. My main program gives 16*L = 0.375048 at the same grid point. They agree. 1-lambda = 0.180654 in main.py matches 1 - 0.8193455.
- Its eigenvector had a roundoff-level negative value (-2e-16), which it handled by dropping its positivity assertion. I did not recheck its choice of eigenvector inside the degenerate pair. My code uses the symmetric combination, and the numbers agree.
- T154 was released with task-release.

## Rerun (from this directory; results files open with mode x, so remove them first)
```
rm -f control.txt results.json
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 control.py
python3 main.py
cd grandchild && rm -f control.txt result.txt && python3 run.py
```
PCP register: pcp/register.jsonl (checks K1 control, K2 main failed, K3 main-rev).

## Verify lines (last line of each)
- Python `verify --ws pcp`: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- Rust `pcpos verify pcp/register.jsonl`: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
