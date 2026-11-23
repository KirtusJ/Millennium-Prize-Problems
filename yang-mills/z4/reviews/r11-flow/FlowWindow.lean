/-
r11-flow, A5. Predicates fixed before first compile:
  L1 file compiles with exit 0 under Lean 4.19.0 + Mathlib, no `sorry` in the source;
  L2 `#print axioms` of pow_mul_exp_neg_le, gauss_factor_le and markov_window shows only
     propext, Classical.choice, Quot.sound;
  L3 (measured only) the hypothesis 0 < M of markov_window is stated, and its role recorded.
Content:
  pow_mul_exp_neg_le : y^m e^{-y} <= m^m e^{-m}  (y >= 0, m >= 1)  -- the scalar bound used for
                       the flow factor: k^{2m} e^{-a k^2} <= (m/(e a))^m, see gauss_factor_le.
  markov_window      : finite-sum Markov window: sum w >= v, sum w E <= M  ==>
                       weight with E <= 2M/v is >= v/2.
-/
import Mathlib

open Real Finset

namespace R11

/-- y^m e^{-y} ≤ m^m e^{-m} for y ≥ 0 and m ≥ 1. -/
lemma pow_mul_exp_neg_le (m : ℕ) (hm : 0 < m) (y : ℝ) (hy : 0 ≤ y) :
    y ^ m * exp (-y) ≤ (m : ℝ) ^ m * exp (-(m : ℝ)) := by
  have hm' : (0 : ℝ) < m := by exact_mod_cast hm
  have hz0 : 0 ≤ y / m := div_nonneg hy hm'.le
  have h1 : y / m ≤ exp (y / m - 1) := by linarith [add_one_le_exp (y / m - 1)]
  have h2 : (y / m) ^ m ≤ exp (y / m - 1) ^ m := pow_le_pow_left₀ hz0 h1 m
  have h3 : exp (y / m - 1) ^ m = exp (y - m) := by
    rw [← exp_nat_mul]
    congr 1
    field_simp
  have hy' : y ^ m = (m : ℝ) ^ m * (y / m) ^ m := by
    rw [← mul_pow]
    congr 1
    field_simp
  calc y ^ m * exp (-y) = (m : ℝ) ^ m * (y / m) ^ m * exp (-y) := by rw [hy']
    _ ≤ (m : ℝ) ^ m * exp (y - m) * exp (-y) := by
        apply mul_le_mul_of_nonneg_right _ (exp_pos _).le
        apply mul_le_mul_of_nonneg_left (h3 ▸ h2) (by positivity)
    _ = (m : ℝ) ^ m * exp (-(m : ℝ)) := by rw [mul_assoc, ← exp_add]; ring_nf

/-- The flow-factor bound: x^{2m} e^{-a x^2} ≤ (m/(e a))^m, written as
    a^m · x^{2m} e^{-a x^2} ≤ m^m e^{-m}, for a > 0, m ≥ 1, any real x. -/
lemma gauss_factor_le (m : ℕ) (hm : 0 < m) (a : ℝ) (ha : 0 < a) (x : ℝ) :
    a ^ m * (x ^ (2 * m) * exp (-(a * x ^ 2))) ≤ (m : ℝ) ^ m * exp (-(m : ℝ)) := by
  have hy : 0 ≤ a * x ^ 2 := by positivity
  have h := pow_mul_exp_neg_le m hm (a * x ^ 2) hy
  have e : a ^ m * (x ^ (2 * m) * exp (-(a * x ^ 2))) = (a * x ^ 2) ^ m * exp (-(a * x ^ 2)) := by
    rw [mul_pow, pow_mul]; ring
  rw [e]; exact h

/-- Finite-sum Markov window. If the total weight is at least v > 0 and the first moment
    is at most M > 0, then the weight carried by atoms with E ≤ 2M/v is at least v/2. -/
theorem markov_window {ι : Type*} (s : Finset ι) (w E : ι → ℝ)
    (hw : ∀ i, 0 ≤ w i) (hE : ∀ i, 0 ≤ E i) (v M : ℝ) (hv : 0 < v) (hM0 : 0 < M)
    (hsum : v ≤ ∑ i ∈ s, w i) (hmom : ∑ i ∈ s, w i * E i ≤ M) :
    v / 2 ≤ ∑ i ∈ s.filter (fun i => E i ≤ 2 * M / v), w i := by
  classical
  have split := Finset.sum_filter_add_sum_filter_not s (fun i => E i ≤ 2 * M / v) w
  have hB : ∑ i ∈ s.filter (fun i => ¬ E i ≤ 2 * M / v), (2 * M) * w i
      ≤ ∑ i ∈ s.filter (fun i => ¬ E i ≤ 2 * M / v), v * (w i * E i) := by
    apply Finset.sum_le_sum
    intro i hi
    rw [Finset.mem_filter] at hi
    have hlt : 2 * M / v < E i := lt_of_not_le hi.2
    have h2 : 2 * M < E i * v := (div_lt_iff₀ hv).mp hlt
    nlinarith [hw i]
  rw [← Finset.mul_sum, ← Finset.mul_sum] at hB
  have hsub : ∑ i ∈ s.filter (fun i => ¬ E i ≤ 2 * M / v), w i * E i ≤ ∑ i ∈ s, w i * E i :=
    Finset.sum_le_sum_of_subset_of_nonneg (Finset.filter_subset _ _)
      (fun i _ _ => mul_nonneg (hw i) (hE i))
  have hvB : v * ∑ i ∈ s.filter (fun i => ¬ E i ≤ 2 * M / v), w i * E i ≤ v * M :=
    mul_le_mul_of_nonneg_left (hsub.trans hmom) hv.le
  have hBle : ∑ i ∈ s.filter (fun i => ¬ E i ≤ 2 * M / v), w i ≤ v / 2 := by
    have h1 : M * (2 * ∑ i ∈ s.filter (fun i => ¬ E i ≤ 2 * M / v), w i) ≤ M * v := by linarith
    have h2 := le_of_mul_le_mul_left h1 hM0
    linarith
  linarith

end R11

#print axioms R11.pow_mul_exp_neg_le
#print axioms R11.gauss_factor_le
#print axioms R11.markov_window
