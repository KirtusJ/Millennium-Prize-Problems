import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Millennium.G4.Refinement

set_option linter.unusedVariables false

theorem matched_loop (s p n : ℝ) (hn : n ≠ 0) :
    n * (p * n) * (s / n^2) = p*s := by
  field_simp
  ring

theorem elementary_loop (s n : ℝ) (hn : n ≠ 0) :
    n * 4 * (s / n^2) = 4*s/n := by
  field_simp
  ring

open Filter Topology in
theorem elementary_limit (s : ℝ) :
    Tendsto (fun n : ℕ => 4*s/(n : ℝ)) atTop (𝓝 0) := by
  simpa using tendsto_const_div_atTop_nhds_zero_nat (4*s)

-- NATIVE CHILD 1
theorem subdivision_energy (s p n b : ℝ) (hb : b ≠ 0) :
    s * (b*p) / (b*n) = s*p/n := by
  by_cases hn : n = 0
  · simp [hn]
  · field_simp
    ring

theorem electric_correlation (s p n k : ℝ) (hn : n ≠ 0) :
    Real.exp (-(n*k)*(p*n)*(s/n^2)) = Real.exp (-(p*s)*k) := by
  congr 1
  field_simp
  ring

theorem split_minorization (eps x y D : ℝ) (he : eps ≤ 1) (hd : x-y ≤ D) :
    (1-eps)*x - (1-eps)*y ≤ (1-eps)*D := by
  simpa only [mul_sub] using mul_le_mul_of_nonneg_left hd (sub_nonneg.mpr he)

-- NATIVE CHILD 2
theorem fine_shell_form (a b eta q x y : ℝ)
    (hx : 0 ≤ x) (hy : 0 ≤ y) (heta : 0 ≤ eta)
    (ha : a + eta ≤ q) (hb : b + eta ≤ q) :
    a * x^2 + 2 * eta * x * y + b * y^2 ≤ q * (x^2 + y^2) := by
  have hxa : 0 ≤ (q - (a + eta)) * x^2 :=
    mul_nonneg (sub_nonneg.mpr ha) (sq_nonneg x)
  have hyb : 0 ≤ (q - (b + eta)) * y^2 :=
    mul_nonneg (sub_nonneg.mpr hb) (sq_nonneg y)
  have hxy : 0 ≤ eta * (x - y)^2 :=
    mul_nonneg heta (sq_nonneg (x - y))
  apply sub_nonneg.mp
  calc
    0 ≤ (q - (a + eta)) * x^2 + (q - (b + eta)) * y^2 +
        eta * (x - y)^2 := add_nonneg (add_nonneg hxa hyb) hxy
    _ = q * (x^2 + y^2) - (a * x^2 + 2 * eta * x * y + b * y^2) := by
      ring

theorem fine_shell_sharp (a b eta q x y : ℝ) (hu : 0 < q-a)
    (hdet : eta^2 ≤ (q-a)*(q-b)) :
    a*x^2+2*eta*x*y+b*y^2 ≤ q*(x^2+y^2) := by
  have square := sq_nonneg ((q-a)*x-eta*y)
  have rest := mul_nonneg (sub_nonneg.mpr hdet) (sq_nonneg y)
  have h : 0 ≤ (q-a)*(q*(x^2+y^2)-(a*x^2+2*eta*x*y+b*y^2)) := by
    nlinarith only [square, rest]
  exact sub_nonneg.mp (nonneg_of_mul_nonneg_right h hu)

#print axioms matched_loop
#print axioms elementary_loop
#print axioms elementary_limit
#print axioms subdivision_energy
#print axioms electric_correlation
#print axioms split_minorization
#print axioms fine_shell_form
#print axioms fine_shell_sharp

end Millennium.G4.Refinement
