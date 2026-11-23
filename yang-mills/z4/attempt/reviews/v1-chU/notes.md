# notes v1-chU (referee, tun_upper.tex)
- step0: control.txt = 0.272341 (-ln tanh 1). Lean READY exists.
- step1: register pcp initialised; child admitted (see below).
- step2: child task T181; child/PROMPT.txt written (numerics of 12 scalar items). Launching.
- step3: child run finished exit 0 (register event child-run1). Control graded FIRST: 9.000000 and 1.762747 = correct. Child released T181.
  Child claims 11 MET, 0 FAILED, 1 MEASURED ONLY; item 12: beta-threshold for deficit<0.2 is 2.03e13 (note: ~2.2e13), deficit range on beta<=4096 is 7.33..14.23 for beta in [100,4096] (note: 8.6..14). Grandchild T184 (item 5 boundary). To be rerun by me.
- step4: referee pass through all of tun_upper.tex done in head; findings being written to findings below.
- step5: prog1_fibre.py written (predicates P1-P5 in docstring); running as pcp check prog1.
- step6: prog1 run1 (res_prog1_run1.txt): P1 18/0 (Nystrom vs Legendre-matrix eps_eff agree <=2.5e-10), P1c 18/0, P2 18/0, P3 12/0 (6 not qualifying, b=64<=125), P4 16/2 FAILED at b=64,a=0.05 (1.038 vs 0.98) and a=0.1 (0.980 vs 0.95): defect of the TARGET's measured Remark tu:U-R-rem ("same at 64,256,1024 within 2%") -- harmless, remark unused. P5: s=0.1 met (-4.06e-4 in claimed range); s=0.3,0.6,1.0 NaN = OWN program defect (exp overflow). Fixed in prog1b (log-space).
- step7: prog2 run1 exit 1 (OWN defect: math.exp overflow in Lemma K RHS at b=16384,H=18); W-section results stand in res_prog2_run1.txt: W1..W7 9/9 each met, glue 9/9. prog2b = same predicates, log-space for K/KR.
- step8: prog2b run1 exit 1 (OWN defect: omega computed with math.exp overflow; at b=4096 omega ~ +2800 nats, i.e. Remark K bound is VACUOUS there, not false). run2: omega in log space, b in {4096,16384,1e6,1e8}. K: worst log(lhs/rhs)=-0.0139 (0 fail), KR worst ratio 0.982.
- step9: prog2b run2 exit 0: W1-W7 9/9 each, K 180/0 (12 not qualifying beta'<=0), KR 36/0, S 480/0 (omega=2820,5417,32070 nats at b=4096,16384,1e6: vacuous; omega=0.0062 at 1e8; measured log w - Phi'^2/2 <= 0.0127,0.0033,5e-5,~0), MC1-MC6 all met.
- step10: prog1b exit 0: P5a 4/0, P5 4/0 (s=1: -1.951e-4, inside claim only by my +-1e-5 rounding allowance), P5c 4/0. Lean referee_scalar.lean exit 0, axioms propext/Classical.choice/Quot.sound only (outer Taylor core, Prop B exponent steps, e^{1/8}<=2).
- step11: report.md written; final verify quoted. Verdicts 31 STANDS / 3 DEFECT / 0 GAP / 0 NOT CHECKED.
