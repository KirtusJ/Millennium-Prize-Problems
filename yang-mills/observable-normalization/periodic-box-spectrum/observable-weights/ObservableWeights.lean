import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace YangMills.ObservableWeights

/-- Squared curl in the two selected spatial directions kills longitudinal modes. -/
theorem curlLongitudinal (a b t : ℝ) : a*(b*t)-b*(a*t)=0 := by ring

/-- Coefficient for the covariance of a half-squared three-color Gaussian. -/
theorem wickColor (v c : ℝ) :
    (3*(v^2+2*c^2)+6*v^2)/4-(3*v/2)^2=3*c^2/2 := by ring

theorem pairAtom (u v : ℝ) :
    3*(u+v)^2/2=3*u^2/2+3*u*v+3*v^2/2 := by ring

theorem thresholdCoefficient (p : ℝ) : 3*(4*p)^2/2=24*p^2 := by ring

theorem variancePositive (v : ℝ) (h : 0 < v) : 0 < 3*v^2/2 := by
  nlinarith only [mul_pos h h]

/-- A slow leakage estimate from a transfer moment near unit eigenvalue. -/
theorem massFromMoment (mass moment threshold : ℝ) (ht : 0 < threshold)
    (h : threshold*mass ≤ moment) : mass ≤ moment/threshold := by
  apply (le_div_iff₀ ht).mpr
  simpa [mul_comm] using h

/-- A single strictly positive spectral weight gives a positive transformed sum. -/
theorem survivingWeight (weight factor rest : ℝ) (hw : 0 < weight)
    (hf : 0 < factor) (hr : 0 ≤ rest) : 0 < weight*factor+rest :=
  add_pos_of_pos_of_nonneg (mul_pos hw hf) hr

end YangMills.ObservableWeights
#print axioms YangMills.ObservableWeights.curlLongitudinal
#print axioms YangMills.ObservableWeights.wickColor
#print axioms YangMills.ObservableWeights.pairAtom
#print axioms YangMills.ObservableWeights.thresholdCoefficient
#print axioms YangMills.ObservableWeights.variancePositive
#print axioms YangMills.ObservableWeights.massFromMoment
#print axioms YangMills.ObservableWeights.survivingWeight
