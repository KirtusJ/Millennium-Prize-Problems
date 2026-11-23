# notes g2-conv (T77)
Step 0: control.txt = 0.272341 (-ln tanh 1, python). Read NUMERICS.md, TORON_GAP.md.
Step 1: register init (pcp/). Child control answer computed first: -ln(I_3(16)/I_1(16)) = see below.
Child control answer (mine, power series 4000 terms): -ln(I_3(16)/I_1(16)) = 0.257416
Step 2: child T82 admitted under T77; PROMPT.txt written (Q: coercivity Lambda(beta,c1) of 1-K+V-c1 D; control -ln(I3(16)/I1(16))=0.257416)
Step 3: checks.py run1 (K1) exit 1: own defect (json.dumps of numpy bools crashed after writing results/checks.json; all predicates in the file are met). Fixed print, run2 -> results/checks2.json.
  Citation for Bessel-ratio bounds: Ruiz-Antolin & Segura, arXiv:1606.02008 (2016), Theorem 2 (b_0 upper, nu>=1/2; b_1 lower, nu>=0) for I_nu/I_{nu-1}; read via a fetch sub-agent from arXiv HTML; Amos 1974 only in bibliography.
Step 4: Lean scalar.lean exit 0, axioms propext/Classical.choice/Quot.sound only (F1-F6).
Step 5: child control.txt = 0.257416 == mine 0.257416: CORRECT (graded before reading the rest).
Step 6: child report read; T82 released; grandchild T85 (admitted+released by child, seen in graph). Child P1 FAILED (beta^{1/3}Lambda(c1=1) = -2.39 @16, -3.35 @64, not converged downward).
Step 7: reran child lam.py check/main in rerun_child/ (K4,K5, exit 0): identical numbers. Diagnosis of child P1 failure: 1-K<=1 caps kinetic; localized high-spin state at a1=a2=pi/2, common axis gives H-D <~ -1; my predicate's expectation was wrong; correct coercivity is capped (L4/L5).
Step 8: SCALING_LIMIT.md written (limsup PROVED; liminf CLAIMED with L4 capped fibre lemma PROVED, L6/L7 sketch). Statement defect: unnormalized K adds c(beta)~3 ln beta.
