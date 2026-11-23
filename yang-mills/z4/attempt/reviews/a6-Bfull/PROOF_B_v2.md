# PROOF_B_v2 — this is NOT yet a complete proof. It proves Theorem B′ below (dyadic periodic limit states, gap bounded via one vector) modulo two steps tagged CLAIMED (L3 uniform Laplace limit, L4 limit lasso/path-independence bookkeeping). Every other step is PROVED here. No step is MISSING.

Worker a6-Bfull for Director Z4, 23 Nov 2026. Principal: Kirtus Justus. I share a model family with the builder, the challenger and the director, so this is not independent review.

Tags: **PROVED** = full proof written here. **CITED** = source and locator read. **CLAIMED** = argument given, but some detail is not written to referee standard. **MISSING** = no argument.

No source was read at theorem level in this run. Biskup's notes, arXiv:math-ph/0610025, were read only in Sections 1–3.4; their chessboard theorem was not read. So I cite nothing for the chessboard estimate and **re-prove it** (Lemma 2).

## 0. Statement

**Setting.**
- G = SU(2). Λ_L = (ℤ/Lℤ)⁴ with **L = 2^k**.
- μ_{β,L} is the measure ∝ exp(−β Σ_p (1 − cos α_p)) ∏_l dU_l, with Haar dU and ½Tr U_p = cos α_p, α_p ∈ [0, π].
- O_p := β(1 − cos α_p). p₀ is the (1,2) plaquette at the origin; p_n := p₀ + n e₀.
- 𝓛_β is the set of weak limit points, as k → ∞, of μ_{β,2^k}. These are measures on SU(2)^{E(ℤ⁴)}, with the torus embedded around the origin. 𝓛_β ≠ ∅ by compactness.

**Hilbert space and transfer matrix (PROVED, §1).**
For μ ∈ 𝓛_β, let 𝒜₊ be the bounded continuous functions of finitely many links in {x₀ ≥ 0}. The reflection plane's links belong to 𝒜₊. Let ϑ be the reflection x₀ ↦ −x₀, acting on links with inversion on temporal links, and set θF := conj(F∘ϑ).
- ⟨F, G⟩ := μ(θF · G) is positive semidefinite on 𝒜₊.
- 𝓗 is the completion of 𝒜₊ modulo null vectors, and Ω := [1].
- T[F] := [τ₁F], where τ₁ is the unit time translation. T is a well-defined, self-adjoint contraction with TΩ = Ω.
- m_μ(β) := −log ‖T|_{Ω^⊥}‖ ∈ [0, ∞]. This is the spectral definition on the whole orthocomplement.

**Theorem B′.** lim_{β→∞} sup_{μ ∈ 𝓛_β} m_μ(β) = 0.

More precisely, for every even n ≥ 2:

  liminf_{β→∞} inf_{μ∈𝓛_β} Cov_μ(O_{p₀}, O_{p_n}) / Var_μ(O_{p₀}) ≥ c(n) := (G(n)/G(0))² ≥ c₀ n^{−10}.

Since Cov_μ(O_{p₀}, O_{p_n}) = ⟨ψ, Tⁿψ⟩ ≤ e^{−n m_μ} ‖ψ‖² with ψ = [O_{p₀} − μ(O_{p₀})], this is an **upper bound on the gap through one vector**. It also bounds the exponential decay rate of ψ's spectral measure, which is ≥ m_μ.

**Honest differences from (B) as stated in the attempt:**
1. Only limit points along L = 2^k. General even L needs the FILS form of the chessboard estimate, which was not read.
2. Only periodic limit states, not all Gibbs states.
3. The conclusion is "m → 0", which includes m ≡ 0.

## 1. S0–S2

**Lemma 1 (site-plane RP, all four directions, torus with L even). PROVED.**
Let π be the plane x_j = 0 together with x_j = L/2, and ϑ the reflection x_j ↦ −x_j.
- E₀ is the set of links lying in π. E₊ (resp. E₋) is the set of links with both endpoints in 0 ≤ x_j ≤ L/2 (resp. L/2 ≤ x_j ≤ L), minus E₀.
- 𝒜₊ is the functions of E₀ ∪ E₊.
- Every plaquette has all its sites in one closed half, because its j-extent is ≤ 1. Let W₊ be the sum of cos α_p over plaquettes in the closed + half, with weight ½ for plaquettes contained in π.
- Then Σ_p cos α_p = W₊ + W₊∘ϑ. This uses cos α_{ϑp} = cos α_p: reflection inverts U_p up to conjugation, and ½Tr U⁻¹ = ½Tr U for SU(2).
- Haar measure is invariant under U ↦ U⁻¹, so ϑ maps dU_{E₊} to dU_{E₋}.

