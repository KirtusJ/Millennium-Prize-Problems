# notes.md (r11-flow, builder)
- Step 0: control.txt = 0.272341 (-ln tanh 1). Read inputs. PCP register pcp initialised.
- Step 1: B4 delegated to sub-agent (child/); it returned all 5 predicates met (claim, to rerun). Lean try1 compiled (see lean_try1.log). flow_bench.py written, predicates P0a-P7 fixed in docstring before first run.
- Step 2: flow_bench run1 (K1): 76 met, 1 failed (P5 s=0.01: lattice <B^2> 3.1% below 1/(48pi^2 s^2); my tolerance assumed exp-small images, wrong: massless kernel has power tail). Wrote flow_box.py to test the finite-volume explanation. Lean try1 failed (push_neg changed filter predicate); fixed.
- Step 3: Lean try2 exit 0, axioms standard (lean_try2.log). flow_box (K2): Q1 met (lattice Richardson = continuum box sum to <=1.8e-4 all s), Q2 FAILED (fv coef 271,283,310: spread 12.6% > 10%; own expectation, higher order in s). P5 failure = finite volume, not a lattice defect.
- Step 4: child program reread (staple, P_ah, RK3 coefficients correct) and rerun in rerun_child/ via my register (K3): exit 0, results_run1.json byte-identical.
- Step 5: wrote flow_proof.md and flow_structure.md. Next: verify, report.md.
- Step 6: PCP verify PASS; report.md written. Counts 87 met, 2 failed, 4 measured only.
