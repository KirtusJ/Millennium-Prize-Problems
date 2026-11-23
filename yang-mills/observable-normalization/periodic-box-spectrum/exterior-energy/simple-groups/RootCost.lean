import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
namespace YangMills.RootCost

theorem remainder (a b e : ℝ) (he : 0 < e) :
    e*(a+b)^2 ≥ e*(1-e)*a^2 - b^2 := by
  nlinarith only [sq_nonneg (e*a+b), mul_nonneg (le_of_lt he) (sq_nonneg b)]

theorem shift (a b t : ℝ) : a*t+b = a*(t+b/a) ∨ a=0 := by
  by_cases h : a=0
  · exact Or.inr h
  · left
    field_simp
    ring

theorem transverse (x y z a b c : ℝ) :
    (x*b-y*a)^2+(x*c-z*a)^2+(y*c-z*b)^2 =
      (x^2+y^2+z^2)*(a^2+b^2+c^2)-(x*a+y*b+z*c)^2 := by ring

theorem chamber (p q m x y : ℝ) (hp : 0 ≤ p) (hq : 0 ≤ q)
    (hx : m ≤ x) (hy : m ≤ y) : m*(p+q) ≤ p*x+q*y := by
  nlinarith only [mul_nonneg hp (sub_nonneg.mpr hx),mul_nonneg hq (sub_nonneg.mpr hy)]

theorem cluster (n k : ℝ) (hk : 1 ≤ k) (hn : k ≤ n-1) :
    n-1 ≤ k*(n-k) := by
  nlinarith only [mul_nonneg (sub_nonneg.mpr hk) (sub_nonneg.mpr hn)]

end YangMills.RootCost
#print axioms YangMills.RootCost.remainder
#print axioms YangMills.RootCost.shift
#print axioms YangMills.RootCost.transverse
#print axioms YangMills.RootCost.chamber
#print axioms YangMills.RootCost.cluster
