import Mathlib

open Finset Real

namespace R11Flow

/-- The flow factor only decreases each nonnegative term. -/
theorem flow_decreases {x s y : ℝ} (hx : 0 ≤ x) (hs : 0 ≤ s) (hy : 0 ≤ y) :
    x * Real.exp (-(s * y)) ≤ x := by
  have h1 : Real.exp (-(s * y)) ≤ 1 := by
    rw [Real.exp_le_one_iff]; nlinarith [mul_nonneg hs hy]
  calc x * Real.exp (-(s * y)) ≤ x * 1 := mul_le_mul_of_nonneg_left h1 hx
    _ = x := mul_one x

/-- Termwise monotonicity in Euclidean time: t ≤ t', E ≥ 0, w ≥ 0. -/
theorem term_antitone {w E t t' : ℝ} (hw : 0 ≤ w) (hE : 0 ≤ E) (ht : t ≤ t') :
    w * Real.exp (-(t' * E)) ≤ w * Real.exp (-(t * E)) := by
  apply mul_le_mul_of_nonneg_left _ hw
  apply Real.exp_le_exp.mpr
  nlinarith

/-- C(t) = Σ w_i e^{-t E_i} is antitone in t (finite sums). -/
theorem C_antitone {ι : Type*} (S : Finset ι) (w E : ι → ℝ) (hw : ∀ i, 0 ≤ w i) (hE : ∀ i, 0 ≤ E i)
    {t t' : ℝ} (ht : t ≤ t') :
    ∑ i ∈ S, w i * Real.exp (-(t' * E i)) ≤ ∑ i ∈ S, w i * Real.exp (-(t * E i)) :=
  Finset.sum_le_sum fun i _ => term_antitone (hw i) (hE i) ht

/-- Weighted AM-GM used for the moment bounds. -/
theorem weighted_amgm (x y lam : ℝ) (hl : 0 < lam) : x * y ≤ (lam * x ^ 2 + y ^ 2 / lam) / 2 := by
  have h : 0 ≤ (lam * x - y) ^ 2 := sq_nonneg _
  have key : 2 * lam * (x * y) ≤ lam * (lam * x ^ 2) + y ^ 2 := by nlinarith
  rw [le_div_iff₀ (by norm_num : (0:ℝ) < 2)]
  have : lam * x ^ 2 + y ^ 2 / lam = (lam * (lam * x ^ 2) + y ^ 2) / lam := by
    field_simp; ring
  rw [this, le_div_iff₀ hl]; nlinarith

/-- Schur test (the step that replaces sup|fhat|): F ≥ 0 with all row and column sums ≤ P gives
    Σ_{i,j} F i j a_i a_j ≤ P Σ_i a_i². In the application F(k,k') = |fhat_b(k+k')|², P = l³ b³ Σ f². -/
theorem schur {ι : Type*} (S : Finset ι) (F : ι → ι → ℝ) (a : ι → ℝ) (P : ℝ)
    (hF : ∀ i j, 0 ≤ F i j) (hrow : ∀ i, ∑ j ∈ S, F i j ≤ P) (hcol : ∀ j, ∑ i ∈ S, F i j ≤ P) :
    ∑ i ∈ S, ∑ j ∈ S, F i j * a i * a j ≤ P * ∑ i ∈ S, a i ^ 2 := by
  have step : ∀ i j, F i j * a i * a j ≤ F i j * (a i ^ 2 / 2) + F i j * (a j ^ 2 / 2) := by
    intro i j
    have : a i * a j ≤ a i ^ 2 / 2 + a j ^ 2 / 2 := by nlinarith [sq_nonneg (a i - a j)]
    nlinarith [hF i j, mul_le_mul_of_nonneg_left this (hF i j)]
  calc ∑ i ∈ S, ∑ j ∈ S, F i j * a i * a j
      ≤ ∑ i ∈ S, ∑ j ∈ S, (F i j * (a i ^ 2 / 2) + F i j * (a j ^ 2 / 2)) :=
        Finset.sum_le_sum fun i _ => Finset.sum_le_sum fun j _ => step i j
    _ = ∑ i ∈ S, (a i ^ 2 / 2) * ∑ j ∈ S, F i j + ∑ j ∈ S, (a j ^ 2 / 2) * ∑ i ∈ S, F i j := by
        simp only [Finset.sum_add_distrib]
        congr 1
        · apply Finset.sum_congr rfl; intro i _; rw [Finset.mul_sum]
          apply Finset.sum_congr rfl; intro j _; ring
        · rw [Finset.sum_comm]; apply Finset.sum_congr rfl; intro j _; rw [Finset.mul_sum]
          apply Finset.sum_congr rfl; intro i _; ring
    _ ≤ ∑ i ∈ S, (a i ^ 2 / 2) * P + ∑ j ∈ S, (a j ^ 2 / 2) * P := by
        gcongr with i _ j _
        · exact hrow i
        · exact hcol j
    _ = P * ∑ i ∈ S, a i ^ 2 := by
        rw [← Finset.sum_add_distrib, Finset.mul_sum]
        apply Finset.sum_congr rfl; intro i _; ring

/-- Moment ratio from termwise bounds: M0 ≥ v > 0, 0 ≤ M1 ≤ U ⇒ M1/M0 ≤ U/v. -/
theorem ratio_bound {M0 M1 v U : ℝ} (hv : 0 < v) (h0 : v ≤ M0) (h1 : 0 ≤ M1) (hU : M1 ≤ U) :
    M1 / M0 ≤ U / v := by
  have hM0 : 0 < M0 := lt_of_lt_of_le hv h0
  rw [div_le_div_iff₀ hM0 hv]
  nlinarith

/-- e^{-x} ≤ 1/(e x) for x > 0 (used as e^{-s/b²} ≤ b²/(e s)). -/
theorem exp_neg_le_inv {x : ℝ} (hx : 0 < x) : Real.exp (-x) ≤ 1 / (Real.exp 1 * x) := by
  have h := Real.add_one_le_exp (x - 1)
  have hx1 : Real.exp (x - 1) = Real.exp x / Real.exp 1 := by rw [Real.exp_sub]
  rw [hx1] at h
  have he : 0 < Real.exp 1 := Real.exp_pos 1
  have hex : 0 < Real.exp x := Real.exp_pos x
  rw [Real.exp_neg, le_div_iff₀ (by positivity)]
  rw [le_div_iff₀ he] at h
  have : x * Real.exp 1 ≤ Real.exp x := by linarith
  calc (Real.exp x)⁻¹ * (Real.exp 1 * x) = (x * Real.exp 1) / Real.exp x := by field_simp <;> ring
    _ ≤ Real.exp x / Real.exp x := by gcongr
    _ = 1 := div_self (ne_of_gt hex)

end R11Flow

#print axioms R11Flow.flow_decreases
#print axioms R11Flow.C_antitone
#print axioms R11Flow.weighted_amgm
#print axioms R11Flow.schur
#print axioms R11Flow.ratio_bound
#print axioms R11Flow.exp_neg_le_inv
