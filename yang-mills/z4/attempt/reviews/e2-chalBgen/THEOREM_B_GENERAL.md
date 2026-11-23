**The extension is PROVED here, relative to the SU(2) proof in sec_proof_SU2.tex, for every compact Lie group G (connected or not) with a faithful finite-dimensional unitary representation rho and dim G >= 1. Every step that changes is proved below. Three new standard facts are cited and not re-proved (Section 6). The ratio bound is exactly (G(n)/G(0))^2 with no group-dependent factor. The proof FAILS for finite groups (dim G = 0): the limit variance is 0 there, and for Z_2 the conclusion is false (cited literature, CLAIMED, not checked here). What is not done: the tail constant D*_G contains a non-explicit compactness constant eta_*, and it cannot be bounded in terms of (dim G, N) alone (counterexample in Section 3).**

Worker d1-Bgen (task T36). In this file N_rho denotes the dimension of rho. The paper's N (box half-side) is written N_box.

## 1. Theorem (B_gen)

**Hypotheses.**
- (H1) G is a compact Lie group with d := dim G >= 1. G need not be connected.
- (H2) rho: G -> U(N_rho) is a continuous unitary representation that is faithful. If rho is not faithful, replace G by rho(G). This changes nothing, because the action and O_p depend only on rho(U), and Haar measure pushes forward to Haar measure. The effective condition is therefore dim rho(G) >= 1.
- (H3) Dimension 4, Wilson action S = sum_p s(U_p) with s(U) := 1 - (1/N_rho) Re Tr rho(U), periodic boxes of side 2^k, and the class L_beta of weak limit points. These are exactly as in the SU(2) paper.

**Conclusion.** Put O_p := beta s(U_p). Then

    liminf_{beta->inf} inf_{mu in L_beta} Cov_mu(O_{p0},O_{pn}) / Var_mu(O_{p0}) >= (G(n)/G(0))^2   for every n >= 1,

and sup_{mu in L_beta} m_mu(beta) -> 0. Here G(n) is the same one-colour free Maxwell correlation, and there is no factor depending on G or rho.

**The limit object.** Put <X,Y>_rho := -(1/N_rho) Tr(drho X drho Y) on the Lie algebra g. This form is positive definite because drho is injective (rho is faithful) and -Tr(A^2) = ||A||_HS^2 for anti-Hermitian A. It is Ad(G)-invariant for all of G because rho is unitary. In a <,>_rho-orthonormal basis the limit field has d independent colours, and

    O_p -> (1/2)|F_p|_rho^2,   Cov(X_0,X_n) = (d/2) G(n)^2 + G(n) E|f|^2 + (1/4) Var|f|^2,   Var X_0 >= d/8.

**Why no factor appears.** The quadratic form in the Gaussian weight and the quadratic form in the observable are the same form, namely the Hessian of s at 1, which is (1/2)|X|_rho^2. "Diagonalising" is therefore the choice of a rho-orthonormal basis, and the form becomes the identity. More generally, let the observable use any positive form B while the action uses A. Then the Gaussian part is (1/2) G(n)^2 Tr((B A^{-1})^2) and the cross term is G(n) E[f^T B A^{-1} B f]. Each still has ratio (G(n)/G(0))^2 or G(n)/G(0) to its n = 0 value, so the bound is robust. Nowhere is it used that <,>_rho is a multiple of the Killing form on simple factors, or that Ad acts transitively. Example: for U(2) the u(1) part has Killing form 0, but <,>_rho is positive there.

## 2. Replacement of the class angle (used everywhere)

