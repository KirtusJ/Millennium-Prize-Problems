# notes r4-c

1. control.txt = 0.272341 (-ln tanh 1).
2. 28 .md files in input (17 central-quotients, 10 spectral-support, 1 top README). Larger lane = central-quotients (mine); smaller = spectral-support (delegated to child/).
3. count_md.py run 1 FAILED P1,P2: own expectation error (I miscounted: spectral-support has 11 .md, total 29 incl. top README). count_md2.py with corrected predicates. Smaller lane still spectral-support (11 files, 68KB) vs central-quotients (17, 120KB).
4. Delegated spectral-support lane to child/ (template + control question -ln tanh 1).
5. Read in full: CQ/README.md, CQ/execution.md, CQ/cube-strip.md.
6. Read in full: CQ/local-response/README.md, finite-graph.md.
7. Read in full: CQ/local-response/analytic-groups.md, rotor.md, transfer.md.
8. Read in full: CQ/local-response/adjoint-weight.md, execution.md (17 Lean decls, 3 mutations failed, analytic parts in notes not Lean).
9. Read in full: CQ/momentum/README.md, local-estimates.md, infinite-volume.md.
10. Read in full: CQ/momentum/third-moment.md, adjoint-refinement.md. Convention cross-check (by hand, not a proof check): g=0 adjoint energy 8k (adjoint-weight) = 4kC_Ad with C_Ad=2 in half-speed metric (momentum README) = n(n+2)k at n=2 (rotor); consistent given stated normalizations.
11. Read in full: CQ/momentum/wilson-time.md, execution.md. All 17 CQ files read in full.
12. CQ lane: no note explicitly flags statements 'for independent review'; selection of three made from lane's own statements of which steps are text-only (not in Lean). Arithmetic spot check: 1+(3/5)^6=16354/15625, 8177/2048-15625/4096=729/4096 consistent across README and cube-strip.
13. Drafted CQ section in report_cq_draft.md. Now reading 5 spectral-support files to check child rows.
14. Read in full (for checking child): SS/README.md, SS/diagonal/README.md.
15. Read in full: SS/adjoint-band/README.md, wilson-limit.md. Convention check: SS H=-(k/4)Delta_round equals CQ H=-k Sum X^2 with i sigma/2 generators (|X|=1/2 in round metric); both give M1=8k at g=0; CQ wilson-time states kappa=2/kappa_B. No unconverted clash found here.
16. Read in full: SS/positive-time/README.md, SS/positive-time/vacuum/README.md. Cross-lane note: SS positive-time strong-coupling obstruction (tanh beta_s,beta_t<=1/20, all connected autocorrelation limits vanish) vs CQ wilson-time band transfer (beta_t=kappa_B/a -> inf, fixed spatial mesh) are different regimes; no direct contradiction, but both say 'Wilson trajectory'. Toolchains differ: SS Lean 4.24.0/Mathlib f897ebcf, CQ Lean 4.19.0/Mathlib c44e0c8e.
17. Read SS/adjoint-band/review.md (D4 readback of B4, A4, C4 analytic-groups). Cross-lane count difference: SS review.md says 'All twelve declarations of JointCutoff' (revision 48fe5d2c, and 12 at evidence line); CQ momentum/execution.md says 'B4's fourteen JointCutoff declarations at 10820b46'. Different revisions are stated, no conversion given -> listed as convention/count discrepancy, not contradiction.
18. Child returned (report text only; harness blocked its file write; parent saved it to child/report.md, marked as such). Checked 5 child rows vs files: SS/README (6 decls, 3 mutations in execution.md adverse table) MATCH; diagonal (5 decls, 3 mutations, CONDITIONAL) MATCH; vacuum (5 decls, 4 mutations 'exercised') MATCH; wilson-limit (JOINT, no stated rate, mesh fixed) MATCH; adjoint-band/README counts 13 decls & 'Lean rejected all four' MATCH but regime ONE-LIMIT disputed: headline is fixed-mesh bound uniform in box (FIXED), volume limit is a sub-claim -> PARTIAL. Result 4 matched, 1 partial. Extra: positive-time 15 decls & 5 negative controls confirmed.
19. report.md assembled; final verify PASS.
