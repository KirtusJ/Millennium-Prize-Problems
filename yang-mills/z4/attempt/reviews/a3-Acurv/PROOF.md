# a3-Acurv: claim (A) for SU(2), d = 4, by positive curvature — the chain, written for attack

**NOT A PROOF.** Step S6 is CLAIMED and my own test refutes it. Step S7 is MISSING, and what it needs amounts to (A) in a stronger form. Steps S8 and S9 are CLAIMED. (A) is not established at any β_W ≥ 1/12 by this chain.

Conventions. SU(2) with metric ⟨X,Y⟩ = −Tr(XY); orthonormal basis e_a = iσ_a/√2; Ric = 1 (= N/2; SZZ (4.8), LIT_RIGOROUS R5b). The Wilson weight is exp(−V) with V = −(β_W/2) Σ_p Re Tr Q_p. Here β_W is the conventional coupling: β_W = 4β_SZZ, and SZZ's S = 2β_SZZ Re Tr. Link coordinates are U_e → exp(t_e·e)U_e. B(U) := Ric + Hess V = I + Hess V on T(SU(2)^E). The horizontal space H_U is the orthogonal complement of the infinitesimal gauge directions. κ_H(U) := min of B(U) on H_U.

Order of limits used throughout: β is fixed first. Then a finite box Λ (periodic, or with boundary condition τ on the links outside it). Functional-inequality constants must be uniform in (Λ, τ). Then Λ → Z⁴ (infinite-volume Gibbs state). Then time separation n → ∞. No uniformity in β is needed for (A).

## The chain

**S0 (PROVED, definitions).** For each finite Λ and boundary condition τ, μ_{Λ,τ} ∝ e^{−V} dHaar on SU(2)^{E(Λ)}. Its Langevin generator is L = Δ − ∇V·∇, with Dirichlet form E(f) = ∫|∇f|² dμ. μ is reversible for L. Target: a Poincaré inequality Var_μ(f) ≤ γ⁻¹ E(f) for gauge-invariant f, with γ > 0 independent of Λ and τ.

**S1 (PROVED).** The gauge group G^Λ acts by isometries of SU(2)^E: U_{xy} ↦ g_x U_{xy} g_y⁻¹ is a left and right translation in each factor, and the metric is bi-invariant. The action preserves V and Haar measure. So L commutes with the action, P_t = e^{tL} maps gauge-invariant functions to gauge-invariant functions, and for invariant f, ∇f(U) ∈ H_U, since df vanishes on orbit directions.

**S2 (PROVED, using the Bakry–Émery theorem, which is CITED via SZZ Thm 1.4 and its proof (4.7), LIT_RIGOROUS R5a).** Bochner's formula gives Γ₂(f) = ‖∇²f‖² + B(∇f, ∇f). For invariant f, ∇f is horizontal (S1), so Γ₂(f) ≥ κ_H Γ(f). If inf_U κ_H(U) ≥ K > 0, the Bakry–Émery semigroup argument (d/dt Γ(P_t f) ≤ −2K Γ(P_t f) on the P_t-stable algebra of invariant smooth functions) gives Poincaré with constant 1/K, and LSI with 2/K, for gauge-invariant functions. This is uniform in Λ and τ because K is pointwise.
Gain over SZZ: gauge directions are dropped. Numerically this removes a deficit that grows like √β_W: on L=3, λ_min(B) ≈ −6.4, −9.0, −12.2 at β_W = 12, 24, 48, against κ_H ≈ −1.6, −2.0, −1.5 (result_curv_L3_large.txt).

**S3 (CITED: SZZ (4.2), (4.8), Thm 1.4; LIT_RIGOROUS R5a/R5b).** ‖Hess V‖ ≤ 8(d−1)Nβ_SZZ = 12β_W, so κ_H ≥ κ ≥ 1 − 12β_W. Hypothesis check: SU(N) with N = 2, d = 4, the same normalization (checked: S = Nβ Re Tr ⇔ β_W = 4β_SZZ). Gives (A) for β_W < 1/12. My test, predicate C3: ‖Hess V‖ ≤ 12β_W on 76/76 samples; the observed maximum is ≈ 6.6β_W.

