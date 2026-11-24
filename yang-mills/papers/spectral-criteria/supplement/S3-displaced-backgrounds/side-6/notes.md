# z1-mix6 notes (T205)
## Step 0 control
control.txt = 0.272341 (-ln tanh 1).
## Child
Admitted T208 (parent T205). PROMPT: independent implementation of side-6 W=-I control at reduced stats (4 streams, 200 burn, 80 meas). Control question: Haar E[(TrU/2)^2] = 0.25. Launched via pcp check child-run1 (background).
## Step 0: the measurement in my own words (from fixed.md, replicas.md, replicas.rs, fixed.py)
- Lattice N^3 x T periodic (N=6, T=12), SU(2) quaternions, weight exp(beta sum_p Re U_p), beta=3.276133577.
- Frozen: on t=0, spatial link (s,i) frozen iff the two coordinates of s other than i are even (straight spacing-two skeleton, both halves of every coarse edge). All set to I except y-link at (2,0,0) := W (sign*I in G4) and z-link at (2,0,0) := i. So coarse xy square at 0 has holonomy W, coarse xz square at 0 has holonomy B=i. Other coarse squares sharing these two edges also change (xy at (2,0,0) gets conj W, yz at (2,0,0) gets W*conj(B)-type holonomy...).
- Free links (all time links, all other links) updated by conditional heat bath only ("conditional_sweep": heat bath, no overrelaxation, in the fixed mode).
- Tests: g_j = four fine xy plaquettes of marked square, transported to root along +x then +y; gbar = mean. f1 = Re(B g1), f4 = Re(B gbar), B = face(0,x,z,2) (actual xz holonomy, = i). spread = 1-|gbar|^2.
- Colour: (plane o in xy,xz,yz) x (parity of base site s on slice 0) = 24; each colour = 27 pairs at N=6; a pair = the two links of the fine plaquette at s in plane (i,j) with odd transverse coordinate (i-link at s or s+e_j, whichever has odd j coordinate; likewise j-link). Never frozen.
- J (per measurement): for each colour, refresh all its pairs by the exact pair law (independent heat-bath proposals with staples omitting the common face, accept exp(beta(ReU_p-1))), read f'; refresh again (independent draw, law does not depend on current pair), read f''; J += (f'-f'')^2/48 (i.e. mean over 24 colours of half squared difference); restore. Refresh uses separate RNG stream (seed ^ 0x6a09e667f3bcc909), so the main chain is unaffected.
- Denominator: plug-in variance (np.var, ddof=0) of f over all measurements pooled across the 4 streams. Ratio = mean J / pooled var. Errors: paired delete-one-stream jackknife sqrt(3*mean((drop-mean)^2)) (with 4 streams; factor (n-1)/n * sum = 3*mean).
- Runs: 4 streams, hot = i%2, seed = base+7919 i; 288 burn conditional sweeps, 144 measurements 6 sweeps apart. minus6 base seed 1700451.
- Build: replicas.rs includes ../../g4/full-attempt/two-site-gap/wilson_mc.rs (from G4's tree, copied read-only into build/; sha256 5366fd10...). Compiles only with --edition 2021 (edition 2015 array into_iter gives refs). Source unchanged (cmp OK).
## Step 0b: control run (ctl.py, pcp check K1, 13.7 s)
- C1 FAILED (bit replay with G4 seeds): outputs not byte-identical. Cold streams 0,2 match G4 to ~1e-5 in row 1 then diverge chaotically (row 20: O(1)); hot streams differ already at row 1. Diagnosis: same seeds/algorithm (row-1 agreement 5e-6 on cold), differences are floating-point (libm ln/cos/exp or compiler) amplified by the rejection-sampling chain. My expectation (byte identity) was wrong; not a defect of the target.
- G4-seed replay (statistically independent of G4 after divergence): ratio4 .0432(33), ratio1 .0606(72), spread .3458(74), var4 .0653(50).
- New seeds 7700451: ratio4 .04516(315) vs G4 .0464(55): z=-0.20 C2 MET. ratio1 .0573(9) vs .0639(23): z=-2.66 C3 FAILED (4-stream jackknife error on my side looks too small: per-stream ratio1 .0591 .0608 .0556 .0563; G4-seed replay gives .0606(72)). Attribution open: probably underestimated 4-stream errors (my expectation), see larger control below.
- C4 MET: cold .0409 vs hot .0511, z=-1.62.
- Speed: ~1.7 s per stream (288+864 sweeps + 144 J). Big statistics affordable.
## Step 1 setup
- Own sampler build/src/mine/z1m6.rs (includes G4's wilson_mc.rs primitives only). Predicates P1-P4 in its header.
- P1 (colour disjointness, 27 pairs/colour, no frozen pair link) passed (asserts). P4 MET: at skeleton d0 with G4 seeds 1700451 (cold) and 1708370 (hot), first five columns byte-identical to build/g4_replicas on this machine (results/p4).
- Skeletons: mkskel.py; W_delta = (-cos d,0,0,sin d) on y-link at (2,0,0) (= marked xy holonomy), B=i on z-link at (2,0,0); all other frozen links I. Realised exactly as G4 realised W=-I: only the second-half y edge of the coarse edge from (2,0,0). Note: this also moves the coarse xy face at (2,0,0) (holonomy conj W) and yz faces through that edge; min clearance = delta. (Cosmetic bug: comment line in skeleton files prints W[1] in place of W[3]; data lines correct.)
- Production design: 8 streams, seed base+7919i, hot=i%2, burn 576, 576 meas spacing 6. d0:3100001 d0.5:3200001 d1:3300001 d2:3400001. Started runs_perturbed.sh.
## Step 1 results, round 1 (8 streams x 576, reduce.py; results/<tag>/summary.json)
d0:   minang 0     spread .3418(17) var4 .05975(171) J4 .002902(37) r1 .0623(23) r4 .0486(12) b*r1 .2040; T2 z r1 -0.03 r4 -1.28 MET
d0.5: minang .1526 spread .3481(19) var4 .06502(84)  J4 .002940(49) r1 .0619(11) r4 .0452(11) b*r1 .2027; T2 z -1.30, 0.19 MET
d1:   minang .3052 spread .3434(23) var4 .06376(146) J4 .002985(51) r1 .0636(9)  r4 .0468(13) b*r1 .2082; T2 MET
d2:   minang .6105 spread .3369(31) var4 .05949(90)  J4 .002900(32) r1 .0618(10) r4 .0487(9)  b*r1 .2025; T2 MET
Per-colour (d0): J1 carried by colours 0,1,2 (.45,.28,.27), J4 by colours 0-3 (.32,.31,.15,.22); all xz/yz colours and pz=1 colours exactly 0 (they do not touch the test's links).
## Clear skeletons: clear.py (pcp K4): 60 unconditioned skeletons, 40 clear at theta=pi/4, 57 at pi/8, 59 at pi/16; theta=pi/4 chosen by the fixed rule; kept 0,2,4. min-angle quantiles (0,25,50,75,100%): .073 .738 .910 1.041 1.357. slice-0 plaquette mean .7498.
## Child returned (K6 310 s). Control 0.250000 graded CORRECT before reading anything else. Released T208.
Child results (4 streams x 80, numpy): r4 .0574(38), r1 .0713(44), spread .3684(44) (z=2.56 vs G4), var4 .0491(36).
REREAD: child's sweep() updates all free links of one direction SIMULTANEOUSLY (vectorised heatbath over gp[mu]). Links U_mu(x), U_mu(x+nu) share plaquette (x,mu,nu): simultaneous update is not a valid heat bath (no checkerboard) -> chain does not sample the Wilson law exactly. DEFECT in the child's implementation. Pair draw and KP heat bath formula look right.
## Round 2 launched: clear0/2/4 (8x576, seeds 5100001..), L-d0..L-d4 (24 streams x 1152, seeds 6100001..; d4 = 4/beta extra, outside brief).
## Clear backgrounds (8 x 576 each; K8-K10)
clear0 (chain skel 0): minang 1.1427; spread .3509(13); var1 .04795(110) var4 .00770(20); J1 .00386(5) J4 .000708(8); r1 .0805(21) r4 .0920(24); traceless-B: r1 .0700(15) r4 .0848(34); T2 MET
clear2: minang .9586; spread .3510(16); var4 .00972(19); J4 .000836(12); r1 .0716(15) r4 .0860(20); tl r1 .0683(8) r4 .0827(25); T2 MET
clear4: minang 1.1820; spread .3487(13); var4 .00773(17); J4 .000718(9); r1 .0714(21) r4 .0928(23); tl r1 .0707(18) r4 .0955(34); T2 MET
J4 on clear: colours 0-3 ~ equal quarters; J1 colours 0,1,2 (.42-.44,.28-.29,.28). Other 20 colours exactly zero.
Mean pair proposals per accepted draw: 2.97-3.10 (clear), 2.75-2.82 (d0,d2).
(meta label 'B_full_and_tests_at_start' actually prints the five tests at the start configuration, not B; cosmetic.)
## Round 2 large runs (24 x 1152, K11-K15) — see results/tables.md
beta*J1/V1: d0 .2008(13), d0.5 .2020(18), d1 .1991(22), d2 .2040(17), d4(extra) .2158(16). Relative to d0: 1.006(11), .992(13), 1.016(11), 1.075(11). Disk relative: 1.010, 1.039, 1.152, (4/beta) 1.531.
J4/V4: .0469(5), .0467(5), .0452(6), .0479(4), d4 .0577(7). Var4: .0613 .0631 .0662 .0596 .0369. J4: .002875 .002948 .002992 .002858 .002129.
All T2 hot/cold MET (|z| <= 1.64). Larger-run d0 r1 .0613(4) vs G4 .0639(23): z=-1.1 -> C3 failure in the 4-stream control is attributed to underestimated 4-stream errors (my expectation), not a defect of G4.
## Child rerun (K16) and heat-bath tests (K17, K18 failed: scipy missing / my dict-iteration bug; K19 passed)
- childcheck/orig stream0 rerun: bit-identical to child/results80/stream0.json (determinism confirmed).
- checkerboard-patched child code (childcheck/mix6_cb.py, 4 x 80): r1 .0614(37), r4 .0440(50), Var4 .0651(103), spread .3640(28) -> ratios agree with G4 and me; spread still above my .3416(12). With per-measurement sd .154, SE of 320 child measurements >= .0086 -> about 2.6 sigma; unresolved, not used.
- Exact single-link law E[a0]=I2(k)/I1(k) for k in {.5,.99,1.01,1.9,2.1,5,10,20}: G4 wilson_mc heat 8/8 within 4 SE, child heatbath 8/8.
