# notes

## step 1
control.txt = 0.272341. 28 .md in input/ (27 lane obs-normalization incl. its README, 1 lane volume-uniformity, 1 problem README). Register pcp init.
## step 2
Delegated volume-uniformity lane (1 .md) to child/. Read in full so far (obs-norm): README, execution, energy-density/{README,spatial-limit,execution}, hamiltonian-variance/{README,execution}, excited-band/{README,execution}.
- top README: CONDITIONAL (on constructed spectral rep / OS reconstruction); 2 Lean decls.
- energy-density: FIXED (finite SU(2) Hamiltonian, b^3 D_H<=25 on bare traj); spatial-limit: ONE-LIMIT (spatial mesh b->0, time already continuous) but only first-moment form; 9 Lean decls, analytic steps outside Lean.
- ham-variance: FIXED spatial cutoff, uniform in volume; 9 Lean; 1 mutation + 1 numeric mutation.
- excited-band: FIXED couplings, volume subsequence; ITERATED via B4 (time step then volume); 6 Lean; 1 mutation.
## step 3
Read in full all 27 obs-norm .md (16 result notes incl. controls.md/refinement.md/spatial-limit.md, 11 execution receipts). count_md.py run via register.
Constant cross-checks by hand: C_3=72*1200^2+1+1536=103,681,537 matches moment-bounds G_pp; 86401^2>=72*C_3; sqrt(16*145*18*C_3)~2.08e6<2.1e6; b^3 D_H<=4(5+9/8)=24.5<=25. All consistent.
## step 4
count-md K1 exit 1: P1 failed (29 not 28: I forgot to add yang-mills_README.md to the 27+1), P3 failed (12 execution.md not 11). Both are MY expectation errors, not defects of target. Kept; not rerun (result file not overwritten).
obs-norm: 15 result notes + 12 execution receipts = 27; all read in full.
## step 5
Child returned (report as text; child/report.md write refused by harness). 5/5 fields matched. Both registers verify PASS. report.md written.
