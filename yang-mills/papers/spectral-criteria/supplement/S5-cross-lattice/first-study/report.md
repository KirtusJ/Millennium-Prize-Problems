# e2-cross report — worker under T231 (Director Z4), 2026-11-24

## Verdict table
| # | Item | Verdict | One line of evidence |
|---|---|---|---|
| 1 | Control -ln(tanh 1) | STANDS | control.txt = 0.272341 |
| 2 | G4's 2l four-bin endpoints .06197 (side 5) and .00408 (side 10) from its streams | STANDS | own reducer src/control_reduce.py on g4/cyclic-transfer/unz: 0.0619674 ± 0.0025710, 0.0040821 ± 0.0007179 (results/control_reduce.out.txt) |
| 3 | G4's 4l endpoints .06157 and .00169 | NOT CHECKED | long-streams.zip is not in g4/cyclic-transfer; G4's winding.py crashes there |
| 4 | Setup: N=5 β=3.196581051, N=10 β=3.493705679; T=2N (2l), 4N (4l); lag l/5 = 1 step on N=5, 2 steps on N=10; common coarse links = straight spacing-two products on the even sublattice | STANDS | winding.rs (`stride=n/5`, `lag=stride`, `step_by(stride)`) and measurements.md; couplings copied, not recalibrated |
| 5 | Comparison in R form, R_fine(f) ≥ α R_coarse(f), α ≤ 1: is there a frozen eligible test that breaks it? | STANDS (not defeated) | 22 frozen tests on held-out chains: smallest R_f/R_c = 0.999 ± 0.008 at 2l and 1.002 ± 0.004 at 4l. None is significantly below 1, 0.5 or 0.1 |
| 6 | Comparison in E form, E_fine(f) ≥ c E_coarse(f), with c ≥ 0.0042 | DEFECT | one frozen test (the ratio-optimal test trained at 2l) gives held-out E_f/E_c = 0.00407 ± 0.00005 at 2l and 0.00409 ± 0.00007 at 4l (results/cross-eval.txt). Its Var_f/Var_c is 0.0034 and its R_f/R_c is 1.21 to 1.23, so the variance ratio drives it, not slower decay |
| 7 | G4: at lag l/5 side 10 keeps less correlation than side 5 | STANDS (for my slice-averaged tests) | every held-out R_fine is in [0.976, 1.003]; R_coarse is in [0.597, 0.997] |
| 8 | G4: the fine result shifts between preparations | STANDS (small in my tests) | f4 vs f2: 5 tests have R(f4)/R(f2) significantly < 1, the smallest 0.9867 ± 0.0037. c4 vs c2: no test differs (results/analysis-null-*.txt) |
| 9 | Spectral deficit inequality b_f ≥ α d_c | NOT CHECKED | needs a certified lower bound on the full coarse deficit, which nobody has; by the rule fixed before the runs, items 5 and 6 do not bear on it |
| 10 | Gauge invariance and center neutrality of my observables, tested numerically | NOT CHECKED | argued only: all observables are traces of closed loops, squared windings or products of these. No gauge-transform self-test was run |

Interpretation rule, written before the runs (src/analysis_predicates.txt): a single frozen eligible test with held-out ratio < x at both temporal circumferences defeats an energy comparison with constant c ≥ x for that pair. It does NOT defeat the spectral deficit inequality. "Significantly below y" means ratio + 2 SE < y.
Applied to the E form: one test is significantly below 0.005 at both circumferences, so E-comparisons with c ≥ 0.0042 are defeated for this pair (ratio + 2 SE ≈ 0.0042 at both).
Applied to the R form: no test is significantly below 1 at either circumference.

Predicate counts: **met 20, failed 0, measured only 9**.
- Met (20): control C1 and C2 on n5 and n10 (4); P1 hot/cold and half/half on c2, c4, f2, f4 (8); P2 τ_int of Pa1 and Wa1 on 4 ensembles (8).
- Measured only (9): P3 hot/cold R agreement on 4 ensembles (c2 has 1 of 16 disagreeing, the others 0); the main tables 2l, 4l, two period nulls and cross-eval (5).
- P2 for Wa1 on f4 is marginal: 24.63 against a limit of 25. On f2 it is 2.82.

