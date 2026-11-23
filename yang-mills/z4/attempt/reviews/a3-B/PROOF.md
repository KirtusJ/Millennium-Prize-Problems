# (B) for SU(2), d = 4: m(β) → 0 as β → ∞. A chain, built for attack

**This is NOT a proof.** Steps S3a, S3b and S3c are CLAIMED (argued in full, but not proved here). No step is MISSING in the sense of "no argument at all", but the chain stands or falls with S3a to S3c. The weakest link is named in §5.

Worker a3-B for Director Z4, 23 Nov 2026. Principal: Kirtus Justus. Same model family as the director, so this is not independent review.

Conventions. Wilson action β Σ_p ½Tr U_p with β = 4/g². For U ∈ SU(2), ½Tr U = cos α, where α ∈ [0, π] is the class angle. Λ_L = (ℤ/Lℤ)⁴ is a periodic box with L even. O_p := β(1 − cos α_p), and p₀ is a spatial (1,2) plaquette at time 0. G(n) := ⟨F₁₂(0) F₁₂(n e₀)⟩ in the free one-colour lattice Maxwell field (action ½Σ(dA)², the field-strength correlator, which is gauge invariant).

**Order of limits, used throughout.** (1) L → ∞ at fixed β (S0). (2) β → ∞ at fixed time separation n (S3). (3) n → ∞ (S2). Uniformity in the volume is used only in S3a, where bounds must hold for every L, or in the L → ∞ limit at each fixed β, so that they pass to the infinite-volume state.

## 1. The chain

**S0. Infinite-volume state and transfer matrix. CITED + PROVED (elementary parts).**
For fixed β, the Gibbs states ⟨·⟩_{β,L} on local observables have a subsequential limit ⟨·⟩_β as L → ∞. This follows from compactness of SU(2)^links and a diagonal argument (PROVED, standard). The limit is translation invariant. It is reflection positive (RP) for time reflections, because each ⟨·⟩_{β,L} is (CITED: Osterwalder–Seiler 1978 and Lüscher 1977, LIT_RIGOROUS R2, ABSTRACT ONLY; INDEX_EXTRACT (a)1: G4 Lean, Wilson RP on a periodic box, every β, any compact G). RP is preserved because ⟨F·θF⟩ ≥ 0 for each local F is a closed condition (PROVED).
OS reconstruction then gives a Hilbert space 𝓗_β, a vacuum Ω, and a self-adjoint contraction T (one time step) with TΩ = Ω (CITED OS78, abstract level).
Define m(β) := −log ‖T restricted to Ω^⊥‖ ∈ [0, ∞]. When T > 0 this equals A1's inf spec H on Ω^⊥.
Everything below holds for **every** such limit state. Uniqueness is not used.
Hypotheses used: RP of the Wilson action for time reflections (for S0), and for reflections in all coordinate planes through sites (for S3a). The second is **not** confirmed by any source read in this program (see §3).

**S1. Spectral bound. PROVED.**
Let O be a bounded function of links in the time-0 slice and ψ = (O − ⟨O⟩)Ω ⟂ Ω. For even n, C(n) := ⟨ψ, Tⁿψ⟩ = ⟨ψ, (T²)^{n/2} ψ⟩. Since T² ≥ 0 and ‖T²|_{Ω⊥}‖ = e^{−2m}, the spectral theorem gives 0 ≤ C(n) ≤ e^{−mn} C(0). Only even n are used, so positivity of T itself is not needed.
C(n) is the connected correlation Cov_β(O(0), O(n e₀)).

**S2. Reduction. PROVED (algebra checked in Lean: `S2.lean`, theorem `s2_gap_le`).**
Suppose that for an even n, liminf_{β→∞} C_β(n)/C_β(0) ≥ c(n) > 0. Then limsup_β m(β) ≤ −log c(n)/n.
Proof: c·C₀ ≤ C_n ≤ e^{−mn}C₀ with C₀ > 0 gives m ≤ −log c/n. Pass to limsup.
If moreover c(n) ≥ K n^{−p} for all large even n, then limsup m(β) ≤ inf_n (p log n − log K)/n = 0 (`s2_power` gives the identity). Hence m(β) → 0, which includes "m(β) = 0 from some β on" (no gap at all).
C_β(0) > 0: the plaquette variance is positive, because the DLR conditional density of one link given the rest is continuous and strictly positive.

