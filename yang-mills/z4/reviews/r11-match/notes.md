# r11-match notes
- 09:54 control.txt = 0.272341 (-ln tanh 1). Lean READY absent -> no Lean used. scipy absent; numpy only.
- register pcp initialised.
- 09:56 child PROMPT written (M0 lit lookup), launching in background
- child-run1 finished (exit 0, 77 s). Control I2(1)/I1(1)=0.240194 graded CORRECT before reading rest.
- Child M0 output checked by me against child/src/fhk.txt (FHK hep-lat/9208012): Table 3 a*sqrt(sigma): 2.30 0.3690(30) [10^4], 2.40 0.2660(20), 2.50 0.1905(8) [32^4]; Table 8 1-<U_p>: 2.2986 0.39746(1), 2.3726 0.37661(2), 2.4265 0.36352(1), 2.5115 0.34564(1). CONFIRMED verbatim.
  Teper hep-th/9812187 Table 1: m0++/sqrt(sigma) continuum 3.74(12) (child claim; checking).
  Child violated "do not copy paper text": child/src holds pdf+txt of papers. Will delete after verification.
- Choice: (beta_c,N_c)=(2.3,6), (beta_f,N_f)=(2.5,12). l*sqrt(sigma)=2.214 vs 2.286, mismatch +3.25% (FHK) -> systematic.
  LTW hep-lat/0307017 Table 1 gives 0.17680(76) at 2.5115, i.e. ~0.180-0.185 at 2.5 -> mismatch could be ~0%; treat +-3% systematic.
- ym.py written (predicates C1-C6 in docstring). Timing (1 core): 6^4 sweep(1HB+3OR) 0.04 s, flow s=0.5 eps=0.01 0.44 s; 12^4 sweep 0.61 s, flow s=2 eps=0.02 12.4 s.
- PLAN CHANGE (before any data, reason: time): production eps = 0.025 (6^4) and 0.05 (12^4); C5 step-halving control is run at exactly these eps.
- controls (seed 7, controls_7.txt): C1 MET, C3 MET (both L), C4 MET, C5 MET (1.1e-5, 5.5e-7), C6 s=0.5 MET (+7.5%), C6 s=1.0 FAILED (+29.6%).
  DEFECT (mine): jk_err used sqrt((nb-1)var(b)) instead of sqrt(var(b)/(nb-1)) -> C1 error overstated x19. C1 diff -5.75e-4 is within 1e-3 anyway. Fix and re-run controls with seed 8.
  C6 s=1.0 failure: sqrt(8s)=2.8 on L=6; likely finite-volume zero modes (k_s=0 constant modes not damped by flow) -- my expectation, not established. Diagnostic: 8^4 later if time.
- 10:00 launched production:
  python3 ym.py run --L 12 --beta 2.5 --ncfg 170 --nsweep 2 --nor 3 --ntherm 100 --seed 1205 --s 2.0 --eps 0.05 --out meas_L12_b2.5_s1205.txt
  python3 ym.py run --L 6 --beta 2.3 --ncfg 3000 --nsweep 2 --nor 3 --ntherm 200 --seed 623 --s 0.5 --eps 0.025 --out meas_L6_b2.3_s623.txt
- jk_err fixed in ym.py (affects controls only; production analysis is in analyse.py)
- child report read. Grandchild question (via child): re-locate a*sqrt(sigma) at beta=2.5; grandchild/control.txt = 0.876282 (correct, = 1-I2(.5)/I1(.5) computed by me). Grandchild left NO result file; its answer 0.1905(8) exists only as the child's claim; I verified 0.1905(8) in FHK Table 3 myself.
- child/match.py rerun by me in rerun_child/: output identical. Mismatch (2.3,6)-(2.5,12) = +3.25% +- 0.94%.
- child web search was refused (child report) -> only arXiv PDFs. Deleted child/src (paper copies, rule violation by child).
- 10:02 analyse.py written; debug run on partial coarse data (436 cfgs) to scratch: code works. No predicate/plan changed after that look.
- added 'freefield' subcommand (C6 diagnostic, L variable). Note: E_free(s=1) itself depends strongly on L: L=6 1.82e-4, 8 2.26e-4, 10 2.40e-4, 12 2.44e-4 (x s^2). Hypothesis: spatially-constant modes (k_s=0, any k_0) are not damped by spatial flow and contribute via commutators beyond the free-field sum; finite-volume effect. To be tested with 8^4.
- derivations.md written (flow normalisation, free-field mode sum, Q0 normalisation, matching systematic).
- waiting for production; coarse ~0.35 s/cfg, fine ~8-9 s/cfg under load avg 5 (machine shared).
- 10:13 coarse run done (K3, 771 s, 3000 cfgs, 0.24-0.35 s/cfg).
- controls seed 8 (fixed jk): C1 MET (diff -7.96e-4, sigma 7.6e-4), C3 MET, C4 MET, C5 MET, C6 6^4 s=0.5 MET (+5.9%), s=1.0 MET (+14.4%).
  NOTE: C6 6^4 s=1.0 seed7 +29.6(2.2)% vs seed8 +14.4(2.4)%: seeds disagree by ~5 sigma -> quoted errors (12 cfgs, naive) are underestimates; slow zero-mode sector at beta=40, 60 therm sweeps from cold. C6 at s=1.0 on 6^4 is not a reliable test; count: s=0.5 met 3/3 (6^4 x2, 8^4), s=1.0 met 2/3.
- freefield 8^4 (seed 11): s=0.5 +5.6% MET, s=1.0 +10.0% MET. Excess at s=1 decreases 6^4->8^4 consistent with finite-volume zero-mode hypothesis (not proven).
- 10:19 fine run done (K6, 1124 s incl. 100 therm sweeps, 6.2 s/cfg). analyse-1 -> results_1.txt (PRIMARY result, fixed sample: coarse 2990, fine 160 cfgs after skip 10).
  Key: P1 MET both; P2 MET both; R(l/3) fine NOT RESOLVED (4.8e-4 +- 1.2e-3); fine R(6)= -2.0e-3 +-1.1e-3 (-1.8 sig, outside P1 scope, noted).
  P3: R(0) 0.913(33), R(l/6) 0.494(67), R(l/3) 0.13(33), Q0 0.956(12), Q0beta 1.040(13). None consistent with 1 at 2 sigma.
  Fine has only 8 independent jackknife blocks (block 19 cfgs = 10 x tau_int 1.81): error estimate itself ~ +-25% uncertain.
- 10:20 PLAN CHANGE (after seeing data, recorded as optional stopping): extension of fine run by 100 cfgs with --resume (M5 mechanism), copy of first 170 lines kept read-only as meas_L12_b2.5_s1205_first170.txt. results_1.txt stays the primary result; extended analysis is supplementary.
  python3 ym.py run --L 12 --beta 2.5 --ncfg 100 --nsweep 2 --nor 3 --seed 1205 --s 2.0 --eps 0.05 --out meas_L12_b2.5_s1205.txt --resume
- independent FFT recomputation of R(tau) (no jackknife) on both files agrees with results_1 (fine differs by <1% because analyse truncates to 152 cfgs = 8 blocks x 19).
- report.md drafted 10:2x
- 10:31 extension done (K8). analyse-2 -> results_2.txt (supplementary). analyse-1-rerun on first170 copy: identical to results_1. tau_int fine 1.81->2.40; Q0 fine moved +1.3 sigma.
- 10:32 PCP verify: python PASS, rust pass line quoted. report.md finished.