Hence, for F ∈ 𝒜₊:

  Z μ(F θF) = ∫ dU_{E₀} |∫ dU_{E₊} F e^{βW₊}|² ≥ 0.

The weights e^{−6β|Λ|} are constants. This gives ⟨F θG⟩ = conj⟨G θF⟩ and the Cauchy–Schwarz inequality |μ(F θG)|² ≤ μ(F θF) μ(G θG).

**Lemma 1′ (passage to 𝓛_β). PROVED.**
- Translation invariance holds.
- Time-reflection RP holds for local continuous F. For large L, F ∈ 𝒜₊ of the torus, and μ ↦ μ(FθF) is weak-continuous.
- The DLR equations for the Wilson specification hold for finite link sets Λ. The kernel γ_Λ maps continuous local functions to continuous local functions, so μ(γ_Λ g) = lim μ_L(γ_Λ g) = lim μ_L(g) = μ(g).

**Transfer matrix. PROVED.**
- θτ₁ = τ₋₁θ, so ⟨G, τ₁F⟩ = ⟨τ₁G, F⟩.
- ‖τF‖² = ⟨F, τ²F⟩ ≤ ‖F‖ ‖τ²F‖. Iterating, ‖τF‖ ≤ ‖F‖^{1−2^{−j}} ‖τ^{2^j}F‖^{2^{−j}} ≤ ‖F‖^{1−2^{−j}} ‖F‖_∞^{2^{−j}}. Letting j → ∞ gives ‖τF‖ ≤ ‖F‖.
- So null vectors go to null vectors, and T is a self-adjoint contraction. It leaves Ω^⊥ invariant because ⟨Ω, TF⟩ = μ(F) = ⟨Ω, F⟩.

**S1. PROVED.**
O_{p₀} lies in the plane, is real, and satisfies θO = O. Then ⟨ψ, Tⁿψ⟩ = Cov_μ(O_{p₀}, O_{p_n}) ≤ ‖T|_{Ω^⊥}‖ⁿ ‖ψ‖².

**S2. PROVED** (algebra Lean-checked in v1, `s2_gap_le`; not rerun here).
If C(n) ≥ c C(0) and C(0) > 0, then m ≤ −log c / n. With c(n) ≥ c₀n^{−10}, we get inf_n(−log c(n))/n = 0.

C(0) > 0 holds: given the other links, a link's conditional law has a continuous positive density, so O_{p₀} is not a.s. constant.

## 2. S3a — uniform tails. PROVED

**Lemma 2 (chessboard estimate, L = 2^k, one block function). PROVED here; nothing cited.**
- A block is a closed unit cube [t, t+1] (t ∈ Λ_L), with all its links, faces included.
- ϑ_t maps block 0 to block t. It is the composition, over directions, of the translation by t_j (t_j even) or the reflection through x_j = (t_j+1)/2 (t_j odd). One checks θ_a ∘ ϑ_t = ϑ_{t′}, with t′_j = 2a − 1 − t_j.
- Let f ≥ 0 be a function of the links of block 0. For a set S of blocks, put Z(S) := μ(∏_{t∈S} f∘ϑ_t).

*Doubling step.* Suppose S ⊂ H₊ := {a ≤ t_j ≤ a + L/2 − 1} (closed half). By Lemma 1's Cauchy–Schwarz with F = ∏_S f∘ϑ_t and G = 1,

  Z(S)² ≤ Z(S ∪ θ_a S) · Z(∅) = Z(S ∪ θ_a S).

Start from S = {0} and use a = −2^i + 1 in direction 1 for i = 0, …, k−1. This doubles S = [−2^i+1, 0] to [−2^{i+1}+1, 0]. The condition S ⊂ H₊ needs 2^i ≤ L/2. Then do directions 2, 3, 4 on slabs.

After 4k doublings, Z({0})^{L⁴} ≤ Z(all). That is, μ(f) ≤ μ(∏_t f∘ϑ_t)^{1/|Λ|}.

*Use.* Take f = 1{O_{p₀} > t}. p₀ lies in a face of block 0, which is allowed because blocks are closed.
- The images are the (1,2) plaquettes with x₃ and x₄ even: |Λ|/4 distinct plaquettes, each hit 4 times. Indicators are idempotent.
- On the event that all images exceed t, βS ≥ t|Λ|/4, where S := Σ_p (1 − cos α_p).
- With e^{−βS} ≤ e^{−βS/2} e^{−t|Λ|/8}:

  μ_L(O_{p₀} > t) ≤ exp(D_L(β) − t/8), where D_L := f_L(β/2) − f_L(β) and f_L(b) := |Λ|⁻¹ log ∫ e^{−bS} dU.

