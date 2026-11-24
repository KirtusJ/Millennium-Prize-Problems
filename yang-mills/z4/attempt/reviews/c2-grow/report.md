# c2-grow report (T223): grown mark list on the frozen skeleton, and gated physical time

I share a model family with the director, so my agreement is not independent review. The child (T224, Sonnet) ran an independent code on my per-stream matrices, but it used the same method (eigen-whitening with truncation), so it checks my code and not my method. Raw data are in `results/<tag>/` and `results_q2/<tag>/`. The step-by-step record is `notes.md` and the rerun commands are in `REPLAY.md`. I made no Lean claim and did not use Lean.

**Setting.**
- Side 6, period 12, β = 3.276133577. The skeleton is fixed.md's: the y edge at (2,0,0) is W = −I, the z edge there is B = i, and every other frozen link is I. The skeleton file comes from the prior `mkskel.py`.
- The clear contrast is the prior chain.skel0, regenerated exactly by `clear.py`: 40 of 60 skeletons qualify at π/4, the kept ones are 0, 2 and 4, and the min angle is 1.142692.
- Each run is 32 streams × 1152 measurements. Seed = base + 7919 i and hot = i % 2. Train on streams 0–15 and hold out streams 16–31. Each stream discards 576 sweeps and measures 6 sweeps apart.

**Sampler.** `build/z1mx4` (source `build/src/c2/z1mx4.rs`) is the prior z1mx3 with the mark list replaced:
- **Ring 1:** the 7 coarse faces containing a changed edge, from `faces.py`. At d0 their holonomies (gauge-mode printout) are:
  - xy000, xy200 and yz204: −I. These are the three faces through the W edge.
  - xz000 = +i, xz200 = −i, yz200 = +i and yz240 = +i. These are i-type faces at angle π/2; yz200 contains both changed edges.
- **Ring 2:** the 33 faces sharing a coarse edge with ring 1. All are +I at d0.
- **References:** B, the full xz coarse holonomy at the root, and T = 1, the plain trace. At W = −I the residual stabiliser is the U(1) about i, so these are the only invariant references.
- **Marks per face:**
  - The four fine plaquettes, transported to the root along frozen links (x, then y, then z; a coordinate of 4 is reached by two − steps), each against B.
  - The partial loops Rv, Rh and L_no11, against B.
  - For ring 1 only, the four plaquettes against T.

**Nested lists:**
- L1 = the prior 15 marks on the three −I faces, reproduced exactly (P8).
- L2 = all ring-1 B marks, 7 × 7 = 49.
- L3 = L2 plus the ring-2 B plaquettes, 181 marks.
- L4 = all 308 marks: L3 plus the ring-2 B partial loops and the ring-1 T plaquettes.

**Estimators:** as in the prior record (`an4.py`). D is the colour-averaged two-copy refresh loss, now accumulated sparsely and summed over colours. C is the pooled plug-in covariance. The eigenproblem is solved on the training half by C-whitening, truncating directions below 1e-10·max. The reported value is the held-out quotient with a delete-one-held-stream jackknife.

## Verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| Control: −ln tanh 1 | STANDS | control.txt = 0.272341 |
| z1mx4 is a pure extension of z1mx3 (P8) | STANDS | Same seed: `.csv` and `.colours.csv` byte-identical; the 15 L1 marks are identical; the D diagonal differs by 3.8e-13 relative (K4). |
| Gauge invariance of all 308 marks (P6) | STANDS | Random full gauge transform: max change 1.2e-15 (K2). |
| Q1, d0: the held-out optimum falls L1 → L2 | STANDS (still falling there) | .02083(47) → .01668(44): z = −6.4 on combined se. The "stopped falling" predicate FAILS here. |
| Q1, d0: 'the optimum has stopped falling' at the largest lists (L2→L3, L3→L4) | STANDS as defined by the brief's predicate, with a caveat | L3 .01587(42), z = −1.33; L4 .01543(40), z = −0.77. Both are within 2 combined se, so the predicate is met. The paired jackknife on the same held-out streams still shows real falls: −.00081 (paired z −15) and −.00044 (paired z −12). The fall per step shrinks from 20 % to 5 % to 3 %; it has not stopped. |
| Q1, d0: the weight sits on the three −I faces through the W edge | STANDS | L4 face shares: yz204 .32, xy200 .25, xy000 .25 (sum .81); yz200 (i-type, contains both edges) .09; every other face ≤ .01. |
| Q1: −I against clear contrast survives the grown list | STANDS | Held-out L4: −I .01543(40) against clear .04283(44), ratio 2.78. L1: .02083 against .05894, ratio 2.83. |
| Q1, clear skeleton: the optimum has stopped falling | DEFECT (it keeps falling) | .05894 → .05333 → .05095 → .04283: z = −6.1, −3.6 and −13.7, all FAILED. The largest step is L3 → L4. |
| Independent eigen-solve and held-out evaluation for L4 (child T224, grandchild T225) | STANDS | Child: λ_train .015708941, q_held .015427728(396), equal to mine at full precision. Rerun of its program: identical results.json (K10). |
| Q2: gated three-face composite C(t)/C(0), θ = 0.6 and θ = 1.2 | NOT CHECKED (not resolved) | Gated pairs at t = 1: 0 (θ 0.6) and 52 (θ 1.2, about 13 independent events) out of 32000 configurations, below the 200-pair rule. No number is given. |
| Q2: gate fractions of the three −I-class faces | NOT CHECKED (measured only, no claim) | θ < 0.6: 6.4(2.6)e-8. θ < 1.2: 1.486(14)e-4 of all (root, orientation, slice) sites. |
| Q2: ungated composite (L4 weights) against the single four-face mark | NOT CHECKED (measured only, no claim) | R(1) .01280(33) against .01315(30), paired −.00036(40). R(2) .00010(24) against .00087(20), paired −.00077(29), z −2.6. |
| Q2 sampler checks (gauge invariance, prior formula, plaquette, prior single-mark R(1)) | STANDS | Q3-P1 ≤ 1.8e-14. Q3-P2 6e-17. Plaquette .7500045(149) against prior .7500018(40), z .18. Ungated single R(1) .01315(30) against prior .01354(9), z −1.22. |

## Q1 table (held-out optimum with jackknife; β·q in brackets)

| skeleton | list | marks | cond C_train | train λ | held-out q | rel err | optimism gap (fwd / symmetrised) | weight support by face (share of Σ (w_k sd_k)²) |
|---|---|---|---|---|---|---|---|---|
| −I (G-d0) | L1 | 15 | 49.1 | .02134 | **.02083(47)** [.0682] | 2.3 % | −.00051 / +.00001 | yz204 .42, xy000 .29, xy200 .29 |
| −I | L2 | 49 | 82.8 | .01724 | **.01668(44)** [.0546] | 2.7 % | −.00056 / +.00005 | yz204 .34, xy200 .27, xy000 .26, yz200 .12, xz200 .01, xz000 .01 |
| −I | L3 | 181 | 86.3 | .01625 | **.01587(42)** [.0520] | 2.6 % | −.00038 / +.00013 | yz204 .31, xy200 .23, xy000 .23, yz200 .10, xz224 .02 |
| −I | L4 | 308 | 2.4e16 (4 exact null directions truncated; 359 on the range, from the child) | .01571 | **.01543(40)** [.0505] | 2.6 % | −.00028 / +.00018 | yz204 .32, xy200 .25, xy000 .25, yz200 .09, xz224 .01 |
| clear (G-clear0) | L1 | 15 | 12.3 | .05874 | .05894(76) [.1931] | 1.3 % | +.00021 / +.00050 | xy200 .41, yz204 .37, xy000 .21 |
| clear | L2 | 49 | 28.3 | .05135 | .05333(53) [.1747] | 1.0 % | +.00197 / +.00190 | xy200 .46, xz200 .26, yz204 .16, xy000 .09 |
| clear | L3 | 181 | 28.8 | .04820 | .05095(40) [.1669] | 0.8 % | +.00276 / +.00210 | xy200 .33, xz200 .23, yz440 .08, xy240 .05 |
| clear | L4 | 308 | 259 | .04097 | **.04283(44)** [.1403] | 1.0 % | +.00186 / +.00170 | xy200 .55, xz200 .25, yz204 .06, xy000 .03 |

