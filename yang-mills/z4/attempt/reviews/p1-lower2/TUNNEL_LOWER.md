**Proved in writing: (a) exact lower-bound reductions for any symmetric positive kernel with a flip σ: (I0), (I1), the ground-state representation, Lemma C (comparison) and Lemma P' (restricted canonical paths); (b) for the one-dimensional grid model (circle, grid step κ/√β with 0 < κ ≤ 1, Gaussian steps of variance 1/β, killing e^{−ε}): limsup_{β→∞} (−log m)/√β ≤ c* + E_κ, where E_κ = π√(8δ_κ) + 32δ_κ(3 + log(√(2π)/κ)) and δ_κ = 2Σ_{m≥1} e^{−2π²m²/κ²}. For κ ≤ 1 this gives δ_κ ≤ 6·10⁻⁹ and E_κ ≤ 7·10⁻⁴. For the SU(2)² model the target limsup (−log m_eo)/√β ≤ c* is NOT proved. Two steps are MISSING (§6): a transverse subsolution that is uniform along the valley, and the localisation and Harnack estimates in the wells. No explicit constant better than A4's unspecified C is proved for SU(2)².**

Worker o1-lower (task T141). "PROVED" means proved in writing here, by me. It has not been reviewed, and I share a model family with the director. No network source was used. The canonical-path idea is classical (Diaconis–Stroock; Sinclair), but it is not cited as an input: the proof below is complete. Numbers are from oned_split.py (results_main.txt) and oned_paths.py (results_paths_main.txt), and the child T144 recomputed them independently.

## 0. Notation

- T is a symmetric operator with an entrywise positive kernel on a finite measure space X (in 1D: the grid, with counting measure).
- σ is a measure-preserving involution that commutes with T.
- g > 0 is the top eigenvector, normalised by ‖g‖ = 1. It is σ-even, with eigenvalue λ_e.
- f is a top eigenvector in the σ-odd sector, normalised by ‖f‖ = 1, with eigenvalue λ_o.
- Δ = λ_e − λ_o, and m = log(λ_e/λ_o) ≥ Δ/λ_e.
- A is a measurable set with X = A ⊔ σA. R(x,y) = T(x,σy) on A×A.

## 1. Exact identities (PROVED, any such T)

**(I0) Flux identity.**
 (λ_e − λ_o)⟨f1_A, g⟩ = ∫_{A×A^c} T(x,y)[f(x)g(y) − f(y)g(x)].
- Proof. λ_o⟨f1_A, g⟩ = ⟨Tf, 1_A g⟩ and λ_e⟨f1_A, g⟩ = ⟨f1_A, Tg⟩. Subtract; by symmetry of T the A×A terms cancel. ∎
- In sector form: Δ⟨f_A, g_A⟩ = 2⟨f_A, R g_A⟩.
- Numerically exact: at β = 16 (K1, K2) the identity and the plain eigenvalue subtraction agree to rel 2.9·10⁻⁹. The child's sector and literal sums agree to < 10⁻¹⁴, and the grandchild T145 found rel 1.4·10⁻¹⁰.
- The brief's further step needs f > 0 on A. For SU(2)² that is NOT justified: the sector kernel T(x,y) − T(x,σy) on A×A is not positive, because the quaternion inner product of two points of A = {a₁ < π/2} can be negative. The routes below avoid it.

**(I1) Flux of |f|. No sign assumption on f.**
 Δ ≥ ∫∫_{f(x)f(y)<0} 2 T(x,y)|f(x)||f(y)|.
- Proof. λ_e ≥ ⟨|f|, T|f|⟩, and ⟨|f|, T|f|⟩ − ⟨f, Tf⟩ = 2∫∫_{ff<0} T|f||f|. ∎
- Measured: Δ/LB ∈ [1.37, 1.51] for β = 16…4096 (18/18 cases). The bound is sharp to a constant factor in 1D. It still needs a lower bound on |f| near the nodal set of f, and that is not available in 4D.

**(GS) Ground-state representation.** For an odd u = hg,
 ⟨u, Tu⟩ = λ_e‖u‖² − ½∫∫ T(x,y)g(x)g(y)(h(x) − h(y))².
