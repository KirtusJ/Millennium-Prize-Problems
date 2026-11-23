# notes a2-chalR
step0: control.txt = 0.272341 (-ln tanh 1). Read A1_REDUCTION.md. Register pcp initialised.
step1: child started (A7 free-field computation, control: int_1^inf e^-E = 0.367879). Log child_run.log
step2: families.py run (check K1, exit 0). results_families.txt.
 - F1 (A,B,C hold, atom at E=1 included): R2, R4 bounds, Jensen mean, R3 convergence all MET. Atom at m harmless.
 - F2a (C fails, mu tight): G(2)->e^-1 anyway: (C) not necessary for t>=1 conclusions; tightness suffices.
 - F2b (C fails, mass escapes): G(1)=1, G(t>1)->0: degenerate, not a Laplace transform of a prob measure.
 - F3 (C holds, C+ fails): G_beta(1/4) -> inf while limit G(t)=e^{-(t-1)} continues to e^{3/4}: the t<1/2 limit is not the continuation.
 - F4 (bottom weight 1/xi): limit mu=delta_3: limit gap seen by psi is 3, not 1.
 - F5: subsequence dependence (listed in sec 4 item 6).
 - A3: exact D_j limit = 2^{jp} Gamma(p,2^-j)/Gamma(p,1). Text's e*2^{jp} exact only as j->inf for p=1; overestimates by ~Gamma(p)/(e Gamma(p,1)) for p>1; UNDERestimates for p<1 (p=0.5, j=4: 1.69x). 
 FAILED: P3a (my bound wrong: limit e+sqrt(e)=4.367 > 3, own error), P4a (my predicate used e^-2, correct is e^-3, own error; data = e^-3), P6b (target: e*2^jp not an upper bound for p<1).
step3: child control graded: child/control.txt = 0.367879, correct. Child (sonnet) R(m)=C(xi/2)/C(xi) for psi=phi(0): .4:5.469 .2:6.513 .1:5.739 .05:5.551 .025:5.515 .0125:5.507, Rc=2K1(1/2)/K1(1)=5.503975.
 My independent recomputation freefield.py (graded Gauss-Legendre, check K2): agrees with child to <=3.3e-9 relative at all six m; Q0-Q5 all MET. (C) holds for the free field with D~6.52 (phi) and D~42.4 (phi^2). Row 5 of sec 6 STANDS for (A),(B),(C).
step4: sources (A7). Row1: Guth, Phys Rev D 21 (1980) 2291 (link.aps.org/doi/10.1103/PhysRevD.21.2291), Villain action, Coulomb phase; Fröhlich-Spencer CMP 83 (1982) 411. Confirmed from abstracts only (bibliographic level). Row3: Göpfert-Mack CMP 82 (1982) 545 (projecteuclid euclid.cmp/1103920658): Villain action, all couplings; that the continuum limit is a free massive scalar is stated in a secondary summary found by search, not checked against the original. Wilson-action versions: from memory/not confirmed.
step5: reran child's ratio.py (copy in rerun/, check K3, args 0.1 0.0125): reproduces R(0.1)=5.738552049, R(0.0125) as reported. Grandchild (Bessel/Schwinger representation, m=0.1) in progress; its run1 shows P1 FAIL (Bessel impl 1.5e-2 worst rel vs series) and P2 FAIL at 2.8e-8 (> its own 1e-9 tol); its P5 "0<R<1" is a wrong expectation (R>1 always since C decreasing).
step6: analysis of proof lines done (see report). Writing report.md.
step7: report.md written. K4 (grandchild rerun) and K5 (child-run1) timed out; registers verify PASS. Verdict: STANDS 16 / DEFECT 8 / NOT CHECKED 1.
