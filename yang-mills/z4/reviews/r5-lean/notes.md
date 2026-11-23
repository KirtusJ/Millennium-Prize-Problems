# notes r5-lean (formalizer, S5)
- step 0: control.txt = 0.272341 (-ln tanh 1).
- step 1: read S5. Hand analysis: (a) uses x e^{-x} <= e^{-1} at x=tau E (true for all real x); (b) x^2 e^{-x} <= 4e^{-2} needs x>=0; (c) CS; (d) needs tau>=0 only, E0>0 unused; (e) V>0, v<=V and E0>0 follow from C(tau)>=C(2tau)>=v>0 (uses E_i>=0, tau>0).
- step 2: delegated numerics to child/ (background). PCP register initialised.
- step 3: S5.lean first compile: all theorems except S5e pass; S5e had a commutativity goal after field_simp (my proof defect, fixed with ring).
- step 4: S5.lean exit 0, axioms clean. Mutations a (1/(2e tau)) and b (3) rejected: exit 1, 'unsolved goals' at the theorem, sorryAx in axioms. PCP K1-K3 as expected.
- step 5: child numerics reread and rerun (K4): identical table, 0 failures; results_2.txt identical to child's results.txt.
- step 6: verify PASS; report.md written.
