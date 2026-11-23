# notes u1-gapB (T174)
- step0: control.txt = -ln(tanh 1) = 0.272341. Lean READY exists.
- step1: register init (method not found, expected); child admit: ADMITTED T177
- step2: child T177 admitted, PROMPT written (control: c* integral = 4.6054132; checks N1,N2,N3), child-run1 started in background.
- step3 (analysis, gap A): with x=c1/G, y=c2/E, k=sqrt(1+S^2)/S: G=exp(-kV/2) exactly, so (A2/A1)x = P x^gamma with
  P=exp(e(S)-M^2/k), gamma=1-1/k. Needed (Delta=0): F=a(1-x)(1-y)+P x^gamma + b y <= 1, a=lambda/A1<=e^{-3eta/4}, b=e^{-t}, t=Theta'(a2)^2/2.
  F linear in y => max at y=0 or y=1. y=1 only reachable (beyond y_beta->0) when a2>=l, where t>=theta0^2/4=1/16.
  y=0 slice: weighted AM-GM P x^g <= g a1 x + (1/k)P^k a1^{1-k}, a1=e^{-3eta/4} => F(x,0)<=1-m0 if M^2>=k e+(k-1)3eta/4+log(1/(k m0)).
  y=1 slice: F<=P+e^{-1/16}<=1-m1 if P<=m1=(1-e^{-1/16})/2, i.e. M^2>=k(e+log 1/m1). Corner forces M^2 ~ 3.5/eta (k<=coth eta).
  Margin m=min(m0,m1) ~ 3eta/8 for eta<=1/12: proportional to eta, necessarily (at x=y=0,a2=0 slack=1-e^{-eta}).
- gap B analysis: g>=phi holds on all X (Prop sub), phi=mu e^{-sqrt(b) min(Psi(a1),Psi(pi-a1))}(G-c1)+(E-c2)+ everywhere (not only on Omega);
  so every point of a valley ball is covered by the subsolution irrespective of a1; step-1/3 ball points by H4 pointwise. Case split must be by ball type.
- gap C: note's c1 formula gives M^2(0.4)=18.05 (writer right, FULL's 14.8 wrong); eta*M^2 -> sqrt2(e(sqrt2)+1)=4.656 as eta->0 (FULL's 3.4/eta wrong for c1 cond).
- step4: check_gaps.py run (register K2) exit 0, all P1-P7 met; minimal M^2 on physical grid ~2.75/eta (measured). child control.txt = 4.605413: CORRECT (c*=4.6054132).
- step5: child T177 released. Child report: N1,N2,N3 hold on grid; its slacks equal mine (7.5269e-3 @0.4, 2.3872e-3 @0.1, 3.7360e-3 @0.01). Grandchild T178 (MA2,Mc2 recompute) matched.
  I reran child/grid.py under my register (child_grid_rerun, exit 0).
- step6: Lean corner.lean (amgm_step, corner, strip, absorb, sq_step): exit 0, axioms propext/Classical.choice/Quot.sound only. No sorry.
- step7: wrote note/tun_lower_patched.tex (S4-alg replaced, Lemma balls replaced, assembly bullet/beta0/remark, statuses)
- step8: pdflatex wrapper (upper + lower_patched) exit 0 twice, 0 undefined refs, 28 overfull boxes = same count as original. Registered as pdflatex_patched.
- step9: GAPS.md and report.md written; verify PASS (both). Done.