- **Metric.** Let dist be the Riemannian distance of the bi-invariant metric <,>_rho on G, and put a(U) := dist(1,U), with a = infinity off the identity component G_0. Bi-invariance under all of G gives the four relations of (pf:eq-alpha) verbatim. Translations are isometries; Ad-invariance covers conjugations; and a(U^{-1}) = a(U).
- **Chordal function.** Put chi(U) := ||rho(U)-1||_HS / sqrt(2 N_rho), which takes values in [0, sqrt 2]. Then s = chi^2, which is (E1) in general form. chi is finite on all of G. It satisfies chi(UV) <= chi(U) + chi(V) and |chi(AVB) - chi(AB)| <= chi(V), because rho is unitary. Consequently |s(AVB) - s(AB)| <= 2 sqrt2 chi(V) (Lean L4).
- **Injectivity.** Let Omega := {X : ||drho X||_op < pi}. Then exp is injective on Omega. Proof: if e^A = e^B with A, B anti-Hermitian and ||A||, ||B|| < pi, then A = B = principal Log, and drho is injective. Also d exp_X is invertible on Omega, because the eigenvalues of ad X are among i(theta_j - theta_k), whose moduli are < 2 pi. Let X be in Omega and let Y be a minimal geodesic vector for exp X, so |Y| = dist(1, exp X) <= |X|. If moreover |X| < pi/sqrt(N_rho), then Y lies in Omega as well, so Y = X. Hence exp maps the ball B_r diffeomorphically onto the dist-ball of radius r, for every r < pi/sqrt(N_rho). On G_* := {a < pi/sqrt N_rho} define log U as the unique X with |X| = a(U). Off G_* put log U := 0; this choice is measurable.
- **Two-sided comparison.** Let the eigenvalues of drho X be i theta_j. Then |X|^2 = (1/N_rho) sum_j theta_j^2 and s(exp X) = (1/N_rho) sum_j (1 - cos theta_j). It follows that:
  - (C1) s(exp X) <= |X|^2/2 for ALL X (Lean L5; B4 checked numerically). Hence s <= a^2/2 on G_0.
  - (C2) s(exp X) >= (2/pi^2)|X|^2 when ||drho X||_op <= pi, in particular when |X| <= pi/sqrt N_rho. Hence on G_*, a^2 <= (pi^2/2) s.
  - (C3) 0 <= |X|^2/2 - s(exp X) <= (N_rho/24)|X|^4.
- **Compactness constant.** Put eta_* := inf{s(U) : U not in G_*}. It is positive: the complement of G_* is compact and s vanishes only at 1 (faithfulness). It is not explicit. Consequently {s < eta_*} is contained in G_*, and on G_* we have |sqrt(beta) log U|^2 <= (pi^2/2) beta s(U).

## 3. Ball volume (brief item 2)

Let V(t) := Haar{s <= t}, let Vol_rho(G) be the total Riemannian volume, and let omega_d be the volume of the unit ball in R^d. The Haar density in the exponential chart on B_{pi/sqrt N_rho} is

    j(X) = prod over ad-eigenpairs ±i l of (sin(l/2)/(l/2))^2 / Vol_rho(G)

(standard, cited). This gives j <= 1/Vol_rho(G). We also have ||ad X||_op <= 2||drho X||_op <= 2 sqrt(N_rho)|X|. By Jordan's inequality (Lean L1, numerical check B6), j >= (2/pi)^d / Vol_rho(G) on |X| <= pi/(2 sqrt N_rho).

**Lemma V.** For t in (0,1], c_V t^{d/2} <= V(t), and for all t > 0, V(t) <= C_V t^{d/2}, with

    c_V = omega_d min(2/pi, N_rho^{-1/2})^d / Vol_rho(G),
    C_V = max( omega_d (pi^2/2)^{d/2} / Vol_rho(G), eta_*^{-d/2} ).

Moreover lim_{t->0} V(t)/t^{d/2} = omega_d 2^{d/2} / Vol_rho(G).

*Proof.*
- Lower bound. By (C1), {a <= sqrt(2t)} is contained in {s <= t}. Use the Jacobian lower bound when sqrt(2t) <= pi/(2 sqrt N_rho). Otherwise use monotonicity and t <= 1.
- Upper bound. Take t < eta_*. Then {s <= t} is contained in G_*, and by (C2) it is contained in {a <= pi sqrt(t/2)}, whose measure is at most omega_d (pi^2 t/2)^{d/2} / Vol. For t >= eta_*, V <= 1 <= (t/eta_*)^{d/2}.
- Limit. Use (C3) and the continuity of j at 0, where j(0) = 1/Vol. ∎

**Where compactness, connectedness and dim G enter.**
- Compactness gives Vol < infinity and eta_* > 0.
- Connectedness is NOT used. The chart lives in G_0, Vol counts all components, and other components carry s >= eta_* > 0.
- For a finite group, d = 0, and V(t) = 1/|G| for t < min over g ≠ 1 of s(g). The exponent d/2 = 0 is formally consistent, so Lemma V, the free-energy bounds and the tail all hold. What fails is in Section 5 (variance 0).

**Constants cannot be functions of (d, N_rho) alone.** Take U(1) with rho_k = e^{it} ⊕ e^{ikt}, which is faithful with N_rho = 2 and d = 1. Then lim V(t)/sqrt t = 2/(pi sqrt(1+k^2)), while V(1) ≈ 1/2 (B2 and B3 met; the ratio is 39 at k = 50). Any valid C_V/c_V therefore grows at least like k. Only the tail constant depends on this. The final bound c(n) does not.

