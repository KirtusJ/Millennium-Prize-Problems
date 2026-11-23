import Mathlib

open Filter Topology

/-- Generic area-law limit (W1). Hypotheses exactly as used:
  `hρ`: ρ N > 0 for every N (needed for log; ρ ≤ 1 is NOT used),
  `hσ`: N² · (−log ρ N) → σ,
  `hA`: n N / N² → A (real division; the value at N = 0 is irrelevant).
  Conclusion: ρ N ^ n N → exp (−σ · A). -/
theorem wilson_area_limit (ρ : ℕ → ℝ) (n : ℕ → ℕ) (σ A : ℝ)
    (hρ : ∀ N, 0 < ρ N)
    (hσ : Tendsto (fun N : ℕ => (N : ℝ) ^ 2 * (-Real.log (ρ N))) atTop (𝓝 σ))
    (hA : Tendsto (fun N : ℕ => (n N : ℝ) / (N : ℝ) ^ 2) atTop (𝓝 A)) :
    Tendsto (fun N => ρ N ^ n N) atTop (𝓝 (Real.exp (-σ * A))) := by
  have hprod : Tendsto (fun N : ℕ =>
      -(((n N : ℝ) / (N : ℝ) ^ 2) * ((N : ℝ) ^ 2 * (-Real.log (ρ N))))) atTop
      (𝓝 (-(A * σ))) := (hA.mul hσ).neg
  have hexp := (Real.continuous_exp.tendsto _).comp hprod
  have hlim : Real.exp (-(A * σ)) = Real.exp (-σ * A) := by ring_nf
  rw [← hlim]
  refine hexp.congr' ?_
  filter_upwards [eventually_ge_atTop 1] with N hN
  have hN0 : (N : ℝ) ≠ 0 := by
    have : (1 : ℝ) ≤ N := by exact_mod_cast hN
    linarith
  have hN2 : (N : ℝ) ^ 2 ≠ 0 := pow_ne_zero 2 hN0
  simp only [Function.comp]
  rw [← Real.exp_log (pow_pos (hρ N) (n N)), Real.log_pow]
  congr 1
  field_simp

#print axioms wilson_area_limit
