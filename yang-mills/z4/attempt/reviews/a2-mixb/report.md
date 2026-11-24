# a2-mixb report (T211) — side 6, period 12

Same model family as the director; this is not independent review. beta = 6.0 and beta = 12.0 are **not matched points**: same side 6 and period 12 at both, no scale setting. Q2 is at the matched point beta = 3.276133577.

## Verdict table
| item | verdict | evidence |
|---|---|---|
| Control: prior row L-d0, J4/Var4 = 0.0469(5), with the prior programs (run.py, build/z1m6, reduce.py), 8 x 576 | STANDS | 0.0456(12), z = -1.0. The prior hot/cold check on J1/Var1 gives z = -2.14, FAILED (kept). |
| Q1: the one-face ratio J1/Var1 stays flat at beta 6 and 12 up to round distance 0.67 (beta 6) / 0.33 (beta 12) | STANDS (resolution 2-4 %, not 2 %) | Relative to d0: beta 6 between 0.966(38) and 0.989(24); beta 12 between 0.910(44) and 0.986(35). No row differs from 1 by more than 2.1 sigma. |
| Q1: the four-face ratio J4/Var4 stays flat (within 2 %) at beta 6 and 12, as it does at the side-6 matched point | DEFECT | It falls below d0: beta 6 0.87(3) at 1/beta, 0.86(2) at 2/beta, 0.85(3) at 0.305. beta 12 0.81(4) at 1/beta, 0.71(3) at 2/beta, 0.80(3) at 4/beta, 0.78(3) at 0.305. These are 4-10 sigma. It then rises above d0 at 1.22: 1.15(3) at beta 6, 1.07(3) at beta 12. |
| Q1: rise of J1/Var1 at round distance 1.22 (side-6 matched point: 1.075(11)) | NOT CHECKED (not resolved) | beta 6: 1.060(33), +1.8 sigma. beta 12: 0.998(38). Errors too large to confirm or exclude. |
| Q1: rows at about the same angle but different k/beta agree (beta 6: 2/beta = 0.333 vs 0.305; beta 12: 4/beta = 0.333 vs 0.305) | STANDS | Four-face relative: 0.856(24) vs 0.845(29); 0.796(29) vs 0.778(32). |
| Q1: beta 12 at fixed distance 0.61048 | NOT CHECKED (no number) | The first run failed hot/cold on J1/Var1 (z = 2.12). The rerun with 4608 burn-in failed on plaquette (z = -2.73) and on spread (z = 2.38). Per the rule, no number is given. |
| Q2: gated marks (theta < 0.3, 0.6, 1.2) have smaller C(1)/C(0) and C(2)/C(0) than the clear mark | STANDS | C(1)/C(0): 0.00029(21), 0.00037(14), 0.00326(8) vs clear 0.01147(7), z = -53, -90, -71. C(2)/C(0): z = -6.7, -7.4, -5.1. |
| Q2: child's independent implementation agrees with mine | STANDS | Ungated C(1)/C(0) 0.0130(11) vs 0.01354(9). Gate 1.2: 0.0021(27) vs 0.00326(8). Clear: 0.0122(13) vs 0.01147(7). Gate-1.2 fraction 0.0402(5) vs 0.04032(1). All \|z\| <= 1.6. |

Predicate counts (met, failed, measured only): **161, 7, 22**.
- Met: 120 Q1 run checks, 32 Q2 sampler asserts, 6 Q2 checks, control C0, control T2 on J4/Var4, P4.
- Failed: 6 Q1 hot/cold checks and 1 control hot/cold check.
- Measured only: 13 Q1 rows, 5 Q2 gate rows, 4 Q2 conditional/indicator rows.

## Question 1 (beta 6 and 12; not matched points)
Setup:
- Program: build/a2m, a copy of the prior worker's z1m6. The beta < 8 guard is removed and a plaquette column is added. Check P4: its output is byte-identical to z1m6 at beta 3.276133577.
- Runs: 8 streams per row (4 cold, 4 hot), 576 measurements 6 sweeps apart. Burn-in 1152 sweeps at beta 6 and 2304 at beta 12.
- Skeletons: same convention as the prior worker. W_delta = (-cos d, 0, 0, sin d) on the y-link at (2,0,0); B = i; all other frozen links = I.
- Fixed distances: the exact matched-point values k/3.276133577 = 0.30524, 0.61048, 1.22095.

