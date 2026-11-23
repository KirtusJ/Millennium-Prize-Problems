PROVED (with K normalised, κ_0 = 1): limsup β^{1/3} ν_k(β) ≤ E_k for every k, with complete proofs. CLAIMED: liminf β^{1/3} ν_k(β) ≥ E_k for every k, and hence β^{1/3} m_e(β) → E_1 − E_0 > 0. The liminf lemmas are written out, but the final Γ-liminf and compactness step (L6, L7) is only a sketch and has not been reviewed independently. As the brief states it, with K unnormalised, the theorem is FALSE (see §0).

# Scaling limit of the center-even spectrum, two-direction SU(2) model (g2-conv, T77)

Tags:
- **PROVED**: the argument is given here.
- **PROVED+LEAN**: the scalar step is checked in `scalar.lean` (exit 0; axioms propext, Classical.choice, Quot.sound).
- **CITED**: with a locator and how it was read.
- **NUM**: checked numerically in `checks.py` (results/checks2.json).
- **SKETCH**: a standard argument, outlined but not written in full.
- **CLAIMED** / **MISSING**: as named.

The director and I share a model family, so my agreement with this text is not independent review.

## 0. Statement, and a defect in the statement as posed

**Notation.**
- Sector S: functions on SU(2)² that are invariant under simultaneous conjugation and even under both center flips.
- Kernel: k(g) = e^{(β/2)Tr g}/Z with Z = 2I_1(β)/β, so ∫k = 1.
- K = convolution by k(U_1W_1^{-1})k(U_2W_2^{-1}) on S. Its eigenvalue on Peter–Weyl degree (n_1, n_2) is κ_{n_1}κ_{n_2}, where κ_n = I_{n+1}(β)/I_1(β) and n = 2j.
- T = e^{−V/2}Ke^{−V/2}. Its eigenvalues on S are λ_0 > λ_1 ≥ …. Define ν_k := −ln λ_k.
- h = −½Δ + 2|Y_1×Y_2|² on L²(R⁶), defined as the Friedrichs extension from C_c^∞. E_0 < E_1 ≤ … are its eigenvalues on rotation-invariant functions.

**Defect (of the target statement).** The brief puts the per-link eigenvalue e^{−β}(2/β)I_{2j+1}(β) into K.
- Then −log T_brief = −log T + c(β), with c(β) = −2 ln(e^{−β}(2/β)I_1(β)) = 3 ln β + ln(π/2) + o(1) → ∞.
- So β^{1/3}μ_k → ∞ and the statement as written is false.
- With K normalised (κ_0 = 1) the statement is the one below. Gaps are unaffected.

**Theorem.** For every k, β^{1/3} ν_k(β) → E_k as β → ∞. Hence β^{1/3} m_e(β) → E_1 − E_0 > 0.

**Status of each part:**
- Upper half (limsup): PROVED (§2).
- Lower half (liminf): CLAIMED (§3). Its new ingredient, the capped fibre lemma L4, is PROVED. The concluding compactness step is a SKETCH.

## 1. The continuum operator h

**C1. h has compact resolvent, and E_0 ≥ 2.9458.** PROVED + CITED.
- Fibre inequality: for fixed Y_1, write Y_2 = Y_∥ + Y_⊥, so that |Y_1×Y_2|² = |Y_1|²|Y_⊥|². The harmonic-oscillator bound a p² + b x² ≥ √(ab) in each of the two ⊥ coordinates (a = ¼, b = |Y_1|²) gives
  −¼Δ_{Y_2} + |Y_1×Y_2|² ≥ |Y_1|.
- Adding this to the same bound with the roles of Y_1 and Y_2 exchanged:
  q_h(φ) ≥ ¼‖∇φ‖² + ∫(|Y_1|+|Y_2|)|φ|²  on C_c^∞.
- The right side, A = −¼Δ + |Y_1| + |Y_2|, has compact resolvent because its potential tends to ∞. CITED: Reed–Simon IV, Thm XIII.67 (from memory, not reread).
- Min-max comparison gives N_h(E) ≤ N_A(E) < ∞, so h has compact resolvent.
- Restricting to rotation-invariant functions (a reducing subspace) keeps this.
- E_0 ≥ inf spec A = 2(¼)^{1/3}·a′, where a′ = 2.33810741 is the ground energy of −u″ + ru on the half-line.
  - a′ is CITED (Abramowitz–Stegun, Table 10.13, from memory) and NUM: reproduced by shooting, B7.
  - So E_0 ≥ 2.94583 (B8). This is consistent with E_0 = 3.35053 in NUMERICS.md.

