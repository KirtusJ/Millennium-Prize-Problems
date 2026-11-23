import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Algebra.BigOperators.Ring.Finset

namespace YangMills.SquareBends

/-- Each corner face uses two of the four incident face slots per edge. -/
theorem incidence (k : ℝ) : (4*k-8)+2*4=4*k := by ring
theorem residualNorm : (1 : ℝ) - (1/2)^2 = 3/4 := by norm_num

/-- Differentiating a power remains regular at coincident eigenvalues. -/
theorem finiteSum (u r : ℝ) (n : ℕ) :
    (u-r)*(∑ j ∈ Finset.range n, u^j*r^(n-1-j)) = u^n-r^n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ]
    have aux : (∑ j ∈ Finset.range n, u^j*r^(n+1-1-j)) =
        (∑ j ∈ Finset.range n, u^j*r^(n-1-j))*r := by
      rw [Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro j hj
      have h := Finset.mem_range.mp hj
      have e : n+1-1-j = (n-1-j)+1 := by omega
      rw [e, pow_succ]
      ring
    rw [aux]
    simp only [Nat.add_sub_cancel, Nat.sub_self, pow_zero, mul_one, pow_succ]
    linear_combination r * ih

theorem singletSlope (d : ℝ) : (4-(4-2*d))/4/4=d/8 := by ring
theorem tripletSlope (d : ℝ) : (4-(4+2*d/3))/4/4= -d/24 := by ring

/-- Weighted Cauchy remainder for a singlet and triplet pair. -/
theorem weightedRemainder (a b x y s t : ℝ) :
    (t*a^2+s*b^2)*(s*x^2+t*y^2)-s*t*(a*x+b*y)^2 =
    (t*a*y-s*b*x)^2 := by ring

end YangMills.SquareBends
#print axioms YangMills.SquareBends.incidence
#print axioms YangMills.SquareBends.residualNorm
#print axioms YangMills.SquareBends.finiteSum
#print axioms YangMills.SquareBends.singletSlope
#print axioms YangMills.SquareBends.tripletSlope
#print axioms YangMills.SquareBends.weightedRemainder