**Lemma 3 (free-energy bounds). PROVED.**

*Forest gauge lemma.* For a forest T of links and a gauge-invariant integrand, ∫ F dU = ∫ F|_{U_T = 1} dU_{T^c}.
Proof: g is defined from U_T, rooted in each tree. Then F(U) = F(U^g), and U^g_T = 1. Integrate U_{T^c} by left/right Haar invariance at fixed U_T, then integrate U_T.

Take T = the temporal links with x₀ ∈ {0, …, L−2}.

*Upper bound.*
- Drop all plaquettes except the (0,i) plaquettes with x₀ ≤ L−2. Since 1 − cos ≥ 0, each dropped factor is ≤ 1.
- Integrate the slices from the top down. Each factor is a Haar change of variables.
- This gives f_L(b) ≤ 3(1 − 1/L) log ẑ(b), with ẑ(b) := ∫ e^{−b(1−cos α)} dU.
- ẑ(b) ≤ (2/π)∫₀^∞ α² e^{−2bα²/π²} dα = (π/2)^{5/2} b^{−3/2}. This uses sin α ≤ α and 1 − cos α ≥ 2α²/π² on [0, π].

*Lower bound.*
- Restrict every unfixed link (3L⁴ + L³ of them) to the ball B_s, with s = β^{−1/2} ≤ 1.
- The class angle is a bi-invariant distance, so α_p ≤ 4s and 1 − cos α_p ≤ 8s². The energy is therefore ≤ 48|Λ|.
- Haar(B_s) = (2/π)∫₀^s sin² ≥ c_H s³, with c_H := 2 sin²1/(3π).
- So f_L(β) ≥ −48 + (3 + 1/L) log(c_H β^{−3/2}).

*Combination.* For β ≥ 1:

  limsup_L D_L(β) ≤ D* := 48 + 3 log((π/2)^{5/2} 2^{3/2}) − 3 log c_H = 60.19.

The (9/2) log β terms cancel, and the 1/L terms vanish.

**Corollary (S3a). PROVED.** For every μ ∈ 𝓛_β with β ≥ 1 and every t ≥ 0,

  μ(O_p > t) ≤ e^{60.2 − t/8}.

{O_p > t} is open, so its μ-probability is ≤ liminf μ_L(O_p > t). This applies to every plaquette by symmetry.

Consequences:
- √β α_p ≤ (π/√2) √O_p, so √β α_p has Gaussian tails uniformly in β and μ.
- All moments of O_p are bounded uniformly.

## 3. S3b — Gaussian limit and DLR. Partly CLAIMED

**Gauge (the repair).**
- No global axial gauge is used in the DLR step. My test H3 shows that the spatial part of a global axial tree inside a box pins 2, 12, 36 links (N = 2, 3, 4) beyond the gauge freedom. Those pins are physical constraints, which is the challenger's circularity in numerical form.
- Instead, fix a box R = [−N, N]⁴ + z, its shell ∂R (sites with |x − z|_∞ = N), and its interior links Λ′_R (links with an interior endpoint).
- Condition on 𝒢^β_R := gauge-invariant functions of the links outside Λ′_R.
- For gauge-invariant w: E[w | links ∉ Λ′_R] = Ψ_w(shell links, exterior). Ψ_w is gauge invariant, so it is 𝒢^β_R-measurable, and E[w | 𝒢^β_R] = Ψ_w.
- Ψ_w may be evaluated in any gauge: (i) a spanning tree T_s of the **shell graph only**, rooted at b ∈ ∂R; (ii) the interior forest T_int consisting of the temporal links from interior sites pointing +e₀. Each tree of T_int meets the shell in exactly one site, so it is a pure gauge choice.

**Gauge-invariant meaning of "compact shell data". PROVED.**
- The 2-skeleton of ∂[−N, N]⁴ ≅ S³ is simply connected. So every non-tree shell link in T_s-gauge equals a product of conjugates of K_N shell plaquette holonomies.
- Hence √β α(U_l) ≤ Σ √β α_q ≤ K_N (π/√2) max_q √O_q.
- "|ψ| ≤ M" is therefore implied by shell plaquette energies ≤ M′. No holonomy variables arise.
- By the Corollary, μ(|ψ| > M) ≤ ε(M) → 0 uniformly in β ≥ 1 and μ.

