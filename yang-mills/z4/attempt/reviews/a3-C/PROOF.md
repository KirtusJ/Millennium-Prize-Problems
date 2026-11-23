# Claim (C) for SU(2), d = 4, assuming (A) and (B): the chain and where it stops

Worker a3-C (builder, positive arc), 23 November 2026, for Director Z4. Principal: Kirtus Justus.

**This is not a proof of (C).** The chain has one MISSING step (step 6, inequality (C′) for the slice-flowed magnetic density of SU(2)). It also has one CLAIMED step (step 7, needed only for the lattice-local variant), and step 0 rests on an assumption. Everything else is PROVED (elementary spectral theory) or CITED at abstract level. What the chain does is reduce (C) to a single one-time-step inequality, and it shows that (C) cannot be made true by smearing in Euclidean time. It also shows that (C) does not rule out a single-atom limit.

Notation as in A1_REDUCTION.md §1: T = e^(−H) on 𝓗_β, ψ ⟂ Ω, ν its spectral measure, C(n) = ∫e^(−nε)dν(ε) for real n ≥ 0, m = m(β) the infinite-volume gap, ξ = 1/m, E = εξ. **Effective mass**: u(n) := −(d/dn) log C(n).

## The chain

**Step 0 (CITED, abstract level only + assumption).** For the Wilson action, physical (reflection) positivity holds and gives a positive self-adjoint transfer matrix (Osterwalder–Seiler, Ann. Phys. 110 (1978); Lüscher, CMP 54 (1977) 283). Locator: LIT_RIGOROUS.md rows "R2 Osterwalder-Seiler" and "R2 Lüscher 1977". Both were read at abstract level only, and strict positivity T > 0 was not read. Hypothesis check: the use here needs (i) the infinite-volume state at every β and (ii) T ≥ 0, so that C(n) is a Laplace transform for real n. (ii) is in the abstracts. (i) is **not** in the literature at large β; it is the standing assumption of A1 §1 and §4.5. Order of limits: L → ∞ at fixed β first, then β → ∞. Every constant below must be uniform in β. The volume enters only through this step.

**Step 1 (PROVED). Log-convexity and effective mass.** For n > 0, C is finite and smooth (ν is finite, ε ≥ 0, and ε^k e^(−nε) is bounded, so dominated convergence applies). (log C)″(n) = Var_n(ε) ≥ 0, where the variance is taken under the probability measure e^(−nε)dν/C(n). Hence:
(1a) log C is convex and decreasing.
(1b) u(n) = ∫ε e^(−nε)dν / C(n) = ⟨φ_n, Hφ_n⟩/‖φ_n‖², with φ_n = e^(−nH/2)ψ. This is the mean energy of the propagated vector.
(1c) u is nonincreasing, and u(n) ≥ m₀ := min supp ν ≥ m.
(1d) u(n) → m₀ as n → ∞: the measure e^(−nε)dν/C(n) concentrates at m₀.
(1e) For integers, C(n+1)/C(n) is nondecreasing.
Step 1 uses only Step 0. The group, the dimension and the volume do not enter.

**Step 2 (PROVED). Equivalences of (C) (mechanism (a)).**
(2a) If u(ξ/2) ≤ K m, then (C) holds with D = e^(K/2). Proof: log C(ξ/2) − log C(ξ) = ∫_{ξ/2}^{ξ} u ≤ (ξ/2)u(ξ/2).
(2b) If (C) holds with D, then u(ξ) ≤ 2 log D · m. Proof: the same integral is ≥ (ξ/2)u(ξ), because u is nonincreasing.
So (C) is equivalent, up to constants and up to moving the time from ξ/2 to ξ, to the statement that the mean energy of e^(−cξH/2)ψ is O(m). By (1b), "effective mass" and "mean energy of the propagated vector" are the same number.
(2c) Spectral weight. Fix K. Suppose ∫_{E>K} e^(−E/2)dν ≤ B ∫_{E≤K} e^(−E)dν. Then C(ξ/2) ≤ (e^(K/2) + B) C(ξ). Conversely, (C) with D implies this condition with K = 2 log(2D) and B = 2D: by (R2), ∫_{E>K}e^(−E)dν ≤ De^(−K/2)C(ξ) = C(ξ)/2.
Lean: the finite-sum form of the forward direction of (2c) is `A3C.weight_implies_C` (lean/A3C.lean). It compiles with exit 0 and uses only the axioms propext, Classical.choice and Quot.sound.

