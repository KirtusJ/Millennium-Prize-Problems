# Disposition report: two Yang–Mills lanes (transfer-operator, g4)

Worker r4-b for Director Z4. This report extracts what the notes claim; it does not judge whether their proofs are correct. The sub-agent and I share a model family with the authors, so our agreement is not independent review. Control value: −ln(tanh 1) = 0.272341 (control.txt).

## 1. Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| Control (−ln tanh 1 = 0.272341) | STANDS | control.txt; the child obtained the same value independently |
| File-count hypothesis: 28 .md (18 transfer-operator, 9 g4, 1 README) | STANDS | count_files.py run through the PCP register, check K1 exit 0; count_result.txt |
| transfer-operator lane: what it establishes | STANDS as extracted | All results are at a FIXED spatial mesh: a gap uniform in time step and volume, a joint a→0, L→∞ local limit, and positivity at fixed mesh. On spatial refinement it gives only obstructions. It claims nothing for the 4D continuum. |
| g4 lane: what it establishes | STANDS as extracted (sub-agent rows, 6/6 spot-checked) | Reflection positivity on a finite open slab (text proof only). Lean-checked lemmas that RP is preserved under limits, conditional on a limit existing. Pushforward transport. No continuum, gap or nontriviality claim. |
| Any note claiming a Clay requirement for the 4D continuum | NONE FOUND | Both lanes disclaim it explicitly (transfer-operator/README.md last §; g4/README.md line 3) |
| Lean/mutation counts reported by the notes | NOT CHECKED | No .lean source is in input/. Counts are copied from the execution notes. |
| Direct contradictions between statements | NONE FOUND | 4 convention clashes without a stated conversion (§6) |

Counts (met, failed, measured only): **6 met, 0 failed, 1 measured only**.
- Met: the control; P1 and P2 of count_files.py; the child's g4-count predicate; the spot-check of the child's rows (6/6); "no note asserts a continuum requirement".
- Measured only: the reported Lean and mutation totals.

Hypothesis count (rule 4): input/ holds 28 .md files, namely yang-mills_README.md and 27 lane notes.
- transfer-operator: 18 files. 13 state a result and 5 are execution logs. I read all 18 in full.
- g4: 9 files. 6 state a result (counting cross-lane-review) and 3 are execution logs. The child read all 9 in full. I read 6 of them in full to check its rows, and checked the 3 execution logs by grep for their counts.
- No file is NOT READ.

## 2. Per-note rows

