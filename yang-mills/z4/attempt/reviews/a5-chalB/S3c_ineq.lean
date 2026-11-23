import Mathlib
/-- S3c(ii): with background f independent of the free field, the normalised covariance
  (A*Gn + B*Gn^2 + V)/(A*G0 + B*G0^2 + V) is at least (Gn/G0)^2, where
  A = E|f|^2 >= 0, B = 3/2 > 0, V = Var(|f|^2/2) >= 0, 0 <= Gn <= G0, G0 > 0. -/
theorem s3c_ratio (A B V Gn G0 : ℝ) (hA : 0 ≤ A) (hB : 0 < B) (hV : 0 ≤ V)
    (hn : 0 ≤ Gn) (hle : Gn ≤ G0) (h0 : 0 < G0) :
    (Gn / G0) ^ 2 ≤ (A * Gn + B * Gn ^ 2 + V) / (A * G0 + B * G0 ^ 2 + V) := by
  have hden : 0 < A * G0 + B * G0 ^ 2 + V := by positivity
  rw [div_pow, div_le_div_iff₀ (by positivity) hden]
  have h1 : 0 ≤ A * Gn * G0 * (G0 - Gn) := by
    apply mul_nonneg (mul_nonneg (mul_nonneg hA hn) h0.le); linarith
  have h2 : 0 ≤ V * (G0 ^ 2 - Gn ^ 2) := by
    apply mul_nonneg hV; nlinarith
  nlinarith [h1, h2]
#print axioms s3c_ratio
