# notes

## Step 1 control
-ln(tanh(1)) = 0.272341 written to control.txt.

## Step 2 hypothesis count
28 files in input/: 27 lane .md + yang-mills_README.md. g4: 9 files (68 KB), transfer-operator: 18 files (140 KB). Smaller lane g4 -> delegated to child; transfer-operator done by me.

## Step 3 transfer-operator lane, read in full so far
- README.md (two-sector determinant test; adverse family; one-link SU(2) bound 3g/(2g+3)); execution.md: 9 Lean decls, 2 mutations rejected.
- blocked-time/README.md: SU(2), fixed spatial mesh, a<=kappa/4, z<=1/384, gap >= 4log3/(13kappa) uniform in L,a; local corr converge along every joint a->0,L->inf.
- blocked-time/compact-groups.md: any compact connected G w/ faithful rep; gap >= log3/((T+1)kappa), constants (G,pi)-dependent, nonexplicit T,h0; RP crossing-face check for open slab.
- blocked-time/local-limit.md: O(a^{1/3}) Wilson vs Hamiltonian; liminf/limsup gap in [4log3/(13k),12/k]; OBSTRUCTION: on tree-level trajectory kappa=beta b, gap diverges as 1/(beta b); only contact terms survive for scalar probes.
- blocked-time/momentum.md: per-momentum convergence O(a^{1/3} log^3).
- blocked-time/execution.md: 18 Lean decls, analytic steps listed as supplied in notes; 6 adverse changes failed.
- hamiltonian-time/README.md: fixed spatial mesh+volume, a->0 Wilson->Hamiltonian H (ONE-LIMIT time step); free gap 3min(L,4)/(2kappa); Yarotsky gap 3gamma/(8kappa) for 8z below unquantified threshold (CONDITIONAL on applicability of external theorem, threshold not numerical); extension to compact simple G for Hamiltonian; uncoupled rotation-test counterexample.
- hamiltonian-time/plaquette.md: variance>=5/9, M/v<=12/kappa for z<=1/384; large z>=36 bounds 3/64<=sqrt z d_p<=3.
- hamiltonian-time/execution.md: 11 Lean decls, 4 false changes rejected; analytic steps in notes.
- joint-cutoff/README.md: SU(2), fixed spatial mesh, finite L; |log-gap - Ham gap|<=180ac^2 for ac<=1/36, c=6lambda L^3+6/kappa. JOINT schedule aL^6->0 (fixed mesh) / a(1+c)^2->0. Open: isotropic removal, uniform gap on spatial continuum trajectory, nontriviality, 4D reconstruction (end).
- joint-cutoff/evolution.md: norm bound on positive-time evolution, six terms.
- joint-cutoff/finite-volume-vacuum.md: Delta >= e^{-sB}/(s 2^N), s=2kappa -> 0 as L grows; explicit schedule a_n.
- joint-cutoff/energy-density.md: three-reading test D(t); conversion gamma=kappa_A/4=1/(2kappa_B) STATED; sign of limit signal undetermined.
- joint-cutoff/execution.md: 14 Lean decls, 5 mutations rejected; numerical 32-mode circuit.
- spatial-plaquette/README.md: even L, V attains 0 and 2N_p; inf_c ||I-cB_kappa|| = (1-b)/(1+b) -> 1. FIXED obstruction. kappa here = SPATIAL action coefficient (clash with kappa = electric param elsewhere).
- strong-coupling/README.md: 4D Wilson, tanh beta_s,tanh beta_t <= 1/20: centered transfer norm <=1/3 (sharp comparison (22-3sqrt35)/13), uniform in L, LATTICE units per step; at fixed physical time connected elements vanish as a->0; influence lower bound obstructs Dobrushin for beta>=2/15. Execution: 14 Lean decls, 5 mutations rejected.
All 18 transfer-operator files read in full: 13 state results, 5 execution logs.
- Step 4: transfer-operator rows drafted in to_rows.md
- Step 5: read g4/README, cross-lane-review, complex/README, integral/README, open-slab, wilson-kernel in full for verification of child rows
- Step 6: g4 evidence counts from execution files: root 8thm+3def=11 reports,1 mutation; complex 24+9=33, 4 mutations; integral 28+3=31, 5 mutations
- Step 7: child returned g4_disposition.md; checked 6 rows (README, cross-lane, complex, integral, wilson-kernel, open-slab) vs files: 6 matched. Reran child count script and child verify.
- Step 8: report.md assembled from report_head/to_rows/report_mid/report_tail/report_end
