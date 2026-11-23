/-
R12Analytic.lean  (namespace R12)  -- worker r12-lean, director Z4.

Predicates fixed before the first run (rule 3):
 P1. `lake env lean R12Analytic.lean` exits with code 0.
 P2. No `sorry` in this file (checked by grep, exit 1 = no match).
 P3. `#print axioms` for every theorem below lists only propext, Classical.choice, Quot.sound
     (or a subset of them).
 P4. Mutation control: theorem `F3_const_25_false` proves the NEGATION of F3 with 24 replaced
     by 25, at the witness k = 1, b = 1/5 (y = k b / 2 = 1/10).
-/
import Mathlib

open Real MeasureTheory Set

namespace R12

/-- auxiliary: g(y) = sin y - y + y^3/6 is monotone on all of ℝ, since g' = cos y - 1 + y^2/2 ≥ 0. -/
theorem sin_sub_cubic_monotone :
    Monotone (fun y : ℝ => Real.sin y - y + y ^ 3 / 6) := by
  have hd : ∀ y : ℝ, HasDerivAt (fun y : ℝ => Real.sin y - y + y ^ 3 / 6)
      (Real.cos y - 1 + y ^ 2 / 2) y := by
    intro y
    have h1 := ((Real.hasDerivAt_sin y).sub (hasDerivAt_id y)).add
      ((hasDerivAt_pow 3 y).div_const 6)
    convert h1 using 1
    simp; ring
  apply monotone_of_deriv_nonneg
  · intro y; exact (hd y).differentiableAt
  · intro y
    rw [(hd y).deriv]
    linarith [Real.one_sub_sq_div_two_le_cos (x := y)]

/-- F1. For all real y ≥ 0: y - y^3/6 ≤ sin y. -/
theorem F1 (y : ℝ) (hy : 0 ≤ y) : y - y ^ 3 / 6 ≤ Real.sin y := by
  have := sin_sub_cubic_monotone hy
  simp at this
  linarith

/-- auxiliary: for y ≤ 0, sin y ≤ y - y^3/6. -/
theorem F1_neg (y : ℝ) (hy : y ≤ 0) : Real.sin y ≤ y - y ^ 3 / 6 := by
  have := sin_sub_cubic_monotone hy
  simp at this
  linarith

/-- F2. For all real y: |sin y - y| ≤ |y|^3/6. -/
theorem F2 (y : ℝ) : |Real.sin y - y| ≤ |y| ^ 3 / 6 := by
  rcases le_total 0 y with hy | hy
  · rw [abs_of_nonneg hy, abs_of_nonpos (by linarith [Real.sin_le hy])]
    linarith [F1 y hy]
  · rw [abs_of_nonpos hy, abs_of_nonneg (by linarith [Real.le_sin hy])]
    have := F1_neg y hy
    have h3 : (-y) ^ 3 = -(y ^ 3) := by ring
    rw [h3]; linarith

/-- F3. Lattice momentum error: for b > 0, real k: |(2/b) sin(k b/2) - k| ≤ b^2 |k|^3 / 24. -/
theorem F3 (b k : ℝ) (hb : 0 < b) :
    |(2 / b) * Real.sin (k * b / 2) - k| ≤ b ^ 2 * |k| ^ 3 / 24 := by
  have e : (2 / b) * Real.sin (k * b / 2) - k = (2 / b) * (Real.sin (k * b / 2) - k * b / 2) := by
    field_simp; ring
  rw [e, abs_mul, abs_of_pos (by positivity : (0:ℝ) < 2 / b)]
  have h := F2 (k * b / 2)
  have hab : |k * b / 2| = |k| * b / 2 := by
    rw [abs_div, abs_mul, abs_of_pos hb, abs_of_pos (by norm_num : (0:ℝ) < 2)]
  rw [hab] at h
  calc (2 / b) * |Real.sin (k * b / 2) - k * b / 2| ≤ (2 / b) * ((|k| * b / 2) ^ 3 / 6) :=
        mul_le_mul_of_nonneg_left h (by positivity)
    _ = b ^ 2 * |k| ^ 3 / 24 := by field_simp; ring

/-- F4a. Jordan, two-sided: for |y| ≤ π/2: (2/π)|y| ≤ |sin y| ≤ |y|.
    (The upper bound holds for all y; the hypothesis is used only for the lower bound.) -/
