# T233 report
**Control:** -ln(tanh(1/2)) = 0.771937 (control.txt).

## Numbers (value ± delete-one-stream jackknife, n=32)
| | N-d2 | N-d0 |
|---|---|---|
| J1 | 0.0080467 ± 0.0000340 | 0.0077296 ± 0.0000394 |
| Var1 | 0.128358 ± 0.000766 | 0.123748 ± 0.000808 |
| r1 | 0.062689 ± 0.000472 | 0.062463 ± 0.000494 |
| J4 | 0.0028914 ± 0.0000120 | 0.0029112 ± 0.0000117 |
| Var4 | 0.059114 ± 0.000411 | 0.061513 ± 0.000549 |
| r4 | 0.048912 ± 0.000380 | 0.047327 ± 0.000456 |
| z(r1) | 0.104 | -0.425 |
| z(r4) | -0.532 | -0.280 |
| d(r1) | 1.712 | 1.607 |
| d(r4) | 0.773 | **2.110** |
| meta hot==parity | 32/32 | 32/32 |

Q1 = r1(N-d2)/r1(N-d0) = 1.0036 ± 0.0110; Q4 = 1.0335 ± 0.0128 (independent-directory error).
Per-stratum/half values: results_run3.json.

## Predicates
- |z|<=2: met in all 4 marks (4/4).
- meta flag == ID parity: met, 64/64 (hypothesis tested per stream; all qualify).
- |d|<=2: met 3/4; **failed N-d0 r4 (d=2.110)**. Failure of my own expectation (2-sigma is a convention from the task; ~1 in 20 expected per mark, 4 marks), not a target defect; not a bug in code. Reported as measured, no further claim.
- Tolerance source: the 2 is from the task statement; no numeric tolerance otherwise.
- Process failures kept: run1 (pcp check K1, exit 1) and run2 died with a TypeError (numpy bool not JSON serialisable) — my own bug; partial results.json and results_run2.json kept, fixed, run3 -> results_run3.json (K2 exit 0).
- Note: jackknife for strata not needed; z uses the pooled-r error as specified.

## Grandchild
Task id **T237** (admitted under T233, released). Question: independent no-numpy recomputation of Var1 of N-d0 pooled, with control var(1,2,3,4)=1.25 (passed). Returned: rows 36864, Var1 = 0.123747700718, mean j_single = 0.00772964793526. I reread and recomputed myself (plain csv+fsum): 0.12374770071831 and 0.0077296479353 — agree with my numpy 0.12374770071831025. Rerunning its var1.py is refused by design (out.txt mode x already exists); I used an inline recompute instead.

## Rerun
```
cd child
python3 reduce.py   # needs a fresh output name: edit results_run3.json -> new name (mode x)
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name reduce_fixed --expect-exit 0 -- python3 reduce.py
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
## Verify last lines
- python verify: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- rust verify: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