**S3. Local Gaussian limit in infinite volume (the core). CLAIMED, in three parts.**
Target statement (S3*): for every even n, in every limit state of S0,
  liminf_{β→∞} Cov_β(O_{p₀}(0), O_{p₀}(n e₀)) / Var_β(O_{p₀}) ≥ c(n) := (G(n)/G(0))².
The free value of c(n) and its decay are computed in `free_benchmark.py`: G(0) = 1/2, c(1) = 1.9·10⁻², c(4) = 1.5·10⁻⁶, c(10) = 4.6·10⁻¹⁰, and c(n) ~ K n^{−8} (n·log(c(n)/c(n+1)) → ≈ 7.8 at n = 9). So S2 applies with p = 8.
Free normalisation. U = exp(iA·σ/2) gives cos α_p ≈ 1 − |F_p|²/8. With φ := (√β/2)A, the weight is exp(−½Σ|dφ|²) and O_p → ½Σ_a (F^a_p[φ])². By Wick's theorem, Cov → (3/2)G(n)² and Var → (3/2)G(0)². The number of colours cancels in the ratio.

**S3a. Uniform exponential tails at the Gaussian scale. CLAIMED** (tested in 2D, `sharp_chess2d_v2.py`).
Claim: there is C < ∞ such that for all β ≥ 2, all t ≥ 0 and every limit state, P_β(O_p > t) ≤ C e^{−t/8}.
Argument:
(i) **Chessboard estimate.** RP in all coordinate site-planes on the even torus, with unit cubes as blocks, gives P(B_p) ≤ [P(∩_{images} B_q)]^{1/|Λ|}.
  - The images of a (1,2) plaquette are the (1,2) plaquettes with x₃ and x₄ of fixed parity: |Λ|/4 distinct plaquettes, each counted 4 times.
  - On the intersection event, β Σ(1 − cos α) ≥ t|Λ|/4. Write e^{−βS} = e^{−βS/2}·e^{−βS/2} ≤ e^{−βS/2} e^{−t|Λ|/8}.
  - Hence P(O_p > t) ≤ exp(f_L(β/2) − f_L(β) − t/8), where f_L(β) := |Λ|⁻¹ log Z_L(β) − 6β.
(ii) **Upper bound on Z (PROVED here).** In temporal gauge (all temporal links = 1 except one slice; Haar invariance), drop all plaquettes except the (0,i) ones, using cos ≤ 1. Then integrate the spatial links slice by slice: each (0,i) plaquette is U_{x+e₀,i}U_{x,i}⁻¹, a Haar change of variables. Result:
  f_L(β) ≤ 3(1 − 1/L) log ẑ(β), with ẑ(β) = e^{−β}·2I₁(β)/β ~ (2/π)^{1/2} β^{−3/2}.
(iii) **Lower bound on Z (argued).** Same gauge, Jensen with a product trial measure: each remaining link uniform on the Haar ball of radius s = β^{−1/2}. Plaquette angle ≤ 4s, so the energy loss is ≤ 6·8 = 48 per site, and the entropy is −log Haar(B_s) = (3/2) log β + O(1) per link.
  f_L(β) ≥ −48 − (9/2)(1 + 1/(3L)) log β − C.
(iv) Combining (ii) and (iii): lim sup_L [f_L(β/2) − f_L(β)] ≤ (9/2) log 2 + 48 + C' uniformly in β. The 1/L·log β terms vanish because L → ∞ first.
Tails at the O(1) scale give tightness and uniform integrability of every power of O_p, uniformly in β and in volume.
*Weakest point:* (i) needs RP for reflections in planes **through sites** for Wilson SU(2), and the chessboard theorem for link variables whose block functions sit on shared faces. I have not read a source that states either for lattice gauge theory.

