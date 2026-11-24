# notes f2-lean (T238)
- step 0: control.txt = 0.272341 (-ln tanh 1). Lean READY present.
- step 1: read target/inheritance.md, Checks.lean, inheritance_ungated.md. Register pcp initialised. Child admitted as T240 (f2-lean-child, parent T238); child started in background (numerical test of L2 indexing).
- math plan: x(1-x^r)<=r(1-x) for all real r>=0 via 1-e^{-ry}<=ry and y e^{-y}<=1-e^{-y}.
  BSB step at vector level: c||EBv||^2 <= <Bv,S Bv> <= kappa||Bv||^2 and ||EBv|| >= ||Bv||^2 (unit v, Ev=v) gives c||Bv||^2<=kappa (Bv!=0) -- no ||BE|| needed.
- step 2: numtest.py (seed 20261124) recorded as check 'numtest': N1 0 fail /200000; N2 0 fail; N3 (L2, M_{i-1}) 0 fail /20000, min slack -3.3e-16 (equality cases, rounding), variant M_i fails 634 (expected; when K_i<1); N4 finite-dim operator instances 1863 qualifying, 0 fail.
- step 3: author's Checks.lean rerun (check K2) exit 0, axioms propext/Classical.choice/Quot.sound for all 5. Contents: gated_deficit = final scalar step AFTER linearisation (b<=d+rd/g+k => (b-k)g<=d(g+r)); weighted_step = one multiplied step of accumulation (no telescoping, no induction); rare_suppression, sum_weighted_rows, gaussian_floor = other files' arithmetic. NOT in it: x(1-x^r)<=r(1-x), telescoped accumulation, any operator step.
- step 4: rpow inequality x(1-x^r)<=r(1-x) for real r>=0 compiles (lean/T1.lean scratch). Writing Inheritance.lean.
- step 5: Inheritance.lean v1 compiles exit 0, 17 decls, axioms only propext/Classical.choice/Quot.sound. Adding composed norm-form corollary.
- step 6: added gated_main_norm; full file exit 0 recorded as check 'inheritance-lean'; axioms_printout.txt = 18 lines all [propext, Classical.choice, Quot.sound]; grep sorry = 0.
- step 7: child (T240) finished in 57 s (check K3 exit 0). Control graded first: child/control.txt = 5, correct. Child: C (M_{i-1}) holds 4000/4000 exact, equality 506/506; C' (M_i) holds when K>=1 (weaker); C'' (M_{i-2}) false, 495 fails. Grandchild T241: n=2 exact case d2=13/300=RHS(C), RHS(C'')=4/75 fails; grandchild control 5 correct. I reread both scripts, reran copies under child_rerun/ (checks K5, K6), outputs byte-identical. Hand check of n=2: d1=.19, d2=.13/3=13/300 = (0.5-.12-2*.06)/6. T240 released (event 486); T241 admitted+released by child (events 480/481).
- step 8: report.md written; verify PASS (python) and rust verify pass line quoted.