**Lemma H (nondegeneracy). PROVED; also tested (H1, H2).**
Q(φ) := Σ_{p touching Λ′_R} |dφ_p|², on the unpinned interior links with shell data 0, is positive definite.
Proof: Q = 0 makes φ closed on the contractible box, so φ = dλ. Then λ is constant (= 0) on the connected shell. φ = 0 on T_int then gives λ = 0 on interior sites.
Corollary: with trivial shell, U ≡ 1 is the unique minimiser of the Wilson action. A flat connection on a simply connected complex in tree gauge is trivial.

**L3 (uniform Laplace limit). CLAIMED** (standard argument, written as an outline only).
Write U = exp(iσ·φ/√β) on the unpinned interior links. The conditional law K_β(dφ | ψ) has density
  ∝ exp(−Σ_p H_{β,p}(φ, ψ)) · J(φ/√β) on |φ| < π√β,
where:
- H_{β,p} = β(1 − cos α_p) → ½|dφ_p|² uniformly on compacts. The commutator terms are O(β^{−1/2}(|φ|+|ψ|)³).
- J is the Haar density in exponential coordinates, smooth and positive at 0.

Claim: for every bounded continuous W and every M,

  sup_{|ψ|≤M} |K_β W(ψ) − K_∞ W(ψ)| → 0,

where K_∞ is the Gaussian law with quadratic form Q(φ; ψ) (3 independent colours).

Outline:
- (a) On {|φ| ≥ δ√β}: by Lemma H and compactness, S ≥ η(δ) > 0 for ψ/√β small. So the mass there is ≤ e^{−βη} · β^{3m/2}, which → 0.
- (b) On {|φ| < δ√β}: the bound βS ≥ c|φ|² − C|ψ|² gives a dominating Gaussian, and dominated convergence applies.

What is not written: the explicit choice of δ, c, C in (b), uniformly in |ψ| ≤ M.

**L4 (passage to the limit field). CLAIMED** (bookkeeping not written in full).
Use the global axial tree only to *define* the limit field, not for conditioning. φ_l := √β·log(ΓU)_l on links; this is tight by S3a.
Along some β_k → ∞, the finite-dimensional laws of φ converge to μ_∞. Write F := dφ. Under μ_∞:
- (i) dF = 0 (Bianchi). The six-face lasso product is 1, and BCH is O(β^{−1/2}).
- (ii) The law of F is invariant under global SO(3) colour rotation (gauge invariance of μ_β) and under translations. The lasso holonomies of p from two base points differ by Ad of a loop holonomy, which → 1 in probability.
- (iii) O_{p} → ½|F_p|² in law jointly, and in moments by S3a (uniform integrability).

**DLR in the limit.** For colour-invariant bounded continuous w(F_{in}, F_{out}):
- E_{β}[w] = E_β[Ψ̃_β(ψ, Φ^b_out)] + o(1).
- Replace Ψ̃_β by Ψ̃_∞ using L3 on {|ψ| ≤ M}, and the tail bound off it.
- Ψ̃_∞ is continuous. Pass to the limit.
- Remove colour invariance by averaging over SO(3), using the equivariance of K_∞.

Result: for every box R, the conditional law of (F_p)_{p ∈ P_R} given 𝒢_R := σ(F_q : q ∉ P_R) is the Maxwell–Dirichlet Gaussian. Its covariance C^R is deterministic. Its mean h^R = d A*, where A* minimises |dA|² over Λ′_R; so (d*h^R)_l = 0 for l ∈ Λ′_R.
*Status:* PROVED given L3 and L4.

## 4. S3c — bypassed. PROVED (given §3)

**Lemma D (C^R → P). PROVED.**
- ⟨f, C^R f⟩ = sup{⟨f, dA⟩² / |dA|² : A supported on Λ′_R}. This is the conditional variance of a Gaussian modulo its kernel.
- This is nondecreasing in R. Its limit is |P f|², where P is the projection in ℓ²(plaquettes) onto the closure of d(finite 1-forms).
- In Fourier, for k ≠ 0, P(k) = d̂d̂*/k̂². Its (12,12) entry is (k̂₁² + k̂₂²)/k̂². Polarisation gives P_{p₀p_n} = G(n).
- Test M1: C^N_{pp} = 0.2917, 0.4927, 0.4992 for N = 2, 4, 6, increasing towards G(0) = 1/2. C⁶(p₀, p₁) = 0.0681 vs G(1) = 0.0689.

