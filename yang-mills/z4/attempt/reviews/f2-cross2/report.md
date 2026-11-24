# f2-cross2 report: worker under T239 (Director Z4), 2026-11-24

**Matched pair.** Side 5 at β = 3.196581051 and side 10 at β = 3.493705679, SU(2) Wilson, heat bath only. The sampler is g4/wilson_mc.rs, included verbatim.
**Lag.** l/5, which is 1 coarse step on side 5 and 2 fine steps on side 10.
**Observables.** Every observable is a fixed function of the common coarse links on the 5³ coarse slice, computed by the same code on both lattices (src/cross2.rs).
**Ensembles.**
- 2l: c2 (N=5, T=10) and f2 (N=10, T=20), each 16 chains × 2000 measurements.
- 4l: c4 (N=5, T=20) with 16 × 2000 measurements, and f4b (N=10, T=40) with 16 × 1000.
- Every ensemble used 3 heat-bath sweeps between measurements and a 500-sweep burn-in.

## Verdict table
| # | Item | Verdict | One line of evidence |
|---|---|---|---|
| 1 | Control −ln tanh 1 | STANDS | control.txt = 0.272341 |
| 2 | What G4's four-bin endpoints are | STANDS: they are 1 − R_min, not slice-averaged R | λ2 of the pooled one-line 4-bin joint matrix equals 1 − min R over centred 4-bin functions of **one line** in the direction-pooled local law. On all 4 ensembles the two agree to ≤ 2.4e-16 (Q1). The prior worker's Wa1 is the **slice average** over 25 lines, whose R includes cross-line correlations. On c2 the 4-bin local quantity is 1 − R = 0.0621, while the slice-averaged Wsum has 1 − R = 0.316. These are different statistics. |
| 3 | G4's numbers on my ensembles | DEFECT (side-10 2l value not reproduced; side-5 values and side-10 4l value stand) | λ2: c2 .06215(28) vs G4 .06197(257); c4 .06132(22) vs G4 4l .06157(68); f4b .00145(13) vs G4 4l .00169(47). But f2 .00158(14) vs G4 2l .00408(72) is 3.4 combined SE apart. My 2l and 4l side-10 values agree with each other, so I see no period shift on side 10. G4's 2l side-10 run was 4 streams × 128 measurements after 256 sweeps. |
| 4 | The quotient comparison R_fine(f) ≥ α R_coarse(f) for frozen eligible tests (predicate D) | DEFECT for every α > 0.951 | One frozen test, Z:ratio-opt, was trained on 2l TRAIN chains. On 2l held-out chains it gives R_f/R_c = 0.9409 ± 0.0049 (bound 0.9507). On the fully independent 4l ensembles it gives 0.9357 ± 0.0027 (bound 0.9412). Var_f/Var_c = 1.18 and E_f/E_c = 1.11. Retraining at 4l finds the same kind of test: 0.9378 ± 0.0039. |
| 5 | Slowest inherited mode on side 10 at lag l/5 (predicate S) | STANDS: resolved, in every class | Held-out 1 − R_f of the fine-optimal test at 2l: local 0.0115 ± 0.0006; zero momentum 0.122 ± 0.008; lowest momentum along x/y/z 0.0087 ± 0.0021, 0.0100 ± 0.0014, 0.0122 ± 0.0016. At 4l: 0.0122(4), 0.116(7), 0.0085(14), 0.0119(15), 0.0098(14). |
| 6 | Prior claim "every R_fine in [0.976, 1.003]" | DEFECT of the span, not of their numbers | The claim holds for their 16 slice-averaged functions; my like-for-like Z:Wsum gives R_f = 0.983(3) against their 0.989(5). In the 54-function span, Z:fine-opt has R_f = 0.878(8). Its leading coefficients are on products of half-trace windings of neighbouring parallel lines (hh), which were absent from the prior span. |
| 7 | Prior "no frozen test has R_f/R_c below one" | DEFECT (span too small) | See item 4. The defeating test is dominated by the slice average of the **local** product w_μ(s)·p_μ(s) and by w_μ. The prior worker had only the product of slice averages. |
| 8 | Gauge and center invariance of every observable (Q0) | STANDS | Random Haar gauge transformation: max change 4.0e-15 (N=10) and 3.8e-15 (N=5). Center flips in μ = 0..3: change exactly 0. The sensitivity controls (a raw link component; the x-winding under the μ=0 flip) change by 0.14 to 1.7, so the test is not blind. All Z/P classes and indicators are fixed functions of these 54 fields. |
| 9 | Momentum-projected (lowest nonzero momentum) tests | STANDS: no defeat | The best momentum-class bounds are 1.002 to 1.009 at both circumferences. Fine-optimal momentum modes have 1 − R_f ≈ 0.01 against coarse 1 − R_c ≈ 0.11. |
| 10 | Period dependence | STANDS: none seen | Null c2 vs c4: min bound 1.0004. Null f2 vs f4b: min bound 1.0003. No test differs between periods on either lattice. |
| 11 | Spectral deficit inequality b_f ≥ α d_c | NOT CHECKED | It needs a certified lower bound on the full coarse deficit. Item 4 defeats only the constant-α quotient comparison for these tests. |

