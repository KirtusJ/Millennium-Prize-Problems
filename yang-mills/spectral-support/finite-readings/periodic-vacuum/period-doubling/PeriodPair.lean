import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace YangMills.PeriodPair

theorem doubledRow (w z : ℝ) : w^2*z=w*(w*z) := by ring

theorem weightedBudget (w h k b : ℝ) (hw : 0 ≤ w) (hc : k ≤ h*b) :
    w*k ≤ h*(w*b) := by
  nlinarith only [mul_nonneg hw (sub_nonneg.mpr hc)]

theorem comparePowers (x y : ℝ) (hx : 0 ≤ x) (hxy : x ≤ y) (l n : ℕ)
    (h : n ≤ l) :
    x^l*y^n ≤ y^l*x^n := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le h
  rw [pow_add, pow_add]
  have hk := pow_le_pow_left₀ hx hxy k
  nlinarith only [mul_nonneg (mul_nonneg (pow_nonneg hx n)
    (pow_nonneg (hx.trans hxy) n)) (sub_nonneg.mpr hk)]

theorem massFloor (h m w tax : ℝ) (bound : w ≤ h*m+tax) :
    w-tax ≤ h*m := by linarith

end YangMills.PeriodPair
#print axioms YangMills.PeriodPair.doubledRow
#print axioms YangMills.PeriodPair.weightedBudget
#print axioms YangMills.PeriodPair.comparePowers
#print axioms YangMills.PeriodPair.massFloor
