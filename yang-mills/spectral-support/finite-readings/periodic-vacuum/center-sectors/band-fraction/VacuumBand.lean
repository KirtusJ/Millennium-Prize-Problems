import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace YangMills.VacuumBand
open scoped RealInnerProductSpace
variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℝ H]

/-- A positive tail with a known upper endpoint can be centered at half its width. -/
theorem centeredTail (r ε : ℝ) (lower : 0 ≤ r) (upper : r ≤ ε) :
    |r - ε / 2| ≤ ε / 2 := by
  apply abs_le.mpr
  constructor <;> linarith

/-- Squared length after removal of the component along a unit trial vector. -/
theorem perpendicularSquare (f x : H) (unit : ⟪f,f⟫ = 1) :
    ‖x - ⟪f,x⟫ • f‖ ^ 2 = ‖x‖ ^ 2 - ⟪f,x⟫ ^ 2 := by
  rw [← real_inner_self_eq_norm_sq, ← real_inner_self_eq_norm_sq]
  simp only [inner_sub_left, inner_sub_right, real_inner_smul_left, real_inner_smul_right, unit]
  rw [real_inner_comm x f]
  ring

/-- Lower bound on a band direction's overlap using both perpendicular lengths. -/
theorem projectedDirection (f h x : H) (unit : ⟪f,f⟫ = 1) :
    ⟪f,h⟫ * ⟪f,x⟫ - ‖h-⟪f,h⟫ • f‖ * ‖x-⟪f,x⟫ • f‖ ≤ ⟪h,x⟫ := by
  have lower := (abs_le.mp (abs_real_inner_le_norm (h-⟪f,h⟫ • f) (x-⟪f,x⟫ • f))).1
  simp only [inner_sub_left, inner_sub_right, real_inner_smul_left, real_inner_smul_right,
    unit] at lower
  rw [real_inner_comm h f] at lower ⊢
  nlinarith only [lower]

theorem polynomialDegree : 2 * 6 + 2 * 18 + 4 ≤ 2 * 32 - 1 := by decide

/-- A band whose weights decay more slowly preserves its share at positive lag. -/
theorem bandShareAtLag (w r wt rt k : ℝ) (hw : 0 ≤ w) (hr : 0 ≤ r)
    (inside : k*w ≤ wt) (outside : rt ≤ k*r) : w*rt ≤ wt*r := by
  calc
    w*rt ≤ w*(k*r) := mul_le_mul_of_nonneg_left outside hw
    _ = (k*w)*r := by ring
    _ ≤ wt*r := mul_le_mul_of_nonneg_right inside hr

end YangMills.VacuumBand
#print axioms YangMills.VacuumBand.centeredTail
#print axioms YangMills.VacuumBand.perpendicularSquare
#print axioms YangMills.VacuumBand.projectedDirection
#print axioms YangMills.VacuumBand.polynomialDegree
#print axioms YangMills.VacuumBand.bandShareAtLag
