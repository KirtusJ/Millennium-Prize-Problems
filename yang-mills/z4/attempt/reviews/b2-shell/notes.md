# notes b2-shell
- step0: control.txt = 0.272341; Lean READY exists. register pcp initialised.
- step1: child admitted T218 (parent T215), PROMPT.txt written (question (i): brute-force shell weights 3D/2D; control sum k^2 k=1..10 = 385). launched in background via pcp check child-run1.
- step2: wrote shell_audit.py with predicates P1..P6 in docstring (before first run).
- step3: run1 (pcp check shell-audit-run1, exit 1 expected 0). All predicates P1..P6 met EXCEPT "P6 W quadratic growth": W(512)/W(256)=3.97701, my tolerance |ratio-4|<0.01 too tight. This is MY expectation defect (O(1/N) correction), not the target's: W/N^2 = .015204,.013691,.013060,.012763,.012617,.012544 decreasing with halving differences -> positive limit. Follow-up program p6b.py with limit L=(1/3)int_0^{1/2} u^2 cosh(u-1/2)/cosh(1/2) du.
  Key numbers: 3D/2D weights exact for m=1..12 (78+78 cases); sharpness ratio 7.996 at m=4^10; min W/I = 0.250 >> 1/(48e)=0.00766; chi(16)=4.329314, chi(512)=4.327908, 2coth(1/2)=4.3279068275 = 2tanh(1/2)coth^2(1/2) identically.
- step4: wrote p6b.py (predicates Q1,Q2 in docstring).
- step5: p6b run1 exit 0: L=0.012471810183, err*N -> 0.037 (O(1/N)); W ~ L N^2 quadratic confirmed. Claim 6 STANDS.
- step6: child control 385 graded CORRECT before reading output. Child report: d=3 and d=2 STAND, 156 met 0 failed; own failed P2 (its expectation). Grandchild T219 (m=1,2 hand list 7/3, 26/3, 37/3; control 56 correct), admitted and released by child. Reran child/shell_check.py in my register (K4): 156 ok 0 false. Released T218.
- step7: verify PASS (both). report.md written. Verdicts 6 STANDS / 0 DEFECT / 0 NOT CHECKED.