**C2. Simplicity and gap.** CITED.
- e^{−th} is positivity improving for V ∈ L²_loc bounded below (Reed–Simon IV, Thm XIII.47, from memory). So the ground state is simple and positive.
- It is therefore rotation invariant, and E_1 > E_0 on the invariant sector.

**C3. A core for min-max.** PROVED (standard).
- C_c^∞ is a form core by the definition of the Friedrichs extension.
- Rotation averaging maps C_c^∞ to C_c^∞, commutes with h, and is a form-norm contraction. So invariant C_c^∞ functions form a core for h restricted to the invariant sector.
- Consequently, for every ε > 0 and k there are invariant φ_0..φ_k ∈ C_c^∞, supported in {|Y| ≤ R(ε)}, whose span Φ satisfies max_Φ q_h/‖·‖² ≤ E_k + ε. (Approximate the eigenvectors in form norm; the Gram and form matrices converge.)

## 2. Upper bound: limsup β^{1/3} ν_k ≤ E_k (PROVED)

**U0. Variational form.** PROVED; this is TORON_GAP S1.
- With f = e^{V/2}g and W = e^V − 1:
  1 − λ_k = μ_k := min_{dim G=k+1} max_{g∈G} Q(g), with Q(g) = ⟨g,(1−K+W)g⟩/⟨g,(1+W)g⟩ ≤ ⟨g,(1−K+W)g⟩/‖g‖².
- ν_k = −ln(1−μ_k) ≤ μ_k/(1−μ_k) (PROVED+LEAN F5).

**U1. Kinetic comparison.** CITED + PROVED + NUM.
- CITED: Ruiz-Antolín & Segura, "A new type of sharp bounds for ratios of modified Bessel functions", arXiv:1606.02008 (2016), Theorem 2, bounds b_1 (lower, ν ≥ 0) and b_0 (upper, ν ≥ ½) for I_ν/I_{ν−1}. Read by a fetch sub-agent from the arXiv HTML page. After the shift ν → ν+1:
  x/(ν+1+√((ν+1)²+x²)) ≤ r_ν(x) := I_{ν+1}/I_ν ≤ x/(ν+½+√((ν+½)²+x²)),  for ν ≥ 0.
- NUM (B1, B2): 5614 grid cases, 0 failures.
- From the lower bound:
  −ln r_ν ≤ arsinh((ν+1)/x) ≤ (ν+1)/x,
  so −ln κ_n = Σ_{ν=1}^{n} −ln r_ν ≤ n(n+3)/(2β) (B3, 0 failures).
- Since n(n+3) ≤ n(n+2) + √(n(n+2)), and using 1−ab ≤ (1−a)+(1−b) (PROVED+LEAN F1) and 1−κ ≤ −ln κ:
  **1 − K ≤ (1/2β) Σ_i (−Δ_i + (−Δ_i)^{1/2})**,
  where −Δ_i is the Laplacian of the unit S³ in U_i (eigenvalue n_i(n_i+2)).

**U2. Chart comparison.** PROVED.
- Use exponential coordinates U = exp(iA·σ), with |A| = a = geodesic distance to 1, and normalised Haar measure (1/2π²) sin²a da dω.
- For f supported in a < π:
  - ‖f‖² ≥ (1 − a_max²/3)·(1/2π²)∫|f|²d³A, from sin²a ≥ a²(1−a²/3) (B6);
  - ∫|∇f|²dvol = (1/2π²)∫[(∂_a f)² sin²a + |∇_ω f|²] da dω ≤ (1/2π²)∫|∇_A f|² d³A, from sin²a ≤ a² (B6).
  - The same comparisons hold in each factor.

**U3. Potential.** PROVED.
- V = 2β sin²a_1 sin²a_2 sin²γ ≤ 2β|A_1×A_2|² = β^{−1/3}·2|Y_1×Y_2|² when Y = β^{1/3}A.
- W ≤ V e^{V}, and V ≤ R⁴β^{−1/3}/2 on {|Y| ≤ R}.

