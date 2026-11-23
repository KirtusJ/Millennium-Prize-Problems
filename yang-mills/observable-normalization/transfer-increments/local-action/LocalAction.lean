import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

open Finset
namespace YangMills.LocalAction

/-- Site reflection in the midpoint exchanges the two positively oriented
face bases within a pair, with their order reversed. -/
theorem pairReflection (j k : ℤ) :
    2*(j+k+1)-(2*j)-1 = 2*k+1 ∧
    2*(j+k+1)-(2*j+1)-1 = 2*k := by
  constructor <;> ring

/-- Nonpositive mean inner products between different blocks leave only
diagonal contributions to the upper bound for their sum. -/
theorem blockSum {ι : Type*} [DecidableEq ι] (s : Finset ι)
    (K : ι → ι → ℝ) (D : ℝ) (diag : ∀ i ∈ s, K i i ≤ D)
    (off : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → K i j ≤ 0) :
    (∑ i ∈ s, ∑ j ∈ s, K i j) ≤ (s.card:ℝ)*D := by
  calc
    _ ≤ ∑ i ∈ s, ∑ j ∈ s, (if j=i then D else 0) := by
      apply sum_le_sum
      intro i hi
      apply sum_le_sum
      intro j hj
      by_cases eq : j=i
      · subst j
        simpa using diag i hi
      · simpa [eq] using off i hi j hj (Ne.symm eq)
    _ = _ := by simp

/-- Quaternion magnitude converts the scaled imaginary curvature back to
the Wilson action with one explicit quadratic remainder. -/
theorem actionRemainder (b x y f : ℝ) (h : y=b*(1-x))
    (hf : f=b*(1-x^2)) : b*(2*y-f)=y^2 := by
  rw [h,hf]
  ring

/-- Connected covariance of two sums of three squared Gaussian colors,
including the normalization of each scalar action by one half. -/
theorem wickAction (v g : ℝ) :
    (3*(v^2+2*g^2)+6*v^2)/4 - (3*v/2)^2 = 3*g^2/2 := by ring

/-- Combining a reflected-mean error with a cubic primitive cost after
writing s for the eighth root of the coupling. -/
theorem balance (s : ℝ) (hs : 0 < s) :
    1/s + s^3/s^4 = 2/s := by
  field_simp
  ring

/-- Fixed positive-time tilt converts centered covariance readings into
normalized moments, with a denominator bounded away from zero. -/
theorem tiltError (A B C D e f : ℝ) (hB : 0 < B) (hD : 0 < D)
    (hC : |C| ≤ D) (hA : |A-C| ≤ e) (hBD : |B-D| ≤ f) :
    |A/B-C/D| ≤ (e+f)/B := by
  have eq : A/B-C/D = ((A-C) + (C/D)*(D-B))/B := by
    field_simp
    ring
  have hc' : |C/D| ≤ 1 := by
    rw [abs_div, abs_of_pos hD, div_le_one hD]
    exact hC
  rw [eq, abs_div, abs_of_pos hB]
  apply div_le_div_of_nonneg_right _ hB.le
  calc
    _ ≤ |A-C| + |(C/D)*(D-B)| := abs_add_le _ _
    _ ≤ e + f := by
      rw [abs_mul, abs_sub_comm D B]
      exact add_le_add hA ((mul_le_mul_of_nonneg_right hc' (abs_nonneg _)).trans (by simpa using hBD))

end YangMills.LocalAction
#print axioms YangMills.LocalAction.pairReflection
#print axioms YangMills.LocalAction.blockSum
#print axioms YangMills.LocalAction.actionRemainder
#print axioms YangMills.LocalAction.wickAction
#print axioms YangMills.LocalAction.balance
#print axioms YangMills.LocalAction.tiltError
