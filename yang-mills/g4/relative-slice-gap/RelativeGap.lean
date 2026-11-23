import Mathlib.Analysis.InnerProductSpace.Projection
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace Millennium.G4.RelativeGap

/-- In one weighted cell the squared norm of the residual is its variance. -/
theorem column_residual (size projected residual h : ℝ) (hs : 0 ≤ size)
    (hh : 0 ≤ h) (hp : h * size ≤ projected)
    (orth : residual^2 + projected^2 = size^2) :
    residual^2 ≤ (1-h^2)*size^2 := by
  have hsq := pow_le_pow_left₀ (mul_nonneg hh hs) hp 2
  nlinarith [hsq]

/-- Losing an orthogonal component of norm at most t‖v‖ changes the squared
quadratic form of an actual Hilbert-space operator by at most t²‖v‖². -/
theorem projection_form {E F : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    [NormedAddCommGroup F] [InnerProductSpace ℝ F] (A : E →L[ℝ] F)
    (K : Submodule ℝ F) [K.HasOrthogonalProjection] (t : ℝ)
    (res : ∀ v : E, ‖A v - (K.orthogonalProjection (A v) : F)‖ ≤ t*‖v‖) (v : E) :
    ‖A v‖^2 ≤ ‖(K.orthogonalProjection (A v) : F)‖^2 + t^2*‖v‖^2 := by
  have hp := K.orthogonalProjectionFn_norm_sq (A v)
  simp only [Submodule.orthogonalProjectionFn_eq] at hp
  have h := pow_le_pow_left₀ (norm_nonneg _) (res v) 2
  rw [mul_pow] at h
  nlinarith only [hp, h]

/-- Comparing every direction on every trial subspace is enough for the same
additive bound on its minimax threshold. The threshold is expressed directly
by existence of a subspace with a bound on all its unit directions. -/
theorem variational_threshold {V S : Type*} (unitIn : S → V → Prop)
    (small large : V → ℝ) (a loss : ℝ)
    (test : ∃ s, ∀ v, unitIn s v → small v ≤ a)
    (perturb : ∀ s v, unitIn s v → large v ≤ small v + loss) :
    ∃ s, ∀ v, unitIn s v → large v ≤ a + loss := by
  obtain ⟨s, hs⟩ := test
  exact ⟨s, fun v hv => (perturb s v hv).trans (add_le_add_right (hs v hv) _)⟩

-- NATIVE CHILD 1
/-- The two scale factors cancel from a relative, squared transfer ratio. -/
theorem scale_free_upper (s v b l num : ℝ) (hb : 0 < b) (hl : 0 < l)
    (hs : l*b ≤ s) (hv : v^2 ≤ num*b^2) (hn : 0 ≤ num) :
    v^2 / s^2 ≤ num / l^2 := by
  have hs' : 0 < s := (mul_pos hl hb).trans_le hs
  have hsq := pow_le_pow_left₀ (mul_nonneg hl.le hb.le) hs 2
  rw [mul_pow] at hsq
  apply (div_le_div_iff₀ (sq_pos_of_pos hs') (sq_pos_of_pos hl)).2
  calc
    v^2*l^2 ≤ (num*b^2)*l^2 := mul_le_mul_of_nonneg_right hv (sq_nonneg _)
    _ = num*(l^2*b^2) := by ring
    _ ≤ num*s^2 := mul_le_mul_of_nonneg_left hsq hn

/-- A normalized second singular value from a table with relative operator error. -/
theorem measured_ratio (x y b measured error : ℝ) (hm : 0 < measured)
    (hb : b ≤ (1+error)*measured) (r : ℝ) (hr : 0 ≤ r)
    (hx : x ≤ r*b) (hy : y ≤ x+error*measured) :
    y/measured ≤ (1+error)*r+error := by
  apply (div_le_iff₀ hm).2
  nlinarith only [hy, hx, mul_le_mul_of_nonneg_left hb hr]

-- NATIVE CHILD 2
lemma two_compressions (u p c t : ℝ) (h₁ : u ≤ p + t^2) (h₂ : p ≤ c + t^2) :
    u ≤ c + 2 * t^2 := by
  linarith only [h₁, h₂]

theorem packing_constants :
    32^32 < 24*29^32 ∧ (1/100 - 1/128 : ℝ) = 7/3200 := by
  constructor <;> norm_num

theorem finite_test_constants :
    (25:ℕ)^13 < 3*23^13 ∧
    (((((1+1/1000)*(23/25+1/200)+2/1000)/(1-1/1000)+1/200)^2+
      2*(1/20)^2)/(199/200)^2 : ℝ) < 9/10 := by
  constructor <;> norm_num

#print axioms column_residual
#print axioms projection_form
#print axioms variational_threshold
#print axioms scale_free_upper
#print axioms measured_ratio
#print axioms two_compressions
#print axioms packing_constants
#print axioms finite_test_constants

end Millennium.G4.RelativeGap
