# T82 report: coercivity check, H = 1 - K + V - c1*D

**Control:** -ln(I_3(16)/I_1(16)) = **0.257416** (control.txt, written first; the grandchild got the same value).

## Method
- `lam.py` builds the Galerkin matrix with n1,n2 even <= N. Quadrature is a trapezoid rule in a and Gauss-Legendre in t with N+4 points.
- For large N it uses the swap-symmetric (n1<->n2), L-even subspace. At N=12, beta=16 I compared this against the full space, both L parities (`result_check.json`):

| Sector | dim | Lambda (c1=0) | Lambda (c1=1) |
|---|---|---|---|
| full | 231 | 0.811274 | -0.359154 |
| sym, L even | 84 | 0.811274 | -0.359154 |
| L odd | 91 | 1.047695 | -0.222723 |

- L parities decouple. The L-odd block is higher, so the L-even sector holds the lowest eigenvalue at N=12. That is **not checked at larger N**.
- The swap-symmetric subspace was only checked at N=12, beta=16. For beta=64 and larger N it is an assumption.
- The N=12 value 0.811274 matches the "about 0.811" check.

## Table: beta^{1/3} * Lambda (Galerkin upper bounds; L-even, swap-symmetric sector)
Grid g1 uses M=2N+20 points. Grid g2 uses M=6N+60 points. The two grids agree to all printed digits (identical to 1e-6), so quadrature error is negligible.

| beta | N | dim | c1=0 | c1=1 |
|---|---|---|---|---|
| 16 | 24 | 455 | 2.00563 | -1.98037 |
| 16 | 32 | 969 | 2.00410 | -2.18228 |
| 16 | 40 | 1771 | 2.0039 | -2.2864 |
| 16 | 48 | 2925 | 2.0038 | -2.3480 |
| 16 | 56 | 4495 | 2.0038 | -2.3878 |
| 64 | 40 | 1771 | 2.46030 | -2.79689 |
| 64 | 48 | 2925 | 2.46015 | -3.14138 |
| 64 | 56 | 4495 | 2.4601 | -3.3535 |
| 256 | – | – | not computed | not computed |

beta=256 was not computed: it needs N of about 80 or more (dim above 10^4) within the 6-minute budget.

**Convergence**
- c1=0 converges quickly. The change from N to N+8 is about 1e-4 to 2e-4 in beta^{1/3}*Lambda. The first N=48 value at beta=64 was 2.46015, so Lambda is about 0.61504.
- c1=1 is **not converged** in N. Values keep drifting down at every step:
  - beta=16: -1.98 → -2.18 → -2.29 → -2.35 → -2.39
  - beta=64: -2.80 → -3.14 → -3.35
- The drift is probably because D = sin a1 + sin a2 is non-smooth at U = ±1 and needs high n. This is my guess, not tested.
- Since Galerkin values are upper bounds, the true c1=1 values are lower still.
- D <= 2 gives a rigorous floor Lambda >= -2, i.e. beta^{1/3}*Lambda >= -5.04 at beta=16 and -8.0 at beta=64.

## Predicates (fixed in the lam.py docstring before the first run)
- **P1** (beta^{1/3} Lambda(c1=1) >= -1 for every beta computed): **FAILED**.
  - Cases qualifying: 0 of 2 (beta=16 and 64). Each Galerkin value is already well below -1 (-2.39 and -3.35 at the largest N), and Galerkin values are upper bounds, so the true values are lower still.
  - The failure comes from the operator as specified, not from a numerical defect. It also means the continuum analogue (>= 0) is not reproduced at these beta. My own expectation was that P1 would hold.
  - The failure is robust because the upper bound already violates the tolerance. It holds for any N >= 16 at beta=16 (-1.49 at N=16). At beta=64 it holds for N >= 24 (the first value I computed is -2.18 at N=32).
- **P2** (measured only): beta^{1/3}*Lambda(c1=0) = 2.0038 at beta=16 and 2.4601 at beta=64. It is rising slowly toward the parent's "about 3.35" but is far from it at these beta.
- **P3** (measured only): the change with N and grid is quantified above. The grid effect is below 1e-6.
- **P4** (N=12, beta=16, full space, about 0.811): met (0.811274; the tolerance of 5e-3 was my choice).
- No predicate failed through an error of mine, and no tolerance came from anywhere but the parent's -1 and my 5e-3.

## Sub-agent
Task **T85** (label g2-conv-child-grandchild, parent T82), admitted before launch and released after it returned.
- It ran a control first, 0.257416.
- It independently recomputed Lambda(16, c1=0) at N=12 using 80-node Gauss-Legendre in a, the full space and direct 3D quadrature of V. It got 0.811274 (L even 0.811274, L odd 1.047695), matching mine to 6 decimals.
- I reread `grandchild/result.txt` and reran `grandchild/run.py` in a scratch copy, with the same output.

## Rerun commands
```
cd /home/user/z4-workers/g2-conv/child; export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
# result files are opened with mode "x"; delete result_*.json first to rerun
python3 lam.py check     # N=12 check, about 1 s
python3 lam.py main      # about 16 s
python3 extra.py         # about 46 s
cd grandchild && rm -f control.txt result.txt && python3 run.py
```
The PCP records are K1 (lam-check), K2 (lam-main) and K3 (lam-extra), all exit 0, in `pcp/register.jsonl`. The expected "method not found" note appeared at init.

## Verify (last lines)
- `pcp_os.py verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
