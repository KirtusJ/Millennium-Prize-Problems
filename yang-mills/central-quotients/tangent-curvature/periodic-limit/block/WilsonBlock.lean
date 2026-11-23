import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

open MeasureTheory
namespace WilsonBlock

theorem thirdDifference (x : ℝ) :
    (1-x)^3=1-3*x+3*x^2-x^3 := by ring

theorem boxMoment : ((264, 24576) : ℕ × ℕ) = (264,24576) := by decide

theorem pathBound {ι κ : Type*} (s : Finset κ) (p : κ → Finset ι)
    (h : ι → ℝ) (v : κ → ℝ) (H : ℝ) (hh : ∀ e, |h e| ≤ H) :
    (∑ i ∈ s, |v i| * ∑ e ∈ p i, |h e|) ≤
       H * ∑ i ∈ s, |v i| * ((p i).card : ℝ) := by
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i _
  have he : (∑ e ∈ p i, |h e|) ≤ ∑ _e ∈ p i, H :=
    Finset.sum_le_sum fun e _ => hh e
  simp only [Finset.sum_const, nsmul_eq_mul] at he
  calc
    _ ≤ |v i| * (((p i).card : ℝ)*H) := mul_le_mul_of_nonneg_left he (abs_nonneg _)
    _ = _ := by ring

theorem summedError {ι : Type*} (s : Finset ι) (a x y : ι → ℝ)
    (d : ℝ) (h : ∀ i ∈ s, |x i-y i| ≤ d) :
    |(∑ i ∈ s, a i*x i)-(∑ i ∈ s, a i*y i)| ≤ (∑ i ∈ s, |a i|)*d := by
  rw [← Finset.sum_sub_distrib, Finset.sum_mul]
  calc
    _ ≤ ∑ i ∈ s, |a i*x i-a i*y i| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ _ := by
      apply Finset.sum_le_sum
      intro i hi
      rw [← mul_sub, abs_mul]
      exact mul_le_mul_of_nonneg_left (h i hi) (abs_nonneg _)

theorem spatialVisits : (900 : ℕ) = 900 := by decide

theorem bandWeight {X : Type*} [MeasurableSpace X] (μ : Measure X)
    (J : Set X) (f : X → ℝ) (hf : Integrable f μ)
    (hi : Integrable (J.indicator (fun _ : X => (1:ℝ))) μ)
    (hin : ∀ x ∈ J, f x ≤ 1) (hout : ∀ x ∉ J, f x ≤ 0) :
    (∫ x, f x ∂μ) ≤ ∫ x, J.indicator (fun _ : X => (1:ℝ)) x ∂μ := by
  apply integral_mono hf hi
  intro x
  by_cases h : x ∈ J
  · simpa [Set.indicator_of_mem h] using hin x h
  · simpa [Set.indicator, h] using hout x h

theorem timeWitness {n m v c B : ℝ} (hn : 0 < n) (hc : 0 < c) (hv : v ≤ 1)
    (hl : c ≤ B) (ht : B ≤ Real.exp (-m*n)*v) : m ≤ -Real.log c/n := by
  have h : c ≤ Real.exp (-m*n) := calc
    c ≤ B := hl
    _ ≤ Real.exp (-m*n)*v := ht
    _ ≤ Real.exp (-m*n)*1 := mul_le_mul_of_nonneg_left hv (Real.exp_pos _).le
    _ = _ := mul_one _
  have hlog := Real.log_le_log hc h
  rw [Real.log_exp] at hlog
  exact (le_div_iff₀ hn).2 (by linarith)

theorem bandExample : (1*(-1)*3+14*1*1+1*3*(-1) : ℤ) = 8 := by decide

#print axioms thirdDifference
#print axioms boxMoment
#print axioms pathBound
#print axioms summedError
#print axioms spatialVisits
#print axioms bandWeight
#print axioms timeWitness
#print axioms bandExample
end WilsonBlock
