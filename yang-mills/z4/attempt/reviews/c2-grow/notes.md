# notes c2-grow (T223)
- step0: control.txt = 0.272341 (-ln tanh 1). started 01:10
- step1 (01:20): read prior record. Geometry (faces.py): ring 1 = 7 coarse faces containing E_y=((2,0,0),y) [W] or E_z=((2,0,0),z) [B]:
  xy(0,0,0) marked, xz(0,0,0), xy(2,0,0), xz(2,0,0), yz(2,0,0), yz(2,0,4), yz(2,4,0). Ring 2 = 33 faces sharing a coarse edge with ring 1.
  Plan z1mx4: references B (xz coarse holonomy at root) and T = 1 (plain trace; both invariant under the U(1) stabiliser about i at W=-I).
  Lists: L1 = prior 15; L2 = ring1 B marks (4 plaq + Rv,Rh,L_no11 per face) = 49; L3 = L2 + ring2 B plaquettes (132) = 181;
  L4 = L3 + ring2 B partial (99) + ring1 trace plaquettes (28) = 308. Trace refs not used on partial loops (Re(L_no11) = -Re(g11) exactly at -I faces).
  D stored summed over colours only (sparse accumulation) + per-colour diagonal, to keep files small.
- step2: build/z1mx4 compiled (rustc --edition 2021 -O; source build/src/c2/z1mx4.rs). mkskel K1. gauge d0 (K2 + direct run gauge_d0 output):
  P6 MET (1.2e-15). P9 MET: ring1 holonomies xy000 -I, xy200 -I, yz204 -I; xz000 +i, xz200 -i, yz200 +i, yz240 +i (angle pi/2); all 33 ring-2 faces +I (angle pi).
  So the three -I faces are exactly the three faces through the twisted y edge (as the prior record); the B edge adds four i-type faces.
- step3: P8 MET (K4: csv byte-identical to z1mx3; 15 L1 marks identical; D diag rel dev 3.8e-13). clear.py K3 reproduced prior selection (40/60 at pi/4, kept 0,2,4). Started G-d0 = prod4.py G-d0 skeletons/d0.txt 11100001 at 01:13 (32x1152, 2 streams concurrently).
- step4: child admitted T224 (parent T223). Child control answer (mine): smallest lambda with det(diag(2,3) - lambda [[2,1],[1,2]]) = 0 is (10 - sqrt 28)/6 = 0.784749.
- correction: control answer to 6 decimals is 0.784750 (0.78474956), not 0.784749 (my arithmetic slip in the line above).
- G-d0 done (K5, 158 s). Started G-clear0 = prod4.py G-clear0 results/gen/chain.skel0.txt 11300001.
## G-d0 results (an4 K6; results/G-d0/an4.txt)
- held-out optimum (jackknife): L1 .02083(47) [train .02134, cond 49]; L2 .01668(44) [train .01724, cond 83]; L3 .01587(42) [train .01625, cond 86];
  L4 .01543(40) [train .01571, cond 2.4e16 -> 4 exact null directions truncated]. All held BELOW train (gap -.0003..-.0006): the held half is slightly easier; A3 met.
- G1 'stopped falling' (|diff| <= 2 comb se): L1->L2 FAILED (z -6.4: still falling); L2->L3 MET (z -1.33); L3->L4 MET (z -0.77).
  Measured only: paired jackknife differences are significant (paired z -38, -15, -12): small but real further falls (5 %, 3 %).
