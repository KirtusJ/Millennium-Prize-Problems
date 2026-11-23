# Report: chessboard bound for 2D SU(2) bad-plaquette probability

Control: control.txt = 1.590637, which is I_1(2). The numeric quadrature gave the same value.

## Verdict table
| Item | Verdict | Evidence |
|--|--|--|
| Claim (c), all 200 cases (beta x delta x L in {2,4,6,8,inf}) | STANDS (on this grid) | 200/200 satisfy P <= min Bound. 0 violations on the 20001-point eps grid and on a 2e6-point grid. Smallest log(minBound/P) is 6.7 (beta=1, delta=0.2, L=6). Full table: `table.md`, `results.jsonl`. |
| Claim is non-trivial | MEASURED | Only 30 of 200 cases have minBound < 1. They occur at (beta,delta) = (32,1.0), (64,0.5), (64,1.0), (128,0.2), (128,0.5), (128,1.0), each for 5 L. The other 170 are satisfied only because the bound exceeds 1. Smallest log ratio among the 30 is 17.9, so the bound is very loose where it is non-trivial. |
| Sanity: delta=-1 gives P=1 | STANDS (weak) | max abs(P-1) = 2.2e-16. This is close to an identity, because the numerator and denominator are the same sum. It checks the code path only. |
| Sanity: P_L -> P_inf | STANDS | S4: L=8 is closer to P_inf than L=2 in 40/40 (beta,delta) pairs. Example at beta=16, delta=0.2: P_L is 0.06847, 0.08566, 0.08875, 0.08924 for L=2,4,6,8, and P_inf = 0.0892708. |
| Truncation | STANDS | Characters j <= 400. Results with J=400 and J=200 are identical. The last kept denominator term r_J^N is <= 7.6e-71 (r_j = a_j/a_0, N >= 4). Terms behave like exp(-j(j+2)N/(2 beta)). The tail for j > J is bounded by the sum of r_j^N, which is smaller than the last kept term times a factor of order 1. |
| Quadrature | STANDS | 400 vs 800 Gauss-Legendre panels (30 nodes each) agree to 1.4e-14 relative. |
| Item 3: -log(P_inf)/beta vs delta | MEASURED | -log(P_inf)/beta is below delta and approaches it from below. Gap (beta=8,16,32,64,128) at delta=1.0: -0.106, -0.074, -0.047, -0.029, -0.017. At delta=0.2: -0.067, -0.049, -0.033, -0.022, -0.013. Table: `m1.md`. The gap shrinks roughly like log(beta)/beta, consistent with the prefactor P ~ beta^{-3/2} e^{-beta delta}. The prefactor is not fitted here. |
| Delegated MC for P_inf(16, 0.2) | STANDS | MC gives 0.089362 +/- 0.000094. My quadrature gives 0.0892708. The difference is 9.1e-5, about 1.0 SE. |
| Larger lattices, odd L, finite-size effects beyond L=8 | NOT CHECKED | |
| Rigorous proof of the chessboard bound | NOT CHECKED | Numerical evidence on a finite grid only. |

## Hypotheses
- "For all" in (c): hypothesis is L even or L = infinity, and the cases are tested per case. 200/200 qualify, since every L in the grid is even or infinite. 200/200 satisfy the bound.
- Tolerances: S1 1e-12 (roundoff scale 1e-16 times the number of terms). S2 1e-9 (double roundoff amplified by cancellation in oscillatory integrals). S3 1e-12 and 1e-30 (below any meaningful P; the smallest P is ~1e-56). Grid refinement for the eps minimum was checked with 2e6 points. The MC control tolerance is 3 SE.

## Failed predicates
None failed. Notes:
- S4 is my own expectation, not a theorem. It was not expected to hold uniformly in beta, and it did hold in 40/40 pairs. The check compares only L=2 against L=8.
- The S1 predicate is nearly an identity. It could not fail except through a code defect.

## Not checked
- Odd L.
- L > 8.
- eps grid minima beyond 2e6 points.
- A proof of the bound.
- The sub-leading prefactor fit in item 3.
- The result for a_0 at general beta against an independent Bessel implementation. Only the beta=2 control, I_1(2), was checked.

## Delegated question and outcome
Question: independent recomputation of P_inf at beta=16, delta=0.2 by Haar-SU(2) Monte Carlo (sampling points on S^3, plain self-normalised, seed 12345, 4e7 samples).
- Known-answer control, computed by me: E_Haar[exp(2 cos alpha)] = 1.590637. The sub-agent's estimate was 1.590466 +/- 0.000420 (0.4 SE), so the control passed.
- Main result: P = 0.08936 with SE 9.4e-5 (delta method) and 9.1e-5 (batch means). Mine is 0.0892708, a difference of about 1.0 SE.
- I reread `grandchild/result.txt`, `mc.py` and `notes.md`, and reran the program under `pcp check` with a new output name (`result_rerun.txt`). It reproduced the same numbers exactly.

## PCP OS
- `pcp_os.py verify`, last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify` (Rust), last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
- Register file SHA-256: b1f97d279e0ce2fb6859aa28cdc017316af3518dce2ddfaec908829fc182154b

## Rerun
```
cd /home/user/z4-workers/a3-B/child
# results.jsonl, table.md and m1.md open with mode "x", so move or delete them before a rerun
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name main --expect-exit 0 -- python3 pcp_main.py     # ~3 min
$P check --ws pcp --name grandchild_rerun --expect-exit 0 -- bash -c "cd grandchild && python3 mc.py result_rerun.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Counts: met 8, failed 0, measured only 2.
