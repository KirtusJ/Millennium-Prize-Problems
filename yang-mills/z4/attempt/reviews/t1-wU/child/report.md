# report.md (T170 fidelity check of src/tun_upper.tex)

Control 2*asinh(1)=1.762747 (control.txt). Full table with evidence: findings.md.

| item | verdict | one-line evidence |
|---|---|---|
| tu:U-thm | MATCHES | lim = c* as in LOWER_FULL; c*=4.605413245 recomputed |
| tu:U-kernel | CHANGED (writer addition) | proof of (3) new, re-derived OK |
| tu:U-K | CHANGED (writer addition, radial form) | all constants = THEOREM s3; 150/150 numeric cases hold |
| tu:U-R | MATCHES (nit) | line 297 C_h^{-1}F_aC_h should be C_hF_aC_h^{-1} |
| tu:U-F | MATCHES | = LEMMA_F |
| tu:U-Frad | MATCHES | = I3 |
| tu:U-barta | CHANGED (CHAL_lemmaF I4) | boundedness hypothesis explicit |
| tu:U-fixed | MATCHES | = I5 |
| tu:U-bessel | MATCHES | = I6; 1800 cases, 0 violations |
| tu:U-I1 | WRONG | line 432: D(1)>0.039 false, D(1)=0.038931 |
| tu:U-amgm | MATCHES | = I8 |
| tu:U-outer | MATCHES | Taylor step correct; 707/707 qualifying cases pass |
| tu:U-F-master | MATCHES | M_in, M_out identical term by term; deficits 8.73-14.23 at beta<=4096, 2.2e13 threshold reproduced |
| tu:U-F-cor | CHANGED (CHAL_lemmaF header defect) | log max -> 0+, not M->0 |
| tu:U-weight | CHANGED (writer addition, c^rho for c*_eta) | (3),(4) correct, source version did not follow |
| tu:U-schur | CHANGED (CHAL_conditional item 7) | Taylor/cosh line added, correct |
| tu:U-A | MATCHES | = (A) |
| tu:U-B | CHANGED (C5 + writer additions) | C(eta) algebra re-derived; eta<=1/2 added |
| tu:U-flux | CHANGED (CHAL_conditional item 10) | prefactor 4; 3x3 ratio 4.0000 in 6/6 |
| tu:U-main | CHANGED (item 10, C5, c^rho) | final inequality re-derived, constants 4,2,8 consistent |

Counts: MATCHES 10, CHANGED 9, WRONG 1 (of 20).

Programs: check.py (predicates C1-C11 in docstring; result_check_run1.json). Failed predicate: C3 (tex claim D(1)>0.039) -> defect of the target, as I expected; run exit 1 was registered with --expect-exit 1. Tolerances: see docstring. Hypothesis counts: C9 150/150 qualify, C7 707/707, C10 only beta>125.

Grandchild: question = does the flux identity have prefactor 4 (3x3 symmetric positive matrices, 3 matrices x 2 splits)? id T172 (admitted by me, parent T170; released, event 343). Control: top eigenvalue of [[2,1],[1,2]] = 3.000000 correct. Outcome: ratio 4.0000000000 in 6/6, predicates 6/6 pass. I reread prog.py and reran it in gc_rerun/ (registered check K2, exit 0).

Not done: Lean files not compiled; second-half lemma tu:L-L4 not checked; (W1),(W3) existence only asserted.

Verify lines:

- pcp_os.py verify --ws pcp: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- pcpos verify pcp/register.jsonl: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