## Main numbers (held-out chains i%4 ∈ {2,3}; delete-one-chain jackknife, 8 chains per lattice)
| Test (frozen on TRAIN) | 2l R_f | 2l R_c | 2l R_f/R_c | 2l Var_f/Var_c | 4l R_f/R_c | 4l Var_f/Var_c |
|---|---|---|---|---|---|---|
| fine-optimal (min R_fine) | 0.986(2) | 0.673(14) | 1.466(30) | 0.176 | 1.521(27) | 0.62 |
| coarse-optimal (min R_coarse) | 0.989(5) | 0.609(18) | 1.624(48) | 0.619 | 1.575(28) | 0.577 |
| ratio-optimal (min E_f/E_c) | 0.996(5) | 0.822(5) | 1.212(10) | 0.00336 | 1.247(9) | 0.00328 |
| Wa1 (slice-avg squared winding) | 0.989(5) | 0.701(6) | 1.410(14) | 0.54 | 1.416(20) | 0.54 |
| Pa1 (coarse plaquette A1) | 1.000(4) | 0.957(6) | 1.045(7) | 2.95 | 1.049(4) | 2.96 |
| Pe² (smallest R ratio) | 0.996(3) | 0.997(8) | 0.999(8) | 10.5 | 1.002(4) | 10.6 |
Full tables are in results/analysis-2l.txt and results/analysis-4l.txt. The training fine-optimal R_fine was 0.973 (2l) and 0.977 (4l), so the slowest inherited mode in this 16-function span decorrelates almost completely on the fine lattice at lag l/5.

## Hypotheses each statement uses, and where they are stated
- Matched couplings for g²_SF(l)=2.38: taken from g4/cyclic-transfer/measurements.md (calibration in physical-refinement/methods.md). Not rechecked.
- Sampler correctness: g4/wilson_mc.rs, included verbatim in src/cross.rs. winding.rs includes ../../g4/full-attempt/two-site-gap/wilson_mc.rs, which is not in this tree, so I assume the two files are identical. Heat bath only, as in winding.rs.
- Stationarity: predicates P1 and P2 (src/analysis.py docstring). Chains are independent through distinct SplitMix seeds (REPLAY.md).
- Eligibility: g4/G4_FINAL_AUDIT_2026-11-23.md, table row 1. All observables are fixed functions of the even-sublattice spacing-two links on N=10 and of the links themselves on N=5. The same code (`obs` on the 5³ coarse slice) is used on both lattices.
- Finite periodic T is not the vacuum: g4/cyclic-transfer/vacuum.md. None of the numbers here is a vacuum or full-orbit statement.
- Convention difference from G4: my W_μ is the slice average over 25 lines of (½ Tr W)². G4 pools the per-line joint histogram and does not average values. These statistics are related but not the same.

## Failed predicates
None. The only expectation of mine that failed: I expected f4's winding MC autocorrelation to be similar to f2's (about 3). It was 24.6, just inside the limit. This is my expectation, not a defect of the target. Errors use the chain jackknife and do not depend on it.

## What I did not check
- G4's 4l streams (absent).
- A G4-style per-line pooled four-bin statistic on my own ensembles; single-line (not slice-averaged) observables.
- Skeletons on the odd sublattice.
- The coupling calibration.
- A numerical gauge or center-flip invariance test of src/cross.rs observables.
- A Haar null run of my instrument.
- That g4/wilson_mc.rs is the file winding.rs includes.
- Any spectral or full-orbit bound.
- Lean (ready, but not used).

## Delegated questions and outcomes
- Child T235 (admitted under T231 and released; child_admit.log, child_release.log). Question: independent reduction of my per-chain S1/S00/SL sums (c2, f2, held-out chains) to held-out R and jackknife SE for four tests fixed in its prompt (Wa1, Pa1, Wa1², P_yz−P_xz).
  - Control (periodic 1,2,3,4: R = 1.2): answered 1.2. Graded correct before I read anything else.
  - Result: c2 0.701337, 0.956860, 0.706880, 0.968748; f2 0.988970, 0.999851, 0.988906, 0.999851. These agree with my analysis to all printed digits, SEs included.
  - I reread child/analyze.py and reran it under PCP (child-rerun, in scratch/childrerun): the output is byte-identical.
  - Both use the same specified formula, so this checks the implementation, not the method.
- Grandchild T236 (admitted under T235 by the child and released; both events are seen in /home/user/z4-work/graph/attempt.jsonl). Question: recompute R(Wa1) on c2 held-out chains. Its control was 1.2 (child/grandchild/control.txt). The child reports it returned R = 0.7013370728, matching. I did not rerun the grandchild's script myself.
- The child is the same model family, lower tier. Its agreement is not independent review.

## Exact commands
See REPLAY.md: every command with all arguments and seeds. Bases are c2 5101307, c4 5201307, f2 5301307, f4 5401307, and chain i uses base + 7919 i.

## PCP verification (last lines)
- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
