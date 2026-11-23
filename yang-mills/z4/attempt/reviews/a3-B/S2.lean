import Mathlib

/-- Step S2 (pure algebra): spectral upper bound + correlation lower bound give a gap upper bound. -/
theorem s2_gap_le (m c C0 Cn n : ℝ) (hC0 : 0 < C0) (hc : 0 < c) (hn : 0 < n)
    (h1 : Cn ≤ Real.exp (-(m * n)) * C0) (h2 : c * C0 ≤ Cn) : m ≤ -Real.log c / n := by
  have h3 : c ≤ Real.exp (-(m * n)) := le_of_mul_le_mul_right (by linarith) hC0
  have h4 : Real.log c ≤ -(m * n) := by
    rw [← Real.log_exp (-(m * n))]; exact Real.log_le_log hc h3
  rw [le_div_iff₀ hn]; linarith

/-- The power-law case: if c = K * n^(-p) then the bound tends to 0; here the algebraic identity. -/
theorem s2_power (K p n : ℝ) (hK : 0 < K) (hn : 0 < n) :
    -Real.log (K * n ^ (-p)) / n = (p * Real.log n - Real.log K) / n := by
  rw [Real.log_mul hK.ne' (Real.rpow_pos_of_pos hn _).ne', Real.log_rpow hn]; ring

#print axioms s2_gap_le
#print axioms s2_power
