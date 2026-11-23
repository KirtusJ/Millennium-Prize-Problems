import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Algebra.BigOperators.Ring.Finset

namespace YangMills.CoarseResponse

/-- A face can erase at most two occupied edges and contributes four
minus the number of mesh edges as private fundamental links. -/
theorem supportCount (E occupied mesh : ℤ) (ha : occupied ≤ mesh)
    (hm : mesh ≤ 2) : E ≤ E-occupied+(4-mesh) := by omega

/-- Difference of endpoint powers plus the remaining geometric sum,
without division by a spectral difference. -/
theorem telescopes (r t : ℝ) (n : ℕ) :
    (t-r)*(∑ j ∈ Finset.range n, t^j*r^(n-1-j))=t^n-r^n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ]
    have aux : (∑ j ∈ Finset.range n, t^j*r^(n+1-1-j)) =
        (∑ j ∈ Finset.range n, t^j*r^(n-1-j))*r := by
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

theorem derivativeSplit (t r l h : ℝ) :
    (t-l*r)*h=(t-r)*h+(1-l)*r*h := by ring

theorem endpoints (T R Q : ℝ) (ht : 0 ≤ T) (hr : 0 ≤ R)
    (hT : T ≤ Q) (hR : R ≤ Q) : |T-R| ≤ Q := by
  rw [abs_le]; constructor <;> linarith

theorem squaredNorm (N u : ℝ) : (2*u)^2*N=4*N*u^2 := by ring

end YangMills.CoarseResponse
#print axioms YangMills.CoarseResponse.supportCount
#print axioms YangMills.CoarseResponse.telescopes
#print axioms YangMills.CoarseResponse.derivativeSplit
#print axioms YangMills.CoarseResponse.endpoints
#print axioms YangMills.CoarseResponse.squaredNorm
