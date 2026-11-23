import Mathlib

open Real

/-- Phase-0 length: if 0 ≤ m ≤ M and 0 ≤ s ≤ 1 then (m s)^2 ≤ m M s (so m s ≤ sqrt(|u1×u2|)). -/
theorem phase0_len (m M s : ℝ) (hm : 0 ≤ m) (hmM : m ≤ M) (hs0 : 0 ≤ s) (hs1 : s ≤ 1) :
    (m * s) ^ 2 ≤ m * M * s := by
  have h1 : m * s ≤ M := by nlinarith
  have h2 : 0 ≤ m * s := mul_nonneg hm hs0
  nlinarith [mul_le_mul_of_nonneg_left h1 h2, mul_nonneg h2 hs0]

/-- Jordan-type bound used for the I₁ upper bound: 1 - cos θ ≥ 2 θ²/π² on [0, π]. -/
theorem one_sub_cos_ge_jordan (θ : ℝ) (h0 : 0 ≤ θ) (h1 : θ ≤ π) :
    2 * θ ^ 2 / π ^ 2 ≤ 1 - cos θ := by
  have hp : 0 < π := pi_pos
  have hs : 2 / π * (θ / 2) ≤ sin (θ / 2) := mul_le_sin (by linarith) (by linarith)
  have hc : cos θ = 1 - 2 * sin (θ / 2) ^ 2 := by
    have h2 := sin_sq_add_cos_sq (θ / 2)
    have : cos θ = cos (2 * (θ / 2)) := by ring_nf
    rw [this, cos_two_mul]; nlinarith
  have hnn : 0 ≤ 2 / π * (θ / 2) := by positivity
  have hsq : (2 / π * (θ / 2)) ^ 2 ≤ sin (θ / 2) ^ 2 := pow_le_pow_left₀ hnn hs 2
  have he : (2 / π * (θ / 2)) ^ 2 = θ ^ 2 / π ^ 2 := by field_simp; ring
  have h2 : 2 * θ ^ 2 / π ^ 2 = 2 * (θ ^ 2 / π ^ 2) := by ring
  rw [hc, h2, ← he]; nlinarith

/-- Ball volume core: for 0 ≤ x ≤ 1, x - sin x ≥ 11 x³/96 (used with x = 2r, r ≤ 1/2). -/
theorem x_sub_sin_ge (x : ℝ) (h0 : 0 ≤ x) (h1 : x ≤ 1) :
    11 * x ^ 3 / 96 ≤ x - sin x := by
  have hb := sin_bound (show |x| ≤ 1 by rw [abs_of_nonneg h0]; exact h1)
  rw [abs_of_nonneg h0] at hb
  have := (abs_le.mp hb).2
  have hx4 : x ^ 4 ≤ x ^ 3 := by
    have : x ^ 4 = x ^ 3 * x := by ring
    rw [this]; nlinarith [pow_nonneg h0 3]
  nlinarith

/-- Kernel lower bound core: cos θ ≥ 1 - θ²/2. -/
theorem cos_ge_quad (θ : ℝ) : 1 - θ ^ 2 / 2 ≤ cos θ := one_sub_sq_div_two_le_cos

/-- Phase 3: V(t) = (sin(t a)/sin a)^2 V(y) ≤ V(y) for 0 ≤ t ≤ 1, 0 ≤ a ≤ π/2. -/
theorem phase3_mono (a t : ℝ) (ha0 : 0 ≤ a) (ha1 : a ≤ π / 2) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    sin (t * a) ≤ sin a := by
  apply sin_le_sin_of_le_of_le_pi_div_two
  · nlinarith [pi_pos]
  · exact ha1
  · nlinarith

#print axioms phase0_len
#print axioms one_sub_cos_ge_jordan
#print axioms x_sub_sin_ge
#print axioms cos_ge_quad
#print axioms phase3_mono