**Step 3 (PROVED). The one-step criterion (C′) implies (C) and (C⁺) with a single constant.**
(C′): 1 − C_β(1)/C_β(0) ≤ K′ m(β) for all β ≥ β₁.
Proof. Put q = C(1)/C(0). By convexity, the slope of log C on [a, ∞) with a ≥ 1 is at most the chord slope on [0, 1], which is log(1/q). So for ξ/2^j ≥ 1,
 log C(ξ/2^j) − log C(ξ) ≤ ξ·log(1/q) ≤ ξ·2K′m = 2K′, using −log(1 − x) ≤ 2x for x ≤ 1/2, that is ξ ≥ 2K′.
Hence (C) and (C⁺) hold with D_j = e^(2K′) for every j. The integer form "q^k C(n) ≤ C(n+k)" is `A3C.step_chain` in Lean (exit 0, standard axioms).
(C′) is implied by M₁/M₀ := ⟨ψ,Hψ⟩/‖ψ‖² ≤ K′m, because log(1/q) ≤ u(0) = M₁/M₀ by (1c). This is the bounded physical energy at time zero, B3 of SPATIAL_FLOW.md.

**Step 4 (PROVED). (C′) is false for every lattice-local observable in the free discriminator, so step 3 is useless there.**
For the free field φ(0)², measured ξ(1 − C(1)/C(0)) = 0.963ξ (P4 of test_c.py, ξ = 4…256). C(1)/C(0) tends to a lattice constant (0.0373), so (C′) fails. (C) itself holds there (step 9). So (C′) is sufficient and not necessary, and it applies only to vectors smeared on the physical scale. This forces the choice in step 6.

**Step 5 (PROVED). Doubling (mechanism (b)).**
(5a) Suppose u(n₀) ≤ K′/n₀ and the additive doubling u(2n) ≤ u(n)/2 + A·m holds for n₀ ≤ n ≤ ξ/4, with ξ/(2n₀) a power of 2. Iterating gives u(ξ/2) ≤ 2^(−k)K′/n₀ + 2Am with n₀2^k = ξ/2, that is u(ξ/2) ≤ (2K′ + 2A)m. So (C) holds with D = e^(K′+A). Running the same iteration to ξ/2^j gives (C⁺) with D_j ≤ e^(j(K′+A)), which is power-law growth in 2^j.
(5b) The multiplicative form u(2n) ≤ (1/2 + δ)u(n) with fixed δ > 0 is **not enough**. It permits u(ξ/2) ≍ (K′/ξ)(ξ/n₀)^(log₂(1+2δ)), which is unbounded in units of m. The free field satisfies (5a) with A = 1/2, since u(n) ≈ m + p/n.
(5c) The converse, from (C⁺) with geometric D_j to pointwise doubling, was NOT CHECKED. (C⁺) controls only averages of u over dyadic intervals.
For a lattice-local ψ the start u(1) ≤ log(C(0)/C(1)) = O(1) needs C(1)/C(0) ≥ c > 0 uniformly in β (step 7, CLAIMED). The doubling inequality between n₀ and ξ is then MISSING for SU(2). It is no weaker than (C) and is the same statement in a different form.

**Step 6 (MISSING). The inequality on which (C) rests for SU(2).**
For the slice-flowed magnetic density ψ_β = O_{β,s}(f) of SPATIAL_FLOW.md §2, at flow time s·ξ(β)² lattice units, fixed s > 0 and fixed f, it is needed that
 **(C′) 1 − C_β(1)/C_β(0) ≤ K′(s,f)·m(β) for all β ≥ β₁, in infinite volume,**
or the stronger ⟨ψ_β, H_β ψ_β⟩ ≤ K′ m(β) ‖ψ_β‖².
Testable form: on a lattice with L ≫ √s ξ, measure ξ·(1 − C(1)/C(0)) for the flowed magnetic density at three or more β with ξ(β) growing. (C′) predicts a bounded sequence. A growth ∝ ξ^α with α > 0 refutes this route; it does not refute (C).
Free field (discriminator, not SU(2)): ξ(1 − C(1)/C(0)) = 3.56, 4.13, 4.46, 4.64, 4.73, 4.78 at ξ = 8…256, with s = 0.1 (test_c.py, P3 met). This agrees with B3 of SPATIAL_FLOW.md (CITED, internal: "M₁/M₀ … bounded uniformly in b", proved by the builder; per the challenge it holds only under s·Ψ′_b/P_b < 1/7 and ℓ/√s ≳ 9).
For SU(2) nothing is known. It is the finiteness hypothesis H-fin of SPATIAL_FLOW.md in a stronger, dynamical form: a bounded physical energy for a sharp-time functional.

