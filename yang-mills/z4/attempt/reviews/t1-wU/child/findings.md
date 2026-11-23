# findings.md -- fidelity check of src/tun_upper.tex (T170)

Control: 2*asinh(1) = 1.762747 (control.txt). Method: every statement and proof was read against LEMMA_F.md, TUNNEL_THEOREM.md, TUNNEL_LOWER2_sec3.md, CHAL_conditional.md, CHAL_lemmaF.md, TUNNEL_LOWER_FULL.md (C1-C7); constants re-derived by hand, scalar ones re-run in check.py (result_check_run1.json). I share a model family with the authors; this is not independent review. Not checked: the Lean files (not compiled here), the sections of the second half, existence of (W1)/(W3) (asserted in source and tex).

## Verdict table (20 items)

| # | label | verdict | evidence |
|---|---|---|---|
| 1 | tu:U-thm | MATCHES | Statement = LOWER_FULL header (lim = c*); tex proves only liminf half, says so. c*=4.605413245 recomputed (C1). |
| 2 | tu:U-kernel | CHANGED (writer addition) | Statement = THEOREM s0. Proof of (3) (character expansion, I_n-I_{n+2}=2(n+1)I_{n+1}/beta) is new, flagged in its Remark; I re-derived it, correct. |
| 3 | tu:U-K (Lemma K) | CHANGED (writer addition for the radial form; main bound MATCHES) | First bound: every constant equals THEOREM s3 ((beta/beta')^{3/2}, e^{|p|^2 beta/(2beta')}, (beta/2pi)^{3/2}2pi^2, 1/(1-1/beta)); denominator (1-1/beta) via E theta^2=3/beta re-derived; numeric C9: 150/150 cases qualify (beta'>0), all hold, min margin 0.020 nat. Radial form (E[e^{L sqrt(beta/beta0')|N|}]): not in source ("radial version"); CHAL_conditional hypotheses list calls it a missing line; my derivation agrees. |
| 4 | tu:U-R | MATCHES (1 nit) | (1)-(4) = THEOREM s1 incl. M_jk, l_j=I_{2j+1}/I_1, V_a=beta s^2(1-t). Nit tex line 297: F_{U1}=C_h^{-1}F_aC_h should be C_h F_a C_h^{-1} (given C_h psi(U2)=psi(hU2h^-1)); unitary equivalence unaffected. (2) is the "fibre bound" of THEOREM s4. |
| 5 | tu:U-F (Lemma F) | MATCHES | = LEMMA_F header + cor (a); all s in [0,1]. |
| 6 | tu:U-Frad | MATCHES | = LEMMA_F I3; prefactor 1/(pi Z) = beta/(2 pi I_1) re-derived. |
| 7 | tu:U-barta | CHANGED (CHAL_lemmaF, row I4) | = I4, with the hypothesis 0<inf psi<=sup psi<infty made explicit, which CHAL_lemmaF says is automatic and unstated. |
| 8 | tu:U-fixed | MATCHES | = I5; (x-y)(1+2x+2y)=x+y <=> x^2=y^2+y re-derived; density statement is read off the same computation. |
| 9 | tu:U-bessel | MATCHES | = I6; C5: 1800 (z,delta) cases, 0 violations. |
| 10 | tu:U-I1 | **WRONG** (minor constant) | tex line 432 "D(1)>0.039" is false: D(1)=0.0389315 < 0.039 (C3 FAILED, my predicate was "tex claim true"; the failure is a defect of the target, my prior suspicion was right). Sources write "D(1)=0.039" (CHAL_lemmaF I7 hypotheses) i.e. rounded; the tex turned a rounded value into a strict inequality. Consequence: none; only D>0 for beta>1 is used and D is increasing (2000 grid points, C3b) with D(1)>0. First claim I_1 >= e^z(1-1/2z)/sqrt(2 pi z)-1/2 holds on 400 points (C4). |
| 11 | tu:U-amgm | MATCHES | = I8. |
| 12 | tu:U-outer | MATCHES | = I9 (g(1)=0, g'(1)=gamma=(r/2)(1-A^-2) in [0,1/2), g''<=8 on [1/2,1], h=gamma/8, bound -h gamma+4h^2=-gamma^2/16). Taylor step re-derived: gamma_r(1-h) <= -h gamma + (h^2/2)*8 correct, h in [0,1/16] so 1-h in [1/2,1]. C7: 707/707 qualifying (r,c) cases pass; C6 (inequality itself, 707 cases) pass, min margin 0 at r=0. Lean scope statement (duality yes, Taylor no) agrees with CHAL_lemmaF. |
| 13 | tu:U-F-master | MATCHES | M_in and M_out identical to LEMMA_F Thm 1 term by term; hypotheses beta>1, s in (0,1], tau<1/5, delta<=1 identical. Proof re-derived: Gaussian tail P(|W'-m|>sqrt tau)=e^{-beta A tau/2} exact; outer prefactor beta e^beta/(2 I_1) <= beta sqrt(2 pi beta)/(2D). Numbers cited in Remark F-num reproduced: C10a deficit in [8.73,14.23] for beta in {256,1024,4096}, s in [0.1,1] (tex "8.6 to 14"); C10b first beta with deficit<0.2: 2.24e13. |
| 14 | tu:U-F-cor | CHANGED (CHAL_lemmaF, header defect) | LEMMA_F header said M_in,M_out ->0; tex (b) correctly says log max -> 0^+ (M_in->1, A M_out->0), as CHAL_lemmaF demands. Rest = LEMMA_F s3. |
| 15 | tu:U-weight | CHANGED (writer addition, flagged in tu:U-weight-rem) | (1),(2) = THEOREM s4-5. (3): tex uses c^rho_eta=2f(pi/2) instead of c*_eta in the barrier inequality; source's c*_eta version does not follow because rho_eta<=(eps-eta)_+, so tex is right and the source (and CHAL_conditional item 11) glossed this. New: c*-c^rho <= pi sqrt(6 eta) (re-derived; scalar claims C8 15000/15000) and f~>=f-L tau. (4) correct: f(a_x)+f(a_y)>=c^rho-L(a_y-a_x), times (1-delta). Window not meeting I: eps(pi/2-1/2)=1.585>1.3 re-computed. |
| 16 | tu:U-schur | CHANGED (CHAL_conditional item 7) | Adds the Taylor line cosh(x+y)<=cosh x e^{|y|}, |R_X|<=H theta^2/2 that the challenger found missing; correct (|sinh x|<=cosh x). Nit: omega(beta) is only defined once beta'>0, statement does not say "beta large". |
| 17 | tu:U-A | MATCHES | = THEOREM s4 (A), mu h=B*WBh, then Lemma R(2) with m=w; no positivity of u (LOWER2 s3). |
| 18 | tu:U-B | CHANGED (change C5; writer additions) | Statement = (B) with u in {g,f}, part (2)=LOWER2 s3 Exchange. C5: lambda_ee,lambda_eo>=e^{-eta/4} from L4 not sketches. Writer additions: eta<=1/2 (source: eta in (0,1)) and the explicit C(eta)=1+(e^{eta/2}-e^{-eta/4})/(e^{-eta/4}-e^{-eta/2}); algebra re-derived (q<=-eta/2 on I^c, <=eta/2 on I; C11 500 eta values finite). |
| 19 | tu:U-flux | CHANGED (CHAL_conditional item 10) | Prefactor is 4 in the tex (source had 2). Re-derived: 1-s(x)s(y)=2 on cross pairs, both orders count -> 4. Grandchild T172 confirmed on 3x3 symmetric positive matrices: ratio (lam-(sg)^T T(sg))/S = 4.000000000000 in 6/6 cases (3 matrices x 2 splits), not 2. Reread and rerun by me: same. |
| 20 | tu:U-main | CHANGED (CHAL_conditional item 10 for the 4; C5; writer addition c^rho) | Final chain re-derived line by line: Delta<=4 C(eta) C_L e^{-sqrt(beta)(1-delta)(c^rho-2L tau)}; (1-delta) factor on the L d_1 term dropped legitimately (upper bound); m_eo<=Delta/lambda_eo<=e^{eta/4}Delta<=2 Delta (eta<=1/2); -log m/sqrt(beta) >= (1-delta)(c^rho-2L tau)-log(8 C C_L)/sqrt(beta); then (3) gives c*-pi sqrt(6 eta)-2L tau. Constants 4, 2, 8=2*4 consistent. |

Counts: MATCHES 10 (1,4,5,6,8,9,11,12,13,17); CHANGED 9 (2,3,7,14,15,16,18,19,20), all with a listed correction or an explicit "writer addition" that I checked as correct; WRONG 1 (item 10).

## WRONG items (exact text)

1. src/tun_upper.tex line 432, proof of Lemma tu:U-I1: "...; $D(\beta)$ is increasing for $\beta\ge1$ and $D(1)>0.039$." D(1)=1-1/2-sqrt(2 pi)e^{-1}/2=0.0389315 < 0.039. Suggested fix: "D(1)>0.038" (or "D(1)=0.0389..."). No later step uses the number; only D>0 for beta>1, which holds.

## Nits (not counted WRONG)
- tex line 297: C_h^{-1}F_aC_h should read C_h F_a C_h^{-1} (conclusion unchanged).
- Lemma tu:U-schur: omega(beta) is meaningful only for beta' = beta(1-5eta_K^2/48)-sqrt(beta)H > 0; add "for beta large".
- Intro item 4: "agrees with c* to about 0.1%": 4.599 vs 4.6054 is 0.14%. The value c=4.599 is from the companion paper, not in the given sources; unverified.
- Remark tu:U-F-num: "8.6" vs my 8.73 minimum on the 0.01 s-grid for beta in {256,1024,4096}; within the quoted range, not a conflict.
