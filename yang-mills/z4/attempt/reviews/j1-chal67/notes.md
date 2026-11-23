# notes j1-chal67 (T113)
- step 0: control.txt = 0.272341 (-ln tanh 1). Register pcp init'd. Child admitted T114, started (child-run1) delegating (a): K1/K2 constants on grid.
- step 1: read LIMINF.md, SCALING_LIMIT.md, Liminf.lean. Hand recheck (my own algebra, same model family):
  (3.1) rescaling powers: (2pi^2)^-2 int|grad_A u|^2 = beta^{2/3} ||grad_Y Ru||^2 -> (2b)^-1 int|grad u|^2 >= 1/2 j^2 b^{-1/3}||grad_Y Ru||^2 : correct.
  (3.2): sin^2 a >= j a^2 on Omega; V >= 2b j^2 |A1xA2|^2 = j^2 b^{-1/3} w ; with J >= j^2 gives j^4 int w|phi|^2: correct LOWER bound.
  L2 / IMS constant: 1/2 (pi/(2 sigma_R))^2 * 2pi^2/b = pi^4/(4R^2) b^{-1/3}: correct.
  eps_X exponent: 1-cos 2alpha = 2 sin^2 alpha = 8R^2 b^{-2/3}, so exponent 8R^2 b^{1/3}; text has 16R^2 (overestimate, harmless).
  L7 step 3: 1-K1K2 - (1-K1)x1 = K1 x (1-K2) >= 0 needs K1>=0 AND K2<=1; text cites only "0<=K2<=1" (wrong reason, true statement).
  L7 step 5: q_h(psi_c) bound holds for every c because beta_l chosen with b^{1/3} nu_k -> Lambda (limit, not liminf); c-dependent further subsequence harmless.
- step 2: prog/kin.py (point a). One unrecorded dry run (output to scratch, deleted) showed Q0 fail at (beta=10,n=30):
  quadrature cancellation (kappa ~ 4.6e-16 below double eps*I1) -- MY cross-check's defect, not the target's. Predicates left unchanged;
  recorded run kin-run1 expect-exit 1 -> results/kin_run1.json.
- step 3: kin-run1 result: Q1 3695/0, Q2 3695/0, Q3 (LOW) 81090/0, Q4 (HIGH) 706608/0, Q5 6/0, Q0 17/1 (own cross-check defect, beta=10 n=30).
  measured: min over LOW of (1-kk)/((l1+l2)/2b) sits at n1=n2=M (never at n=1,2 unless M<=2); value 0.884 at m=.5 vs theta->0.8: bound holds, not sharp.
- step 4: ims-run1 (exit 0): I1 6/0, I2 30/0 (identity holds with the '+' sign as LIMINF L3 says), I3 6/0 (Schur bounds exact op norm; ratio 0.29-0.68),
  I4 6/0 (D <= (pi/2sigma)^2 (d1^2+d2^2) pointwise), I5 6/0, I6 8/0 (SU(2): E[a^2] ~ 3/beta <= pi^2/beta; 1-E cos ~ 1.5/beta <= 2/beta).
- step 5: lean-run1 exit 0, all 9 theorems axioms propext/Classical.choice/Quot.sound, no sorry.
- step 6: child T114 returned (control 5050 CORRECT, graded first). LOW/HIGH/K1 0 failures on its grid; grandchild T115 kappa_1(100)=0.98503788000816 (matches); LOW at (M,M), b=1e4,m=.5 ratio 1.1196 (my kin_run1: 0.88061/0.78654 = 1.1196, agrees).
  Reran child's check.py under my register (child-rerun1, exit 0), output identical to child/results_run1.txt. T114 released.
- step 7: flagged minor defects: L7 step 3 reason (needs K1>=0 too); eps_X exponent 16R^2 vs 8R^2 (harmless overestimate); corollary omits C1.
