# Z4 challenger notes on B4 heat-trace (r6-heat)
Step 0: control.txt = 0.272341 (-ln tanh 1).
Step 1: read all seven input files (README, wilson-law, rare-cubes, positive-time, hamiltonian, representations, execution).
Step 2: read-through findings (draft): upper bound arithmetic in wilson-law reproduces (5m^2+65536B) exactly; lower bound cost 5 x^{3/5}L^{2/5}; positive-time Cauchy-Schwarz step correct; spectral threshold x^eta/a exceeds cutoff 1/a by x^eta.
Step 3: delegated toy (exact optimization + 1D trap survival exponent 1/3) to child/ (background).
Step 4: check_constants.py run via PCP (K1, exit 0): P1-P9 all met, M1/M2 measured. results_constants_1.txt.
  M1: on beta=log(1/b), s=V=1 the stated upper bound on E F_s is vacuous (c x^{3/5} < log 2^{3.5}) for b>=1e-3; at b=1e-50 window for the ratio is [0.549, 0.619]; convergence ~ log(1/c)/log x. Asymptotic only.
Step 5: check_cube.py via PCP (K2, exit 0): Q1 small-cube r_p^2-coercivity met on 3000/3000 (min lam/r_p^2=0.041 vs 1/256); Q2 near-flat Dirichlet trial bound met 600/600 (lam <= 0.32 of bound).
Step 6: H-analysis drafted (see report). Key items: (i) 3/5 needs B=x^{o(1)} on lower side; upper side only needs B<=x^{2/5}; for B=x^gamma window is [min(3/5,1-gamma), (3+2gamma)/5]. (ii) positive-time bound uniform in j>=1, so covers fixed physical separation too. (iii) threshold x^eta/a = s^eta b^{-1-2eta} is above the cutoff 1/a. (iv) README says 'simple' group, representations.md says 'compact connected Lie group'; general-G 3/5 only sketched. (v) Notation clashes F_t / U_t / V / kappa_B.
Step 7: child returned; reran toy via my register K3 (exit 1 expected 1): A1,A2,B0 met, B1 failed (0.39376 vs 1/3, tol .06), A3 measured; A3 at k=300 (0.582931) matches my independent M1 (0.5829).
Step 8: report.md written.
