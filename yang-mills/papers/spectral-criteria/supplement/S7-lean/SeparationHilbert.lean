/-
SeparationHilbert.lean. The test at one time separation on a complex Hilbert space.
For a bounded self-adjoint operator `S` and a real `r ≤ 1`: the real spectrum of `S` does not meet
the open interval `(r, 1)` if and only if
`(1 + r) re⟪S v, v⟫ - re⟪S (S v), v⟫ ≤ r ‖v‖²` for every vector `v`.
The proof is the continuous functional calculus: `(r - S)(1 - S) = cfc (fun x => (r - x)(1 - x)) S`
is non-negative exactly when the function is non-negative on the spectrum.
-/
import Mathlib

namespace SeparationHilbert
open scoped InnerProductSpace

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

theorem one_separation_hilbert (S : H →L[ℂ] H) (hS : IsSelfAdjoint S) (r : ℝ) (hr : r ≤ 1) :
    (∀ x ∈ spectrum ℝ S, ¬ (r < x ∧ x < 1)) ↔
      ∀ v : H, (1 + r) * (⟪S v, v⟫_ℂ).re - (⟪S (S v), v⟫_ℂ).re ≤ r * ‖v‖ ^ 2 := by
  have hcfc : cfc (fun x : ℝ => (r - x) * (1 - x)) S
      = (algebraMap ℝ (H →L[ℂ] H) r - S) * (1 - S) := by
    rw [cfc_mul (fun x : ℝ => r - x) (fun x : ℝ => 1 - x) S,
      cfc_sub (fun _ : ℝ => r) (fun x : ℝ => x) S,
      cfc_sub (fun _ : ℝ => (1 : ℝ)) (fun x : ℝ => x) S,
      cfc_const r S, cfc_const (1 : ℝ) S, cfc_id' ℝ S]
    simp
  have hsa : IsSelfAdjoint (cfc (fun x : ℝ => (r - x) * (1 - x)) S) := cfc_predicate _ S
  have hnn := cfc_nonneg_iff (fun x : ℝ => (r - x) * (1 - x)) S
  rw [ContinuousLinearMap.nonneg_iff_isPositive] at hnn
  have hpos : (cfc (fun x : ℝ => (r - x) * (1 - x)) S).IsPositive ↔
      ∀ v : H, 0 ≤ (⟪(cfc (fun x : ℝ => (r - x) * (1 - x)) S) v, v⟫_ℂ).re := by
    constructor
    · intro h v; have := h.2 v; rwa [ContinuousLinearMap.reApplyInnerSelf_apply] at this
    · intro h; exact ⟨hsa, fun v => by rw [ContinuousLinearMap.reApplyInnerSelf_apply]; exact h v⟩
  have hform : ∀ v : H, (⟪(cfc (fun x : ℝ => (r - x) * (1 - x)) S) v, v⟫_ℂ).re
      = r * ‖v‖ ^ 2 - ((1 + r) * (⟪S v, v⟫_ℂ).re - (⟪S (S v), v⟫_ℂ).re) := by
    intro v
    rw [hcfc]
    have e : ((algebraMap ℝ (H →L[ℂ] H) r - S) * (1 - S)) v
        = (r : ℂ) • v - (r : ℂ) • S v - S v + S (S v) := by
      simp [Algebra.algebraMap_eq_smul_one, sub_smul, smul_sub, map_sub]
      abel
    rw [e, inner_add_left, inner_sub_left, inner_sub_left, inner_smul_left, inner_smul_left,
      inner_self_eq_norm_sq_to_K]
    simp
    have hre : (((‖v‖ : ℝ) : ℂ) ^ 2).re = ‖v‖ ^ 2 := by norm_cast
    rw [hre]; ring
  have hscal : ∀ x : ℝ, 0 ≤ (r - x) * (1 - x) ↔ ¬ (r < x ∧ x < 1) := by
    intro x
    constructor
    · rintro h ⟨h1, h2⟩
      have : (r - x) * (1 - x) < 0 := mul_neg_of_neg_of_pos (by linarith) (by linarith)
      linarith
    · intro h
      by_cases h1 : x ≤ r
      · exact mul_nonneg (by linarith) (by linarith)
      · push_neg at h1
        have h2 : 1 ≤ x := le_of_not_lt fun hc => h ⟨h1, hc⟩
        exact mul_nonneg_of_nonpos_of_nonpos (by linarith) (by linarith)
  constructor
  · intro h v
    have h1 : ∀ x ∈ spectrum ℝ S, 0 ≤ (r - x) * (1 - x) := fun x hx => (hscal x).mpr (h x hx)
    have h2 := (hpos.mp (hnn.mpr h1)) v
    rw [hform] at h2; linarith
  · intro h x hx
    have h1 : ∀ v : H, 0 ≤ (⟪(cfc (fun x : ℝ => (r - x) * (1 - x)) S) v, v⟫_ℂ).re := fun v => by
      rw [hform]; linarith [h v]
    exact (hscal x).mp ((hnn.mp (hpos.mpr h1)) x hx)

omit [CompleteSpace H] in
/-- The quadratic inequality passes from a dense set of vectors to all vectors. -/
theorem dense_to_all (S : H →L[ℂ] H) (r : ℝ) (D : Set H) (hD : Dense D)
    (h : ∀ v ∈ D, (1 + r) * (⟪S v, v⟫_ℂ).re - (⟪S (S v), v⟫_ℂ).re ≤ r * ‖v‖ ^ 2) :
    ∀ v : H, (1 + r) * (⟪S v, v⟫_ℂ).re - (⟪S (S v), v⟫_ℂ).re ≤ r * ‖v‖ ^ 2 := by
  have hclosed : IsClosed {v : H | (1 + r) * (⟪S v, v⟫_ℂ).re - (⟪S (S v), v⟫_ℂ).re ≤ r * ‖v‖ ^ 2} := by
    apply isClosed_le
    · exact ((continuous_const.mul (Complex.continuous_re.comp
        (Continuous.inner S.continuous continuous_id))).sub
        (Complex.continuous_re.comp (Continuous.inner (S.continuous.comp S.continuous)
        continuous_id)))
    · exact continuous_const.mul (continuous_norm.pow 2)
  intro v
  have : v ∈ closure D := hD v
  exact hclosed.closure_subset_iff.mpr (fun x hx => h x hx) this

/-- Proposition (a test at one time separation), as stated: testing on a dense set suffices. -/
theorem one_separation_dense (S : H →L[ℂ] H) (hS : IsSelfAdjoint S) (r : ℝ) (hr : r ≤ 1)
    (D : Set H) (hD : Dense D) :
    (∀ x ∈ spectrum ℝ S, ¬ (r < x ∧ x < 1)) ↔
      ∀ v ∈ D, (1 + r) * (⟪S v, v⟫_ℂ).re - (⟪S (S v), v⟫_ℂ).re ≤ r * ‖v‖ ^ 2 := by
  rw [one_separation_hilbert S hS r hr]
  exact ⟨fun h v _ => h v, fun h => dense_to_all S r D hD h⟩

end SeparationHilbert

#print axioms SeparationHilbert.one_separation_hilbert
#print axioms SeparationHilbert.one_separation_dense