**Checked numerically (test (i)).** SU(3): lim V/s^4 = 9 sqrt3/(8 pi) = 0.620245 = omega_8 2^4 / Vol_rho(SU(3)), with Vol_rho = sqrt3 (2pi)^5/(2·3^4). This was obtained three ways: child T37 by Monte Carlo, grandchild T39 by deterministic quadrature, and my B1 by an independent Weyl grid, which gave 0.62022. U(1): V = arccos(1-s)/pi, with slope 1/2. The Hessian q(X) = |X|_rho^2/2 was checked for SU(3) and U(1).

## 4. Table: statement by statement

Legend: V = carries over verbatim; C = carries over with the stated change; N = needs a new argument (given here); F = fails for some G.

| Paper item | Status | Change / argument |
|---|---|---|
| Setting, class angle α, (pf:eq-alpha) | C | α is replaced by a = dist(1,·) together with chi (Section 2). The Weyl density is replaced by Lemma V. |
| Lie algebra identification R^3 = su(2), ‖Ad(U)-I‖ <= 2α | N | g carries <,>_rho with an orthonormal basis, giving R^d. ‖Ad(V)-I‖_op <= 2‖rho(V)-1‖_op <= 2 sqrt(2N_rho) chi(V), from rho(V) Y rho(V)^{-1} - Y. |
| Lemma rp (reflection positivity) | V | Only two facts are needed: s(U^{-1}) = s(U), since Re Tr rho(U^{-1}) = Re conj(Tr rho(U)); and inversion invariance of Haar measure, since compact groups are unimodular. Reversing a plaquette's orientation gives U_p^{-1} up to conjugation, and s is a class function. |
| Lemma limit (1)-(3) | V | Compactness of G^E only. |
| Lemma transfer, Prop spectral (bound) | V | — |
| Prop spectral: Var_mu(O_p0) > 0 | N | Level sets of U -> s(UV) need not be null on every component. For O(2) in the defining representation, s ≡ 1 on the reflection component. The new argument: on the coset G_0 V^{-1}, the map U -> s(UV) is real-analytic and not constant, so its level sets are null. The conditional density is positive, so the law of O has a non-atomic part of positive mass, and therefore Var > 0. |
| Lemma chess | V | Group-independent. |
| Lemma forest | V | Haar invariance only. |
| Lemma free | C | ẑ(b) = ∫ b e^{-bt} V(t) dt <= C_V Γ(d/2+1) b^{-d/2}. For the lower bound, restrict the free links to {a <= β^{-1/2}}. Then a(U_p) <= 4β^{-1/2}, (C1) gives βs <= 8, and βS <= 48|Λ| as before. Haar of that set is >= c_V β^{-d/2} for all β >= 1. Resulting constant: D*_G = 48 + 3 log(C_V Γ(d/2+1) 2^{d/2}) - 3 log c_V. The β-terms cancel, leaving (2d/L) log β → 0. |
| Cor tail | C | μ(O_p > t) <= e^{D*_G - t/8}. The bound "sqrt(β) α_p <= (π/sqrt2) sqrt(O_p)" becomes \|F_p\|^2 <= (π^2/2) O_p everywhere, by (C2) and log := 0 off G_*. |
| Lemma E (E1) | C | s = chi^2. |
| Lemma E (E2) | V | Valid for matrices of any size. |
| Lemma E (E3) | C | Put sigma = Σ‖drho x_i‖_op <= sqrt(N_rho) s_p. Then a(U_p) <= s_p, and \|y_p - dx_p\|_rho <= N_rho s_p^2 e^{sqrt(N_rho) s_p} when s_p < π/sqrt(N_rho). This uses \|Z\|_rho <= ‖drho Z‖_op. |
| Elementary inequalities | V | — |
| Lemma flat, Lemma shell (first claim) | V | Already stated for any group. |
| Lemma shell (K_N bound) | C | State it with chi in place of α: chi(V_l) <= K_N max_q chi_q, using bi-invariance and subadditivity of chi on all of G. Then chi(V_l)^2 < η_* forces V_l ∈ G_* with \|log V_l\| <= (π/sqrt2) chi(V_l). |
| Cor zero (1) | V | With rho faithful, s(U) = 0 iff rho(U) = 1 iff U = 1. Flat implies pure gauge for any group. Centre elements on links are not zeros unless they form a gauge transformation, because a central z on one link changes the adjacent plaquettes to z·U_p ≠ 1. |
| Cor zero (2), λ_N > 0 | V | Scalar per colour. |
| §L3 gauge and chart, (pf:eq-Kbeta) | N | The chart does not cover G. Split the conditional law into the near set {a(U_l) <= δ for all l} (in the chart, density j) and its complement. The complement is a compact set on which S_R(·; 1) >= η(δ) > 0. Its mass is <= e^{-βη/2} times (Vol β^{d/2})^{ν_R} relative to the chart normalisation, which tends to 0 (Section 5). |
| (pf:eq-epsM) | C | Holds for β >= β_1(M) (also including the event V_l ∉ G_*), using the tail bound and K_N. |
| Thm L3 near region | C | Choose δ <= π/(2 sqrt N_rho) with 48 N_rho^2 δ^2 e^{8 sqrt(N_rho) δ} <= min(λ/16, 1). Then βS_R >= (λ/16)\|φ\|^2 - 7\|ψ\|^2 (Lean L2, L3). |
| Thm L3 far region | N | The bound "\|φ\|^2 < ν π^2 β on the chart" is replaced by the mass estimate above. The perturbation becomes \|S_R(U;ψ/sqrtβ) - S_R(U;0)\| <= 12 Σ\|ψ_l\|/sqrtβ, via chi(exp y) <= \|y\|/sqrt2 and the 2 sqrt2 Lipschitz constant. |
| Thm L3 pointwise / convergence | C | Constants carry N_rho factors by (C3) and E3. j·Vol → 1 uniformly on bounded sets. The TV statement holds for the near part, and the far part → 0. |
| Prop L4 existence, (a) | C | Tightness from \|F_p\|^2 <= (π^2/2) O_p. The path step uses ‖Ad(V)-I‖ <= 2 sqrt(2N_rho) chi(V). The base-point step uses Haar measure on G and Ad(R)-invariance for every R ∈ G; transitivity is not used. |
| (b) Bianchi | C | Cube word identity in the free group: V. The estimate uses E2 for N_rho×N_rho matrices, with constants scaled by N_rho. For U(1) the error term is 0: y_p = dx_p exactly on the event. |
| (c), (d) | C | (c) verbatim with Ad(G). (d) uses \|O_p - \|F_p\|^2/2\| <= N_rho \|F_p\|^4/(24β) on {U_p ∈ G_*}, whose complement has probability <= e^{D* - βη_*/8}. |
| (e) Gaussian DLR | C | Replace R^3 by R^d (ρ-orthonormal colours). |
| Lemma D, Lemma R | C | d independent colours instead of 3. Background colours may be correlated. |
| Lemma G | V | Scalar. |
| Lemma Wick | C | Cov = (d/2) G(n)^2 + G(n) E\|f\|^2 + (1/4) Var\|f\|^2, Var X_0 = (d/2) G(0)^2 + ..., Var X_0 >= d/8. |
| Assembly | C | Needs Var_{μ∞} X_0 >= d/8 > 0. **F for d = 0:** the field is identically 0 and the argument gives nothing. |

