# notes d2-time (T226)
- step0 01:27: control.txt = 0.272341 (-ln tanh 1; control.txt existed with 9 bytes before, rewritten by me with the same 6-decimal value).
- step1: read PRIOR_REPORT/NOTES/REPLAY, build/src/c2/z1mx4.rs. Key fact: the D refresh uses a separate RNG (meas) and restores links,
  so the chain (rng) does not depend on whether D is measured. Plan: new mode "time" in z1mx5 = z1mx4 + Y marks, skipping the refresh.
- step2 01:31: build/z1mx5 (source build/src/d2/z1mx5.rs, diff z1mx5.diff, 159 lines, additions only + mode dispatch). z1mx4 rebuilds byte-identical from source.
  mkskel (K1), clear.py (K2: 40/60 at pi/4, kept 0,2,4 as prior). gauge_t (K3): T-P2 MET (Y(0)=X exactly, 0.0), T-P1 MET (<=3.4e-15, d0 and chain.skel0, hot and after 20 sweeps).
- ctl5.py (K4) exit 1: T-P0 FAILED for .meta.txt only (3 of 15 files): the meta line records the output prefix, which I made differ (…_old vs …_new).
  Defect of MY test design, not of the target. .csv .colours.csv .X.csv .Dc.txt byte-identical in all 3 cases; T-P3 MET (3/3).
  Re-test with identical relative prefixes in separate directories: ctl5b.py.
- ctl5b (K5) exit 0: T-P0b MET 15/15 (same relative prefix in separate dirs: all five files byte-identical, 3 cases), T-P4 MET 3/3 (<=5.1e-11).
- timing: time mode ~2.5 ms per measurement on top of the sweeps (~12 s per stream).
- step3 01:34: prodt.py written (design + INTERPRETATION RULE in its docstring, before any production run). Started
  prodt.py T-d0 skeletons/d0.txt weights/w_d0.txt 21100001 (K6, background).
- K6 T-d0 done (137 s). Child data: child/data = copies of results/T-d0/s*.mom.txt + w.txt (row 1 = prior w_L4). Child control (mine):
  R^2 for (0,0),(1,1),(2,1),(3,3) = 4.5^2/(5*4.75) = 0.852632.
- child-run1 launched (K7, background, T227); fitw.py (K8) launched after it.
- note: weights/w_d0.txt was written by an inline python (not a saved program): rows = prior w_L4 (308), prior w_L1 embedded by name, f4;
  asserted name order = prior_weights/names.txt = sampler X.csv header (checked: True). Clock correction: step3 started 01:31, not 01:34.
- K8 fitw.py: RP1 MET for L4 (train .0409724, held .0428277) and L1 (.0587371, .0589445): F-clear0 reproduces prior G-clear0; weights/w_clear.txt written.
- K9 antime T-d0 (01:37): 20 met, 0 failed. NOTE process defect (mine): numpy used >1 thread (user 15 s / real 5 s), briefly 3+ cores;
  later numpy runs use OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1.
  -I results t=1: wL4 loc rho .0224(40) R2_held -.0133(21) R2_train .0189; tr rho .0834(56) R2_held -.0023(18) R2_train .0287.
  f4 loc rho -.0023(57) R2_held -.0171(16); f4 tr rho .0759(53) R2_held -.0016(27). t=2: rho tr .016(6); t=3 all ~0.
  Held R2 negative = over-fitting of 308 predictors on 16x1152 correlated measurements (train R2 .015-.019 even at t=3 where rho ~ 0).
  L1-Y-only (15 predictors, measured only): tr t=1 R2_held .0113(17), loc .0002(5).
  Interpretation rule at -I: 'does not' clause (R2_held(1) < .02, se < .01) MET for loc and tr. (rule does not need the clear run for this clause)
- started prodt.py T-clear0 ... 21300001 (K10?, background) 01:38.
- child (K7, 90 s): control.txt 0.852632 = CORRECT (graded before reading anything else). results.json b0 (t=1 loc): rho .02241412755, R2_held -.01325896115(209),
  R2_train .01890697; b1 (t=1 tr): rho .08341148921, R2_held -.00233129207(176), R2_train .02869245; 0 discarded. Equal to my antime values at all printed digits.
  Its analyze.py = same formulas as mine (my prompt prescribed them): independent code, not an independent method.
  Grandchild T228 (admitted+released by child under T227): rho block 0 recomputed by streaming triangle sum with fsum: .022414127551879784 (control 0.852632 correct).
  Child's own process failure: its K2 (grandchild rerun from wrong cwd, exit 1), rerun K3 exit 0.
- K10 T-clear0 done (137 s). Released T227 (child_release.log). child rerun K11 in childcheck/ (python3 -I analyze.py, OMP 1 thread):
  NOT byte-identical: all values agree to <= 7e-16 (BLAS thread-count summation order). Measured only.
- K12 antime T-clear0: 20 met 0 failed. clear t=1: wL4 loc rho -.0031(60) R2_held -.0192(16); tr rho .0321(50) R2_held -.0145(22).
- K13 verdict.py: loc: -I minus clear R2_held .0060(26) z 2.27; tr .0121(28) z 4.30; neither > .1 -> 'persists' false; 'does not' clause true
  for both -> OVERALL 'does not' (per the rule). Measured only: tr rho diff .0514(75) z 6.9; tr L1-Y R2_held diff .0118(18) z 6.6:
  a small -I-specific carry-over to t=1 exists in the transported definition (R2 ~ .01), gone by t=2.
- 01:42 report.md written (8 STANDS, 1 DEFECT, 2 NOT CHECKED); verify PASS (py) and rust verify after K14.