**U4. Center copies.** PROVED.
- For φ ∈ Φ, let g_φ = Σ_{z∈{±1}²} f(zU) with f(U) = φ(β^{1/3}A(U)). This g_φ lies in S: conjugation acts on A by a rotation, φ is invariant, and the sum is center-even. The map φ ↦ g_φ is linear and injective.
- The supports are disjoint, and W and 1 are local.
- Cross terms of K between copies z ≠ z′: in some factor U_iW_i^{-1} lies within 2Rβ^{−1/3} of −1. So the kernel product is ≤ e^{β}/Z² ≤ C β³ e^{−β}, using Z ≥ (2/π)(δ³/3)(1−δ²/3)e^{β(1−δ²/2)} with δ = β^{−1/2}.
- Combined with ‖f‖_1 ≤ ‖f‖_2, the cross terms are O(β³e^{−β})‖g‖².

**U5. Conclusion.**
- Combining U1–U4 and rescaling (d^6A = β^{−2}d^6Y; each ∇_A brings β^{1/3}), uniformly on the finite-dimensional Φ (where ‖∇φ‖/‖φ‖ ≤ C_Φ):
  max_{g∈g_Φ} Q(g) ≤ β^{−1/3}(E_k + ε)(1 + O(R⁴β^{−1/3}) + O(R²β^{−2/3})) + O(β^{−2/3}C_Φ) + O(β³e^{−β}).
- Then U0 gives limsup β^{1/3}ν_k ≤ E_k + ε for every ε.
- No decay of the eigenfunctions of h is needed, because C3 supplies compactly supported trial functions.
- The same trial functions bound the eigenvalues ν_k^H of H := 1 − K + V from above, since W ≥ V.

## 3. Lower bound: liminf β^{1/3} ν_k ≥ E_k (CLAIMED)

**L1. From T to H = 1 − K + V.** PROVED + PROVED+LEAN F2, F3, F6.
- With a = ⟨g,(1−K)g⟩ ≤ n = ‖g‖² and v = ⟨g,Vg⟩ ≤ w = ⟨g,Wg⟩:
  Q(g) = (a+w)/(n+w) ≥ (a+v)/(n+v) ≥ t/(1+t), where t = (a+v)/n.
- t ↦ t/(1+t) is increasing, so min-max gives μ_k ≥ ν^H_k/(1+ν^H_k), and ν_k ≥ μ_k (F6).
- It therefore suffices to show liminf β^{1/3}ν^H_k ≥ E_k, where ν^H_k are the eigenvalues of H on S.
- These are discrete below 1: K is trace class, so σ_ess(H) = σ_ess(1+V) ⊂ [1, 1+2β].

**L2. Moments of k.** PROVED + NUM.
- E_k[cos a] = (d/dβ) ln Z = I_2/I_1, using I_1′ = I_2 + I_1/x.
- 1 − I_2/I_1 ≤ 2/β follows from the cited lower bound (B5).
- a² ≤ (π²/2)(1 − cos a) on [0, π] (B6).
- Hence ∫k(g) d(g,1)² dg ≤ π²/β per link.

**L3. IMS localisation for the non-local K.** PROVED.
- For real, conjugation- and center-invariant χ_α with Σχ_α² = 1 and Lipschitz constant ≤ L:
  ⟨g,(1−K)g⟩ = Σ_α⟨χ_αg,(1−K)χ_αg⟩ + ½∫∫k₂(U,W)g(U)g(W)Σ_α(χ_α(U)−χ_α(W))².
  This is the identity Σ_αχ_α(U)χ_α(W) = 1 − ½Σ(χ_α(U)−χ_α(W))².
