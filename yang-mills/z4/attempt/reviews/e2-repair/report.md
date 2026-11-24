# e2-repair report (T230) — side-six record repair (final)

Worker e2-repair, Director Z4, principal Kirtus Justus. Control: control.txt = 0.272341 (−ln tanh 1).
All numbers below are produced by programs in this directory, run through the PCP register `pcp/` (checks K1–K7).
The child shares my model family (it is a lower tier); our agreement is a recomputation, not independent review.

## 1. Verdict table

| # | item | verdict | evidence (one line) |
|---|---|---|---|
| 1 | G4 finding (1): reduce.py splits hot/cold by lexical list position | **DEFECT** (of our reducer; G4 is right) | `sorted(..., key=p.name)` then `main[0::2]`/`main[1::2]`; legacy recomputation reproduces PRIOR_TABLES z exactly (−1.62, 0.67, 0.42, 1.64, −1.14) |
| 2 | G4's corrected one-face hot−cold z 1.21, −0.58, −0.30, −2.68, 0.66 | STANDS | reduce_fixed.py: +1.21, −0.58, −0.30, −2.68, +0.66; four-face at L-d2 −0.33 (G4 −0.33) |
| 3 | Prior "L-d2 hot/cold control MET" (one-face) | **DEFECT** | corrected z = −2.68, |z| > 2 → FAILED; only verdict change among 12 runs × 2 marks |
| 4 | Pooled estimators and their errors unaffected by the split bug | STANDS | reduce_fixed pooled r1, r4 and errors equal PRIOR_TABLES for all 12 runs |
| 5 | reduce.py `per_stream` records (24-stream runs) | **DEFECT** (new, not in G4) | L-d2 summary.json per_stream "stream 2, hot 0" holds s10's data (J1 0.0082581 = s10, s2 is 0.0081610) |
| 6 | Archived hot flags equal numerical ID parity | STANDS | F1 assertion passed for every stream of all 12 archived runs and the 64 new streams |
| 7 | Prior claim "one-face quotient at 2/β relative to 0 is 1.016(11)" | STANDS as registered (R5 "reproduced"), but its excess over 1 is **not** confirmed | new Q1 = 1.0036(110), |Q1−1.016| = 0.012 ≤ 0.031; Q1 is also 0.33σ from 1; archive gives 1.0158(106) |
| 8 | New run hot/cold control with numerical split (R3, 2 arms × 2 marks) | STANDS | z: N-d2 r1 +0.10, r4 −0.53; N-d0 r1 −0.43, r4 −0.28 |
| 9 | New run burn-in drift (R4) with doubled burn-in | **DEFECT** (1 of 4) | N-d0 four-face d = +2.11 > 2; all four half-differences positive (+1.71, +0.77, +1.61, +2.11) |
| 10 | Four-face quotient Q4 = r4(2/β)/r4(0) | measured only | new 1.0335(128) vs archive L-runs 1.0218(146); on first/second halves 1.0490(205)/1.0177(187) |
| 11 | (c) Clear references, raw B vs normalised traceless B, side six | STANDS (G4's numbers) | r4 raw .09201, .08599, .09281; traceless .08476, .08266, .09546 = G4 to 5 decimals (C1) |
| 12 | G4 finding (2), mixed conventions in headlines | side six: STANDS (headline used raw B); side eight: NOT CHECKED | PRIOR_TABLES main J4/V4 column = raw; side-eight data not in this directory |
| 13 | Child's independent reduction of the new run | STANDS | all numbers equal mine to 4e-16; reran its code (K8), identical; see §8 |

Counts (registered predicates, raw-B marks): **met 71, failed 3, measured only 9** (§3 lists failures; §2 items marked "measured only").
Breakdown: F1 12/0; F2 (old hot/cold) 23/1; F3 (old drift, my reducer's predicate applied post hoc) 23/1; C1 1/0; R1 2/0 (64 sampler calls); R2 2/0; R3 4/0; R4 3/1; R5 1/0.
Measured only: Q4; Q1 vs 1; paired-index jackknife errors (Q1 0.0117, Q4 0.0145); paired half-difference drift; Q per half (2); traceless versions; legacy lexical z; old-data per-stream mislabel.

## 2. (a) Old vs corrected hot/cold z, every archived row

Code: reduce.py `files = sorted(d.glob("s*.csv"), key=lambda p: p.name)` → s0, s1, s10, s11, …, s19, s2, s20, …; `cold = est(main[0::2]); hot = est(main[1::2])`. For 24 streams this places e.g. s10 (cold start) in "hot". For the 8-stream rows lexical = numeric order; only the sign convention differs (old z = cold−hot, G4 and the fix = hot−cold).

| run | old z r1 (cold−hot, lexical) | corrected z r1 (hot−cold, numeric) | old z r4 | corrected z r4 | verdict change |
|---|---:|---:|---:|---:|---|
| d0 | −0.03 | +0.03 | −1.28 | +1.28 | none |
| d0.5 | −1.30 | +1.30 | +0.19 | −0.19 | none |
| d1 | −0.66 | +0.66 | −0.69 | +0.69 | none |
| d2 | +0.94 | −0.94 | −0.68 | +0.68 | none |
| clear0 | +0.66 | −0.66 | +1.49 | −1.49 | none |
| clear2 | +1.52 | −1.52 | +0.93 | −0.93 | none |
| clear4 | +1.13 | −1.13 | −0.02 | +0.02 | none |
| L-d0 | −1.62 | +1.21 | −0.85 | +0.34 | none |
| L-d0.5 | +0.67 | −0.58 | −0.59 | +1.20 | none |
| L-d1 | +0.42 | −0.30 | +0.14 | −0.52 | none |
| L-d2 | +1.64 | **−2.68** | −0.42 | −0.33 | **one-face MET → FAILED** |
| L-d4 | −1.14 | +0.66 | −0.79 | +0.21 | none |

Traceless-B z equals raw-B z on the d-rows (identical columns there); clear rows traceless one-face: −0.38, −2.00 (clear2, at the boundary, MET), −1.54. Archive Q1 = r1(L-d2)/r1(L-d0) = 1.0158(106) independent, 1.0158(93) paired-by-index (sensitivity; L-d2/L-d0 seeds are not paired).
New fixed reducer: reduce_fixed.py (numeric-ID order; hot = ID % 2; hard assert against the meta "args" hot token).

## 3. (b) New run, side 6, T = 12, β = 3.276133577 (REGISTRATION.md, sha256 b094da48…b539, hashed 01:45:40Z before the first stream)

32 streams per arm (16 hot = odd ID, 16 cold), burn-in 1152 sweeps (prior L-runs 576), 1152 measurements 6 sweeps apart.
Fresh seeds: N-d2 9310007 + 7919 i, N-d0 9420013 + 7919 i, i = 0..31 (9310007 … 9555496; 9420013 … 9665502); 0 collisions with any 5–9-digit integer in non-CSV files under /home/user/z4-workers. Errors: delete-one-stream jackknife.

| arm | J1 | Var1 | r1 = J1/Var1 | J4 | Var4 | r4 = J4/Var4 | z hot−cold r1 / r4 | drift d r1 / r4 |
|---|---:|---:|---:|---:|---:|---:|---|---|
| N-d2 (δ = 2/β) | 0.0080467(340) | 0.12836(77) | 0.06269(47) | 0.0028914(120) | 0.05911(41) | 0.04891(38) | +0.10 / −0.53 | +1.71 / +0.77 |
| N-d0 (δ = 0) | 0.0077296(394) | 0.12375(81) | 0.06246(49) | 0.0029112(117) | 0.06151(55) | 0.04733(46) | −0.43 / −0.28 | +1.61 / **+2.11** |

Strata: N-d2 r1 hot/cold .06274/.06264, r4 .04871/.04911; N-d0 r1 .06226/.06268, r4 .04720/.04746.
Ratios (independent-arm errors — seeds are independent; paired-by-index jackknife in brackets as sensitivity only):
- Q1 = r1(2/β)/r1(0) = **1.0036 ± 0.0110** [0.0117]
- Q4 = r4(2/β)/r4(0) = **1.0335 ± 0.0128** [0.0145]
Traceless-B values identical to raw on these prescribed skeletons.

**Verdict on "one-face quotient at 2/β relative to 0 is 1.016(11)": reproduced** by the registered rule R5 (difference 0.012, tolerance 2√(0.0110²+0.011²) = 0.031). But the new central value is 1.004 and Q1 is consistent with 1 (0.33σ); the combined evidence does not support a nonzero one-face excess at 2/β. The four-face Q4 is 2.6σ above 1 in the new run and 1.5σ in the archive.
Drift (measured-only follow-up, drift_paired.py, paired jackknife over streams): D/err r1 +1.65 (N-d2), +1.55 (N-d0); r4 +0.71, +1.98. All four positive; Var falls and r rises from the first to the second half in both arms, so a residual slow relaxation after 1152 burn-in sweeps is plausible. Q1 is stable across halves (1.0034 → 1.0039); Q4 is not (1.0490 → 1.0177), so Q4 should not be quoted to better than ~2%.

## 4. (c) Clear-reference conventions, side six (results_fixed/clear_conventions.md)

| skeleton | min angle from −I | r1 raw B | r1 traceless B | r4 raw B | r4 traceless B |
|---|---:|---:|---:|---:|---:|
| clear0 | 1.14269 | 0.08052(208) | 0.07003(153) | 0.09201(241) | 0.08476(340) |
| clear2 | 0.95857 | 0.07157(146) | 0.06828(75) | 0.08599(203) | 0.08266(254) |
| clear4 | 1.18204 | 0.07140(206) | 0.07068(183) | 0.09281(228) | 0.09546(343) |

Side eight's values are in G4's readback (raw .09052(453), .10824(527), .08237(393); traceless .08984(352), .10826(528), .07420(369)); I did not recompute them.

## 5. Hypotheses and where they are stated
- Estimators (pooled ddof-0 variance, J mean, r = J/Var, stream jackknife): reduce.py docstring, reduce_fixed.py docstring, REGISTRATION.md.
- Hot flag = ID % 2 and recorded in meta "args" token 4: run.py/run_big.py (z1-mix6), run_new.py, REGISTRATION.md; asserted in reduce_fixed.py (F1).
- Tolerance 2 on hot/cold z with SE = 2 × pooled jackknife error: z1-mix6 run.py T2 (prior preregistration), REGISTRATION.md R3.
- Drift halves treated as independent (R4): REGISTRATION.md; neglects within-stream correlation (checked by drift_paired.py).
- Independence of arms for Q errors: REGISTRATION.md (independent seeds).
- R5 reproduction tolerance 2√(e²+0.011²): REGISTRATION.md.
- Skeleton d2 has δ = 2/β = 0.6104757 (header of skeletons/d2.txt; min angle in meta 0.610476); d0 has δ = 0.
- Archived data in ../z1-mix6/results are the data PRIOR_TABLES was made from: supported by the legacy recomputation matching the table.

## 6. Failed predicates (all kept)
1. F2 L-d2 one-face hot/cold z = −2.68 (archive) — defect of the target (prior record's control was misreported as MET because of the reducer bug).
2. F3 d0.5 (8-stream archive) one-face drift d = −2.08 — post-hoc application of my reducer's drift predicate to a run that never registered it; target-side observation, weak (8 streams).
3. R4 N-d0 four-face drift d = +2.11 — registered; my expectation (doubled burn-in suffices) failed; it is a property of the sampler's relaxation, not a code defect (child reproduces 2.110).

## 7. Not checked
- Side-eight anything (data not present here); G4's angle geometry (81 face products) beyond the meta min angles; the per-colour decomposition; the signed-angle symmetry argument; the clear-background selection; the sampler's correctness (taken as given, exit 0 + its internal asserts only); a two-time measurement (G4's further request); longer burn-in than 1152 sweeps (the drift suggests it is needed for Q4).

## 8. Delegated questions
- **Child** (task T233 under T230; admitted, run as pcp check K7 `child-run1`, exit 0 in 63 s, released): independent reduction of the new run from the per-stream files (J1, Var1, r1, J4, Var4, r4, numeric-ID hot/cold z, half drift d, Q1, Q4, meta-flag check). Control question −ln tanh(1/2) = 0.771937: **graded first, correct**. Its prompt held only definitions, not my notes or numbers.
  Returned: every number equal to mine (max difference 4.4e-16 relative); Q1 = 1.0036 ± 0.0110, Q4 = 1.0335 ± 0.0128; meta flags 64/64; the same R4 failure (N-d0 r4 d = 2.110). It kept two of its own failed runs (JSON bool bug). I reread child/reduce.py (independent code: own loader, own jackknife, strata by `range(1,32,2)`) and reran it unchanged in childcheck/ (K8 `child-rerun`): output byte-identical as JSON to its results_run3.json.
- **Grandchild** (task T237 under T233; admission and release present in the graph): no-numpy recomputation of pooled Var1 of N-d0; control var(1,2,3,4) = 1.25 (correct). Returned Var1 = 0.123747700718, mean j_single = 0.00772964793526 over 36864 rows; agrees with my 0.1237477 and J1 0.0077296.
- Caveat: child and grandchild share my model family; this is a recomputation from the same definitions, not an independent review of the definitions.

## PCP verification (last lines)
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
Task graph: T230 (mine), child T233 admitted+released, grandchild T237 admitted+released.

## 9. Rerun commands
See REPLAY.md, section "e2-repair additions" (all commands with all arguments). Summary:
```
cd /home/user/z4-workers/e2-repair; P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name reduce-old --expect-exit 0 -- bash reduce_old.sh
$P check --ws pcp --name clear-table --expect-exit 0 -- python3 clear_table.py
$P check --ws pcp --name run-N-d2 --expect-exit 0 -- python3 run_new.py N-d2 skeletons/d2.txt 9310007
$P check --ws pcp --name run-N-d0 --expect-exit 0 -- python3 run_new.py N-d0 skeletons/d0.txt 9420013
$P check --ws pcp --name reduce-new --expect-exit 0 -- bash reduce_new.sh
$P check --ws pcp --name drift-paired --expect-exit 0 -- python3 drift_paired.py
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
(results_fixed/ and results/N-* must not exist before a rerun; outputs are create-new.)
