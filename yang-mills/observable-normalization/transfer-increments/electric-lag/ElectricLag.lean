import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace YangMills.ElectricLag

/-- The square characters have fourth moment four; distinct doubled
faces give three pairings. -/
theorem fourthCount (N : ℝ) : 4*N+3*N*(N-1)=3*N^2+N := by ring
theorem fourthNormalized (N : ℝ) (h : N ≠ 0) :
    (3*N^2+N)/N^2=3+1/N := by field_simp; ring

/-- The likelihood comparison for two distinct normal shifts
changes sign at their midpoint. -/
theorem logDifference (a b s : ℝ) :
    (a*s-a^2/2)-(b*s-b^2/2)=(a-b)*(s-(a+b)/2) := by ring
theorem midpointTest (a b s : ℝ) (hab : b<a) :
    b*s-b^2/2 < a*s-a^2/2 ↔ (a+b)/2 < s := by
  rw [← sub_pos, logDifference]
  exact (mul_pos_iff_of_pos_left (sub_pos.mpr hab)).trans sub_pos

/-- Tilting the standard normal changes the mean while keeping the
quadratic part of its density the same. -/
theorem gaussianTilt (s h : ℝ) : -s^2/2+h*s-h^2/2=-(s-h)^2/2 := by ring
theorem informationMean (h : ℝ) : h*h-h^2/2=h^2/2 := by ring

end YangMills.ElectricLag
#print axioms YangMills.ElectricLag.fourthCount
#print axioms YangMills.ElectricLag.fourthNormalized
#print axioms YangMills.ElectricLag.logDifference
#print axioms YangMills.ElectricLag.midpointTest
#print axioms YangMills.ElectricLag.gaussianTilt
#print axioms YangMills.ElectricLag.informationMean
