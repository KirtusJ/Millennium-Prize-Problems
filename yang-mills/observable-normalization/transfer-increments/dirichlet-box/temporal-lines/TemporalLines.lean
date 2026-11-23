import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

open Finset
namespace YangMills.TemporalLines

/-- Subtracting the minimizing ramp leaves its constant temporal flux
orthogonal to every variation with equal endpoint values. -/
theorem rampEnergy {ι : Type*} (s : Finset ι) (r : ι → ℝ) (b : ℝ)
    (hr : ∑ i ∈ s, r i = 0) :
    ∑ i ∈ s, (r i - b)^2 = (∑ i ∈ s, (r i)^2) + s.card*b^2 := by
  simp_rw [sub_sq]
  simp only [sum_add_distrib, sum_sub_distrib, ← sum_mul, ← mul_sum,
    hr, mul_zero, zero_mul, sub_zero, sum_const, nsmul_eq_mul]

/-- The shell mean cancels even when it is random. -/
theorem meanCancel (m x y : ℝ) : (m+x)-(m+y)=x-y := by ring

/-- A uniform diagonal evaluation bound and the Dirichlet energy bound
give a fourth-power budget for all zero-shell free links. -/
theorem fourthBudget {ι : Type*} (s : Finset ι) (v : ι → ℝ) (B E : ℝ)
    (hB : 0 ≤ B) (h : ∀ i ∈ s, (v i)^2 ≤ B)
    (he : ∑ i ∈ s, (v i)^2 ≤ E) :
    ∑ i ∈ s, (v i)^4 ≤ B*E := by
  calc
    _ ≤ ∑ i ∈ s, B*(v i)^2 := by
      apply sum_le_sum
      intro i hi
      calc
        _ = (v i)^2 * (v i)^2 := by ring
        _ ≤ _ := mul_le_mul_of_nonneg_right (h i hi) (sq_nonneg _)
    _ ≤ _ := by rw [← mul_sum]; exact mul_le_mul_of_nonneg_left he hB

/-- The quadratic action error has one mixed and one squared remainder. -/
theorem quadraticError (a b d e : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hd : |a-b| ≤ e) (hs : a+b ≤ 2*d+e) :
    |a^2-b^2| ≤ e*(2*d+e) := by
  have he := (abs_nonneg (a-b)).trans hd
  rw [show a^2-b^2=(a-b)*(a+b) by ring, abs_mul, abs_of_nonneg (add_nonneg ha hb)]
  exact mul_le_mul hd hs (add_nonneg ha hb) he

/-- Comparison with the reversed product cancels all normalizers. -/
theorem exchangedRatio (a b c d m n : ℝ) (ha : a ≠ 0) (hd : d ≠ 0)
    (hm : m ≠ 0) (hn : n ≠ 0) :
    ((b/m)*(c/n))/((a/m)*(d/n)) = (b*c)/(a*d) := by
  field_simp

/-- Coupling the two conditional replicas loses at most twice the
one-copy probability of disagreement. -/
theorem twoCopies (p : ℝ) : 1-(1-p)^2 ≤ 2*p := by nlinarith [sq_nonneg p]

end YangMills.TemporalLines
#print axioms YangMills.TemporalLines.rampEnergy
#print axioms YangMills.TemporalLines.meanCancel
#print axioms YangMills.TemporalLines.fourthBudget
#print axioms YangMills.TemporalLines.quadraticError
#print axioms YangMills.TemporalLines.exchangedRatio
#print axioms YangMills.TemporalLines.twoCopies
