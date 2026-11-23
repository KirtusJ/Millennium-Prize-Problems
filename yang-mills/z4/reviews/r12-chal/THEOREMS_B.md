## 2. The statements, proofs and hypotheses

Notation: k ∈ BZ (−π < k_i b ≤ π, each mode once, per the review note); k̂_i = (2/b)sin(k_i b/2); P₃₃ = (k̂₁² + k̂₂²)/k̂².
- a(k) = P₃₃ (k̂/2) e^(−t k̂) e^(−2s k̂²).
- Step 1 of PROOF_FREE_BOUNDS carries over unchanged, with w replaced by a. Its proof is unaffected, because the flow is a positive multiplier on each mode:
  C_{b,s}(t) = (2/l⁶) Σ_{k,k'≠0} |f̂_b(k+k')|² a(k) a(k').
  Checked numerically: position space and momentum double sum agree to ≤ 1.5·10⁻¹⁵ (P0). The child agreed independently to 6·10⁻¹⁵.

**Hypotheses used:**
- H1 (normalization of D, from STATEMENT/brief; not rederived here). The brief's D_{t,s} carries e^(−2s k̂²), i.e. the flow factor once per field.
- H2 (Wick).
- H3: f real, C⁴, periodic, ∫f ≠ 0.
- H4: N ≥ 3.
- HΩ = 0 (review note).
- s > 0.
- b ≤ b₀ = min(l/3, 2π(|∫f|/(2S₄D₄))^(1/4)), from PROOF_FREE_BOUNDS 4c. Here b₀ = 0.2537.
- For v₂ only: N ≥ 2M + 1 with M = ⌈l/(π√s)⌉, so effectively b ≲ √s.

**Lemmas that carry over unchanged:**
- aliasing lemma (2, 2a, 2b);
- Jordan bound 3a, (2/π)|k| ≤ k̂ ≤ |k|;
- the 4-mode selection 4a, the concavity argument 4b, and b₀ from 4c;
- the spectral identification of section 1. Because the flow is within the time slice, the flowed O is still a function of time-zero fields.

**Lemmas that need the flow factor or are replaced:**
- 3b–3d (replaced);
- 4a (gains a factor);
- a new lower bound v₂;
- B2 and B3, which are new.

**Theorem B1.** For all t ≥ 0, including t = 0:
v(s,t) := max(v₁, v₂) ≤ C_{b,s}(t) ≤ V(s), where:
- v₁(s,t) = (1/(2l⁶))(∫f)² · m(t) · e^(−16π²s/l²), with m(t) = min(κ₃² e^(−2tκ₃), (2π/l)² e^(−4πt/l)) and κ₃ = 3√3/l.
  This is PROOF_FREE_BOUNDS 4a–4c. The flow factor e^(−4s κ_N²) is bounded below using κ_N ≤ 2π/l.
- v₂(s,t) = (1/(2l⁶))(∫f)² (16/π⁶) Σ_{0<|n|∞≤M} ((k₁²+k₂²)²/|k|²) e^(−2t|k| − 4s|k|²), with k = 2πn/l.
  - Proof: keep all diagonal pairs (k, −k) with |n|∞ ≤ M ≤ (N−1)/2, not just four.
  - Use |f̂_b(0)| ≥ ∫f/2 (2b, for b ≤ b₀).
  - Use P₃₃ ≥ (4/π²)(k₁²+k₂²)/|k|² and k̂² ≥ (4/π²)|k|² (from 3a), with e^(−2tk̂ − 4sk̂²) ≥ e^(−2t|k| − 4s|k|²).
- V(s) = (2/l³) Φ · (π²/l²) · U₂(64s/l²). Here:
  - U_q(c) is a rigorous upper bound for Σ_{n≠0} |n|^q e^(−c|n|²). It is built as a product of 1-D bounds:
    - θ₀ ≤ 1 + √(π/c);
    - θ_j = Σ m^(2j) e^(−cm²) ≤ Γ(j+½) c^(−j−½) + 2(j/(ec))^j (unimodal integrand: integral plus maximum);
    - multinomial expansion of |n|^(2p).
  - Φ ≥ b³Σ_x f(bx)². It is either l³ sup f² (no condition), or ∫f² + S₄(b₀/2π)⁴ ‖Δ²(f²)‖₁ (aliasing lemma applied to f² at q = 0).
- Proof of the upper bound:
  1. Schur step [Lean `schur`]. With F(k,k') = |f̂_b(k+k')|², every row and column sum is ≤ Σ_q |f̂_b(q)|² = l³ b³ Σ f² (Parseval). Hence C ≤ (2/l³) Φ Σ_k a(k)².
  2. Then use a(k)² ≤ (|k|²/4) e^(−16s|k|²/π²). For the polynomial factor use k̂ ≤ |k|; for the Gaussian use k̂ ≥ (2/π)|k|; drop e^(−2tk̂) ≤ 1.
  3. Enlarge the BZ to all n ≠ 0.
  4. V does not depend on t. This is consistent because t ↦ C is antitone [Lean `C_antitone`].
- Scaling: U₂(c) ~ (3/2)π^(3/2) c^(−5/2) as c → 0. This gives V ~ 2Φ (3/2)π^(7/2)/32768 · s^(−5/2), independent of l.
  - The loss against the true constant is a factor ≈ 60 asymptotically:
    - (π/2)⁵ from Jordan;
    - 15/8 from P₃₃² ≤ 1;
    - Φ/∫f² = 3.3, because the aliasing margin at b₀ is large for this f.

Numbers at t = 0:

| s | v₁ | v₂ | C (continuum) | V |
|---|---|---|---|---|
| 0.002 | 19.9 | 52.9 | 5633 | 6.63·10⁵ |
| 0.005 | 12.4 | 5.44 | 533 | 9.16·10⁴ |
| 0.02 | 1.16 | 0.128 | 9.39 | 5825 |

**Theorem B3 (t = 0).** Write A_p = Σ_k a(k)² k̂^p ≤ (1/4)(2π/l)^(2+p) U_(2+p)(64s/l²).
- Weighted AM–GM [Lean `weighted_amgm`] in the Schur step, with the optimal λ, gives:
  - M₀ ≤ (2/l³)ΦA₀;
  - M₁ ≤ (4/l³)Φ√(A₀A₂);
  - M₂ ≤ (4/l³)Φ(√(A₀A₄) + A₂).
- With M₀ ≥ v(s,0) [Lean `ratio_bound`]:
  - M₁/M₀ ≤ (4/l³)Φ√(A₀A₂)/v(s,0);
  - M₂/M₀ ≤ (4/l³)Φ(√(A₀A₄) + A₂)/v(s,0).
  Both are independent of b for b ≤ b₀ (and N ≥ 2M + 1 when v₂ is used).
- s-scaling. A_p ~ s^(−(5+p)/2) (proved from the U asymptotics). With v₂ ~ s^(−5/2), this gives M₁/M₀ ≲ s^(−1/2) and M₂/M₀ ≲ s^(−1).
  - The v₂ ~ s^(−5/2) step is **measured** (v₂ s^(5/2) = 9.463, 9.448, 9.445, 9.445·10⁻⁶), not proved. It needs a Riemann-sum lower bound for the finite sum in v₂, which I did not write.
  - With v₁ alone (proved), the ratios are b-uniform but scale only like s^(−3) and s^(−4).
- Measured moments: M₁/M₀ = 33.95, 21.65, 13.56 and M₂/M₀ = 1269, 513, 188 at s = 0.002, 0.005, 0.02 (N = 128). So √s·M₁/M₀ ≈ 1.52, 1.53, 1.92 and s·M₂/M₀ ≈ 2.5, 2.6, 3.8, consistent with the expected scaling.
- The proved bounds are loose: 7.1·10⁵, 2.6·10⁵, 9.1·10⁴ for M₁/M₀.

**Theorem B2.** C_s(t) is the continuum sum over all k ∈ (2π/l)ℤ³∖0, with |k| in place of k̂ and the continuum flow e^(−2s|k|²). For s > 0, t ≥ 0 and b ≤ b₀:
|C_{b,s}(t) − C_s(t)| ≤ K₁ b² + K₂ e^(−s/b²) ≤ (K₁ + K₂/(es)) b², with

- K₁ = (2/l⁶)[(F + ‖f‖₁) S₄ D₄ b₀²/π⁴ (Σā)² + 2l³ ∫f² √(Σh² Σā²)];
- K₂ = (2/l⁶)·2l³(Φ + 2∫f²)·√(Σā*² Σā²).

Here:
- ā = (|k|/2) e^(−8s|k|²/π²);
- ā*² = (|k|²/4) e^(−8s|k|²/π²);
- h = (|k|³/24)[3/2 + |k|(t + 4s|k|)/2] e^(−8s|k|²/π²);
- every sum over ℤ³∖0 is bounded by U_q.

Steps:
1. Termwise: |k̂_i − k_i| ≤ b²|k_i|³/24, from sin y ≥ y − y³/6. Hence |k̂vec − k| ≤ b²|k|³/24.
2. Mean value theorem for φ(p) = ((p₁²+p₂²)/(2|p|)) e^(−t|p| − 2s|p|²) on the segment [k̂vec, k]. The segment avoids 0, and |p| ∈ [(2/π)|k|, |k|] on it. The gradient bound is |∇φ| ≤ (3/2 + |p|(t+4s|p|)/2)e^(…), since |∇g| ≤ 1 + ½. This gives |a_b − a_c| ≤ b² h.
3. Pairs with k + k' ∈ BZ: use the aliasing lemma, |f̂_b(q) − f̃(q)| ≤ S₄(b/π)⁴D₄.
4. Remaining pairs. Either k + k' ∉ BZ for k, k' ∈ BZ, so max(|k|,|k'|) ≥ π/(2b); or one momentum lies outside the BZ in the continuum sum. Both are Gaussian tails, ā(k) ≤ ā*(k) e^(−s/b²) [Lean `exp_neg_le_inv` for e^(−x) ≤ 1/(ex)].
5. The b²-term and the tail term use the Schur/Parseval step with ∫f² or Φ, not sup|f̃|.

A first version (P3, sup|f̃| in place of Parseval and e^(−s/b²) ≤ b²/(es) throughout) is also valid, but 100× looser.
- K₁ = 8.0·10¹², 1.3·10¹¹, 4.0·10⁸ for s = 0.002, 0.005, 0.02. The aliasing term dominates. That term is honestly b⁴; I bounded b⁴ ≤ b₀²b².
- True error coefficient e_N/b²: 2.4·10⁵, 9.5·10³, 88. So K₁ is 10⁷ to 10⁹ too large. The rate is proved; the constant is useless in practice.

**Lean (R11Flow.lean), exactly what is proved, all over ℝ:**
1. `flow_decreases`: 0 ≤ x, 0 ≤ s, 0 ≤ y ⇒ x e^(−sy) ≤ x.
2. `C_antitone`: for finite sums with w_i ≥ 0, E_i ≥ 0 and t ≤ t': Σ w_i e^(−t'E_i) ≤ Σ w_i e^(−tE_i).
3. `weighted_amgm`: for λ > 0, xy ≤ (λx² + y²/λ)/2.
4. `schur`: F ≥ 0 with all row and column sums over a Finset ≤ P ⇒ Σ_{i,j} F_ij a_i a_j ≤ P Σ a_i².
5. `ratio_bound`: 0 < v ≤ M₀, 0 ≤ M₁ ≤ U ⇒ M₁/M₀ ≤ U/v.
6. `exp_neg_le_inv`: x > 0 ⇒ e^(−x) ≤ 1/(e·x).

Not in Lean:
- sin y ≥ y − y³/6 (Mathlib has no ready lemma for all y; not attempted);
- the theta-function bounds;
- the mean-value step;
- the aliasing lemma;
- Parseval;
- the identification of C with the momentum sum.

