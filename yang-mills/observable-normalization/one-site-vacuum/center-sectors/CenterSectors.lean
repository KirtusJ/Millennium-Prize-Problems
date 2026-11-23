import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

namespace YangMills.CenterSectors

/-- Pairwise remainder from testing the kinetic equation with w²g. -/
theorem weightedPair (g f w v : ℝ) :
    (w*g-v*f)^2-(g-f)*(w^2*g-v^2*f) = g*f*(w-v)^2 := by ring

theorem absorbExterior (q t inside outside err : ℝ) (h : q*outside ≤ err*(inside+outside))
    (gap : t ≤ q-err) (pos : 0 ≤ outside) : t*outside ≤ err*inside := by
  nlinarith only [h, mul_nonneg (sub_nonneg.mpr gap) pos]

/-- Undoing the positive ground state when a sign is attached to it. -/
theorem signLoss (s t a b : ℝ) (hs : s^2=1) (ht : t^2=1) :
    a*b*(s-t)^2=2*a*b*(1-s*t) := by
  have eq : (s-t)^2 = 2*(1-s*t) := by nlinarith only [hs,ht]
  rw [eq]; ring

/-- Cancellation on a center-stable corner set after minorization. -/
theorem cornerLoss (absMass signedMass : ℝ) (hz : signedMass=0) :
    absMass^2-signedMass^2=absMass^2 := by rw [hz]; ring

/-- Recover a one-step separation from a separation of transfer powers. -/
theorem powerLoss (a b : ℝ) (hb : 0 ≤ b) (hab : b ≤ a) (ha : a ≤ 1) (n : ℕ) :
    a^n-b^n ≤ (n:ℝ)*(a-b) := by
  induction n with
  | zero => simp
  | succ n ih =>
    have cap : b^n ≤ 1 := pow_le_one₀ hb (hab.trans ha)
    have order : 0 ≤ a^n-b^n := sub_nonneg.mpr (pow_le_pow_left₀ hb hab n)
    have first := mul_nonneg (sub_nonneg.mpr ha) order
    have second := mul_nonneg (sub_nonneg.mpr hab) (sub_nonneg.mpr cap)
    rw [pow_succ, pow_succ, Nat.cast_succ]
    nlinarith only [first, second, ih]

end YangMills.CenterSectors

#print axioms YangMills.CenterSectors.weightedPair
#print axioms YangMills.CenterSectors.absorbExterior
#print axioms YangMills.CenterSectors.signLoss
#print axioms YangMills.CenterSectors.cornerLoss
#print axioms YangMills.CenterSectors.powerLoss
