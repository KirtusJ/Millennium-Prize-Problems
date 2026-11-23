**Theorem S is a conditional theorem with five lattice hypotheses, H0 to H4, plus three further hypotheses that it does not conclude: (E1) nontriviality, (E2) asymptotic freedom and (G) other groups. For SU(2), two of the five are proved: H0, the lattice axioms (cited and re-derived in this program), and H2, which is (B), Theorem B′ (one model family, not independently reviewed). H1 is (A), the lattice mass gap, and it is the problem. H3 and H4 are open.**

Worker c1-OS (child of Director Z4), 23 November 2026, for Kirtus Justus. Prepared with assistance from Claude (Anthropic). Same model family as the director, so this is not independent review.

Tags used below: **PROVED** (full proof here, sometimes a sketch with every constant's dependence stated), **CITED** (locator read), **CITED-2nd** (read only in a secondary source, which is named), **CLAIMED** (from memory or unread), **MISSING**.

---

## 0. What the whole thing amounts to

This is Prokhorov/Arzelà–Ascoli, limits of quadratic forms, and the OS reconstruction theorem, applied to hypotheses that hold all of the difficulty. As with Theorem R′, its content is its hypotheses. Jaffe and Witten exclude "existence by compactness alone" unless other techniques establish the properties of the limit (GROUNDING.md §1). Theorem S does not escape that: here the properties are assumed, as H1, H3 and H4.

## 1. Setting

- For each β ≥ β₁, μ_β is a probability measure on SU(2)^{edges of ℤ⁴}, chosen from 𝓛_β, the weak limit points of the periodic Wilson states on boxes of side 2^k (THEOREM_B.md). Expectations are written ⟨·⟩_β.
- **Fields.** Fix a finite family O₁, …, O_r of *site-scalar* observables. Each O_i(n) is a bounded, real, gauge-invariant function of the links within lattice distance 1 of the site n, invariant under the hypercubic group W₄ (the 384 signed permutations of axes) acting about n. Example: O(n) = Σ over the 24 plaquettes having n as a corner of ½ Tr U_p. Write Ô_i(n) := O_i(n) − ⟨O_i⟩_β.
  *Why site-scalar:* a reflection in the site plane through n maps Ô_i(n) to Ô_i(θn) **exactly**, with no shift of the base point.
- **Gap and scale.** T_β is the transfer matrix for time reflections in site planes (H0). m(β) := −log ‖T_β restricted to Ω_β^⊥‖ is the gap, ξ := 1/m, and **a(β) := m(β)**, so the unit of length is the correlation length. N_β := 2⌊ξ/2⌋.
- **Normalization.** Z_i(β)² := ⟨Ô_i(0) Ô_i(N_β e₀)⟩_β.
- **Lattice Schwinger functions.** For x = (x₁, …, x_k) ∈ (aℤ⁴)^k and indices ι = (i₁, …, i_k):
  S^β_ι(x) := Π_j Z_{i_j}(β)^{−1} · ⟨Π_j Ô_{i_j}(x_j/a)⟩_β.
  As distributions: S^β_ι(f) := a^{4k} Σ_{x ∈ (aℤ⁴)^k} S^β_ι(x) f(x) for f ∈ ⁰𝒮(ℝ^{4k}).
- ⁰𝒮(ℝ^{4k}) is the Schwartz functions that vanish, with all derivatives, wherever x_i = x_j (KQR eq. 2.25). ⁰𝒮₊ is those with support in {0 < t₁ < … < t_k}. A coinciding lattice configuration therefore contributes 0.
- **Choice of fields: lattice-local fields, taken to points.** There is no flow, so neither problem in A1_LEDGER.md arises. (i) With no slice flow there is no unregularized electric part. Instead every point is a local composite, renormalized multiplicatively by Z_i(β) and taken only at non-coinciding points, which is exactly what ⁰𝒮 allows. (ii) Reflection positivity is the exact lattice RP of products of site-scalar observables in t ≥ 0, so no flowed algebra is needed. The price is that all short-distance control goes into hypothesis H3.

## 2. The hypotheses (each a statement about the lattice theories, uniform as β → ∞)

- **H0 (lattice axioms).** μ_β is invariant under the translations ℤ⁴ and under W₄. It is reflection positive for reflections in every site hyperplane {x_μ = c}, c ∈ ℤ: ⟨\overline{Θ F}·F⟩_β ≥ 0 for every bounded F depending only on links in {x_μ ≥ c}.
- **H1 = (A) (gap).** m(β) > 0 for all β ≥ β₁ (the infinite-volume state μ_β).
- **H2 = (B) (criticality).** m(β) → 0 as β → ∞.
- **H3 (uniform regularity in units of the gap).** There are constants α, γ, b, D < ∞, and for each k and δ > 0 a constant L_{k,δ}, such that for all β ≥ β₁, all k, all ι:
  - (a) Z_i(β) > 0.
  - (b) *Growth bound:* |S^β_ι(x)| ≤ α γ^k (k!)^b Π_{j=1}^{k} max(1, ρ_j(x)^{−D}) for x ∈ (aℤ⁴)^k with distinct points, where ρ_j(x) := min_{l≠j} |x_j − x_l|.
  - (c) *Equicontinuity:* |S^β_ι(x) − S^β_ι(y)| ≤ L_{k,δ} |x − y| for x, y ∈ (aℤ⁴)^k with all pairwise distances ≥ δ.
- **H4 (asymptotic rotation invariance, one rotation).** For one angle θ with θ/π irrational, let R_θ be the rotation in the (x₁, x₂)-plane and [y]_a the nearest point of aℤ⁴ (ties broken lexicographically). For every k, ι, δ > 0 and R < ∞: sup |S^β_ι([R_θ x]_a) − S^β_ι([x]_a)| → 0 as β → ∞, the sup taken over configurations in the ball of radius R with pairwise distances ≥ δ.

Not concluded, kept separate:
- **(E1) Interacting.** See §5. The form the brief suggests is too weak, and a free field passes it.
- **(E2) Asymptotic freedom at short distance.** For the action density, S_{OO}(0, x) behaves as c·|x|^{−8}·(log 1/|x|)^{−2}·(1 + o(1)) as x → 0. The exponent of the logarithm is CLAIMED from memory of the RG invariance of (β(g)/g)·F²; not read.
- **(G)** The same hypotheses for every compact simple group. Theorem S's proof uses no property of SU(2), so (G) reduces to H1 to H4 for each group. H0 holds for every compact group (Osterwalder–Seiler, CLAIMED: snippets only).

## 3. Theorem S

> **Theorem S.** Assume H0 to H4. Then there is a sequence β_j → ∞ such that, for every k and ι:
> 1. S^{β_j}_ι → S_ι uniformly on compact sets of δ-separated configurations (through lattice approximants), with S_ι continuous on {pairwise distinct points}; and S^{β_j}_ι(f) → S_ι(f) := ∫ S_ι f for every f ∈ ⁰𝒮(ℝ^{4k}).
> 2. The S_ι satisfy the Osterwalder–Schrader axioms in the 1975 form: E0′ (linear growth), E1 (Euclidean covariance under translations and O(4)), E2 (reflection positivity), E3 (symmetry), and E4 (cluster).
> 3. S_{ii}(0, e₀) = 1 for every i, so the theory is not empty.
> 4. By the OS II reconstruction theorem there is a Wightman theory with fields φ₁, …, φ_r. Its vacuum is the unique translation-invariant vector, and the joint spectrum of (H, P⃗) on Ω^⊥ lies in {p² ≥ 1, p⁰ > 0}: **mass gap ≥ 1** in these units.
>
> The theorem asserts nothing about uniqueness of the limit, interaction (E1), short-distance behaviour (E2) or other groups (G).

**OS version used** (CITED-2nd). Projecteuclid blocked every fetch, so neither OS paper was read. Both are read through Kravchuk, Qiao and Rychkov, "Distributions in CFT II. Minkowski space", arXiv:2104.02090 (full text, via pdftotext; §2.2 eqs. 2.21–2.25, §9.1–9.2 eqs. 9.16–9.18, footnote 20).
- **E0′:** there is an integer s with |S_n(f)| ≤ σ_n |f|_{n·s} for f ∈ ⁰𝒮, where σ_n ≤ α(n!)^β (KQR eq. 9.18).
- **OS II (1975):** E0′ together with E1–E3 implies the Wightman axioms.
- **The 1973 error:** Lemma 8.8 of OS 1973 is wrong (KQR §9.2.1).
- **E4:** E4 is the OS cluster property for spatial translations (KQR fn. 20).
- **From memory (CLAIMED):** the axiom numbering E0–E3, and that, given E0′–E3, E4 is equivalent to uniqueness of the vacuum.

**Glimm–Jaffe's formulation is not used.** It is stated for a measure on 𝒮′, with smeared fields at coinciding points. Composite fields taken to points do not give that.

## 4. Proof, step by step

| # | Step | Tag |
|---|---|---|
| 1 | **Compactness.** Extend each lattice function S^β_ι to (ℝ⁴)^k by piecewise-linear interpolation on the simplices of the lattice; this keeps H3(b, c) up to constant factors. On K_{ℓ} := {configurations in the ball of radius ℓ with pairwise distances ≥ 1/ℓ} the family is uniformly bounded (H3b) and equi-Lipschitz (H3c). Arzelà–Ascoli applies on each K_ℓ, and a diagonal extraction over the countably many (k, ι, ℓ) gives β_j and continuous limits S_ι. | PROVED |
| 2 | **Distribution property and E0′.** *Lemma.* If f ∈ ⁰𝒮(ℝ^{4k}) and M ≥ 1, then \|f(x)\| ≤ (4k)^M/M! · 2^P · sup_y (1+\|y\|)^P \|∂^M f(y)\| · min_{i<j}\|x_i − x_j\|^M · (1+\|x\|)^{−P} whenever min\|x_i − x_j\| ≤ 1. *Proof:* Taylor's formula along the segment to the nearest point of {x_i = x_j}, whose length is \|x_i − x_j\|/√2 < 1. There all derivatives of order < M vanish, and Σ_{\|α\|=M} M!/α! = (4k)^M. When min ≥ 1, use the weight directly. Take M = Dk + 1 and P = 4k + 1, and use Π_j max(1, ρ_j^{−D}) ≤ max(1, ρ_min^{−Dk}). Then a^{4k} Σ_x \|S^β(x) f(x)\| ≤ α γ^k (k!)^b C^k \|f\|_{(D+6)k} uniformly in β. The Riemann sum of the majorant is bounded by its integral up to a constant: count lattice configurations with ρ_min in dyadic shells. Convergence of S^{β_j}(f) to ∫ S f: split into ρ_min ≥ δ inside the ball of radius R, where convergence is uniform by step 1 and Riemann sums of continuous functions converge; the remainder is ≤ C(δ + R^{−1}) uniformly in β. The bound passes to the limit and gives E0′ with s = D + 6 and σ_k ≤ α′(k!)^{b+ε}. | PROVED (sketch, constants traced) |
| 3 | **Translations.** S^β(x + a n) = S^β(x) for n ∈ ℤ⁴ by H0. For y ∈ ℝ⁴ choose n_j with a_j n_j → y (possible since a_j → 0 by H2). By step 1 and H3(c), S(x + y) = lim S^{β_j}(x + a_j n_j) = S(x). | PROVED |
| 4 | **Rotations.** The set 𝒢 := {R ∈ O(4): S_ι(Rx) = S_ι(x) for all k, ι, x} is a closed subgroup, because each S_ι is continuous. W₄ ⊂ 𝒢: by H0, μ_β is W₄-invariant, aℤ⁴ is W₄-invariant, and each O_i is W₄-scalar. R_θ ∈ 𝒢 by H4 together with H3(c) (rounding costs O(a)). Because θ/π is irrational, the powers of R_θ are dense in SO(2)₁₂ (Kronecker), so SO(2)₁₂ ⊂ 𝒢. Conjugating by permutations in W₄ gives SO(2)_{μν} for all six planes. Their generators span so(4), so they generate SO(4). With the reflections in W₄, 𝒢 = O(4). | PROVED |
| 5 | **Symmetry (E3) and reality.** The lattice fields are commuting real random variables, so S^β_ι(x) is symmetric under simultaneous permutation of points and indices, and real. Both properties pass to the limit. | PROVED |
| 6 | **Reflection positivity (E2).** Take finitely many f_k ∈ ⁰𝒮₊(ℝ^{4k}) (with indices) and set F_β := Σ_k a^{4k} Σ_x f_k(x) Π_j Ô_{i_j}(x_j/a). On the lattice the support of f_k lies in t > 0, so only sites with t ≥ a contribute (f vanishes at t = 0), and each Ô(n) with n₀ ≥ 1 depends on links in {t ≥ 0}. The sum converges in L²(μ_β) because the Ô are bounded and f is Schwartz. Site-scalarity gives ΘÔ_i(n) = Ô_i(θn) exactly. H0 gives 0 ≤ ⟨\overline{ΘF_β} F_β⟩ = Σ_{k,l} S^β(Θf_k^* ⊗ f_l) times positive Z factors, which are absorbed into the normalization. Each term converges by step 2, and positivity of a finite quadratic form is closed under pointwise limits of its coefficients. *Convergence needed:* only S^{β_j}(g) → S(g) for the finitely many g = Θf_k^* ⊗ f_l ∈ ⁰𝒮. | PROVED |
| 7 | **Reconstruction.** E0′ and E1–E3 give a Wightman theory. Its Hilbert space is the completion of ⁰𝒮₊ under the E2 form; e^{−tH} acts by time translation t ≥ 0, and Ω is the class of the constant 1. | CITED-2nd (KQR §9.2 on OS II; §2.2 for the form). The identification of e^{−tH} is CLAIMED from memory of OS 1973 §4 |
| 8 | **Gap ≥ 1 (extends Theorem R′ to n-point functions).** For Ψ = [f] in the dense set, let F(t) := ⟨Ψ, e^{−tH} Ψ⟩ − \|⟨Ω, Ψ⟩\|² = S(Θf^* ⊗ f_t) − \|S(f)\|². On the lattice, with t ∈ aℤ: F^β(t) = ⟨v, e^{−tH_β/a} v⟩ for v := F_β Ω − ⟨F_β⟩Ω ⟂ Ω. H_β/a ≥ 1 on Ω^⊥ by H1 and the choice a = m, so **F^β(t+s) ≤ e^{−s} F^β(t)** for t, s ≥ 0. Off-lattice t is handled by H3(c). This inequality is closed under pointwise limits, so F(t+s) ≤ e^{−s} F(t). If the spectral measure ν_Ψ of H on Ω^⊥ gave mass c > 0 to [0, 1−ε], then F(s) ≥ c e^{−(1−ε)s}, which contradicts F(s) ≤ e^{−s} F(0) for large s. So E_H([0,1)) Ψ_⊥ = 0 on a dense set, hence everywhere. *Uniform bound needed:* only H1 with the exact scale a = m. No uniform bound on the n-point functions beyond H3 is needed, because the gap passes through the inequality, not through decay estimates. | PROVED |
| 9 | **Unique vacuum.** A translation-invariant vector is time-invariant, and by step 8 time-invariant vectors are multiples of Ω. | PROVED |
| 10 | **Mass hyperboloid.** Boosts are unitarily implemented, so the joint spectrum is Lorentz invariant. A spectral point with 0 ≤ p² < 1 and p ≠ 0 boosts to energy < 1 (or arbitrarily small energy when p² = 0), which contradicts step 8. | PROVED, given step 7 |
| 11 | **Cluster (E4).** Approximate f and g by compactly supported test functions; E0′ controls the error. Rotate the configuration (step 4) so that the spatial direction a becomes e₀. For large λ the support of the translated g lies above a time plane and the other factor below it, so the term equals ⟨Ψ′, e^{−(λ−c)H} Ψ″⟩. By step 8 this tends to ⟨Ψ′, Ω⟩⟨Ω, Ψ″⟩ with error e^{−(λ−c)}: exponential clustering at rate ≥ 1. | PROVED (sketch) |
| 12 | **Not empty.** S^β_{ii}(0, aN e₀) = 1 and \|aN − 1\| ≤ 2a, so S_{ii}(0, e₀) = 1 by H3(c). Smear near ±e₀/2: Ψ_f ≠ 0 and ⟨Ω, Ψ_f⟩ = S_i(f) = 0 (the fields are centered), so H has spectrum in [1, ∞) and a finite mass exists. | PROVED |

**Relation to attempt 1.** H3(b) with k = 2, together with the normalization, gives Z^{−2} C_β(ξ/2^j) ≤ 2αγ² 2^{2jD}. That is (C⁺) of A1_REDUCTION.md, hence (C). Theorem R′ is the case k = 2, x on the time axis, of steps 1 and 8.

## 5. (E1) as the brief suggests it is too weak

The brief's suggested form is: a renormalized connected four-point function bounded away from zero, i.e. "the limit is not a generalized free field". **The free field passes it.** For the Wick square :φ²: of the free field, the truncated 3- and 4-point functions are nonzero (they are cycle graphs of S₂), so :φ²: is not a generalized free field. Yet the theory is free.

Since Yang–Mills has no elementary field, a test on composite fields cannot detect interaction in this form. A correct (E1) must be a statement about the theory, for example a nontrivial Haag–Ruelle S-matrix for the lightest particle. Its lattice proxy, a nonzero two-particle energy shift in finite volume (Lüscher), is CLAIMED from memory and not formulated here as a theorem. **(E1) is left as: the reconstructed theory has a non-trivial S-matrix (MISSING as a lattice statement).**

## 6. Known-answer test: the 4D lattice free field, m → 0

Program: `freefield_S.py`, output `freefield_S.out`, register check K2. Scale a = E₀(m) = 2 asinh(m/2), the exact transfer-matrix gap. Fields φ and :φ²:.

| Hypothesis | Free field | How |
|---|---|---|
| H0 | holds | Nearest-neighbour Gaussian measure is RP in site planes (CLAIMED, standard). Numerical illustration P8: 40 random points with seed 12345, minimum eigenvalue +3.1·10⁻¹⁰ ≥ 0 |
| H1 | holds, gap exactly 2 asinh(m/2) | One-particle energies 2 asinh(½√(m² + Σ 4 sin²(p_i/2))), minimum at p = 0. Numerically P1: zero-momentum correlator equals e^{−E₀n}/(2 sinh E₀) to 10⁻¹³ (n ≥ 1), 4 of 4 masses |
| H2 | holds | a → 0 (P2) |
| H3(a) | holds | G > 0 |
| H3(b) | holds with D = 1, b = 1/2 for φ; D = 2, b = 1 for :φ²: | Wick's theorem; each pair factor \|x_i − x_j\|^{−2} ≤ ρ_i^{−1}ρ_j^{−1}. Needs G_m(n) ≤ C/\|n\|² (CLAIMED, Green-function asymptotics) and G_m(N e₀) ≍ a². Numerically P6: sup \|x\|² S₂ = 1.64, 2.00, 2.11, 2.15 for m = 1/4 … 1/32 (bounded, converging) |
| H3(c) | holds | P7: Lipschitz constant on the axis for \|x\| ≥ ½: 5.1, 10.0, 15.0, 19.1, below the continuum value 25.1 (it approaches it as a → 0) |
| H4 | holds | P5: \|S(0,cos 1, sin 1,0) − S(0,1,0,0)\| = 3.9·10⁻², 2.7·10⁻², 6.7·10⁻³; \|S(1,0,0,0) − S(½,½,½,½)\| = 3.7·10⁻², 9.0·10⁻³, 2.2·10⁻³ (m = 1/8, 1/16, 1/32). Proof that the limit is isotropic: CLAIMED (local CLT), numerics only |
| Conclusion | free field of mass 1, S₂(x) = K₁(\|x\|)/(\|x\| K₁(1)) | P4: relative error at m = 1/32 ≤ 2.4·10⁻³ at all 8 points, including off-axis (½,½,½,½), (0.6,0.8,1.2,0.4) and the irrational-rotation point. P9: :φ²: gives the square, as Wick predicts |
| (E1) | fails for φ (truncated 4-point = 0); "passes" for :φ²: | see §5 |

**No hypothesis fails for the free field, so Theorem S is not mis-stated on this test.** Before running, I had considered a = m (the bare mass). The exact gap is 2 asinh(m/2), and the statement uses the gap. The difference vanishes as m → 0.

The child session (T7) and the grandchild (T11) independently computed m^{−2} G_m at 4 points for a = m. I reran their code (check K3, identical bytes), and my program reproduces two of their numbers to 10⁻⁹ (P0b).

## 7. Discriminators

| Model | H0 | H1 | H2 | H3 | H4 | E1 | Outcome |
|---|---|---|---|---|---|---|---|
| Free lattice field, m → 0 | ✓ | ✓ | ✓ | ✓ | ✓ (numerics) | ✗ | Free field of mass 1: correct |
| Compact U(1), 4D, β → ∞ | ✓ | **✗** (massless photon: Guth; Fröhlich–Spencer, abstracts per GROUNDING) | ✓ (Theorem B′ discriminator) | undefined (a = m = 0) | – | – | chain stops at H1: correct |
| 4D Ising, β ↑ β_c, spin field | ✓ (CLAIMED) | ✓ above T_c (sharpness: Aizenman–Barsky–Fernández, CLAIMED) | ✓ (CLAIMED) | expected (Gaussian-domination and Lebowitz bounds, CLAIMED) | **unknown**: no rigorous rotation result found for 4D (Sakai's lace expansion gives isotropic critical 2-point asymptotics only for d > 4, spread-out or d ≫ 4: arXiv math-ph/0510093, abstract) | **✗** Gaussian limit at or near criticality (Aizenman–Duminil-Copin, arXiv:1912.07973, abstract read) | if H3 and H4 hold, Theorem S gives a Gaussian theory: consistent, E1 not concluded |
| SU(2), 4D | ✓ (THEOREM_B Lemma 1, 1′; Osterwalder–Seiler CLAIMED) | **open** (the problem) | ✓ Theorem B′ | open | open | open | – |

Rotation restoration known rigorously: in two dimensions, large-scale rotational invariance of the critical random-cluster model for 1 ≤ q ≤ 4 (Duminil-Copin, Kozlowski, Krachun, Manolescu, Oulamara, arXiv:2012.11672, abstract). This is for that model's correlations, not a full field-theory limit. Nothing rigorous was found for four-dimensional interacting models.

## 8. THE LIST

| Hyp. | Status for SU(2) | Implied by / implies |
|---|---|---|
| H0 lattice axioms | **proved** (THEOREM_B Lemma 1, 1′, re-derived by challengers; Osterwalder–Seiler CLAIMED) | – |
| H1 = (A) gap | **no proof; four routes broken** (A1_LEDGER). Expected (lattice glueball masses) | implies a unique vacuum on the lattice; with H0 it gives exponential clustering on the lattice |
| H2 = (B) | **proved** (Theorem B′, one family; C4 with a rate) | independent of H1. True for U(1) too |
| H3 regularity (all k) | **no evidence beyond perturbation theory and the free field**. Proved for the free field. Contains (C⁺) of A1, against which the ledger's three-spacing data lean weakly, but only in its stronger form (C′), which H3 does not need. The uniform k-point bound is UV stability for gauge-invariant composites, which Jaffe–Witten list as open beyond Bałaban | H3 ⇒ (C⁺) ⇒ (C). Not implied by H1 + H2 |
| H4 one irrational rotation | **open.** Expected (hypercubic artefacts are irrelevant operators of dimension 6, CLAIMED). Proved for the free field only in the sense of numerics plus the local CLT (CLAIMED) | with W₄ invariance gives O(4) (step 4) |
| (E1) | **open; the brief's form is too weak** (§5). Needs an S-matrix statement | not implied by H0 to H4 |
| (E2) | open. Expected from perturbation theory | would imply (E1) heuristically, not by proof |
| (G) | H0 proved for all compact groups (CLAIMED); H2 expected by the same proof (non-abelian structure enters only as error terms); H1, H3, H4 open | Theorem S itself is group-independent |

## 9. Lean

Not used. /home/user/z4-lean/READY exists. Nothing in this file is claimed in Lean.
