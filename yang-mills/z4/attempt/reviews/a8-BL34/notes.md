# notes a8-BL34

- step0: control.txt = 0.272341 (-ln tanh 1). Read PROOF_B_v2.md fully. Lean READY exists. pcp init done.
- step1: wrote child/PROMPT.txt (numerical test of L3b and MC Gaussian limit on N=1 box; control = lambda_min tridiag5 = 2-2cos(pi/6) = 0.267949). Launching child.
- step2: prog1_checks.py: run K1 failed (no scipy; own defect, not target). v2 (closed-form SU(2) exp/log) all pass: lambda_min N=1 0.837722, N=2 0.147122; C_pp(p0) N=1 0.291667, N=2 0.492675; shell H^1(R)=0 & connected N=1,2,3; expansion bounds Q3,Q4 hold on 20001 samples; Q5 holds.
  Observation: PROOF_B_v2 M1 "C^N_pp=0.2917,0.4927 for N=2,4" matches my N=1,2 -> its M1 'N' is side length 2N, not N of R=[-N,N]^4 (labelling inconsistency, harmless).
- step3: L34.lean passes (exit 0; axioms propext, Classical.choice, Quot.sound): one_sub_cos_ge, half_pos_part_sq, norm_add_sq_ge, exp_rem. Earlier attempts failed on two tactic steps (own defects), fixed.
- step4: wrote L3_L4.md (L3, L4 proved modulo 6 standard measure-theory facts not read this run; eta(delta) non-explicit).
- step5: child done (K4 exit 0). Control 0.267949 CORRECT (graded first). Child: lambda 0.837722 C_pp 7/24 (matches prog1), T2 c_eff>=0.1738 >= lambda/16 in 120/120, T3b MC 0.437448+-0.000852 vs 0.4375 at beta=1000. Child P2 trivially true (noted by child). Child failed own expectation (acceptance 5% in t3 run1), retuned. Grandchild: control 2-sqrt2 correct, lambda/C_pp identical. My rerun (K5, scratch copy) of t1, grandchild prog, t3b 1000, t2 1000: bit-identical outputs.
- step6: report.md written; final verify.
