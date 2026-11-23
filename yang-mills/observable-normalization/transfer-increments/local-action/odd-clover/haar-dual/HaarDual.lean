import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

open Finset
namespace YangMills.HaarDual

/-- The common site coefficient from three colors and 48 oriented pairs. -/
theorem haarContact : (48:ℝ) * ((1/16)^2 * (3*(1/4)^2)) = 9/256 := by norm_num

/-- A positive conditional density can be canceled in the dual
pairing, for every value of the conditioned exterior field. -/
theorem cancelWeight (f g ρ : ℝ) (h : 0 < ρ) :
    (f*(g/ρ))*ρ = f*g := by
  rw [mul_assoc, div_mul_cancel₀ _ (ne_of_gt h)]

/-- Pairing against a covariance kernel supported on the diagonal. -/
theorem diagonalPair {ι : Type*} [DecidableEq ι] (s : Finset ι) (f : ι → ℝ) (v : ℝ) :
    (∑ i ∈ s, ∑ j ∈ s, f i * (if i=j then v else 0) * f j)
      = v * ∑ i ∈ s, (f i)^2 := by
  classical
  rw [mul_sum]
  apply sum_congr rfl
  intro i hi
  rw [sum_eq_single i]
  · simp; ring
  · intro j _ hji
    simp [Ne.symm hji]
  · simp [hi]
/-- Symmetric finite-range cross terms are bounded by the squared
coefficient budget of their two endpoints. -/
theorem edgePair (x y : ℝ) : 2 * |x*y| ≤ x^2 + y^2 := by
  rw [abs_mul]
  nlinarith [sq_nonneg (|x|-|y|), sq_abs x, sq_abs y]

/-- The Gram bound on the local dual and its exact mixed overlap
give a variance floor for every real smearing. -/
theorem dualFloor (v n gram variance upper : ℝ)
    (hn : 0 < n) (hu : 0 < upper) (hv : 0 ≤ variance)
    (bound : gram ≤ upper*n) (cs : (v*n)^2 ≤ variance*gram) :
    v^2/upper*n ≤ variance := by
  have h : (v^2*n)*n ≤ (variance*upper)*n := by
    calc
      _ = (v*n)^2 := by ring
      _ ≤ variance*gram := cs
      _ ≤ variance*(upper*n) := mul_le_mul_of_nonneg_left bound hv
      _ = _ := by ring
  have h' := (le_of_mul_le_mul_right h hn)
  rwa [div_mul_eq_mul_div, div_le_iff₀ hu]
/-- A first-order error in the dual norm costs at most the same
first-order error in the optimal lower variance bound. -/
theorem smallCouplingFloor (v e : ℝ) (hv : 0 < v) (he : 0 ≤ e) :
    v-e ≤ v^2/(v+e) := by
  apply (le_div_iff₀ (add_pos_of_pos_of_nonneg hv he)).2
  nlinarith [sq_nonneg e]

/-- The error of a local weighted witness remains controlled after
summing over all possible roots, with a constant independent of the support. -/
theorem neighborhoodBudget {ι κ : Type*} (roots : Finset ι) (patch : Finset κ)
    (a : ι → κ → ℝ) (n : ℝ) (column : ∀ b ∈ patch, ∑ x ∈ roots, (a x b)^2 ≤ n) :
    (∑ x ∈ roots, (∑ b ∈ patch, a x b)^2) ≤ (patch.card:ℝ)^2 * n := by
  calc
    _ ≤ ∑ x ∈ roots, (patch.card:ℝ) * ∑ b ∈ patch, (a x b)^2 := by
      apply sum_le_sum
      intro x _
      simpa using sum_mul_sq_le_sq_mul_sq patch (fun _ ↦ (1:ℝ)) (a x)
    _ = (patch.card:ℝ) * ∑ b ∈ patch, ∑ x ∈ roots, (a x b)^2 := by
      rw [← mul_sum, sum_comm]
    _ ≤ (patch.card:ℝ) * ∑ _b ∈ patch, n := by
      exact mul_le_mul_of_nonneg_left (sum_le_sum column) (Nat.cast_nonneg _)
    _ = _ := by simp [nsmul_eq_mul]; ring

theorem mixedRemainder (a b : ℝ) : a^2/2-b^2 ≤ (a+b)^2 := by
  nlinarith [sq_nonneg (a+2*b)]

end YangMills.HaarDual
#print axioms YangMills.HaarDual.haarContact
#print axioms YangMills.HaarDual.cancelWeight
#print axioms YangMills.HaarDual.diagonalPair
#print axioms YangMills.HaarDual.edgePair
#print axioms YangMills.HaarDual.dualFloor
#print axioms YangMills.HaarDual.smallCouplingFloor
#print axioms YangMills.HaarDual.neighborhoodBudget
#print axioms YangMills.HaarDual.mixedRemainder
