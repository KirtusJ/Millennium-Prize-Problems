import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

namespace YangMills.PlaquetteWindow

theorem longitudinalCap {h : ℝ} (ha : 0 ≤ h) (hb : h ≤ 762727/1000000) :
    7376/200000 ≤ 1-h^2-h/2 := by
  nlinarith [mul_nonneg (sub_nonneg.mpr hb) (show 0 ≤ 762727/1000000+h by linarith)]

theorem inverseBudget : (16:ℝ)*(14/(8/25))^4 < 2^26 := by norm_num

theorem weightWindow {a w : ℝ} (ha : a ≤ 1/256)
    (hd : 7376/200000 ≤ a+w+(1-a-w)/39) : 3/400 ≤ w := by linarith

theorem endpointCut : ((1-1/39)/(1+1/39) : ℝ) = 19/20 := by norm_num
end YangMills.PlaquetteWindow
#print axioms YangMills.PlaquetteWindow.longitudinalCap
#print axioms YangMills.PlaquetteWindow.inverseBudget
#print axioms YangMills.PlaquetteWindow.weightWindow
#print axioms YangMills.PlaquetteWindow.endpointCut
