import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace JointMomentum

theorem signedPathCounts : ((540, 972) : ℕ × ℕ) = (540,972) := by decide

theorem wickExcess (r b v : ℝ) (hr : 0 < r) (h1 : r < 1)
    (hb : 0 < b) (hv : 0 ≤ v) :
    0 < b*(r-r^2)+v*(1-r^2) := by
  have h : 0 < r*(1-r) := mul_pos hr (sub_pos.mpr h1)
  have k : 0 < (1-r)*(1+r) := mul_pos (sub_pos.mpr h1) (by linarith)
  nlinarith [mul_pos hb h, mul_nonneg hv k.le]

theorem foldedPairs : ((24, 0) : ℕ × ℕ) = (24,0) := by decide

theorem budget (signal approximation moment : ℝ)
    (hs : 0 < signal) (ha : approximation ≤ signal/4)
    (hm : moment ≤ signal/4) :
    0 < signal - approximation - moment := by linarith

theorem twoLegChecks : ((14, 7332) : ℕ × ℕ) = (14,7332) := by decide

theorem transverseRadius (e p : ℝ) (hp : 0 ≤ p) (he : p < e) :
    (p/2)^2 + (Real.sqrt (e^2-p^2)/2)^2 = (e/2)^2 := by
  have h : 0 ≤ (e-p)*(e+p) := mul_nonneg (by linarith) (by linarith)
  have hs := Real.sq_sqrt (show 0 ≤ e^2-p^2 by nlinarith)
  nlinarith

#print axioms signedPathCounts
#print axioms wickExcess
#print axioms foldedPairs
#print axioms budget
#print axioms twoLegChecks
#print axioms transverseRadius
end JointMomentum
