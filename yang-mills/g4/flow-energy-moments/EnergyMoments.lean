import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

open MeasureTheory Set
open scoped BigOperators

namespace Millennium.G4.EnergyMoments

/-- Dividing a Wilson Lie jet by k! removes the linear degree growth per step. -/
theorem normalized_jet_bound (s : ℕ → ℝ) (a b : ℝ) (hb : 0 ≤ b)
    (h0 : s 0 ≤ a)
    (h : ∀ k : ℕ, s (k+1) ≤ (b*(4+4*(k:ℝ)))/(k+1) * s k) :
    ∀ k : ℕ, s k ≤ a*(4*b)^k := by
  intro k
  induction k with
  | zero => simpa using h0
  | succ k ih =>
    have c : (b*(4+4*(k:ℝ)))/(k+1) = 4*b := by
      have hk : (k:ℝ)+1 ≠ 0 := by positivity
      field_simp
      ring
    calc
      s (k+1) ≤ (4*b)*s k := by simpa [c] using h k
      _ ≤ (4*b)*(a*(4*b)^k) := mul_le_mul_of_nonneg_left ih (by positivity)
      _ = a*(4*b)^(k+1) := by ring

/-- Estimate the sum of the degree costs for a single monomial's active links. -/
theorem degree_cost {I : Type*} [Fintype I] (d w : I → ℝ) (D W : ℝ)
    (hn : ∀ i, 1 ≤ d i) (hw : ∀ i, w i ≤ W) (hW : 0 ≤ W)
    (hD : ∑ i, d i ≤ D) :
    ∑ i, (d i + 1)*w i ≤ 2*D*W := by
  calc
    ∑ i, (d i+1)*w i ≤ ∑ i, (2*d i)*W := by
      apply Finset.sum_le_sum
      intro i _
      have hi := hn i
      exact (mul_le_mul_of_nonneg_left (hw i) (by linarith)).trans
        (mul_le_mul_of_nonneg_right (by linarith) hW)
    _ = (2 * ∑ i, d i)*W := by rw [Finset.mul_sum, Finset.sum_mul]
    _ ≤ 2*D*W := mul_le_mul_of_nonneg_right (by linarith) hW

-- NATIVE CHILD 1
/-- A gap gives nonnegative shifted forms for every real square-integrable test
whenever the shifted integrand is integrable. -/
theorem shifted_form_nonneg {X : Type*} [MeasurableSpace X] (μ : Measure X)
    (E p : X → ℝ) (gap : ℝ) (h : ∀ᵐ x ∂μ, gap ≤ E x) :
    0 ≤ ∫ x, (E x - gap)*(p x)^2 ∂μ :=
  integral_nonneg_of_ae (h.mono fun _ hx => mul_nonneg (sub_nonneg.mpr hx) (sq_nonneg _))

/-- A set of positive spectral mass strictly below the proposed gap gives a
strictly negative shifted form for its indicator. -/
theorem below_edge_test {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsFiniteMeasure μ]
    (E : X → ℝ) (s : Set X) (hs : MeasurableSet s) (a gap : ℝ)
    (hm : 0 < μ.real s) (ha : a < gap) (he : ∀ x ∈ s, E x ≤ a)
    (hi : IntegrableOn (fun x => E x - gap) s μ) :
    ∫ x in s, (E x - gap) ∂μ < 0 := by
  have hconst : IntegrableOn (fun _ : X => a-gap) s μ := integrable_const _
  have h := setIntegral_mono_on hi hconst hs (fun x hx => sub_le_sub_right (he x hx) gap)
  rw [setIntegral_const, smul_eq_mul] at h
  exact h.trans_lt (mul_neg_of_pos_of_neg hm (sub_neg.mpr ha))

-- NATIVE CHILD 2
lemma quotient_edge_upper (edge mass energy : ℝ) (hm : 0 < mass)
    (he : edge * mass ≤ energy) : edge ≤ energy / mass :=
  (le_div_iff₀ hm).2 he

/-- Finite moment matching is preserved by adding an identical spectral component. -/
theorem common_component {I : Type*} (a b c : I → ℝ) (w : ℝ)
    (h : ∀ i, a i = b i) :
    ∀ i, w*a i + (1-w)*c i = w*b i + (1-w)*c i := by
  intro i
  rw [h i]

/-- The common mass of the two Jordan parts in the interpolation construction. -/
theorem jordan_masses (pos neg total : ℝ) (h0 : pos - neg = 1)
    (h1 : pos + neg = total) : pos = (total+1)/2 ∧ 1+neg = (total+1)/2 := by
  constructor <;> linarith

#print axioms normalized_jet_bound
#print axioms degree_cost
#print axioms shifted_form_nonneg
#print axioms below_edge_test
#print axioms quotient_edge_upper
#print axioms common_component
#print axioms jordan_masses

end Millennium.G4.EnergyMoments
