import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace YangMills.InteriorLeakage

/-- Fixing either leg within δ of r forces the energy above the one-leg threshold. -/
theorem oneLegFloor {k r p q δ : ℝ} (hδ : 0 ≤ δ) (hr : r-δ ≤ p)
    (hsum : k ≤ p+q) (hdif : p-q ≤ k) :
    max k (2*r-k) - 2*δ ≤ p+q := by
  rcases le_total k (2*r-k) with h | h
  · rw [max_eq_right h]
    linarith
  · rw [max_eq_left h]
    linarith

/-- The closure of the physical momentum triangle attains that floor. -/
theorem edgeAttains {k r : ℝ} (hk : 0 ≤ k) (hr : k < 2*r) :
    0 ≤ |k-r| ∧ k ≤ r+|k-r| ∧ abs (r - abs (k-r)) ≤ k ∧
    r+|k-r| = max k (2*r-k) := by
  refine ⟨abs_nonneg _, ?_, ?_, ?_⟩
  · linarith [le_abs_self (k-r)]
  · rw [abs_le]
    rcases le_total r k with h | h
    · rw [abs_of_nonneg (sub_nonneg.mpr h)]
      constructor <;> linarith
    · rw [abs_of_nonpos (sub_nonpos.mpr h)]
      constructor <;> linarith
  · rcases le_total r k with h | h
    · rw [abs_of_nonneg (sub_nonneg.mpr h), max_eq_left (by linarith)]
      ring
    · rw [abs_of_nonpos (sub_nonpos.mpr h), max_eq_right (by linarith)]
      ring

/-- A third affine cost beats both endpoint costs somewhere precisely when its
slope is strictly below their mean. Both transitions cost d to lose one leg. -/
theorem middlePhase {e s k d : ℝ} (he : s < e) (hk : k ≤ s) (hd : 0 < d) :
    (∃ t : ℝ, 0 < t ∧ d+t*s < t*e ∧ d+t*s < 2*d+t*k) ↔ 2*s < e+k := by
  constructor
  · rintro ⟨t, ht, h₁, h₂⟩
    by_contra h
    have hx := mul_nonneg ht.le (sub_nonneg.mpr (le_of_not_gt h))
    nlinarith
  · intro h
    have hden : 0 < e-k := by linarith
    refine ⟨2*d/(e-k), div_pos (by linarith) hden, ?_, ?_⟩
    all_goals
      field_simp [hden]
      apply (div_lt_div_iff_of_pos_right hden).mpr
      nlinarith [mul_pos hd (sub_pos.mpr h)]

/-- For the magnetic triangle the intermediate slope lies strictly between
the endpoint slopes and is exposed exactly in this momentum range. -/
theorem interiorRange {k e : ℝ} :
    (k < max k (e-k) ∧ 2*max k (e-k) < e+k) ↔
      2*k < e ∧ e < 3*k := by
  rcases le_total k (e-k) with h | h
  · rw [max_eq_right h]
    constructor <;> rintro ⟨h₁,h₂⟩ <;> constructor <;> linarith
  · rw [max_eq_left h]
    constructor <;> rintro ⟨h₁,h₂⟩ <;> constructor <;> linarith

end YangMills.InteriorLeakage
#print axioms YangMills.InteriorLeakage.oneLegFloor
#print axioms YangMills.InteriorLeakage.edgeAttains
#print axioms YangMills.InteriorLeakage.middlePhase
#print axioms YangMills.InteriorLeakage.interiorRange
