# notes t1-wL
- step0: control.txt = 0.272341; register pcp initialised.
- step1: read TUNNEL_LOWER_FULL, TUNNEL_LOWER, TUNNEL_LOWER2, E13, HARNACK.
- step2: read PATHS, CHAL_parts, CHAL_assembly.
- step3: read TUNNEL_THEOREM sec3-4 (Lemma K, (B)), LEMMA_F header, CHAL_conditional/lemmaF (fixes: sign-trial prefactor 4; Schur Taylor line; LemmaF header).
- findings while planning:
  * FULL sec4: "M^2 >= 2 rho_B^2" does NOT give e^{-1.5rho_B^2}-e^{-M^2} >= e^{-1.5rho_B^2}/2 (needs M^2 >= 1.5rho_B^2+log2). Harmless (c1-condition forces M^2>=14.8).
  * S4-alg corner term c1c2(A1-A2-A3): parts argue qualitatively ("V large, A2~0"); no quantified condition on M. To test numerically (main terms only).
  * M4 constant: "2C(eta)" depends on whether C(eta) bounds the norm or its square; I write C(eta) for the squared weighted norm.
- step4: wrote Section 5 (flux I0,I1,I2 with prefactor 4; GS; Lemma C; P'c; Cor B; remark 1D; L2,L3).
- step5: wrote L4, M4, tangent lemma, ansatz (C2,C3,C6,C7).
- step6: wrote exact algebra, Taylor, Gaussian, tails, Prop E1/E3, E2.
- step7: prog/s4corner.py run1 (K1, exit 0): P1 MET 5/5 eta (S4-alg main-term inequality on support grid; min slack 0.107,0.107,0.095,0.049,0.0100 at eta=0.4..0.01; M^2 at equality = 18.0,30.4,54.4,101.6,475.7 -- note FULL quotes 14.8 at eta=0.4, differs).
  P2 FAILED (writer expectation = target defect): M^2 = 2 rho_B^2 = 0.5 gives e^{-1.5rho^2}-e^{-M^2}=0.081 < 0.344; needed M^2 >= 1.068. Harmless since c1-condition gives M^2>=18.
  P3 MET: min l(K0)/d=8.346 (d=3.645, rho=0.264), l(K_K)/d=9.085.
- step8: wrote S4-alg, norm on tube, Prop subsolution.
- step9: wrote Section 7 (Harnack).
- step10: wrote Section 8 (assembly, chain, Theorem, Corollary).
- step11: tex compiles (only tu:U-* undefined). Child T169 admitted and started (fidelity check), control: int_0^pi sin^2 = 1.570796.
- step12: report.md drafted (child section pending).
- step13: child control graded CORRECT (1.570796 = pi/2) before reading other output.
- step14: child finished (K2 exit 0, 353 s). findings: 0 WRONG, 38 items; unlisted changes 5 harmless; status of L-balls to soften; 9.09 is value at (3.65,0.265) not min.
- step15: reran child fid_check (K3): identical, all MET. Released T169. Applied child findings (I2 hypothesis, L-balls status, 9.09 wording). Recompiled.
- step16: report.md finalised; verify lines quoted.