**Verdict counts: STANDS 6, DEFECT 4, NOT CHECKED 1. Predicate counts: met 37, failed 2, measured only 10.**

What item 4 does and does not mean. It is a finite-periodic, finite-statistics measurement for one matched pair. It says that a fixed coarse-measurable test keeps **more** correlation at lag l/5 on side 10 than on side 5: 1 − R_f ≈ 0.068 against 1 − R_c ≈ 0.005 to 0.010. So R_fine ≥ α R_coarse fails for this test whenever α > 0.951. The result is not a vacuum statement, not a full-orbit statement, and not a spectral bound. It inherits the coupling-match uncertainty. The size of the effect (6%) is small but significant: 12σ on the 2l held-out chains and 24σ on the 4l set. It also survives:
- re-evaluation under the two cyclic axis rotations of the frozen vector (held-out 0.932(4) and 0.932(4); on 4l 0.941(3) and 0.948(3));
- independent retraining at 4l;
- the coarse null, where the same selection procedure on two coarse ensembles gives no spurious defeat (bound 1.0004).

## Main numbers
2l values are held-out chains (i%4 ∈ {2,3}, 8 + 8). 4l values come from the 2l-frozen vector evaluated on all 16 + 16 chains of c4/f4b. Errors are delete-one-chain jackknife.

| Frozen test (2l TRAIN) | 2l R_f | 2l R_c | 2l R_f/R_c | 2l Var_f/Var_c | 4l R_f/R_c | 4l Var_f/Var_c |
|---|---|---|---|---|---|---|
| Z:ratio-opt | 0.9318(40) | 0.9903(30) | **0.9409(49)** | 1.185 | **0.9357(27)** | 1.182 |
| Z:fine-opt | 0.8780(76) | 0.4707(87) | 1.865(38) | 0.260 | 1.820(22) | 0.270 |
| Z:coarse-opt | 0.8938(53) | 0.4666(88) | 1.916(38) | 0.356 | 1.961(22) | 0.347 |
| Z:Wsum (slice-avg w) | 0.9827(30) | 0.6835(44) | 1.438(10) | 0.539 | 1.434(12) | 0.545 |
| L:fine-opt (local) | 0.98848(64) | 0.8478(23) | 1.166(3) | 0.615 | 1.160(2) | 0.623 |
| L:ratio-opt | 0.99879(30) | 0.99967(57) | 0.99912(65) | 3.80 | 0.99876(25) | 3.82 |
| L:Wsum (per-line w) | 0.99845(22) | 0.93897(39) | 1.0634(5) | 0.894 | 1.0628(6) | 0.900 |
| P0/P1/P2 ratio-opt | ≈ 0.998 to 1.002 | ≈ 0.997 to 0.999 | 1.002(2), 0.999(2), 1.004(2) | 2.9, 1.3, 3.3 | 1.000(1), 1.003(1), 1.001(1) | 2.9, 1.3, 3.3 |

Full tables, including E_f/E_c for all 25 tests, are in:
- results/analysis-2l.txt
- results/analysis-4l.txt
- results/cross-eval-2l-frozen-on-4l.txt

The leading standardised coefficients of Z:ratio-opt are: w1p1 −1.00, w1 +0.76, w2p2 +0.27, hh12 +0.23, hh10 +0.21.

## Hypotheses each statement uses, and where they are stated
- **Matched couplings** (g²_SF(l) = 2.38). Taken from g4/cyclic-transfer/measurements.md; the calibration is in g4/physical-refinement. Not rechecked here. Every R-ratio statement depends on it.
- **Sampler.** g4/wilson_mc.rs, included verbatim in src/cross2.rs. G4's winding.rs includes ../../g4/full-attempt/two-site-gap/wilson_mc.rs, which is not in this tree. I assume the two files are identical.
- **Stationarity.** P1 and P2 (src/predicates.txt). Chains are independent through distinct SplitMix seeds BASE + 7919 i.
- **Eligibility.** g4/G4_FINAL_AUDIT_2026-11-23.md, table row 1: fixed functions of the common coarse links. The coarse links are U(x,μ)U(x+μ,μ) at even x on N=10 and the links themselves on N=5. Q0 checks gauge and center invariance numerically. It does not check eligibility beyond coarse-link measurability, which holds by construction (src/cross2.rs, `coarse_slice`).
- **Finite periodic T is not the vacuum** (g4/cyclic-transfer/vacuum.md). All numbers here are finite-T statements, at T = 2l and 4l.
- **Translation and momentum classes.** The L class is the translation-averaged same-position correlator. The Pk class pools the cos and sin projections, which is the translation average of the law of the cos-projected function. Means are not subtracted in Pk because they vanish by translation invariance (src/analysis2.py `mats`).
- **Jackknife over 8 held-out chains per lattice.** The two lattices are independent, so their relative errors are combined in quadrature.

