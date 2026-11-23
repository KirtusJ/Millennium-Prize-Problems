# notes a3-Afs
Step 0: control.txt = 0.272341 (-ln tanh 1). Lean READY exists.
Step 1: register pcp initialised. Child control answer computed first by me: I_2(2)/I_1(2)=0.433127 (trapezoid, 2e5 pts). Child task: 2D exact z(L) + 2D U(1) MC check. Starting child.
Step 2: wrote zflux.py (4D MC of z(L)=L m_L from spatial Polyakov-loop correlators, SU(2) and U(1), beta=2.3, L=2,4,6, T=12); predicates C1,C2,P_A..P_D fixed in docstring before the first run. Timing probe only (no result file): SU2 L=6 0.033 s/sweep.
Step 3: child control.txt = 0.433127 -> CORRECT (graded before reading anything else of its output). zflux controls C1 (both groups), C2 MET; SU2 L=2 z=0.562+-0.016. Drafting PROOF.md while MC runs.
Step 4: zflux-run1 done: P_A,P_B,P_C MET, P_D FAILED (U1 z=0.34,0.55,0.68 vs 1/(2b)=0.217; rotor model at T=12 predicts 0.32,0.42,0.50 -> finite-T thermal population of flux zero-mode, my own expectation). SU2 z=0.56,2.12,8.02. Child returned 2D table and MC L=2; rerunning in rerun/.
Step 5: reruns K2 (table), K3 (grandchild series), K4 (child MC L=2) identical to child outputs (only runtime line differs).
Step 6: child finished (K5 exit 0, 287 s). Child report read; it agrees with my reruns. Writing report.md.
Step 7: report.md written; verify PASS (both).
