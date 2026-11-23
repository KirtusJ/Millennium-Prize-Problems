# T73 report

Control: I_1(1)/I_0(1) = 0.446390 (control.txt, power series).

| item | value | verdict | evidence |
|---|---|---|---|
| Q1 -ln(I_1/I_0), β=4 | 0.1467351964 | STANDS | 50-digit series vs midpoint-trapezoid integral, rel diff 4e-16 |
| Q1 n=2, β=4 | 0.5652137118 | STANDS | rel diff 4e-16 |
| Q1 n=1, β=16 | 0.03228793485 | STANDS | rel diff 6e-15 |
| Q1 n=2, β=16 | 0.1290027702 | STANDS | rel diff 6e-16 |
| Q2 A | -0.0833333333 (numerically -1/12, \|A+1/12\|=3e-16) | STANDS | deterministic rule N=24..40 identical to 1e-12; full 6-D rule (16,14,28) agrees 3e-15; MC 2e6: -0.08438±0.00056 (z=-1.9); sub-agent (Euler angles) -0.083333333333 |
| Q2 B | 0.198249519694 (err est ~2e-15 from N=32→40 change) | STANDS | full 6-D unreduced rule 0.198249519852 (diff 1.6e-10); MC 0.198201±0.00018 (z=-0.27); sub-agent 0.198249519694 |
| "A = -1/12 exactly" | not proven | NOT CHECKED | only numerical coincidence to 3e-16, no derivation |

Error-estimate caveat: the 2e-15 is a convergence difference between resolutions, not a rigorous bound. The reduced rule uses conjugation invariance, which I argued rather than tested separately. The unreduced rule (q2b) does test it, to 1.6e-10 (B, limited by that rule's resolution).

## Failed predicates
- q2.py Q4: full(10,8,16) vs reduced N=40, tolerance 1e-8. A agreed (8e-17) but B differed by 1.6e-5. Cause: **my expectation**. The tolerance was too tight for a coarse 6-D rule (reduced N=10 already differs from N=40 by 2.8e-6 on B). It is not a defect of the target. Retested in q2b.py with a finer rule (16,14,28): PASS at 1.6e-10. Both results are kept.
- No other predicate failed. Q5 (MC within 4σ) passed. Q6 ("for all") had no universal claim, so there was no case count to report.

Tolerances: 1e-13/1e-12 for float64 sums (eps × ~1e4 terms); 1e-11 for Q1 (eps amplified by ln); MC at 4σ from the sample standard error; the others are as stated in each docstring.

## Not checked
- No analytic derivation of A or B (no Peter–Weyl or character expansion).
- No independent library, since scipy is absent.
- The MC result (z_A=-1.9) is weak confirmation of A, which is its only role.
- Q1 uses float64 for the integral. The 10 significant digits come from the Decimal series.

## Sub-agent
Question: independently recompute A and B with Euler-angle parametrization (a different measure and rule), with a known-answer control first. Task id **T75**, admitted before and released after (`task-release` event 150), directory grandchild/.
Outcome: control 0.446390 and ∫χ1²=1 passed. A=-0.083333333333 and B=0.198249519694 (n=40 and n=64 identical, n=24 off by 1e-7). I reread result.txt and reran run.py in a scratch directory, and the output was byte-identical. Note that the sub-agent reduced via the Weyl class density for U1, so it is not fully unreduced. Its agreement with mine is partly shared structure (both use conjugation invariance).

## Verify (last lines)
- `pcp_os.py verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

## Rerun
Files must be new (mode "x"); run in a fresh copy or delete the result files first.
```
export OMP_NUM_THREADS=1
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name q1  --expect-exit 0 -- python3 q1.py
$P check --ws pcp --name q2  --expect-exit 0 -- python3 q2.py
$P check --ws pcp --name q2b --expect-exit 0 -- python3 q2b.py
(cd grandchild && python3 run.py)
$P verify --ws pcp; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