## Failed predicates
1. **My expectation for D, "no frozen test defeats α = 1": FAILED.** This was my own expectation, not a defect of the target. Z:ratio-opt defeats every α > 0.951 at both circumferences.
2. **My expectation for S, "resolved in the local class, unresolved or tiny at zero momentum": FAILED for Z.** This was my own expectation. The zero-momentum fine-optimal test has 1 − R_f = 0.12.

Also kept on record:
- **Killed run.** The first f4 run (16 × 2000, base seed 6401307) was killed by my session's 600 s background limit after 2 complete chains. This was my process-management error. results/f4 is partial and unused. The rerun f4b used 1000 measurements per chain and new seeds 6501307.
- **Child's failed P6.** The child reported that 1 − λ2 ≠ its "min R". This is a defect of **my prompt**: I specified the direction-SUM function Σ_μ c·ind(w_μ(s)), which is not G4's one-line pooled law. src/check_dirsum.py reproduces the child's 0.943850 and gives the pooled 0.938135 = 1 − λ2.
- **Side-10 2l value against G4 (measured only).** Mine is .00158(14) against G4's .00408(72), a 3.4 SE difference. I cannot say which preparation is wrong. Possible causes on G4's side are its 256-sweep burn-in and only 4 streams. On my side, I found no defect; P1 and P2 are met.

The 37 met are:
- Q0: 14 (7 per lattice).
- P1: 8 (2 conditions × 4 ensembles).
- P2: 8.
- Q1 identity: 4.
- Child control graded correct: 1.
- check-dirsum: 1.
- Child rerun output identical: 1.

The 10 measured only are:
- the 4 comparisons with G4's numbers;
- the 2l and 4l main tables;
- the cross-evaluation;
- the 2 period nulls;
- the rotation checks.

## What I did not check
- The coupling calibration, and the identity of g4/wilson_mc.rs with the file winding.rs includes.
- Any spectral, full-orbit or vacuum bound. I did not check the spectral deficit inequality.
- Chair loops beyond the 6 all-positive orientations. Odd-sublattice skeletons. Momenta other than the lowest one along one axis per class. Momentum classes with rotated labels.
- Side-10 4l at 2000 measurements; I ran 1000.
- The physical origin of the Z:ratio-opt effect.
- Whether a different coupling match within its error would move R_f/R_c above 0.95.
- I did not rerun the grandchild's script myself; the child did.
- Lean: READY exists, but I did not use it.
- **Core use.** The child session and the 4–5 s analysis runs overlapped with the 2-process ensemble runs, so for short periods more than 2 cores were in use.

## Delegated questions and outcomes
- **Child T242.** Admitted under T239 (child_admit.log) and released (child_release.log).
  - Question: an independent reduction of my per-chain moment matrices (c2 held-out chains, copied to child/data). It was to compute R of Wsum and Psum in classes L and Z with jackknife, G4's λ2, and a 4-bin min R as specified (wrongly) in my prompt.
  - Control: R for x = 1..5, lag 2, which is 1.5. It answered 1.500000. I graded this correct before reading anything else.
  - Result: R_L(W) .938965(394), R_L(P) .974134(129), R_Z(W) .683533(440), R_Z(P) .955176(202), λ2 .0618653(354). These agree with my analysis2 to all printed digits. Its failed P6 is explained above as my defect.
  - I reread child/analyze.py and reran it under PCP (child-rerun, scratch/childrerun). results.json is identical.
  - It uses the same specified formulas, so it checks my implementation, not the method.
- **Grandchild T243.** Admitted under T242 and released (seen in /home/user/z4-work/graph/attempt.jsonl, events 483 and 484).
  - Question: recompute the pooled λ2 and its jackknife SE by characteristic-polynomial roots and by deflated power iteration.
  - Control: 1.5, answered correctly.
  - Result: λ2 = 0.0618652849 by all three methods (differences ≤ 8e-17); SE 0.000354333. The child reran it; I did not.
- The child and grandchild are the same model family as me, lower tier. Their agreement is not independent review.

## Exact commands
REPLAY.md lists every command with all arguments and seeds. Seed bases: c2 6101307, f2 6301307, c4 6201307, f4b 6501307 (killed f4: 6401307). Chain i uses BASE + 7919 i. Self-tests used seeds 77 and 78. The ratio search uses numpy seed 239.

## PCP verification (last lines)
- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
