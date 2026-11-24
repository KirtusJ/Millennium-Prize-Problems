# f2-cross2 notes (worker T239, Director Z4)
## Step 0 (01:58Z+)
- control.txt = 0.272341 (-ln tanh 1). Lean READY exists; Lean not planned.
- PCP register pcp/ initialised.
- Read PRIOR_*, g4/cyclic-transfer/measurements.md.
- G4's four-bin statistic: per LINE squared winding w=(1/2 Tr W)^2, binned in 4 bins, joint histogram (t, t+lag) POOLED over 75 lines and all time origins, symmetrized; lambda2 = second-largest eigenvalue of J_ij/sqrt(v_i v_j) = max over centred bin-functions f of Corr(f(t),f(t+lag)) in the per-line (local, translation-pooled) law = 1 - min R over the 3-dim centred 4-bin span. So .06197/.00408 are 1 - R_min (local, 4-bin span), NOT slice-averaged R.
  Prior worker's Wa1 is the 25-line SLICE AVERAGE of w (zero momentum); its R includes cross-line correlations. Different statistic.
- Prior worker's per-chain data (results/) are not in this directory, and they only hold slice-averaged moment sums: G4's per-line histogram cannot be derived from them -> regenerate (new instrument computes both on the same ensembles).
## Step 1 instrument src/cross2.rs (built rustc --edition 2021 -O -o src/cross2 src/cross2.rs)
- 54 local fields (header of cross2.rs), classes L/Z/P0/P1/P2 + G4 joint histogram J.
- timing N10 T20: ~9 ms/sweep + ~7 ms/measurement -> chain of 500+2000x3 sweeps ~73 s; 16 chains on 2 cores ~10 min. c2 ~1 min.
- scratch selftest (pre-PCP): gauge maxdiff 4e-15, center flips 0, controls change -> fine.
- predicates fixed: src/predicates.txt (before production runs).
- seeds: c2 6101307, f2 6301307 (c4 6201307, f4 6401307 if run).
- child T242 admitted (child_admit.log); started 02:03Z on copies of c2 HELD chains in child/data
- analysis program src/analysis2.py written (predicates in docstring = src/predicates.txt). Test run on c2 vs c2 (scratch) for code smoke.
- smoke (scratch/smoke-c2c2.txt, c2 against itself): code runs; Q1 identity exact (|diff| 2e-16); c2 lambda2 = 0.06215(28) vs G4 .06197(257): agrees.
  c2 local fine-opt 1-R = 0.154, Z fine-opt 0.533, momentum ~0.13; tau_int Wa1 14.4 meas (limit 100).
- child control: 1.500000 (expected 1.5): CORRECT, graded before reading other output.
## Step 2: child T242 returned (released, child_release.log). Grandchild T243 (admitted under T242 by the child, released).
- child numbers on c2 HELD: R_L(Wsum) .938965(394), R_L(Psum) .974134(129), R_Z(Wsum) .683533(440), R_Z(Psum) .955176(202),
  lambda2 .0618653(354): all agree with my analysis2 (scratch smoke) to printed digits.
- child's failed P6 (1-lambda2 vs 'min R'): DEFECT OF MY PROMPT, not of the child or target: I defined the direction-SUM
  function sum_mu c.ind(w_mu(s)), which is not G4's one-line pooled law. My own check (src/check_dirsum.py, results/check-dirsum.txt)
  reproduces the child's .943850 (to 4e-7, rounding of its printed value) and the pooled one-line value .938135 = 1 - lambda2.
- reran child/analyze.py under PCP in scratch/childrerun: results.json identical.
- grandchild: recomputed lambda2 by charpoly/power iteration: agree to 1e-16 (child reran it; I did not).
## Step 3: 2l pair analysis results/analysis-2l.txt (K8)
- P1, P2, Q1 met on c2 and f2 (met 10 failed 0).
- G4 statistic on my ensembles: c2 lambda2 .062147(275) [G4 .06197(257): agree]; f2 .001578(136) [G4 .00408(72): differ by 3.4 combined SE;
  G4's own 4l value .00169(47) agrees with mine]. Measured only. My 2l f2 has 16x2000 meas vs G4's 4x128 after 256 burn.
- MAIN 2l: Z:ratio-opt held-out R_f/R_c = 0.94092(490), R_f .93177(396), R_c .99027(297), Var_f/Var_c 1.185 -> ratio+2SE = 0.9507 < 1.
  At 2l this defeats alpha > 0.951 (my expectation 'no test defeats alpha=1' FAILED -- my expectation, not a defect of the target).
  Needs the same frozen test at 4l (cross_eval2.py).
- S: slowest inherited mode on fine RESOLVED in every class: L 1-R_f .0115(6), Z .122(8), P0..P2 ~.009-.012(14-21).
  Contrary to prior 'R_fine in [0.976,1.003]' (16-function slice-averaged span): larger span Z finds 1-R_f = .12.
- src/cross_eval2.py written (retrain on 2l TRAIN, freeze, evaluate on HELD and on ALL chains of another pair; rotated copies
  of L/Z optima as a measured-only symmetry check). Smoke with eval=c2/f2 (scratch/ce-smoke2.txt): Z:ratio-opt rotated copies
  give held 0.932(4), 0.932(4): the effect is not a direction-specific fluke. Leading coefficients: w1*p1 (-1), w1 (+.76) ...
  Z:fine-opt/coarse-opt dominated by hh (neighbouring-line winding products) -- observables absent from the prior span.
## Step 4: 4l
- c4 done (K9, 109 s). f4 (16x2000, T=40) was KILLED by my harness's 600 s background limit (my process-management error,
  not a defect of the target): 2 chains complete, 2 partial (results/f4 kept, NOT used, no PCP record closed for it).
  Measured cost: ~270 s per T=40 chain of 6500 sweeps on the shared machine (estimate was ~145 s).
- Rerun as f4b: 16 chains x 1000 meas (gap 3), base seed 6501307 (new seeds), timeout 40 min. Budget forced 1000 not 2000.
- coarse period null c2 vs c4 (results/analysis-null-c2c4.txt, K10): P1,P2,Q1 met; c4 lambda2 .061323(224); min ratio+2SE = 1.0004:
  the same selection procedure on two ensembles of the same coarse lattice produces no spurious 'defeat' (false-positive control).
## Step 5: 4l results (f4b 16x1000, c4 16x2000)
- analysis-4l (K12): P1,P2,Q1 met; 4l-trained Z:ratio-opt held R_f/R_c .93783(393) (bound .9457); L:ratio-opt .99895(31) bound .99957.
  lambda2: c4 .061323(224) [G4 4l .06157(68): agree], f4b .001451(132) [G4 4l .00169(47): agree].
- cross-eval (K13, results/cross-eval-2l-frozen-on-4l.txt): 2l-frozen Z:ratio-opt on independent 4l ensembles (all 16+16 chains):
  R_f .93173(248), R_c .99571(114), R_f/R_c .93574(271), Var_f/Var_c 1.182 -> bound .9412; 2l held bound .9507.
  PREDICATE D: alpha > 0.9507 defeated at both circumferences by one frozen test. Rotated copies: .941(3), .948(3) at 4l.
- fine period null f2 vs f4b (K14): no test differs (min ratio+2SE 1.0003); f2 vs f4b lambda2 .00158(14) vs .00145(13): no period shift seen.
## Step 6: report.md final, REPLAY.md complete; PCP verify PASS (both). 02:34Z
