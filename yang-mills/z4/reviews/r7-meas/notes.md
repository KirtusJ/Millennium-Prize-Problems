# notes r7-meas (formalizer, measure lift of S5)

- step 0: control.txt = 0.272341 (-ln tanh 1). PCP register pcp initialised.
- step 1: MeasureHeat.lean first compile (4 min per compile!): M2_tail OK (std axioms); M2_window failed (linarith: C not unfolded in hypothesis, my slip); C_sub_P0 failed (this Mathlib writes integral_indicator_const with ν.real, my slip). Fixing.
- delegated M6 (Hölder/Cauchy-Schwarz route) to child/ in background; I prove M6 myself by the AM-GM quadratic-form route.
- step 2: full compile: 9 of 11 printed theorems standard axioms; M6 failed (Pi.add form of integral_add, my slip), M3 failed (field_simp left a ring goal, my slip). Fixed. Mutant copies made in mutants/.
- child returned: M6_child via integral_mul_le_Lp_mul_Lq_of_nonneg, claims exit 0 + std axioms + verify PASS. To be recompiled by me.
- step 3: K1 MeasureHeat.lean exit 0, all 11 printed theorems std axioms, no sorry (only occurrence of the word is in the header comment).
- step 4: K2 child recompile exit 0 std axioms; K3-K5 mutants all rejected (exit 1); K6 mutcheck 5 met. e->2 mutant is TRUE (rejection = proof brittleness only).
- step 5: report.md written; verify PASS.