## 5. Proofs of the new steps

**(N1) Far region and the chart.** Fix δ as in the near region. Put A := {U ∈ G^{Λ''} : a(U_l) < δ for all l}; its complement A^c is closed. On A^c, S_R(U; shell = 1) > 0 by Cor zero(1), so η(δ) := min_{A^c} S_R(·; 1) > 0. For |ψ| <= M and β >= (24 sqrt(ν_s) M/η)^2, the perturbation bound gives S_R >= η/2 on A^c.

Write the conditional integral as I_A + I_{A^c}, so that I_{A^c} <= e^{-βη/2}. On A use x_l = log U_l and φ = sqrtβ x. Then

    (Vol_rho β^{d/2})^{ν} I_A = ∫_{|φ_l| < δ sqrtβ} f_β dφ,   f_β := e^{-βS_R} prod_l Vol·j(φ_l/sqrtβ).

By the near-region bound and Vol·j <= 1, f_β <= e^{7M^2} e^{-(λ/16)|φ|^2}. Pointwise, f_β → e^{-Q/2} uniformly on compact sets. Hence ∫ f_β → Z_∞(ψ) >= z_M uniformly in |ψ| <= M. The far part, measured in the same normalisation, is at most (Vol β^{d/2})^ν e^{-βη/2} → 0. Hence

    sup_{|ψ|<=M} TV( conditional law, K_∞ ) <= 2 ∫|f_β - f_∞| / Z_∞ + 2 (Vol β^{d/2})^ν e^{-βη/2} / z_M + o(1) → 0,

where on A^c a test function is bounded by its sup norm. This replaces "(pf:eq-lower) on the whole chart" and the null-set remark. The tightness statement follows in the same way. ∎

