import Mathlib

open Finset

/-- (P1) Cauchy–Schwarz along a path of n steps: (sum of increments)^2 ≤ n * sum of squares. -/
theorem path_cs (n : ℕ) (a : ℕ → ℝ) :
    (∑ k ∈ range n, a k) ^ 2 ≤ (n : ℝ) * ∑ k ∈ range n, a k ^ 2 := by
  have := sq_sum_le_card_mul_sum_sq (s := range n) (f := a)
  simpa using this

/-- (P2) telescoping: h(z_0) - h(z_n) is the sum of the n increments. -/
theorem telescope (n : ℕ) (z : ℕ → ℝ) :
    z 0 - z n = ∑ k ∈ range n, (z k - z (k + 1)) := by
  induction n with
  | zero => simp
  | succ m ih => rw [sum_range_succ, ← ih]; ring

/-- (P3) closing algebra of Lemma P'c: 4F ≤ n ρ (2Δ), n, ρ > 0  ⟹  2F/(nρ) ≤ Δ. -/
theorem close_bound (F n ρ Δ : ℝ) (hn : 0 < n) (hρ : 0 < ρ) (h : 4 * F ≤ n * ρ * (2 * Δ)) :
    2 * F / (n * ρ) ≤ Δ := by
  have hnr : 0 < n * ρ := mul_pos hn hρ
  rw [div_le_iff₀ hnr]
  nlinarith

/-- (P4) completing the square in the Gaussian tilt (continuum Lemma S, exact moment), with s = √β. -/
theorem tilt_square_s (s t ρ : ℝ) (hs : 0 < s) :
    -(s ^ 2) * t ^ 2 / 2 - ρ * s * t = -(s ^ 2) * (t + ρ / s) ^ 2 / 2 + ρ ^ 2 / 2 := by
  field_simp
  ring

theorem tilt_square (β t ρ : ℝ) (hβ : 0 < β) :
    -β * t ^ 2 / 2 - ρ * Real.sqrt β * t
      = -β * (t + ρ / Real.sqrt β) ^ 2 / 2 + ρ ^ 2 / 2 := by
  have h := tilt_square_s (Real.sqrt β) t ρ (Real.sqrt_pos.mpr hβ)
  rwa [Real.sq_sqrt hβ.le] at h

/-- (P5) odd ratio: if h(σx) = -h(x) then (h x - h σx)^2 = 4 h(x)^2. -/
theorem odd_sq (u v : ℝ) (h : v = -u) : (u - v) ^ 2 = 4 * u ^ 2 := by
  subst h; ring

#print axioms path_cs
#print axioms telescope
#print axioms close_bound
#print axioms tilt_square
#print axioms odd_sq
