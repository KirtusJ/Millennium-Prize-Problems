# notes m1-wild (T128)
- step0: control.txt = 0.272341 (-ln tanh 1). PCP register pcp/ initialised.
- step1: surveyed README, THEOREM_B, main.tex, sec_reduction (Thm R', hyp A/B/C), sec_smallbox; spot-checked by hand: h_k scaling h=beta^-1/3, constant-mode H=(beta L^3)^-1/3 h_3, 4^{1/3} normalisation, e'=4^{-1/3}e, Wick-inequality with constant background (needs G(n)>0), G(0)=1/2 from P_{12,12}=(k1^2+k2^2)/k^2. All consistent.
- step2: child admitted T130; child/PROMPT.txt = G(n) check (G(0)=1/2, G(n)>0 n<=8, pi^2 n^4 G -> 1); control: int x^2 = 0.333333. launched in background.
- step3: wrote h2spec.py (third-method Rayleigh-Ritz of h_2, Legendre x HO radial basis); scipy absent -> numpy dense per l-parity. Smoke: (14,12) w=1.6 gives 3.350533, 5.3255(doublet), 5.725432 nondeg.
- step4: h2spec-run1 (K2): all 6 predicates met; e0=3.35053304, e1=e2=5.32549702, first charge-0 excited 5.72540816 (scalar gap 2.37487512, not in paper), gap 1.97496398. Converged to 8e-7 between (22,18) and (28,22).
- step5: child T130 control 0.333333 CORRECT. Child: G(0)=0.5, G(1)=0.068874745841,...,G(8)=2.70232e-5, pi^2 n^4 G(8)=1.0924; grandchild T131 G(1) Schwinger agrees 1e-12. Reran child g130.py in child_rerun/ (K3): numbers identical. Released T130.
- step6: report.md written; verifies PASS (python, rust).
