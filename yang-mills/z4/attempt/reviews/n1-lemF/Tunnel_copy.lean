import Mathlib

open Real

/-- Valley lemma (scalar core): the harmonic transverse energy on the commuting valley,
2 arsinh(sqrt(sin^2 a + sin^2 b)), dominates the single-link valley value 2 arsinh |sin a|. -/
theorem valley_energy_ge (a b : ℝ) :
    2 * arsinh |sin a| ≤ 2 * arsinh (sqrt (sin a ^ 2 + sin b ^ 2)) := by
  have h1 : |sin a| = sqrt (sin a ^ 2) := (sqrt_sq_eq_abs (sin a)).symm
  have h2 : sqrt (sin a ^ 2) ≤ sqrt (sin a ^ 2 + sin b ^ 2) :=
    sqrt_le_sqrt (by nlinarith [sq_nonneg (sin b)])
  have h3 : arsinh |sin a| ≤ arsinh (sqrt (sin a ^ 2 + sin b ^ 2)) := by
    rw [arsinh_le_arsinh]; rw [h1]; exact h2
  linarith

/-- Kernel lemma ingredient: for 0 ≤ θ ≤ η ≤ 1, 1 - cos θ ≥ (θ^2/2)(1 - 5 η^2/48). -/
theorem one_sub_cos_ge (θ η : ℝ) (h0 : 0 ≤ θ) (h1 : θ ≤ η) (h2 : η ≤ 1) :
    θ ^ 2 / 2 * (1 - 5 * η ^ 2 / 48) ≤ 1 - cos θ := by
  have hθ : |θ| ≤ 1 := by rw [abs_of_nonneg h0]; linarith
  have hb := Real.cos_bound hθ
  have hb' : cos θ - (1 - θ ^ 2 / 2) ≤ |θ| ^ 4 * (5 / 96) := le_trans (le_abs_self _) hb
  rw [abs_of_nonneg h0] at hb'
  have hsq : θ ^ 2 ≤ η ^ 2 := by nlinarith
  have h4 : θ ^ 4 ≤ θ ^ 2 * η ^ 2 := by nlinarith [sq_nonneg θ]
  nlinarith

#print axioms valley_energy_ge
#print axioms one_sub_cos_ge