**S4 (PROVED; this is where non-abelian structure enters).** At every flat configuration (all Q_p = 1), Hess V(t,t) = (β_W/2)·Σ_p |Σ_{k∈p} ±Ad(·)t_k|². This is a sum of squares, ≥ 0, with zero modes. So κ_H = 1 = Ric there, exactly. Proof: at Q = 1, the second derivative of −(β_W/2)Re Tr(E₁u₁E₂u₂E₃⁻¹u₃E₄⁻¹u₄) reduces to −(β_W/2)Re Tr(Y²) with Y the signed sum of the transported generators, and −Tr(Y²) = |Y|². Test C0: κ_H = 1.000000000000 at U ≡ 1. For U(1), Ric = 0, so the same computation gives κ_H = inf (curl form) = 0 in infinite volume (the photon).

**S5 (PROVED for one plaquette by exact computation; measured on the 4D lattice).** For one plaquette with Q = −1, B has eigenvalues 1 − 2β_W (×3, horizontal) and 1 (×9). The child derived this by hand and computed it with FD agreement 1.7e-7. I reproduced it exactly with my own code. On 4D L=3, the configuration "all links 1, one link −1" gives κ_H = 1 − 4.31β_W for β_W = 1…6 (T1). Every μ_{Λ,τ} has full support, so inf_U κ_H < 0 for β_W > 1/2. The pointwise criterion S2 therefore cannot reach β_W > 1/2 (and S3 reaches only 1/12). An integrated criterion is needed: route (b).

**S6 (CLAIMED; REFUTED by my test).** Statement as I would have defended it: "For large β_W, κ_H(U) ≥ 1/2 except when U contains plaquettes far from 1 (Re Tr Q_p < 0). Those occur with density e^{−cβ_W}, so negative curvature is a rare event and a Holley–Stroock/Lyapunov perturbation of S2 applies locally." Argument: at flat configurations κ_H = 1 (S4), and the Hessian changes by O(β_W |F_p|) away from them.
Weakest point (written before the test): the O(β_W|F|) correction is not small, since β_W·β_W^{−1/2} ≫ 1.
**Test (curv_test.py, predicate T2): FAILED.** At β_W = 4 and 6, 0/8 equilibrium samples on 4D L=3 have κ_H ≥ 0.5. Every sample has κ_H between −1.5 and −2.2, while the fraction of plaquettes with Re Tr Q < 0 is 0.002 and 0.000. At β_W = 12, 24, 48 (4 samples each), κ_H is between −1.17 and −2.30 on every sample. On L=4 (2 samples each), κ_H = −1.60, −1.88 at β_W = 4 and −1.53, −1.58 at β_W = 6. So horizontal curvature below 0 is typical at weak coupling, not rare. It is an O(1) deficit (Hess V reaches about −2.5 to −3.3 on horizontal vectors), apparently bounded in β_W. Per brief (iii) I do not build on S6.
Measured, not a theorem. Small volumes, few samples, short thermalization at large β_W. The volume trend (L=3 → 4) can only push the minimum down.

**S7 (MISSING).** What would replace S6 is an integrated, volume-uniform criterion that tolerates κ_H < 0 on typical configurations. The only such route I can state is local-to-global. It needs, as an exact and testable statement:
> There are ℓ, C < ∞ and m > 0 such that for every cube B of side ≥ ℓ, every pair of boundary conditions τ, τ′ and every gauge-invariant f supported in B with ‖f‖∞ ≤ 1:
> |μ_{B,τ}(f) − μ_{B,τ′}(f)| ≤ C · Σ_{e: τ_e ≠ τ′_e} e^{−m·dist(supp f, e)}.

