import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
namespace YangMills.BlockVariance

noncomputable def pureStep (x : ℝ) := (1-x)/3

/-- Three orthogonal pure directions acting on a unit quaternion. -/
theorem oneAxisAverage {a b c d : ℝ} (unit : a^2+b^2+c^2+d^2=1) :
    ((-b)^2+(-c)^2+(-d)^2)/3 = pureStep (a^2) := by
  unfold pureStep
  linarith only [unit]

theorem twoAxes (x : ℝ) : pureStep (pureStep x) = (2+x)/9 := by
  unfold pureStep
  ring

theorem traceSquareFloor (a : ℝ) :
    8/9 ≤ 4 * pureStep (pureStep (a^2)) := by
  rw [twoAxes]
  linarith only [sq_nonneg a]

/-- Two independent evaluations along a fair sign yield the Walsh energy identity. -/
theorem splitSign (plus minus : ℝ) :
    (plus^2+minus^2)/2 = ((plus+minus)/2)^2+((plus-minus)/2)^2 := by ring

/-- Assemble a conditional bound from an independent color carrying a fraction of the weights. -/
theorem assemble {total block cond variance c : ℝ}
    (color : total ≤ 11*block) (cost : 0 ≤ c)
    (localBound : c*block ≤ cond) (varianceBound : cond ≤ variance) :
    (c/11)*total ≤ variance := by
  have h := mul_le_mul_of_nonneg_left color cost
  linarith only [h,localBound,varianceBound]

/-- Cost of a shift on the good-score event after scaling the angular step. -/
theorem localCost {b u : ℝ} (h₁ : b*u ≤ 1/4) (h₂ : b^2*u^2 ≤ 1/16) :
    12*b*u + 12*b^2*u^2 ≤ 15/4 := by
  linarith only [h₁,h₂]

end YangMills.BlockVariance
#print axioms YangMills.BlockVariance.oneAxisAverage
#print axioms YangMills.BlockVariance.twoAxes
#print axioms YangMills.BlockVariance.traceSquareFloor
#print axioms YangMills.BlockVariance.splitSign
#print axioms YangMills.BlockVariance.assemble
#print axioms YangMills.BlockVariance.localCost