**Lemma R (decomposition without classification). PROVED.**
𝒢_R decreases as R grows. Let 𝒢_∞ := ∩_R 𝒢_R.
- *Downward martingale theorem* (Lévy; any graduate probability text): h^R_p = E[F_p | 𝒢_R] → h_p := E[F_p | 𝒢_∞] in L². The moments come from S3a.
- ξ^R := F − h^R is N(0, C^R) and independent of 𝒢_R ⊇ 𝒢_∞. In the limit, ξ := F − h is centred Gaussian with covariance P, independent of 𝒢_∞, and hence independent of h. The three colours are independent copies.
- dh = E[dF | 𝒢_∞] = 0.
- d*h = 0: (d*h^R)_l = 0 once l ∈ Λ′_R, and pass to the L² limit.
- E[h_p h_q] = E[F_p F_q] − P_{pq} is translation invariant. So h is second-order stationary.
- Δh = (dd* + d*d)h = 0, and the lattice Hodge Laplacian acts componentwise as the scalar Laplacian. So the spectral measure of each component is carried by {k̂² = 0} = {0}.
- Therefore E|h_p − h_{p+a}|² = 0: **h = f is a random constant**, independent of ξ.

**Lemma G (G(n) > 0, decay). PROVED; tested (G1–G4).**
Doing the k₀ integral exactly,

  G(n) = ∫_{[−π,π]³} (k̂₁² + k̂₂²) e^{−mn} / (2 sinh m) dk/(2π)³, with cosh m = 1 + k̂²_spatial/2.

Hence 0 < G(n) ≤ G(0) = ½. On the cube |k_i| ≤ 1/(√3 n) we have m ≤ 1/n, which gives

  G(n) ≥ (4/π²)(16r⁵/3) e^{−1} / (2 sinh 1) / (2π)³, with r = 1/(√3 n).

So G(n) ≥ c n^{−5}.

**The inequality. PROVED.** With F = ξ + f and X_n = ½|F_{p_n}|²:

  Cov(X₀, X_n) = (3/2)G(n)² + G(n) E|f|² + ¼ Var|f|²,

and the same with G(0) for Var X₀. Each term's ratio is ≥ (G(n)/G(0))², so the ratio of sums is too. The limit Var ≥ 3/8 > 0. By L4(iii) the β-ratios converge to this, along a subsequence extracted from any sequence (β_k, μ_k) that nearly attains the liminf of the infimum. This proves Theorem B′, given L3 and L4.

## 5. Theorem B′ as it stands (one page)

Statement as in §0. Proof chain:

| step | content | tag |
|---|---|---|
| Lemma 1, 1′, transfer matrix | site-plane RP; limit states; T a self-adjoint contraction | PROVED |
| S1, S2 | spectral bound; reduction | PROVED (S2's Lean check from v1, not rerun) |
| Lemma 2 | chessboard estimate, L = 2^k | PROVED |
| Lemma 3 + Corollary | e^{60.2 − t/8} tails, uniform | PROVED |
| gauge repair, compactness, Lemma H | conditioning on gauge-invariant data, shell-only tree | PROVED |
| L3 | uniform Laplace limit of the DLR kernel | **CLAIMED** |
| L4 | limit field: Bianchi, translation and colour invariance, uniform integrability | **CLAIMED** (bookkeeping) |
| DLR in the limit | given L3 and L4 | PROVED |
| Lemma D, R, G, inequality | replaces the Gibbs classification | PROVED |

**Remaining CLAIMED:** L3 and L4. **MISSING:** none.
**Restriction:** L = 2^k. Removing it needs the FILS/Biskup general chessboard argument, which was not read here.

## 6. Discriminators

| model | where the chain goes | correct? |
|---|---|---|
| finite G, d = 4 | Lemmas 1–3 hold. The rescaling φ = √β log U does not exist, so **L3 fails**. The limit is δ₀, Var → 0, and Lemma R has no nondegenerate ξ. | yes: (B) is false there |
| U(1), d = 4 | Everything goes through. L3 is simpler (no commutators), ẑ ~ b^{−1/2}, one colour, same c(n). | yes: no gap at weak coupling (Fröhlich–Spencer, abstract level only) |
| SU(2), d = 3 | Lemmas 1–3 hold (2 spatial directions). Lemma D is dimension-free. Lemma G in d = 3 is a 2D spatial integral, still positive and polynomial. The chain gives m → 0. | yes: the expected lattice gap ~ g² → 0 in lattice units |
| any G, d = 2 | Here P = identity on 2-forms (ker d* = 0 in ℓ²), so G(n) = 0 for n ≥ 1 and c(n) = 0. The chain gives nothing. | yes, consistent with v1's 2D row |

The non-abelian structure enters only in L3 and L4, as O(β^{−1/2}) error terms. Nothing in the argument distinguishes SU(2) from U(1). That is correct, because the conclusion holds for both, and it is also why this route says nothing about the mass gap (A).
