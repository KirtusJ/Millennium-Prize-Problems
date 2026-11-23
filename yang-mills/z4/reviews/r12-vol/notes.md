# notes r12-vol
step0: control.txt = 0.272341 (-ln tanh 1). Lean READY exists. register pcp initialised.
step1: child/PROMPT.txt written (l=1,N=48,s=0.005, product periodized Gaussian center 0.3 width 0.15); launching child-run1 in background
step2 (proof route, t=0). Pair bound: u=p+q/2, w=q/2-p, g(v)=|v_perp|^2/(2|v|).
 |u||w| <= |p|^2+|q|^2/4 ; |u_perp|^2|w_perp|^2 >= (|p_perp|^2-|q_perp|^2/4)^2 >= |p_perp|^4 - |p_perp|^2 |q|^2/2
 => 4 g(u) g(w) >= |p_perp|^4/|p|^2 - (3/4)|q|^2 >= p1^2+p2^2-p3^2 - (3/4)|q|^2  (x^2/(x+y) >= x-y)
 gaussians: e^{-2s(|u|^2+|w|^2)} = e^{-4s p^2} e^{-s q^2}. SECOND ORDER in q (first try with (|p|+|q|/2)^2 gave a first-order error 4.5*eta: vacuous; discarded).
 lattice: for |k|_inf<=K: a(k) >= (1-eps)^2 phi(k), eps=K^2 b^2/24 (sin y >= y-y^3/6, khat<=|k|).
 => G(q) >= A - B'|q|^2 for all q in BZ (needs K^2 >= A/B'), product-form 1-D sums, unimodal Riemann lemma.
 => C(0) >= (2/l^3)[A P_b - B' Psi'_b], P_b=b^3 sum f^2, Psi'_b = l^-3 sum_q |q|^2 |fhat_b(q)|^2.
 t>0: Jensen on positive atoms: C(t) >= C(0) exp(-t M1/M0).
step3: lower constants: A-term ~0.48*true, B'-term ~3.37*true*s (kappa=2.5,theta=0.5); launching vol-run1
step4: child graded. control.txt = 0.00028060. Exact value 0.0002806049 -> 8 decimals 0.00028060. The brief's "known answer" 0.00028061 is a rounding defect of the brief; child's answer is correct.
 child claims C=2.177968313057 (l=1,N=48,s=0.005), b^3 sum f^2 = 0.01879479225576, ratio 2.0485e-4; grandchild N=8 brute force vs position 2.4e-13.
step5: Lean R12Vol.lean exit 0, 6 theorems, axioms propext/Classical.choice/Quot.sound only (gauss_lin needed hB: 0<=B, added).
step6: vol-run1 (K3) done. P0 2/2 met; P1 18/18 met (hyp 18/18); P2 18/18 met; P4 18/18 met; P3 3/9 met, 6/9 FAILED (bump at s=0.002,0.005: bound negative; my expectation, needs s*Psi'/P < ~0.14, have 0.155, 0.387). L/C = 0.26 (bump) / 0.06 (dbump) at s=0.001, same for l=1,2,4.
 R/true: 0.94 (s=.001), 0.88, 0.73-0.75 (bump). Lean K4 exit 0.
step7: report.md written. Verdicts: STANDS 7, DEFECT 1 (non-vacuity at s>=0.002), PARTIAL 1, NOT CHECKED: t>0 numerics. Predicates 59 met / 6 failed / 4 measured only.