**Step 7 (CLAIMED; needed only for the lattice-local variant). C_β(1)/C_β(0) ≥ c > 0 uniformly in β, for a fixed lattice-local O (the plaquette).**
Argument as I would defend it: at weak coupling the fluctuations of the plaquette are Gaussian to leading order. The connected correlator at one lattice step is then the free value 2G(1)²; normalized by 2G(0)², it gives (0.1932)² = 0.0373, as in the free φ² measurement. Corrections are O(1/β).
Weakest point: "Gaussian to leading order, uniformly in the infinite volume" is Balaban-type control of gauge-invariant expectations, which does not exist (LIT_ATTEMPTS hole 11). It is also not enough for (C) anyway, because the doubling of step 5 is still missing.

**Step 8 (PROVED). Smearing in Euclidean time does not make (C) automatic (mechanism (d)).**
(8a) For ψ = T^(kξ/2)φ (smearing over k/2 correlation lengths), C_ψ(n) = C_φ(n + kξ). With k = 2, the ratio R_ψ = C_φ(2.5ξ)/C_φ(3ξ). For the admissible two-atom measure ν_φ = wδ_m + δ_1 with w = e^(−3ξ+3), R_ψ ≥ e^(ξ/2)/3 → ∞. This holds for every fixed k with w = e^(−(k+1)ξ+(k+1)), the same construction (test_c2.py Q3 and test_c3.py Q3b: 7/7 cases). Log-convexity gives only R_ψ ≥ e^(1/2).
(8b) Adaptive smearing does work, trivially. By (1d) there is n_β with u_φ(n_β) ≤ (1+δ)m₀; then ψ_β = e^(−n_β H/2)φ satisfies (C) with D = e^((1+δ)m₀ξ/2). The price is threefold.
 (i) If n_β/ξ is unbounded, ψ_β is smeared over unbounded physical Euclidean time. It is no longer a sharp-time local field, so the OS reconstruction of a local field from it fails: it is a function of the transfer matrix, not of fields in a bounded region.
 (ii) If n_β/ξ stays bounded, that boundedness is (C)-type information about φ, so nothing is gained.
 (iii) The limit is a single atom. The mean of E under μ_β equals ξ·u_φ(n_β + ξ), which lies in [m₀ξ, (1+δ)m₀ξ], while E ≥ m₀ξ on the support; as δ → 0, μ_β → δ_{m₀ξ} and G(t) = e^(−(t−1)E₀).
In the free field (measured only, P8): the first n with u(n) ≤ 1.5×(bottom of the sector) is n ≈ 3.19ξ, stable for ξ = 8…64, for both φ(0) and φ(0)². There, smearing by O(ξ) suffices, consistent with (C).

**Step 9 (PROVED numerically for the discriminator; not SU(2)). Free massive lattice field, m → 0, lattice-local observables.**
R(ξ) = C(ξ/2)/C(ξ):
- φ(0): 6.584, 5.921, 5.580, 5.522, 5.508, 5.505, 5.504 at ξ = 4…256. The continuum value is 2K₁(1/2)/K₁(1) = 5.503975.
- φ(0)²: R tends to the square of the φ(0) value, 30.2937.
I used the Schwinger representation. The child, with a momentum integral, agrees to under 10⁻⁶ relative, and the grandchild (Schwinger, ξ = 16) gives 5.5796296. So (C) holds for these with D ≈ 6.6 and 43.4. Here (C) holds by a power law n^(−3), n^(−6) between the lattice scale and ξ, as in A1 §2.

**Step 10 (PROVED). (C) fails exactly when the bottom weight is exponentially small; a hole alone does not break it.**
- Two-atom family ν = e^(−ξ)δ_m + δ_1: R ≥ e^(ξ/2)/3. The family μ_β is not tight: μ_β(E = ξ) = 1/(1+e^(−1)) = 0.731 for all ξ (Q1, Q5). In the limit, G(1) = 1 but G(1+) = 0.269, so G is discontinuous at 1, mass escapes to infinite energy, and G(t) is infinite for t < 1.
- Hole family ν = wδ_m + ε²·1[√m, 3]dε with w = e^(−√ξ): R(4096)/R(64) = 1.5·10⁷ (Q2).
- The same hole with w = m⁴ gives R → e^(1/2) (bounded, sup 151 at ξ = 256). Here (C) holds and **the limit is a single atom δ₁**: the continuum above the hole escapes.
So (C) does not exclude a degenerate one-particle limit. A1 §4 lists Gaussianity under (E) but not this case explicitly (see report).