Full table: results_q1/table_3.md. It gives J, Var, the one-face and four-face ratios, beta times each ratio, per-stream sd, hot/cold z, mean spread, min angle and pair-proposal cost. Summary (errors: delete-one-stream jackknife; relative errors combined in quadrature):

| beta | delta | min angle | J1/Var1 | J4/Var4 | beta·J1/Var1 | beta·J4/Var4 | r1/r1(d0) | r4/r4(d0) | mean spread | Var4 | J4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | 0 | 0 | .0599(12) | .0464(10) | .360(8) | .278(6) | 1 | 1 | .2226(22) | .0247(6) | .001143(18) |
| 6 | 1/β | .1667 | .0587(12) | .0403(10) | .352(7) | .242(6) | .980(29) | .870(29) | .2189(18) | .0350(12) | .001410(42) |
| 6 | 2/β | .3333 | .0579(19) | .0397(7) | .347(12) | .238(4) | .966(38) | .856(24) | .2146(27) | .0408(10) | .001619(24) |
| 6 | 4/β ¹ | .6667 | .0580(7) | .0456(10) | .348(4) | .274(6) | .968(23) | .983(30) | .2089(15) | .0357(7) | .001626(22) |
| 6 | .30524 | .3052 | .0593(7) | .0392(11) | .356(5) | .235(6) | .989(24) | .845(29) | .2161(16) | .0399(6) | .001564(30) |
| 6 | .61048 | .6105 | .0584(10) | .0428(7) | .350(6) | .257(4) | .973(27) | .922(25) | .2086(15) | .0389(5) | .001662(13) |
| 6 | 1.22095 | 1.2210 | .0635(15) | .0532(8) | .381(9) | .319(5) | 1.060(33) | 1.148(29) | .2015(18) | .0220(3) | .001174(9) |
| 12 | 0 | 0 | .0620(19) | .0483(13) | .744(23) | .579(16) | 1 | 1 | .1458(11) | .00728(33) | .000352(11) |
| 12 | 1/β | .0833 | .0611(10) | .0393(18) | .733(12) | .471(22) | .986(35) | .814(44) | .1467(10) | .0111(6) | .000437(10) |
| 12 | 2/β | .1667 | .0601(19) | .0343(10) | .722(22) | .412(12) | .970(42) | .711(28) | .1428(5) | .0169(4) | .000580(7) |
| 12 | 4/β ¹ | .3333 | .0568(14) | .0384(9) | .682(17) | .461(11) | .917(36) | .796(29) | .1391(6) | .0216(4) | .000830(10) |
| 12 | .30524 ¹ | .3052 | .0564(21) | .0376(12) | .677(25) | .451(14) | .910(44) | .778(32) | .1409(12) | .0213(4) | .000798(10) |
| 12 | .61048 | .6105 | NO NUMBER (hot/cold failed twice) | | | | | | | | |
| 12 | 1.22095 | 1.2210 | .0619(14) | .0515(5) | .743(17) | .618(6) | .998(38) | 1.067(31) | .1165(4) | .0120(1) | .000620(4) |

¹ From the rule rerun with doubled burn-in. The first run failed one hot/cold check.

Measured-only facts:
- The pair-proposal cost of the exact pair draw grows with beta at small displacement: about 4 proposals per draw at beta 6 and 124-179 at beta 12 for d0, 1/beta and 2/beta. It is 3.8 at beta 12, delta 1.22.
- The min angle from -I over all 81 coarse spatial faces equals delta in every row. Example b12-k1: 3 faces at delta, 4 at pi/2 (the faces carrying B = i), 74 at pi.
- Mean plaquette is 0.8704 at beta 6 and 0.9363 at beta 12.

