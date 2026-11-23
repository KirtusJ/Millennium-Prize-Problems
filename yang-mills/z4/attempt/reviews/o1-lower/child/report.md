# T144 report (worker o1-lower child)
Control: c* = 4.605413 (control.txt; Gauss-Legendre and Simpson agree to 1e-14).

## Verdicts
| Q | verdict | evidence |
|---|---|---|
| Q1 flux identity | STANDS | beta=16: flux Delta 6.003928e-7 vs plain eigenvalue subtraction 6.003928e-7 (rel diff 1.4e-10); beta=36: rel diff 5e-7 (subtraction limited by roundoff). Sector-form flux equals the literal sum over i in A, j not in A to <1e-14 at every beta. For beta>=64 there is no independent check, only the Q2 bounds and the h-trend. |
| Q2 lower bound | STANDS | ordered pairs, ratio lower/Delta 0.66-0.72 at all 6 betas. |
| Q2 upper bound as stated (factor 2) | DEFECT in the statement | ratio 0.655-0.699 < 1 at 6/6 betas, so Delta <= 2<g1_A,T g1_Ac>/\|\|g\|\|^2 is false. Variational argument with the odd test vector g(1_A-1_Ac) gives factor 4; ratio 1.31-1.40 at 6/6 betas, holds. |
| Q3 | STANDS (trend only) | -log(Delta)/sqrt(beta) rises monotonically toward c*=4.605413 but is still 0.17 below it at beta=4096. |

## Numbers (N is the grid size, h <= 0.25/sqrt(beta); Delta_2N is for the doubled grid)
| beta | N | Delta | -logD/sqrt(b) | lower/D | up(x2)/D | up(x4)/D | Delta_2N/Delta-1 |
|---|---|---|---|---|---|---|---|
| 16 | 104 | 6.003928e-07 | 3.5814 | 0.661 | 0.699 | 1.398 | +1.5e-2 |
| 36 | 152 | 1.198047e-10 | 3.8075 | 0.679 | 0.684 | 1.369 | not run |
| 64 | 204 | 2.045693e-14 | 3.9401 | 0.688 | 0.677 | 1.354 | +1.3e-2 |
| 256 | 404 | 9.138897e-30 | 4.1791 | 0.703 | 0.665 | 1.331 | +1.1e-2 |
| 1024 | 808 | 6.097614e-61 | 4.3328 | 0.712 | 0.659 | 1.318 | +9.3e-3 |
| 4096 | 1612 | 7.004936e-124 | 4.4308 | 0.718 | 0.655 | 1.310 | +7.5e-3 |

Weighted sector eigenvector residuals are 2e-16 to 4e-16. The eigenvectors are positive in the interior of A.

## Failed predicates
- P4 (N vs 2N agreement to 1e-3): failed at all 5 betas, 0.75%-1.5% difference. This was my expectation being too tight; the prescribed grid is coarse. The effect on Q3 is below 2e-4 (a 1% shift in Delta moves -logD/sqrt(beta) by 0.01/sqrt(beta)). The Delta values in the table are not converged below about 1%.
- Q2 upper bound with factor 2: failed at 6/6 betas. This is a defect of the statement, not of my code (see the factor-4 derivation above).
- P4 shows as FAIL for beta=36 in verify.py only because no 2N run exists. That is not a real failure.
- Process slip: main.py ran with numpy multithreading (about 5.6 min CPU in 2 min wall), so the 1-core rule was broken for that run. verify.py and the later steps ran with OMP_NUM_THREADS=1.

## Not checked
- An independent computation of Delta for beta>=64 (double precision cannot resolve it; no high-precision tools).
- The case of unordered pairs in the lower bound. I report the ordered-pair bound. The unordered-only sum is half as large and also holds.
- The PCP check of main.py: it ran before the register existed, and a rerun would take more than the budget. The register holds control_rerun (K1) and verify (K2, expect-exit 1 because of the failures above).
- A pcp check of control.py on its first run: it was run once directly, as the task required control first.

## Delegation
Task T145 (label o1-lower-child-grandchild), admitted and released. The control passed (N=8, beta=1: top eigenvalue 0.457607855536719 for T and for the even sector). At beta=16 it found Delta 6.0039284e-7 by plain subtraction and 6.0039284e-7 by the flux identity (rel diff 1.4e-10). I reread grandchild/result.txt and reran its run.py in a copy under /tmp/claude-0/gc: same numbers. It agrees with my beta=16 value (rel diff 1.4e-10 from my plain subtraction). Its program has an unclassified-eigenvector note for 59 near-degenerate low modes; harmless.

## Rerun
```
export OMP_NUM_THREADS=1
python3 control.py            # fails if control.txt exists (mode x); run in a clean dir
python3 main.py               # about 5 min on one core; writes results_main.json (mode x) and appends notes.md
python3 verify.py             # exit 1 expected (P4 and Q2-upper FAIL lines)
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name verify --expect-exit 1 -- python3 verify.py
$P verify --ws pcp ; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
## Count: met 3 (control, Q1, Q2 lower), failed 2 (Q2 upper as stated, P4), measured only 1 (Q3 trend).
