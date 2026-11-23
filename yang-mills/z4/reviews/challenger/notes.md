# notes (challenger)

- step0: control.txt = 0.272341 (-ln tanh 1). Read input/README.md, Scaling.lean, FiniteGroupControl.lean. numpy absent; pure python + mpmath.
- step1: wrote challenge.py with predicates Q1-Q6 in docstring (before first run); delegated SU(2) T3 recomputation to child/ (background).
- step2: run K1 (result_challenge_1.txt): met 7 failed 2. Q3 FAILED = my defect (mp.log(1-x) underflows to 0 for x~1e-220 at dps 50; need log1p). Q1d FAILED = my expectation: README's "remainder" is N^2(M-1/2)-1/4, not M-1/2 (my ratios 4.19,4.04,4.01,4.00 for M-1/2). U(1) M(64)=0.500061048820197 matches README. Q2 lattice structure check met (Z5, N=3). Q4 met: Z_n on tuned trajectory beta_N ~ ln N has M=1/2 and finite charge-k levels -> README sec.3 inference defective. Q5 met.
- step3: K2 (challenge_v2.py, result_challenge_2.txt): met 9 failed 0 measured 1. Z_n table reproduced (rel dev <=2.3e-3, 3 sig. digits). Asymptote rel dev at N=16 <=1.7e-49. Q6: U(1)xZ2 product: full lattice gap 1e-3554 at N=64 while U(1) levels -> 1/2.
- step4: Lean K3,K4 exit 0, axioms standard. Child (SU(2)) returned; reran gap.py (K5) and transfer_v2.py (K6): result files byte-identical to child's; M(64)=0.375011444266 confirmed; chi_1/2 eigenvalue (w/w0)^2 on N=2 lattice resid 1e-16. Child report.md not written (tool refusal).
- step5: report.md written. Verdicts: STANDS 10, DEFECT 3 (T2b, T2c, T4b), NOT CHECKED 0. verify: PASS.