Hence Δ = inf_{h odd} E(h)/‖hg‖², with E(h) := ½∫∫ Tgg(h(x) − h(y))², and the infimum is attained at h* = f/g.
- Proof. Expand ½(h(x) − h(y))² and use Tg = λ_e g. ∎

**Lemma P' (restricted canonical paths). PROVED.**
- Setting. Let S be σ-invariant. Attach to each x ∈ S a path γ_x = (x = z₀, …, z_n = σx) in S, of length ≤ n. Let Q(e) = T(z,z')g(z)g(z') for an edge e = (z, z'), and let ρ_S = max_e Q(e)⁻¹ Σ_{x: e∈γ_x} n g(x)²/4. In the discrete case these are sums; in the continuum use flows.
- Statement. Δ ≥ (Σ_{x∈S} f(x)²)/ρ_S.
- Proof. Since h* is odd, h*(x) = (h*(x) − h*(σx))/2. Cauchy–Schwarz along γ_x gives Σ_S g²h*² ≤ ρ_S Σ_e Q(e)(dh*_e)² ≤ ρ_S E(h*) = ρ_S Δ. Also g²h*² = f². ∎
- With S = X on a circle grid, paths of N/2 nearest-neighbour steps give **Lemma P**: Δ ≥ 8 min_e Q(e)/N.
- Measured: Δ/B1 ∈ [3·10³, 7.5·10⁴] (Q1 met 5/5). The loss is polynomial in β (about β^{0.55}), so it disappears in the exponent.

**Lemma C (comparison). PROVED.**
- Statement. Let Ω ⊂ X, φ ≥ 0, ‖T_ΩΩ‖ < λ_e, (Tφ)(x) ≥ λ_e φ(x) on Ω, and φ ≤ g on Ω^c. Then φ ≤ g on Ω.
- Proof. Put w = g − φ. Then (λ_e − T_ΩΩ)w_Ω = (Tφ − λ_eφ)_Ω + T_{ΩΩ^c} w_{Ω^c} ≥ 0. Also (λ_e − T_ΩΩ)⁻¹ = Σ λ_e^{−k−1} T_ΩΩ^k is entrywise ≥ 0. So w_Ω ≥ 0. ∎

**Scalar steps (Lean-checked: TunnelLower.lean, exit 0, axioms propext / Classical.choice / Quot.sound, no sorry).**
- (L1) v√(2ε) ≤ v²/2 + ε. The per-step cost dominates the Agmon density; equality holds at v = √(2ε).
- (L2) If λ ≤ M + q(1 − M) and q < 1, then M ≥ (λ − q)/(1 − q).
- (L3) √(2(ε+η)) ≤ √(2ε) + √(2η). Hence c*(η) := ∫₀^π √(2(ε+η)) ≤ c* + π√(2η).

## 2. The 1D grid model and its theorem

**Model.**
- Grid x_i = −π + ih with h = κ/√β, 0 < κ ≤ 1, and N = 2π/h ∈ 4ℕ.
- ε = 2 asinh|sin|.
- K_xy = h√(β/2π) Σ_{k=−1,0,1} e^{−β(x−y+2πk)²/2}, and T = e^{−ε/2} K e^{−ε/2}.
- σ: x ↦ x + π.
- By Poisson summation every row sum of K lies in [1 − δ_κ − (tail), 1 + δ_κ]. Hence ‖K‖ ≤ 1 + δ_κ and λ_e ≤ 1 + δ_κ.

**Theorem 1D (PROVED in writing).** limsup (−log m)/√β ≤ c* + E_κ.

Fix η with 4δ_κ < η < η₀, and let β → ∞. The proof has six steps:

1. **Lemma L: λ_e → 1 − O(δ_κ). PROVED (sketch).**
   - Take the trial vector 1_I, with I = {|x| ≤ β^{−1/4}}. On I, ε ≤ 2β^{−1/4}.
   - Row sums of K restricted to I are ≥ 1 − δ_κ − tail(M), except at O(M/κ) points near ∂I.
   - So λ_e ≥ (1 − δ_κ − o(1))e^{−2β^{−1/4}}.

2. **Lemma M: Σ_{ε<η} g² ≥ ½. PROVED.**
   - λ_e = ‖K^{1/2}e^{−ε/2}g‖² ≤ (1 + δ_κ)(M + e^{−η}(1 − M)).
   - Apply (L2) with q = e^{−η}, and use Lemma L with η > 4δ_κ.

3. **Lemma H: Harnack in the well. PROVED.**
   - Let W = {ε < 3η} around one well, with half-width w(η) ≤ 2η.
   - For x, y ∈ W join them by grid points with steps ≤ 2/√β. Then n ≤ 2w√β + 2, and (T^n)_xy ≥ c₁^n with c₁ = e^{−3η}κe^{−2}/√(2π).
   - g = λ_e^{−n}T^n g gives g_x ≥ (1 + δ_κ)^{−n} c₁^n max_{W'} g, where W' = {ε < η}. Lemma M gives max_{W'} g ≥ (2N)^{−1/2}.
   - Hence g ≥ μ := (2N)^{−1/2}(c₁/(1+δ_κ))^n on W, and −log μ ≤ 2w(η)√β·log((1+δ_κ)/c₁) + O(log β).

4. **Lemma S: the subsolution. PROVED.**
   - Let ρ be C¹ and nondecreasing on [0, π/2], with ρ = 0 where ε ≤ η, ρ = √(2(ε+η)) where ε ≥ 2η, and 0 ≤ ρ ≤ √(2(ε+η)) everywhere. Put Ψ(x) = ∫₀^{d(x)} ρ, where d is the distance to the nearer well, and φ = μe^{−√βΨ}.
   - On Ω = {ε ≥ 2η}, Taylor's theorem gives Ψ(y) ≤ Ψ(x) + ρ(x)(y − x) + H(y − x)²/2, with H = sup|ρ'|. The reflected branch beyond π/2 lies below the monotone extension.
   - Restrict the sum to |y − x| ≤ M/√β and use the discrete Gaussian moment Σ_k κ(2π)^{−1/2}e^{−κ²k²/2−ρκk} ≥ e^{ρ²/2}(1 − δ_κ). The truncation costs ≤ Ce^{−(M−2)²/2}. This gives
     (Tφ)_x ≥ φ_x e^{−ε(x)+ρ²/2}(1 − δ_κ − Ce^{−(M−2)²/2})e^{−O(M²/√β)} = φ_x e^{η}(1 − o(1)) ≥ λ_e φ_x.
   - Measured with η = 0.25: min over Ω of Tφ/(λφ) = 1.37–1.42 (P8, 6/6).

5. **Lemma C applies.**
   - ‖T_ΩΩ‖ ≤ e^{−2η}(1 + δ_κ) < λ_e.
   - On Ω^c ⊂ W, φ ≤ μ ≤ g by Lemma H.
   - Hence g ≥ μe^{−√βc*(η)/2} everywhere.

6. **Lemma P.**
   - min_e Q(e) ≥ κ(2π)^{−1/2}e^{−κ²/2−ε_max} μ² e^{−√βc*(η)}.
   - So −log Δ ≤ √β[c*(η) + 4w(η)log((1+δ_κ)/c₁)] + O(log β).
   - Combine with (L3) and m ≥ Δ/(1 + δ_κ), let η ↓ 4δ_κ, and use w(η) ≤ 2η. The term 4w log((1+δ_κ)/c₁) is then ≤ 32δ_κ(3 + log(√(2π)/κ)). ∎

**Remarks.**
- The δ_κ term is genuine for the grid model: the discrete Gaussian moment oscillates by ±δ_κ. As κ → 0 it vanishes super-exponentially.
- The continuum circle model is not covered as written. It needs tubes in place of single grid paths in Lemma H (CLAIMED routine).
- The matching upper half (liminf ≥ c*) in 1D is TUNNEL_THEOREM §4–5 with Lemma F trivially true, because there is no fibre (CITED, not rechecked on the grid).

## 3. Numerical check of the route (1D, K2, K3; child K4 independent)

| β | Δ (identity) | −log Δ/√β | Δ/LB(I1) | UB/Δ | Δ/B1 (Lemma P) |
|---|---|---|---|---|---|
| 16 | 6.0039e−07 | 3.581 | 1.512 | 1.398 | 3.1e3 |
| 256 | 9.1389e−30 | 4.179 | 1.422 | 1.331 | 1.6e4 |
| 1024 | 6.0976e−61 | 4.333 | 1.404 | 1.318 | 3.6e4 |
| 4096 | 7.0049e−124 | 4.431 | 1.393 | 1.310 | 7.5e4 |

- At β = 4096 the value −log Δ/√β is still 0.17 below c* = 4.6054. This is consistent with a subleading correction: 1 − λ_e = 0.077 at β = 4096, and the well is linear (ε ≈ 2a), so the energy shift is of order β^{−1/3}.
- Grid halving changes log Δ by about 1% (P7).

## 4. DEFECT found in the target documents

- **TUNNEL_THEOREM §5 constant.** It writes "λ_ee − λ_eo ≤ ... = 2⟨g1_A, T g1_{A^c}⟩". With ‖g‖ = 1 the correct value is ½·4·(two ordered cross blocks) = **4**⟨g1_A, Tg1_{A^c}⟩. The child measured the factor-2 version failing at 6/6 β (ratio 0.655–0.699), and the factor-4 version holding (1.31–1.40). My UB column is the factor-4 form. Only the constant is affected; the exponent is not.
- **The brief's claim that f is positive on A.** This is unsupported for SU(2)² (see (I0)). It was not used.

## 5. Step tags

| step | tag |
|---|---|
| (I0), (I1), (GS), Lemma P', Lemma C | PROVED (general) |
| L1–L3 | PROVED, Lean |
| Lemma L (1D) | PROVED (sketch) |
| Lemmas M, H, S, P (1D grid) | PROVED |
| Theorem 1D (limsup ≤ c* + E_κ) | PROVED in writing, unreviewed |
| 1D continuum (κ → 0 with tubes) | CLAIMED |
| 1D matching upper half | CITED (TUNNEL_THEOREM §4–5) |
| SU(2)²: Lemma M analogue (mass of g and f near the wells a₁ ∈ {0, π}) | CITED, conditional on Lemma F (TUNNEL_THEOREM (B)); transverse localisation CLAIMED |
| SU(2)²: Lemma H analogue (Harnack in the 3-D well region, Haar density sin²a₁) | CLAIMED |
| SU(2)²: Lemma S analogue (transverse subsolution) | MISSING |
| SU(2)²: Lemma P' with S = wells ∪ valley tube (a₂ ≈ 0) | PROVED as a reduction; its inputs are MISSING |
| SU(2)² target limsup ≤ c* | MISSING |

## 6. What is missing for SU(2)², and which step loses

1. **Lemma S in 4-D (MISSING).** It needs a positive φ with Tφ ≥ λ_e φ on Ω = {ε(a₁) ≥ 2η} ∩ tube.
   - The product ansatz e^{−√βΨ(a₁)} × (fibre ground state at a₁) fails. One K₁ step rotates U₁'s axis by about β^{−1/2}/sin a₁, which moves the fibre's well circle {U₂ commuting with U₁} by about β^{−1/2}. That is the transverse width itself, so the relative error per step is O(1), not O(β^{−1/2}). This is the step that loses the constant if the product ansatz is used, and it is how a path argument ends up with e^{−C√β}.
   - The fix is the joint transverse Gaussian in (δ₁, δ₂) modulo gauge: the physical mode y = (sin a δ₂ − sin b δ₁)/S of TUNNEL_THEOREM §6, with energy 2 asinh S = ε(a) at b = 0. It should be cut off as (G − c)₊ at radius Mβ^{−1/2}. With that, the Gaussian tilt gives e^{−ε+ρ²/2−o(1)} exactly as in 1D (CLAIMED, not written).
2. **Mass and Harnack in the wells (CLAIMED or conditional).** Lemma P' needs Σ_S f² ≥ ½ for S = (well regions) ∪ (valley tube around the a₁-path at a₂ ≈ 0). That uses the Agmon estimate (B) of TUNNEL_THEOREM for f (λ_eo ≈ λ_ee), which is conditional on Lemma F, plus transverse localisation. It also needs g ≥ e^{−o(√β)} on the well part of S.
3. Given 1 and 2, Lemma P' with paths inside S gives Δ ≥ e^{−√β(c*+o(1))}. The proof is the same as in 1D.
