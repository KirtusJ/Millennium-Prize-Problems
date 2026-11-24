# a2-mixb notes (T211)
## Step 0
control.txt = 0.272341 (-ln tanh 1). Register pcp initialised (method not found, expected).
## Child
Admitted T212 (parent T211). Question: independent implementation of the gated time correlation (Q2) at reduced statistics (gates none, 1.2, clear, 0.6 optional; C(1)/C(0), C(2)/C(0), fractions). Control: Haar P(arccos(-a0) < 1.2) = (2.4 - sin 2.4)/(2 pi) = 0.274474. Launched 00:17 via pcp check child-run1 (background, log child_check.log).
## Control (pcp K2, K4): prior row L-d0 reproduced with the existing programs (run.py, build/z1m6, reduce.py), 8 x 576, base 6100001
J4/Var4 = 0.0456(12) vs prior 0.0469(5): z = -1.0 (sigma = sqrt(12^2+5^2)e-4) -> C0 MET (|z|<=2).
J1/Var1 0.0596(10) (prior L-d0 .0613(4): z=-1.6), var4 .0638(21), J4 .002912(51), spread .3424(34).
Prior T2 (hot/cold) on this control: ratio4 z=-1.84 MET, ratio1 z=-2.14 FAILED (threshold 2). Attribution: expected chance level of a 2-sigma check (prior L-d0 with same base seed, 24x1152, passed); not a defect of the target; not rerun.
## Q1 setup
- build/a2m = copy of z1m6 with beta<8 guard removed and a plaquette column. P4 (pcp K5): first 10 columns and colours file byte-identical to z1m6 (2 streams). 
- Pair-draw cost grows steeply with beta at the W=-I skeleton: mean proposals per draw 3 (3.28), 3.7 (6), 8.3 (8), 78 (10), 100-195 (12). Exact rejection sampling regardless; cost only. Hot and cold short tests at beta 12 give plaq .9362, .9363 (perturbative 1-3/(4beta) = .9375).
- Skeletons (mkskel_q1.py, K3): d0; b6-k{1,2,4} = k/6; b12-k{1,2,4} = k/12; fix-k{1,2,4} = k/3.276133577 = .30524, .61048, 1.22095 (exact matched-point values, not the rounded .305/.61/1.22).
- Design: run_q1.py docstring (predicates T1, T2, T2p, T2s, T5 and rerun rule fixed before the runs). Burn 1152 (beta 6), 2304 (beta 12). Seeds 7000001+100000k, k = order in q1_all.sh. Launched 00:24.
## Child control graded at 00:30 before reading anything else: child/control.txt = 0.274469, exact 0.2744686 -> CORRECT.
## Q1 beta 6 partial (pcp reduce-q1-b6-part): d0, b6-k1, b6-k2 all checks MET; b6-k4 T2s FAILED (spread hot/cold z=3.16) -> rerun with burn 2304, base+50000 queued (rule).
## MY ERROR: reduced q1-b6-fix-k4 while its streams 2-7 were still running -> results_q1/q1-b6-fix-k4/summary.json is from partial data (s0,s1 complete, s2,s3 partial), INVALID, kept. reduce_q1.py now takes SUMMARY env var for the output name; the valid reduction is summary_full.json. Also: the clock shows 00:21 here, my earlier '00:24' timestamp in these notes was a guess, wrong.
## Q1 beta 6 fix-k4 full reduction (summary_full.json): all checks MET.
## Child returned (K16, 340 s); released T212.
Reread: lat.py checkerboard = site parity x direction (valid: same-parity sites never share a plaquette for the same direction); staples recomputed per direction; marks: loop2 path, transport P, plaquette orientation match the definition. 6 hot-start chains, 300 therm, 150 cfg x 10 sweeps; hot/cold checked only in a test (P2 hot .74944 vs cold .74987).
Child numbers: plaq .750028(80); ungated R1 .0130(11), R2 -.0008(10); gate1.2 R1 .0021(27), R2 .0005(27), frac .0402(5); clear R1 .0122(13), R2 -.0016(8), frac .9598(5); gate0.6 R1 -.0003(0) (error not trustworthy, few or no consecutive gated pairs), frac .0020.
Grandchild T213 (released by child): known-answer P(theta<pi/2)=.5; quadrature .27446856; single-link KP <a0> check. Child reran it: identical.
Parent rerun of child's analyze.py on prod_v1.json (pcp child-analyze-rerun): see diff result below.
-> analysis_parent_rerun.txt byte-identical to child's analysis_v1.txt.
## Q1 beta 12 (pcp reduce-q1-b12): d0, b12-k1, b12-k2, fix-k4 all checks MET. FAILED: b12-k4 T2_ratio1 z=-2.13; fix-k1 T2p z=2.44; fix-k2 T2_ratio1 z=2.12. Reruns (burn 4608, base 8050001/8150001/8250001) queued after Q2 (rerun_b12.sh).
Bases used: k-index in q1_all.sh: b12-k4 k=10 (8000001), fix-k1 k=11 (8100001), fix-k2 k=12 (8200001); reruns = base+50000.
## b6-k4 rerun (burn 2304, base 7350001) reduced (pcp reduce-q1-b6-k4-r).
## Q1 table (table_q1.py -> results_q1/table_2.md): b6 complete (b6-k4 from rerun); b12: 4 of 7 rows, 3 reruns pending.
Observation (numbers only): J1/Var1 at beta 6 and 12 within ~1.5 sigma of d0 for all displacements up to 0.61 (relative .97-.99) and 1.06 (b6, 1.22), 1.00 (b12, 1.22). J4/Var4 drops below d0 by 13-16% (beta 6: 1/beta, 2/beta, 0.305) and 19-29% (beta 12: 1/beta, 2/beta), then rises above d0 at 1.22 (1.15 b6, 1.07 b12).
## Q2 production done (K28, 476 s, 16 x 30000). First reduction (pcp reduce-q2-main) FAILED exit 1: my glob c*.txt matched commands.txt (my defect in reduce_q2.py), fixed to c[0-9]*.txt; rerun as reduce-q2-main-2.
## Q2 results (reduce-q2-main-2 K30, reduce-q2-more K31): all predicates MET: T1 16 chains (8/8); T2 plaq z .82, R1_all z .83, frac1.2 z .53; T3 max tau_int .86 cfg (need <= 150); T4 burn-in z -.30. Plaq .7500018(40).
R1/R2 (indicator-weighted): all .01354(9)/.00078(10); lt0.3 .00029(21)/.00003(4); lt0.6 .00037(14)/.00005(7); lt1.2 .00326(8)/.00025(7); clear .01147(7)/.00070(9).
Fractions: lt0.3 1.585(10)e-4; lt0.6 1.8954(38)e-3; lt1.2 .040325(11); clear .959675(11).
Gate - clear: D1 z = -53, -90, -71; D2 z = -6.7, -7.4, -5.1 (all significant, |z|>2).
Measured only, conditional (both times in gate): Rc1 lt1.2 .0381(18) vs clear .0119(1) z=+14.8; lt0.6 .017(40) z=.1; lt0.3 based on ~11 pairs total, not usable.
Child comparison: ungated R1 .0130(11) vs .01354(9) z=-.5; gate1.2 R1 .0021(27) vs .00326(8) z=-.4; clear .0122(13) vs .01147(7) z=.6; frac1.2 .0402(5) vs .04032 z=-.2; ungated R2 -.0008(10) vs .00078(10) z=-1.6. Agreement.
## beta-12 reruns (K32-K34, reduce K35): b12-k4-r all MET; fix-k1-r all MET; fix-k2-r FAILED T2p z=-2.73 and T2s z=+2.38 -> NO NUMBER for beta 12 at 0.61048 (rule). Final table results_q1/table_3.md (K36).
Overall first-run hot/cold failures: control (1 check), b6-k4, b12-k4, b12-fix-k1, b12-fix-k2 (x2 runs). With ~18 runs x 4 checks at 2 sigma about 3.6 chance failures expected; the fix-k2 double failure at beta 12 is not attributed to chance.
## Parent rerun of child production (K37 run.py prod_parent_rerun.json 135 s, K38 analyze): analysis byte-identical to child's analysis_v1.txt.
## Final: verify PASS (both). report.md complete.
