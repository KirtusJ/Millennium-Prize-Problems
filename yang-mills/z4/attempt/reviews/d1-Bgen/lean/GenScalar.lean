import Mathlib

open Real

/-- (L1) Haar-Jacobian factor: Jordan's inequality squared. -/
theorem jacobian_factor (x : ℝ) (hx : 0 < x) (hx' : x ≤ π / 2) :
    (2 / π) ^ 2 ≤ (sin x / x) ^ 2 := by
  have h1 : 2 / π * x ≤ sin x := Real.mul_le_sin hx.le hx'
  have hpi : 0 < π := Real.pi_pos
  have h2 : 2 / π ≤ sin x / x := by
    rw [le_div_iff₀ hx]; exact h1
  have h0 : 0 ≤ 2 / π := by positivity
  exact pow_le_pow_left₀ h0 h2 2

/-- (L2) the remainder coefficient in the near region, general N. -/
theorem remainder_coeff (N δ s : ℝ) (hN : 0 ≤ N) (hs : 0 ≤ s) (hsd : s ≤ 4 * δ) :
    N * s ^ 2 / 2 * exp (sqrt N * s) ≤ 2 * N * δ * exp (4 * sqrt N * δ) * s := by
  have hq : 0 ≤ sqrt N := Real.sqrt_nonneg N
  have he : exp (sqrt N * s) ≤ exp (4 * sqrt N * δ) := by
    apply Real.exp_le_exp.mpr; nlinarith
  have hs2 : s ^ 2 ≤ 4 * δ * s := by nlinarith
  have hE : 0 ≤ exp (sqrt N * s) := (Real.exp_pos _).le
  have hδ : 0 ≤ δ := by linarith
  calc N * s ^ 2 / 2 * exp (sqrt N * s) ≤ N * (4 * δ * s) / 2 * exp (sqrt N * s) := by
        apply mul_le_mul_of_nonneg_right _ hE
        apply div_le_div_of_nonneg_right _ (by norm_num)
        exact mul_le_mul_of_nonneg_left hs2 hN
    _ = 2 * N * δ * s * exp (sqrt N * s) := by ring
    _ ≤ 2 * N * δ * s * exp (4 * sqrt N * δ) := by
        apply mul_le_mul_of_nonneg_left he; positivity
    _ = 2 * N * δ * exp (4 * sqrt N * δ) * s := by ring

/-- (L3) combination step: from b ≤ k t and t² ≤ 4S. -/
theorem combine (a b k t S : ℝ) (hb : 0 ≤ b) (hk : 0 ≤ k) (hbt : b ≤ k * t)
    (htS : t ^ 2 ≤ 4 * S) : a ^ 2 / 4 - b ^ 2 / 2 ≥ a ^ 2 / 4 - 2 * k ^ 2 * S := by
  have h1 : b ^ 2 ≤ (k * t) ^ 2 := pow_le_pow_left₀ hb hbt 2
  have h2 : (k * t) ^ 2 = k ^ 2 * t ^ 2 := by ring
  have h3 : k ^ 2 * t ^ 2 ≤ k ^ 2 * (4 * S) := mul_le_mul_of_nonneg_left htS (sq_nonneg k)
  nlinarith

/-- (L4) chordal Lipschitz: s = χ², χ ∈ [0, √2]. -/
theorem chordal_lip (x y : ℝ) (hx : 0 ≤ x) (hy : 0 ≤ y) (hx2 : x ≤ sqrt 2) (hy2 : y ≤ sqrt 2) :
    |x ^ 2 - y ^ 2| ≤ 2 * sqrt 2 * |x - y| := by
  have : x ^ 2 - y ^ 2 = (x - y) * (x + y) := by ring
  rw [this, abs_mul, abs_of_nonneg (by linarith : 0 ≤ x + y)]
  have : x + y ≤ 2 * sqrt 2 := by linarith
  nlinarith [abs_nonneg (x - y)]

/-- (L5) global upper bound on the plaquette function, per eigenvalue. -/
theorem one_sub_cos_le (θ : ℝ) : 1 - cos θ ≤ θ ^ 2 / 2 := by
  have := Real.one_sub_sq_div_two_le_cos (x := θ)
  linarith

#print axioms jacobian_factor
#print axioms remainder_coeff
#print axioms combine
#print axioms chordal_lip
#print axioms one_sub_cos_le
