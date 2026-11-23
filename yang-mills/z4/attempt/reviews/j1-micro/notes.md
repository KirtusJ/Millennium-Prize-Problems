# notes j1-micro
step0: control.txt = 0.272341 (-ln tanh 1). register pcp initialised.
step1: child admitted as T110; PROMPT.txt written (arithmetic Q1-Q14, control sum 1/n^2 = 1.644934).
step2: child control graded 1.644934 = pi^2/6 CORRECT. child-run1 K1 exit 0 78.5s. records read (9 reports + SCALING_LIMIT + LIMINF).
step3: arith.py run K2 (expect-exit 1, declared before run): met 14, failed 4 (P11 12%, P12 'five orders', P14 E-T2 zero from 1024, P18 m_oo 2.00000) - all four defects of the target text, not of my expectation of the arithmetic.
step4: child recompute.py reread and rerun in child_rerun/ (K3): results.json identical to child's. Child Q1-Q13 agree with my P1-P10; Q14 agrees with my P11.
step5: findings compiled; writing report.md
step6: report.md written. WRONG 5, OVERSTATED 12, MATCHES 46, not checkable 19.