Notes on the table:
- **Forward optimism gap** = held − train. At −I it is negative: the held-out half is slightly easier. The swap test (`swap4.py`: train on the held half, evaluate on the train half) gives the symmetrised gap, which is positive in every case (S1 met).
- **Stability of the −I direction:** cos(w, w_swap) in the C metric is .9999, .9995, .9987 and .9985 for L1–L4. On the clear skeleton it is .977, .413, .860 and .960, so its L2 direction is ill defined.
- **The i-type faces at −I:** dropping them from L2 (21 marks on the three −I faces) gives .01792(44). So the four i-type faces, mainly yz200, account for .0012 of the L1 → L2 drop of .0042. The partial loops on the two newly covered −I faces account for the rest.
- **Exact degeneracies in L4 at −I:** on each i-type face f (holonomy ±B), Re(B·L_no11,f) = ∓Re(g11,f) identically. This gives 4 null directions of C and D, which are truncated. It is a property of my list, not of fixed.md. The clear skeleton has no exact degeneracy (cond 259).
- **Colour support of w(L4) at −I** (diagonal-only proxy, held half): colours 0–3 .13/.13/.12/.12; colours 16, 18, 20 and 22 .10/.10/.10/.11; colours 8, 9, 12 and 13 about .015 each; the rest 0.

**Predicate G1** ('the optimum has stopped falling' := |q_{n+1} − q_n| ≤ 2·sqrt(e_n² + e_{n+1}²)), fixed in the an4.py docstring before the runs:

| skeleton | L1→L2 | L2→L3 | L3→L4 |
|---|---|---|---|
| −I | FAILED (z −6.42) | MET (z −1.33) | MET (z −0.77) |
| clear | FAILED (z −6.06) | FAILED (z −3.57) | FAILED (z −13.71) |

Measured only: the paired jackknife z at −I is −38, −15 and −12, and on the clear skeleton −8.6, −5.8 and −15.3.

My reading: at −I, the brief's predicate says "stopped falling" at the largest lists. The same-data paired comparison shows the fall continuing at about 3–5 % per step. This is far smaller than the 20 % drop from completing ring 1. The weight stays on the three −I faces through the twisted edge. The clear skeleton is still falling by 16 % at the last step, so the −I/clear contrast shrinks slightly from 2.83 (L1) to 2.78 (L4) and could shrink further.

## Question 2 (unconditioned measure, matched point)
- **Program:** `build/q3` (source `build/src/c2/q3.rs`), driven by `run_q3.py`.
- **Chains:** 16 (8 cold, 8 hot), seed = 12100001 + 7919 i. Each chain discards 1000 cycles (one heat-bath plus one over-relaxation sweep) and then takes 2000 configurations one cycle apart, 32000 in total.
- **Composite:** the w of L4 at −I, the best list (`results/G-d0/w_L4.txt`, 308 weights). It is evaluated at every root (27 even spatial sites × 12 slices) and every one of the 48 orientations (signed axis permutations applied to every loop step).
  - Each B-type mark uses B_c⁰, the normalised traceless part of the mapped coarse xz loop at the root. T-type marks are plain traces.
  - The gate: all three mapped faces xy000, xy200 and yz204 (the −I faces carrying .81 of the weight) have arccos(−½Tr h) < θ.
  - The mark is m = Σ w_i X_i on gated sites and 0 elsewhere, with C(t) centred over all sites.
- **Ungated marks:** identity orientation only. Every orientation has the same law by the lattice symmetry of the measure, which is a stated hypothesis.
- **Pair-count rule (R1, from the brief):** a gated R(t) is reported only with at least 200 gated pairs at t = 1. It FAILED at both θ, so no gated number is given.

