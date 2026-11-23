# notes a3-B
- step 0: control.txt = 0.272341. Read A1_REDUCTION, INDEX_EXTRACT, LIT_RIGOROUS, LIT_ATTEMPTS. Lean READY exists. No scipy; numpy/mpmath checked.
- register init done.
- step 1: child/PROMPT.txt written (2D exact test of chessboard bad-plaquette bound). Child control: (2/pi)int e^{2cos a}sin^2 a = I_1(2) = 1.590637 (numpy trapezoid and series agree).
- step 2: child-run1 launched in background (register). 
- step 3: free_benchmark.py (K1, exit 0): G(0)=0.5 exact to 1e-6; G(n)>0; log-convex; n^4 G(n) ratio 0.88 (P4 met within 15%). c(n)=(G(n)/G(0))^2: c(1)=1.9e-2, c(4)=1.5e-6, c(10)=4.6e-10. n*b(n) -> ~7.8 (expected 8). 5 met, 0 failed, 3 measured.
  4D chessboard bound: only nontrivial for beta*delta >~ 40 (e.g. beta=128, delta=0.5: e^-10). Controls LARGE fields only, not the O(1/beta) fluctuations.
- plan of chain: S0 state/OS; S1 spectral ineq (PROVED); S2 reduction to fixed-n limit (PROVED); S3a chessboard (CLAIMED, chessboard theorem for gauge links not located with locator); S3b local Laplace given boundary (CLAIMED); S3c boundary-term (MISSING). 2D row of A1 is a DEFECT: 2D infinite-volume OS space for gauge-invariant obs is C*Omega (plaquettes iid), m=+inf.
- step 4: S2.lean passes (exit 0, axioms propext/Classical.choice/Quot.sound), register lean-S2.
- step 5: child control graded CORRECT (1.590637). Sharpened S3a: chessboard + two-sided free energy f(beta)=-(9/2)log beta+O(1) -> P(O_p>t)<=exp(f(b/2)-f(b)-t/8) in 4D (images |Lambda|/4 -> factor 1/4: the measured 4D numbers in result_free_benchmark_1 used -beta*delta without the 1/4 image factor: my error, superseded). Writing sharp_chess2d.py (exact 2D torus test).
- step 6: sharp-chess2d-1 (K4) exit 1. Q1 FAILED: defect of MY program (logsumexp_pow returns num/den = a0 * P, missing 1/a0), so torus P values in result_sharp_chess2d_1.txt are a0*P (too small) and Q2 240/240 is VOID for finite L (inf-volume rows are correct). Q3 FAILED: my own expectation (1e-30 below double-precision quadrature floor). Also run used ~3.6 cores (numpy threads): rule-8 breach, mine. v2: fix normalisation, J=200, 100001 pts, Q3 -> (ahat_J/ahat_0)^(N-1)*J < 1e-12 or |ahat_J/ahat_0|<1e-12, OMP_NUM_THREADS=1.
- step 7: child report read (control graded first: correct). Reread pcp_main.py: P_L = sum r^(N-1) rp / sum r^N with r=A/A0, rp=Ap/A0 -- correct normalisation. Rerunning in child_rerun/ (single thread).
- step 8: sharp-chess2d-v2: Q1 MET, Q2 MET 240/240 (149 informative, min log(bound/P)=0.594), Q3 MET. Count line printed "met True, failed 2" and exit code 1: numpy-bool addition bug in MY count line (np.bool_ + -> logical or), not a predicate failure. Delta(beta) -> 1.0368 vs (3/2)log2=1.0397 (measured): the free energy step of S3a is borne out in 2D.
- step 9: PROOF.md written.
- step 10: child-main-rerun K6 exit 0; results.jsonl, table.md, m1.md byte-identical to child's. verify run.
