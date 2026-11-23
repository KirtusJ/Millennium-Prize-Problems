# notes y1-rect (T194)
- step0: control.txt = 0.272341 (-ln tanh 1). Lean READY exists (not planned to use).
- step1: located the sign use: target/isotropic-variance/README.md "Integrating every plaquette": j_e >= 2^-22 beta^2|A|^2/(1+k)^2, E|A|^2 = 2+2E(a+.a-) >= 2, a+.a- = half-trace of 1x2 rectangle (long side along y, normal to reflection plane), proved by site reflection in plane {y=y0} containing selected x-link. Also referenced in coarse-plaquette-floor/README.md "Cross-check on the auditor's checkerboard": R=E(a+.a-)>=0 used for (1+R cos q_y)>=1 on a half band.
- step2: child admitted T197 (parent T194); child/PROMPT.txt written (MC of W11,W12 4^4, control 1/(H_4)=0.480000). Launching.
- step3: analytic.py run1 (K1, exit 0) -> results/analytic_run1.txt. All predicates A1-A8 met.
  * R'(k)=1-3R/k-R^2 confirmed (FD err 3e-11). R' <= R/k on grid, so j_e >= beta^2 R'(k)|A|^2 exactly.
  * c1 = inf (1+k)^2 m(k) = 1/4 (at k=0) vs target lemma 2^-22: lemma TRUE but 1e6 weak.
  * c2 = inf_{k} max(1,k/6)^2 m(k) = 0.036886 at k=6 (beta=1,|H|=6); asymptote 1/24. Improved floor J >= c2 (1+R) >= 0.0369 vs target 2^-22/49=4.9e-9. Numerical grid [0,2000] + asymptotics; not a proof.
  * Reflection combinatorics (L=4,6): theta(a+)=a- as oriented paths, rectangle excludes common link, no plaquette straddles open halves, plane links fixed. Checkerboard: each xy face exactly one selected link.
  * strong coupling u(beta)=I2/I1: 0.5->0.123718, 1->0.240194, 2->0.433127, 2.3->0.479279, 3.4->0.608359.
  * weak coupling LO: 1-W11 = 3/(4beta), 1-W12 = r*3/(4beta), r = 8[G0-G11]+4[G0-G20] = 1.72450.
- step4: mc.py written; smoke test (scratch) found my diagnostic bug (unitarity summed over wrong axis) -> fixed before production; heatbath orientation U=W conj(V) checked by reasoning.
- step5: child control graded BEFORE reading anything else: child/control.txt = 0.480000, correct (1/(25/12)=0.48).
- step6: literature: web search did not surface OS 1978 text; cited by locator only (Osterwalder-Seiler, Ann. Phys. 110 (1978) 440, not read here). Site-reflection argument re-derived myself; combinatorial core checked in A7.
- step7 analysis: J in [c, 2K] => Var M = chi - J bounded uniformly IFF chi bounded: decomposition relocates, does not reduce, the open problem. RP sign used only unconditionally; a coarse-conditional R (random coarse coefficients) is NOT given by RP.
- step8: own MC L=4 beta 0.5,1,2 done, all predicates met; agree with child's L4 numbers within 1 sigma (W12 0.5: 0.015316(111) vs child 0.015509(182); 1: 0.058965(140) vs 0.059081(197); 2: 0.259599(313) vs 0.259598(604)).
- step9: all own MC done (L4 x5, L6 x3), all predicates met. Child returned (K5 exit 0), T197 released. Child report reread; rerun of child L4 b2.3 seed 23 reproduced bit-identical (K11). Grandchild T198 (beta=0, 2^4 beta=0.5) read, not rerun.
- step10: registers verified (python PASS, rust pass); report.md written.
