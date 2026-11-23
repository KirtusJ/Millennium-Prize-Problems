# notes m1-agmon (T129)
Step 0. control.txt = 0.272341 (-ln tanh 1). Lean READY exists.
Step 1. Read brief, TUNNEL_MEASURED.md, A4_center_bounds.md. Register pcp initialised. Child admitted T132 (child_admit.log), started (child-run1), question: eps_eff(a) numerically, control arccosh(3)=1.762747.
Step 2. Key observations (derivations, to be put in TUNNEL_THEOREM.md):
 - Fibre: V_a(U2)=2 beta s^2 (x1^2+x2^2) vanishes on the whole circle {U2 commuting with U1}, not only at U2=+-1 (brief's "concentrated at two points" is wrong).
 - Exact reduction: fibre top eigenfunction is bi-U(1) invariant -> function of t=x0^2+x3^2-x1^2-x2^2 (uniform on [-1,1]); Legendre basis; V=beta s^2(1-t).
 - Valley is 2-dim (commuting pairs (a,b)); harmonic transverse energy at (a,b) = 2 asinh(sqrt(sin^2 a + sin^2 b)) >= eps(a); Agmon distance between wells (0,0),(pi,0) = c* exactly, minimiser b=0 (needs sin b = 0).
 - Agmon inequality with weight Phi(a1) only: B=K2^{1/2}e^{-V/2}, T=B*K1B, B*B fibrewise norm e^{-eps_eff(a1)} => lambda||h||^2 <= int w(a1) e^{-eps_eff(a1)} |h|^2, w = int k cosh(sqrt(beta)(Phi(x)-Phi(y))). Rigorous; only missing input: Lemma F (eps_eff >= eps - o(1) uniformly on compacts).
 - Splitting bound: sign trial s=sign(cos a1) gives lambda_ee-lambda_eo <= 2<g1_A, T g1_{A^c}> (exact identity for s^2=1).
 - Brief's needed kernel bound with radial d(g) is false at small p (E e^{p|Z|} ~ 1+1.6p > e^{p^2/2}); correct form uses p.X and cosh.
Step 3. eps_eff.py (check 'eps_eff' -- NB the register auto-named the check K1? see register) run1: 64 met, 0 failed, 12 measured only.
 eps_eff - eps = -c(a)/beta with beta*diff = -0.65 (a=pi/2) ... -0.87 (a=0.3) ... -0.98 (a=0.05), stable across beta=64,256,1024 to 1e-2.
 So eps_eff < eps (slightly) but eps_eff >= eps - 1/beta on all tested points. Lemma F (eps_eff >= eps - o(1)) numerically supported; NOT proved.
 Convergence J->J+60, Q->2Q: <= 3e-14.
Step 4. Child T132 returned (check K2 child-run1 exit 0, 198 s). Control graded FIRST: 1.762747 = arccosh(3) correct.
 Child eps_eff table equals mine to 10 printed digits (beta=64,256,1024). It used my reduction hint (not independent on the reduction; independent code).
 Child failed predicates: H5 (min eig>0, its own expectation), C3 (expected eps_eff>eps; false: eps_eff<eps in 21/21).
 Grandchild T133 (admitted/released by child): eps_eff(64,pi/2), (64,0.1) by Simpson: 1.75256092, 0.18402420 agree.
 I reran child/eps_eff.py in rerun_child/ (check K4): eps_eff and d identical to all printed digits; only roundoff columns (min eig ~1e-17, symmetry ~1e-16) differ (BLAS nondeterminism). Exit was 0; I had registered expect-exit 1 (my wrong expectation: the child's program exits 0 despite failed predicates) -> register shows mismatch.
 Released T132.
Step 5. kernel_lemma.py: run1 killed (numpy leggauss O(n^3) with 8000 nodes; own defect; no result file). K3 amended to 2000/4000 nodes (documented in docstring). run2 (check K3) exit 1:
 K1 rigorous bound R_lin <= B: 50/50 cases qualify, 50/50 met. K3 met 50/50. K4 met 5/5 (radial form: log R_rad/(p^2/2) = 13.2 at p=0.25: brief's 'needed bound' with d(g) false). K5 met 4/4.
 K2 failed 4/12 (H=1, p<=0.5, beta 1024,4096): my expectation wrong -- the Hessian error is ADDITIVE O(H/sqrt beta), not multiplicative in p^2; not a defect of the lemma.
Step 6. Lean lean/Tunnel.lean (check lean_tunnel): valley_energy_ge and one_sub_cos_ge, exit 0, axioms propext/Classical.choice/Quot.sound, no sorry.
Step 7. TUNNEL_THEOREM.md written. Now verify registers and write report.
Step 8. report.md written. Done.