**S3b. Every β → ∞ limit is a Gibbs measure of the free 3-colour Maxwell specification. CLAIMED.**
Fix a finite box R ⊃ {p₀, p₀ + n e₀}. In R ∪ ∂R choose a local axial gauge from a base point (measurable, local). Express links as exp(iσ·A/2) and set φ = (√β/2)A.
By S3a, the plaquette curvatures in φ-units are tight. On the simply connected R ∪ ∂R, the gauge-fixed φ is a path sum of curvatures plus O(β^{−1/2}|R|) commutator corrections. Hence the laws of φ|_{R∪∂R} are tight, and along a subsequence β_k they converge to some μ_∞, jointly for all R (diagonal argument).
The DLR kernel K_β(dφ_R | φ_∂) of the Wilson specification is a fixed-box integral. By the Laplace method it converges, uniformly for φ_∂ in compacts, to the Gaussian kernel K_∞ (mean = Maxwell-harmonic extension, covariance = Dirichlet Maxwell Green function). Gauge orbits are compact, and non-abelian terms are O(β^{−1/2}) at fixed R.
Then μ_∞(g) = lim E_β[K_β g] = μ_∞(K_∞ g) for bounded continuous g, using tightness to restrict to compacts. So μ_∞ is Gibbs for the free specification, translation invariant and RP.
Uniform integrability (S3a) gives Cov_{β_k}(O(0), O(n)) → Cov_{μ∞}(½|F(0)|², ½|F(n)|²), and the same for the variance.
*Weakest point:* uniformity of the Laplace limit of K_β over boundary data, and the measurable local gauge fixing. **This is the step where infinite volume and β → ∞ are exchanged.** It is also the step where non-abelian structure enters (commutator terms), only as an error term to be shown negligible.

**S3c. Classification and the inequality. CLAIMED.**
(i) A translation-invariant Gibbs measure μ_∞ of the free massless Maxwell specification in d = 4, with finite second moments of F, decomposes as F = ξ + h. Here ξ is the free infinite-volume field, and h is independent of ξ, closed and co-closed, stationary and in L². For the scalar case this is Georgii-type (Gibbs Measures and Phase Transitions, Ch. 13, FROM MEMORY, not read). For the field strength, transience of the d = 4 Green function for F, together with the reverse-martingale limit of harmonic extensions, gives the decomposition. A stationary L² solution of dh = 0, d*h = 0 has spectral measure on {k : k̂² = 0} = {0}, so h = f is a random constant.
(ii) With F = ξ + f:
  Cov(O(0), O(n)) = E|f₁₂|² G(n) + (3/2)G(n)² + Var(½|f₁₂|²), and the same with n = 0 for the variance.
  Since 0 < G(n) < G(0) (positivity: `free_benchmark.py` P2; also RP), the ratio is ≥ min{G(n)/G(0), (G(n)/G(0))², 1} = c(n). This proves (S3*) given (i) and S3b.
*Weakest point:* (i) for 1-form (gauge) Gaussian fields is transferred from the scalar case, not proved. "Finite second moment" for μ_∞ comes from S3a.

**Conclusion (conditional).** S0 to S3 give liminf C_β(n)/C_β(0) ≥ c(n) ~ K n^{−8}, so m(β) → 0 by S2. The conclusion rests on the three CLAIMED steps S3a, S3b and S3c.

## 2. Hypotheses each step uses
- S0: Wilson RP for time reflections (OS78/Lüscher, abstract level; G4 Lean); OS reconstruction; compactness.
- S1: self-adjointness of T (time-reflection RP plus translation invariance); even n.
- S2: none beyond S1 (Lean-checked algebra).
- S3a: RP for reflections in all four coordinate site-planes on the even torus; a chessboard theorem for gauge link variables; temporal gauge on the torus; Jensen (Gibbs variational) inequality; L → ∞ before β → ∞.
- S3b: DLR property of periodic limit states; Laplace method with boundary data; local gauge fixing on a simply connected box.
- S3c: classification of Gaussian Gibbs measures (scalar: Georgii, from memory; 1-form: claimed); positivity of G(n).

## 3. Discriminators