**(N2) Near region (general N_rho).** By E2 for N_rho×N_rho matrices with sigma <= sqrt(N_rho) s_p:

    ‖rho(U_p) - 1 - drho(dx_p)‖_op <= (sigma^2/2) e^sigma.

Since ‖·‖_HS <= sqrt(N_rho) ‖·‖_op and ‖drho Z‖_HS = sqrt(N_rho) |Z|_rho, this gives sqrt(2 N_rho s(U_p)) >= sqrt(N_rho) (|dx_p| - (N_rho s_p^2/2) e^{sqrt(N_rho) s_p}). Hence βs >= (1/2)(a_p - b_p)_+^2 with b_p <= 2 N_rho δ e^{4 sqrt(N_rho) δ} s̃_p (Lean L2, using s_p <= 4δ). Lean L3 then gives βs >= a_p^2/4 - 8 N_rho^2 δ^2 e^{8 sqrt(N_rho) δ} Σ_{i∈p} |φ̃_i|^2. Summing with multiplicity 6 and continuing as in the paper gives the result. ∎

**(N3) Var > 0 at finite β.** Covered in the table. Real-analytic functions on a connected manifold that are not constant have null level sets. s(·V) is not constant on G_0 V^{-1}: it equals 0 at V^{-1} and is positive nearby, by faithfulness and d >= 1. ∎

**(N4) Box normalisation, test (ii).** On R_1 with the shell fixed to 1, the Gaussian limit in ρ-orthonormal coordinates is d independent copies of the one-colour Dirichlet field. So E O_p → (1/2) E|dφ_p|^2_rho = (d/2) C_pp with C_pp = 7/24, and the normalisation factor is 1. Monte Carlo at β = 300 (box_mc.py; all predicates met):

| Group | Measured E O_p (all 24 plaquettes) | Prediction |
|---|---|---|
| SU(3) | 1.16802 ± 0.00111 | 7/6 = 1.16667 |
| SU(2) | 0.43685 ± 0.00040 | 0.4375 |
| U(1) | 0.14589 ± 0.00015 | 7/48 = 0.14583 |
| U(1) with rho_2 (Hessian factor 5/4) | 0.14592 ± 0.00014 | 7/48 (same) |

The last row confirms that there is no ρ-dependent factor. Measured only for SU(3): 1.17198 at β = 75 and 1.16529 at β = 1200.

**(N5) Finite groups.** The Lie algebra is 0, so F^β ≡ 0 and Var_{μ∞} X_0 = 0. The assembly breaks. Indeed O_p = β s(U_p) is 0 or >= β s_min, and the tail gives μ(O_p ≠ 0) <= e^{D* - β s_min/8}, so all moments of O_p → 0. For G = Z_2 in d = 4 at large β, the low-temperature (Peierls/cluster) expansion is known to give exponential clustering with a mass of order β. This is cited and was **not checked** here, so it is CLAIMED. The conclusion "m → 0" is then false, and the hypothesis dim G >= 1 is sharp.

**(N6) U(1).** Ad is trivial. Lasso fields need no transport. For small curvatures y_p = dx_p exactly (mod 2π), so the (b) and E3 errors vanish identically. Only the cos-Taylor term remains. The conclusion m → 0 is consistent with the proved massless (Coulomb) phase of 4D U(1) at weak coupling (Guth; Fröhlich–Spencer; cited). The argument does not distinguish U(1) from SU(N). This is expected: the theorem asserts only a vanishing gap in lattice units, which holds in both cases.

## 6. CLAIMED / MISSING

- CITED, not re-proved:
  - Hopf–Rinow and bi-invariant geodesics (minimal geodesics exp(tY) exist in G_0; dist is bi-invariant).
  - The Haar density in exponential coordinates, det((1 - e^{-ad X})/ad X) / Vol.
  - Real-analytic functions have null level sets.
  - The Z_2 mass gap at weak coupling (N5).
  - The U(1) Coulomb phase (N6).
- MISSING / not explicit:
  - η_* (compactness) and the paper's η(δ) and K_{N_box}. None of them enters c(n).
  - No explicit D*_G in terms of (d, N_rho) alone; this is impossible (Section 3).
- Only scalar inequalities are formalised in Lean (lean/GenScalar.lean: L1–L5, exit 0, axioms propext / Classical.choice / Quot.sound). The matrix and group statements are checked numerically (B4–B7), not formally.
- I (Claude Opus, same model family as the director) wrote both the proof and the tests. This is not independent review.
