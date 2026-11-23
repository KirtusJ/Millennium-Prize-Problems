# notes a8-chalB2
step0: control -ln(tanh 1)=0.272341 written; register init.
step1: child launched (A4 delegated)
step2: read PROOF_B_v2.md. Line-by-line pass (paper):
 - Lemma 2: index check a=-2^i+1, theta_a maps t->2a-1-t; site plane x_j=a; S subset H+ ok incl. last step i=k-1. Images of p0: x3,x4 even -> |Lambda|/4 distinct, hit 4x; exponent 1/2*1/4=1/8. Paper check: consistent.
 - Lemma 3: zhat bound (pi/2)^{5/2} b^{-3/2} re-derived; lower bound 3L^4+L^3 free links, alpha_p<=4s, 1-cos<=8s^2, energy<=48|Lambda|; (9/2)log beta cancels; uses only beta>=1. Paper check consistent.
 - Lemma R: Wick-with-background formula re-derived: Cov=(3/2)G^2+G E|f|^2+1/4 Var|f|^2 needs f_{p0}=f_{pn} (constant background). Load-bearing: constancy of h.
 - Lemma G: lower bound gives only n^-5 => c(n)>=n^-10 (true decay n^-4 => n^-8); weaker but valid.
 - T self-adjoint contraction; 'even n' not needed (site-RP gives self-adjoint T, T^2>=0; bound |<psi,T^n psi>|<=||T||^n holds all n).
step3: chess2d run (2D exact U1/SU2 L=2,4): see chess2d_results.txt
step4: chess2d 100/100 met (76 nontrivial t<2beta, 24 trivial P=0). Child control.txt=1.0 graded CORRECT.
step5: child report read; child/pcp verify PASS; child G(0)=0.5, G(1)=0.0688747, p(8..16)=4.09, grandchild G(1) 4D direct agrees 4e-10. Child used rm -f before rerun in its instructions (contrary to mode-x spirit) - noted.
step6: lemmaGD run K3 FAILED exit 1: scipy not installed (my program's defect, not target's). Replacing scipy with numpy CG / dense eig.
step7: run2 K4 exit 1: KeyError p1 not in box N=1 (my defect). G part completed: G(0)=0.5, G(n)>0, p=4.094, matches child to 1e-7. Rerun writes lemmaGD_results_run3.txt.
step8: run3 K5 exit 1, one FAILED predicate D1b: file's M1 values 0.2917/0.4927/0.4992 labelled N=2,4,6 equal my box [-N,N]^4 values at N=1,2,3 (0.29167,0.49267,0.49916); file's C^6(p0,p1)=0.0681 = my N=3 0.06811. => target's test labels off by factor 2 (target defect, reporting only; math of Lemma D unaffected). All else met: G1-G5, D1a, D2, H1 s=3..6, D*=60.1922, zhat/haar bounds, R1 80 cases. R2: anti-correlated background gives negative ratio -> constancy of h in Lemma R is load-bearing. D_L at finite L exceeds D* by O(log beta / L) (measured) - fine since corollary is stated only for limit states.
step9: reran child g.py in rerun_child/ (K6 exit 0): identical to child's file; agrees with my lemmaGD G(n) to 4.8e-8 (my print rounding). Grandchild G(1)=0.0688747462 4D direct consistent.
step10: report.md written. Verdicts STANDS 12, DEFECT 2, NOT CHECKED 2.
