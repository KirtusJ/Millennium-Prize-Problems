# notes r12-lean
- step 0: control.txt = 0.272341 (-ln tanh 1). READY exists. Register pcp initialised.
- step 1: child started early (child-run1, sonnet). Child exit 0.
- step 2: R12Analytic.lean written; predicates P1-P4 in file docstring. First compile EXIT 1: F5 index rewrite (my proof error), F6 two field_simp closures (my proof error). After fixes EXIT 0, all 10 theorems axioms [propext, Classical.choice, Quot.sound].
- step 3: child control 0.008138 = expected (graded before reading rest). Child: F1-F6 0 fails on 1e5 pts, tolerance 8 ulps of operand magnitude. Grandchild: F6 equality point at 50 digits, rel diff 9e-48.
- step 4: register checks K2 lean-compile exit0; K3 no-sorry FAILED (expected exit 1, got 0): the only match is line 7, my own docstring text "No `sorry` in this file" -> defect of my predicate, not of the target. K7 refined check (excluding line 7). Axiom output shows no sorryAx, which is the binding evidence. K4 witness numeric: lhs 1.66583e-3 > 1.6e-3 (b^2/25), <= 1.66667e-3 (b^2/24). K5 child rerun identical; K6 grandchild rerun identical.
- step 5: K7 FAILED, my error (excluded line 7, docstring match is line 6). K8 excludes line 6.
- step 6: report.md written. Verdicts: 10 STANDS, 0 DEFECT, 0 NOT CHECKED. Register 6 met, 2 failed (own predicates).
