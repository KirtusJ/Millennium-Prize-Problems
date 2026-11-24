/-
Criterion.lean. The spectral criterion (Theorem "Spectral criterion") for a bounded self-adjoint
operator `S` on a complex Hilbert space whose real spectrum lies in `[0, 1]` (in the paper
`S = e^{-τH}`). For `v` and `n` put `dd v n = re⟪S^n (v - S v), v⟫` (the paper's `d_{v,n}`).
Let `0 < r < 1` and let `D` be a set of vectors with dense linear span. Then the spectrum of `S`
misses the open interval `(r, 1)` if and only if for every `v ∈ D` and every `ρ > r` there is a
constant `C` with `dd v n ≤ C ρ^n` for all `n`.
The condition on the right is the statement `limsup_n d_{v,n}^{1/n} ≤ r` written without roots;
the equivalence of the two forms is elementary and is not formalised here.
-/
import Mathlib

namespace Criterion
open scoped InnerProductSpace

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- the paper's `d_{v,n}` -/
noncomputable def dd (S : H →L[ℂ] H) (v : H) (n : ℕ) : ℝ := (⟪(S ^ n) (v - S v), v⟫_ℂ).re

/-- A function that is non-negative on the spectrum gives a non-negative form. -/
theorem form_nonneg (S : H →L[ℂ] H) (hS : IsSelfAdjoint S) (f : ℝ → ℝ)
    (hf : ContinuousOn f (spectrum ℝ S)) (h : ∀ x ∈ spectrum ℝ S, 0 ≤ f x) (v : H) :
    0 ≤ (⟪(cfc f S) v, v⟫_ℂ).re := by
  have h1 : 0 ≤ cfc f S := (cfc_nonneg_iff f S hf hS).mpr h
  rw [ContinuousLinearMap.nonneg_iff_isPositive] at h1
  have := h1.2 v
  rwa [ContinuousLinearMap.reApplyInnerSelf_apply] at this

theorem cfc_dd (S : H →L[ℂ] H) (hS : IsSelfAdjoint S) (n : ℕ) :
    cfc (fun x : ℝ => x ^ n * (1 - x)) S = S ^ n * (1 - S) := by
  rw [cfc_mul (fun x : ℝ => x ^ n) (fun x : ℝ => 1 - x) S,
    cfc_pow (fun x : ℝ => x) n S, cfc_sub (fun _ : ℝ => (1 : ℝ)) (fun x : ℝ => x) S,
    cfc_const (1 : ℝ) S, cfc_id' ℝ S]
  simp

theorem dd_eq (S : H →L[ℂ] H) (hS : IsSelfAdjoint S) (n : ℕ) (v : H) :
    dd S v n = (⟪(cfc (fun x : ℝ => x ^ n * (1 - x)) S) v, v⟫_ℂ).re := by
  rw [cfc_dd S hS n]; unfold dd
  simp [map_sub]

/-- Direction (1) ⇒ (2), with the explicit constant `‖v‖²`. -/
theorem gap_implies_rate (S : H →L[ℂ] H) (hS : IsSelfAdjoint S)
    (hspec : ∀ x ∈ spectrum ℝ S, 0 ≤ x ∧ x ≤ 1) (r : ℝ) (hr0 : 0 < r)
    (hgap : ∀ x ∈ spectrum ℝ S, ¬ (r < x ∧ x < 1)) (v : H) (n : ℕ) :
    dd S v n ≤ ‖v‖ ^ 2 * r ^ n := by
  have hscal : ∀ x ∈ spectrum ℝ S, 0 ≤ r ^ n - x ^ n * (1 - x) := by
    intro x hx
    obtain ⟨h0, h1⟩ := hspec x hx
    by_cases hxr : x ≤ r
    · have a1 : x ^ n ≤ r ^ n := pow_le_pow_left₀ h0 hxr n
      have a2 : 0 ≤ x ^ n := pow_nonneg h0 n
      nlinarith
    · push_neg at hxr
      have hx1 : x = 1 := le_antisymm h1 (le_of_not_lt fun hc => hgap x hx ⟨hxr, hc⟩)
      rw [hx1]; simp; positivity
  have hnn := form_nonneg S hS (fun x : ℝ => r ^ n - x ^ n * (1 - x))
    (by fun_prop) hscal v
  have hsplit : cfc (fun x : ℝ => r ^ n - x ^ n * (1 - x)) S
      = algebraMap ℝ (H →L[ℂ] H) (r ^ n) - cfc (fun x : ℝ => x ^ n * (1 - x)) S := by
    rw [cfc_sub (fun _ : ℝ => r ^ n) (fun x : ℝ => x ^ n * (1 - x)) S, cfc_const (r ^ n) S]
  rw [hsplit] at hnn
  rw [dd_eq S hS n v]
  have e : (⟪(algebraMap ℝ (H →L[ℂ] H) (r ^ n) - cfc (fun x : ℝ => x ^ n * (1 - x)) S) v, v⟫_ℂ).re
      = ‖v‖ ^ 2 * r ^ n - (⟪(cfc (fun x : ℝ => x ^ n * (1 - x)) S) v, v⟫_ℂ).re := by
    simp [Algebra.algebraMap_eq_smul_one, inner_sub_left, inner_smul_left,
      inner_self_eq_norm_sq_to_K]
    rw [← Complex.ofReal_pow, ← Complex.ofReal_pow]
    simp only [Complex.ofReal_re, Complex.ofReal_im]; ring
  rw [e] at hnn; linarith

/-- A tent function: continuous, between `0` and `1`, equal to `1` at `x0`, zero at distance
`δ` or more from `x0`. -/
noncomputable def tent (x0 δ : ℝ) (x : ℝ) : ℝ := max 0 (1 - |x - x0| / δ)

theorem tent_cont (x0 δ : ℝ) : Continuous (tent x0 δ) := by
  unfold tent; fun_prop

theorem tent_nonneg (x0 δ x : ℝ) : 0 ≤ tent x0 δ x := le_max_left _ _

theorem tent_le_one (x0 δ : ℝ) (hδ : 0 < δ) (x : ℝ) : tent x0 δ x ≤ 1 := by
  unfold tent
  have : 0 ≤ |x - x0| / δ := div_nonneg (abs_nonneg _) hδ.le
  exact max_le zero_le_one (by linarith)

theorem tent_center (x0 δ : ℝ) : tent x0 δ x0 = 1 := by
  unfold tent; simp

theorem tent_pos (x0 δ : ℝ) (hδ : 0 < δ) (x : ℝ) (h : 0 < tent x0 δ x) : |x - x0| < δ := by
  unfold tent at h
  by_contra! hc
  have : 1 - |x - x0| / δ ≤ 0 := by
    have : 1 ≤ |x - x0| / δ := by rw [le_div_iff₀ hδ]; linarith
    linarith
  rw [max_eq_left this] at h; exact lt_irrefl 0 h

/-- Direction (2) ⇒ (1). -/
theorem rate_implies_gap (S : H →L[ℂ] H) (hS : IsSelfAdjoint S)
    (hspec : ∀ x ∈ spectrum ℝ S, 0 ≤ x ∧ x ≤ 1) (r : ℝ) (hr0 : 0 < r)
    (D : Set H) (hD : Dense (Submodule.span ℂ D : Set H))
    (hrate : ∀ v ∈ D, ∀ ρ : ℝ, r < ρ → ∃ C : ℝ, ∀ n : ℕ, dd S v n ≤ C * ρ ^ n) :
    ∀ x ∈ spectrum ℝ S, ¬ (r < x ∧ x < 1) := by
  rintro x0 hx0 ⟨hrx, hx1⟩
  obtain ⟨α, hα⟩ : ∃ α : ℝ, α = (r + x0) / 2 := ⟨_, rfl⟩
  obtain ⟨ω, hω⟩ : ∃ ω : ℝ, ω = (x0 + 1) / 2 := ⟨_, rfl⟩
  obtain ⟨δ, hδ⟩ : ∃ δ : ℝ, δ = min (x0 - α) (ω - x0) := ⟨_, rfl⟩
  have hαr : r < α := by rw [hα]; linarith
  have hαx : α < x0 := by rw [hα]; linarith
  have hωx : x0 < ω := by rw [hω]; linarith
  have hω1 : ω < 1 := by rw [hω]; linarith
  have hα0 : 0 < α := by linarith
  have hδpos : 0 < δ := by rw [hδ]; exact lt_min (by linarith) (by linarith)
  have hδ1 : δ ≤ x0 - α := by rw [hδ]; exact min_le_left _ _
  have hδ2 : δ ≤ ω - x0 := by rw [hδ]; exact min_le_right _ _
  obtain ⟨g, hg⟩ : ∃ g : ℝ → ℝ, g = tent x0 δ := ⟨_, rfl⟩
  have hgc : Continuous g := by rw [hg]; exact tent_cont x0 δ
  have hg0 : ∀ x, 0 ≤ g x := fun x => by rw [hg]; exact tent_nonneg x0 δ x
  have hg1 : ∀ x, g x ≤ 1 := fun x => by rw [hg]; exact tent_le_one x0 δ hδpos x
  have hgx0 : g x0 = 1 := by rw [hg]; exact tent_center x0 δ
  have hgpos : ∀ x, 0 < g x → α < x ∧ x < ω := fun x hx => by
    rw [hg] at hx
    have := tent_pos x0 δ hδpos x hx
    rw [abs_lt] at this
    constructor <;> linarith
  obtain ⟨G, hG⟩ : ∃ G : H →L[ℂ] H, G = cfc g S := ⟨_, rfl⟩
  have hGsa : IsSelfAdjoint G := by rw [hG]; exact cfc_predicate g S
  have hGG : cfc (fun x : ℝ => g x * g x) S = G * G := by
    rw [hG, cfc_mul g g S hgc.continuousOn hgc.continuousOn]
  -- the form of G * G is ‖G v‖²
  have hGGform : ∀ v : H, (⟪(G * G) v, v⟫_ℂ).re = ‖G v‖ ^ 2 := fun v => by
    have h1 : ⟪(G * G) v, v⟫_ℂ = ⟪G v, G v⟫_ℂ := by
      have := ContinuousLinearMap.adjoint_inner_right G (G v) v
      rw [hGsa.adjoint_eq] at this
      exact this.symm
    rw [h1, inner_self_eq_norm_sq_to_K]; norm_cast
  -- lower bound for dd
  have hlow : ∀ (v : H) (n : ℕ), α ^ n * (1 - ω) * ‖G v‖ ^ 2 ≤ dd S v n := by
    intro v n
    have hscal : ∀ x ∈ spectrum ℝ S,
        0 ≤ x ^ n * (1 - x) - α ^ n * (1 - ω) * (g x * g x) := by
      intro x hx
      obtain ⟨h0, h1⟩ := hspec x hx
      rcases (hg0 x).eq_or_lt with hz | hp
      · rw [← hz]; simp
        exact mul_nonneg (pow_nonneg h0 n) (by linarith)
      · obtain ⟨ha, hb⟩ := hgpos x hp
        have a1 : α ^ n ≤ x ^ n := pow_le_pow_left₀ hα0.le ha.le n
        have a2 : 0 ≤ α ^ n := pow_nonneg hα0.le n
        have a3 : g x * g x ≤ 1 := by nlinarith [hg0 x, hg1 x]
        have a4 : 0 ≤ g x * g x := mul_nonneg (hg0 x) (hg0 x)
        have a5 : 0 < 1 - ω := by linarith
        have a6 : α ^ n * (1 - ω) ≤ x ^ n * (1 - x) :=
          mul_le_mul a1 (by linarith) a5.le (pow_nonneg h0 n)
        have a7 : α ^ n * (1 - ω) * (g x * g x) ≤ α ^ n * (1 - ω) * 1 :=
          mul_le_mul_of_nonneg_left a3 (mul_nonneg a2 a5.le)
        linarith
    have hcont : ContinuousOn (fun x : ℝ => g x * g x) (spectrum ℝ S) :=
      (hgc.mul hgc).continuousOn
    have hnn := form_nonneg S hS
      (fun x : ℝ => x ^ n * (1 - x) - α ^ n * (1 - ω) * (g x * g x))
      ((by fun_prop : Continuous fun x : ℝ => x ^ n * (1 - x)).continuousOn.sub
        (continuousOn_const.mul hcont)) hscal v
    have hsplit : cfc (fun x : ℝ => x ^ n * (1 - x) - α ^ n * (1 - ω) * (g x * g x)) S
        = cfc (fun x : ℝ => x ^ n * (1 - x)) S - (α ^ n * (1 - ω)) • (G * G) := by
      rw [cfc_sub (fun x : ℝ => x ^ n * (1 - x))
        (fun x : ℝ => α ^ n * (1 - ω) * (g x * g x)) S
        (by fun_prop : Continuous fun x : ℝ => x ^ n * (1 - x)).continuousOn
        (continuousOn_const.mul hcont),
        cfc_const_mul (α ^ n * (1 - ω)) (fun x : ℝ => g x * g x) S hcont, hGG]
    rw [hsplit] at hnn
    have e : (⟪(cfc (fun x : ℝ => x ^ n * (1 - x)) S - (α ^ n * (1 - ω)) • (G * G)) v, v⟫_ℂ).re
        = dd S v n - α ^ n * (1 - ω) * ‖G v‖ ^ 2 := by
      rw [dd_eq S hS n v, ContinuousLinearMap.sub_apply, inner_sub_left, Complex.sub_re,
        ContinuousLinearMap.smul_apply, ← hGGform v]
      congr 1
      rw [← Complex.coe_smul, inner_smul_left]
      simp
      have h1 : ((α : ℂ) ^ n).re = α ^ n := by rw [← Complex.ofReal_pow]; exact Complex.ofReal_re _
      have h2 : ((α : ℂ) ^ n).im = 0 := by rw [← Complex.ofReal_pow]; exact Complex.ofReal_im _
      rw [h1, h2]; ring
    rw [e] at hnn; linarith
  -- G vanishes on D
  have hGD : ∀ v ∈ D, G v = 0 := by
    intro v hv
    obtain ⟨ρ, hρ⟩ : ∃ ρ : ℝ, ρ = (r + α) / 2 := ⟨_, rfl⟩
    have hρr : r < ρ := by rw [hρ]; linarith
    have hρα : ρ < α := by rw [hρ]; linarith
    have hρ0 : 0 < ρ := by linarith
    obtain ⟨C, hC⟩ := hrate v hv ρ hρr
    rcases eq_or_ne (G v) 0 with hz | hne
    · exact hz
    exfalso
    have hnpos : 0 < ‖G v‖ := norm_pos_iff.mpr hne
    obtain ⟨a, ha⟩ : ∃ a : ℝ, a = (1 - ω) * ‖G v‖ ^ 2 := ⟨_, rfl⟩
    have hapos : 0 < a := by rw [ha]; exact mul_pos (by linarith) (by positivity)
    have hone : 1 < α / ρ := by rw [one_lt_div hρ0]; exact hρα
    obtain ⟨n, hn⟩ := pow_unbounded_of_one_lt (C / a) hone
    have h1 := (hlow v n).trans (hC n)
    have h2 : α ^ n * a ≤ C * ρ ^ n := by rw [ha]; linarith [h1]
    have hρn : 0 < ρ ^ n := pow_pos hρ0 n
    have h3 : (α / ρ) ^ n * a ≤ C := by
      rw [div_pow, div_mul_eq_mul_div, div_le_iff₀ hρn]; exact h2
    have h4 : (α / ρ) ^ n ≤ C / a := by rw [le_div_iff₀ hapos]; exact h3
    linarith
  -- hence G = 0
  have hker : ∀ v : H, G v = 0 := by
    have hsub : (Submodule.span ℂ D : Set H) ⊆ (LinearMap.ker (G : H →ₗ[ℂ] H) : Set H) := by
      have : Submodule.span ℂ D ≤ LinearMap.ker (G : H →ₗ[ℂ] H) :=
        Submodule.span_le.mpr (fun v hv => by
          simp only [SetLike.mem_coe, LinearMap.mem_ker]; exact hGD v hv)
      exact this
    have hclosed : IsClosed (LinearMap.ker (G : H →ₗ[ℂ] H) : Set H) :=
      ContinuousLinearMap.isClosed_ker G
    intro v
    have hv : v ∈ closure (Submodule.span ℂ D : Set H) := hD v
    have := (hclosed.closure_subset_iff.mpr hsub) hv
    simpa using this
  have hG0 : G = 0 := by ext v; simp [hker v]
  -- but g x0 = 1 lies in the spectrum of G
  have hmap : spectrum ℝ (cfc g S) = g '' spectrum ℝ S := cfc_map_spectrum g S hS hgc.continuousOn
  have hmem : (1 : ℝ) ∈ spectrum ℝ (cfc g S) := by
    rw [hmap]; exact ⟨x0, hx0, hgx0⟩
  rw [← hG, hG0] at hmem
  rcases subsingleton_or_nontrivial (H →L[ℂ] H) with hsub | hnt
  · rw [spectrum.of_subsingleton] at hmem; exact hmem
  · rw [spectrum.zero_eq] at hmem
    exact one_ne_zero (Set.mem_singleton_iff.mp hmem)

/-- Theorem (spectral criterion) for `S = e^{-τH}`: the spectrum of `S` misses `(r, 1)` if and
only if the differences `dd v n` decay at any rate `ρ > r` for every `v` in a set with dense
span. -/
theorem spectral_criterion (S : H →L[ℂ] H) (hS : IsSelfAdjoint S)
    (hspec : ∀ x ∈ spectrum ℝ S, 0 ≤ x ∧ x ≤ 1) (r : ℝ) (hr0 : 0 < r)
    (D : Set H) (hD : Dense (Submodule.span ℂ D : Set H)) :
    (∀ x ∈ spectrum ℝ S, ¬ (r < x ∧ x < 1)) ↔
      ∀ v ∈ D, ∀ ρ : ℝ, r < ρ → ∃ C : ℝ, ∀ n : ℕ, dd S v n ≤ C * ρ ^ n := by
  constructor
  · intro hgap v _ ρ hρ
    refine ⟨‖v‖ ^ 2, fun n => ?_⟩
    have h1 := gap_implies_rate S hS hspec r hr0 hgap v n
    have h2 : r ^ n ≤ ρ ^ n := pow_le_pow_left₀ hr0.le hρ.le n
    have h3 : ‖v‖ ^ 2 * r ^ n ≤ ‖v‖ ^ 2 * ρ ^ n := mul_le_mul_of_nonneg_left h2 (by positivity)
    linarith
  · exact rate_implies_gap S hS hspec r hr0 D hD

end Criterion

#print axioms Criterion.spectral_criterion
