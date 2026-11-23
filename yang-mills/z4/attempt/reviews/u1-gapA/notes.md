# notes u1-gapA
- step0: control.txt = 0.272341 (-ln tanh 1). Lean READY exists.
- step1: admitted child T175 (child_admit.log); child/PROMPT.txt written (grid check of A1-A4,B1-B3,C1,D1-D2; control: int_0^1 e^{-x^2} = 0.746824).
- child control known answer sqrt(pi)/2*erf(1)=0.746824
- step2: prog/w1w3.py -> results/w1w3.txt, exit 0, P1-P3,P5-P12 met for all eta in {.5,.2,.05,.01}, tau in {.5,.1,.02}.
  max|g'|/(3/sqrt(2eta)) = 0.665; max|ft''|/(6/sqrt(eta)+3L/tau) <= 0.90.
  DISCREPANCY (own defect): docstring P4 tolerance 1e-12, code used 1e-5; measured jumps up to 1.9e-10 (eta=0.01).
  Against the docstring tolerance P4 FAILED for eta=0.05,0.01 (own expectation: one-sided values evaluated at offset 1e-13/1e-12
  are O(offset/eta) or rounding, not 0). C^1 of g is proved analytically (Sm'(0)=Sm'(1)=0); the numeric is secondary.
- Gap 3 finding: h(S)=1+sqrt(1+1/S^2) is a function of sigma=S^2; dh/dsigma = -1/(2 sigma^2 sqrt(1+1/sigma)), decreasing in |.|,
  so MVT gives exactly the stated Delta h bound with sigma_- = S^2 - DeltaS^2 a lower bound for S'^2. Stated bound is CORRECT
  (not dimensionally wrong: sigma is S^2). Explicit: r_b <= S/8 => Delta h <= 4 r_b/S^2 + 4 sqrt2 r_b^2/S^3 <= 5 r_b/S^2.
- Gap 4 finding: exact closed form gap = 1/2 log(1-x) + 1/2 log(1+h x) + h x |b|^2/D_w + h(kappa^2/beta - 2kappa/sqrt beta)|b|^2/D_w,
  x=4hW/A, D_w = 1+2h sigma_w^2 = A(1-x), W=|b|^2/beta.  Hence DG1', DG3' with D_w>=1; stated DG1, DG3 follow.
- step3: lean/GapA.lean (9 lemmas: smoothstep bounds, -1/2log(1-x)<=x/(2(1-x)), 1/2log(1+y)<=y/2, log(1-x)<=0, cross term h/(1+2hs)<=1/(2s),
  det factor, coeff diff, flat identity, delta_h (no MVT)) -> exit 0, axioms propext/Classical.choice/Quot.sound only, no sorry. (check K4)
- step4: patch_upper.py applied -> note/tun_upper_patched.tex (new Lemma tu:U-W13; W1 weakened to C^1 of sqrt rho)
- step5: child T175 run (check K2, exit 0, 103 s). Control graded FIRST: 0.746824 = sqrt(pi)/2 erf(1) -> correct.
  Child reports A1-A4,B1-B3,C1,D1,D2 all met, 0 failed. Grandchild T176 (admitted+released in graph, events seen) recomputed c*, c_rho(0.05).
  I reread child/gridcheck.py (predicates match prompt; analytic g', ftilde''), reran it in child_rerun/ (check K5): results.json byte-identical.
  Child's c_rho values equal mine (2.667426, 3.947568, 4.456390, 4.577243). Released T175.
- step6: patch_lower.py applied -> note/tun_lower_patched.tex (Delta h derivation + explicit 5 r_b/S^2; exact gap formula + DG1',DG3'; Err explicit constant in Prop E13)
- step7: err_const.py (K6) E1-E6 met, 0 failed (max ratio E6 0.86). pdflatex wrapper build/wrap_patched.tex: 29 pages, exit 0, no undefined refs (orig 26 pages).
- step8: overfull fixes; final compile K8 exit 0 (29 overfull vs 28 in original, cosmetic). verify run.
- step9: GAPS.md and report.md written. Done.
