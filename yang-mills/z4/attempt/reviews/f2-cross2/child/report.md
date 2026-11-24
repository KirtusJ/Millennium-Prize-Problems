# T242 report (cross2, 8 chains pooled; jackknife SE = sqrt(7/8 sum (R_(j)-mean)^2))
Control (step 0): control.txt = 1.500000 (hand check: C0=2, C2=-1).

## Numbers (value ± SE)
| quantity | value | SE |
|---|---|---|
| R(a_W), class L | 0.938965 | 0.000394 |
| R(a_P), class L | 0.974134 | 0.000129 |
| R(a_W), class Z | 0.683533 | 0.00440 |
| R(a_P), class Z | 0.955176 | 0.00202 |
| lambda2 | 0.0618653 | 0.000354 |
| 1 - lambda2 | 0.938135 | |
| min R, block-grouped a (42..53), L, pooled | 0.943850 | |
Generalized eigenvalues on the 3-dim complement of (1,1,1,1): 0.943850, 0.999365, 1.000192. V4 eigenvalues: -1.3e-16, 0.2919, 0.5467, 1.0488. M eigenvalues: 1, 0.0618653, 4.38e-4, -6.96e-5.
Full-precision values and leave-one-out lists: results.json.

## Result: 1 - lambda2 vs min R
1 - lambda2 = 0.938135, min R = 0.943850, difference 5.71e-3. They do NOT agree to 1e-6 (min R is larger by 0.0057, roughly 16x the SE of lambda2).

## Predicates (fixed in analyze.py docstring before the first run)
- MET: P1 Var>0 for all 4 (class,vector) pairs, pooled and for all 8 leave-one-out sets (32 of 32 sets qualify, plus 4 pooled). P2 all jackknife SEs finite and >0. P3 J_sym symmetric, row sums >0, top eigenvalue of M = 1 within 1e-9. P4 V4 has one null eigenvalue (-1.3e-16) with eigenvector (1,1,1,1)/2 within 1e-9. P5 Csym symmetric to 1e-12 and NS totals equal the sum. P7 control = 1.5.
- FAILED: P6 "|lambda2-(1-minR)| <= 1e-6". It was my own expectation, not a defect of the target. I wrote it down without any reason it must hold, and its tolerance came from the task text. Nothing makes the 4-state J-chain eigenvalue equal a 12-variable block minimum. Recorded as measured only; the failure is kept.
- Measured only: no tolerance claim for the jackknife SEs; they use 8 chains and the SE assumes leave-one-out pseudo-values are comparable.
- Note: the Rust verify output below says a pass authenticates nothing about whether the findings are right.

## Grandchild
Question: independent recomputation of pooled lambda2 and its jackknife SE by two other methods (characteristic polynomial roots, deflated power iteration), with a known-answer control (R=1.500000) first, in grandchild/.
Id: T243 (task-admit event 483, task-release event 484).
Outcome: control 1.500000. lambda2 = 0.06186528489785906 (eigh), ...904 (charpoly), ...914 (power); differences ≤ 8.3e-17. Leave-one-out values and SE 0.000354333164 match mine to about 1e-16. I reread findings.md and reran gc.py with its two file writes redirected to /dev/null, since it opens its outputs with mode "x"; same numbers. It covered lambda2 only, not minR4 or the R values.

## PCP OS
Last line of `pcp_os.py verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
Last line of `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
Init reported the method as not found (expected). Checks K1 check_results (exit 0), K2 analyze.py rerun (expected exit 1, no-overwrite guard: results.json already exists), K3 grandchild control.

## Rerun
cd /home/user/z4-workers/f2-cross2/child; python3 -I analyze.py   # needs results.json removed first (mode "x"); numpy only
python3 -I check_results.py