**Step 11 (literature, mechanism (c)).** The only lower-bound tools used are group-blind: reflection positivity ⇒ log-convexity (step 1), and Jensen ⇒ C(n) ≥ C(0)e^(−nM₁/M₀) (internal `R12Vol.jensen_exp`). Infrared bounds are upper bounds. Griffiths/Ginibre-type inequalities give lower bounds and monotonicity for abelian spin and gauge models. That is my recollection and NOT CHECKED: no locator in LIT_RIGOROUS.md, and nothing fetched. I know of no correlation inequality giving lower bounds for SU(2) lattice gauge theory. Nothing from the literature is used in the chain beyond step 0.

## Discriminator table

| Model | (C) true? | First step of this chain that fails | Comment |
|---|---|---|---|
| Compact U(1), d = 4, weak coupling | n/a ((A) false) | Step 0/2: ξ = ∞, so (C) is undefined; (C′) would demand C(1) = C(0), which is false | **No step of the chain detects the group.** The chain is conditional on (A) and is group-blind; it does not claim (A). It cannot be "wrong for U(1)" in the A1 sense, because it never asserts a gap. |
| Finite group, d = 4, weak coupling | trivially (ξ → 0 < 1) | none: (C′) with m → ∞ is trivially true | Theorem R is vacuous (ξ < 1, flow time sξ² → 0); there is no continuum. Correct behaviour. |
| Compact U(1), d = 3 (Villain) | not known; believed true | Step 6 (MISSING), same as SU(2) | (A) and (B) per Göpfert–Mack (LIT_RIGOROUS R3b, abstract level). The limit is believed to be a free scalar of mass m_D; (C′) is expected to hold there. |
| d = 2, infinite spatial line | vacuous | none | Gauge-invariant functions of the links of a spatial line, which is a tree, are constants (gauge fixing), so ψ = 0. On a spatial circle, ψ = Polyakov loop gives a single atom, R = e^(1/2) exactly, and the limit is a single atom. |
| Free massive field, m → 0 | **true** (computed) | none for lattice-local (steps 2 and 9); step 3 not applicable (step 4); for the flowed observable (C′) holds numerically | R → 5.504 (φ) and 30.29 (φ²); flowed s = 0.1: ξ(1 − C1/C0) → 4.78 |
| Measure with a hole and an exponentially small bottom | **false** | any proof of (C′) or doubling must fail here | R ~ e^(ξ/2); μ_β not tight |
| Measure with a hole and a polynomial bottom | true | none | limit is a single atom |

**(ii) Where non-abelian structure enters:** nowhere in steps 0–5 or 8–10. It could enter only in the MISSING step 6 (and the CLAIMED step 7). The chain itself is pure spectral theory of one positive operator.

**(iv) Quantifiers and limits.** At fixed β: infinite volume first (assumption, step 0), with m(β) the infinite-volume gap. Steps 1–3, 5, 8 and 10 are exact statements for each β. Constants K, K′, A, D must be uniform in β ≥ β₁; then β → ∞ (Theorem R). Uniformity in the volume enters only if (C′) is proved in boxes. Then C_L(0) and C_L(1) must converge to their infinite-volume values (true for fixed local observables if the infinite-volume state is the limit). The bound must use the infinite-volume m(β), not m_L(β): the periodic-box gap is positive for trivial reasons (A1 §4.5) and need not be comparable. For the flowed observable, L ≫ √s·ξ(β) is required.

## Weakest link

Step 6: (C′) for the slice-flowed SU(2) magnetic density, in infinite volume and uniform in β. This is a bounded physical energy, one lattice step at a time, for an observable smeared at physical scale √s. Nothing in the literature controls the transfer matrix of four-dimensional SU(2) between the lattice scale and ξ. The chain moves (C) to this one inequality; it does not prove it.

## What a challenger should attack first

1. Step 6: whether (C′) is even true for the flowed SU(2) density. Look for a growth of ξ(1 − C(1)/C(0)) with ξ in a matched measurement. Also check whether the electric contact term of SPATIAL_FLOW §1.3 enters C(1) through the temporal links between slices.
2. Step 3: the chord argument needs ξ/2^j ≥ 1 and ξ ≥ 2K′. Check it, and check the claim "D_j = e^(2K′) uniform in j".
3. Step 8(iii) and step 10: (C) does not exclude a single-atom limit. Theorem R's "nontrivial" then means only "a single mass", and (E) has to carry everything.
4. Step 0: the infinite-volume state at large β is assumed, not cited.
