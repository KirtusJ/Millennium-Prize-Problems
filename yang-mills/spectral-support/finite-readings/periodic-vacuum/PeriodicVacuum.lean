import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Data.Real.Basic
namespace PeriodicVacuum
theorem corners : (8 : ℕ) = 8 := by decide
theorem components (x y z : ℝ) : 3*(x-y)^2+(x+y-2*z)^2 = 2*((x-y)^2+(y-z)^2+(z-x)^2) := by ring
theorem pair_rows (p s a h k : ℝ) (hp : 0 ≤ p) (ha : 0 ≤ a) (hk : k ≤ (1+s)*h) : p*a*k ≤ (p+p*s)*a*h := by
  calc
    p*a*k ≤ p*a*((1+s)*h) := mul_le_mul_of_nonneg_left hk (mul_nonneg hp ha)
    _ = (p+p*s)*a*h := by ring
theorem occupation (u v : ℝ) (hu : 0 ≤ u) (hv : u ≤ v) : u/(1+u) ≤ v/(1+v) := by
  apply (div_le_div_iff₀ (by linarith : 0 < 1+u) (by linarith : 0 < 1+v)).2
  nlinarith
#print axioms corners
#print axioms components
#print axioms pair_rows
#print axioms occupation
end PeriodicVacuum
