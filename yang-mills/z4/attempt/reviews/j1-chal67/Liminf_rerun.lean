import Mathlib

open Real

/-- G1: t + sqrt(1+t^2) ≤ exp t for t ≥ 0 (gives -ln r_ν ≤ (ν+1)/x from the lower Bessel bound). -/
theorem G1 (t : ℝ) (ht : 0 ≤ t) : t + Real.sqrt (1 + t ^ 2) ≤ Real.exp t := by
  have h1 : Real.sqrt (1 + t ^ 2) ≤ 1 + t ^ 2 / 2 := by
    rw [Real.sqrt_le_left (by positivity)]
    nlinarith [sq_nonneg t, sq_nonneg (t^2)]
  have h2 := Real.quadratic_le_exp_of_nonneg ht
  linarith

/-- G2: log(1+y) ≥ y/(1+y) for y ≥ 0 (gives -ln r_ν ≥ (ν+½)/(x+ν+½) from the upper Bessel bound). -/
theorem G2 (y : ℝ) (hy : 0 ≤ y) : y / (1 + y) ≤ Real.log (1 + y) := by
  have hpos : 0 < 1 + y := by linarith
  have h := Real.add_one_le_exp (-(Real.log (1 + y)))
  rw [Real.exp_neg, Real.exp_log hpos] at h
  rw [div_le_iff₀ hpos]
  have : 1 - Real.log (1 + y) ≤ 1 / (1 + y) := by rw [one_div]; linarith
  have h3 : (1 - Real.log (1 + y)) * (1 + y) ≤ 1 := by
    calc (1 - Real.log (1 + y)) * (1 + y) ≤ (1 / (1 + y)) * (1 + y) :=
          mul_le_mul_of_nonneg_right this hpos.le
      _ = 1 := by field_simp
  nlinarith

/-- G3: 1 - exp(-y) ≥ y/(1+y) for y ≥ 0. -/
theorem G3 (y : ℝ) (hy : 0 ≤ y) : y / (1 + y) ≤ 1 - Real.exp (-y) := by
  have hpos : 0 < 1 + y := by linarith
  have he : 1 + y ≤ Real.exp y := by linarith [Real.add_one_le_exp y]
  have hexp : Real.exp (-y) = 1 / Real.exp y := by rw [Real.exp_neg]; ring
  have hey : 0 < Real.exp y := Real.exp_pos y
  rw [hexp, div_le_iff₀ hpos]
  have : 1 / Real.exp y ≤ 1 / (1 + y) := one_div_le_one_div_of_le hpos he
  have h4 : (1 / (1 + y)) * (1 + y) = 1 := by field_simp
  nlinarith [mul_le_mul_of_nonneg_right this hpos.le]

/-- G4: S7 minimisation: 4s - 8su + 4s²u² ≥ 4s - 4. -/
theorem G4 (s u : ℝ) : 4 * s - 4 ≤ 4 * s - 8 * s * u + 4 * s ^ 2 * u ^ 2 := by
  nlinarith [sq_nonneg (s * u - 1)]

/-- G5: chart: for 0 < a ≤ 1, a²(1 - a²/2) ≤ sin² a and sin a ≤ a. -/
theorem G5 (a : ℝ) (ha : 0 < a) (ha1 : a ≤ 1) :
    a ^ 2 * (1 - a ^ 2 / 2) ≤ Real.sin a ^ 2 ∧ Real.sin a ≤ a := by
  have h := Real.sin_gt_sub_cube ha ha1
  have hp : 0 ≤ a - a ^ 3 / 4 := by nlinarith [pow_le_one₀ ha.le ha1 (n := 2)]
  refine ⟨?_, Real.sin_le ha.le⟩
  have : (a - a ^ 3 / 4) ^ 2 ≤ Real.sin a ^ 2 := by
    exact pow_le_pow_left₀ hp h.le 2
  nlinarith [sq_nonneg (a ^ 3)]

/-- G6: Σ_{ν=1}^{n} (2ν+1) = n(n+2) and Σ_{ν=1}^{n} (2ν+2) = n(n+3). -/
theorem G6a (n : ℕ) : ∑ v ∈ Finset.Icc 1 n, (2 * v + 1) = n * (n + 2) := by
  induction n with
  | zero => simp
  | succ k ih =>
    rw [Finset.sum_Icc_succ_top (by omega), ih]; ring

theorem G6b (n : ℕ) : ∑ v ∈ Finset.Icc 1 n, (2 * v + 2) = n * (n + 3) := by
  induction n with
  | zero => simp
  | succ k ih =>
    rw [Finset.sum_Icc_succ_top (by omega), ih]; ring

/-- G7: 1 - ab ≥ 1 - a for 0 ≤ a, 0 ≤ b ≤ 1 (high-spin set), and IMS partition identity. -/
theorem G7 (a b : ℝ) (ha : 0 ≤ a) (hb : b ≤ 1) : 1 - a ≤ 1 - a * b := by nlinarith

theorem G8 (x u : ℝ) :
    (1 - u ^ 2) * (1 - x ^ 2) + u ^ 2 * (1 - x ^ 2) + x ^ 2 = 1 := by ring

#print axioms G1
#print axioms G2
#print axioms G3
#print axioms G4
#print axioms G5
#print axioms G6a
#print axioms G6b
#print axioms G7
#print axioms G8