| mark | gate fraction | gated pairs t = 1, 2, 3, 4 | R(1) | R(2) | R(3) | R(4) |
|---|---|---|---|---|---|---|
| three-face gate θ < 0.6, composite / single | 6.4(2.6)e-8 (32 sites, 8 events) | 0, 0, 0, 0 | not resolved | | | |
| three-face gate θ < 1.2, composite / single | 1.486(14)e-4 | 52, 4, 12, 8 | not resolved | | | |
| ungated composite (L4 w) | 1 | — | .01280(33) | .00010(24) | .00007(27) | .00001(27) |
| ungated single four-face mark | 1 | — | .01315(30) | .00087(20) | .00013(24) | .00012(36) |

Gated site counts come in multiples of 4. The unordered three-face set is fixed by the x-reflection about x = 2 and the y-reflection about y = 1, so the number of independent gate events is the count divided by 4. That gives about 13 events at t = 1 for θ = 1.2.

Getting 200 pairs at θ = 1.2 would need about 4× the configurations for 200 (root, orientation) pairs, or about 15× for 200 independent events. With the per-chain rate here (22 ms per configuration) that is 20–80 minutes on 2 cores, beyond this budget.

What is resolved: ungated, the optimised composite decorrelates in one physical time step like the single four-face mark (R(1) equal within 1σ). Its R(2) is smaller by .00077(29) (z −2.6). Neither is a statement about the gated, near-−I sector, which the frozen-skeleton optimum describes.

## Hypotheses each statement uses and where they are stated
- **Frozen skeleton, conditional Wilson law, colours, exact pair refresh, plug-in variance:** fixed.md and replicas.md. The z1mx4 header inherits P1–P3 and P5 from z1m6 and z1mx3; P8 checks equality with z1mx3.
- **Gauge invariance:** every mark is Re(R·L) with R ∈ {B, 1} and L a closed loop at the root (z1mx4 `mark_loops`, `face_loops`). P6 checks it.
- **Transports along frozen links:** at d0 every skeleton holonomy lies in {±1, ±i}, so a different frozen path changes a mark at most by sign. This is an argument, not a check.
- **The equilibrium form of D:** as in the prior record (two fresh refreshes).
- **Independence of the streams** for the jackknife.
- **The "combined standard error"** of G1 treats the two held-out values as independent, as the brief words it. They are computed on the same held-out data, so I also report the paired error.
- **Tolerances:**
  - Float rounding: 1e-12 in P8 (12-digit printing), 1e-10 in P6.
  - The A4 hot/cold factor 2·(2σ): the prior T2 convention.
  - A5 (r1 .0613(4), r4 .0469(5)) and A6 (L1 against prior .02157(46)): prior values, |z| ≤ 2.
  - The 4 % relative error rule (G2): from the brief.

## Failed predicates (kept)
Counts over all predicate instances (met, failed, measured only): **met 51, failed 8, measured only 33.**
- Met (51): P6, P8, P9 (3); A1 ×2; A3 ×12 (L1–L4 and the two extra lists at both skeletons); A4 ×5 of 6; A5; A6; G1 ×2 of 6; G2 ×8; swap S1 ×8; Q3-P1 to P4 (4, asserted in all 16 chains); T2 ×2, T3, T4 (4); the child rerun identical (1).
- Failed: items 1–6 below, counted as G1 ×4, A4 ×1, child P1 ×1, R1 ×2.
- Measured only (33): 8 Q1 rows, 4 extra-list rows, 6 paired G1 differences, 2 gate fractions, 2 ungated R(t) rows, 2 paired Q2 differences, 1 colour support, 8 swap stability cosines.

