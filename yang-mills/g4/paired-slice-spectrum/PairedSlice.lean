import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

open MeasureTheory
open scoped BigOperators

namespace Millennium.G4.PairedSlice

/-- The upper secant of the square, integrated over one conditional cell. -/
theorem cell_second_moment {X : Type*} [MeasurableSpace X]
    (μ : Measure X) [IsProbabilityMeasure μ] (f : X → ℝ) (m M : ℝ)
    (hf : Integrable f μ) (h₂ : Integrable (fun x => f x ^ 2) μ)
    (range : ∀ x, m ≤ f x ∧ f x ≤ M) :
    (∫ x, f x ^ 2 ∂μ) ≤ (m+M)*(∫ x, f x ∂μ) - m*M := by
  have h := integral_mono h₂ ((hf.const_mul (m+M)).sub (integrable_const (m*M)))
    (fun x => show f x ^ 2 ≤ (m+M)*f x-m*M by
      nlinarith [mul_nonneg (sub_nonneg.mpr (range x).1) (sub_nonneg.mpr (range x).2)])
  simpa [integral_sub (hf.const_mul (m+M)) (integrable_const (m*M)), integral_const_mul] using h

/-- Squared mean-to-RMS bound before replacing M/m by the exponential oscillation. -/
theorem reverse_rms (m M mean second : ℝ) (hm : 0 ≤ m) (hM : 0 ≤ M)
    (secant : second ≤ (m+M)*mean-m*M) :
    4*m*M*second ≤ ((m+M)*mean)^2 := by
  have h := mul_le_mul_of_nonneg_left secant (show 0 ≤ 4*m*M by positivity)
  nlinarith [sq_nonneg ((m+M)*mean-2*m*M)]

-- NATIVE CHILD 1
/-- Domination of block entries implies domination on a nonnegative trial vector. -/
theorem trial_domination {I : Type*} [Fintype I] (v : I → ℝ)
    (a b : I → I → ℝ) (hv : ∀ i, 0 ≤ v i) (h : ∀ i j, a i j ≤ b i j) :
    ∑ i, ∑ j, v i * a i j * v j ≤ ∑ i, ∑ j, v i * b i j * v j := by
  exact Finset.sum_le_sum fun i _ => Finset.sum_le_sum fun j _ =>
    mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left (h i j) (hv i)) (hv j)

/-- Product of the block means with their measured RMS values. -/
theorem overlap_lower {I : Type*} [Fintype I] (h b c : I → ℝ)
    (hb : ∀ i, 0 ≤ b i) (bound : ∀ i, h i * b i ≤ c i) :
    ∑ i, h i * (b i)^2 ≤ ∑ i, c i * b i := by
  apply Finset.sum_le_sum
  intro i _
  simpa [pow_two, mul_assoc] using mul_le_mul_of_nonneg_right (bound i) (hb i)

-- NATIVE CHILD 2
lemma block_residual (u b inner error : ℝ) (hu : u = 1) (hb : b = 1)
    (he : 1-error ≤ inner) : u+b-2*inner ≤ 2*error := by
  linarith

/-- A bracket on the two leading singular values bounds the excitation ratio. -/
theorem excitation_ratio (s₁ s₂ lo hi numLo numHi : ℝ)
    (hlo : 0 < lo) (hs : 0 ≤ s₂)
    (a : lo ≤ s₁) (b : s₁ ≤ hi) (c : numLo ≤ s₂) (d : s₂ ≤ numHi) :
    numLo/hi ≤ s₂/s₁ ∧ s₂/s₁ ≤ numHi/lo := by
  have h₁ : 0 < s₁ := hlo.trans_le a
  have h₂ : 0 < hi := h₁.trans_le b
  constructor
  · exact (div_le_div_iff₀ h₂ h₁).2 (mul_le_mul c b h₁.le hs)
  · exact (div_le_div_iff₀ h₁ hlo).2 (mul_le_mul d a hlo.le (hs.trans d))

/-- Squared Ritz values are coordinatewise below the true thermal probabilities.
Their total deficit bounds the loss at each index. -/
theorem individual_ritz_loss {I : Type*} [Fintype I] (p c : I → ℝ)
    (dom : ∀ i, c i ≤ p i) (loss : ℝ) (budget : ∑ j, (p j-c j) ≤ loss) (i : I) :
    p i ≤ c i + loss := by
  have hi : p i-c i ≤ ∑ j, (p j-c j) :=
    Finset.single_le_sum (fun j _ => sub_nonneg.mpr (dom j)) (Finset.mem_univ i)
  linarith

/-- A normalized finite partition gives a quadratic budget for the omitted mass. -/
theorem compression_budget {I : Type*} [Fintype I] (w h c : I → ℝ)
    (norm : ∑ i, w i = 1) (dom : ∀ i, w i * (h i)^2 ≤ (c i)^2) :
    1-(∑ i, (c i)^2) ≤ ∑ i, (w i - w i * (h i)^2) := by
  rw [Finset.sum_sub_distrib, norm]
  exact sub_le_sub_left (Finset.sum_le_sum fun i _ => dom i) 1

#print axioms cell_second_moment
#print axioms reverse_rms
#print axioms trial_domination
#print axioms overlap_lower
#print axioms block_residual
#print axioms excitation_ratio
#print axioms individual_ritz_loss
#print axioms compression_budget
end Millennium.G4.PairedSlice
