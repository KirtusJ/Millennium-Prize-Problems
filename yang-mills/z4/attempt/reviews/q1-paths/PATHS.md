**Proved in writing here (unreviewed): (i) Lemma P'c, the continuum flow form of the canonical-path lemma P', on an arbitrary measure space: if every x in a σ-invariant set S sends a random path of n steps x = z₀, …, z_n = σx and the path-flow measures satisfy Σ_k π_k ≤ ρ·Q, with Q(dz,dz') = T(z,z')g(z)g(z')dz dz', then Δ ≥ 2∫_S f²/(nρ); (ii) Corollary B, a chain-of-balls construction giving ρ ≤ n·sup_S g²·max(1/v, |S|/v²)/Q_min, which is polynomial in β whenever n = O(√β), the balls have radius ~ β^{-1/2} and sup g ≤ poly(β); so −log Δ ≤ 2·sup_{balls}(−log g) + O(log β) − log ∫_S f², and no e^{-C√β} is lost; (iii) the one-dimensional theorem in the continuum (circle, Gaussian steps of variance 1/β, killing e^{−ε}, no grid): limsup_{β→∞} (−log m)/√β ≤ c* = ∫₀^π √(2ε). For SU(2)², item (i)–(ii) closes the step "continuum Lemma P'" of TUNNEL_LOWER2 §4 (tagged MISSING there). It does not close the three other inputs of TUNNEL_LOWER2 §5: (E1), (E3) and the Harnack chain H4 with its path geometry (H-c) are still CLAIMED, so the target limsup (−log m_eo)/√β ≤ c* for SU(2)² is still NOT proved. The brief's ball-to-ball form, with the wells as end sets, is true but is not enough by itself (§2.2): it needs a lower bound on |mean_{B₀} f/g|, a sign or concentration fact about f in the well that nothing here supplies. The point-start flow form avoids this.**

Worker q1-paths (task T151). I share a model family with the director and with the authors of the input files, so this is not independent review. No network source was used. Inputs read: TUNNEL_LOWER.md (§0–§2: (GS), Lemma P', Lemma C, Theorem 1D), TUNNEL_LOWER2.md (§2–§5), oned_split.py, oned_paths.py. TUNNEL_THEOREM.md and LEMMA_F.md were not reread; nothing below depends on them except the SU(2)² inputs cited in §4.

## 0. Setting and hypotheses

- (H1) (X, dx) is a σ-finite measure space. T(x,y) ≥ 0 is a measurable symmetric kernel, and T is a bounded self-adjoint operator on L²(X).
- (H2) σ is a measure-preserving involution with T(σx, σy) = T(x,y).
- (H3) g > 0 a.e. is an eigenfunction, Tg = λ_e g, with ‖g‖ = 1 and g∘σ = g. f is an eigenfunction, Tf = λ_o f, with ‖f‖ = 1 and f∘σ = −f. Δ = λ_e − λ_o.
- (H4) h := f/g, which is odd: h(σx) = −h(x).

Ground-state identity (GS, TUNNEL_LOWER §1, rechecked).
- Expand ∫∫ T g(x)g(y)h(x)h(y) using h(x)h(y) = ½(h(x)² + h(y)²) − ½(h(x) − h(y))².
- By Tonelli, ∫∫ T(x,y)g(y) g(x)h(x)² = ∫ (Tg)g h² = λ_e ∫ f².
- So λ_o = ⟨f, Tf⟩ = λ_e − E(h), where E(h) := ½∫∫ T(x,y)g(x)g(y)(h(x) − h(y))² dx dy.
- Hence **E(h) = Δ** (PROVED). Numerically this holds to 5·10⁻¹⁵ relative at β = 16 and 64 (flow_paths.py, check F0).

## 1. Lemma P'c (flow form): PROVED

**Data.**
- S ⊂ X is measurable and σ-invariant, and n ≥ 1.
- For each x ∈ S, P_x is a probability law of a path (z₀, …, z_n) ∈ X^{n+1} with z₀ = x and z_n = σx. The map x ↦ P_x is a measurable kernel.
- For k = 0, …, n−1, π_k is the measure on X × X given by π_k(F) := ∫_S g(x)² E_x[F(z_k, z_{k+1})] dx.
- Q(dz, dz') := T(z,z')g(z)g(z') dz dz'.

**Hypothesis.** Σ_{k<n} π_k ≤ ρ·Q as measures on X × X, off the diagonal. Pairs with z_k = z_{k+1} contribute 0 and can be dropped.

**Conclusion.** **Δ ≥ 2 ∫_S f² / (n ρ).**

**Proof.**
1. Fix x ∈ S. By oddness, (h(x) − h(σx))² = 4h(x)² (Lean `odd_sq`).
2. h(z₀) − h(z_n) = Σ_k (h(z_k) − h(z_{k+1})) (Lean `telescope`).
3. Cauchy–Schwarz along the path (Lean `path_cs`) gives, P_x-almost surely, 4h(x)² ≤ n Σ_k (h(z_k) − h(z_{k+1}))².
4. Take E_x, multiply by g(x)², and integrate over S. Since g²h² = f²:
   4∫_S f² ≤ n Σ_k ∫ (h(z) − h(z'))² dπ_k ≤ nρ ∫∫ T g g (h(z) − h(z'))² = nρ · 2E(h) = 2nρΔ.
   Everything is nonnegative, so Tonelli applies.
5. Rearrange (Lean `close_bound`). ∎

**Remarks.**
- No sign of f is used. Only ∫_S f² enters.
- The diagonal: if P_x gives z_k = z_{k+1} positive probability, then π_k has an atom on the diagonal and Q (which is absolutely continuous) cannot dominate it. The integrand (h(z) − h(z'))² vanishes there, so the hypothesis is only needed off the diagonal.
- The discrete Lemma P' of TUNNEL_LOWER is the special case of counting measure and deterministic paths. There the sum over edges must be over unordered edges for "≤ E(h)". If a path family uses both orientations of an edge as separate edges, one gets 2E, which is a factor 2. That is harmless, but the TUNNEL_LOWER statement ("edge e = (z, z')") leaves it ambiguous. My version uses ordered pairs and 2E throughout.

## 2. Chain of balls

### 2.1 Corollary B (construction and explicit ρ): PROVED

**Data.**
- X is a metric measure space, r_β > 0, and v := inf_c |B(c, r_β)| > 0.
- For each x ∈ S there are measurable centres c₁(x), …, c_{n−1}(x).
- Under P_x the points z_k (1 ≤ k ≤ n−1) are independent and uniform on B(c_k(x), r_β), with z₀ = x and z_n = σx.
- U is the union of the supports of the π_k. It is contained in the set of pairs (z, z') with z ∈ B(c_k(x)) (or z = x), z' ∈ B(c_{k+1}(x)) (or z' = σx), for some x and k.
- Q_min := inf_U T(z,z')g(z)g(z').

**Claim.** **ρ ≤ n · sup_S g² · max(1/v, |S|/v²) / Q_min**, and therefore Δ ≥ 2∫_S f² · Q_min / (n² sup_S g² max(1/v, |S|/v²)).

**Proof.** Write p_k for the density of π_k with respect to dz dz'.
1. For 1 ≤ k ≤ n−2: p_k(z,z') = ∫_S g(x)² 1_{B(c_k(x))}(z) 1_{B(c_{k+1}(x))}(z') / (|B||B|) dx ≤ sup_S g² |S|/v².
2. For k = 0: p₀(x, z') = g(x)² 1_S(x) 1_{B(c₁(x))}(z') / |B| ≤ sup g²/v.
3. For k = n−1: substitute w = σx, which is measure preserving, and use g∘σ = g. This gives p_{n−1}(z, w) = g(w)² 1_S(w) 1_{B(c_{n−1}(σw))}(z) / |B| ≤ sup g²/v.
4. So Σ_k p_k ≤ n · max(…), and on U this sum divided by Q is ≤ n · max(…)/Q_min. ∎

In 1D a sharper bound holds: ∫ 1{|z − x − ks| ≤ r}dx = 2r. With it, every p_k ≤ sup g²/(2r).

**Exponent accounting.** This is the point the brief asks about.
- Q_min ≥ T_min(U) · (inf_{balls} g)².
- So −log Δ ≤ 2 sup_{balls}(−log g) + log(n² sup g² max(1/v, |S|/v²)/T_min) − log(2∫_S f²).
- With n = O(√β), r_β = r/√β in dimension d (so v ≍ β^{−d/2}), sup g ≤ poly(β) and T_min ≥ poly(β)^{−1}, the middle term is O(log β).
- The exponent comes entirely from the lower bound on g at the worst ball, which is the saddle: e^{−√βΨ(saddle)} squared.
- The one-step factors e^{−(ε − Ψ'²/2)} do not appear in P'c at all. They are inside Lemma S, which produces that lower bound on g.
- Nothing of the form e^{−C n} is lost, because the hypothesis on ρ is a density comparison and not a product along the chain.

### 2.2 The brief's ball-to-ball form, and why it is not the version needed

**Corollary CB: PROVED.** Let ν_i be probability measures on B_i and m_i := ∫ h dν_i.
- By the triangle sum, Jensen ((∫∫(h(x) − h(y))dν_i dν_{i+1})² ≤ ∫∫(h(x) − h(y))² dν_i dν_{i+1}) and Cauchy–Schwarz:
  (m₀ − m_N)² ≤ N Σ_i ∫∫ (h(x) − h(y))² dν_i(x) dν_{i+1}(y).
- If Σ_i ν_i ⊗ ν_{i+1} ≤ ρ_CB Q, the right side is ≤ N ρ_CB · 2E(h) = 2Nρ_CB Δ.
- The brief's "bound each term by D(h)/min(Tgg density)" is missing this factor 2. If the products B_i × B_{i+1} overlap, the overlap multiplicity enters through ρ_CB.

**Why it does not suffice with the wells as end sets.**
- With B_N = σB₀ and ν_N = σ_*ν₀ one gets m_N = −m₀, so it yields Δ ≥ 2m₀²/(Nρ_CB).
- A useful bound then needs |m₀| = |mean_{B₀} f/g| ≥ e^{−o(√β)}. That is a statement about the sign or size of f/g in the well.
- Neither TUNNEL_LOWER nor TUNNEL_LOWER2 has it for SU(2)². TUNNEL_LOWER (I0) says plainly that positivity of f on A is not justified there.
- The weighted choice ν₀ = g²1_W/∫_W g² does not help: it gives m₀ = ∫_W fg/∫_W g², which still needs a lower bound on ∫_W fg.
- Lemma P'c avoids this by starting a path at every point x ∈ S. That is the form to use: it needs only ∫_S f², which TUNNEL_LOWER2 M4 supplies.
- Tag: CB is PROVED, and the child tests it numerically (§5). "CB with well end sets ⇒ Δ ≥ e^{−√β(c*+o(1))}" is **MISSING** the input |m₀| ≥ e^{−o(√β)}, and that input is not needed.

## 3. The one-dimensional continuum theorem: PROVED in writing

**Model.**
- X = ℝ/2πℤ with Lebesgue measure, ε(x) = 2 asinh|sin x|, σx = x + π.
- K(x,y) = Σ_{k∈ℤ} √(β/2π) e^{−β(x−y+2πk)²/2}, and T = e^{−ε/2}Ke^{−ε/2}.
- K is a symmetric Markov kernel, so ‖K‖ = 1 and λ_e ≤ ‖T‖ ≤ 1.
- T is compact with a continuous positive kernel. By Jentzsch's theorem the top eigenfunction g > 0 is simple and σ-even. f is the top eigenfunction of the odd sector.
- m := log(λ_e/λ_o) ≥ (λ_e − λ_o)/λ_e ≥ Δ, using λ_e ≤ 1.

**Theorem.** limsup_{β→∞} (−log m)/√β ≤ c* := ∫₀^π √(2ε(a)) da.

Fix η ∈ (0, η₀). Let w(η) := arcsin(sinh(3η/2)) be the half-width of {ε < 3η} around each well, so w(η) → 0. Write r := 1/(2√β). The proof has six steps.

**(L) λ_e, λ_o ≥ 1 − O(β^{−1/4}).**
- Trial u = 1_I/√|I| with I = [−ℓ, ℓ] and ℓ = β^{−1/4}.
- ⟨u, Tu⟩ ≥ e^{−2ℓ}(1 − |I|^{−1}∫_I∫_{I^c} K). The second term is ≤ E|Z|/(√β |I|) = O(β^{−1/4}).
- For λ_o use the odd trial (1_I − 1_{σI})/√(2|I|). The extra cross term is ≤ √β e^{−β(π−2ℓ)²/2}.

**(M) ∫_{ε<η} g² ≥ M_g := (λ_e − e^{−η})/(1 − e^{−η}) → 1.**
- λ_e = ‖K^{1/2}e^{−ε/2}g‖² ≤ ∫e^{−ε}g² ≤ M + e^{−η}(1 − M), where M = ∫_{ε<η} g².
- This is (L2) of TUNNEL_LOWER, Lean-checked there.
- By σ-evenness each well carries at least M_g/2 ≥ ¼ for β large.

**(H) Harnack: g ≥ μ on W' = {ε < 3η}, with μ := √β c₁ⁿ/(4 sup g), c₁ := e^{−3η−2r−2}/√(2π), n := ⌈2w√β⌉ + 1.**
- Fix x, y in one component of W'. Put c_k = x + k(y − x)/n and J_k = [c_k − r, c_k + r].
- Consecutive points satisfy |z_k − z_{k+1}| ≤ 2w/n + 2r ≤ 2/√β, and ε ≤ 3η + 2r on the J_k (ε is 2-Lipschitz).
- So T ≥ e^{−3η−2r}√(β/2π)e^{−2} on consecutive pairs. Restricting the integral of the positive kernel to the J_k gives Tⁿ(x,y) ≥ (2r)^{n−1}(e^{−3η−2r−2}√(β/2π))ⁿ = √β c₁ⁿ.
- Then g(x) = λ_e^{−n}(Tⁿg)(x) ≥ √β c₁ⁿ ∫_{well∩{ε<η}} g ≥ √β c₁ⁿ (¼)/sup g.
- sup g bound: g(x) = λ_e^{−1}∫T(x,·)g ≤ λ_e^{−1}(∫K(x,·)²)^{1/2} ≤ λ_e^{−1}(sup K)^{1/2} ≤ 2(β/2π)^{1/4}.
- Hence **−log μ ≤ 2w(η)√β(3η + 2 + ½ log 2π) + O(log β)**.
- This is the "tubes" step that TUNNEL_LOWER §2 Remarks tagged CLAIMED for the continuum. The chain of intervals J_k is the tube.

**(S) Subsolution: Tφ ≥ λ_e φ on Ω = {ε ≥ 2η}, with φ = μe^{−√βΨ}.**
- Ψ(x) := ∫₀^{d(x)} ρ_η, where d is the distance to the nearer well. ρ_η is C¹ and nondecreasing on [0, π/2], 0 where ε ≤ η, equal to √(2(ε+η)) where ε ≥ 2η, ≤ √(2(ε+η)) everywhere, and extended by reflection about π/2. The reflection is C¹ because ε'(π/2) = 0. Let H := sup|ρ_η'| and ρ̄ := sup ρ_η.
- Taylor step. For x ∈ Ω ∩ [0, π/2] and |t| ≤ M/√β, with M/√β < a₋ := (the point where ε = 2η), Ψ(x + t) ≤ Ψ₀(x + t) ≤ Ψ(x) + ρ(x)t + Ht²/2. Here Ψ₀(y) = ∫₀^y ρ̃ and Ψ = min(Ψ₀(y), Ψ₀(π − y)) ≤ Ψ₀(y).
- Also e^{−ε(x+t)/2} ≥ e^{−ε(x)/2 − |t|}.
- Gaussian tilt. The integral ∫√(β/2π)e^{−βt²/2 − √βρt}dt equals e^{ρ²/2} exactly (Lean `tilt_square`: completing the square). Restricted to |t| ≤ M/√β it is ≥ e^{ρ²/2}(1 − 2e^{−(M−ρ̄)²/2}).
- Therefore (Tφ)(x)/φ(x) ≥ e^{−ε+ρ²/2}(1 − 2e^{−(M−ρ̄)²/2})e^{−(2M+HM²)/(2√β)} = e^{η}(…)(…).
- Choose M with 1 − 2e^{−(M−ρ̄)²/2} ≥ e^{−η/2}. Then the ratio is ≥ e^{η/2 − o(1)} > 1 ≥ λ_e for β ≥ β₀(η).
- The other quarters of Ω follow by x ↦ −x and x ↦ π − x.

**(C) Lemma C (TUNNEL_LOWER §1, rechecked in the continuum).**
- Put w = g − φ. Then (λ_e − T_ΩΩ)w_Ω = T_{ΩΩᶜ}w_{Ωᶜ} + (Tφ − λ_eφ)_Ω ≥ 0.
- ‖T_ΩΩ‖ ≤ e^{−2η} < λ_e for β large, by (L). So (λ_e − T_ΩΩ)⁻¹ = Σ λ_e^{−k−1}T_ΩΩ^k preserves positivity.
- On Ωᶜ = {ε < 2η} ⊂ W' we have φ ≤ μ ≤ g by (H).
- Hence **g ≥ μe^{−√βΨ} ≥ μe^{−√βc*(η)/2} everywhere**, where c*(η) := ∫₀^π √(2(ε+η)).

**(P) Apply Corollary B (1-D sharp form) with S = X.**
- Then ∫_S f² = 1, so no Lemma M is needed for f.
- Paths: z_k = x + ks + U_k with s = π/n, n = ⌈π√β⌉, U_k uniform on [−r, r]. So s + 2r ≤ 2/√β.
- T_min ≥ e^{−2 asinh 1 − 2}√(β/2π) and Q_min ≥ T_min μ² e^{−√βc*(η)}.
- Every p_k ≤ sup g²/(2r) = √β sup g², so ρ ≤ n√β sup g²/Q_min.
- Hence **Δ ≥ 2Q_min/(n²√β sup g²) ≥ c β^{−2} μ² e^{−√β c*(η)}**.

**Conclusion.**
- −log m ≤ −log Δ ≤ √β c*(η) + 4w(η)√β(3η + 2 + ½ log 2π) + O(log β).
- By (L3) of TUNNEL_LOWER (Lean), c*(η) ≤ c* + π√(2η).
- Divide by √β, let β → ∞, then η → 0. **limsup (−log m)/√β ≤ c*.** ∎
- Compared with the grid theorem, the error E_κ has disappeared: in the continuum the Gaussian moment is exact, so δ_κ = 0.

## 4. Transfer to SU(2)²: what P'c needs and what is still open

P'c (PROVED, §1) and Corollary B (PROVED, §2.1) are dimension-free. For SU(2)² (6-dim, Haar measure, T = e^{−V/2}k⊗k e^{−V/2} as in TUNNEL_LOWER2 §0), with S = C_η ∩ {V ≤ K} (the four corners, which is σ-invariant):

| input to Corollary B | status |
|---|---|
| ∫_S f² ≥ 1 − o(1) − (1−λ_eo)/(1−e^{−K}) | PROVED given (B) (TUNNEL_LOWER2 M4); not rechecked by me |
| n = O(√β) chains of balls of radius r/√β from each x ∈ S to σx, inside D_K ∪ (tube core) | CLAIMED: it is the same geometry as (H-c) of TUNNEL_LOWER2 |
| v ≍ r⁶β^{−3}, \|S\| ≤ vol(SU(2)²): max(1/v, \|S\|/v²) = O(β⁶) | PROVED (polynomial) |
| sup g ≤ Cβ³ | CITED, TUNNEL_LOWER2 (H-b), not rechecked |
| T_min ≥ e^{−K'}(cβ^{3/2}e^{−r²})² on pairs at distance ≤ C/√β with V ≤ K' | CITED, TUNNEL_LOWER2 (H-a), not rechecked |
| inf g on corner balls ≥ μ | CLAIMED (H4) |
| inf g on tube-core balls ≥ μ(1−c₁)(1−c₂)e^{−√βΨ(a₁)}; balls of radius r/√β at the valley lie in {G ≥ 2c₁, E ≥ 2c₂} if r is small compared with M | Lemma C + S4-alg PROVED given (E1), (E3) (CLAIMED) and H4 |

Given those inputs, Corollary B gives −log Δ ≤ √β·2Ψ(π/2) + 2(−log μ) + O(log β), which is TUNNEL_LOWER2 §5 exactly. **The continuum-P' step is closed. The SU(2)² target still rests on (E1), (E3), H4 and the path geometry (H-c), all CLAIMED.**

## 5. Numerical evidence

**My test: flow_paths.py, results_flow_main.txt (check K2).**
- The model is the circle discretised with grid step κ/√β, κ = 0.25. Because P'c holds on any measure space, it must hold exactly on the grid.
- Flow as in §3(P): S = X, step s = 4 grid points = 1/√β, uniform noise over 5 points (radius 1/(2√β)).

| β | Δ (identity) | B_flow (P'c, exact ρ) | Δ/B_flow | −logΔ/√β | −logB_flow/√β | −logB_crude/√β |
|---|---|---|---|---|---|---|
| 16 | 6.004e−07 | 8.17e−09 | 73 | 3.581 | 4.656 | 5.938 |
| 64 | 2.047e−14 | 1.17e−16 | 176 | 3.940 | 4.586 | 5.363 |
| 256 | 9.142e−30 | 2.50e−32 | 366 | 4.179 | 4.548 | 5.009 |
| 1024 | 6.098e−61 | 8.04e−64 | 758 | 4.333 | 4.540 | 4.807 |
| 4096 | 7.005e−124 | 4.43e−127 | 1583 | 4.431 | 4.546 | 4.698 |

c* = 4.6054.
- F1 (P'c holds) MET 5/5.
- F2 (the explicit Corollary-B bound ≤ B_flow) MET 5/5.
- F3: log(Δ/B_flow) ≤ 3 log β, MET 4/4. The loss is about β^{0.9–1.5}, i.e. polynomial.
- F5: the crude bound's exponent gap (log Δ − log B_crude)/√β = 1.42, 0.83, 0.47, 0.27 → 0, MET.
- Child T153 (independent code, 50-digit Decimal eigenvectors) tested Corollary CB with uniform ν_i on B_i = [c_i − r, c_i + r], c_i = iπ/N, N = ⌈π√β⌉, r = 1/(2√β), κ = 0.25.
  - L = (m₀ − m_N)² ≤ M = N Σ∫∫(h−h)²dν_i dν_{i+1} ≤ R = 2Nρ_CB Δ held at 7/7 β ∈ {16, 36, 64, 100, 144, 196, 256}.
  - L = 4.00003 at β = 16 and 4.000000 for β ≥ 36, i.e. m₀ ≈ 1: in 1D h ≈ 1 in the well. That is exactly the fact §2.2 says is not available for SU(2)².
  - M/L = 6.3 → 27 and R/M = 38 → 64. Δ(identity) = Δ(E(h)) to 10⁻⁴⁹, and its Δ equals mine at β = 16, 64, 256.
  - I reran its program at β = 16, 64 (check K5): identical.

## 6. Step tags

| step | tag |
|---|---|
| (GS) E(h) = Δ in the continuum | PROVED |
| Lemma P'c (flow form, any measure space) | PROVED; scalar steps in Lean (Paths.lean) |
| Corollary B (balls, explicit ρ, polynomial loss) | PROVED |
| Corollary CB (brief's ball-to-ball Poincaré) | PROVED (with factor 2 on D) |
| CB with well end sets ⇒ lower bound | MISSING input \|mean_{B₀} f/g\| ≥ e^{−o(√β)}; not needed, P'c replaces it |
| 1D continuum (L), (M), (H) tubes, (S), (C), (P) | PROVED in writing |
| 1D continuum theorem limsup ≤ c* | PROVED in writing, unreviewed |
| SU(2)² continuum P' step | PROVED (abstract), with inputs as in the §4 table |
| SU(2)² target limsup ≤ c* | NOT PROVED; rests on (E1), (E3), H4, (H-c) |