theorem F4a (y : ℝ) (hy : |y| ≤ π / 2) :
    2 / π * |y| ≤ |Real.sin y| ∧ |Real.sin y| ≤ |y| :=
  ⟨Real.mul_abs_le_abs_sin hy, Real.abs_sin_le_abs⟩

/-- F4b. For b > 0, |k b| ≤ π: (2/π)|k| ≤ |(2/b) sin(k b/2)| ≤ |k|. -/
theorem F4b (b k : ℝ) (hb : 0 < b) (hkb : |k * b| ≤ π) :
    2 / π * |k| ≤ |(2 / b) * Real.sin (k * b / 2)| ∧
      |(2 / b) * Real.sin (k * b / 2)| ≤ |k| := by
  have hab : |k * b / 2| = |k| * b / 2 := by
    rw [abs_div, abs_mul, abs_of_pos hb, abs_of_pos (by norm_num : (0:ℝ) < 2)]
  have hy : |k * b / 2| ≤ π / 2 := by
    rw [abs_div, abs_of_pos (by norm_num : (0:ℝ) < 2)]; linarith
  obtain ⟨h1, h2⟩ := F4a (k * b / 2) hy
  rw [hab] at h1 h2
  rw [abs_mul, abs_of_pos (by positivity : (0:ℝ) < 2 / b)]
  constructor
  · calc 2 / π * |k| = (2 / b) * (2 / π * (|k| * b / 2)) := by field_simp; ring
      _ ≤ (2 / b) * |Real.sin (k * b / 2)| := mul_le_mul_of_nonneg_left h1 (by positivity)
  · calc (2 / b) * |Real.sin (k * b / 2)| ≤ (2 / b) * (|k| * b / 2) :=
          mul_le_mul_of_nonneg_left h2 (by positivity)
      _ = |k| := by field_simp; ring

/-- F5. Gaussian sum against integral: c > 0, M : ℕ:  ∑_{m=1}^{M} exp(-c m^2) ≤ √(π/c)/2. -/
theorem F5 (c : ℝ) (hc : 0 < c) (M : ℕ) :
    ∑ m ∈ Finset.Icc 1 M, Real.exp (-c * (m : ℝ) ^ 2) ≤ √(π / c) / 2 := by
  set f : ℝ → ℝ := fun x => Real.exp (-c * x ^ 2) with hf
  have hanti : AntitoneOn f (Icc (0:ℝ) (0 + M)) := by
    intro x hx y hy hxy
    simp only [hf]
    apply Real.exp_le_exp.mpr
    have : x ^ 2 ≤ y ^ 2 := by nlinarith [hx.1, hy.1]
    nlinarith
  have h1 := hanti.sum_le_integral
  have hsum : ∑ m ∈ Finset.Icc 1 M, Real.exp (-c * (m : ℝ) ^ 2)
      = ∑ i ∈ Finset.range M, f (0 + ((i + 1 : ℕ) : ℝ)) := by
    rw [← Nat.Ico_succ_right, Finset.sum_Ico_eq_sum_range]
    simp only [hf, Nat.succ_sub_one]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    push_cast; ring_nf
  rw [hsum]
  refine h1.trans ?_
  rw [intervalIntegral.integral_of_le (by simp), ← integral_gaussian_Ioi c]
  apply setIntegral_mono_set
  · exact (integrable_exp_neg_mul_sq hc).integrableOn
  · exact Filter.Eventually.of_forall (fun x => (Real.exp_pos _).le)
  · exact (Ioc_subset_Ioi_self).eventuallyLE

/-- F6. For x ≥ 0 (in fact any real x), natural j ≥ 1, c > 0:
    x^(2j) exp(-c x^2) ≤ (j/(e c))^j,  with e = exp 1. -/
