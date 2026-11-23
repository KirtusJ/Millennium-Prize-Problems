import Mathlib

open Real

/-- (L1) log A = 2 arsinh s, with A = 1 + 2 s^2 + 2 s sqrt(1+s^2). -/
theorem two_arsinh_eq_log (s : ℝ) (hs : 0 ≤ s) :
    2 * arsinh s = log (1 + 2 * s ^ 2 + 2 * s * sqrt (1 + s ^ 2)) := by
  have h2 : sqrt (1 + s ^ 2) ^ 2 = 1 + s ^ 2 := sq_sqrt (by positivity)
  have key : (s + sqrt (1 + s ^ 2)) ^ 2 = 1 + 2 * s ^ 2 + 2 * s * sqrt (1 + s ^ 2) := by
    linear_combination h2
  rw [← key, log_pow, arsinh]
  push_cast
  ring

/-- (L2) Gaussian fixed point: with alpha = 2 s sqrt(1+s^2), c = s^2 + alpha/2, A = 1 + 2c,
    (alpha/2 - s^2) * A = c. -/
theorem fixed_point (s : ℝ) :
    let α := 2 * s * sqrt (1 + s ^ 2)
    let c := s ^ 2 + α / 2
    (α / 2 - s ^ 2) * (1 + 2 * c) = c := by
  intro α c
  have h2 : sqrt (1 + s ^ 2) ^ 2 = 1 + s ^ 2 := sq_sqrt (by positivity)
  simp only [α, c]
  nlinarith [h2]

/-- (L3) weak duality on the circle: for a unit vector q, mu > 0, c ≥ 0,
    p1 q1 + p2 q2 - c q2^2 ≤ p1^2/(2 mu) + p2^2/(2 (mu + 2c)) + mu/2. -/
theorem weak_duality (p1 p2 q1 q2 μ c : ℝ) (hq : q1 ^ 2 + q2 ^ 2 = 1) (hμ : 0 < μ) (hc : 0 ≤ c) :
    p1 * q1 + p2 * q2 - c * q2 ^ 2 ≤ p1 ^ 2 / (2 * μ) + p2 ^ 2 / (2 * (μ + 2 * c)) + μ / 2 := by
  have hν : 0 < μ + 2 * c := by linarith
  have e1 : p1 * q1 ≤ p1 ^ 2 / (2 * μ) + μ * q1 ^ 2 / 2 := by
    rw [div_add_div _ _ (by positivity) (by norm_num), le_div_iff₀ (by positivity)]
    nlinarith [sq_nonneg (p1 - μ * q1), hμ]
  have e2 : p2 * q2 ≤ p2 ^ 2 / (2 * (μ + 2 * c)) + (μ + 2 * c) * q2 ^ 2 / 2 := by
    rw [div_add_div _ _ (by positivity) (by norm_num), le_div_iff₀ (by positivity)]
    nlinarith [sq_nonneg (p2 - (μ + 2 * c) * q2), hν]
  nlinarith [e1, e2, hq]

/-- (L4) AM-GM and the lower comparison used for the Bessel argument:
    for x, y ∈ [0,1], x*y ≤ sqrt(x*y) ≤ (x+y)/2. -/
theorem amgm_pair (x y : ℝ) (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (hy0 : 0 ≤ y) (hy1 : y ≤ 1) :
    x * y ≤ sqrt (x * y) ∧ sqrt (x * y) ≤ (x + y) / 2 := by
  have hxy0 : 0 ≤ x * y := mul_nonneg hx0 hy0
  have hxy1 : x * y ≤ 1 := by nlinarith
  constructor
  · rw [le_sqrt hxy0 hxy0]; nlinarith
  · rw [sqrt_le_left (by linarith)]; nlinarith [sq_nonneg (x - y)]

/-- (L5) quadratic step for the outer bound: if g(1) = 0, g'(1) = γ, g'' ≤ 8 on [1/2,1],
    the scalar core is: -θγ + 4θ² = -γ²/16 at θ = γ/8. -/
theorem quad_step (γ : ℝ) : -(γ / 8) * γ + 4 * (γ / 8) ^ 2 = -(γ ^ 2 / 16) := by ring

#print axioms two_arsinh_eq_log
#print axioms fixed_point
#print axioms weak_duality
#print axioms amgm_pair
#print axioms quad_step