- L4 null directions: B.f.L_no11 = -/+ T.f.g11 on the four i-type faces (xz000, xz200, yz200, yz240): Re(B L_no11) = Re(B B_f g11^-1...) = -/+ Re(g11) identically. Structural property of MY list, not of the target.
- face support (L4): yz204 .32, xy200 .25, xy000 .25, yz200 .09 (i-type face containing both changed edges), others <= .01.
- A1 MET, A5 MET (z -.30, +.63), A6 MET (L1 vs prior .02157(46): z -1.12), G2 MET (rel err 2.3-2.7 %). A4: opt z 1.56 MET, f1 .88 MET, f4 z 2.22 FAILED (my expectation; same test failed in prior X-d0; chance-level).
- L2 minus the four i-type faces (21 marks): .01792(44): the i-type faces (mostly yz200) give .0012 of the L1->L2 drop of .0042; the partial marks on -I faces give the rest.
- child-run1 launched 01:16 (cwd child/, data = copy of results/G-d0/mats: per-stream sum1, sum2, m, D for all 308 marks).
- G-clear0 done (K7, 163 s). Q2: build/q3 (source build/src/c2/q3.rs) tested in scratch/: Q3-P1 1.1e-14, P2 6e-17, P4 0; ~22 ms/config; pilot 200 configs: 2.1 gated (r,o) per config at theta 1.2, 0 at 0.6, 0 pairs at t=1. Started q3-main: run_q3.py main results/G-d0/w_L4.txt 12100001 2000 (16 chains x 2000) at 01:19.
## G-clear0 (chain.skel0, min angle 1.142692; an4 K9)
- held: L1 .05894(76) [cond 12]; L2 .05333(53) [28]; L3 .05095(40) [29]; L4 .04283(44) [cond 259, no truncation]. Held ABOVE train here (gap +.0002..+.0028).
- G1 FAILED at every step (z -6.1, -3.6, -13.7): on the clear skeleton the optimum keeps falling, most at L3->L4 (ring-2 partial + ring-1 trace marks).
- face support L4: xy200 .55, xz200 .25, yz204 .06, xy000 .03. A1 MET, A4 MET (z .21, -.07, -.75), G2 MET.
- contrast L4: -I .01543(40) vs clear .04283(44): ratio 2.78; L1: .02083 vs .05894 (2.83).
- child control.txt = 0.784750: CORRECT (graded before reading anything else of its output).
- child (T224) report read after grading control. Its numbers for L4: lambda_train .015708941, q_held .015427728(396), cond on range 359 (rank 304), best single held B.yz204.Rv .045581, B.xy000.g00 single held .060564; grandchild T225 (B.xy000.g00 single .06056377, cond first-15 block 42.68; control 2.000000 correct). Child's own P1 (C PD) FAILED: the 4 exact null directions of my list (structural, my list).
- child-rerun K10 in childcheck/: results.json byte-for-byte equal content (identical True). Child's method = eigen-whitening + truncation, same as mine: an independent code, not an independent method.
- released T224: RELEASED T224
- swap4 (K11, K12): symmetrised optimism gap d0: L1 +.00001, L2 +.00005, L3 +.00013, L4 +.00018 (S1 MET all); cos(w, w_swap) in C metric .9999/.9995/.9987/.9985.
  clear: +.0005/+.0019/+.0021/+.0017; cos .977/.413/.860/.960 (clear L2 direction ill defined).
- report.md (Q1) written 01:21.
## Q2 (q3-main K13, 237 s; an_q3 K14; diff K15 failed = my bug (__file__ in exec), rerun K16)
- 16 chains x 2000 configs (32000), plaquette .7500045(149) (T3 vs prior z .18 MET). Q3-P1 (<=1.8e-14), P2, P3, P4 asserted in all 16 chains (exit 0).
- gate theta<0.6 (all three -I-class faces): fraction 6.4(2.6)e-8, 32 gated (root,orientation) sites in total, 0 pairs at t=1 -> NOT RESOLVED.
- gate theta<1.2: fraction 1.486(14)e-4, 73928 sites, pairs at t=1..4: 52, 4, 12, 8 -> fewer than 200 -> NOT RESOLVED (R1 FAILED as an outcome). No gated R(t) reported.
  Gated counts come in multiples of 4: the three-face set has a 4-element stabiliser (x-reflection about x=2, y-reflection about y=1), so independent gate events = count/4 (13 at t=1 for theta 1.2).
- ungated (identity orientation, 324 sites/config): composite R(t) t=1..4 .01280(33), .00010(24), .00007(27), .00001(27); single four-face .01315(30), .00087(20), .00013(24), .00012(36) (T4 vs prior .01354(9): z -1.22 MET).
  paired comp - single: t=1 -.00036(40) (z -.9), t=2 -.00077(29) (z -2.6). T2 hot/cold MET (plaq .76, comp R1 -1.33).
- final: report.md complete; verify PASS (py), rust verify last line quoted. 01:24
