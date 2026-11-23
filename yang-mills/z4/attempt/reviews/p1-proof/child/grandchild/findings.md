# Statement comparison: pf:thm-L3 (thmL3_excerpt.tex) vs Theorem L3, L3_L4.md section 2(d)

## Control
L3_L4.md section 2(b): "Each link lies in at most 6 plaquettes, so summing over p". Answer 6, matching the principal's expectation. control.txt contains `6`.

## Texts compared (statements only)
Source 2(d): "For every box R, every M < infinity, and every bounded measurable W(phi, psi): sup_{|psi|<=M} |K_beta W(psi) - K_inf W(psi)| -> 0 as beta -> infinity, where K_inf(.|psi) ~ e^{-1/2 Q(phi;psi)}dphi, with 3 independent colours. In addition, K_beta(|phi|>r | psi) <= z_M^{-1} e^{7M^2} int_{|phi|>r} e^{-c|phi|^2} + o(1), uniformly in |psi|<=M: the conditional laws are uniformly tight."

LaTeX: "Fix a box R and M<infinity. There are c>0 and beta_0(M)<infty such that, for all beta>=beta_0(M), all |psi|<=M and all phi in the chart, beta S_R(phi/sqrt beta; psi/sqrt beta) >= c|phi|^2 - 7M^2. Moreover lim_{beta->inf} sup_{|psi|<=M} ||K_beta(.|psi) - K_inf(.|psi)||_TV = 0, so sup_{|psi|<=M}|K_beta W(psi) - K_inf W(psi)| -> 0 for every bounded measurable W, also when W depends on psi or on further parameters with ||W||_inf uniformly bounded. Finally, uniformly in |psi|<=M and beta>=beta_0(M), K_beta(|phi|>r|psi) <= z_M^{-1} e^{7M^2} int_{|phi|>r} e^{-c|phi|^2} dphi + o(1) as beta->inf, with z_M>0. The constant c = min(lambda_N/16, eta(delta)/(2 nu_R pi^2)) contains eta(delta)>0, obtained by compactness and not explicit."

## Ways the LaTeX statement is STRONGER than 2(d)
1. Claim absent from 2(d): the whole-chart lower bound beta S_R >= c|phi|^2 - 7M^2 for beta>=beta_0(M), all |psi|<=M, all phi in the chart, is a conclusion of the LaTeX theorem. In the source it is only the "Bound" paragraph of 2(b), and 2(d) does not state it.
2. Explicit constants/shape made part of the statement: the constant 7 in 7M^2 and the formula c = min(lambda_N/16, eta(delta)/(2 nu_R pi^2)) (with beta_0 and the existence of c, beta_0 asserted). 2(d) uses "c" and "e^{7M^2}" only inside the tail bound, with c undefined there (defined only in 2(b)). Note both texts say eta(delta) is not explicit, so no stronger claim on that.
3. Changed quantifier / stronger mode of convergence: LaTeX asserts sup_psi ||K_beta - K_inf||_TV -> 0, which is uniform over all W with ||W||_inf<=1 (up to a factor 2). 2(d) fixes W first ("for every bounded measurable W ... sup_psi ... -> 0"), so the limit is only for each W, not uniform over W. Because the LaTeX bound is uniform over W, it also gives convergence for W depending on psi or on "further parameters" with uniformly bounded norm. 2(d) allows W(phi,psi) but says nothing about further parameters or uniformity in W. (The source mentions this uniformity only in the proof text of 2(c) and in the "Colour" remark of section 3(c), not in 2(d).)
4. K_inf made explicit in the theorem context: LaTeX preceding the theorem gives K_inf as three independent N(-Q^{-1}B psi, Q^{-1}) with Q from Corollary zero(2). 2(d) says only "proportional to e^{-1/2 Q}, 3 independent colours"; the mean formula m(psi) = -Q^{-1}B psi appears in the source in 2(c), not 2(d). This is a minor, definitional strengthening (statement-adjacent, not in the theorem environment itself).

## Equal
- Quantification over box R, M<infinity, bounded measurable W, and the limit sup_{|psi|<=M}|K_beta W - K_inf W| -> 0 (the weak-form conclusion is the same).
- Tail bound: same expression z_M^{-1} e^{7M^2} int e^{-c|phi|^2} + o(1), uniform in |psi|<=M. The LaTeX adds "beta>=beta_0(M)" and "z_M>0" but since the o(1) is as beta->inf this is equivalent. Hypotheses on R, psi (|psi|<=M) are identical.

## Weaker
- Only cosmetic: the LaTeX does not use the phrase "the conditional laws are uniformly tight", but that is an immediate reading of its tail bound. Nothing substantive in 2(d) is missing from the LaTeX. No hypothesis is stronger in the LaTeX (no additional assumptions on R, M, W, psi).

## Summary
LaTeX is stronger than or equal to 2(d); never weaker in substance. Stronger items: (1) lower bound as a theorem conclusion, (2) explicit 7 and c formula, (3) TV/uniform-in-W convergence and extra W parameters, (4) explicit Gaussian mean/covariance.
