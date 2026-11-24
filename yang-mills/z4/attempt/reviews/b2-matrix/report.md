# b2-matrix report (T217): the full mark list on the frozen skeleton, side 6

The director and I are the same model family, so my agreement with the director is not independent review. The child (T221, Sonnet) checked the δ = 0 eigen-solve with its own code. Raw data are in `results/<tag>/`, the record in `notes.md` and the rerun commands in `REPLAY.md`. Lean was not used (`/home/user/z4-lean/READY` exists, but no Lean claim is made).

Setting: side 6, time period 12, β = 3.276133577, and the frozen skeleton of fixed.md. The δ = 0 and δ = 1/β skeletons come from `mkskel.py`. The clear skeleton is `chain.skel0` from the prior record, regenerated exactly. The design is 32 streams × 1152 measurements, seed = base + 7919 i and hot = i % 2. The training half is streams 0–15 and the held-out half is streams 16–31; each half has 8 hot and 8 cold streams. Each stream discards 576 conditional sweeps and takes measurements 6 sweeps apart.

Estimators:
- **C:** the pooled plug-in covariance (ddof 0) over all measurements of a stream set. It is centred by that set's pooled mean, which is G4's convention, and re-centred in every jackknife deletion.
- **D:** the mean over the 24 colours of E[(X′−X″)(X′−X″)ᵀ]/2. X′ and X″ are the two independent exact conditional pair refreshes of the colour that the existing program already draws for f1 and f4. This equals (1/48) Σ_j E[(X−X′_j)(X−X′_j)ᵀ] at equilibrium.
- **Generalised eigenproblem:** solved on the training half by C-whitening. Directions with C-eigenvalue below 1e-10·max are truncated; only the exactly degenerate runs needed this.
- **Reported number:** the quotient on the held-out half, with a delete-one-stream jackknife over the 16 held-out streams.

## Verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| (0) Control: the single-mark values at δ = 0 (8 × 576) with the existing programs | STANDS | `run.py` and `reduce.py` with seeds 3100001 give r1 .0623(23) and r4 .0486(12), equal to every printed digit of the prior d0 row. |
| Extended sampler `z1mx` is a pure addition to `z1m6` | STANDS | P7: `.csv` and `.colours.csv` are byte-identical to z1m6. P5: B.g00 = f1 and the mean of g = f4 to 1e-12 at every measurement. P6: a random gauge transform changes the marks by ≤ 1.2e-15. |
| (ii) j/k-type references at W = −I | STANDS (excluded) | The global exp(iπ/8) leaves every frozen link fixed (change 0) but moves Re(j g1) from −.536 to −.210. So these marks are not functions of the gauge orbit at δ = 0. At δ ≠ 0 the references Wt = unit Im W and Ct = unit Im(Bt·Wt) are traces of closed loops and are invariant. |
| Auditor: single marks do not exclude a collective slow mode | STANDS | At δ = 0, the brief's 14-mark list gives a held-out optimum of .02675(69), against .04808(81) for the best single mark: ratio .556(8). f1 is .0617 and f4 is .0464. |
| The four-face mark f4 = Re(B ḡ) as the most discriminating slice test at −I | DEFECT | It is beaten on held-out data by 1.74× (14 marks) and 2.20× (35 marks, .02138(45)). The plaquette span alone gives .03926(59) with weights (.85, 1, .76, −.02), not the equal weights of f4. |
| The mode is local to the marked square | DEFECT | The weight sits on the faces through the twisted W edge. The marked square alone gives .0328; adding the xy face (2,0,0) gives .0265–.0274; adding the yz face (2,0,4) gives .0255; all three faces give .02157(46). The other five adjacent xy squares add nothing resolvable (X2). |
| −I against clear contrast survives optimisation | STANDS | With the same 15-mark set: δ = 0 gives .02157(46) and the clear skeleton .05983(53), 2.8× apart. Full lists: .02138(45) against .05710(64). |
| The dip at δ = 1/β changes the optimum | measured only (STANDS as "no large change") | With the same 15 marks, d1/d0 = .959(23). With the same 11 marks (M-runs), .993(28). The disk's single-mark prediction is 1.039; the two are not the same quantity. |
| Independent check of the eigen-solve and the held-out evaluation (child, grandchild) | STANDS | The child (Cholesky on the 11 independent marks) gets λ .02691319, q .02674971(69346), best single B.Rh .04807613 and cond 43.44. All equal mine, and its program reran byte-identically. |
| Disk transfer (factor ≈ 4.5, weights (1, 1.77, 1)) | NOT CHECKED (no analogue established) | In 4D the gain over the best single mark is 1.8× (brief's list) to 2.3× (35–43 marks). β·q_opt is .070 at −I, against .262 on the disk. There is no 3-mark analogue with those weights. |
| A lower bound on the all-test floor | NOT CHECKED | All numbers are Rayleigh quotients, so they are upper bounds only. The optimum still falls as marks are added (.0328 → .0265 → .0216 → .0214), with no sign of convergence. |

## Results per background (held-out quotients; β·q in brackets)

| background | min angle from −I (all 81 coarse faces) | marks | cond C_train | held-out optimum | best single mark (held) | opt / best single | f1 | f4 | colours carrying w^T D w |
|---|---|---|---|---|---|---|---|---|---|
| δ = 0 (M-d0) | 0 (faces xy(0,0,0), xy(2,0,0), yz(2,0,4)) | 14 (11 independent) | 2.6e17 → 43.4 after dropping 3 exact duplicates | **.02675(69)** [.0876] | B.Rh .04808(81) | .556(8) | .06173(86) | .04642(67) | 0,1,2,3: .26/.27/.22/.25 |
| δ = 1/β = .3052 (M-d1) | .305238 (same three faces) | 22 (19 independent) | 9.5e16 → (19-mark set 60) | **.02532(28)** [.0830] | Ct.g10 .04562(70) | .555(12) | .06093(56) | .04620(78) | 0–3: .27/.27/.22/.24 |
| clear chain.skel0 (M-clear0) | 1.142692 | 22 | 49.4 | **.05663(55)** [.1855] | Ct.g01 .06732(57) | .841(10) | .07738(106) | .08637(123) | 0–3: .30/.23/.24/.23 |
| δ = 0, extra list (Y-d0) | 0 | 35 | 48.1 | **.02138(45)** [.0700] | B.Rh .04843(81) | .441(8) | .06072(69) | .04699(61) | 0–3 .18/.18/.15/.16; yz 16/18/20/22 .10/.05/.11/.08 |
| δ = 1/β, extra list (Y-d1) | .305238 | 43 | 63 | **.01984(19)** [.0650] | Ct.g10 .04517(39) | .439(4) | .06035(77) | .04417(47) | 0–3 .18/.18/.15/.16; yz 16/18/20/22 .09/.04/.11/.08 |
| clear, extra list (Y-clear0) | 1.142692 | 43 | 28.9 | **.05710(64)** [.1871] | Ct.g01 .06876(63) | .830(11) | .07707(113) | .08842(90) | 0–3 .21/.18/.20/.19; yz .06/.02/.08/.07 |

Weights (training half, largest |w| = 1):
- **M-d0, 11 independent marks:** neighbour xy(2,0,0) plaquettes +1, +.66, +.92, +.12. Marked g00..g11 −.57, −.81, −.55, +.05; Rv −.52, Rh −.63, L_no11 −.81.
- **Y-d0, the 15 marks on the three −I faces:**
  - marked square: g −.42, −.63, −.40, +.04; Rv −.36, Rh −.43, L_no11 −.59;
  - xy(2,0,0): +.78, +.49, +.70, +.11;
  - yz(2,0,4): +.69, +.65, +1, +.12.

This is a relative colour-axis mode of the three coarse faces at −I that share the twisted y edge. The plaquette touching the far corner (g11 type) is always about 0. Swapping the halves (training on the held-out half) gives cos angle .9997 (M-d0) and .9986 (Y-d1) in the C metric. On the clear skeleton it is .816 (M) and .952 (Y): the direction there is less sharply defined. The other 20 colours carry exactly zero, because they do not touch the marks' links.

The held-out evaluation never fell below training: A3 z ranges from −.61 to +2.33. All C matrices used without truncation have cond ≤ 63.

## Hypotheses and where they are stated
- **Frozen skeleton, conditional Wilson law, colours, exact pair refresh, plug-in variance:** fixed.md and replicas.md. The prior record's z1m6.rs is reused unchanged, and z1mx.rs only adds outputs (P7).
- **Gauge invariance:** every mark is Re(R·L), with R and L closed loops based at the root (header and `mark_loops` in build/src/mine/z1mx.rs). Checked by P6 and by the residual stabiliser test above.
- **Disk analogue for (iii):**
  - The marks are the two half squares Rv and Rh (2 plaquettes, the analogue of q2) and four L-shapes (3 plaquettes, the analogue of q3). q1 is g1.
  - Each is a closed loop whose interior part is a product of consecutive free links between frozen boundary sites.
  - At W = −I, three of the L-shapes equal plaquette marks identically: Re(B·(−conj g)) = Re(B g) for pure imaginary B. At δ ≠ 0 they are fixed combinations of B.g and Ct.g. So they add only L_no11.
- **(iv) neighbour square:** xy face based at (2,0,0), the face that shares the W edge (z1mx). In the extra runs I added all six adjacent xy squares (z1mx2) and then the yz face (2,0,4) (z1mx3).
- **Stationarity:** D from two fresh refreshes equals the brief's D with X itself, assuming the chain is at equilibrium. Checked only by the hot/cold predicate A4.
- **Held-out split and jackknife:** treats streams as independent; stated in the analyze.py docstring.
- **Tolerances:** float rounding for P5, P6 and A1. The hot/cold predicate A4 (2σ_d with σ_d = 2× the jackknife error) is the prior record's T2 convention. The A5 band of 2σ uses the prior record's 24 × 1152 values and errors.

## Failed predicates (all kept)
Counts over all predicate instances: **51 met, 5 failed, plus the tabulated values measured only.**
1. **X-d0, A4 for f4:** hot/cold z = 2.23 against the bound 2. My expectation. In total 2 of 18 two-sigma hot/cold tests (6 runs × 3) failed (this one and item 2), about what chance gives. Not shown to be a burn-in defect.
2. **Y-d1, A4 for f1:** hot/cold z = 2.08. Same attribution as item 1.
3. **X2 (my expectation):** the five other adjacent xy squares add nothing resolvable: .00033(87).
4. **Y1 at Y-clear0** (z = 39): my own predicate defect. It compares with the δ = 0 value and was not restricted to δ = 0 runs, so it is meaningless at the clear skeleton.
5. **Child's own predicate** (C_train positive definite): failed because of the exact duplicate marks. The child calls this a "target defect". Correction: it is a property of my mark list, not of fixed.md.

Rule 4: no predicate here is a "for all" over cases beyond the per-run lists. The one per-case check was the child's P7 (λ_min no larger than every single training quotient), and all 11 cases qualified. The clear-skeleton rule qualified 40 of 60, 57 of 60 and 59 of 60 skeletons at θ = π/4, π/8 and π/16 (`clear.py`, identical to the prior record).

## Not checked
- Any lower bound on the all-test floor.
- Marks beyond 35–43 (further faces, deeper loops, nonlinear marks).
- Other sides or couplings.
- δ = 0.5/β, 2/β, and other clear skeletons.
- Burn-in dependence beyond the hot/cold split.
- The disk's (1, 1.77, 1) structure.
- Lean.
- Whether the optimum converges as marks are added; it was still decreasing.

## Delegated questions and outcomes
- **Child T221** (admitted under T217, released): an independent generalised eigen-solve and held-out evaluation from my raw M-d0 files (`child/data`: `s*.X.csv` and `s*.Dc.txt` only).
  - Control: det(diag(1,4) − λ[[1,.5],[.5,1]]) = 0, smallest root 0.929632. The child answered 0.929632, graded **correct** before I read anything else of its output.
  - Outcome: agreement to all digits (see the verdict table). I reran its `an3.py` in `childcheck/`: byte-identical output.
- **Grandchild T222** (parent T221, admitted and released by the child): the single quotient of B.g00 on the held-out half, and cond C_train.
  - Control: diag(2,5) against I gives 2.000000, correct.
  - Returned .06172628688 and 2.58e17, equal to mine (.061726286884).

## Exact commands to rerun
These are in `REPLAY.md`. All are run from `/home/user/z4-workers/b2-matrix`, and every results directory must not already exist.

```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"                     # control.txt 0.272341
cd build && rustc --edition 2021 -O -o z1mx src/mine/z1mx.rs && rustc --edition 2021 -O -o z1mx2 src/mine/z1mx2.rs && rustc --edition 2021 -O -o z1mx3 src/mine/z1mx3.rs && cd ..
python3 mkskel.py
python3 run.py d0 skeletons/d0.txt 3100001 && python3 reduce.py d0
build/z1mx gauge 4242 6 12 skeletons/d0.txt ; build/z1mx gauge 4242 6 12 skeletons/d1.txt
mkdir -p results/p7 && build/z1m6 fixed 3.276133577 3100001 0 576 64 6 6 12 skeletons/d0.txt results/p7/old && build/z1mx fixed 3.276133577 3100001 0 576 64 6 6 12 skeletons/d0.txt results/p7/new && cmp results/p7/old.csv results/p7/new.csv && cmp results/p7/old.colours.csv results/p7/new.colours.csv
python3 prod.py M-d0 skeletons/d0.txt 8100001 && python3 analyze.py M-d0 && python3 supp.py M-d0
python3 prod.py M-d1 skeletons/d1.txt 8300001 && python3 analyze.py M-d1 && python3 supp.py M-d1
python3 clear.py
python3 prod.py M-clear0 results/gen/chain.skel0.txt 8500001 && python3 analyze.py M-clear0 && python3 supp.py M-clear0
build/z1mx2 gauge 4242 6 12 skeletons/d0.txt ; build/z1mx3 gauge 4242 6 12 skeletons/d0.txt
python3 prod2.py X-d0 skeletons/d0.txt 8700001 && python3 analyze.py X-d0 && python3 supp2.py X-d0
python3 prod3.py Y-d0 skeletons/d0.txt 8900001 && python3 analyze.py Y-d0 && python3 supp3.py Y-d0
python3 prod3.py Y-d1 skeletons/d1.txt 9100001 && python3 analyze.py Y-d1 && python3 supp3.py Y-d1
python3 prod3.py Y-clear0 results/gen/chain.skel0.txt 9300001 && python3 analyze.py Y-clear0 && python3 supp3.py Y-clear0
mkdir childcheck && cp child/an.py child/an3.py childcheck/ && ln -s ../child/data childcheck/data && (cd childcheck && python3 -I an3.py)
python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

The diffs are `z1mx.diff` (the minimal extension, 125 lines), `z1mx2.diff` and `z1mx3.diff`.

PCP record: 32 events (K1–K30 checks, among them child-run1 = K9 and the child rerun = K14).
- `pcp_os.py verify --ws pcp`, last line: "The guards are those of pcpos 1.0.22. A register is read under the rules of the program that reads it: an event an earlier build accepted may be reported here, and its bytes are unchanged." The line before it is "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)".
- `pcpos verify pcp/register.jsonl`, last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right." It also reports "chain intact: 32 events".
