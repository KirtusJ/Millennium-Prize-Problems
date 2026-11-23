import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Millennium.G4.CyclicTransfer

theorem compression_error (fine coarse upper lower err : ℝ)
    (hf : fine ≤ upper) (hc : lower ≤ coarse) (he : upper - lower ≤ err) :
    1 - coarse - err ≤ 1 - fine := by linarith

theorem one_mode_moment (single rest : ℝ) (h : 0 ≤ rest) :
    single ≤ single + rest := by linarith

-- NATIVE CHILD 1
theorem sweep_loss (u d : ℝ) (hu : u < 1)
    (h : (1-u)^2 ≤ d*(1-u^2)) :
    1-u ≤ d*(1+u) := by
  by_contra! hn
  have hp := mul_lt_mul_of_pos_left hn (sub_pos.mpr hu)
  nlinarith

theorem cycle_leakage (full projection excursion : ℝ)
    (h : full = projection + excursion) (hp : 0 ≤ excursion) :
    projection ≤ full := by linarith

-- NATIVE CHILD 2
theorem neutral_cubic (s : ℝ) :
    s*(2*s-9)/48 - (s/3)*(3*(2*3-9)/48) = s*(s-3)/24 := by ring

theorem gated_power (x r : ℝ) (hx : 0 ≤ x) (hr : 0 ≤ r) :
    x * (1 - x ^ r) ≤ r * (1 - x) := by
  rcases hx.eq_or_lt with he | hp
  · subst x
    simpa using hr
  have hlog := Real.log_le_sub_one_of_pos (inv_pos.mpr hp)
  rw [Real.log_inv] at hlog
  have hm := mul_le_mul_of_nonneg_left hlog hp.le
  have hlog' : -x * Real.log x ≤ 1 - x := by
    rw [mul_sub, mul_inv_cancel₀ hp.ne', mul_one] at hm
    linarith
  have hpow : 1 - x ^ r ≤ -(Real.log x * r) := by
    rw [Real.rpow_def_of_pos hp]
    linarith [Real.add_one_le_exp (Real.log x * r)]
  have h1 := mul_le_mul_of_nonneg_left hpow hp.le
  have h2 := mul_le_mul_of_nonneg_right hlog' hr
  nlinarith

#print axioms compression_error
#print axioms one_mode_moment
#print axioms sweep_loss
#print axioms cycle_leakage
#print axioms neutral_cubic
#print axioms gated_power
end Millennium.G4.CyclicTransfer
