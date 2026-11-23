# T19 report: TABLES.md against src/

**Control (control.txt):** `1`. Ric(SU(2)) = 1 (= N/2) in a3-Acurv.PROOF.md, "Conventions" paragraph, line 3 of the file body. The basis e_a = iσ_a/√2 has −Tr(e_a²) = 1, so it is orthonormal.

## Result in one line
No number in TABLES.md is absent, different, or attributed to the wrong file. All derived arithmetic is right. The findings are discrepancies between the sources, and a few spots where the writer repaired or loosened a source. They are listed below.

## Table (presence = same digits and same stated uncertainty in the named file)
Line numbers are the line of the source file.

| Table | Number(s) | Verdict | Where |
|---|---|---|---|
| T1 builder | L3 β4,6: −2.2..−1.5 (8 each); β12–48: −2.30..−1.17 (4 each); L4: −1.60, −1.88; −1.53, −1.58 | present | a3-Acurv.PROOF.md S6 (line 36). "0/8" at L=3 is counted per β in a3-Acurv.report.md line 36. |
| T1 challenger | all 7 ranges and 2 pairs | present | a4-chalcurv.report.md line 18 (A2) |
| T1 open L=4, mechanism, SU(3) | present | a4-chalcurv.report.md lines 19–21 |
| T1 pointwise | 1−2β, 1−4.31β, 1/12, 76/76, ≈6.6β, −6.4, −9.0, −12.2 vs −1.6, −2.0, −1.5 | present | a3-Acurv.PROOF.md S2, S3, S5 |
| T1 derived | union [−2.30, −1.12]; 16+12+4 = 32; 20+4 = 24; 0 of each | OK | recomputed |
| T1 ledger / report | "−1.1 to −2.3", [−2.3, −1.2] | present | A1_LEDGER.md line 28; a3-Acurv.report.md line 15 |
| T2 | all SU(2) values | present | a3-Avort.PROOF.md (iii), lines 70–71 |
| T2 | Z2 0.0774, 0.0041, 0.0061; 3.205, 8.244, 15.84; exact 0.0325242683, 0.6912790067 | present | a3-Avort.report.md lines 36, 58, 62 |
| T2 claim | +1.26 ± 1.05 (1.2σ) | present, but in the report only | a3-Avort.report.md line 39. The PROOF says only "1.2σ". Arithmetic: 2.81−1.55 = 1.26, √(.45²+.95²) = 1.05. |
| T3 | all 9 table entries, 0.217, 11.7 | present | a3-Afs.PROOF.md lines 120–126; a3-Afs.report.md lines 52, 55 |
| T4 | 4/141/584/729, −0.003086419753, −0.002892 ± 0.000237, seed 7, N = 4e7, 27/27 | present | a7-wild.report.md lines 13, 14, 70, 107 |
| T5 | all values | present | a3-C.PROOF.md lines 36, 49, 66, 67 |
| T6 | a√σ, R(0), R(1 step), counts 1500, 840/834, 3.74(12) | present | MATCHED_MEASUREMENT.md, extension table and restart paragraph |
| T6 derived | q, ξ, ξ(1−q), all 9 | OK (tolerance: rounding to the printed digits) | grandchild and my program agree. Unrounded: q 0.2698, 0.3225, 0.3851; ξ 0.7246, 1.0052, 1.4036; ξ(1−q) 0.5291, 0.6810, 0.8631 |
| T6 exponent | ≈ 0.75 | OK | measured 0.740 from the rounded table, so within 0.05. The ledger's derivation is at A1_LEDGER.md line 79. |
| T7 | all values | present | c1-E.report.md lines 15, 16, 18; HYPOTHESIS_E.md lines 46, 48. g_R = 0.34 ± 1.20 and the child's 0.6115 and 0.6107 appear only in HYPOTHESIS_E.md. |
| T8 | all values | present | c1-excl.report.md lines 12, 41, 42, 108 |

## Discrepancies and soft spots
1. **c1-E.report.md line 16 gives four values, "36±2, ≈29, 22±2, 20±3", for "L = 6, 8, 12".** There are four numbers and three sizes. TABLES.md T7 supplies "L = 6, 8, 12, 16" for them. The L = 16 label is the writer's repair of the source, not something in the source.
2. **T8 "below 0.002"** is weaker than the source's "below 0.0015" (c1-excl.report.md line 108). It is true but not the same number.
3. **MATCHED_MEASUREMENT.md gives two values for the N = 12 quantities.** The first table has R(0) = 3.42(12)e−2, R at 2 steps = 5.00(66)e−3 and Q0 = 8.93(11)e−2. The extension table has 3.233(61), 5.90(47) and 9.138(46). The first comes from 160 configurations, the second from the pooled seeds. T6 correctly uses the extension values. The file also admits that the 840 rows include repeated IDs.
4. **Challenger range for κ_H.** a4-chalcurv.report.md says "−1.1 and −2.0" in its bottom line (line 6) and −2.04 in its table (line 18). The ledger says "−1.1 to −2.3", the builder PROOF says −1.17 and the builder report says −1.2. All are the same data at different rounding. TABLES.md's [−2.30, −1.12] is consistent with the detailed tables.
5. **Ricci/Hessian conventions.** Only a3-Acurv.PROOF.md states the normalization (Ric = 1). a4-chalcurv.report.md uses it without stating a value.
6. **Ambiguous source wording (not an error in TABLES.md).** a3-Acurv.PROOF.md S6 "0/8" reads as 8 samples in total, but a3-Acurv.report.md line 36 shows it is 8 per β at L = 3. TABLES.md's "8 each" is correct.

## Programs and predicates
- check_tables.py: 116 tokens tested (no sampling), 115 present. The one ABSENT was a **mistake of my own expectation**: I looked for "+1.26 ± 1.05" in the PROOF, but it is in the report (see the T2 claim row). It is not a defect of the target. Tokens are matched as exact substrings after normalising ± and the minus sign. Some tokens are short (e.g. "0.38", "2.2", "1500"). That is a weakness of the substring test, so I read ranges and lists by hand. No tolerance beyond exact digits was used for presence. For derived values the tolerance is rounding to the printed digits (±0.5 in the last place).
- grandchild/recompute.py (T6 derived): all 9 match; I reran it in rerun_gc/ and the output is identical.
- No for-all predicate was used. The presence test covers all 116 tokens, with no sampling.

## Grandchild
Task id **T20**, admitted with `--label p2-neg-grandchild --parent T19` and released after it returned. Its control was 1.0695, correct. Its outcome: all 9 derived T6 values match the writer's, and I reran and read its script. It uses the same inputs I do, so it is not independent of my reading of the table.

## Rerun commands
```
cd /home/user/z4-workers/p2-neg/child
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
mv results_check_tables.txt old1.txt   # result files open with mode "x"
$P check --ws pcp --name check-tables --expect-exit 0 -- python3 -I check_tables.py
(cd rerun_gc && mv results.txt old.txt; $P check --ws ../pcp --name rerun-grandchild --expect-exit 0 -- python3 -I recompute.py)
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
(`$P init` reported the method as not found, as expected.)

## Verify, last lines
- Python: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Rust: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Same model family throughout; this is not independent review.
