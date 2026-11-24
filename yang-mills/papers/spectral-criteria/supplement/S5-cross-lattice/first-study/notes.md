# e2-cross notes (worker under T231)

## Step 0: control
- control.txt = 0.272341 (-ln tanh 1).
- Lean READY exists; Lean not used.

## Step 0: setup read from g4/ (sources: cyclic-transfer/measurements.md, winding.rs, winding.py, G4_FINAL_AUDIT)
- Lattices: periodic in all 4 directions, SU(2) Wilson, heat bath only (winding.rs: 3 HB sweeps between measurements, no overrelaxation).
  - coarse: N=5, beta=3.196581051; fine: N=10, beta=3.493705679 (calibration g^2_SF(l)=2.38, measurements.md).
  - temporal circumference 2l: T=10 (N=5), T=20 (N=10); 4l: T=20 and T=40 (optional 8th arg of winding.rs, measurements.md).
- Common coarse links: on N=10 the straight spacing-two links U(x,mu)U(x+mu,mu) with x on the even sublattice (stride 2, origin 0, as in winding.rs bases `step_by(stride)`); on N=5 the links themselves.
- Lag l/5: 1 step on N=5, 2 steps on N=10 (winding.rs: lag = stride = n/5). Checked in source.
- G4 time origins: ALL time slices t=0..T-1 on both lattices (fine includes odd slices), periodic wrap (t+lag)%T.
- G4 winding: value = (winding[0])^2 = (1/2 Tr W)^2, W = product of n fine links around the box along dir, at 25 transverse bases on the stride grid, 3 directions = 75 lines.
- Eligible observables: fixed functions of the common coarse links at each endpoint (squared winding, coarse plaquette half-trace = perimeter loop of spacing-two square on fine). NOT raw fine four-face sums.

## Definitions (fixed before any run)
For a test f (real function of one time slice's coarse links), stationary law of the ensemble:
- Var(f) = C(0) = E[(f(t0)-Ef)^2]
- E(f) = (1/2) E[(f(t0)-f(t0+lag))^2] = Var(f) - Cov(f(t0), f(t0+lag))
- R(f) = E/Var = 1 - C(lag)/C(0).
For a vector of observables x and coefficients a: f = a.x; Var = a^T C0 a, E = a^T (C0 - Csym(lag)) a,
Csym(lag) = (C(lag)+C(lag)^T)/2.

## Control (2l, G4 streams): G4's reducer winding.py on unz/ (= streams.zip, checked identical for n5-0):
  n5 0.0619674 +- 0.0025710 ; n10 0.0040821 +- 0.0007179 -> reproduces .06197 and .00408.
  4l: long-streams.zip is NOT in g4/cyclic-transfer -> 4l numbers (.06157, .00169) cannot be reproduced from files. winding.py crashes there.
  Own reducer: src/control_reduce.py (below).

## Step 1: instrument
- src/cross.rs (built: rustc --edition 2021 -O -o src/cross src/cross.rs), includes g4/wilson_mc.rs verbatim.
  Note: winding.rs includes ../../g4/full-attempt/two-site-gap/wilson_mc.rs (not in this tree); I assume g4/wilson_mc.rs is that file (not verifiable here).
- Timing: N10 T20: 24 sweeps+4 meas in 0.23 s (~9 ms/sweep). N10 T40 ~18 ms/sweep. N5 ~16x cheaper.
- Plan: 16 chains/ensemble (8 cold, 8 hot), burn 500, 500 meas every 3 sweeps, 4 ensembles incl. fine 4l (fits: ~900 core-s total).
- Predicates fixed: src/analysis_predicates.txt (before runs).
- Seeds: c2 5101307, c4 5201307, f2 5301307, f4 5401307; chain i seed = base+7919 i.
- control: own reducer src/control_reduce.py: see results/control_reduce.out.txt

## Step 2: child (T235, admitted under T231; child_admit.log)
- Delegated: independent reduction of per-chain S1/S00/SL sums (c2, f2, held-out chains) to held-out R of four
  tests fixed in the prompt (Wa1, Pa1, x10=Wa1^2, P_0-P_1) with chain jackknife; control: R for periodic 1,2,3,4 (known answer 1.2).

## Step 3: analysis program src/analysis.py; smoke test c2 vs c4 (both coarse, as a null control of period
   sensitivity on the coarse lattice): all held-out ratios R(c4)/R(c2) consistent with 1 (min 0.983+-0.044); P1,P2 met.
   (scratch/smoke-c2c4.txt; formal rerun under PCP into results/ later.)

## Step 4: 2l pair (c2 vs f2) results/analysis-2l.txt
- P1, P2 met on both; P3 1/16 hot-cold disagreement on c2 (measured only).
- Fine lattice: every eligible test has held-out R_fine in [0.984, 1.003] (lag-2 correlation of slice-averaged coarse
  observables ~0 within errors). Coarse: R_coarse from 0.597 (W_x-W_y) to 0.997.
- Smallest held-out R_f/R_c = 0.999 +- 0.008 (Pe^2); none significantly below 1. Training fine-optimal R_f = 0.973.
- E form: ratio-opt test (min E_f/E_c on train) held-out E_f/E_c = 0.00407 +- 0.00005, Var_f/Var_c = 0.00336; R_f/R_c = 1.21.
  So the E-form constant is driven by different stationary variances of the same function, not by slower decay.
- report.md early version written

## Step 5: 4l pair (c4 vs f4) results/analysis-4l.txt; nulls results/analysis-null-c2c4.txt, -f2f4.txt; cross-eval results/cross-eval.txt
- P1, P2 met on all four ensembles (f4 Wa1 tau_int 24.63 vs limit 25: marginal; f2 2.82).
- 4l: smallest held-out R_f/R_c = 1.0018 +- 0.0038 (Pe^2); none significantly below 1.
- Single frozen test across both circumferences: ratio-opt trained on 2l, held-out E_f/E_c = 0.00407+-0.00005 (2l), 0.00409+-0.00007 (4l, fully independent chains); its R_f/R_c = 1.212, 1.234.
- Period null: coarse c2 vs c4 no test differs; fine f4 vs f2: 5 tests with R(f4)/R(f2) significantly < 1 (smallest 0.9867+-0.0037) -> ~1% period dependence on fine only.
- Child rerun: identical output (scratch/childrerun).
- REPLAY.md written
- report.md final written