## Question 2 (matched point, unconditioned Wilson measure)
Setup:
- Program: build/q2. One cycle is one heat-bath sweep plus one over-relaxation sweep (G4's primitives).
- 16 independent chains (8 cold, 8 hot), 1000 burn-in cycles, 30000 configurations 1 cycle apart.
- Each configuration gives 324 marks: 27 coarse xy squares (roots with even coordinates) times 12 slices.
- C(t) = <m(c,t0) m(c,t0+t)> - <m>^2, pooled over squares, time origins (periodic), configurations and chains. Errors: delete-one-chain jackknife.
- The gated marks are indicator-weighted, m_g = m1·1[gate], as the brief defines.

Predicates (fixed in run_q2.py before the runs), all met:
- Chains: 16.
- Hot/cold: plaquette z = 0.82, ungated C(1)/C(0) z = 0.83, gate-1.2 fraction z = 0.53.
- tau_int: at most 0.86 configurations, against an allowed 150.
- Burn-in drift: z = -0.30.
- Gauge invariance of all marks: largest deviation about 1e-14 (allowed 1e-10).
- Agreement with the prior worker's test formula at root 0: deviation 0.

Plaquette 0.7500018(40).

| mark | fraction of squares | C(1)/C(0) | C(2)/C(0) | C(3..6)/C(0) |
|---|---|---|---|---|
| ungated m1 | 1 | .01354(9) | .00078(10) | all \|.\| <= .00011, within 1.5 sigma of 0 |
| theta < 0.3 | 1.585(10)e-4 | .00029(21) | .00003(4) | within 1.3 sigma of 0 |
| theta < 0.6 | 1.8954(38)e-3 | .00037(14) | .00005(7) | within 1 sigma of 0 |
| theta < 1.2 | .040325(11) | .00326(8) | .00025(7) | within 0.7 sigma of 0 |
| clear (theta > 1.2) | .959675(11) | .01147(7) | .00070(9) | R4 = -.00009(7), others within 1.3 sigma |

Differences against the clear mark (paired jackknife):
- C(1)/C(0): -0.01118(21) for theta < 0.3 (z = -53); -0.01109(12) for theta < 0.6 (z = -90); -0.00821(12) for theta < 1.2 (z = -71). All significant.
- C(2)/C(0): z = -6.7, -7.4, -5.1. All significant.

Measured only, not asked:
- Indicator autocorrelation at t = 1: 0.00029(11) for theta < 0.3, 0.00178(13) for theta < 0.6, 0.01212(8) for theta < 1.2.
- Correlation of m1 among pairs whose square is in the gate at both times (Rc1):
  - theta < 1.2: 0.0381(18), against 0.0119(1) for clear-clear pairs (z = +14.8).
  - theta < 0.6: 0.017(40).
  - theta < 0.3: rests on about 11 pairs in total and is not usable.
- The indicator-weighted gated C(t)/C(0) is small mainly because a square rarely stays in a near -I gate from one slice to the next (pairs per configuration: 2.3e-5, 2.3e-3, 0.68 for the three gates).

File: results_q2/main/more.txt.

## Hypotheses each statement uses and where they are stated
- **Q1 (J, Var, ratios):**
  - Definitions of the frozen skeleton, colours, pair law, tests f1 and f4, J, and the plug-in variance: g4/full-complement/fixed.md, PRIOR_NOTES.md Step 0, header of build/src/mine/z1m6.rs.
  - Displacement convention: g4/sparse-coarse-fields/disk.md, mkskel.py and mkskel_q1.py docstrings. I did not reread disk.md; the convention is inherited from the prior worker.
  - Independence of the streams, which the jackknife needs: distinct seeds, run_q1.py.
  - Thermalisation: checks T2, T2p and T2s in the run_q1.py docstring.
  - The exactness of the pair rejection draw at any beta: argument in the a2m.rs header. Assert P3 checks that the acceptance exponent is at most 0.
- **Q2:**
  - Mark definitions: the brief and the header of build/src/a2/q2.rs.
  - A valid Wilson-measure chain (sequential heat bath plus over-relaxation): G4's wilson_mc.rs, validated by the prior worker's exact single-link test.
  - Independent chains for the jackknife.
  - Predicates T1-T4: run_q2.py docstring.
- **Control:** the prior table SIDE6_TABLES.md row L-d0.

## Failed predicates (all kept)
1. **Control, prior T2 on J1/Var1:** z = -2.14 (threshold 2). Attributed to chance under my expectation of a 2-sigma check. The same base seed at 24 x 1152 passed in the prior record. Not a defect of the target.
2. **Q1 b6-k4, T2s (spread hot/cold):** z = 3.16. The rerun with 2304 burn-in passed every check.
3. **Q1 b12-k4, T2 on J1/Var1:** z = -2.13. The rerun with 4608 burn-in passed.
4. **Q1 b12-fix-k1, T2p (plaquette hot/cold):** z = 2.44. The rerun passed.
5. **Q1 b12-fix-k2, T2 on J1/Var1:** z = 2.12. The rerun failed T2p (z = -2.73) and T2s (z = 2.38). No number is given. I do not attribute this to chance: it is either slower thermalisation at beta 12 or a long tail; unresolved.

About 18 runs x 4 checks at 2 sigma give about 3.6 failures by chance; 6 were seen.

Process errors (my own, not predicates):
- (a) I reduced q1-b6-fix-k4 while its streams were still running. That results_q1/q1-b6-fix-k4/summary.json is from partial data and invalid; it is kept. summary_full.json is the valid one.
- (b) reduce_q2.py's first run (pcp reduce-q2-main) exited 1 because the glob c*.txt matched commands.txt. I fixed the glob and reran it as reduce-q2-main-2.

## What I did not check
- Whether beta 6 and 12 sit inside a scaling window; they are not matched points.
- 24-stream statistics at beta 6 and 12. At 8 streams the ratios carry 2-4 % errors, so "flat within 2 %" cannot be resolved for J1/Var1.
- Longer burn-in than 4608 for beta 12 at 0.61048.
- The traceless-B variant in Q1. The columns exist, but I did not tabulate them.
- Per-colour shares in Q1.
- A re-derivation of fixed.md or disk.md.
- In Q2: coarse squares in other planes and other root parities; finite-size effects; a check of the over-relaxation sweep beyond hot/cold agreement.
- The conditional correlation at theta < 0.3 (too few pairs).
- A Lean result: Lean was not used.

## Delegated questions
- **Child, T212** (admitted under T211, released): an independent implementation of the gated time correlation at reduced statistics.
  - Control: the Haar probability P(arccos(-a0) < 1.2) = (2.4 - sin 2.4)/(2 pi) = 0.274469. I graded it **CORRECT** before reading anything else.
  - Child's code: Python/numpy, Kennedy-Pendleton heat bath with a site-parity x direction checkerboard (I reread it; valid). Marks: I reread loop2, the transport path and plaquette orientation; they match the definition. 6 hot-start chains, 900 configurations, 10 sweeps apart.
  - Child's numbers agree with mine within 1.6 sigma (verdict table). Its gate-0.6 C(1) error of ±0.0000 is not trustworthy, as the child itself says.
  - Child's own failure: its P4 (its own expectation that theta = 0 at a cold start, but theta = pi there) failed and was corrected.
  - I reran its analysis from its raw output: byte-identical (pcp child-analyze-rerun, K20).
  - I reran its full production (run.py prod_parent_rerun.json, 135 s, K37) and analysis (K38): analysis_parent_rerun2.txt is byte-identical to its analysis_v1.txt.
- **Grandchild, T213** (admitted by the child under T212, released by the child): known answer P(theta < pi/2) = 0.5; independent quadrature 0.27446856; single-link KP <a0> = 0.596413(313) against exact 0.5965322. The child reran it and got identical output. I did not rerun the grandchild myself.

## Commands to rerun
See REPLAY.md: build, control, Q1 (q1_all.sh, after_q1.sh, rerun_b12.sh, reduce_q1.py, table_q1.py), Q2 (run_q2.py main 9100001, reduce_q2.py main, reduce_q2_more.py main), and the child rerun. All runs went through `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp ...`.

## PCP OS
Register pcp/register.jsonl, checks K1-K38. The run checks all exited as expected, except reduce-q2-main (exit 1, my glob defect, listed above).
- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.` (register SHA-256 a4ad61a1beedb97773e82e0c30b791acb0d09a1e62f700a74bda13900e1e7b5f)
