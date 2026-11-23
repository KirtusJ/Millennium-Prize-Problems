import Mathlib

/-- Taylor step of Lemma tu:U-outer: if g(1)=0, g'(1)=γ, g'' ≤ 8 on [1/2,1], then g(1-γ/8) ≤ -γ²/16.
    Scalar core: with h = γ/8, 0 ≤ γ < 1/2, the quadratic majorant -hγ + 4h² equals -γ²/16. -/
theorem outer_taylor_core (γ : ℝ) : -(γ/8)*γ + 4*(γ/8)^2 = -γ^2/16 := by ring

/-- Mean-value form used: for g with g(1)=0, the Taylor bound g(1-h) ≤ -h γ + (M/2) h² with M = 8. -/
theorem outer_taylor (γ g1h : ℝ) (hg : g1h ≤ -(γ/8)*γ + (8/2)*(γ/8)^2) : g1h ≤ -γ^2/16 := by
  nlinarith [hg]

/-- Exponent step of Proposition tu:U-B on I^c: (1-δ)^2(ε-η) - ε + η/4 + ω ≤ -η/2 when ε ≥ η, 0≤δ≤1, ω ≤ η/4. -/
theorem propB_step (δ ε η ω : ℝ) (hη : 0 < η) (hε : η ≤ ε) (hδ0 : 0 ≤ δ) (hδ1 : δ ≤ 1) (hω : ω ≤ η/4) :
    (1-δ)^2*(ε-η) - ε + η/4 + ω ≤ -η/2 := by
  have h1 : (1-δ)^2 ≤ 1 := by nlinarith
  have h2 : 0 ≤ ε - η := by linarith
  nlinarith [mul_le_mul_of_nonneg_right h1 h2]

/-- Proposition tu:U-B on I: ω - (ε - η/4) ≤ η/2 when ε ≥ 0, ω ≤ η/4. -/
theorem propB_stepI (ε η ω : ℝ) (hε : 0 ≤ ε) (hω : ω ≤ η/4) : ω - (ε - η/4) ≤ η/2 := by linarith

/-- Main theorem: e^{eta/4} <= e^{1/8} <= 2 for eta <= 1/2. -/
theorem exp_eighth_le_two : Real.exp (1/8) ≤ 2 := by
  by_contra h
  push_neg at h
  have h8 : Real.exp 1 = Real.exp (1/8) ^ 8 := by
    rw [← Real.exp_nat_mul]; norm_num
  have hpow : (2:ℝ)^8 < Real.exp (1/8) ^ 8 := by
    exact pow_lt_pow_left₀ h (by norm_num) (by norm_num)
  have := Real.exp_one_lt_d9
  nlinarith

#print axioms outer_taylor
#print axioms propB_step
#print axioms propB_stepI
#print axioms exp_eighth_le_two
