import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

noncomputable section
namespace Millennium.G4.Blocking

theorem doob_channel (r s u c : ℝ) (hs : s ≠ 1)
    (hc : c = (1 + s) / (2 * (1 - s))) :
    (r + u) / 2 + c * (u - r) = (u - s * r) / (1 - s) := by
  subst c
  have h : 1 - s ≠ 0 := sub_ne_zero.mpr (Ne.symm hs)
  field_simp [h]
  ring

-- NATIVE CHILD 1
def channelSum (r u : ℝ) : ℕ → ℝ
  | 0 => 0
  | n+1 => u * channelSum r u n + r^n

theorem channel_sum (r u : ℝ) (n : ℕ) :
    (r-u) * channelSum r u n = r^n-u^n := by
  induction n with
  | zero => simp [channelSum]
  | succ n ih =>
    rw [channelSum, pow_succ r n, pow_succ u n]
    calc
      _ = u * ((r-u) * channelSum r u n) + (r-u)*r^n := by ring
      _ = _ := by rw [ih]; ring

-- NATIVE CHILD 2
theorem detour_step (r q : ℝ) (hq : q^4 ≠ 1) :
    (r*q^2-q^4*r)/(4*(1-q^4)) = r*q^2/(4*(1+q^2)) := by
  have h₁ := sub_ne_zero.mpr (Ne.symm hq)
  have h₂ : 1+q^2 ≠ 0 := ne_of_gt (by positivity)
  field_simp [h₁, h₂]
  ring

theorem detour_positive (r q : ℝ) (hr : 0 < r) (hq : 0 < q) :
    0 < r*q^2/(4*(1+q^2)) := by positivity

#print axioms doob_channel
#print axioms channel_sum
#print axioms detour_step
#print axioms detour_positive

end Millennium.G4.Blocking
