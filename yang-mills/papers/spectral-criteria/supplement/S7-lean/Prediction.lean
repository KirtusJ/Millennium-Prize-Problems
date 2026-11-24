/-
Prediction.lean. The Hilbert-space core of the proposition "Conditional prediction".
On a real inner product space (think of square-integrable functions of two consecutive slices):
 `Ey`  conditional expectation given the next slice,
 `Eyc` conditional expectation given the next slice and the coarse field of the present one,
 `P`   conditional expectation given the coarse field,
 `M`   multiplication by the indicator of the good set of coarse fields,
all self-adjoint idempotent bounded operators, with `Ey Eyc = Ey` (tower property),
`Eyc P = P` (a function of the coarse field is known given it) and `M Eyc = Eyc M`.
If `‖Eyc g‖² ≤ (1 - γ) ‖g‖²` for every `g = M (f - P f)` (this is what a bound `1 - γ` on the squared
conditional maximal correlation over the good set gives), then
`‖f‖² - ‖Ey f‖² ≥ γ ‖M (f - P f)‖²` for every `f`.
The identification `⟪f, (I - A²) f⟫ = ‖f‖² - ‖Ey f‖²` for functions of the present slice, and the
passage from the maximal correlation to the hypothesis, are measure theory and are not formalised.
-/
import Mathlib

namespace Prediction
open scoped InnerProductSpace

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

theorem pyth_proj (R : E →L[ℝ] E) (hsa : ∀ x y, ⟪R x, y⟫_ℝ = ⟪x, R y⟫_ℝ)
    (hid : ∀ x, R (R x) = R x) (x : E) : ‖x‖ ^ 2 = ‖R x‖ ^ 2 + ‖x - R x‖ ^ 2 := by
  have o : ⟪R x, x - R x⟫_ℝ = 0 := by
    rw [inner_sub_right, hsa x x, hsa x (R x), hid, sub_self]
  have := norm_add_sq_real (R x) (x - R x)
  rw [o, add_sub_cancel] at this; linarith

theorem proj_norm_le (R : E →L[ℝ] E) (hsa : ∀ x y, ⟪R x, y⟫_ℝ = ⟪x, R y⟫_ℝ)
    (hid : ∀ x, R (R x) = R x) (x : E) : ‖R x‖ ^ 2 ≤ ‖x‖ ^ 2 := by
  have := pyth_proj R hsa hid x
  nlinarith [sq_nonneg ‖x - R x‖]

theorem conditional_prediction (Ey Eyc P M : E →L[ℝ] E)
    (hYsa : ∀ x y, ⟪Ey x, y⟫_ℝ = ⟪x, Ey y⟫_ℝ) (hYid : ∀ x, Ey (Ey x) = Ey x)
    (hCsa : ∀ x y, ⟪Eyc x, y⟫_ℝ = ⟪x, Eyc y⟫_ℝ) (hCid : ∀ x, Eyc (Eyc x) = Eyc x)
    (hMsa : ∀ x y, ⟪M x, y⟫_ℝ = ⟪x, M y⟫_ℝ) (hMid : ∀ x, M (M x) = M x)
    (htower : ∀ x, Ey (Eyc x) = Ey x)
    (hP : ∀ x, Eyc (P x) = P x)
    (hcomm : ∀ x, M (Eyc x) = Eyc (M x))
    (γ : ℝ)
    (hρ : ∀ f, ‖Eyc (M (f - P f))‖ ^ 2 ≤ (1 - γ) * ‖M (f - P f)‖ ^ 2) (f : E) :
    γ * ‖M (f - P f)‖ ^ 2 ≤ ‖f‖ ^ 2 - ‖Ey f‖ ^ 2 := by
  obtain ⟨h, hh⟩ : ∃ h : E, h = f - P f := ⟨_, rfl⟩
  rw [← hh]
  -- conditioning on more: ‖Ey f‖ ≤ ‖Eyc f‖
  have s1 : ‖Ey f‖ ^ 2 ≤ ‖Eyc f‖ ^ 2 := by
    have := proj_norm_le Ey hYsa hYid (Eyc f)
    rwa [htower] at this
  -- ‖f‖² - ‖Eyc f‖² = ‖f - Eyc f‖²
  have s2 := pyth_proj Eyc hCsa hCid f
  -- f - Eyc f = h - Eyc h
  have s3 : f - Eyc f = h - Eyc h := by
    rw [hh, map_sub, hP]; abel
  -- split h - Eyc h along M
  obtain ⟨a, ha⟩ : ∃ a : E, a = h - Eyc h := ⟨_, rfl⟩
  have s4 := pyth_proj M hMsa hMid a
  have s5 : M a = M h - Eyc (M h) := by rw [ha, map_sub, hcomm]
  have s6 := pyth_proj Eyc hCsa hCid (M h)
  have s7 := hρ f
  rw [← hh] at s7
  rw [s3, ← ha] at s2
  rw [s5] at s4
  nlinarith [sq_nonneg ‖a - (M h - Eyc (M h))‖]

end Prediction

#print axioms Prediction.conditional_prediction
