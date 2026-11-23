# notes a3-C
- step0: control.txt = 0.272341 (-ln tanh 1). Read A1_REDUCTION, SPATIAL_FLOW, LIT_RIGOROUS ten facts.
- step1: K1(1)=0.601907, K1(0.5)=1.656441 (trapezoid, h=1e-3, own one-liner); continuum free 4D ratio 2K1(1/2)/K1(1)=5.503975, squared 30.293739. Child control = K1(1) to 6 decimals, answer 0.601907.
- step2: wrote test_c.py (predicates P1-P8 in docstring), child launched at 12:00
- step3: test_c.py res1: P1,P2,P3,P4 MET; P5,P6,P7 FAILED -- own expectation defect: atom weights mis-chosen (w=e^{-xi/2}, m^4, e^{-2xi} are too large; atom dominates at n=xi and R -> const). Lesson: a hole alone does not violate (C); the bottom weight must be exponentially small, w << e^{-eps_h xi/2} x (weight above). Corrected families in test_c2.py (new predicates, originals kept).
  Free lattice-local phi(0): R1(256)=5.504244 vs continuum 5.503975. phi^2: 30.2967 vs 30.2937. (C') fails for lattice-local (xi(1-C1/C0) ~ 0.96 xi). Flowed s=0.1: xi(1-C1/C0) -> 4.78, R -> 7.095 <= bound 11.16.
- step4: child control 0.601907 CORRECT (graded first). Child R1 (k-space Gauss-Legendre) agrees with my Schwinger R1 to <1e-6 at xi=16..128; child r1.py rerun under my register (child-r1-rerun): bytes identical. Grandchild Schwinger xi=16: 5.5796296 (its P2 tolerance failed marginally, own quadrature).
- step5: test_c2: Q1,Q2,Q5 MET; Q4 FAILED (own expectation: polynomial bottom weight m^4 gives R bounded asymptotically (->e^{1/2}) but sup is 151 at xi=256, not <=5); Q3 crashed at xi=256 (exp underflow, own defect) after 6/6 earlier cases qualified; test_c3 recomputes in log space.
- step6: Lean lean/A3C.lean exit 0, axioms propext/Classical.choice/Quot.sound. res2 identical to res1 at printed digits. PROOF.md written 12:04.
- step7: report.md written 12:05; registers verified (Python PASS, Rust pass).
