# r10-chal notes (challenger of PROOF_FREE_BOUNDS.md)
Step 0: control.txt = 0.272341 (-ln tanh 1). PCP register pcp initialised.
Step 1 (reading, by hand): 
- Sec1 derivation: b^6 sum_xy f f e^{iq.b(x-y)} = conj(fhat(q)) fhat(q) for real f; with D^2 = l^-6 sum_{kk'} gives 2/l^6. Agrees.
- Decay: Delta^2 e^{-ipy} = |p|^4 e^{-ipy}; |ftilde(p)| <= ||Delta^2 f||_1/|p|^4, constant 1. Agrees. Sum |p|^-4 converges in 3D -> Fourier series abs. convergent, pointwise to continuous f. Legit.
- (2a) |q_i| <= pi/b: |q_i + 2pi m_i/b| >= 2pi|m_i|/b - pi/b >= pi|m_i|/b for m_i != 0; at boundary q_i = pi/b: pi|2m_i+1|/b >= pi|m_i|/b. OK.
- WORDING DEFECT: "BZ means representatives with |k_i b| <= pi" counts k_i b = +pi and -pi (same mode) twice for even N if read literally. Test numerically.
- (3c),(3d) recomputed: int |y| e^{-a|y|} = 4pi*6/a^4; (sqrt3/2) int e^{-a|y|} = (sqrt3/2)*8pi/a^3 = 4pi sqrt3/a^3. Agrees.
- (4a): 4 ordered pairs (k,-k), k in {+-e1,+-e2}: 4*(kappa/2)^2 = kappa^2. Agrees.
- Sec6 spot check by hand: v(0.05)=4.738e-3, V(0.05)=1.720e7 reproduced.
Step 2: chal.py (predicates Q0-Q12 in docstring) run via PCP check K1 -> results_chal_run1.json. All 13 predicates met.
 Q1 worst rel 1.9e-15 over 20 cases (N=6,8,9; ell=1,0.7; incl. FFT-free direct sums N=6,9). f non-symmetric (|Im fhat|/max = 0.43).
 Q1b literal "|k_i b|<=pi" double count at even N: rel. deviation +170% (N=6), +95% (N=8) -> mode k_i b = pi must be counted once; proof's wording defective, its numerics (agree 5e-15) evidently counted once.
 Q7 G(a)/latsum 1.26..5.9e5 (a=0.2..10): valid, very loose for large a (G grows like e^{sqrt3 a/2}).
 Q9 30/30 qualifying (b0 = 0.2191 ell for my f), bracket holds.
Step 3: sub-agent (child/) ell-scaling test returned 3 met 0 failed (its K1 crash = json bool bug, kept). I reread scaling.py and reran it (my check K2): result byte-identical in content to child/results_run3.json (written to ./results_run1.json because cwd). Child's C values agree with mine (N=6,tau=.05: 8786.47).
Step 4: Lean recompile of copy (R9Bounds_copy.lean) exit 0, axioms standard; 'sorry' occurs only in the header comment.
Step 5: report.md written. Verdicts STANDS 17, DEFECT 1 (BZ wording), NOT CHECKED 2. verify: PASS.