- By a Schur bound and L2, the last term is ≥ −(#α)·L²·(2π²/β)‖g‖².
- The V-term localises exactly.

**L4. Capped fibre lemma.** PROVED. This is the step where the arms are handled.
- Statement: there are β_0 and s_* = 0.002 such that for β ≥ β_0, 0 < σ ≤ s_*, and any unit vector n, on L²(SU(2)):
  (1 − K_1) + 2βσ²|x⃗ × n|² ≥ σ − 1/β,
  where x⃗ = Im-part coordinates of U, so that |x⃗ × n|² = sin²a sin²γ.
- Proof:
  - B := 2βσ²|x⃗×n|² is a polynomial of degree 2 on S³ ⊂ R⁴, so it couples Peter–Weyl degrees n, n′ only when |n − n′| ≤ 2. Also ‖B‖ ≤ 2βσ².
  - Take a spin partition χ_lo(n)² + χ_hi(n)² = 1, with χ_lo = cos(π/2·clip((n−M)/M, 0, 1)) and M = m√β, m² = ½.
  - K_1 is diagonal in n, so it localises exactly.
  - B = Σχ_iBχ_i + ½Σ_i[χ_i,[χ_i,B]]. The double commutator is a sum of block shifts of B by d ∈ [−2, 2] with weights (χ(n+d)−χ(n))² ≤ (π|d|/2M)², so its norm is ≤ 5π²‖B‖/M². The localisation error is therefore ≤ 5π²σ²/m² ≈ 98.7σ².
  - High part (n ≥ M): B4 (the Amos-type upper bound) gives −ln κ_n ≥ n(n+2)/(2(β+n+½)) ≥ ¼(1−o(1)), so 1 − κ_n ≥ 0.22.
  - Low part (n ≤ 2M): with y = −ln κ_n ≤ n(n+3)/(2β) ≤ 1 + o(1), we have 1 − κ_n ≥ y(1−y/2) ≥ ½(1−o(1))·n(n+2)/(2β). Then TORON_GAP S7 gives −Δ + 4λρ² ≥ 4(√λ−1).
    - S7 rechecked here: (−Δφ)/φ for φ = e^{−k sin²χ} recomputed; minimisation PROVED+LEAN F4.
    - With λ = 2β²σ² this gives ½(−Δ/2β) + 2βσ²ρ² ≥ √2σ − 1/β.
  - Total: ≥ min(√2σ, 0.22) − 98.7σ² − 1/β − o(σ) ≥ σ − 1/β for σ ≤ 0.002 and β ≥ β_0.

**L5. Tightness: the arms carry no low-energy mass.** PROVED from L3 and L4.
- Take σ_R = Rβ^{−1/3} and s_i = |sin a_i|, which is center- and conjugation-invariant.
- Partition with η_i = θ(s_i/σ_R), where θ is a smooth step from 0 at 1 to 1 at 2:
  - χ_2 = η_2;
  - χ_1 = η_1(1−η_2²)^{1/2};
  - χ_0 = ((1−η_1²)(1−η_2²))^{1/2}.
- supp χ_i ⊂ {s_i ≥ σ_R} for i = 1, 2. supp χ_0 lies in the four boxes {s_1, s_2 ≤ 2σ_R}, which are rescaled neighbourhoods |Y_i| ≲ πR of the center points.
- On {s_2 ≥ σ_R}: V = 2βs_2²|x⃗_1×n_2|² ≥ 2βσ_R²|x⃗_1×n_2|², and 1 − K ≥ 1 − K_1. So L4, applied fibrewise in U_2, gives ⟨χ_2g,Hχ_2g⟩ ≥ (Rβ^{−1/3} − 1/β)‖χ_2g‖². The same holds for χ_1.
- With L ≤ Cβ^{1/3}/R, the IMS error is ≤ C′β^{−1/3}/R².
- Hence, for any g ∈ S with ⟨g,Hg⟩ ≤ Eβ^{−1/3}‖g‖²: ‖χ_1g‖² + ‖χ_2g‖² ≤ (E + C′R^{−2})/(R − o(1))·‖g‖².
- In the rescaled picture this is uniform tightness. It also explains why the arm closes: near a_2 = π the box of the other center copy takes over.

**L6. Γ-liminf in one box.** SKETCH.
- Setting: f_β is supported in the box at (1,1), with β^{1/3}⟨f_β,Hf_β⟩ ≤ C. Let φ_β be its rescaling, supported in |Y| ≤ cR.
- High spins: by B4, 1 − K ≥ 0.22 on spins ≥ m√β. So the high-spin part P^⊥f_β has norm² ≤ Cβ^{−1/3}/0.22 → 0.
- Low spins: on spins ≤ m√β with m → 0 slowly, 1 − K ≥ (1−o(1))(−Δ/2β).
- U2 in the lower direction (sin²a ≥ a²(1−a²/3)) shows the rescaled Pf_β is bounded in H¹ on balls.
- By Rellich, φ_β → φ strongly in L² along a subsequence (the supports are bounded).
- Weak lower semicontinuity of the Dirichlet form, together with V ≥ 2|Y_1×Y_2|²(1−O(R²β^{−2/3}))β^{−1/3} on the box, gives
  liminf β^{1/3}⟨f_β,Hf_β⟩ ≥ q_h(φ).

**L7. Conclusion.** SKETCH.
- Let g_0..g_k be orthonormal eigenvectors of H in S. Note ν^H_k ≤ C β^{−1/3} by §2.
- For g = Σc_jg_j, L3 gives Σ_α⟨χ_αg,Hχ_αg⟩ ≤ ν^H_k + C′β^{−1/3}R^{−2}.
- The four box pieces are center translates, and their K-cross terms are O(β³e^{−β}) as in U4.
- Take a subsequence on which the rescaled (1,1)-box pieces of g_j converge (L6). By L5 their limits ψ_j have Gram matrix ¼(I + O(1/R)), so they are independent. They are rotation invariant.
- L6 applied to every combination gives q_h ≤ (liminf β^{1/3}ν^H_k + C′R^{−2})/(1 − C/R) on their span.
- Min-max for h restricted to the invariant sector, followed by R → ∞, gives E_k ≤ liminf β^{1/3}ν^H_k.

**What would make §3 PROVED rather than CLAIMED:**
- write L6 and L7 in full: the m → 0 bookkeeping, and the fact that the low-spin projection does not preserve the box support (handled by a second spatial cutoff);
- an independent reader.

No step of §3 depends on an unproved inequality. Its only external inputs are the cited Bessel bounds (Ruiz-Antolín–Segura Thm 2) and Rellich.

## 4. Numerical check of coercivity 2(a), delegated to child T82: the naive form is FALSE

**The predicate I set.**
- Statement: β^{1/3}·inf spec(1 − K + V − D) ≥ −1, where D = |sin a_1| + |sin a_2|. This is the lattice copy of h ≥ −¼Δ + |Y_1| + |Y_2|.
- It FAILED in 2 of 2 β:
  - Galerkin upper bounds −2.39 at β = 16 and −3.35 at β = 64, still decreasing with N;
  - β = 256 was not computed.
  - The child's numbers were reproduced by my rerun (K4, K5).
- **Cause.** 1 − K ≤ 1. A state localised at high spin at a_1 = a_2 = π/2 with a common axis costs at most about 1 in kinetic energy and V ≈ 0 there, while D = 2. So inf spec(H − D) ≤ about −1 for every β, and β^{1/3}·inf → −∞.
- **Whose failure.** It was my own expectation, not a defect of the target. Any coercivity weight must be capped where 1 − K saturates.
- The correct form is the one proved in L4/L5:
  H ≥ min(s, s_*)-type bound on the arms, i.e. β^{−1/3}·min(|Y|-type, s_*β^{1/3}) − Cβ^{−1/3}R^{−2},
  and this weight still tends to ∞ pointwise in the rescaled variable.
- Measured only: β^{1/3}·inf spec(1−K+V) = 2.004 (β=16) and 2.460 (β=64), rising towards E_0 = 3.35. This is consistent with §2–3 but slow.

## 5. Center-odd sector; U(1)

**Center-odd sector.**
- The center-even restriction is what the symmetrisation in U4 and L7 uses: the four box pieces of a center-even g are translates of each other, so one box carries the whole limit.
- On the full gauge-invariant space the center-odd sectors contain tunnelling copies of the ground state. NUMERICS.md measured splittings of about e^{−c√β} (measured, not proved).
- So **on the full gauge-invariant space the gap is NOT of order β^{−1/3}**. The theorem concerns S only.

**U(1)² discriminator.**
- V ≡ 0, so W = 0 and H = 1 − K, and L4 has no potential term. The fibre bound becomes 1 − K ≥ 0, with no growth along the flat torus.
- L5 fails: there is no tightness.
- The spectrum is exactly −ln(I_{n_1}I_{n_2}/I_0²). The even gap is −ln(I_2/I_0), with β·gap = 2.064, 2.016, 2.004, 2.001 at β = 16, 64, 256, 1024 (checks.py M1), which tends to 2.
- The proof uses the commutator only through L4/L5 and U3.

## 6. What remains
- L6 and L7 written in full, plus an independent check of §3.
- The cited sources were not reread: Reed–Simon XIII.47/67 and Abramowitz–Stegun were cited from memory. Ruiz-Antolín–Segura was read by a sub-agent from the HTML; its last third was only summarised.
- No rate of convergence.
- Three spatial directions: not attempted. The same architecture applies, but V has three terms and the valley is larger.
