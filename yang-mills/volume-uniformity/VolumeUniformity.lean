/-
Director Z5 | Yang–Mills | volume uniformity.
Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada.
Formalized with assistance from Claude (Anthropic), acting as Director Z5.
Lean 4.19.0, Mathlib v4.19.0.
-/
import Mathlib

namespace Z5YM

/-- The lowest non-zero mode of the massless free lattice field on a circle of `N` sites has
transfer-operator energy `2 * arsinh (sin (π / N))`. It is at most `2 π / N`, for every `N > 0`. -/
theorem massless_mode_energy_le (N : ℝ) (hN : 0 < N) :
    2 * Real.arsinh (Real.sin (Real.pi / N)) ≤ 2 * Real.pi / N := by
  have hx : 0 ≤ Real.pi / N := div_nonneg Real.pi_pos.le hN.le
  have h1 : Real.sin (Real.pi / N) ≤ Real.pi / N := Real.sin_le hx
  have h2 : Real.arsinh (Real.pi / N) ≤ Real.pi / N := by
    have h := Real.arsinh_le_arsinh.mpr (Real.self_le_sinh_iff.mpr hx)
    rwa [Real.arsinh_sinh] at h
  have h3 := Real.arsinh_le_arsinh.mpr h1
  have : 2 * Real.pi / N = 2 * (Real.pi / N) := by ring
  linarith

/-- A gap that is bounded above by `C / L` in every volume `L > 0` has no positive lower bound
that is uniform in the volume. -/
theorem no_uniform_gap (gap : ℝ → ℝ) (C c : ℝ)
    (hup : ∀ L : ℝ, 0 < L → gap L ≤ C / L) (hlow : ∀ L : ℝ, 0 < L → c ≤ gap L) : c ≤ 0 := by
  by_contra hc
  push_neg at hc
  have hCpos : 0 < |C| + 1 := by positivity
  have hL : 0 < (|C| + 1) / c := div_pos hCpos hc
  have h := le_trans (hlow _ hL) (hup _ hL)
  have h' : c * ((|C| + 1) / c) ≤ C := (le_div_iff₀ hL).mp h
  rw [mul_div_cancel₀ _ hc.ne'] at h'
  linarith [le_abs_self C]

/-- Combined: in physical units the massless mode on a circle of length `L` with `N` sites
(spacing `L / N`) has energy `(N / L) * 2 * arsinh (sin (π / N)) ≤ 2 π / L`. -/
theorem massless_physical_gap_le (N L : ℝ) (hN : 0 < N) (hL : 0 < L) :
    (N / L) * (2 * Real.arsinh (Real.sin (Real.pi / N))) ≤ 2 * Real.pi / L := by
  have h := massless_mode_energy_le N hN
  have hNL : 0 ≤ N / L := (div_pos hN hL).le
  calc (N / L) * (2 * Real.arsinh (Real.sin (Real.pi / N)))
      ≤ (N / L) * (2 * Real.pi / N) := mul_le_mul_of_nonneg_left h hNL
    _ = 2 * Real.pi / L := by field_simp; ring

end Z5YM

#print axioms Z5YM.massless_mode_energy_le
#print axioms Z5YM.no_uniform_gap
#print axioms Z5YM.massless_physical_gap_le