theorem F6 (x c : ℝ) (j : ℕ) (hj : 1 ≤ j) (hc : 0 < c) :
    x ^ (2 * j) * Real.exp (-c * x ^ 2) ≤ ((j : ℝ) / (Real.exp 1 * c)) ^ j := by
  have hjpos : (0:ℝ) < j := by exact_mod_cast hj
  set t : ℝ := c * x ^ 2 / j with ht
  have ht0 : 0 ≤ t := by positivity
  -- t ≤ exp(t - 1)
  have hte : t ≤ Real.exp (t - 1) := by linarith [Real.add_one_le_exp (t - 1)]
  have htj : t ^ j ≤ Real.exp (t - 1) ^ j := pow_le_pow_left₀ ht0 hte j
  rw [← Real.exp_nat_mul] at htj
  have hx2 : x ^ (2 * j) = ((j : ℝ) / c) ^ j * t ^ j := by
    rw [← mul_pow, ht, pow_mul]; congr 1; field_simp; ring
  have hexp : Real.exp (j * (t - 1)) * Real.exp (-c * x ^ 2) = Real.exp (-1) ^ j := by
    rw [← Real.exp_add, ← Real.exp_nat_mul]; congr 1; rw [ht]; field_simp; ring
  calc x ^ (2 * j) * Real.exp (-c * x ^ 2)
      = ((j : ℝ) / c) ^ j * (t ^ j * Real.exp (-c * x ^ 2)) := by rw [hx2]; ring
    _ ≤ ((j : ℝ) / c) ^ j * (Real.exp (j * (t - 1)) * Real.exp (-c * x ^ 2)) := by
        gcongr
    _ = ((j : ℝ) / c) ^ j * Real.exp (-1) ^ j := by rw [hexp]
    _ = ((j : ℝ) / (Real.exp 1 * c)) ^ j := by
        rw [← mul_pow, Real.exp_neg]; congr 1
        rw [mul_comm (Real.exp 1) c, ← div_div, div_eq_mul_inv _ (Real.exp 1)]

/-- F7a. p^2 + q^2 > 0 ⇒ p^2/(p^2+q^2) ∈ [0,1]. -/
theorem F7a (p q : ℝ) (h : 0 < p ^ 2 + q ^ 2) :
    0 ≤ p ^ 2 / (p ^ 2 + q ^ 2) ∧ p ^ 2 / (p ^ 2 + q ^ 2) ≤ 1 := by
  refine ⟨by positivity, ?_⟩
  rw [div_le_one h]; nlinarith [sq_nonneg q]

/-- F7b. a, a' ∈ [0, A] ⇒ |a^2 - a'^2| ≤ 2 A |a - a'|. -/
theorem F7b (A a a' : ℝ) (ha : a ∈ Icc 0 A) (ha' : a' ∈ Icc 0 A) :
    |a ^ 2 - a' ^ 2| ≤ 2 * A * |a - a'| := by
  have e : a ^ 2 - a' ^ 2 = (a + a') * (a - a') := by ring
  rw [e, abs_mul, abs_of_nonneg (by linarith [ha.1, ha'.1])]
  exact mul_le_mul_of_nonneg_right (by linarith [ha.2, ha'.2]) (abs_nonneg _)

/-- Mutation control: the constant 24 in F3 cannot be replaced by 25.
    Witness k = 1, b = 1/5 (y = 1/10), using Mathlib's `Real.sin_bound`. -/
theorem F3_const_25_false :
    ¬ ∀ b k : ℝ, 0 < b → |(2 / b) * Real.sin (k * b / 2) - k| ≤ b ^ 2 * |k| ^ 3 / 25 := by
  intro H
  have h := H (1/5) 1 (by norm_num)
  have hs := Real.sin_bound (x := (1:ℝ) * (1/5) / 2) (by norm_num [abs_of_pos])
  have e : (1:ℝ) * (1/5) / 2 = 1/10 := by norm_num
  rw [e] at h hs
  rw [abs_le] at hs
  norm_num [abs_of_pos] at hs
  -- hs.2 : sin(1/10) ≤ 1/10 - 1/6000 + 5/960000 ≈ 0.0998385 < 0.09984
  have hneg : (2 / (1/5:ℝ)) * Real.sin (1/10) - 1 < 0 := by linarith [hs.2]
  rw [abs_of_neg hneg] at h
  norm_num at h
  linarith [hs.2]

end R12

#print axioms R12.F1
#print axioms R12.F2
#print axioms R12.F3
#print axioms R12.F4a
#print axioms R12.F4b
#print axioms R12.F5
#print axioms R12.F6
#print axioms R12.F7a
#print axioms R12.F7b
#print axioms R12.F3_const_25_false