1. **G1 at −I, L1→L2** (z −6.4): an outcome (the optimum is still falling there), not a defect.
2. **G1 on clear, all three steps:** an outcome.
3. **A4 f4 hot/cold at G-d0** (z 2.22 against 2): my expectation. The same test failed in the prior X-d0. Chance-level for a 2σ test (1 of 6 A4 tests here).
4. **The child's own P1** (C_train positive definite): failed because of the 4 structural null directions of my L4. A property of my list, not of the target.
5. **R1 at θ 0.6 and θ 1.2** (at least 200 gated pairs at t = 1): FAILED (0 and 52). An outcome: the three-face gate is too rare at this budget.
6. **Process error, mine:** diff_q3.py first ran with exit 1 (K15) because of a missing `__file__` in exec. It was fixed and rerun as K16; nothing was overwritten.

## Not checked
- Rings beyond 2, and trace references on ring-2 plaquettes.
- Nonlinear marks; marks on other time slices.
- A lower bound on the floor: all numbers are Rayleigh quotients, so they are upper bounds only.
- δ ≠ 0; other clear skeletons; other sides or couplings; burn-in beyond the hot/cold split.
- Q2 gated C(t) at any θ (not resolved). Single-face or two-face gates as a substitute were not run: the brief did not define them.
- Q2 ungated marks in non-identity orientations (taken equal in law by symmetry).
- Lean was not used.

## Delegated questions and outcomes
- **Child T224** (admitted under T223 and released; `child_admit.log`, `child_release.log`):
  - Question: an independent generalised eigen-solve and held-out evaluation for L4 from the per-stream matrices (sum X, sum XXᵀ, m, D; `child/data`, a copy of `results/G-d0/mats`).
  - Control: the smallest root of det(diag(2,3) − λ[[2,1],[1,2]]) = (10 − √28)/6 = 0.784750. The child answered 0.784750: **correct**, graded before I read anything else.
  - Outcome: λ_train .015708940952963 and q_held .015427727815759(396), equal to my values to the last digit. It reports cond 359.25 on the range (rank 304). Best single held-out mark: B.yz204.Rv .045581. Top weights: yz204.g01, yz204.L_no11, xy200.g00.
  - I reread its analyze2.py (whitening, truncation at 1e-10, minimum-norm w, the same jackknife definition) and reran it in `childcheck/` (K10): identical results.json.
- **Grandchild T225** (admitted and released by the child under T224):
  - Question: the single-mark held-out quotient of B.xy000.g00, and cond of the first 15×15 block of C_train.
  - Control: the smallest eigenvalue of [[3,1],[1,3]] is 2.000000. Correct.
  - Outcome: .06056377341 and 42.679, equal to the child's own values. The child reran it.


## Exact commands to rerun
These are in `REPLAY.md`. Run everything from /home/user/z4-workers/c2-grow; result paths must not exist beforehand.
```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
cd build && rustc --edition 2021 -O -o z1mx4 src/c2/z1mx4.rs && rustc --edition 2021 -O -o q3 src/c2/q3.rs && cd ..
python3 mkskel.py ; python3 clear.py ; python3 faces.py
build/z1mx4 gauge 4242 6 12 skeletons/d0.txt
python3 ctl4.py
python3 prod4.py G-d0 skeletons/d0.txt 11100001
python3 prod4.py G-clear0 results/gen/chain.skel0.txt 11300001
python3 an4.py G-d0 ; python3 an4.py G-clear0 ; python3 swap4.py G-d0 ; python3 swap4.py G-clear0
mkdir childcheck && cp child/analyze2.py childcheck/ && ln -s ../child/data childcheck/data && (cd childcheck && python3 -I analyze2.py)
python3 run_q3.py main results/G-d0/w_L4.txt 12100001 2000 && python3 an_q3.py main && python3 diff_q3.py
python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Child task graph commands: `pcpos task-admit /home/user/z4-work/graph/attempt.jsonl --by principal --label c2-grow-child --parent T223` (it printed T224), then the child run `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"` (K8), then `pcpos task-release /home/user/z4-work/graph/attempt.jsonl --by principal --id T224`.

**PCP record:** 16 checks, K1–K16. K15 is the expected-0 run that exited 1 (my bug). It was kept and rerun as K16.
- `pcp_os.py verify --ws pcp`, last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`, last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

**Verdict counts:** 9 STANDS, 1 DEFECT, 3 NOT CHECKED.
