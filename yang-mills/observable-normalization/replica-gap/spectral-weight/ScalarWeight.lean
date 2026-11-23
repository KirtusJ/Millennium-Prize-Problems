import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Tactic.Linarith

open scoped BigOperators
namespace YangMills.ScalarWeight

/-- Subtract the motion of the eigenvector from the motion of the probe. -/
theorem derivativeLeak {ι : Type*} [Fintype ι] (u f : ι → ℝ) (c : ℝ) :
    (∑ i, (c*u i/2 - f i*u i/2)^2) = ∑ i, ((c-f i)/2)^2*(u i)^2 := by
  apply Finset.sum_congr rfl
  intro i _
  ring

theorem disconnectedCancellation {r : ℝ} (hr : r ≠ 0) (h1 : r ≠ 1) :
    (r+r^2)/(r-r^2) = (1+r)/(1-r) := by
  have h : r-r^2 ≠ 0 := by
    rw [show r-r^2=r*(1-r) by ring]
    exact mul_ne_zero hr (sub_ne_zero.mpr (Ne.symm h1))
  have h₂ : 1-r ≠ 0 := sub_ne_zero.mpr (Ne.symm h1)
  field_simp
  ring

theorem effectiveExcess {ι : Type*} [Fintype ι] (w x : ι → ℝ) (n : ℕ) :
    (∑ i, w i*(1-(x i)^(n+1))) - (∑ i, w i*(1-(x i)^n)) =
      ∑ i, w i*(1-x i)*(x i)^n := by
  rw [← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro i _
  rw [pow_succ]
  ring

theorem excessPositive {ι : Type*} [Fintype ι] (w x : ι → ℝ) (n : ℕ)
    (hw : ∀ i, 0 ≤ w i) (hx : ∀ i, 0 ≤ x i) (ht : ∀ i, x i ≤ 1) :
    0 ≤ ∑ i, w i*(1-x i)*(x i)^n :=
  Finset.sum_nonneg fun i _ => mul_nonneg (mul_nonneg (hw i) (sub_nonneg.mpr (ht i)))
    (pow_nonneg (hx i) n)

theorem hamiltonianWeight :
    (1/4:ℝ)*(1/6-1/(16-6))^2 + (12/8)*(1/6-1/(9-6))^2 +
      (36/8)*(1/6-1/(13-6))^2 = 1999/44100 := by norm_num

theorem hamiltonianGap :
    ((2*(1/3)-(1/5)-24*((8/21)-(1/3)))/8 : ℝ) = -71/840 := by norm_num

theorem hamiltonianDispersion : (((8/21)-(1/3))/6 : ℝ) = 1/126 := by norm_num

end YangMills.ScalarWeight
#print axioms YangMills.ScalarWeight.derivativeLeak
#print axioms YangMills.ScalarWeight.disconnectedCancellation
#print axioms YangMills.ScalarWeight.effectiveExcess
#print axioms YangMills.ScalarWeight.excessPositive
#print axioms YangMills.ScalarWeight.hamiltonianWeight
#print axioms YangMills.ScalarWeight.hamiltonianGap
#print axioms YangMills.ScalarWeight.hamiltonianDispersion