(Dobrushin–Shlosman strong mixing. Essentially Chatterjee's "strong mass gap", Def 2.3, LIT_RIGOROUS R5e.) This is (A) in a stronger, all-boundary-condition form, so the route is circular. It is false for U(1) in 4D at weak coupling. Nothing in S0–S6 supplies a non-abelian input for it beyond Ric = 1 > 0, and S6 shows that input is outweighed by an O(1) negative Hessian on typical configurations.

**S8 (CLAIMED; literature not read).** Strong mixing (S7) implies an LSI, hence a Poincaré inequality, uniform in Λ and τ, for finite-range systems of compact spins on a lattice. This is Stroock–Zegarlinski (1992) and Zegarlinski for compact-manifold spins, from memory. It is not in LIT_RIGOROUS and I did not fetch it. Application: link variables are compact SU(2) spins with range-1 plaquette interaction.
Weakest point: I have not checked whether the theorem is stated for manifold-valued spins with this interaction geometry, or whether the gauge zero modes of the block measures spoil it. (They should not, because the Langevin dynamics is ergodic on all functions, but this is unverified.)

**S9 (CLAIMED).** A Poincaré inequality with constant γ, uniform in volume, together with the range-1 interaction, gives |Cov(f,g)| ≤ c(f,g)·e^{−r·dist} with r > 0 depending only on γ and the interaction, not on supp f or supp g. This is SZZ's route: Cor 1.6 via Poincaré and Lemma 4.9 (LIT_RIGOROUS R5a: "Sec. 4.3 uses Poincaré plus Lie-bracket Lemma 4.9").
Weakest point: I did not reread SZZ Sec. 4.3 to confirm it uses only the Poincaré constant and not the small-β Assumption 1.1 elsewhere. The rate c_N is not explicit there.

**S10 (PROVED, given the infinite-volume OS reconstruction that A1 §1 assumes).** Let ψ = (O − ⟨O⟩)Ω for local gauge-invariant O. By S9, C(n) = ∫e^{−nε} dν_ψ ≤ c_ψ e^{−rn} with r independent of O. Since ∫e^{−nε} dν_ψ ≥ e^{−nr′} ν_ψ([0, r′)), letting n → ∞ gives ν_ψ([0, r′)) = 0 for every r′ < r. Local vectors are dense in Ω^⊥, so the spectral projection E_H([0, r′)) vanishes on Ω^⊥ and m(β) ≥ r. Uniformity of r in the support is essential here; it is exactly what S9 must deliver.

## Discriminator table (brief (i))

| model | (A) | first step of this chain that fails | why |
|---|---|---|---|
| compact U(1), d=4, weak coupling | **false** | **S3** (no pointwise regime at all: Ric = 0, so K = −12β_W < 0); at weak coupling also S4 (κ_H = 0, soft photon modes) and S7 (strong mixing false: massless photon) | Ric(U(1)) = 0. The chain does fail for U(1), as required. But the step that carries all the weight for SU(2) at large β (S7) is stated group-independently, so it fails for U(1) only because it is false there, not because the chain says why it would hold for SU(2) |
| finite group, d=4 | true (Adhikari–Cao, β large; LIT R3c) | **S0** | no Riemannian structure, no diffusion, no curvature: the mechanism does not apply. No contradiction; it cannot reproduce this gap |
| compact U(1), d=3 | true (Göpfert–Mack, Villain; LIT R3b) | **S3/S4** (Ric = 0) | the mechanism misses the true (monopole) gap, so curvature is not a necessary mechanism. No contradiction |
| d=2 (SU(2) or U(1)) | true (A1 §6; not checked by me) | SU(2): S5 already blocks the pointwise route (it is dimension-independent: one plaquette at −1); S7 is plausibly true via exact solvability (not checked). U(1): S3 | S7 holds in 2D for other reasons (near-independence of plaquettes), not from curvature |

## Where non-abelian structure enters (brief (ii))
Only in **S4**: Ric(SU(2)) = 1 > 0 gives κ_H = 1 at flat configurations, against 0 for U(1). Steps S6–S9 use no non-abelian structure, and S6 shows that Ric = 1 is outweighed on typical weak-coupling configurations.

## Quantifiers and limits (brief (iv))
- S2–S3: for each Λ and τ, with K pointwise, hence uniform in the volume.
- S5–S6: statements about configurations; the volume enters only through how many bad regions there are.
- S7: uniform over all cubes and all boundary conditions; this is where volume uniformity is used.
- S8: produces γ uniform in Λ and τ. Then Λ → ∞: uniqueness of the Gibbs state and Poincaré for cylinder functions.
- S9: rate uniform in the supports.
- S10: n → ∞ last, at fixed β.

## Weakest link
**S7.** It is MISSING, and it is equivalent to a strong form of (A) (circular). S6, the step that was supposed to make the curvature mechanism reach large β, is refuted numerically: horizontal curvature is ≈ −1.5 to −2 on every typical sample for β_W = 3 to 48.

## What a challenger should attack first
1. My refutation of S6. Check curv_test.py's Hessian against an independent code; it passed FD (C1, 1.7e-8) and the child's single-plaquette values. Check thermalization and volume at large β_W. Find out whether the O(1) negative horizontal mode is a torus artefact (constant/toron modes) that disappears in infinite volume; if it is, S6 might survive in a corrected form.
2. S8: does Stroock–Zegarlinski apply to SU(2) link spins with plaquette interaction?
3. S9: does SZZ Sec. 4.3 use only the Poincaré constant?
4. S2: the claim that the invariant algebra is a legitimate Γ₂ algebra (P_t-stable, dense in the invariant L²).