| model | conclusion (B) there | S0 | S1–S2 | S3a | S3b | S3c / free c(n) | verdict on the chain |
|---|---|---|---|---|---|---|---|
| **compact U(1), d = 4, weak coupling** | true in "no gap" form; (A) false | ok | ok | ok (f ≈ −(3/2)·3 log β per site: 3 dof/site) | ok (abelian: no commutators) | c(n) is the same (G(n)/G(0))² (one colour) | chain gives m → 0, consistent. **No step fails, and none should:** the argument never asserts (A). An argument for (A) by this route would fail at S3c, because the free massless limit has no gap. |
| **finite group G, d = 4** | **false** (gap grows; Adhikari–Cao Thm 1.1) | ok | ok | the bound holds, but O_p ∈ {0} ∪ [βΔ_G, ∞) and P(O_p > 0) ≤ e^{−cβ}: everything collapses to 0 | **FAILS**: no Lie algebra, so no scaling φ = √β·A and no Laplace method. The limit μ_∞ is δ₀, Var → 0, and Cov/Var → 0 like e^{−βΔ_G n}. | not applicable | chain correctly breaks at S3b (the Laplace step needs a continuous group) |
| **compact U(1), d = 3** | true (Göpfert–Mack: gap ~ e^{−cβ}, Villain) | ok | ok | ok (d = 3 version) | ok | free 3D Maxwell: G(n) ~ n^{−3}, c(n) ~ n^{−6} | consistent: m → 0. Monopoles are invisible at fixed n (weight e^{−cβ}). |
| **SU(2) or U(1), d = 2** | **vacuous/false in this sense** (see below) | ok | ok | ok (tested exactly) | ok | free 2D Maxwell has no propagating mode: G(n) = 0 for n ≥ 1, so c(n) = 0 | S2 gives nothing, consistent. See the DEFECT on A1's 2D row below. |

**DEFECT in A1_REDUCTION §6, row "SU(2) or U(1), two dimensions: (B) true".** In infinite volume with free boundary conditions, the 2D plaquette variables are i.i.d. (exact, axial gauge). So the OS space built from gauge-invariant half-space observables is ℂΩ: Ω^⊥ = {0}, and m = inf ∅ = +∞. "(B) true" in 2D refers to the string tension or to a finite spatial circle, not to the vacuum-sector gap of A1 §1.

**Where non-abelian structure enters (one line):** only in S3b, as the commutator correction O(β^{−1/2}) to the Laplace method. The argument for (B) is group-blind among continuous groups. That is correct, because (B) holds for U(1), but it means nothing here distinguishes SU(2).

## 4. The test (iii)
The first CLAIMED step is S3a. It was tested in its 2D form exactly (character expansion on L × L tori, L = 2, 4, 6, 8, and in infinite volume) in `sharp_chess2d_v2.py`. The child tested the cruder δ-form in 200 cases. The results and the failed predicates are in report.md. Neither refutes S3a in 2D. A 2D test does not touch the 4D-specific inputs: the site-plane RP in 4D, the image count |Λ|/4, and the −(9/2) log β free energy.
S3b and S3c are NOT tested: no 4D Monte Carlo, and no check of the Maxwell Gibbs classification.

## 5. Weakest link, and what a challenger should attack first
1. **S3b (exchange of L → ∞ and β → ∞).** The claim is that tightness at the Gaussian scale plus local Laplace convergence of the DLR kernel forces every limit to be a free-Maxwell Gibbs state. Attack it with a translation-invariant RP Gibbs state of the SU(2) specification in which non-perturbative configurations persist at fixed distance as β → ∞. These would have to have density o(1) but total influence O(1) on O_p correlations, for example large-scale twisted or "superinstanton" boundary effects (Patrascioiu–Seiler type, cited from memory, not read). S3a excludes large *local* fields only.
2. **S3a(i):** RP of Wilson SU(2) for site-plane reflections in all directions, and the chessboard theorem with plaquettes on shared block faces. The bound is useless (> 1) unless both hold. Check the image count, since it sets the factor 1/8.
3. **S3c(i):** the Gaussian Gibbs classification for 1-forms. A non-constant stationary harmonic part would break the min-inequality. Note, though, that the inequality only needs G(n) > 0 and independence of h from ξ.
4. If all three hold, the chain proves (B) and does not prove (A). This chain says nothing about (A) or (C), and the U(1) row shows it cannot.
