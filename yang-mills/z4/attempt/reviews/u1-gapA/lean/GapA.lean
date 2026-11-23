import Mathlib

open Real

/-! Scalar inequalities used in GAPS.md (u1-gapA). -/

/-- smoothstep range and derivative bound on [0,1] -/
theorem smoothstep_bounds (s : ℝ) (h0 : 0 ≤ s) (h1 : s ≤ 1) :
    0 ≤ 3*s^2 - 2*s^3 ∧ 3*s^2 - 2*s^3 ≤ 1 ∧ 0 ≤ 6*s - 6*s^2 ∧ 6*s - 6*s^2 ≤ 3/2 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> nlinarith [mul_nonneg h0 h0, mul_nonneg h0 (sub_nonneg.2 h1),
    mul_nonneg (mul_nonneg h0 h0) (sub_nonneg.2 h1), sq_nonneg (s - 1/2), sq_nonneg (s-1),
    mul_nonneg (sub_nonneg.2 h1) (sq_nonneg (s-1)), mul_nonneg (sq_nonneg s) (sub_nonneg.2 h1)]

/-- -1/2 log(1-x) <= x/(2(1-x)) -/
theorem neg_log_one_sub (x : ℝ) (h0 : 0 ≤ x) (h1 : x < 1) :
    -(1/2) * Real.log (1 - x) ≤ x / (2 * (1 - x)) := by
  have hp : 0 < 1 - x := by linarith
  have := Real.log_le_sub_one_of_pos (inv_pos.2 hp)
  rw [Real.log_inv] at this
  have e : (1 - x)⁻¹ - 1 = x / (1 - x) := by field_simp
  rw [e] at this
  have e2 : x / (2 * (1 - x)) = (1/2) * (x / (1 - x)) := by field_simp
  rw [e2]; linarith

/-- 1/2 log(1+y) <= y/2 -/
theorem half_log_one_add (y : ℝ) (h0 : 0 ≤ y) : (1/2) * Real.log (1 + y) ≤ y / 2 := by
  have := Real.log_le_sub_one_of_pos (show (0:ℝ) < 1 + y by linarith)
  linarith

/-- log(1-x) <= 0 for 0 <= x < 1 -/
theorem log_one_sub_nonpos (x : ℝ) (h0 : 0 ≤ x) (h1 : x < 1) : Real.log (1 - x) ≤ 0 :=
  Real.log_nonpos (by linarith) (by linarith)

/-- cross term: h/(1+2 h s) <= 1/(2 s) for h, s > 0 (s = sigma^2) -/
theorem cross_term (h s : ℝ) (hh : 0 < h) (hs : 0 < s) : h / (1 + 2*h*s) ≤ 1 / (2*s) := by
  rw [div_le_div_iff₀ (by positivity) (by positivity)]
  nlinarith

/-- product of the two span-eigenvalue factors -/
theorem det_factor (h np nm : ℝ) :
    (1 + 2*h*np) * (1 + 2*h*nm) = 1 + 2*h*(np + nm) + 4*h^2*(np*nm) := by ring

/-- difference of the b-coefficients: 1/D - 1/A = (A-D)/(A D) with A - D = 4hW -/
theorem coeff_diff (h S2 W : ℝ) (hA : 0 < 1 + 2*h*S2) (hD : 0 < 1 + 2*h*(S2 - 2*W)) :
    1/(1 + 2*h*(S2 - 2*W)) - 1/(1 + 2*h*S2) = 4*h*W / ((1 + 2*h*S2) * (1 + 2*h*(S2 - 2*W))) := by
  field_simp; ring

/-- flat identity (h-2)(1+2S^2 h) = h when S^2 h^2 - 2 S^2 h = 1 -/
theorem flat_identity (h S2 : ℝ) (hrel : S2*h^2 - 2*S2*h = 1) : (h - 2)*(1 + 2*S2*h) = h := by
  nlinarith [hrel]

/-- Delta h without the mean value theorem:
 for 0 < s0 <= s1, sqrt(1+1/s0) - sqrt(1+1/s1) <= (s1-s0)/(2 s0^2 sqrt(1+1/s0)). -/
theorem delta_h (s0 s1 : ℝ) (h0 : 0 < s0) (h01 : s0 ≤ s1) :
    Real.sqrt (1 + 1/s0) - Real.sqrt (1 + 1/s1) ≤ (s1 - s0) / (2 * s0^2 * Real.sqrt (1 + 1/s0)) := by
  have hs1 : 0 < s1 := lt_of_lt_of_le h0 h01
  set A0 := Real.sqrt (1 + 1/s0) with hA0
  set A1 := Real.sqrt (1 + 1/s1) with hA1
  have hA0p : 0 < A0 := Real.sqrt_pos.2 (by positivity)
  have hA1p : 0 < A1 := Real.sqrt_pos.2 (by positivity)
  have hA0sq : A0^2 = 1 + 1/s0 := Real.sq_sqrt (by positivity)
  have hA1sq : A1^2 = 1 + 1/s1 := Real.sq_sqrt (by positivity)
  -- s1*A1 >= s0*A0, via squares: s1^2 A1^2 = s1^2 + s1 >= s0^2 + s0 = s0^2 A0^2
  have k1 : (s1*A1)^2 = s1^2 + s1 := by rw [mul_pow, hA1sq]; field_simp; ring
  have k0 : (s0*A0)^2 = s0^2 + s0 := by rw [mul_pow, hA0sq]; field_simp; ring
  have hmono : s0*A0 ≤ s1*A1 := by
    have hsq : (s0*A0)^2 ≤ (s1*A1)^2 := by
      rw [k0, k1]; nlinarith [mul_le_mul h01 h01 h0.le hs1.le]
    exact (pow_le_pow_iff_left₀ (by positivity) (by positivity) (by norm_num)).1 hsq
  -- A0 - A1 = (1/s0 - 1/s1)/(A0+A1) = (s1-s0)/(s0 s1 (A0+A1))
  have hdiff : A0 - A1 = (s1 - s0) / (s0 * s1 * (A0 + A1)) := by
    rw [eq_div_iff (by positivity)]
    rw [show (A0 - A1) * (s0 * s1 * (A0 + A1)) = (A0^2 - A1^2)*(s0*s1) by ring, hA0sq, hA1sq]
    field_simp; ring
  rw [hdiff]
  apply div_le_div_of_nonneg_left (by linarith) (by positivity)
  -- 2 s0^2 A0 <= s0 s1 (A0 + A1)  <=  2 s0 A0 <= s1 A0 + s1 A1
  have : 2*s0*A0 ≤ s1*A0 + s1*A1 := by nlinarith [mul_le_mul_of_nonneg_right h01 hA0p.le]
  nlinarith [mul_le_mul_of_nonneg_left this h0.le]

#print axioms smoothstep_bounds
#print axioms neg_log_one_sub
#print axioms half_log_one_add
#print axioms log_one_sub_nonpos
#print axioms cross_term
#print axioms det_factor
#print axioms coeff_diff
#print axioms flat_identity
#print axioms delta_h
