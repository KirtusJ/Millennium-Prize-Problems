import Mathlib

/-! Scalar steps of TUNNEL_LOWER.md (worker o1-lower, T141). -/

/-- (L1) Per-step optimisation: longitudinal Gaussian cost v²/2 plus fibre energy ε
dominates speed times the Agmon density √(2ε). -/
theorem step_cost_ge (ε v : ℝ) (hε : 0 ≤ ε) :
    v * Real.sqrt (2 * ε) ≤ v ^ 2 / 2 + ε := by
  have h2 : Real.sqrt (2 * ε) ^ 2 = 2 * ε := Real.sq_sqrt (by linarith)
  nlinarith [sq_nonneg (v - Real.sqrt (2 * ε))]

/-- (L2) Mass in the well (Lemma M): if λ ≤ M + q (1 - M) with q < 1 then M ≥ (λ - q)/(1 - q). -/
theorem well_mass (lam M q : ℝ) (hq : q < 1) (h : lam ≤ M + q * (1 - M)) :
    (lam - q) / (1 - q) ≤ M := by
  rw [div_le_iff₀ (by linarith)]
  nlinarith

/-- (L3) Shift of the Agmon density: √(2(ε+η)) ≤ √(2ε) + √(2η), so c*(η) ≤ c* + π √(2η). -/
theorem sqrt_shift (ε η : ℝ) (hε : 0 ≤ ε) (hη : 0 ≤ η) :
    Real.sqrt (2 * (ε + η)) ≤ Real.sqrt (2 * ε) + Real.sqrt (2 * η) := by
  have ha : Real.sqrt (2 * ε) ^ 2 = 2 * ε := Real.sq_sqrt (by linarith)
  have hb : Real.sqrt (2 * η) ^ 2 = 2 * η := Real.sq_sqrt (by linarith)
  have hpa : 0 ≤ Real.sqrt (2 * ε) := Real.sqrt_nonneg _
  have hpb : 0 ≤ Real.sqrt (2 * η) := Real.sqrt_nonneg _
  have key : 2 * (ε + η) ≤ (Real.sqrt (2 * ε) + Real.sqrt (2 * η)) ^ 2 := by
    nlinarith [mul_nonneg hpa hpb]
  calc Real.sqrt (2 * (ε + η)) ≤ Real.sqrt ((Real.sqrt (2 * ε) + Real.sqrt (2 * η)) ^ 2) :=
        Real.sqrt_le_sqrt key
    _ = Real.sqrt (2 * ε) + Real.sqrt (2 * η) := Real.sqrt_sq (by positivity)

#print axioms step_cost_ge
#print axioms well_mass
#print axioms sqrt_shift
